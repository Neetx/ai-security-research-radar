---
name: radar-render-dashboard
description: |
  Regenerate README.md, the repo's landing page and only output surface: badges, a 3-4 bullet "since last scan" digest with inline links, a clickable trend table, the study shelf, and an output map. Use after every change to TRENDS.md, in the same commit. README.md is fully derived and never edited by hand: if it disagrees with TRENDS.md, TRENDS.md wins — regenerate. On daily runs it also overwrites SUMMARY.md — the run's results in at most 6 one-line linked bullets, no process detail.
---

# Render the dashboard (README.md) and the daily summary (SUMMARY.md)

`README.md` is what GitHub renders on the repo home page — it IS the radar's
output surface. It is fully derived from `TRENDS.md`; regenerate it from scratch
on every run, never patch it. Design goal: one screen, everything clickable.

## Layout (exactly these blocks, in this order)

1. **Title** — `# AI Radar`.
2. **Badge row** — four shields.io static badges, style `flat-square`:
   `trends-<total>-3266ad`, `accelerating-<n>-e8590c`,
   `watchlist-<queue count>-6c757d`, `updated-<YYYY--MM--DD>-2f9e44`
   (escape `-` in dates as `--`).
3. **Intro line** — one sentence: what the radar tracks, for whom, and that the
   page is generated from [TRENDS.md](TRENDS.md).
4. **Digest** — `**Since last scan (YYYY-MM-DD):**` + 3–4 bullets MAX, in
   priority order: stage moves, queue promotions/drops, strongest new evidence.
   Every bullet must contain at least one link (trend anchor or evidence URL).
   If nothing changed: one bullet, "Quiet scan — no ledger changes."
   NAME every trend by its LABEL, never by a bare number: write the readable slug or the
   short label (`agentic-attack-surface-001`, "Agent-stack attacks"). `001`, `Trend 008`
   and every other bare-number reference are FORBIDDEN in prose — the number belongs
   inside the anchor/URL, not in the text a human reads. An id is self-describing only to
   someone who already has the ledger open, and this page is read by someone who does not.
5. **Pinned topics (⭐)** — `## ⭐ Pinned topics` then a table of ONLY the trends
   with `pinned: true`, same columns as the main table. These are the curator's
   standing-watch axes; they appear here AND in the main table (where their
   trend label is prefixed with ⭐). Sort by `last_evidence` descending.
6. **Trends section** — stage strip on one line
   (`🌱 n · 📈 n · 🚀 n · 🌊 n · 🏔 n · 📉 n · 💤 n`), then ONE table
   `| trend | stage | latest signal |` with ALL trends (pinned included, prefix
   their label with ⭐), sorted accelerating → emerging → seed → mainstreaming →
   saturated → declining → dormant, then by `last_evidence` descending:
   - **trend** = short label (≤5 words; reuse previous README labels for
     stability) linking to the trend's anchor in TRENDS.md (see anchor rule);
     prefix with `⭐ ` when `pinned: true`.
   - **stage** = emoji + word.
   - **latest signal** = the `last_evidence` date linking to the evidence URL
     whose date equals `last_evidence` (first match in list order); if none
     matches, link the top evidence item.
7. **🛠️ Tools & releases** — `## 🛠️ Tools & releases` — a FIRST-CLASS output block (public,
   usable offensive tools ARE a primary deliverable): up to ~8 bullets of the newest / newly
   -updated on-axis GitHub tools & tool releases from the watched list AND the tool-discovery lane
   — `[owner/repo](github-url) — one line (what it does + new version/date if a release)`. ONLY
   tools with a REAL PUBLIC repo you could clone today (verified per SOURCES → tool-discovery) —
   a paper that merely CLAIMS a tool with no public/populated repo does NOT go here (it stays in
   Worth studying as a paper). Draw from Discovered-source candidates promoted this cycle +
   `study_shelf`/`observation_queue` tool items. If genuinely none: one line "No new tools this
   scan." Never leave it out — an empty-but-present block tells the reader the lane ran.
8. **Worth studying** — the `study_shelf` section of TRENDS.md (papers/writeups; tools go in the
   Tools block above), newest first, up to 12 bullets: `[name](url) — one line of why`.
9. **Community pulse** — `## Community pulse` (Phase 3): up to 5 bullets distilled
   from the latest `radar-pulse` intake — non-evidence, link-only, NEVER naming
   individuals (link the thread/profile, summarise). If no pulse data yet, one
   line: "No community pulse sampled yet." This section is clearly marked as
   unverified sentiment, separate from the verified trend table.
10. **Output map** — one line of links: TRENDS.md, watchlist (queue count) →
   `TRENDS.md#observation_queue`, `reports/` + newest daily, newest weekly
   ("weekly: none yet" if absent), AGENTS.md, SOURCES.md.

## SUMMARY.md — the daily summary page (daily runs only)

A second derived page, for a reader who wants the run's RESULTS in ten seconds. Write it
on EVERY daily run, in the same commit as README.md, OVERWRITING the previous version
(history lives in `reports/`). Weekly runs do not touch it. It states the same facts as
today's report and README digest — no new claims; every link must already be in TRENDS.md
or today's report.

Exact shape — nothing above, between or below these lines:

```
# AI Security Radar — YYYY-MM-DD

- **New trend** · [<trend label>](TRENDS.md#<anchor>) — <what it is>.
- **Stage** · [<trend label>](TRENDS.md#<anchor>) <old> → <new> — [<source title>](<url>): <what it shows>.
- **New** · [<source title>](<url>) — <what it shows> (→ [<trend label>](TRENDS.md#<anchor>)).
- **Study pick** · [<source title>](<url>) — <why it is worth reading>.

[Full report](reports/YYYY-MM-DD.md) · [Dashboard](README.md)
```

Rules:
- At most 6 bullets, most significant first. Only the four kinds above; any may be absent,
  any may repeat. One line each; the text after the dash is ≤ 15 words (the `(→ trend)`
  link not counted).
- RESULTS ONLY — what was found, never how it was found or what the radar did with it.
  Nothing about the radar's own machinery: no sweeps, lanes, passes, sources checked or
  degraded, heals, queue/watchlist counts or moves, cap swaps, capture-leak, diffs,
  convergence flags, "Nth independent group" counts, unchanged repos, amendments, dormancy
  rescues, backfills, next steps.
- Verified results only: new trends, stage moves, new evidence, study picks. Unverified queue
  signals are not results — leave them out. Do not list the same item twice (a study pick
  already listed as **New** is not repeated).
- No narrative: no evaluative adjectives (striking, genuine, major, finally, notable, real),
  no scene-setting, no "a sign that…" interpretation. State the fact. A result that is a
  claim not yet vetted keeps a one-word tag at the end: `(claim)` or `(preprint)`.
- Trends by their README short label (never a bare id or number); sources by their own
  title, cut at its colon when the title is long.
- A run with no ledger change writes exactly one bullet: `- Nothing new in this run.`

Check before commit (a hit is allowed only inside a source's own title or a trend label):

```bash
test "$(grep -c '^- ' SUMMARY.md)" -le 6 || echo "TOO MANY BULLETS"
grep '^- ' SUMMARY.md | grep -v '](' | grep -v 'Nothing new in this run' && echo "BULLET WITHOUT LINK"
grep -q "^# .* — $(date +%F)$" SUMMARY.md || echo "WRONG DATE"
grep -niwE 'sweeps?|swept|lanes?|pass(es)?|queued?|watchlist|cap-swaps?|capture-leak|degraded|heal(ed)?|sitemap|diff|coverage|convergence|repo-watch|amendments?|dormancy|backfill|triage|flagged' SUMMARY.md && echo "PROCESS WORDS — rewrite"
grep -niE '[0-9]+(st|nd|rd|th) (independent )?(group|org|organi[sz]ation)' SUMMARY.md && echo "INTERNAL COUNT — drop it"
```

## Anchor rule (GitHub heading slugs)

For a heading `### [id: slug-NNN] Title`, the anchor is: lowercase the whole
heading text, delete every character that is not a letter, digit, space or
hyphen (no replacement — `Prefill/decode` → `prefilldecode`), then replace
spaces with hyphens. Example:
`### [id: pd-disagg-002] Prefill/decode disaggregation as the standard LLM serving architecture`
→ `TRENDS.md#id-pd-disagg-002-prefilldecode-disaggregation-as-the-standard-llm-serving-architecture`.
Anchors are recomputed at every render, so title edits stay in sync.

## Checks before commit

- Badge counts = stage-strip counts = table row count = number of `### [id:`
  blocks in TRENDS.md.
- Every table date equals that trend's `last_evidence` exactly; every row has
  two working relative/absolute links.
- No Mermaid, no images besides the badges, no sections beyond the blocks above.
- Pinned-topics table contains exactly the `pinned: true` trends; every pinned
  trend is ⭐-prefixed in the main table too.
- Community-pulse items are link-only and name no individuals.
- Commit README.md together with the TRENDS.md change that triggered it.
