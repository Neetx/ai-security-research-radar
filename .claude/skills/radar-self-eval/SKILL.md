---
name: radar-self-eval
description: |
  Compute the radar's self-calibration: weekly funnel metrics (queue dynamics, exploration compliance, off-axis rate), a monthly hit/miss retrospective against what actually became big, and up to 3 curator proposals. Use during every weekly recalibration, after the source-strategy review; results go into the append-only `logs/calibration.md` and into the weekly report.
---

# Self-evaluation

The radar must measure whether it is winning, not assume it. Three parts:
metrics (every week), retrospective (monthly), curator proposals (every week).

## 1. Weekly metrics

Compute from the week's daily reports (primary source — they list ledger
changes) and, where needed, `git log -p -- TRENDS.md` since the previous weekly
commit:

- **queue funnel**: items added / promoted to trend / dropped / older than 14
  days and still unverified (stale)
- **ledger**: evidence items added, stage moves (up and down)
- **exploration compliance**: daily runs whose `logs/source_rotation.md` line
  contains a venue-exploration entry ÷ daily runs executed
- **off-axis rate**: share of new queue items that do NOT match any axis in
  `strategy_notes` (judgment call — name them)
- **discovery lag**: for each evidence item added this week, the days between
  its evidence-line date and the date it entered the ledger (commit date via
  `git log -p -- TRENDS.md`, or the daily reports). Report the median, split by
  channel — exploration finds vs queue promotions (backfill) — plus the
  backfill share of all new evidence. This is the daily-ness KPI.
- **coverage** (the self-check that auto-detects the alphamatch failure class):
  for each "swept every run" list in SOURCES.md (lab blogs, YouTube curators,
  pointer/digest blogs, discovery venues), diff the list against the week's
  `logs/source_rotation.md` lines and classify every listed source as `opened`,
  `degraded`, or **MISSING** (in SOURCES.md but never in any log line this week).
  MISSING = a coverage lie — NAME them. A source MISSING or `degraded` for the
  whole week is a heal-or-REMOVE candidate (see Amendments): the registry must be
  honest about what it actually sweeps.
- **routing-leak**: queue items tagged with (or clearly on) an EXISTING trend's
  axis yet absent from that trend's evidence — on-axis primaries hoarded in the
  queue instead of routed to evidence. Count and name them; each is a routing
  miss to correct this week.
- **source-discovery**: from SOURCES.md → "Discovered-source candidates" and the
  week's reports — candidates STAGED this week / PROMOTED to a swept source /
  PRUNED, plus discovery-latency = runs (or days) between an org's FIRST
  appearance in the staging tally and its promotion. The tool-author/vendor analog
  of routing-leak: a recurring on-axis org that stays un-promoted (≥2 weeks in the
  tally) is a coverage leak — NAME it and promote-or-drop it now. Zero candidates
  staged for two weeks while new evidence keeps arriving from the SAME few orgs is
  itself a signal the capture-the-source step isn't firing.

Append ONE dated line to `logs/calibration.md` (the externalized self-eval log; the `## calibration` section of TRENDS.md is now only a pointer):
`- YYYY-MM-DD — W<nn>: queue +a/→p/−d/stale s · evidence +e · moves m · exploration c/r · off-axis o/a · lag expl Xd / backfill Yd (Z%) · coverage <opened>/<listed> (miss <n>, degr <d>) · routing-leak <n> · src-disc <staged>/<promoted> (lat L)`
and include the same numbers, readable, in the weekly report.

Interpretation thresholds (act, don't just log):
- exploration compliance < 100% → call it out; two weeks running → propose a
  daily prompt/skill refinement.
- stale > half the queue → scanning breadth exceeds verification capacity:
  propose narrowing or a verification-only day.
- off-axis = 0 for two consecutive weeks → anchoring warning, even if the
  tunnel-vision check passed.
- exploration-channel median lag > 7 days → the venues are stale: rotate them.
- backfill share not shrinking for two consecutive weeks (once the bootstrap
  queue is cleared) → the radar is doing literature review, not daily
  detection: propose rebalancing scan time toward exploration.

## 2. Monthly retrospective (first weekly run of the month: `date +%d` ≤ 7)

Goal: ground truth — did the radar see early what later became big?

1. Pick 2–3 items that clearly became big in the past month by BROWSING venues
   (open the pages — evidence rules apply): HF papers trending, two major lab
   blog indexes, one arXiv listing. Pick what is everywhere, not what is
   interesting.
2. For each, find the radar's earliest mention:
   `git log -S"<term>" --oneline -- TRENDS.md` plus the queue and reports.
3. Classify: **HIT-early** (tracked ≥7 days before it was everywhere),
   **HIT-late**, **MISS**.
4. For every MISS: add it to `observation_queue` now, and name the venue or
   axis that would have caught it — feed that into the proposals.

Log in `logs/calibration.md`:
`- YYYY-MM-DD — retro M<mm>: <item> — HIT-early|HIT-late|MISS (first seen <date or never>), …`

## 3. Amendments (proposed → cooling period → applied)

The radar runs unattended and may change its own operating instructions —
under the autonomy contract in AGENTS.md. Every week, up to 3 proposed
amendments: routine edits (exact replacement text), axis drops/merges/
supersessions, exploration-budget changes. Each must cite the metric or
retrospective result that motivates it.

The new coverage/routing metrics feed amendments directly (this is how the
radar self-corrects the failure classes the curator used to catch by hand):
- a source **MISSING or `degraded` all week** → first a `radar-source-heal`
  attempt; if it was already healed and still fails, a **heal-or-REMOVE**
  amendment (remove it from the SOURCES.md "swept every run" list, or escalate
  the secret/allowlist it needs) — a first-class amendment, because a listed-but-
  unswept source is a coverage lie.
- a non-zero **routing-leak** → not an amendment but a this-week FIX: route the
  hoarded on-axis queue items to their trend's evidence now; if it recurs, amend
  the routing instruction.

Lifecycle:
- **Week N**: propose — log in `calibration` and the weekly report.
- **Week N+1**: apply IF the motivating signal persists AND no dated curator
  veto appeared in `strategy_notes` (silence is consent). One dedicated commit
  per amendment. If the signal vanished, drop the proposal and say so.
- **After applying**: if calibration metrics worsen for two consecutive weeks,
  `git revert` the amendment and log the rollback.

Scope-axis changes are recorded as "radar-adopted" dated entries in
`strategy_notes`, explicitly naming what they supersede. Curator entries are
never deleted or edited — vetoes and mission input belong to the curator alone.
The immutable sections listed in AGENTS.md are out of bounds: an amendment
touching them is invalid.

## Boundaries

- Evidence rules apply to the retrospective: cite only opened pages.
- `logs/calibration.md` is append-only: never edit or delete existing lines.
- If a metric shows the same procedural failure twice, trigger a skill
  refinement per the maintenance policy in AGENTS.md (dedicated commit,
  explained in the report).
