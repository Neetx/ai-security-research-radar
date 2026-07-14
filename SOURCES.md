# Sources registry — AI Security Radar

Agent-owned registry of monitored sources for the **offensive AI-security** beat.
The radar maintains and evolves this file itself (add/remove/mark-dead entries, with
a one-line reason in the day's or week's report) — no curator sign-off needed. Skills
describe the *method*; this file is the *data* (the lists the skills iterate by force).

Hard-rule reminder: papers, tool repos, vendor/lab security blogs, CVEs/advisories and
standards are PRIMARY sources (citable evidence). Social/community sources are an INTAKE
LANE ONLY — never evidence; when a social signal links to or names a primary artifact,
follow the link and verify the artifact. Track and cite; never invent URLs/dates. A
source listed under a "swept every run" heading is a coverage PROMISE — log it opened or
`degraded: <reason>` every run.

Verification: entries marked **[verified 2026-06-23]** had their URL/feed opened and
confirmed during setup. Entries marked **[candidate]** are plausible but NOT yet opened —
the first sweep must verify them (`radar-source-verify`) before citing, and heal or drop
on failure.

---

## Primary feeds — vendor/lab security blogs & advisories (Phase 1 — swept EVERY run)

Method: `radar-lab-sweep`. Iterate EVERY entry; prefer the feed, fall back to `tvly
extract` for feed-less ones. Filter for OFFENSIVE relevance (attack techniques, red-team
tooling, exploitation research); skip product/marketing.

- Google Project Zero — https://googleprojectzero.blogspot.com/ · Atom `…/feeds/posts/default` **[verified 2026-06-23]**
- Trail of Bits — https://blog.trailofbits.com/ · feed `/feed/` (application/xml) **[verified 2026-06-23]** — AI/ML offensive security
- NVIDIA — cybersecurity category Atom https://developer.nvidia.com/blog/category/cybersecurity/feed/ **[verified 2026-06-23; heal 2026-07-01]** (garak / AI red team). HEAL (2026-07-01): the intermittent "feed-empty" returns (06-29/06-30) are a User-Agent gate — fetch with a browser UA: `curl -sL -A "Mozilla/5.0" <feed>`; without it the CDN returns an empty body. HEAL REFINEMENT (2026-07-05): the browser-UA `curl` has itself become UNRELIABLE (returned empty on 4 of the last ~6 passes, 07-02/03/04/05). MORE RELIABLE PATH: `tvly extract "https://developer.nvidia.com/blog/category/cybersecurity/feed/"` — Tavily fetches from its own infra and returns the full Atom body (~80 KB) consistently where the browser-UA curl returns empty. Prefer tvly-extract on the feed; keep the browser-UA curl as a fallback. (07-05: newest post is 07-02 "NVIDIA Confidential Computing for agentic AI" — a defensive/product post, off-axis.) NOTE (2026-06-27): individual article URLs (developer.nvidia.com/blog/<slug>) are blocked by the proxy — ONLY the Atom feed URL above works. Do not attempt to `tvly extract` individual article URLs; `degraded: article-URL-blocked`.
- Microsoft Security blog — https://www.microsoft.com/en-us/security/blog/ · feed `/feed/` (rss+xml) **[verified 2026-06-23]** (AI Red Team / PyRIT posts)
- Microsoft MSRC blog — https://msrc.microsoft.com/blog/ — NO clean RSS, AND a JS-rendered SPA: `tvly extract` (even `--extract-depth advanced`) returns only nav chrome, no post bodies (checked 2026-06-23 Pass 2, 2nd failure). HEAL: do not rely on the blog index; surface MSRC items via `tvly search --include-domains msrc.microsoft.com` for the topic, or via the Microsoft Security blog feed which carries most AI-security items. Mark `degraded: SPA, search-only`.
- OpenAI — https://openai.com/news/ · RSS `/news/rss.xml` (text/xml) **[verified 2026-06-23]** — filter for red-teaming / preparedness items. HEAL-WATCH (2026-07-11, W28): returned empty on 3 CONSECUTIVE daily passes (07-08/07-09/07-10) — escalate from "transient" to heal-watch (the same 2-3-consecutive-empty threshold that triggered Project Zero's heal). HEALED (2026-07-13): `tvly extract "https://openai.com/news/rss.xml"` returns the FULL itemized feed (~213 KB, dated items) where the browser-UA `curl` returns empty — same Tavily-from-own-infra fix that healed Project Zero and NVIDIA. Use `tvly extract` on the RSS URL as the primary method; keep browser-UA curl as fallback. (07-13 newest items are all product/model-launch/enterprise — GPT-5.6, Deutsche-Telekom, bio-bug-bounty, gov-national-security-partnerships — no offensive-AI-security item.)
- Anthropic — TWO index pages, BOTH required every run (HEAL 2026-07-04, W27): `/research` (Frontier Red Team technical posts: N-days, exploit-development, LLM ATT&CK Navigator) alone MISSES security-relevant posts that only appear under `/news` (Newsroom/Announcements) — e.g. "Detecting and preventing distillation attacks" (2026-02-23), "Statement on the US government directive to suspend access to Fable 5 and Mythos 5" (2026-06-12), and "More details on Fable 5's cyber safeguards and our jailbreak framework" (2026-07-02) all sat un-swept for weeks because only `/research` was checked. NO public RSS on either (`/news/rss.xml` 404). Method: `tvly extract "https://www.anthropic.com/research" --extract-depth advanced` AND `tvly extract "https://www.anthropic.com/news" --extract-depth advanced` (the latter has a dated list under "News" — read titles/dates, extract new slugs). **[verified 2026-06-23; heal 2026-07-04 — /news added]**
- Palo Alto Unit 42 — https://unit42.paloaltonetworks.com/ · RSS `/feed/` **[verified 2026-06-29]** — PRIMARY threat-intel research (in-the-wild AI/agent attacks; e.g. OpenClaw/ClawHub malicious-skill disclosure 2026-06-23, cited on trend 001). Cite the article directly. Swept every run.
- Google Threat Intelligence (GTIG) — https://cloud.google.com/blog/topics/threat-intelligence — RSS `/rss` returns only the channel title, no items (JS-filtered blog), so the raw feed alone is `degraded: feed-not-itemized`. HEAL CONFIRMED (2026-07-04): `tvly search "<topic>" --include-domains cloud.google.com --depth advanced` reliably surfaces dated `cloud.google.com/blog/products/identity-security/...` articles, and `tvly extract` on the returned URL yields full body text. **CORRECTION (2026-07-11, W28): this pipeline sat UNUSED for 6 straight daily passes (07-05→07-10) — each just re-logged the old `degraded: feed-not-itemized` label instead of running the confirmed search+extract heal.** Running the raw RSS check and calling it "checked" does NOT satisfy this source's coverage promise — the search+extract pipeline (query terms: "AI agent security", "AI threat detection", rotate) IS the required method every run; only mark `degraded` if THAT pipeline itself returns nothing. Re-run this session (2026-07-11): no on-axis result (all AI-threat-defense/product content).
- Protect AI — huntr disclosures **[verified 2026-06-30; PROMOTED candidate→swept 2026-07-11, W28]** (live AI/ML vuln disclosures). Access method: `tvly extract "https://huntr.com/bounties/hacktivity" --extract-depth advanced` (HTML, JS-rendered — plain curl/HTTP 200 also reachable but Tavily renders the itemized list); NO RSS (`https://huntr.com/feed` → 404). PROMOTION EVIDENCE (2026-07-11): the hacktivity page returned three dated, on-axis ML-framework CVEs from the prior week alone — CVE-2026-12481 (Keras Lambda-layer deserialization RCE, 07-03, queued on TRENDS.md), CVE-2026-8147 (MLflow trace-endpoint authz bypass, 07-02), CVE-2026-12252 (nltk incomplete fix, 07-04) — a live, itemized, dated disclosure feed, not stale. Blog feed https://protectai.com/blog/rss.xml remains STALE (latest 2025-08-15) — do not sweep that URL, use the hacktivity page only. DEGRADED-WATCH (2026-07-13): `tvly extract` on the hacktivity page returned only nav chrome + a banner reading **"This page is sunsetting soon"** and an EMPTY itemized list (the JS-rendered bounty list did not render this pass) — first failure since promotion. The "sunsetting" notice suggests the URL/format is changing; if the empty-list result recurs, find the replacement disclosure surface (huntr may be migrating under Palo Alto/Prisma AIRS) before re-logging degraded. Not healed this pass; carry to next run's heal check. Filter: these are ML-FRAMEWORK/model-supply-chain CVEs (below the agent/MCP layer 001 tracks) — queue as off-axis-adjacent unless/until a dedicated model-supply-chain-vuln nucleus forms.
- Meta — Llama / AI security https://ai.meta.com/blog/ **[candidate]** — re-tried 2026-07-04 (`tvly search --include-domains ai.meta.com,engineering.fb.com`): zero results this pass; page extract returns nav-only (no itemized posts without a more targeted query). Re-tried again 2026-07-11 (W28): scoped search returned only stale generic pages (a "Join Us" careers page, the 2024 Llama-3.1 responsibility post, a researcher bio) — no dated 2026 security post. Still unresolved — try `tvly extract` on a specific known post URL next, or search Meta's engineering blog by name.
- NCC Group / Bishop Fox research blogs **[candidate]** — Bishop Fox confirmed to publish AI/LLM-relevant posts (`tvly search --include-domains bishopfox.com` surfaced "Mythos Doesn't Deploy Itself", title suggests Claude-Mythos-deployment security commentary) but the site is JS-heavy: `tvly extract --extract-depth advanced` on the article URL returned nav/services chrome only, no post body — needs a `--query`-scoped extract or a different render path next attempt. Re-tried 2026-07-11 (W28): same URL, same result (nav/services chrome, no article body) — extraction method still unresolved. NCC Group (research.nccgroup.com) returned zero search hits this pass — still unresolved.
- DEF CON AI Village — https://aivillage.org/ · RSS `https://aivillage.org/feed.xml` **[verified 2026-06-23; RSS found + MOVED here from "Research venues" 2026-07-04]** — the offensive-AI community/event (talks, CTFs, red-team challenges, generative-AI bug bounties); track outputs and writeups. COVERAGE-GAP FIX (2026-07-04, W27): this entry sat in "Research venues" (no "swept every run" heading) and had NEVER appeared in `logs/source_rotation.md` since launch (6 weeks) — a persistent MISSING-source coverage lie caught by this week's self-eval. Feed is plain RSS, `curl` reachable, no browser-UA needed. First sweep this session surfaced "Meta AI Agent Account Takeover" (2026-06-05, → evidence on agentic-attack-surface-001) and "AI Cyber League" (2026-06-30, community-history essay + new AI-security competition announcement — queued as context).
- Advisory feeds: NVD API https://services.nvd.nist.gov/rest/json/cves/2.0 **[verified 2026-06-23]** ; GitHub advisories (GHSA) for AI tooling **[candidate]**

## Standards watch (swept every run) — COVERAGE-GAP FIX 2026-07-11, W28

MOVED here from "Research venues" (a plain bullet with no "swept every run" heading,
same root cause as the DEF CON AI Village gap W27 fixed): daily logs had written "not
changed-checked this pass" for BOTH entries below on every single day since W27 first
flagged it (7 consecutive days, 07-04→07-10) — a standing-miss, not a one-week lapse.
Method: open each URL directly every run and diff against the last noted revision.
- OWASP GenAI / LLM Top 10 — https://genai.owasp.org/llm-top-10/ **[verified 2026-06-23; re-checked 2026-07-11]** — still "LLM TOP 10 FOR 2025", no 2026 revision.
- MITRE ATLAS — https://atlas.mitre.org/ **[verified 2026-06-23; re-checked 2026-07-11]** — matrix page loads; no dated changelog to diff against, eyeball the tactics/techniques list for new entries.
- NIST AI RMF / adversarial-ML taxonomy **[candidate]**.

## Research venues — arXiv & security conferences (primary)

- arXiv — **cs.CR** (core) https://arxiv.org/list/cs.CR/recent **[verified 2026-06-23]**, plus cs.AI / cs.LG / cs.CL for attack-on-model work. Metadata via `export.arxiv.org/api/query?id_list=...`.
- Conferences (proceedings/preprints) **[candidate]**: USENIX Security, IEEE S&P (Oakland), ACM CCS, NDSS; offensive cons (DEF CON, Black Hat AI/ML tracks).

## GitHub watch (Phase 5 — repos, profiles, and fork trees)

Method: `radar-repo-watch`. Watch releases (`<repo>/releases.atom`), notable forks, and
profile activity. New releases/tools are citable artifacts; issue/PR/fork/profile movement
is a queue signal. (Agent owns and grows these lists.)

ACCESS NOTE (2026-07-02 — GitHub scope block, self-heal): the session's GitHub access is
proxy-SCOPED to the radar's OWN repo — every EXTERNAL GitHub endpoint returns HTTP 403
("GitHub access to this repository is not enabled for this session"), confirmed on BOTH
`<repo>/releases.atom` AND `api.github.com/repos/...`. Network egress is FULL, so this is the
GitHub INTEGRATION intercepting github.com/api.github.com — NOT an egress block, and NOT a
network allowlist the curator can widen. WORKING METHOD until scope is restored: route the
GitHub-watch lane through `tvly` — `tvly extract https://github.com/<owner>/<repo>/releases`
(Tavily fetches from its own infra, bypassing the interception), or `tvly search` the
repo/tool + version + month. Lower fidelity (no commit/PR/fork-tree diff) but catches new
release tags. Retest raw `curl .../releases.atom` occasionally in case the scope is restored.
CORRECTION (2026-07-04, W27): this was logged as a "per-session" constraint on 07-02, but it
has now recurred identically across three consecutive sessions (07-02, 07-03, 07-04) — treat
it as a STANDING constraint, not per-session, until proven otherwise. Also, `tvly extract` on
`github.com/<owner>/<repo>/releases` returns nav-chrome only (JS-rendered list, no release
items) and `tvly search` for "<tool> release version 2026" surfaced no dated results this
pass — the Tavily fallback for GITHUB pages specifically does not actually work well. BETTER
HEAL: skip GitHub entirely and query the package registry each tool ships to — no proxy
scoping, no JS-rendering, exact version + timestamp: `curl -sL https://pypi.org/pypi/<pkg>/json`
(garak, pyrit, deepteam, giskard) or `curl -sL https://registry.npmjs.org/<pkg>` (promptfoo) —
read `info.version`/`dist-tags.latest` + `releases[<v>][0].upload_time`/`time[<tag>]`. Verified
this session: garak 0.15.1 (unchanged), promptfoo 0.121.17 dated 2026-06-16 (unchanged), PyRIT
0.14.0, and **deepteam 1.0.7 uploaded 2026-07-01** — a release the radar's GitHub-only watch
missed entirely (last logged version was 1.0.5 from 2026-01-06; 1.0.6 shipped 2026-03-03 and
1.0.7 2026-07-01, neither ever surfaced). No changelog content was found/verified this session
(package-registry timestamps only, no release notes opened) — a daily pass should open
deepteam's changelog/tag diff before citing anything from it as evidence.

W27 PROPOSAL F APPLIED (2026-07-11, W28 — cooling period elapsed, signal persisted all 7 days
this week: GitHub `releases.atom`/`api.github.com` re-tested directly 2026-07-11 and still
403 "sessions are bound to their configured repositories"): the PyPI/npm registry method is
now the PRIMARY method (not a fallback) for garak, PyRIT, deepteam, giskard and promptfoo —
check the registry JSON every run without first trying the blocked GitHub endpoint.

REMAINING GAP (flagged 2026-07-11, W28 — unresolved this session, carry to next weekly's
heal-worklist): 7 of 12 watched repos have NO registry equivalent and therefore ZERO release
coverage since the proxy block took hold (~07-02) — llm-attacks/llm-attacks, protectai/
ai-exploits, meta-llama/PurpleLlama, ethz-spylab/agentdojo, andyzorigin/cybench,
princeton-nlp/intercode, elder-plinius/L1B3RT4S (research/collection repos, not packaged).
Tried `tvly extract` on a commits page as a substitute this session — it renders real
content but from a STALE CACHE (elder-plinius/L1B3RT4S commits page showed Feb 17, 2026 as
the newest commit, 5 months stale) — NOT adopted as a heal, do not rely on it for freshness.
Next attempt: a repo-specific third-party mirror/RSS, or a GitHub search-API path not scoped
the same way as `releases.atom`/`repos/.../releases`.

### GitHub tool-DISCOVERY (swept every run — NEW tools are a PRIMARY output of this radar, not just watched-repo releases)

TWO distinct, CO-EQUAL things to observe — do NOT rank one below the other:
- **(A) RESEARCH** — papers/arXiv (the science of attacks & defenses) → feeds trends + `study_shelf`.
- **(B) usable public TOOLS** — GitHub repos a red-teamer can clone & run → THIS lane + the render's
  `🛠️ Tools & releases` block.
They are complementary, not competing: a paper reports a *method*; a tool is a *thing you run*. Many
strong tools ship with NO paper, and many papers have no public tool — so tool-discovery is GitHub-NATIVE
and does not depend on arXiv (that is WHY it's a separate lane, NOT because papers are lesser). Hunt
GitHub directly, every run. The session's github.com is 403-scoped and `tvly extract` of release pages
returns JS nav-chrome — but `tvly search --include-domains github.com` and the GitHub Topics pages WORK
via Tavily (verified 2026-07-14). Channels:
- **GitHub Topics pages** — the biggest paper-independent firehose: `tvly search --include-domains
  github.com "<tag> GitHub Topics"` → `github.com/topics/<tag>` lists every repo carrying that tag,
  sortable by recency/stars. Rotate through a BROAD tag set (≥3 tags/run, advance through the list):
  - *Prompt/jailbreak:* `prompt-injection` · `indirect-prompt-injection` · `prompt-injection-attacks` ·
    `prompt-injections` · `prompt-security` · `jailbreak` · `llm-jailbreak` · `prompt-hacking`
  - *LLM/AI-sec offensive:* `llm-security` · `ai-security` · `ai-security-tool` · `ai-red-teaming` ·
    `llm-red-teaming` · `red-teaming` · `offensive-security` · `cybersecurity-tools`
  - *Agents/MCP:* `agent-security` · `mcp-security` · `mcp-scan` · `skill-scanner` · `ai-agents` ·
    `autonomous-agents` · `multi-agent-system` · `openclaw-security`
  - *Adversarial-ML / model attacks:* `adversarial-attacks` · `adversarial-machine-learning` ·
    `adversarial-examples` · `textattack` · `backdoor-attack` · `data-poisoning` · `model-extraction` ·
    `membership-inference` · `model-inversion` · `model-stealing`
  - *Misc offensive:* `deepfake` · `abliteration` · `ai-exploitation` · `ml-security` · `machine-learning-security`
  Bolded/first-group tags **[verified real 2026-07-14 via topic-page harvest]**; the rest are plausible
  → confirm each on first use (a `github.com/topics/<tag>` with 0 repos = drop it). SKIP the DEFENSIVE
  variants (`prompt-injection-defense/detection/protection`, `guardrails`) except to find the tool being
  attacked — this is an OFFENSIVE radar. The agent OWNS and grows this tag list.
- **`tvly search --include-domains github.com "<free-text topic>"`** for things without a clean tag:
  `AI pentest toolkit`, `adversarial-suffix / GCG`, `agent-sandbox escape`, `AI supply-chain / malicious
  skill`, `LLM data-exfiltration`, `voice-clone / deepfake offense`, `MCP server exploit`.
- **Curated "awesome" lists** (a firehose of vetted public tools): `user1342/Awesome-LLM-Red-Teaming`,
  plus `tvly search "awesome LLM security / AI red team"` for new ones **[verified 2026-07-14]**.
- **New repos from watched security orgs/researchers** (Watched profiles below) — a known red-teamer's
  brand-new repo is a top signal, no paper required.
- The **pulse/curator lane** (tldrsec, DEF CON AI Village, HN) already names tools — capture the repo here.
For each candidate tool: stage its `owner/repo` in "Discovered-source candidates" → **VERIFY IT IS REAL &
PUBLIC**: package registry `pypi.org/pypi/<pkg>/json` or `registry.npmjs.org/<pkg>` (→ version + timestamp
+ homepage) if it ships to one, else `tvly search`/`tvly extract` the repo to confirm it has actual
code/README/recent activity — REJECT empty, "coming soon", archived, or 404 repos. A verified public tool
→ add to Watched repositories AND surface it in the render's **🛠️ Tools & releases** block. GOAL: never
miss a usable tool the week it ships; never surface a vaporware repo as if it were one.

### Watched repositories  (all **[verified 2026-06-23]** via GitHub API unless noted)
- NVIDIA/garak — the LLM vulnerability scanner (note: `leondz/garak` 301-redirects here)
- Azure/PyRIT — Python Risk Identification Tool for generative AI (Microsoft)
- promptfoo/promptfoo — prompt/agent/RAG red-teaming & pentesting
- confident-ai/deepteam — framework to red-team LLMs and AI agents
- Giskard-AI/giskard — LLM red-team & scanning (repo resolves via 301)
- llm-attacks/llm-attacks — Universal & Transferable Attacks on Aligned LLMs (GCG)
- protectai/ai-exploits — real-world AI/ML exploits for responsibly-disclosed vulns
- meta-llama/PurpleLlama — LLM security tools incl. CyberSecEval offensive benchmarks
- ethz-spylab/agentdojo — dynamic env to evaluate ATTACKS & defenses for LLM agents
- andyzorigin/cybench — CTF benchmark for autonomous agents
- princeton-nlp/intercode — InterCode benchmark (NeurIPS 2023; code/CTF agent tasks)
- elder-plinius/L1B3RT4S — **[verified 2026-06-23 via API]** large public collection of working jailbreaks per model; track ADDITIONS as a leading indicator of new bypasses (intake — link the repo, never paste payloads into the ledger)
- (agent: add tools as they appear in papers/cons; drop abandoned ones)

### Watched profiles/users  (GitHub orgs behind the watched tools — **[verified 2026-06-23]** via API; watch for NEW repos/releases under each)
- github.com/NVIDIA (garak) · github.com/Azure (PyRIT) · github.com/microsoft
- github.com/protectai (ai-exploits, modelscan) · github.com/promptfoo · github.com/confident-ai (deepteam)
- github.com/ethz-spylab (agentdojo, adversarial ML) · github.com/meta-llama (PurpleLlama/CyberSecEval) · github.com/Giskard-AI
- (agent: add individual maintainers/researchers as their repos prove high-signal — link the profile, never quote the person)

### Fork-tree analysis
- Scan notable forks (depth ~3, scored by stars/recency) of the highest-signal repos — a
  diverging fork is often where a new offensive capability first appears. Seed targets:
  `llm-attacks/llm-attacks` (GCG — heavily forked for new adversarial-suffix variants),
  `NVIDIA/garak` (new probes/detectors), `ethz-spylab/agentdojo` (new agent attacks),
  `protectai/ai-exploits` (new disclosed exploits). Add a repo here once its fork tree
  proves productive.

## Discovered-source candidates (auto-staged by the daily — NOT yet swept; the weekly verifies & promotes)

The source-discovery loop's staging area. The radar grows its OWN source coverage the way it
finds papers and curators: when any daily lane NAMES an on-axis primary whose publishing
org/domain is NOT already in a swept list above, the daily APPENDS/increments it here — a tally
only, NO extra fetch (you already hold the URL). The weekly VERIFIES the recurring ones (opens
the feed / repo / channel — never from memory) and PROMOTES them into the swept registry as
`[candidate]`, pruning one-off noise. This closes the gap where an on-axis tool author/vendor
that announces only on its own channel (not a tracked venue) goes untracked because no swept
list points at it. Promotion bar: ≥2 on-axis primary artifacts OR recurrence across ≥2 runs,
AND it survives verification (real feed, on-axis, not SEO). Line format:
`domain/org — times seen — last on-axis artifact (date) — first seen YYYY-MM-DD`.

- hackerfactor.com (Dr. Neal Krawetz, image-forensics researcher) — 1 — "Meta's Un-Stable Signature" AI-image-watermark attack (~2026-06-30, surfaced via HN 2026-07-05) — first seen 2026-07-05
- blog.zksecurity.xyz (zkSecurity — AI audit agent "zkao"; crypto/security research firm) — 1 — "AI meets Cryptography 1: What AI Found in Cloudflare's CIRCL" — 7 AI-found, upstream-fixed crypto bugs (2026-07-07, surfaced via HN, → evidence on ai-vuln-discovery-002) — first seen 2026-07-08. On-axis in-the-wild AI-vuln-discovery series; verify feed/RSS next weekly.
- oddguan.com (Aonan Guan — independent AI-agent-security researcher, "Lyrie Research") — 1 — "Comment and Control: Prompt Injection to Credential Theft in Claude Code, Gemini CLI, and GitHub Copilot" cross-vendor GitHub-Actions PI → Actions-secret theft (pub 2026-04-15, surfaced via tldrsec #336, → queued on agentic-attack-surface-001 + study_shelf) — first seen 2026-07-13. On-axis production-coding-agent PI disclosures; verify feed/RSS + look for a series next weekly.
- specterops.io (SpecterOps — offensive-security firm; Neeraj Gupta) — 1 — "Jailbreaker" open-source repeatable LLM-jailbreak-testing platform (PAIR/TAP/Crescendo/AutoDAN/GPTFuzz), surfaced via tldrsec #336 (→ queued, unverified — primary repo/blog not opened) — first seen 2026-07-13. Offensive-AI red-team tooling; verify the blog/repo next weekly.

## Social & community channels (Phase 2 — INTAKE ONLY, never evidence)

Method: `radar-pulse`. Intake feeds `observation_queue` (unverified) + the pulse note;
never name/quote individuals beyond a bare URL. Multi-channel earthquake check.
NOTE: Reddit blocks direct API from this setup (`about.json` → 403, checked 2026-06-23) —
reach subs via Tavily, not `.json`. RECOVERED 2026-07-04 (W27): a broad `tvly search` (no
domain filter, just `site:reddit.com <topic>` framing) returned 5 live results this session
(r/cybersecurity, r/ClaudeAI, r/technology, r/trainAIjobs, r/AskIreland) after 8+ consecutive
degraded passes across W26–W27 — downgraded from hard `degraded` to `intermittent`. None of
this pass's results were on-axis (no earthquake), so no queue item, but the access path works
again — keep retrying every run, subreddit-scoped queries specifically (not just broad terms).
- Reddit (`intermittent — recovered 2026-07-04, retry each pass`): r/netsec, r/MachineLearning, r/LocalLLaMA, r/hacking, r/AskNetsec (well-known active subs); r/ChatGPTJailbreak (jailbreak community). Read TOP + earthquake check.
- Hacker News — Algolia API https://hn.algolia.com/api/v1/search?tags=front_page (+ `query=<term>`) **[verified pattern; known reliable]**

### YouTube — TRUSTED-CURATOR POINTER LANE (check EVERY run, intake only)
- Microsoft Developer — feed `https://www.youtube.com/feeds/videos.xml?channel_id=UCsMica-v34Irf9KVTh6xx-g` **[verified 2026-06-23; channel_id resolved]** — hosts the "AI Red Teaming 101" series; BROAD channel, filter for AI-red-team/security items only. Re-checked 2026-07-04: recent uploads are generic dev-tool content (M365 Copilot MCP demo, Data Exposed, Cozy AI Kitchen) — no new AI-red-team item this pass.
- Black Hat — feed `https://www.youtube.com/feeds/videos.xml?channel_id=UCJ6q9Ie29ajGqKApbLqfBOg` **[verified 2026-07-04]** — NEW this week: official conference-talk uploads, several published WITHIN DAYS of this session and squarely on-axis, e.g. "Black Hat Europe 2025 | Automatic Detection of Taint-Style Vulnerabilities in LLM-based Agents" (published 2026-07-03) and "...How We Turned AI's 'Web Browsing' Into A Gateway For Targeting 1B+ Users" (published 2026-06-28). Conference talks are explicit primary material per the hard rules (DEF CON/Black Hat) — treat citably like a paper (follow to the talk's own abstract/slides/paper where linked; the video page itself is citable if no companion write-up exists). Both above titles queued this pass as significant, not yet individually opened beyond title/date.
- Embrace The Red (Johann Rehberger) — own channel still **[candidate — channel_id unresolved]**: a video search for his talks resolved to the UPLOADING conference's channel (Black Hat), not a personal channel — his blog (below, swept every run) remains the primary access path; his content is not going untracked.
- (agent: add offensive-AI / red-team / CTF-agent channels as they prove high-signal — resolve `channel_id` once, follow each video's link to the named primary, cite the primary not the video. Do NOT invent channel names.)

### Curated digests + explainer/aggregator blogs (INTAKE LANE — swept every run)
- Embrace The Red — https://embracethered.com/blog/ · RSS https://embracethered.com/blog/index.xml **[verified 2026-06-23]** — Rehberger's own prompt-injection / agent-attack research; often IS the primary artifact (then cite it directly).
- tldrsec — https://tldrsec.com/ **[RECOVERED 2026-07-05 — was `degraded: 403` for 5+ passes since 06-27]** — security newsletter (Clint Gibler), heavy AI-security coverage; follow to the named primary. HEAL (2026-07-05): plain `curl -sL -A "Mozilla/5.0" https://tldrsec.com/` now returns HTTP 200 with the FULL homepage (~487 KB, itemized dated issues) — the 403 wall is gone; issue permalinks are `https://tldrsec.com/p/tldr-sec-<NNN>` and `tvly extract <permalink> --query "<topic>"` pulls the lead-item summaries. First recovered sweep surfaced #335 (07-02) "Prompt Injection as Role Confusion" → followed to arXiv:2603.12277 (queued + shelved). Retry each run; re-mark degraded only if the 403 returns.
- Simon Willison — https://simonwillison.net/ **[verified 2026-06-23]** — extensive prompt-injection coverage and original framing; follow to the primary.
- Kai Greshake — https://kai-greshake.de/ · RSS https://kai-greshake.de/index.xml **[verified 2026-06-23]** — the researcher who pioneered indirect prompt injection; his posts are often the original disclosure (cite directly).
- MLSecOps — https://mlsecops.com/ + https://community.mlsecops.com/ `intermittent-thin (recovered access 2026-07-04)` — both URLs now return HTTP 200 and `tvly extract` renders the page (no more hard fail), but the extracted content is nav-chrome + lorem-ipsum placeholder blocks, no itemized dated posts — same class of issue as tldrsec below. Follow to the primary if a dated post ever surfaces; do not expect a usable article list from the homepage alone.
- Palo Alto Unit 42 — MOVED to "Primary feeds" (verified 2026-06-29, RSS `/feed/`); it is a primary research source, not a digest.
- (agent grows this list; every entry logged opened or `degraded:<reason>`; follow to the primary, never cite the digest unless it is the original disclosure.)

## Discovery / exploration venues (Phase 4 — iterated EVERY run by radar-explore)

Read top/most-attention items regardless of sub-topic, advancing the date window.
- arXiv cs.CR recent **[verified 2026-06-23]** + Hugging Face papers (security-tagged) **[candidate]**.
- Rotating single-category supplement (APPLIED 2026-07-04, W27 — was W26 Proposal C, cooling period held, signal persisted: no session ever actually opened cs.AI/cs.LG despite SOURCES.md documenting them as in-scope, and trend 004's backdoor cluster was seeded entirely from queue accumulation, never from an explore hit, exactly the miss Proposal C flagged): once every ~3–4 daily passes, swap the cs.CR explore pass for **arXiv cs.AI** or **cs.LG** recent-listing (rotate the two), same significance-first method — adversarial-ML / trigger-implantation / backdoor work frequently cross-lists there instead of cs.CR. Track which category and date-window was covered in `logs/source_rotation.md` each time so the rotation actually advances instead of always defaulting back to cs.CR.
- GitHub Trending (security / LLM-attack tooling); alphaXiv / Papers with Code trending (security) **[candidate]**.
- Watch-area venues (surface and queue): autonomous-exploitation / CTF-agent research, AI-malware research, hardware/side-channel attacks on inference.
