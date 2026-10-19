#!/usr/bin/env python3
"""sitemap_diff — find pages a source published since the last run, wherever they live.

Why: a feed or index page only shows what the publisher put THERE. A post on another path
or subdomain, or on a blog whose feed is empty, is invisible to a feed sweep — and a topic
SEARCH is not a substitute (it does not guarantee recency, so "nothing fresh" from a search
is not evidence of silence). This script diffs the set of page URLs a site exposes against
the set it exposed last time, so a NEW URL is new no matter which path it was published on.

Usage (run from the repo root):
  python3 .claude/skills/<sweep-skill>/sitemap_diff.py [--write] [--since YYYY-MM-DD]
          [--include REGEX] TARGET [TARGET ...]

TARGET:
  www.example.com | https://www.example.com/sitemap.xml   → SITEMAP mode (robots.txt
      `Sitemap:` lines, else /sitemap.xml; sitemap indexes and .gz are followed)
  index:https://www.example.com/blog/topics/x               → INDEX mode: the article links
      on that page (raw HTML, no JS needed) under the page's own path

Output: `NEW <lastmod|-> <url>` per new page, then a `#` status line per target.
  - With a snapshot (state/sitemaps/<key>.txt): NEW = URL absent from the snapshot. lastmod
    is ignored for the decision (many sites bulk-rewrite it), shown only as a hint.
  - First run for a target (no snapshot): `BASELINE` lines — pages with lastmod in the last
    30 days (or since --since, if older)
    (index mode: links not already cited anywhere in the repo), capped. NOT proven new:
    triage each by the post's own date, exactly like a feed entry.
  - `--write` merges what was seen into the snapshot (grow-only). The daily passes --write;
    a dry check omits it.
Status `blocked:<code>`, `not-xml` or `no-pages` means use the source's other access method.
Stdlib only.
"""
import argparse, datetime, gzip, hashlib, io, pathlib, re, urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/128 Safari/537.36"
SKIP = re.compile(r"/(tag|tags|category|categories|author|authors|page|search|careers|jobs|"
                  r"legal|privacy|terms|cookies?)(/|$)", re.I)
MAX_CHILD, CAP, BASELINE_DAYS = 40, 25, 30
STATE = pathlib.Path("state/sitemaps")

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    if data[:2] == b"\x1f\x8b":
        data = gzip.GzipFile(fileobj=io.BytesIO(data)).read()
    return data

def parse_xml(data):
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return None, []
    out = []
    for node in root:
        loc = lm = None
        for c in node:
            n = c.tag.split("}")[-1]
            if n == "loc" and c.text: loc = c.text.strip()
            elif n == "lastmod" and c.text: lm = c.text.strip()[:10]
        if loc: out.append((loc, lm))
    return root.tag.split("}")[-1], out

def sitemap_pages(target, since):
    if re.search(r"sitemap[^/]*\.xml(\.gz)?$", target):
        roots = [target]
    else:
        host = urllib.parse.urlparse(target if "://" in target else "https://" + target).netloc
        roots = []
        try:
            for line in fetch(f"https://{host}/robots.txt").decode("utf-8", "ignore").splitlines():
                if line.lower().startswith("sitemap:"):
                    roots.append(urllib.parse.urljoin(f"https://{host}/", line.split(":", 1)[1].strip()))
        except Exception:
            pass
        roots = roots or [f"https://{host}/sitemap.xml"]
    pages, problems, queue, n = {}, [], list(roots), 0
    while queue and n < MAX_CHILD:
        url = queue.pop(0); n += 1
        try:
            kind, items = parse_xml(fetch(url))
            items = [(urllib.parse.urljoin(url, u), m) for u, m in items]   # relative <loc>s
        except urllib.error.HTTPError as e:
            problems.append(f"blocked:{e.code}"); continue
        except Exception as e:
            problems.append(f"error:{type(e).__name__}"); continue
        if kind == "sitemapindex":   # only descend into children that may hold recent pages
            queue += [u for u, m in items if not since or not m or m >= since]
        elif kind == "urlset":
            pages.update(items)
        else:
            problems.append("not-xml")
    return pages, problems

def index_pages(url):
    p = urllib.parse.urlparse(url)
    prefix = p.path.rstrip("/") + "/"
    try:
        html = fetch(url).decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        return {}, [f"blocked:{e.code}"]
    except Exception as e:
        return {}, [f"error:{type(e).__name__}"]
    links = set()
    for href in re.findall(r'href=["\']([^"\'#?]+)', html):
        u = urllib.parse.urljoin(url, href)
        q = urllib.parse.urlparse(u)
        if q.netloc == p.netloc and q.path.startswith(prefix) and len(q.path) > len(prefix) + 3:
            links.add(f"{q.scheme}://{q.netloc}{q.path.rstrip('/')}")
    return {u: None for u in links}, ([] if links else ["no-links"])

def repo_cited():
    s = set()
    for p in [pathlib.Path("TRENDS.md"), *pathlib.Path("logs").glob("*.md"),
              *pathlib.Path("reports").glob("**/*.md")]:
        try:
            s.update(u.rstrip(").,;`>'\"/") for u in
                     re.findall(r"https?://[^\s)`>\"'\]]+", p.read_text(errors="ignore")))
        except Exception:
            pass
    return s

def key_for(target):
    base = re.sub(r"[^a-z0-9]+", "-", target.lower().split("://")[-1]).strip("-")
    return base[:60] + "-" + hashlib.sha1(target.encode()).hexdigest()[:6]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default=None, help="baseline cutoff + sitemap-index pruning")
    ap.add_argument("--include", default=None, help="regex a page URL must match")
    ap.add_argument("--write", action="store_true", help="merge seen URLs into the snapshot")
    ap.add_argument("targets", nargs="+")
    a = ap.parse_args()
    cited = None
    for t in a.targets:
        snap = STATE / (key_for(t) + ".txt")
        known = set(snap.read_text().split()) if snap.exists() else None
        # first diff of a host: widen the window, so recent off-index posts surface once
        since = a.since
        if known is None:
            wide = (datetime.date.today() - datetime.timedelta(days=BASELINE_DAYS)).isoformat()
            since = min(since, wide) if since else wide
        if t.startswith("index:"):
            pages, problems = index_pages(t[6:])
        else:
            pages, problems = sitemap_pages(t, since)
        pages = {u.rstrip("/"): m for u, m in pages.items()
                 if not SKIP.search(urllib.parse.urlparse(u).path)
                 and (not a.include or re.search(a.include, u))}
        # drop listing pages: the site root, and any URL that is a path prefix of another
        pages = {u: m for u, m in pages.items() if urllib.parse.urlparse(u).path not in ("", "/")
                 and not any(v.startswith(u + "/") for v in pages)}
        if known is not None:
            new = [(pages[u] or "-", u) for u in pages if u.rstrip("/") not in known]
            mode = "diff"
        else:
            cited = cited if cited is not None else repo_cited()
            new = [(m or "-", u) for u, m in pages.items() if u.rstrip("/") not in cited
                   and ((m and m >= since) or
                        (not m and t.startswith("index:")))]
            mode = "baseline"
        new.sort(reverse=True)
        tag = "NEW" if mode == "diff" else "BASELINE"
        for m, u in new[:CAP]:
            print(f"{tag} {m} {u}")
        if a.write and pages:
            STATE.mkdir(parents=True, exist_ok=True)
            snap.write_text("\n".join(sorted((known or set()) | {u.rstrip("/") for u in pages})) + "\n")
        more = f" (first {CAP} shown)" if len(new) > CAP else ""
        state = "ok" if pages else ("no-pages" + (": " + ", ".join(sorted(set(problems))) if problems else ""))
        print(f"# {t}: {state} [{mode}] — {len(pages)} pages, {len(new)} new{more}"
              + (" — snapshot updated" if a.write and pages else ""))

if __name__ == "__main__":
    main()
