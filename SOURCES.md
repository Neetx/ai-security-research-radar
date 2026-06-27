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
- NVIDIA — cybersecurity category Atom https://developer.nvidia.com/blog/category/cybersecurity/feed/ **[verified 2026-06-23]** (garak / AI red team). NOTE (2026-06-27): individual article URLs (developer.nvidia.com/blog/<slug>) are blocked by the proxy — ONLY the Atom feed URL above works. Do not attempt to `tvly extract` individual article URLs; `degraded: article-URL-blocked`.
- Microsoft Security blog — https://www.microsoft.com/en-us/security/blog/ · feed `/feed/` (rss+xml) **[verified 2026-06-23]** (AI Red Team / PyRIT posts)
- Microsoft MSRC blog — https://msrc.microsoft.com/blog/ — NO clean RSS, AND a JS-rendered SPA: `tvly extract` (even `--extract-depth advanced`) returns only nav chrome, no post bodies (checked 2026-06-23 Pass 2, 2nd failure). HEAL: do not rely on the blog index; surface MSRC items via `tvly search --include-domains msrc.microsoft.com` for the topic, or via the Microsoft Security blog feed which carries most AI-security items. Mark `degraded: SPA, search-only`.
- OpenAI — https://openai.com/news/ · RSS `/news/rss.xml` (text/xml) **[verified 2026-06-23]** — filter for red-teaming / preparedness items
- Anthropic — https://www.anthropic.com/research — NO public RSS (`/news/rss.xml` 404). HEAL (2026-06-23 Pass 2): `tvly extract "https://www.anthropic.com/research" --extract-depth advanced` yields the dated publication index (Frontier Red Team items: N-days, exploit-development, LLM ATT&CK Navigator); follow each to its `/research/<slug>` article and extract that to cite. **[verified 2026-06-23]**
- Google Threat Intelligence (GTIG) — https://cloud.google.com/blog/topics/threat-intelligence **[candidate]** (verify feed on first sweep)
- Protect AI — huntr disclosures & blog https://protectai.com/ + https://huntr.com/ **[candidate]** (AI/ML vuln disclosures)
- Meta — Llama / AI security https://ai.meta.com/blog/ **[candidate]** (HTML extract if no feed)
- NCC Group / Bishop Fox research blogs **[candidate]** (AI/ML offensive research; verify feeds)
- Advisory feeds: NVD API https://services.nvd.nist.gov/rest/json/cves/2.0 **[verified 2026-06-23]** ; GitHub advisories (GHSA) for AI tooling **[candidate]**

## Research venues — arXiv & security conferences (primary)

- arXiv — **cs.CR** (core) https://arxiv.org/list/cs.CR/recent **[verified 2026-06-23]**, plus cs.AI / cs.LG / cs.CL for attack-on-model work. Metadata via `export.arxiv.org/api/query?id_list=...`.
- Conferences (proceedings/preprints) **[candidate]**: USENIX Security, IEEE S&P (Oakland), ACM CCS, NDSS; offensive cons (DEF CON, Black Hat AI/ML tracks).
- DEF CON AI Village — https://aivillage.org/ **[verified 2026-06-23]** — the offensive-AI community/event (talks, CTFs, red-team challenges, generative-AI bug bounties); track outputs and writeups.
- Standards & taxonomies (track changes/additions): OWASP GenAI / LLM Top 10 https://genai.owasp.org/llm-top-10/ **[verified 2026-06-23]** ; MITRE ATLAS https://atlas.mitre.org/ **[verified 2026-06-23]** ; NIST AI RMF / adversarial-ML taxonomy **[candidate]**.

## GitHub watch (Phase 5 — repos, profiles, and fork trees)

Method: `radar-repo-watch`. Watch releases (`<repo>/releases.atom`), notable forks, and
profile activity. New releases/tools are citable artifacts; issue/PR/fork/profile movement
is a queue signal. (Agent owns and grows these lists.)

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

- (empty — the daily fills this; the weekly drains it)

## Social & community channels (Phase 2 — INTAKE ONLY, never evidence)

Method: `radar-pulse`. Intake feeds `observation_queue` (unverified) + the pulse note;
never name/quote individuals beyond a bare URL. Multi-channel earthquake check.
NOTE: Reddit blocks direct API from this setup (`about.json` → 403, checked 2026-06-23) —
reach subs via Tavily, not `.json`. Additionally, Tavily Reddit searches also failed across multiple attempts in W26 (all subreddits returned 0 results or timeout) — `degraded: Tavily-Reddit-fail (2026-06-27)`; cross-channel pulse via HN + arXiv + curators provides redundancy. Retry on next pass; if 2+ more weeks fail, downgrade to intermittent.
- Reddit (`degraded: Tavily-Reddit-fail 2026-06-27` — retry each pass): r/netsec, r/MachineLearning, r/LocalLLaMA, r/hacking, r/AskNetsec (well-known active subs); r/ChatGPTJailbreak (jailbreak community). Read TOP + earthquake check.
- Hacker News — Algolia API https://hn.algolia.com/api/v1/search?tags=front_page (+ `query=<term>`) **[verified pattern; known reliable]**

### YouTube — TRUSTED-CURATOR POINTER LANE (check EVERY run, intake only)
- Microsoft Developer — feed `https://www.youtube.com/feeds/videos.xml?channel_id=UCsMica-v34Irf9KVTh6xx-g` **[verified 2026-06-23; channel_id resolved]** — hosts the "AI Red Teaming 101" series; BROAD channel, filter for AI-red-team/security items only.
- Embrace The Red (Johann Rehberger) — channel exists; **[candidate — resolve `channel_id` on first use]**. On-topic: prompt injection / AI agent attacks.
- (agent: add offensive-AI / red-team / CTF-agent channels as they prove high-signal — resolve `channel_id` once, follow each video's link to the named primary, cite the primary not the video. Do NOT invent channel names.)

### Curated digests + explainer/aggregator blogs (INTAKE LANE — swept every run)
- Embrace The Red — https://embracethered.com/blog/ · RSS https://embracethered.com/blog/index.xml **[verified 2026-06-23]** — Rehberger's own prompt-injection / agent-attack research; often IS the primary artifact (then cite it directly).
- tldrsec — https://tldrsec.com/ `degraded: 403 all access methods (tvly extract, search, domain filter) — 5+ consecutive passes as of 2026-06-27; HEAL NEEDED` — security newsletter (Clint Gibler), heavy AI-security coverage; follow to the named primary. (Was **[verified 2026-06-23]** via HTML extract but now blocked.)
- Simon Willison — https://simonwillison.net/ **[verified 2026-06-23]** — extensive prompt-injection coverage and original framing; follow to the primary.
- Kai Greshake — https://kai-greshake.de/ · RSS https://kai-greshake.de/index.xml **[verified 2026-06-23]** — the researcher who pioneered indirect prompt injection; his posts are often the original disclosure (cite directly).
- MLSecOps — https://mlsecops.com/ + https://community.mlsecops.com/ `degraded: extract/search fail — 3+ consecutive passes as of 2026-06-27; HEAL NEEDED` — ML/AI-security community & content hub (Protect AI-affiliated); follow to the primary. (Was **[verified 2026-06-23]** but now fails.)
- Palo Alto Unit 42 — https://unit42.paloaltonetworks.com/ **[candidate]** — threat-intel research on in-the-wild prompt injection / agent attacks (verify feed on first sweep).
- (agent grows this list; every entry logged opened or `degraded:<reason>`; follow to the primary, never cite the digest unless it is the original disclosure.)

## Discovery / exploration venues (Phase 4 — iterated EVERY run by radar-explore)

Read top/most-attention items regardless of sub-topic, advancing the date window.
- arXiv cs.CR recent **[verified 2026-06-23]** + Hugging Face papers (security-tagged) **[candidate]**.
- GitHub Trending (security / LLM-attack tooling); alphaXiv / Papers with Code trending (security) **[candidate]**.
- Watch-area venues (surface and queue): autonomous-exploitation / CTF-agent research, AI-malware research, hardware/side-channel attacks on inference.
