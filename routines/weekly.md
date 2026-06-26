# AI Security Radar — Weekly recalibration

You are the weekly operator of the AI Security Radar repository. Work in English.
Compute the ISO week as YYYY-Wnn (`date +%G-W%V`).

## 1. Load state
Recover orphaned state first (see daily.md). Then read `TRENDS.md`, `ARCHIVE.md`, the
daily reports of the past 7 days in `reports/`, and the previous weekly report if present.

## 2. Recalibrate every trend
Judge each trend's velocity over the last 2–3 weeks (count of new independent evidence,
breadth of orgs, presence in tools/standards).
- **Promote** (seed → emerging → accelerating → mainstreaming) only on sustained
  multi-org evidence; one stage max per week; justify in `notes`.
- **Demote** honestly when evidence thinned.
- **Dormancy**: 21+ days without evidence → `dormant`. If `last_evidence` is 45+ days old,
  move the entry to `ARCHIVE.md` as a one-line post-mortem.
- **Merge** overlapping trends (keep the older id, union aliases, keep the 10 strongest
  evidence items, note the merge).
- **Confidence**: raise to `high` when EITHER ≥2 INDEPENDENT authoritative primary sources
  (different orgs/groups) corroborate the trend on concrete artifacts, OR after sustained
  multi-week confirmation — whichever comes first; otherwise hold at `medium`. Lower when
  evidence thins or is mostly vendor-reported.
- After recalibration, regenerate `README.md` (`radar-render-dashboard`).

## 3. Clean the observation queue
Items older than 14 days — verify now and either promote, drop (one-line reason in the
report), or re-date stating what is still missing. HARD CAP ~25 live items: resolve the
oldest over cap regardless of age. Never silently delete. Also curate `study_shelf`
(merge duplicates, prune picks older than 30 days, preserve the rest in their day's report).

## 4. Source strategy review
**Coverage check (first-class — the registry must be honest):** diff every "swept every
run" list in `SOURCES.md` against the week's `logs/source_rotation.md` — every listed
source must appear as `opened` or `degraded`. Any source MISSING all week is a coverage
lie: heal it now (`radar-source-heal`), or if already healed and still un-sweepable,
propose heal-or-REMOVE (don't list what you won't sweep).
Then compare the coverage log against the ledger: which sources produced evidence, which
produced nothing repeatedly; are the scope priorities in `strategy_notes` actually covered?
Tunnel-vision check: if ALL of this week's new evidence landed on pre-existing trends,
record an anchoring warning in `strategy_notes` and redirect next week's exploration.
Grow the curator/source lists (add recurring high-hit sources; drop noisy/dead ones).
**Source discovery (drain the auto-staged candidates — the tool-author/vendor analog of curator
scouting):** review SOURCES.md → "Discovered-source candidates", the tally the daily fills
whenever a lane names an on-axis primary from an org not yet swept. For each org/domain at or
above the promotion bar (≥2 on-axis primary artifacts, OR recurrence across ≥2 runs), VERIFY by
OPENING its feed / repo / channel (Tavily/curl — never from memory, reject SEO); if it is a real
on-axis primary source, PROMOTE it into the matching swept list as `[verified YYYY-MM-DD]` and
clear its staging line; drop one-off noise with a one-line reason. Curators are one source-type
in this same loop. A recurring on-axis org left un-promoted week after week is a coverage leak
(the `source-discovery` metric in `radar-self-eval`).
Append a dated correction entry to `strategy_notes`.

## 5. Self-evaluation
Follow `radar-self-eval`:
- Every run: compute calibration metrics (queue funnel, evidence/stage moves, exploration
  compliance, off-axis rate, discovery lag, `coverage` = registered sources vs the week's
  logs, `routing-leak`) and append one dated line to `logs/calibration.md`.
- First run of each calendar month (`date +%d` ≤ 7): run the hit/miss retrospective.
- Prepare up to 3 proposed amendments, each motivated by a metric or retrospective.

## 6. Self-amendment
Per the autonomy contract in AGENTS.md: APPLY amendments proposed last week whose signal
persists and that have no dated curator veto; one dedicated commit each. Check past
amendments for two-week regression → `git revert` + log. Log this week's new proposals.
Never touch the immutable sections.

## 7. Write the weekly report
Create `reports/weekly/YYYY-Wnn.md` (under ~90 lines): stage moves/merges/archivals;
strongest & weakest trend; 3–5 forward-looking bets; source strategy changes; calibration
block (and monthly retrospective when due); amendments applied/proposed/rolled back.

## 8. Persist
`git add -A`, commit with message exactly `radar: weekly recalibration YYYY-Wnn`.
Push to `main`: `git push origin HEAD:main`, even if the session started on a
`claude/*` working branch — the curator has enabled unrestricted branch pushes and
explicitly authorizes pushing to `main` (platform notes about `claude/*` describe the
default, not a prohibition); attempt it. Push ONLY `main` — do NOT also push the
session working branch. If rejected: retry once after `git pull
--rebase origin main`; only if the server still rejects it, push to the session branch,
open the report with a prominent BRANCH WARNING that `main` must be fast-forwarded
before the next run, and paste the verbatim rejection error. Never force-push.

## Hard rules (same as daily)
Cite only URLs opened this session; primary published sources only; never guess dates/URLs;
do not rename sections; max 10 evidence per trend; track and cite, never reproduce operational
payloads.
