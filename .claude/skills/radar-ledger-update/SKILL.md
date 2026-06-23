---
name: radar-ledger-update
description: |
  Safely update TRENDS.md (the AI Radar ledger): append evidence, move stages, manage observation_queue, source_rotation and strategy_notes without breaking the file contract. Use every time TRENDS.md is edited, before committing radar updates, and when promoting or archiving trends.
---

# Update the ledger safely

`TRENDS.md` is the single source of truth and later sessions parse it. The
structure is a contract.

## File contract (do not change)

- Header: `# Trend ledger — AI Radar`, then `Last updated: YYYY-MM-DD`, then the
  stage legend.
- Sections, in this order: `## Active trends`, `## observation_queue`,
  `## source_rotation`, `## strategy_notes`, `## study_shelf`, `## calibration`.
- `## source_rotation` and `## calibration` are POINTER stubs only: their real
  append-only content lives in `logs/source_rotation.md` and `logs/calibration.md`
  respectively. Keep the two stub headers (the section order is the contract) but
  NEVER inline log lines back into TRENDS.md — appends go to the `logs/` files.
- Trend block: `### [id: slug-NNN] Title` with fields `alias`, optional
  `pinned: true`, `stage`, `confidence`, `first_observed`, `last_evidence`,
  `evidence:` (list), `notes:`.
- Evidence line: `- YYYY-MM-DD — URL — one line of context`.

## Rules

- Match findings to existing trends via id and `alias` before creating a new
  trend. New trends take the next free NNN and start at `seed` or `emerging`.
- ROUTE a captured primary, don't default to "queue it": (a) if it lands on an
  EXISTING trend's axis, append it as EVIDENCE there — a single primary suffices
  for an existing trend; the ≥3-source bar is only for CREATING a trend; (b) if
  the queue now holds ≥3 independent groups on one untracked sub-theme, promote
  that cluster to a `seed` trend; (c) else it stays a queue item. Leaving an
  on-axis primary in the queue (hoarding evidence) or a named primary in report
  prose only is a routing failure.
- Max 10 evidence items per trend — drop the oldest. Keep `last_evidence` equal
  to the newest evidence date.
- Stage moves: at most ONE stage up per trend per day, only on new independent
  evidence, justified in `notes`. Demotions are always allowed. 21+ days without
  evidence → `dormant`; at 45+ days the weekly pass moves the entry to
  `ARCHIVE.md` as a one-line post-mortem.
- Pinned trends (`pinned: true`): NEVER auto-archived, no matter how long
  without evidence — they are the curator's standing-watch axes. They still
  follow the normal stage rules, INCLUDING going `dormant` when quiet (the
  ledger stays truthful about activity); they simply never leave the board.
  Only the curator adds/removes a pin (or the agent proposes it via amendment).
- `observation_queue` items are dated and marked "unverified" unless opened. It
  is a WORKING SET (signals pending verification), not a knowledge store — keep it
  bounded to a soft cap of ~25 live items by a CAP-DRIVEN burndown that runs every
  session, including quiet/no-evidence passes: while the queue is OVER the cap,
  resolve the oldest items toward the cap that run regardless of what the scan
  found; at/under the cap it stops on its own (resolve only the 1–2 oldest if
  stale). This is owed every run, never deferred to the weekly — a no-evidence
  pass is not a no-op for the queue. Items leave ONLY by resolution: promoted to a
  trend (the signal is captured there) or dropped with a one-line reason in the
  day's/week's report (write-once, permanent). NEVER silently delete — because
  every removal is either a promotion or a recorded drop, shrinking the queue
  loses no knowledge. Re-date an item only if it is genuinely still worth watching.
- Append one dated line per session to `logs/source_rotation.md` (the coverage
  log; not the TRENDS.md stub). Append dated corrections to the `strategy_notes`
  section of TRENDS.md; never delete curator entries.
- `study_shelf`: newest first, format `date — [name](url) — one line of why`;
  single-artifact items allowed (the trend bar does not apply), opened primary
  sources only.
- `calibration` (now `logs/calibration.md`) is append-only and written by weekly
  runs only (see the `radar-self-eval` skill); daily runs never touch it.
- Update the `Last updated` line. Keep everything in English.

## Validate before commit

```bash
grep -n '^## ' TRENDS.md
# expected, in order: Active trends, observation_queue, source_rotation, strategy_notes, study_shelf, calibration
grep -c '^### \[id: ' TRENDS.md          # trend count matches expectations
grep -nE '^  - [0-9]{4}-[0-9]{2}-[0-9]{2} — ' TRENDS.md | head -3   # evidence format
grep -n '^Last updated:' TRENDS.md       # date is today
# the two externalized logs must exist and only grow (append-only):
test -f logs/source_rotation.md && tail -1 logs/source_rotation.md | head -c 80
test -f logs/calibration.md && tail -1 logs/calibration.md | head -c 80
# TRENDS.md must NOT have regrown a log body (the stubs stay one-line pointers):
awk '/^## source_rotation/{n=0} /^## strategy_notes/{print "rotation stub lines:", n} {n++}' TRENDS.md
```

If a check fails, fix the file before committing. Commit and push per the
conventions in AGENTS.md.
