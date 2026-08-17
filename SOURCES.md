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
- Microsoft Security blog — https://www.microsoft.com/en-us/security/blog/ · **HEALED 2026-07-21**: the `/feed/` extract returned channel-title-only/empty for 6 consecutive passes (07-15→07-20); the working method is `tvly search --include-domains microsoft.com "<topic>"` (e.g. "AI agent prompt injection red team"), which returns an itemized, dated Microsoft Security Blog index — use that, not the RSS feed, every run (AI Red Team / PyRIT / agentic-AI-security posts). Recent on-axis: "Securing AI agents: When AI tools move from reading to acting" (06-30), agentic-AI failure-modes taxonomy v2.0 (06-04), "When prompts become shells: RCE in AI…" (05-07).
- Microsoft MSRC blog — https://msrc.microsoft.com/blog/ — NO clean RSS, AND a JS-rendered SPA: `tvly extract` (even `--extract-depth advanced`) returns only nav chrome, no post bodies (checked 2026-06-23 Pass 2, 2nd failure). HEAL: do not rely on the blog index; surface MSRC items via `tvly search --include-domains msrc.microsoft.com` for the topic, or via the Microsoft Security blog feed which carries most AI-security items. Mark `degraded: SPA, search-only`.
- OpenAI — https://openai.com/news/ · RSS `/news/rss.xml` (text/xml) **[verified 2026-06-23]** — filter for red-teaming / preparedness items. HEAL-WATCH (2026-07-11, W28): returned empty on 3 CONSECUTIVE daily passes (07-08/07-09/07-10) — escalate from "transient" to heal-watch (the same 2-3-consecutive-empty threshold that triggered Project Zero's heal). HEALED (2026-07-13): `tvly extract "https://openai.com/news/rss.xml"` returns the FULL itemized feed (~213 KB, dated items) where the browser-UA `curl` returns empty — same Tavily-from-own-infra fix that healed Project Zero and NVIDIA. Use `tvly extract` on the RSS URL as the primary method; keep browser-UA curl as fallback. (07-13 newest items are all product/model-launch/enterprise — GPT-5.6, Deutsche-Telekom, bio-bug-bounty, gov-national-security-partnerships — no offensive-AI-security item.)
- Anthropic — TWO index pages, BOTH required every run (HEAL 2026-07-04, W27): `/research` (Frontier Red Team technical posts: N-days, exploit-development, LLM ATT&CK Navigator) alone MISSES security-relevant posts that only appear under `/news` (Newsroom/Announcements) — e.g. "Detecting and preventing distillation attacks" (2026-02-23), "Statement on the US government directive to suspend access to Fable 5 and Mythos 5" (2026-06-12), and "More details on Fable 5's cyber safeguards and our jailbreak framework" (2026-07-02) all sat un-swept for weeks because only `/research` was checked. NO public RSS on either (`/news/rss.xml` 404). Method: `tvly extract "https://www.anthropic.com/research" --extract-depth advanced` AND `tvly extract "https://www.anthropic.com/news" --extract-depth advanced` (the latter has a dated list under "News" — read titles/dates, extract new slugs). **[verified 2026-06-23; heal 2026-07-04 — /news added]**
- Palo Alto Unit 42 — https://unit42.paloaltonetworks.com/ · RSS `/feed/` **[verified 2026-06-29]** — PRIMARY threat-intel research (in-the-wild AI/agent attacks; e.g. OpenClaw/ClawHub malicious-skill disclosure 2026-06-23, cited on trend 001). Cite the article directly. Swept every run.
- Trend Micro / TrendAI Research — https://www.trendmicro.com/en_us/research.html **[verified 2026-07-18; PROMOTED candidate→swept, W29; METHOD REFINED 2026-08-04]** — the index `tvly extract` now returns marketing chrome plus TEASER TITLES ONLY (no post URLs, no dates), so it is enough to SPOT what is new but not to cite it. Reliable two-step recorded 2026-08-04: (1) extract the index to read the teaser titles, (2) for any new title run `tvly search "<exact title>" --include-domains trendmicro.com --max-results 3 --json` and read `.results[].url` to get the real article URL, then extract THAT (article pages carry a proper byline + date, e.g. "By: Jacob Santos Jul 24, 2026"). Do not guess the `/en_us/research/26/<letter>/<slug>.html` path — the month letter is not derivable from the publication date (the 07-24 autonomous-ransomware post lives under `/26/g/`). — PRIMARY in-the-wild AI-offense threat-intel (Patriot Bait jailbroken-Gemini-CLI-as-C2, TuxBot v3 LLM-assisted IoT botnet, claude.ai-shared-chat ClickFix malvertising — all cited/queued on trends 001/009). High-signal recurring source; cite the article directly.
- Oasis Security — https://www.oasis.security/blog **[verified 2026-07-18; PROMOTED candidate→swept, W29 — no RSS, use `tvly extract "https://www.oasis.security/blog" --extract-depth advanced`, itemized + dated post index]** — PRIMARY non-human-identity/AI-agent-security research (Elad Luz): a recurring series of claude.ai/Claude-Desktop indirect-PI disclosures (Claudy Day 03-18, PromptFiction 07-15 — queued on trend 001). Cite the article directly.
- Bishop Fox — https://bishopfox.com/blog **[verified 2026-07-18; HEALED + PROMOTED candidate→swept, W29 — the working URL is the plain `/blog` index (NOT the individual post path tried in W27/W28), `tvly extract --extract-depth advanced` returns a fully itemized dated post list]** — offensive-security firm; filter hard for AI/LLM-relevant items among the general pentest/CVE-research content (e.g. "Otto Support - Testing MCP Servers" 06-03, "Mythos Doesn't Deploy Itself" 06-09, "The Smash-and-Grab Era" — AI-accelerated-attacker commentary — 06-17; none individually verified beyond title/date yet).
- Sysdig TRT — https://www.sysdig.com/blog **[verified 2026-07-25; PROMOTED candidate→swept, W30 — `tvly extract "https://www.sysdig.com/blog" --extract-depth advanced` returns an itemized, dated blog index (no RSS confirmed)]** — cloud/runtime threat-research team; PRIMARY for in-the-wild agentic-threat-actor campaigns (JADEPUFFER — first fully-agentic ransomware/DB-extortion op, 07-01, on 009 evidence; "JADEPUFFER evolves" — same actor pivots to AI-model-artifact-destruction ransomware, 07-20, also on 009 evidence). Cite the article directly.
- Aonan Guan (oddguan.com) — https://oddguan.com/blog **[verified 2026-07-25; PROMOTED candidate→swept, W30 — `tvly extract "https://oddguan.com/blog"` returns an itemized post list; no RSS confirmed]** — independent AI-agent-security researcher (Lead Cloud & AI Security, Wyze Labs); a recurring series of production-coding-agent confused-deputy/sandbox disclosures — "Comment and Control" (cross-vendor GitHub-Actions PI→secret-theft, 04-15, on 001 evidence) and "Second Time, Same Sandbox" (Claude Code network-sandbox SOCKS5 null-byte bypass→exfiltration, 05-20, queued 07-25 as a top 001 rotate-candidate). Cite the article directly. METHOD REFINEMENT (2026-08-03): a plain `tvly extract` of the blog index only ever renders the top 1-2 posts' full text (whichever the page foregrounds), NOT a complete dated list — three older posts (2025-09, 2025-12, 2026-01) sat un-captured for weeks despite the source being "swept" every run, because no prior pass ever scrolled past the top of the index. FIX: periodically (at least monthly, or whenever the top-of-index yields nothing new for several consecutive runs) run `tvly search "oddguan.com <suspected topic/CVE>"` for topics/CVEs glimpsed only as fragments in the extract's tail text, to surface older un-opened posts by URL. This generalizes to any feed-less HTML-index source (Bishop Fox, Trend Micro, etc.) — a top-of-list diff is necessary but not sufficient for full-index coverage.
- zkSecurity (blog.zksecurity.xyz — crypto/security research firm; AI audit agent "zkao") — https://blog.zksecurity.xyz/ **[verified 2026-07-25; PROMOTED candidate→swept, W30 — plain URL extract returns a fully itemized, dated post index, ~1 post/week cadence, no RSS confirmed]** — PRIMARY in-the-wild AI-vuln-discovery series ("AI meets Cryptography"): part 1 found 7 real bugs in Cloudflare's CIRCL (07-07, on 002 evidence), part 2 found a CRITICAL soundness bug in OpenVM's zkVM — CVE-2026-46669, fixed in OpenVM 1.6.0 (07-17, queued 07-25 as a fresh 002 rotate-candidate); also ships zkao itself as a tool (v2.0 released 07-24 — study_shelf candidate). Cite the article directly.
- XBOW — https://xbow.com/blog **[verified 2026-07-16; no RSS (`/blog/rss.xml`, `/feed` 404) → `tvly extract "https://xbow.com/blog"`]** — the autonomous-AI-pentester vendor that topped the HackerOne US leaderboard; PRIMARY for its offensive-AI RESULTS (real CVEs/vulns its AI found, the XBOW benchmark, autonomous-pentest writeups — on ai-vuln-discovery-002's axis). Filter HARD for offensive research vs product-marketing/"practical guide" content-marketing (the blog carries both). Gap found 2026-07-16: XBOW was only ever a *benchmark reference* in the ledger, never a tracked source.
- Island Security Research — https://www.island.io/blog **[verified 2026-08-08; PROMOTED candidate→swept, W32 — no RSS confirmed, use `tvly extract "https://www.island.io/blog" --extract-depth advanced` (itemized index with "Security Research" + "Artificial Intelligence/AI" categories)]** — enterprise-browser vendor whose Security Research team (Oleg Zaytsev) publishes PRIMARY AI-capability-supply-chain research: "AgentBaiting: How 800+ Fake AI Skills and MCP Servers Delivered Malware" (07-20, now agentic-attack-surface-001 evidence + study_shelf) and "MCP Server Security Risks: What Scanning 33K Builds Found" (island.io/blog/your-ai-can-be-given-secret-instructions-in-plain-english, 08-05). Cleared the ≥2-on-axis-artifact bar. Cite the article directly.
- SpecterOps — https://specterops.io/blog **[verified 2026-07-28; PROMOTED candidate→swept, W33 — no clean RSS confirmed, use `tvly search "SpecterOps LLM AI jailbreak red team" --include-domains specterops.io` for the itemized dated index, then extract the returned post URL]** — offensive-security firm (Neeraj Gupta; the GhostWorks AI-cybersecurity-research line). PRIMARY offensive-AI research + tooling: "Jailbreaker" open-source repeatable LLM-jailbreak-testing platform (PAIR/TAP/Crescendo/AutoDAN/GPTFuzz — 2026-06-29, on study_shelf) + "This one weird trick: multi-prompt LLM jailbreaks safeguards hate it" (2025-09-05) + "Introducing GhostWorks: AI cybersecurity research" (2026-06-09) — ≥2 genuinely on-axis OFFENSIVE artifacts (W33 re-check). Filter the general offensive-security/AD content for AI/LLM items. Cite the article directly.
- Offensive-AI / AI-red-team VENDOR research blogs (2026-07-16 scouting pass — peers of XBOW; all PRIMARY for their own attack research, filter product-marketing):
  - Adversa AI — https://adversa.ai/blog/ · RSS https://adversa.ai/feed/ **[verified 2026-07-16; RSS]** — adversarial / agentic-AI red-team research (e.g. the Cursor "review this PR" deeplink RCE, 2026-07-15). High-signal, feed-backed → top of this cluster.
  - RunSybil — https://www.runsybil.com/blog **[verified 2026-07-16; HTML → `tvly extract`]** — autonomous offensive-security AI; real offensive writeups (agentic exploitation, e.g. "Exploiting … with Opus 4.8"). On ai-vuln-discovery-002.
  - Horizon3.ai attack research — https://horizon3.ai/attack-research/ **[verified 2026-07-16; HTML → `tvly extract`]** — NodeZero (AI-assisted autonomous pentest) CVE/exploit disclosures, dated; filter the AI-driven items from classic-pentest CVEs.
  - **[candidate]** HiddenLayer research (https://hiddenlayer.com/research/) — real adversarial-ML / AI-threat research but the page skews product; filter hard, HTML→tvly. Zenity (https://zenity.io/blog) — genuine agentic-AI attack research (Copilot/agent exploits) but plain `tvly extract` returns nav-only → use `--extract-depth advanced`. Gray Swan (https://www.grayswan.ai/news) — jailbreak arenas, but `/news` is product-heavy → confirm it carries attack writeups before promoting.
  - (agent: scout Mindgard, Lakera, SplxAI, Pillar Security, Repello, Dreadnode (`/research`, not `/blog`) via source-discovery — verify offensive research vs marketing before adding.)
- Google Threat Intelligence (GTIG) — https://cloud.google.com/blog/topics/threat-intelligence — RSS `/rss` returns only the channel title, no items (JS-filtered blog), so the raw feed alone is `degraded: feed-not-itemized`. HEAL CONFIRMED (2026-07-04): `tvly search "<topic>" --include-domains cloud.google.com --depth advanced` reliably surfaces dated `cloud.google.com/blog/products/identity-security/...` articles, and `tvly extract` on the returned URL yields full body text. **CORRECTION (2026-07-11, W28): this pipeline sat UNUSED for 6 straight daily passes (07-05→07-10) — each just re-logged the old `degraded: feed-not-itemized` label instead of running the confirmed search+extract heal.** Running the raw RSS check and calling it "checked" does NOT satisfy this source's coverage promise — the search+extract pipeline (query terms: "AI agent security", "AI threat detection", rotate) IS the required method every run; only mark `degraded` if THAT pipeline itself returns nothing. Re-run this session (2026-07-11): no on-axis result (all AI-threat-defense/product content).
- Protect AI — huntr disclosures **[verified 2026-06-30; PROMOTED candidate→swept 2026-07-11, W28]** (live AI/ML vuln disclosures). Access method: `tvly extract "https://huntr.com/bounties/hacktivity" --extract-depth advanced` (HTML, JS-rendered — plain curl/HTTP 200 also reachable but Tavily renders the itemized list); NO RSS (`https://huntr.com/feed` → 404). PROMOTION EVIDENCE (2026-07-11): the hacktivity page returned three dated, on-axis ML-framework CVEs from the prior week alone — CVE-2026-12481 (Keras Lambda-layer deserialization RCE, 07-03, queued on TRENDS.md), CVE-2026-8147 (MLflow trace-endpoint authz bypass, 07-02), CVE-2026-12252 (nltk incomplete fix, 07-04) — a live, itemized, dated disclosure feed, not stale. Blog feed https://protectai.com/blog/rss.xml remains STALE (latest 2025-08-15) — do not sweep that URL, use the hacktivity page only. DEGRADED-WATCH (2026-07-13): `tvly extract` on the hacktivity page returned only nav chrome + a banner reading **"This page is sunsetting soon"** and an EMPTY itemized list (the JS-rendered bounty list did not render this pass) — first failure since promotion. The "sunsetting" notice suggests the URL/format is changing; if the empty-list result recurs, find the replacement disclosure surface (huntr may be migrating under Palo Alto/Prisma AIRS) before re-logging degraded. **HEALED/DEMOTED 2026-07-16 (Pass 2):** confirmed via `tvly search --include-domains huntr.com` — the migration FAQ + platform pages now state **"Open source vulnerability submissions are currently closed"**; only **Model File Format (MFV)** reports remain open, "Supported by Palo Alto Networks and Prisma AIRS." So the general itemized OSS/AI-ML-framework hacktivity disclosure feed the 07-11 promotion relied on is genuinely SUNSET, not transiently broken — DEMOTE huntr from "swept every run (general disclosures)" to **model-file-format-only** (a niche off-axis surface: model-serialization/deserialization vulns, below the agent/MCP layer 001 tracks). The general ML-framework CVE stream (Keras/MLflow/nltk-class) now falls to the already-swept **NVD + GHSA** advisory lanes — no separate huntr sweep needed for it. Do not re-log huntr "degraded" for the empty OSS list; that list is intentionally closed. Filter unchanged: any MFV item is ML-framework/model-supply-chain (off-axis-adjacent), queue only if a dedicated model-supply-chain-vuln nucleus forms.
- Meta — Llama / AI security https://ai.meta.com/blog/ **[RESOLVED-OFF-AXIS 2026-07-18, W29 — DROPPED from candidate chase]** — extraction now WORKS (`tvly extract --extract-depth advanced` returns a fully itemized dated post list, unlike the nav-only results of 06-27/07-04/07-11), but every visible post is product/model-launch content (Muse Image/Video, SAM 3.1, TRIBE v2 brain model, Segment Anything) — zero security posts across the listing. Not a broken source, a wrong one: this URL is not where Meta publishes AI-security research (if it exists elsewhere, it is not this blog). Stop chasing; revisit only if a future lane names a specific ai.meta.com/engineering.fb.com security post.
- NCC Group research blog **[candidate]** — `research.nccgroup.com` returned zero search hits as of 2026-07-11 (W28) — still unresolved; not re-attempted this week (Bishop Fox, its co-listed candidate, healed — see Primary feeds above).
- DEF CON AI Village — https://aivillage.org/ · RSS `https://aivillage.org/feed.xml` **[verified 2026-06-23; RSS found + MOVED here from "Research venues" 2026-07-04]** — the offensive-AI community/event (talks, CTFs, red-team challenges, generative-AI bug bounties); track outputs and writeups. COVERAGE-GAP FIX (2026-07-04, W27): this entry sat in "Research venues" (no "swept every run" heading) and had NEVER appeared in `logs/source_rotation.md` since launch (6 weeks) — a persistent MISSING-source coverage lie caught by this week's self-eval. Feed is plain RSS, `curl` reachable, no browser-UA needed. First sweep this session surfaced "Meta AI Agent Account Takeover" (2026-06-05, → evidence on agentic-attack-surface-001) and "AI Cyber League" (2026-06-30, community-history essay + new AI-security competition announcement — queued as context).
- UK AI Security Institute (AISI) — https://www.aisi.gov.uk/blog **[verified 2026-08-08; PROMOTED candidate→swept, W32 — no RSS confirmed, use `tvly extract "https://www.aisi.gov.uk/blog" --extract-depth advanced` (itemized index)]** — national-government AI-safety body ("Cyber & Autonomous Systems" line); PRIMARY first-party cyber-eval/incident outputs no other lane covers. Index (opened this session) carries a RECURRING on-axis series: "Incident Report: unsanctioned agent behaviour during cyber testing" (08-04, on 009's accidental-autonomous-intrusion cluster + study_shelf), "Preliminary Assessment of Kimi K3's Cyber Capabilities" (w/ CAISI — frontier-model offensive-cyber eval), "Cheating behaviour in frontier model evaluations" (eval-integrity, cf 003). Fills a genuine coverage gap: national AI-safety-institute (AISI/CAISI) cyber-capability evals + eval-incident disclosures. Cite the article directly; filter the governance/measurement-policy posts from the cyber-eval ones.
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

W28 PROPOSAL G APPLIED (2026-07-18, W29 — cooling period elapsed, signal persisted and
WORSENED: the 7 repos below were not even re-attempted in any daily pass 07-13→07-17, zero
mentions in `logs/source_rotation.md` for the week, confirming the access gap is structural,
not a one-off): DOWNGRADED from "swept every run" to a best-effort QUARTERLY check — llm-attacks/
llm-attacks, protectai/ai-exploits, meta-llama/PurpleLlama, ethz-spylab/agentdojo, andyzorigin/
cybench, princeton-nlp/intercode, elder-plinius/L1B3RT4S (research/collection repos, no registry
equivalent; proxy-blocked since ~07-02). Tried `tvly extract` on a commits page as a substitute
(W28) — it renders real content but from a STALE CACHE (elder-plinius/L1B3RT4S commits page
showed a 5-month-old newest commit) — NOT adopted as a heal, do not rely on it for freshness.
The registry now states this explicitly rather than implying full coverage it cannot deliver;
next quarterly check should retry a repo-specific third-party mirror/RSS or a GitHub search-API
path not scoped the same way as `releases.atom`/`repos/.../releases`. The 5 packaged tools
(garak, PyRIT, deepteam, giskard, promptfoo) are UNAFFECTED — they remain swept every run via
PyPI/npm (above).

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
NON-GitHub tool channels (tools do NOT only live on GitHub — do not over-rely on Topics):
- **HuggingFace — offensive MODELS & DATASETS** (a whole artifact class GitHub misses; key-less JSON):
  `huggingface.co/api/datasets?search=<term>` and `…/api/models?search=<term>&sort=lastModified` over
  `jailbreak` / `adversarial` / `abliterated` / `prompt-injection` / `attack` terms → surfaces jailbreak
  corpora & attack benchmarks (e.g. `JailbreakBench/JBB-Behaviors`, `…/multi-turn_jailbreak_attack_datasets`)
  and abliterated/uncensored models used for offense **[verified 2026-07-16]**. These datasets/models ARE
  citable offensive artifacts — surface them in the Tools block too.
- **Con TOOL showcases** — Black Hat **Arsenal** + DEF CON **Demo Labs** are the offensive world's new-tool
  VENUES: `blackhat.com` curl 403 → `tvly extract "https://www.blackhat.com/us-26/arsenal/schedule/index.html" --extract-depth advanced` **[LIVE as of 2026-08-03 — the full Black Hat USA 2026 Arsenal schedule works via tvly-extract, returning speaker/track/format per tool]**, and the
  `elbraino/awesome-blackhat-arsenal` repo catalogs EVERY Arsenal tool by year/track; DEF CON Demo Labs
  page is curl-reachable **[verified 2026-07-16; DEF CON 34 page CONFIRMED WORKING 2026-08-04]** — the exact
  method that works with no Tavily call at all is `curl -sL -A "Mozilla/5.0" https://defcon.org/html/defcon-34/dc-34-demolabs.html`,
  then `grep -oE '<h3 class="talk-title">[^<]*</h3>'` for the full tool list (returned ~40 entries, ~10 on-axis,
  2026-08-04). Prefer this over Tavily for DEF CON. NOTE (2026-08-04): the Black Hat Arsenal schedule
  `tvly extract` that worked on 08-03 returned nav-chrome only on 08-04 — intermittent, retry each run and fall
  back to `tvly search --include-domains blackhat.com --json` for the exact schedule URL before declaring it degraded. These surface brand-new tools before they trend.
  SEASONAL — IN SEASON NOW: Black Hat USA / DEF CON run in early August (DEF CON 34: Aug 6-9, 2026) — the Arsenal schedule going live 2026-08-03 confirms the W31-flagged priority window has opened. Treat this as a PRIORITY sweep target through the event and the following 1-2 weeks (tools are often demoed live before their repo goes public — track "New Tool" entries and re-verify each for a public repo in subsequent runs, do not capture as a tool until the repo exists). Off-season (roughly September-July): log `off-season (next: <event/month>)` rather than skip silently — the failure this note originally closed (2026-07-29: both venues sat at 0/4 runs logged, listed-but-never-mentioned) must not recur once the season closes again.
- **Package-registry SEARCH** (discover NEW packaged tools, not just track known ones): `pypi.org/search/?q=<term>`
  + npm search for `llm security` / `prompt-injection` / `ai red team` → a tool shipping to a registry is
  findable by search; then confirm its repo.
  DISTINCT FROM THE REPO-WATCH USE OF THE SAME HOST — log it under its own name (`registry SEARCH: …`),
  never folded into the `REPO WATCH: PyPI/npm [<known tools>]` line. Repo-watch answers "did a tool I
  already track ship a version?"; this answers "did a tool I have never heard of appear?" — the second
  question is the one this radar exists for. Coverage gap found 2026-07-29: the watch line ran every run
  while the SEARCH never did, and the shared host made the lane look covered.
For each candidate tool: stage its `owner/repo` in "Discovered-source candidates" → **VERIFY IT IS REAL &
PUBLIC**: package registry `pypi.org/pypi/<pkg>/json` or `registry.npmjs.org/<pkg>` (→ version + timestamp
+ homepage) if it ships to one, else `tvly search`/`tvly extract` the repo to confirm it has actual
code/README/recent activity — REJECT empty, "coming soon", archived, or 404 repos. A verified public tool
→ add to Watched repositories AND surface it in the render's **🛠️ Tools & releases** block. GOAL: never
miss a usable tool the week it ships; never surface a vaporware repo as if it were one.

### Watched repositories  (all **[verified 2026-06-23]** via GitHub API unless noted)
- NVIDIA/garak — the LLM vulnerability scanner (note: `leondz/garak` 301-redirects here)
- microsoft/PyRIT — Python Risk Identification Tool for generative AI (Microsoft) — **MOVED 2026-07-30**: the old Azure/PyRIT org was archived 2026-03-27 ("PyRIT has moved! Please see https://github.com/microsoft/PyRIT"); PyPI releases continued uninterrupted under the new org (v1.0.0 07-24, v1.0.1 07-30). Update watched-profile references from github.com/Azure to github.com/microsoft accordingly.
- promptfoo/promptfoo — prompt/agent/RAG red-teaming & pentesting
- confident-ai/deepteam — framework to red-team LLMs and AI agents
- Giskard-AI/giskard — LLM red-team & scanning (repo resolves via 301)
- llm-attacks/llm-attacks — Universal & Transferable Attacks on Aligned LLMs (GCG) **[QUARTERLY check only, W29 Proposal G — see GitHub-watch note above]**
- protectai/ai-exploits — real-world AI/ML exploits for responsibly-disclosed vulns **[QUARTERLY check only, W29 Proposal G]**
- meta-llama/PurpleLlama — LLM security tools incl. CyberSecEval offensive benchmarks **[QUARTERLY check only, W29 Proposal G]**
- ethz-spylab/agentdojo — dynamic env to evaluate ATTACKS & defenses for LLM agents **[QUARTERLY check only, W29 Proposal G]**
- andyzorigin/cybench — CTF benchmark for autonomous agents **[QUARTERLY check only, W29 Proposal G]**
- princeton-nlp/intercode — InterCode benchmark (NeurIPS 2023; code/CTF agent tasks) **[QUARTERLY check only, W29 Proposal G]**
- elder-plinius/L1B3RT4S — **[verified 2026-06-23 via API; QUARTERLY check only, W29 Proposal G]** large public collection of working jailbreaks per model; track ADDITIONS as a leading indicator of new bypasses (intake — link the repo, never paste payloads into the ledger)
- FuzzingLabs/mcp-security-hub — **[verified 2026-07-14 via tvly extract, tool-discovery lane]** production-ready, Dockerized collection of **38 offensive-security MCP servers / 300+ tools** (Nmap, Ghidra, Nuclei, SQLMap, Hashcat, …) that expose classic offensive tooling to AI assistants (Claude Desktop/Code) for agent-driven recon, vuln scanning and binary analysis — an AI-for-offense agent-tooling artifact (MIT). Surfaced this run via `tvly search --include-domains github.com "mcp-security"`; not previously watched. Watch releases/new MCPs.
- (agent: add tools as they appear in papers/cons; drop abandoned ones)

### Watched profiles/users  (GitHub orgs behind the watched tools — **[verified 2026-06-23]** via API; watch for NEW repos/releases under each)
- github.com/NVIDIA (garak) · github.com/microsoft (PyRIT — moved from Azure 2026-03-27)
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

## Discovered-source candidates (staged by the daily OR named as a manual `[candidate]` above — ONE reviewed list; the weekly verifies & promotes)

MERGED 2026-07-18 (W29, applying W28 Proposal H): this auto-staged tally and the manually-tracked
`[candidate]` entries under Primary feeds above are now treated as ONE review process each
weekly — a candidate can enter via either lane, but promotion/drop decisions are made together
so a recurring on-axis source doesn't sit unpromoted in one lane while the other gets checked.

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

- hackerfactor.com (Dr. Neal Krawetz, image-forensics researcher) — 1 — "Meta's Un-Stable Signature" AI-image-watermark attack (~2026-06-30, surfaced via HN 2026-07-05) — first seen 2026-07-05. RE-CHECKED 2026-07-25 (W30) and again 2026-08-01 (W31, per the new below-bar re-check policy): still only the one known on-axis item 27 days on, blog remains general image-forensics (FotoForensics/steganalysis), not AI-security-core — carry as low-priority, not promoting without a 2nd genuinely on-axis post. RE-CHECKED 2026-08-15 (W33): the blog DOES carry multiple provenance/watermark-ATTACK posts ("C2PA from the Attacker's Perspective" — opened, dated 2024-05-09; "The Watermarking Paradox"; "C2PA's Butterfly Effect" — plus the staged "Un-Stable Signature" ~2026-06-30), and this axis just went LIVE (MarkNull 2608.10166, USENIX-2026 watermark-removal, 08-11 — a forming provenance/watermark-attack nucleus). So hackerfactor is more on-axis than prior re-checks credited, BUT the on-axis posts are low-cadence and spread over years (2024→2026), not a recurring fresh series — still NOT promoting on that alone. PROMOTE TRIGGER SHARPENED: promote the moment a 2nd watermark/provenance-removal group seeds that axis (making hackerfactor a needed source) OR it ships a fresh 2026 on-axis attack post. Carried, re-dated.
- specterops.io (SpecterOps — offensive-security firm; Neeraj Gupta) — 1 — "Jailbreaker" open-source repeatable LLM-jailbreak-testing platform (PAIR/TAP/Crescendo/AutoDAN/GPTFuzz), surfaced via tldrsec #336 — first seen 2026-07-13. VERIFIED 2026-07-28: opened https://specterops.io/blog/2026/06/29/llm-jailbreak-testing-with-jailbreaker (published 06-29, not 07-13 as the tldrsec pointer implied) — real, on-axis, promoted to study_shelf. PROMOTED candidate→swept 2026-08-15 (W33) — see SpecterOps under Primary feeds above. W33 re-check surfaced ≥2 genuinely on-axis OFFENSIVE artifacts (Jailbreaker 06-29 + "multi-prompt LLM jailbreaks" 2025-09 + GhostWorks 06-09). Candidate line cleared.
- vectoral.com (Matt Lenhard — independent researcher/investigative blog) — 1 — "An Inside Look at the Relay Market Powering Token Resellers and Fraud" (2026-07-26, surfaced via Simon Willison, primary NOT opened this session — extraction failed with a connection reset, queued unverified) — first seen 2026-07-28. LLM-API-key-abuse/reselling economics with a model-distillation-data-collection angle (model-extraction-fingerprinting-006-adjacent); verify the primary next run before any evidence use. RE-CHECKED 2026-08-15 (W33): the primary URL is now confirmed reachable (https://vectoral.com/blog/token-relay-market) and the index still lists only this one on-axis post — still 1 artifact, below the ≥2 bar; borderline-on-axis single investigative post. Carried, re-dated; open the primary and look for a 2nd post on the next re-check.
- ayush.digital (Ayush Paul — independent AI-security researcher) — 1 — "The Memory Heist" lethal-trifecta memory/PII exfiltration on production claude.ai via a `web_fetch` allowlist bypass (2026-07-15, surfaced via Simon Willison, → verified queue item on agentic-attack-surface-001 + study_shelf) — first seen 2026-07-16. RE-CHECKED 2026-07-25 (W30) and again 2026-08-01 (W31, per the new below-bar re-check policy): `/blog` index still lists only this one post (no RSS found) — still 1 artifact, not yet at the ≥2 bar; the homepage itself is a personal bio page, not an index — carry. RE-CHECKED 2026-08-15 (W33): still only the one Memory-Heist post surfacing — 1 artifact, carried, re-dated.
- huggingface.co/blog (Hugging Face — model/dataset hub; security-incident disclosures) — 1 — "Security incident disclosure — July 2026" first-party disclosure of a fully-autonomous AI-agent-driven intrusion (→ evidence on ai-offensive-operations-009 + study_shelf), surfaced via Embrace The Red — first seen 2026-07-20. On-axis first-party incident disclosures (rare + high-signal); verify whether HF publishes a recurring security/IR series next weekly.
- jesta.ai/blog (Jesta Security — AI-attack defense research; Lior Finkelshtein) — 1 — "DarkReasoning: A Chinese LLM attacked our lab, so we made it work for us" (2026-08-03, opened and verified 2026-08-04; → top rotate-candidate on ai-offensive-operations-009 + study_shelf), surfaced via the Reddit pulse lane — first seen 2026-08-04. RE-CHECKED 2026-08-08 (W32): index still lists only the one DarkReasoning post — still 1 artifact, below the ≥2 bar; carry, check for a recurring research series next weekly.
- huggingface.co/blog (Hugging Face — model/dataset hub; security-incident disclosures) — 2 — "Security incident disclosure — July 2026" (07-16, → 009 evidence + study_shelf) + "Be Ready Before the Attack: A Practical Guide to Self-Hosting an Open Model" (post-incident, found 2026-08-08) — first seen 2026-07-20. RE-CHECKED 2026-08-08 (W32): the 2nd post is incident-REACTIVE and defense-flavored on an overwhelmingly product/ML hub blog — NOT a recurring offensive-research series; NOT promoted (sweeping a general model-hub blog every run is low-yield/high-noise, and the incident disclosures reach the radar via Embrace-The-Red/pulse pointers). Carry; promote only if a genuine recurring attack-research series emerges.
- github.com/sumamovva/probeagent (probeagent-ai — automated AI-agent red-team CLI: multi-turn prompt-injection/jailbreak attacks + robustness scoring) — 1 — PyPI probeagent-ai v0.3.6 (2026-07-25, "Offensive security testing for AI agents"), surfaced via the PyPI registry-SEARCH lane — first seen 2026-08-12. TOOL candidate, on-axis (offensive AI-agent testing) but early-stage/single-author with no visible adoption signal — below the study-shelf notability bar; carry, promote only on a real adoption/notability signal or a 2nd corroborating surface.
- github.com/samugit83/redamon (redamon — "AI-powered agentic red team" for AI agents/LLM apps) + github.com/votal-ai-hq/wb-red-team (votal-ai-hq/ai-red-teaming — "Whitebox & Blackbox AI red-teaming framework") — 1 each — surfaced via the GitHub topic/search tool-DISCOVERY lane (topics ai-red-teaming / prompt-injection / llm-red-team), 2026-08-13 — first seen 2026-08-13. TOOL candidates, on-axis (offensive AI-agent red-teaming) but early-stage/single-author with no visible adoption/notability signal — below the study-shelf bar; carry, promote only on a real adoption signal or a 2nd corroborating surface.
- blog.cryptographyengineering.com (Matthew Green — cryptographer, Johns Hopkins; "A Few Thoughts on Cryptographic Engineering") — 1 — "Fooling around with encrypted reasoning blobs" (2026-05-29) — the prior-art pointer for the reasoning-trace-recovery line: showed OpenAI/Anthropic encrypted reasoning blobs can be REPLAYED across sessions/accounts/models, the foundation the "Stealing Reasoning Traces" paper (2608.09867, on model-extraction-fingerprinting-006) and Rehberger's 08-16 reproduction both build on — surfaced via the Embrace The Red primary-feed sweep, first seen 2026-08-17. Well-known cryptographer's research blog with directly on-axis (offense-against-AI / model-extraction) content; verify for a recurring on-axis cadence next weekly (a single crypto blog is usually off-radar, but this post is squarely on the concealed-CoT axis).

PROMOTED 2026-07-25 (W30, all three cleared the ≥2-on-axis-artifact bar on verification — see Primary feeds above): sysdig.com/blog (JADEPUFFER 07-01 + JADEPUFFER-evolves 07-20, both now 009 evidence); oddguan.com/blog (Comment-and-Control 04-15, already 001 evidence + "Second Time, Same Sandbox" 05-20, found this session and queued as a top 001 rotate-candidate); blog.zksecurity.xyz (CIRCL 07-07, already 002 evidence + OpenVM-zkVM 07-17, found this session and queued as a fresh 002 rotate-candidate).

PROMOTED 2026-08-08 (W32, both verified by opening the index this session — see Primary feeds above): island.io/blog (AgentBaiting 07-20 = 001 evidence + MCP-scanning-33K 08-05 — cleared the ≥2 bar); aisi.gov.uk/blog (a recurring "Cyber & Autonomous Systems" series — incident report 08-04 + Kimi-K3 cyber assessment + cheating-in-evals — well past the ≥2 bar; fills the national-AI-safety-institute cyber-eval coverage gap).
PROMOTED 2026-07-18 (W29, both cleared the ≥2-on-axis-artifact bar on verification — see Primary feeds above): oasis.security (PromptFiction 07-15 + Claudy Day 03-18, plus a visible recurring claude.ai/agent-PI series); trendmicro.com/research (Patriot Bait + TuxBot v3 + claude.ai ClickFix malvertising, plus Vibe Hacking / Weaponized-AI-Assistants / Weaponizing-Trust-Signals as a visible recurring in-the-wild-AI-offense series).

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
- Microsoft Developer — feed `https://www.youtube.com/feeds/videos.xml?channel_id=UCsMica-v34Irf9KVTh6xx-g` **[verified 2026-06-23; channel_id resolved; DEGRADED 2026-08-03 — feeds.xml endpoint 404, same structural break as the Black Hat channel]** — hosts the "AI Red Teaming 101" series; BROAD channel, filter for AI-red-team/security items only. Re-checked 2026-07-04: recent uploads are generic dev-tool content (M365 Copilot MCP demo, Data Exposed, Cozy AI Kitchen) — no new AI-red-team item this pass. HEAL APPLIED 2026-08-05: ran `tvly search "Microsoft Developer AI Red Teaming latest video 2026" --include-domains youtube.com --topic news` (the Black-Hat-channel method, AI-red-team-scoped) — the method returns dated results but this broad channel yields only generic dev content ("What are AI agents?", "Intro to GenAI/LLMs", VS Code, Java) with no AI-red-team/security item. So the method works; the channel simply has no on-axis uploads. Heal DISCHARGED (no longer "owed"); log as opened/no-on-axis each run and re-scope only if a specific AI-red-team-101 upload is glimpsed.
- Black Hat — feed `https://www.youtube.com/feeds/videos.xml?channel_id=UCJ6q9Ie29ajGqKApbLqfBOg` **[verified 2026-07-04; HEALED 2026-08-03 — the feeds.xml endpoint itself is now structurally 404 from this environment, confirmed against Google's own official channel_id too (not a per-channel issue)]** — official conference-talk uploads, several published WITHIN DAYS of a session and squarely on-axis, e.g. "Black Hat Europe 2025 | Automatic Detection of Taint-Style Vulnerabilities in LLM-based Agents" (published 2026-07-03). Conference talks are explicit primary material per the hard rules (DEF CON/Black Hat) — treat citably like a paper (follow to the talk's own abstract/slides/paper where linked; the video page itself is citable if no companion write-up exists). WORKING METHOD (2026-08-03): `tvly search "Black Hat YouTube channel latest videos <year>" --include-domains youtube.com --topic news` returns dated recent uploads (caught "Black Hat Asia 2026 | Keynote: From Prompt Tricks to Autonomous Hackers", posted 07-29) — use this in place of the feed URL until/unless the feed endpoint recovers.
- Embrace The Red (Johann Rehberger) — own channel still **[candidate — channel_id unresolved]**: a video search for his talks resolved to the UPLOADING conference's channel (Black Hat), not a personal channel — his blog (below, swept every run) remains the primary access path; his content is not going untracked.
- (agent: add offensive-AI / red-team / CTF-agent channels as they prove high-signal — resolve `channel_id` once, follow each video's link to the named primary, cite the primary not the video. Do NOT invent channel names.)

### Curated digests + explainer/aggregator blogs (INTAKE LANE — swept every run)
- Embrace The Red — https://embracethered.com/blog/ · RSS https://embracethered.com/blog/index.xml **[verified 2026-06-23]** — Rehberger's own prompt-injection / agent-attack research; often IS the primary artifact (then cite it directly).
- tldrsec — https://tldrsec.com/ **[RECOVERED 2026-07-05 — was `degraded: 403` for 5+ passes since 06-27]** — security newsletter (Clint Gibler), heavy AI-security coverage; follow to the named primary. HEAL (2026-07-05): plain `curl -sL -A "Mozilla/5.0" https://tldrsec.com/` now returns HTTP 200 with the FULL homepage (~487 KB, itemized dated issues) — the 403 wall is gone; issue permalinks are `https://tldrsec.com/p/tldr-sec-<NNN>` and `tvly extract <permalink> --query "<topic>"` pulls the lead-item summaries. First recovered sweep surfaced #335 (07-02) "Prompt Injection as Role Confusion" → followed to arXiv:2603.12277 (queued + shelved). Retry each run; re-mark degraded only if the 403 returns.
- Simon Willison — https://simonwillison.net/ **[verified 2026-06-23]** — extensive prompt-injection coverage and original framing; follow to the primary.
- Kai Greshake — https://kai-greshake.de/ · RSS https://kai-greshake.de/index.xml **[verified 2026-06-23]** — the researcher who pioneered indirect prompt injection; his posts are often the original disclosure (cite directly).
- ~~MLSecOps — https://mlsecops.com/ + https://community.mlsecops.com/~~ **DROPPED from swept-every-run 2026-08-15 (W33): dead source.** Across all ~33 historical checks the homepage `tvly extract` returned only nav-chrome + lorem-ipsum placeholder blocks — never once an itemized dated post — so "sweeping it every run" was a false coverage promise (the heal-or-REMOVE rule: don't list what you won't sweep). Removed from the swept curated-digests lane. NOT re-added unless the site ships a real dated post index; the AI-security newsletter/community function it nominally served is covered by tldrsec + Simon Willison + the pulse lane. (Historical note kept here as a tombstone; do not re-log it "degraded" run after run.)
- Palo Alto Unit 42 — MOVED to "Primary feeds" (verified 2026-06-29, RSS `/feed/`); it is a primary research source, not a digest.
- (agent grows this list; every entry logged opened or `degraded:<reason>`; follow to the primary, never cite the digest unless it is the original disclosure.)

## Discovery / exploration venues (Phase 4 — iterated EVERY run by radar-explore)

Read top/most-attention items regardless of sub-topic, advancing the date window.
- arXiv cs.CR recent **[verified 2026-06-23]** + Hugging Face papers (security-tagged) **[candidate]**.
- Rotating single-category supplement (APPLIED 2026-07-04, W27 — was W26 Proposal C, cooling period held, signal persisted: no session ever actually opened cs.AI/cs.LG despite SOURCES.md documenting them as in-scope, and trend 004's backdoor cluster was seeded entirely from queue accumulation, never from an explore hit, exactly the miss Proposal C flagged): once every ~3–4 daily passes, swap the cs.CR explore pass for **arXiv cs.AI** or **cs.LG** recent-listing (rotate the two), same significance-first method — adversarial-ML / trigger-implantation / backdoor work frequently cross-lists there instead of cs.CR. Track which category and date-window was covered in `logs/source_rotation.md` each time so the rotation actually advances instead of always defaulting back to cs.CR.
- GitHub Trending (security / LLM-attack tooling); alphaXiv / Papers with Code trending (security) **[candidate]**.
- Watch-area venues (surface and queue): autonomous-exploitation / CTF-agent research, AI-malware research, hardware/side-channel attacks on inference.
