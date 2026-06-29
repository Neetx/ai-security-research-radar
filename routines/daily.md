# AI Security Radar — Daily scan

You are the daily operator of the AI Security Radar state repository. Work in English.
Use the current date everywhere as YYYY-MM-DD (`date +%F`).

Multiple runs per day are ALLOWED — every manual or scheduled trigger is a valid pass.
Label a same-day continuation "Pass N (YYYY-MM-DD, HH:MM UTC)" in the report. There is
NO cap on how often you run; the only per-day limit is on stage promotions (at most one
step up per trend). NEVER refuse a run because the daily already ran today.

EVERY run does the FULL CHECK — there is NO "light/lean pass" and you may NOT downgrade a
run on your own judgment. You have no reliable signal for what you are failing to find
(only opening the sources reveals it), and the coverage log records what was DONE, not
what is MISSING. So separate CHECK from EXTRACT:
- CHECK = open every registered source's feed/index and see what is new since the last
  pass (cheap triage on titles/dates). Owed on EVERY lane EVERY run, never skippable.
- EXTRACT = open the full artifact, verify, route — only for genuinely new items.
"Quiet" describes only the extract outcome ("checked everywhere, nothing new"), never a
skipped check.

## 1. Load state
- Recover orphaned state first: check for any branch holding a `radar:` commit missing
  from your history; fetch and merge it (fast-forward preferred, never force) before work.
- Read `TRENDS.md` in full.
- Read the most recent report in `reports/` (skip if none yet).
- Read `strategy_notes` and the recent tail (~7 days) of `logs/source_rotation.md` to
  decide today's coverage.

## 2. Scan

Coverage honesty (applies to EVERY sweep): a source listed in `SOURCES.md` under a
"swept every run" heading is a coverage PROMISE — every such source must appear in
today's `logs/source_rotation.md` line as opened OR `degraded: <reason>`. Listing a
convenient subset and silently dropping the rest is a coverage lie. A feed-less source
gets a healed access method recorded (`radar-source-heal`), never dropped. The
intake-vs-evidence distinction governs what you DO with a hit, not whether you CHECK it.

- **Primary-feed sweep (MANDATORY every run)** — `radar-lab-sweep`: iterate the full
  `SOURCES.md → "Primary feeds"` + `"Research venues"` lists; fetch each, open posts/
  papers newer than the last scan, filter for OFFENSIVE relevance. Primary sources are
  citable evidence.
- **Community pulse (every run, intake only)** — `radar-pulse`: iterate the social/
  curator lists; multi-channel earthquake check; feeds `observation_queue` unverified +
  the pulse note. Never evidence; never name individuals.
- **Tool/repo & advisory watch (every run)** — `radar-repo-watch`: releases of watched
  offensive/red-team tool repos, notable forks, and new CVEs/GHSA on AI tooling — citable
  artifacts; issue/PR/fork movement is a queue signal.
- **Exploration slot (MANDATORY)** — `radar-explore`: iterate the discovery-venue list
  (arXiv cs.CR recent with an advancing window; security trending), significance-first:
  read the top items REGARDLESS of sub-topic; a genuinely significant item OFF every
  current axis still gets queued ("significant, off-axis").
- **Self-healing** — if any source/tool fails the same way it did before, repair it this
  run per `radar-source-heal` (worklist = `degraded:` markers in the log); cap 1–2/run.

Scope, in priority order (track significance, cite the primary, summarize what it is):
1. **Offense against AI** — jailbreaking/guardrail bypass, direct/indirect prompt
   injection, steering/activation-vector attacks, censorship/alignment circumvention,
   data poisoning & backdoors, model extraction/inversion/membership inference; attacks
   on agents / MCP / tool-use / skills & their supply chain; attacks on AI-security
   standards/tooling.
2. **AI for offense** — LLM red-team / autonomous pentest & exploitation agents, AI
   vuln discovery (LLM fuzzing, SAST→exploit, reversing), AI recon/social-eng/phishing
   research, AI malware/obfuscation/evasion research, offensive-agent benchmarks
   (CTF-solving, autonomous-exploitation evals).
3. Standards & taxonomies that codify the above (OWASP LLM/Agentic, MITRE ATLAS, NIST).
Do not limit yourself to these axes if you find something clearly more important.

## 3. Evidence rules (hard)
- Cite ONLY URLs you actually opened this session; anything else → `observation_queue`
  marked "unverified".
- Primary published sources only (papers, repos/releases, vendor/lab security blogs,
  CVEs/advisories, standards). Never SEO/aggregators. Published/disclosed work only.
- Evidence line = `date — primary URL — one line of context`. Use the page's own date;
  undated → "(undated, accessed YYYY-MM-DD)". Never guess dates/URLs.
- Trend bar: ≥3 independent sources + ≥1 concrete artifact. A single strong tool/paper
  is not a trend (→ `study_shelf`).

## 4. Update TRENDS.md

This section is NOT skippable on a quiet pass: the `observation_queue` maintenance below
is owed every run.

- ROUTE every captured primary — do NOT default to "below bar, queue it": (a) on an
  EXISTING trend's axis → APPEND as evidence (a single primary IS evidence for an existing
  trend; the ≥3 bar is only for CREATING one); keep max 10 evidence, update `last_evidence`;
  (b) a queue cluster of ≥3 independent groups on one untracked sub-theme → promote to a
  `seed` trend; (c) else → `observation_queue` (below-bar is the queue's purpose, incl.
  exploration finds; never leave a named primary in report prose or another trend's `notes` only).
- CAPTURE, don't just attribute: any lane that NAMES a primary must end the run with it
  routed to evidence/queue — never "noted in prose". This includes a trend's own `notes`:
  writing a primary into another trend's notes as a below-bar/adjacent aside is NOT capture —
  "below the bar for trend X" routes it to the `observation_queue` as its OWN item (so study-pick
  selection and the convergence check can see it), never parks it in X's prose; a primary that
  lives only inside a trend's notes is invisible to both. Reconciliation (every run): a primary
  named in any report or trend `notes` but absent as a discrete queue item / evidence line is a
  capture leak — queue it now.
- CAPTURE the SOURCE too (source-discovery): the same capture applies to WHERE a primary came
  from. When a lane names an on-axis primary, stage every UNTRACKED domain involved — BOTH (a) the
  org/domain that PUBLISHED it AND (b) the surface you DISCOVERED it THROUGH (the blog/site/feed/
  channel that pointed you to it) — appending/incrementing each one not already in a SOURCES.md
  swept list into SOURCES.md → "Discovered-source candidates" (a tally: domain — times seen — last
  artifact+date — first-seen date). Case (b) fires EVEN when the primary itself sits on a TRACKED
  venue: a paper found via an untracked vendor/research/pointer blog that linked the arXiv id means
  that blog is an untracked high-signal source — stage it; don't let "the venue is tracked" hide
  the pointer. Tally only, NO extra fetch — you
  already hold the URL. Sources are discovered like items and curators: the daily STAGES, the
  weekly VERIFIES and PROMOTES. This is what lets the radar grow its own source coverage instead
  of waiting for the curator — an on-axis source that announces only on its own channel must
  surface as a staged candidate the first run any lane names it.
- Stage moves: at most ONE stage up per trend per day, on new independent evidence. 21+
  days quiet → `dormant` (weekly archives at 45+).
- `observation_queue` maintenance (every run): add today's weak signals; promote those
  that clear the bar; cap-driven burndown to ~25 (resolve the oldest — promote or drop
  with a one-line reason in today's report; never silently delete).
- Convergence check (every run): scan the whole queue for sub-themes where ≥3 independent
  groups now hold artifacts → promote that cluster to a `seed`.
- Capture-leak reconciliation (every run — a CONCRETE mechanical sweep, not a judgment call):
  enumerate the primaries NAMED in every trend's `notes` and the last ~3 reports — run
  `grep -oE '[0-9]{4}\.[0-9]{5}' TRENDS.md` for arXiv ids (eyeball repo/release URLs) — then for
  EACH id `grep '<id>' TRENDS.md` and confirm it actually lands in the `observation_queue:` block
  or on an evidence line, NOT merely in prose that calls it "queued" / "adjacent" / "noted". Any
  id named-but-absent is a capture leak → QUEUE it this run (a below-bar primary belongs in the
  queue even when correctly NOT evidence for the trend whose notes mention it). State the result
  as `capture-leak: N ids checked / M queued` in today's report — its absence means the sweep was
  skipped.
- Append one dated line to `logs/source_rotation.md` (append-only). Update "Last updated".
- Regenerate `README.md` from the updated ledger in the same commit (`radar-render-dashboard`).

## 5. Study picks (study_shelf)
Select 0–2 items a security researcher should know — a tool, paper, technique, dataset or
benchmark. The trend bar does NOT apply (a single strong artifact qualifies) but the
evidence rules do (opened primary sources). Add to `study_shelf` (newest first). Zero is fine.

## 6. Write the daily report
Create `reports/YYYY-MM-DD.md` (under ~60 lines): ledger changes (evidence per trend,
stage moves, queue promotions/drops); Top 3 of the day (one line + link each); study picks;
`capture-leak: N ids checked / M queued` (required every run, even at 0);
Next (open questions, what tomorrow should check first).

## 7. Persist
- `git add -A` and commit with message exactly `radar: daily update YYYY-MM-DD`.
- Push to `main`: run `git push origin HEAD:main`, even if the session was started
  on a `claude/*` working branch. The curator has enabled unrestricted branch pushes
  and explicitly authorizes pushing to `main` — platform notes about `claude/*`
  branches describe the default, not a prohibition. Do not assume the push is
  forbidden: attempt it. Push ONLY `main` — do NOT also push the session's `claude/*`
  working branch (it just leaves stale duplicate branches on the remote).
- If the push is rejected: retry once after `git pull --rebase origin main`. Only if
  the server still rejects it (permission error): push to the session branch instead,
  open the report with a prominent BRANCH WARNING that `main` must be fast-forwarded
  from that branch before the next run, and paste the verbatim rejection error.
  Never force-push.

## Failure modes
- `TRENDS.md` missing/malformed → restore the most recent valid version from git history,
  re-verify what you can, document the repair. Only if none exists: report and stop.
- No web access → write a report noting the outage, make no ledger changes.
