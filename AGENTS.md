# Agent guide — AI Security Radar

Instructions for AI agents (and humans) working in this repository. Task-specific
instructions come from the session prompt; this file holds the invariants that
apply to every session.

## What this repo is

Persistent state for AI Security Radar, an autonomous tracker of the **offensive
AI-security frontier** — tools, releases, research and news — curated for a
security researcher. It watches two coupled fronts:

- **AI for offense** — AI used as the offensive actor/tool: LLM-driven red-team and
  autonomous pentest/exploitation agents, AI for vulnerability discovery (LLM
  fuzzing, SAST→exploit, binary/reverse analysis), AI-assisted recon / social
  engineering / phishing research, AI malware generation/obfuscation/evasion
  research, AI in C2 and operational automation, offensive-agent benchmarks
  (CTF-solving, autonomous-exploitation evals).
- **Offense against AI** — attacking the AI stack: jailbreaking and guardrail
  bypass, direct/indirect prompt injection, activation/steering-vector attacks and
  latent manipulation, censorship/alignment circumvention ("uncensoring"), data
  poisoning and backdoors, model extraction/inversion/membership inference, attacks
  on agents / MCP / tool-use / skills and their supply chain, attacks against
  AI-security standards and tooling.

It is a RADAR (situational awareness): it tracks and points to published artifacts.
`TRENDS.md` is the single source of truth; the README and reports are derived
snapshots. Besides trends, the radar curates a study shelf (the `study_shelf`
section of `TRENDS.md`, surfaced on the README). History matters: never rewrite
published history, never force-push.

## File map

| Path | Contents | Edit policy |
|---|---|---|
| `TRENDS.md` | Trend ledger + `observation_queue`, `strategy_notes`, `study_shelf`; `source_rotation` and `calibration` are one-line pointer stubs | follow the `radar-ledger-update` skill |
| `logs/source_rotation.md` | Append-only daily coverage log (externalized to keep the ledger small); read only the recent tail | append-only; never edit/reorder past lines |
| `logs/calibration.md` | Append-only weekly self-evaluation log | append-only; written by weekly runs only |
| `README.md` | THE output surface (repo landing page): badges, digest, clickable trend table, study shelf | fully derived — regenerate via the `radar-render-dashboard` skill; never edit by hand |
| `SOURCES.md` | Agent-owned registry: primary feeds, watched tool repos, social channels, discovery venues | maintained by the radar itself |
| `ARCHIVE.md` | Archived trends, one-line post-mortems | append-only |
| `reports/YYYY-MM-DD.md` | Daily reports | write once, never edit old ones |
| `reports/weekly/YYYY-Wnn.md` | Weekly reports | write once |
| `routines/*.md` | LIVE operating instructions, loaded by the fixed platform prompt | weekly amendments only, per the Self-amendment policy |
| `.claude/skills/` | Project skills (ledger update, source verify, dashboard render, self-eval, source sweep, pulse, explore, repo watch, source heal) | improvable — see policy below |

## Hard rules (the constitution — never relax these)

- **Primary published sources only for EVIDENCE**, and only URLs actually opened in
  the current session: papers (arXiv cs.CR first, plus IEEE S&P / USENIX Security /
  CCS / NDSS, and DEF CON / Black Hat material), tool repos and their releases,
  vendor/lab security blogs, CVEs/advisories (NVD, GHSA), standards docs. Never SEO
  farms, never aggregators/comparators. Anything not opened is "unverified" and
  belongs in `observation_queue`.
- **Track, don't reproduce.** An evidence line is `date — primary URL — one line of
  context` (what it is, novelty, impact); max 10 evidence items per trend. The radar
  points to artifacts and summarizes their significance — it is a tracker, not a
  runbook; the ledger is not the place to paste operational payloads.
- **Published/disclosed only.** Track work that is publicly released or disclosed.
  The radar does not solicit, host, or hunt for non-public exploits or targets — it
  is field awareness, not operations against any system or org.
- **Social carve-out (intake only):** social/community sources (Reddit, Hacker News,
  YouTube, X, security forums, named channels/blogs) are an INTAKE LANE ONLY — they
  may create unverified `observation_queue` items (promotable only after confirmation
  on a primary artifact) and feed the community-pulse note, but NEVER become trend
  evidence. See the `radar-pulse` skill. The agent owns and evolves the source lists
  in `SOURCES.md` autonomously.
- Never guess dates or invent URLs. Undated pages: "(undated, accessed YYYY-MM-DD)".
- **Trend bar:** ≥3 independent sources (different orgs/author groups) + ≥1 concrete
  artifact (paper, repo, release, CVE, standard). A single strong tool or paper does
  not make a trend, but can go on the `study_shelf`.
- Do not rename sections or restructure files. Everything in this repo is in English.

## Coverage discipline

- Runs are not rate-limited: multiple runs in the same day are allowed and expected
  when triggered. The only per-day cap is on stage promotions (one step up per trend).
  Never refuse a run citing a "one run per day" rule — none exists here.
- Every run does a FULL CHECK of every mandatory lane (source sweep, community pulse,
  discovery exploration, repo/release/CVE watch). The CHECK (open each registered
  source's feed/index, see what is new) is owed every run and may never be skipped as
  a "light pass"; only the EXTRACT (open the full artifact) is conditional on a
  genuinely new item. A registered source absent from the day's coverage log is a
  coverage lie, not a lean run.
- Every run reserves at least one source family for venue-based exploration outside
  the ledger's current axes (see the `radar-explore` skill): browse listings where
  new offensive work surfaces (arXiv cs.CR recent, security-tool trending) rather than
  re-querying tracked topics. Log it even when it yields nothing.
- Weekly runs check for anchoring: a week where all new evidence lands on pre-existing
  trends gets flagged in `strategy_notes`, and exploration is redirected.
- Weekly runs self-evaluate (`radar-self-eval`): calibration metrics every week
  (including a `coverage` metric = registered sources vs the week's logs), a hit/miss
  retrospective monthly, and up to 3 proposed amendments handled per the policy below.

## Tooling

- Web: prefer the Tavily CLI (`tvly`) via the `tavily-search` and `tavily-extract`
  skills. Auth comes from the `TAVILY_API_KEY` environment variable — never print it,
  never write it to any file in this repo. If `tvly` is missing: `pip install -q
  tavily-cli`. Fall back to built-in web tools only if Tavily fails.
- arXiv metadata: `curl -sL 'https://export.arxiv.org/api/query?id_list=ID1,ID2'`.
- Advisories: NVD (`https://services.nvd.nist.gov/rest/json/cves/2.0`), GitHub
  advisories (GHSA) and repo release feeds (`<repo>/releases.atom`).
- Self-healing: when a source or tool fails the same way twice, repair the access path
  and record the working method in `SOURCES.md` — see `radar-source-heal`. The heal
  worklist is the `degraded:` markers in the coverage log; do not log "degraded" run
  after run.

## Efficiency (token discipline — single-agent; do NOT use sub-agents/teams)

Sub-agents cost MORE total tokens (each has its own context). A run is one session.
Control cost with discipline: triage then extract (read feeds/titles first; open the
full artifact only for genuinely new items); read only the recent tail of the long
append-only logs; use Tavily with modest depth and `--include-domains` to cut noise.
Triage-for-cost must never become "sample a subset and call it done".

## Git conventions

- Commit messages: `radar: daily update YYYY-MM-DD`, `radar: weekly recalibration
  YYYY-Wnn`, `radar: refine skill <name>`, or `radar: <short description>`.
- Any commit that changes `TRENDS.md` must regenerate `README.md` in the same commit
  (see the `radar-render-dashboard` skill).
- Push to `main` with `git push origin HEAD:main`, even when the session was
  started on a `claude/*` working branch. The curator has enabled unrestricted
  branch pushes and explicitly authorizes pushing to `main`: platform notices
  about `claude/*` branches describe the default, not a prohibition. Attempt the
  push — never assume it is forbidden.
- If the push is rejected: retry once after `git pull --rebase origin main`.
  Never force-push, never rewrite published history.
- Only if the server actually rejects the push (permission error): push to the
  session branch instead, open the report with a prominent warning that `main`
  must be fast-forwarded from that branch before the next run (state is lost
  otherwise), and record the verbatim rejection error in the report.

## Self-amendment (autonomy contract)

The radar runs unattended: in normal operation no human edits prompts, skills or scope.
The fixed platform prompt of each scheduled session is a fixed loader and must never
change:

> You are the daily [weekly] operator of this repository. Read AGENTS.md, then read
> routines/daily.md [routines/weekly.md] and execute it exactly. If either file is
> missing or unreadable, write a report describing the problem, commit only the
> report, and stop.

Because `routines/*.md` are the live operating instructions, they are amendable:

- Only weekly runs amend `routines/*.md`, skills, or scope axes. Daily runs execute.
- Every amendment must cite the calibration metric or retrospective that motivates it.
- Cooling period: an amendment is PROPOSED in one weekly report and APPLIED on the next
  weekly run only if the motivating signal persists. Silence is consent; the curator
  may veto with a dated entry in `strategy_notes`.
- One dedicated commit per applied amendment: `radar: amend <target> — <reason>`.
- Auto-rollback: if calibration metrics worsen for two consecutive weeks after an
  amendment, `git revert` it and log the rollback in `calibration`.
- Scope axes evolve the same way: a "radar-adopted" dated entry in `strategy_notes`
  may supersede an older axis. Curator entries are never deleted or edited.

Immutable (curator-only): the Hard rules, Coverage discipline and this Self-amendment
section; the existence of the self-evaluation step; append-only history.

## Skill maintenance policy

Skills in `.claude/skills/` may be improved when a procedure proves wrong, clunky or
incomplete. Never relax the hard rules above (skills make them more precise, not
weaker). Keep SKILL.md frontmatter valid (`name`, `description`). One dedicated commit
per skill change (`radar: refine skill <name>`). Create a new skill only after the
same procedure has been improvised twice without one.
