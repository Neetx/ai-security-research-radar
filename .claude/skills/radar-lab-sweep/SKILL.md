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
