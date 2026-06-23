# Sources registry — AI Security Radar

Agent-owned registry of monitored sources for the **offensive AI-security** beat.
The radar maintains and evolves this file itself (add/remove/mark-dead entries, with
a one-line reason in the day's or week's report) — no curator sign-off needed. Skills
describe the *method*; this file is the *data* (the lists the skills iterate by force).

Hard-rule reminder: papers, tool repos, vendor/lab security blogs, CVEs/advisories and
standards are PRIMARY sources (citable evidence). Social/community sources are an INTAKE
LANE ONLY — never evidence; when a social signal links to or names a primary artifact,
follow the link and verify the artifact (that artifact, not the post, becomes evidence).
Track and cite; never invent URLs/dates. A source listed under a "swept every run"
heading is a coverage PROMISE — log it opened or `degraded: <reason>` every run.

---

## Primary feeds — vendor/lab security blogs & advisories (Phase 1 — swept EVERY run)

Method: `radar-lab-sweep` skill (a primary-feed sweep). Prefer RSS/Atom; open only
posts newer than the last scan. Filter for OFFENSIVE relevance (attack techniques,
red-team tooling, exploitation research) — skip pure product/marketing.

- Microsoft — MSRC blog https://msrc.microsoft.com/blog/ + AI Red Team https://www.microsoft.com/en-us/security/blog/ (PyRIT) (verify feeds)
- Google — Project Zero https://googleprojectzero.blogspot.com/ (Atom) + Threat Intelligence (GTIG) https://cloud.google.com/blog/topics/threat-intelligence + DeepMind security posts
- NVIDIA — developer/security blog (garak, AI red team) https://developer.nvidia.com/blog/ (verify feed)
- Meta — AI red team / Purple Llama https://ai.meta.com/blog/ (verify; HTML extract if no feed)
- OpenAI — red-teaming / preparedness posts https://openai.com/news/ (RSS; filter offensive)
- Anthropic — red-team / jailbreak-robustness research https://www.anthropic.com/research (HTML extract; no public RSS as of setup)
- Trail of Bits https://blog.trailofbits.com/ (RSS) — AI/ML offensive security
- NCC Group / research blogs, Bishop Fox, Protect AI (huntr.com) — AI/ML attack research (verify feeds)
- Advisory feeds: NVD https://services.nvd.nist.gov/rest/json/cves/2.0 ; GitHub advisories (GHSA) for AI tooling; Protect AI huntr disclosures.

## Research venues — arXiv & security conferences (primary)

- arXiv — **cs.CR** (core), plus cs.AI / cs.LG / cs.CL for attack-on-model work. Metadata via `export.arxiv.org/api/query?id_list=...`.
- Conferences (proceedings/preprints): USENIX Security, IEEE S&P (Oakland), ACM CCS, NDSS.
- Offensive cons (talk/whitepaper archives): DEF CON, Black Hat (AI/ML tracks), Offensive-security writeups.
- Standards & taxonomies (track changes/additions): OWASP LLM Top 10 + Agentic Security, MITRE ATLAS, NIST AI RMF / adversarial-ML taxonomy.

## GitHub watch (Phase 5 — repos, profiles, and fork trees)

Method: `radar-repo-watch`. Watch releases (`<repo>/releases.atom`), notable forks, and
profile activity for published offensive/red-team AI-security tools. New releases/tools
are citable artifacts; issue/PR/fork/profile movement is a queue signal. (Agent owns and
grows these lists.)

### Watched repositories
- garak (NVIDIA) — LLM vulnerability scanner
- PyRIT (Microsoft) — automated red-teaming for genAI
- promptfoo — red-team / eval harness (jailbreak/injection probes)
- giskard / deepteam — LLM red-team & scanning
- llm-attacks / GCG and successor adversarial-suffix repos (research)
- prompt-injection & agent-exploitation PoC repos (research, as published)
- LLM fuzzers / automated jailbreak-search frameworks (research)
- (agent: add tools as they appear in papers/cons; drop abandoned ones)

### Watched profiles/users
- (seed with orgs/researchers who ship offensive AI-security tooling — Microsoft, NVIDIA,
  Protect AI, Trail of Bits, and individual maintainers — as discovered; track new repos
  and releases under them)

### Fork-tree analysis
- For high-signal tool repos, scan notable forks (depth ~3, scored by stars/recency) — a
  diverging fork is often where a new offensive capability first appears.

## Social & community channels (Phase 2 — INTAKE ONLY, never evidence)

Method: `radar-pulse`. Best-effort via Tavily / public APIs. Intake feeds
`observation_queue` (unverified) + the pulse note; never name/quote individuals beyond
a bare URL. The earthquake check is multi-channel (don't collapse to one).
- Reddit: r/netsec, r/MachineLearning, r/LocalLLaMA, r/ChatGPTJailbreak, r/hacking, r/AskNetsec
- Hacker News — via Algolia API `https://hn.algolia.com/api/v1/search?tags=front_page` (+ `query=<term>`)
- Security research curators / newsletters / YouTube channels (agent-curated; follow to the primary, cite the primary, never the curator)

### YouTube — TRUSTED-CURATOR POINTER LANE (check EVERY run, intake only)
- (seed with offensive-AI / red-team channels as found; resolve each to its `channel_id` once, then use `https://www.youtube.com/feeds/videos.xml?channel_id=UC…`)

### Curated digests + explainer/aggregator blogs (INTAKE LANE — swept every run)
- AI-security / adversarial-ML newsletters and aggregators (follow to the named primary, verify, cite the primary, never the digest). Agent grows this list; every entry is logged opened or `degraded:<reason>`.

## Discovery / exploration venues (Phase 4 — iterated EVERY run by radar-explore)

Where NEW / not-yet-tracked offensive work surfaces; read top/most-attention items
regardless of sub-topic.
- arXiv cs.CR recent listing (advancing date window) + Hugging Face papers (security-tagged).
- GitHub Trending (security / LLM-attack tooling); alphaXiv / Papers with Code trending (security).
- Watch-area venues (surface and queue): autonomous-exploitation / CTF-agent research, AI-malware research, hardware/side-channel attacks on inference.
