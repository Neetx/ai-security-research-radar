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
- NVIDIA — cybersecurity category Atom https://developer.nvidia.com/blog/category/cybersecurity/feed/ **[verified 2026-06-23]** (garak / AI red team)
- Microsoft Security blog — https://www.microsoft.com/en-us/security/blog/ · feed `/feed/` (rss+xml) **[verified 2026-06-23]** (AI Red Team / PyRIT posts)
- Microsoft MSRC blog — https://msrc.microsoft.com/blog/ — NO clean RSS (the `/blog/feed/` path returns HTML, checked 2026-06-23) → fetch via `tvly extract`
- OpenAI — https://openai.com/news/ · RSS `/news/rss.xml` (text/xml) **[verified 2026-06-23]** — filter for red-teaming / preparedness items
- Anthropic — https://www.anthropic.com/research — NO public RSS (`/news/rss.xml` 404, checked 2026-06-23) → `tvly extract`; track jailbreak-robustness / red-team research
- Google Threat Intelligence (GTIG) — https://cloud.google.com/blog/topics/threat-intelligence **[candidate]** (verify feed on first sweep)
- Protect AI — huntr disclosures & blog https://protectai.com/ + https://huntr.com/ **[candidate]** (AI/ML vuln disclosures)
- Meta — Llama / AI security https://ai.meta.com/blog/ **[candidate]** (HTML extract if no feed)
- NCC Group / Bishop Fox research blogs **[candidate]** (AI/ML offensive research; verify feeds)
- Advisory feeds: NVD API https://services.nvd.nist.gov/rest/json/cves/2.0 **[verified 2026-06-23]** ; GitHub advisories (GHSA) for AI tooling **[candidate]**

## Research venues — arXiv & security conferences (primary)

- arXiv — **cs.CR** (core) https://arxiv.org/list/cs.CR/recent **[verified 2026-06-23]**, plus cs.AI / cs.LG / cs.CL for attack-on-model work. Metadata via `export.arxiv.org/api/query?id_list=...`.
- Conferences (proceedings/preprints) **[candidate]**: USENIX Security, IEEE S&P (Oakland), ACM CCS, NDSS; offensive cons (DEF CON, Black Hat AI/ML tracks).
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
- (agent: add tools as they appear in papers/cons; drop abandoned ones)

### Watched profiles/users
- **[candidate]** orgs/maintainers that ship offensive AI-security tooling — NVIDIA,
  Microsoft (Azure), Protect AI, Trail of Bits, ETH SPY Lab — track new repos/releases.

### Fork-tree analysis
- For high-signal tool repos, scan notable forks (depth ~3, scored by stars/recency) — a
  diverging fork is often where a new offensive capability first appears.

## Social & community channels (Phase 2 — INTAKE ONLY, never evidence)

Method: `radar-pulse`. Intake feeds `observation_queue` (unverified) + the pulse note;
never name/quote individuals beyond a bare URL. Multi-channel earthquake check.
NOTE: Reddit blocks direct API from this setup (`about.json` → 403, checked 2026-06-23) —
reach subs via Tavily, not `.json`.
- Reddit (via Tavily): r/netsec, r/MachineLearning, r/LocalLLaMA, r/ChatGPTJailbreak, r/hacking, r/AskNetsec  **[candidate — confirm each resolves]**
- Hacker News — Algolia API https://hn.algolia.com/api/v1/search?tags=front_page (+ `query=<term>`) **[verified pattern; known reliable]**

### YouTube — TRUSTED-CURATOR POINTER LANE (check EVERY run, intake only)
- **[candidate]** seed with offensive-AI / red-team channels as found; resolve each to its `channel_id` once, then use `https://www.youtube.com/feeds/videos.xml?channel_id=UC…`.

### Curated digests + explainer/aggregator blogs (INTAKE LANE — swept every run)
- **[candidate]** AI-security / adversarial-ML newsletters & aggregators — follow to the named primary, verify, cite the primary, never the digest. Agent grows this list; every entry logged opened or `degraded:<reason>`.

## Discovery / exploration venues (Phase 4 — iterated EVERY run by radar-explore)

Read top/most-attention items regardless of sub-topic, advancing the date window.
- arXiv cs.CR recent **[verified 2026-06-23]** + Hugging Face papers (security-tagged) **[candidate]**.
- GitHub Trending (security / LLM-attack tooling); alphaXiv / Papers with Code trending (security) **[candidate]**.
- Watch-area venues (surface and queue): autonomous-exploitation / CTF-agent research, AI-malware research, hardware/side-channel attacks on inference.
