---
name: radar-lab-sweep
description: |
  Sweep the primary security feeds — vendor/lab red-team & security blogs, research venues, and advisory feeds — on EVERY daily run (not rotated) so no attack-technique, red-team tool release, or disclosure is missed. Prefer RSS/Atom over HTML to survive JavaScript-rendered indexes. Use at the start of every daily scan, before the rotating exploration slot.
---

# Primary-feed sweep — every run, no rotation

A real security radar checks its primary feeds every single day. This sweep is
mandatory on every daily run and is separate from (and in addition to) the
rotating exploration slot. Vendor/lab security blogs, research venues, repos and
advisories are primary sources under the Hard rules, so anything found here is
citable evidence (filtered for OFFENSIVE relevance — attack techniques, red-team
tooling, exploitation research).

The CHECK (fetch every feed and see what is new since the last scan) is owed on
EVERY run, even one minute after another pass — it is cheap triage and may never
be skipped as a "light pass". Only the EXTRACT (open a new post in full) is
conditional on a genuinely new entry.

## Method (efficient)

1. For each source in the list, fetch its FEED first (RSS/Atom), not the HTML
   index — feeds are immune to the JS-rendering that hid `lmsys.org/blog`. To
   find a feed: try `/rss.xml`, `/feed`, `/atom.xml`, `/index.xml`, or read the
   page's `<link rel="alternate" type="application/rss+xml">`.
2. Open only entries dated AFTER the last daily scan (check the previous date in
   `logs/source_rotation.md`). Skip everything older — this keeps the sweep cheap.
3. Apply the evidence rules: open the actual post, cite its own date, match to a
   trend or log to `observation_queue`/`study_shelf` as appropriate.
4. Log the sweep in `logs/source_rotation.md` every run, even when nothing is new
   ("lab-sweep: no new posts").

## Off-index publications — the sitemap / index diff (EVERY run, after the feeds)

A feed or index page lists only what the publisher put THERE. Organizations also publish
on other paths and subdomains (a new research subdomain, top-level report slugs, a section
the feed does not carry), and some sites expose no usable feed at all — such posts are
invisible to the feed step no matter how faithfully it runs. So after the feeds, run the
bundled diff over EVERY host in the primary-source lists, in ONE call:

    python3 .claude/skills/radar-lab-sweep/sitemap_diff.py --write --since <last scan date> <host> [<host> ...]

It reads each host's sitemap (robots.txt `Sitemap:` lines; indexes and .gz followed) and
prints only the URLs that were NOT in that host's snapshot last run (`state/sitemaps/`,
grow-only, committed with the run). A `NEW` line is a new page wherever it was published:
triage it exactly like a feed entry (its own date, relevance; open only on-scope ones).
`BASELINE` lines appear the first time a host is diffed — not proven new; triage each by
the post's own date. On a host's FIRST diff pass `--since` 30 days back (not the last scan date): the
baseline is the one chance to surface recent off-index posts the feed step already missed —
once a URL is in the snapshot it can never come back as `NEW`. For a site whose sitemap lists only section pages, diff the section's
index instead: `index:<index url>` (the article links in its raw HTML — most JS-rendered
blogs still server-render the links). Record the working target next to each source in
SOURCES.md (`diff: <host>` or `diff: index:<url>`); a host whose sitemap is blocked or empty
and has no working index target is `degraded: no-diff` → heal it (`radar-source-heal`).
Log one line in `logs/source_rotation.md`:
`sitemap-diff: <n> targets, <m> NEW (<k> routed), degraded: <list or none>`.

VENUE MOVES. When ANY lane surfaces a page on a host or path that SOURCES.md does not list,
but that belongs to an organization already in the primary lists, that is the organization
publishing somewhere new — not a new source awaiting the weekly's verification. Add the new
host as a diff target (and its feed, if it has one) of that same source IN THIS RUN, and log
it. Apply the same test to every entry already sitting in the discovered-candidates list:
a staged candidate owned by an already-tracked organization is promoted now, not left staged.

## Source list

The lists live in `SOURCES.md` → "Primary feeds — vendor/lab security blogs &
advisories" and "Research venues — arXiv & security conferences" (agent-owned: mark
feeds `DEAD` if they stop resolving, add new sources as they appear). Iterate EVERY
entry; prefer the feed URL, fall back to the HTML index via `tvly extract` only if
no feed exists. Log each source opened or `degraded: <reason>`.

## Notes

- The sweep complements, never replaces, the rotating exploration slot.
- Vendor/lab security blogs and cons often disclose attack techniques and red-team
  tool releases that never become arXiv papers — those are exactly what this sweep
  exists to catch. Filter for offensive relevance; skip product/marketing.
- Keep this list in sync with the `SOURCES.md` registry.
