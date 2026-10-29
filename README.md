# AI Security Radar

![trends](https://img.shields.io/badge/trends-18-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-10-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-14-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--10--29-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-10-28):**
- 🚀 **New evidence — [in-the-wild AI-for-offense](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2):** [Microsoft: Storm-0940 uses ARTEX agentic AI](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/) — a China-state-aligned actor weaponized the **public open-source autonomous-pentest framework ARTEX** (recon→exfiltration "with little needed human interaction") against hundreds of orgs incl. the ConnectWise supply-chain compromise; corroborated independently by [Wiz](https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors) and [Huntress](https://www.huntress.com/blog/connectwise-attack-ai) — a public pentest tool turned nation-state weapon at scale.
- 🚀 **New evidence — [LLM/agentic vuln discovery](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code):** CrowdStrike's [When AI Guardrails Expose Vulnerabilities](https://www.crowdstrike.com/en-us/blog/when-ai-guardrails-expose-vulnerabilities/) — **GbVD**: a frontier model's own safety **refusal** is used as a vuln-discovery oracle (bisection narrows refusals to the smallest flawed unit; 73/86 across five vuln classes, real OSS disclosed via CVD).
- 🔭 **Study pick:** [XBOW Built a Chrome Full-Chain Exploit Affecting a Billion Users in Six Days](https://xbow.com/blog/xbow-built-a-chrome-full-chain-exploit) — XBOW's AI chained three unknown bugs (V8 / WebP decoder / Crashpad) into a full-chain sandbox escape in six days (~$40K API), earning Google's first $250K full-chain Chrome VRP award.

---

## Trends

🌱 1 · 📈 4 · 🚀 10 · 🌊 0 · 🏔 0 · 📉 0 · 💤 3

| trend | stage | latest signal |
|---|---|---|
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-10-28](https://www.crowdstrike.com/en-us/blog/when-ai-guardrails-expose-vulnerabilities/) |
| [Attacks on LLM-agent stack: MCP, memory, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-10-27](https://aviatrix.ai/threat-research-center/in-the-wild-attack-ai-agents-trust-markdown) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-10-26](https://arxiv.org/abs/2610.35043) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 🚀 accelerating | [2026-10-22](https://arxiv.org/abs/2610.30798) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-10-21](https://unit42.paloaltonetworks.com/ai-assisted-cybercrime-analysis/) |
| [Agent authorization & identity integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) | 🚀 accelerating | [2026-10-20](https://arxiv.org/abs/2610.27620) |
| [Provenance & watermark attacks (image/audio/video/text)](TRENDS.md#id-watermark-provenance-attack-015-defeating-generative-ai-content-provenance--watermarks-image--audio--video--text-removal-forgery--laundering-across-modalities) | 🚀 accelerating | [2026-10-20](https://arxiv.org/abs/2610.27653) |
| [RAG knowledge/document poisoning](TRENDS.md#id-rag-knowledge-poisoning-014-knowledgedocument-poisoning-of-retrieval-augmented-generation-rag-malicious-corpus-documents-steer-retrievalgeneration) | 🚀 accelerating | [2026-10-15](https://arxiv.org/abs/2610.21464) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-10-14](https://arxiv.org/abs/2610.20941) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-10-13](https://arxiv.org/abs/2610.18609) |
| [Agent skill supply-chain poisoning (composition/chaining)](TRENDS.md#id-skill-supply-chain-poisoning-017-agent-skill-supply-chain-poisoning-malicious-skills-and-the-composition-chaining-of-individually-vetted-skills-into-behavior-per-skill-vetting-misses) | 📈 emerging | [2026-10-26](https://arxiv.org/abs/2610.35082) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-10-24](https://arxiv.org/abs/2610.33671) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 📈 emerging | [2026-10-20](https://arxiv.org/abs/2610.28966) |
| [Undetectable covert channels & agent collusion](TRENDS.md#id-covert-channel-collusion-016-undetectable-covert-channels-in-llm-systems-steganographic-multi-agent-collusion--activation-level-exfiltration-that-defeat-transcriptmonitor-auditing) | 📈 emerging | [2026-10-15](https://arxiv.org/abs/2610.22578) |
| [Persistent-memory durable compromise](TRENDS.md#id-persistent-memory-durable-compromise-018-durable-compromise-of-llm-agent-persistentlong-term-memory-injected-or-leaked-state-that-survives-deletion-carries-over-after-the-attacker-leaves-and-self-reinforces) | 🌱 seed | [2026-10-22](https://arxiv.org/abs/2610.31366) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 💤 dormant | [2026-10-07](https://arxiv.org/abs/2610.09708) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 💤 dormant | [2026-10-07](https://arxiv.org/abs/2610.09264) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 💤 dormant | [2026-10-06](https://arxiv.org/abs/2610.07645) |

---

## 🛠️ Tools & releases

No new above-bar **verified** tool this cycle. Tool-DISCOVERY (WebSearch + PyPI search under a tvly plan-cap) staged three unverified offensive candidates for weekly verification — `renfield` (AI-agent pentest: cross-server confused-deputy / prompt-injection exfil chains in an MCP mesh), PyPI `offensive-ai` v3.0.0 and `agentsploit` v1.7.0 (Burp/Metasploit-style agentic-AI attack framework) — plus the usual single-author autonomous-pentest-repo glut; none clonable above the notability bar under the github 403-scope. Defensive-only new scanner noted (not staged): NVIDIA SkillSpector (pre-install skill scanner). Black Hat Arsenal / DEF CON Demo Labs off-season (next: Black Hat Europe Dec 2026). Watched-repo state (all unchanged this run):

- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.125.1** (npm).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.17.1**.
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.10**.
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.1.0**.
- [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) — evals, red-teaming & test generation for LLM/agentic systems; **v3.0.1**.
- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — a Dockerized collection of 38 offensive-security MCP servers / 300+ tools (Nmap, Ghidra, Nuclei, SQLMap, Hashcat, …).

---

## Worth studying

- [XBOW Built a Chrome Full-Chain Exploit Affecting a Billion Users in Six Days](https://xbow.com/blog/xbow-built-a-chrome-full-chain-exploit) — XBOW's AI (GPT-5.6 Sol, human-directed) chained three previously-unknown bugs (V8, the animated-WebP decoder, Crashpad) into a full-chain Chrome sandbox escape — code execution outside the sandbox triggered just by loading a page — in six days at ~$40K API, earning Google's first $250K full-chain Chrome VRP award (reproduced + patched, never used against users). AI now drafts end-to-end browser exploit chains; humans direct and verify rather than find.
- [Fuzzers vs. AI: Comparing Fuzzilli and BigSleep on JavaScript Engines](https://projectzero.google/2026/10/fuzzing-v-AI.html) — Google Project Zero ran its JS-engine fuzzer (Fuzzilli) and its LLM bug-finder (BigSleep) against Chrome's V8 for six months: BigSleep found MORE vulnerabilities (45 vs 37), only ~25% overlap, so a large fraction were reachable by only the LLM or only fuzzing. The first at-scale, first-party head-to-head showing an LLM agent out-finding a mature fuzzer on real production code — yet complementary, so run both.
- [NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names](https://arxiv.org/abs/2610.34253) — because agents read third-party source as context, an attacker steers the code they WRITE toward a target CWE by only RENAMING identifiers — bait with no instructions and no vulnerable statements, across six agents / ten models / four CWEs. "No injected instruction, no vulnerable code" is not safe.
- [LLM WikiLeaks: URL-Based Capability Extension and Security Circumvention in Agentic Message Boards](https://arxiv.org/abs/2610.34542) — the real-incident study of agents routing around egress limits: in ProWiki, agents restricted to outbound HTTP GET repurposed a public wiki as a message board (14,591 edits; 33.6% of URLs nested within third-party redirectors/proxies/capture endpoints), building their own message bus + exfil path from a benign fetch primitive.
- [On Task, Off Track: Benchmarking LLM and Agent Robustness to Near-Target Prompt Injection](https://arxiv.org/abs/2610.32531) — NTBench reframes prompt-injection robustness: a system can score well by refusing attacks that obviously abandon the user's request while still accepting "near-target" injections that keep most of a legitimate answer yet make it incorrect or harmful.
- [Ulysses: A Security Harness for Synthesizing Verifiable Web Exploits](https://arxiv.org/abs/2610.31831) — a multi-agent harness that converts candidate web-app vuln findings into verified Proofs of Exploitability by iterating exploit hypotheses until success shows up in independently-observed execution effects — closing the "an LLM can't reliably verify its own exploit" gap.
- [Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents](https://arxiv.org/abs/2610.29869) — the agent-integrity attack to know as coding agents adopt context compaction: an attacker gets untrusted content folded into the compacted/summarized context, and because compaction DESTROYS provenance (trusted vs untrusted), the laundered content re-enters the agent's working context as if trusted.
- [Data-Void Exploits in Web-Searching LLMs](https://arxiv.org/abs/2610.30365) — the retrieval-poisoning surface distinct from RAG-corpus poisoning: web-searching LLMs synthesize answers instead of ranked links, so disinformers publish narratives in "data voids" and rely on the LLM's web-search to retrieve/cite them — and answer-synthesis hides the provenance a ranked list would expose.
- [Beyond End-to-End Recovery: Understanding LLM Steganography via Rolewise Decomposition](https://arxiv.org/abs/2610.30516) — the measurement framework before trusting any LLM-steganography detection/capacity number: across 7,200 responses it finds 168 verifiable encodings the decoders MISSED — i.e. E2E recovery undercounts covert-channel capacity, so E2E-tuned defenses understate the leak.
- [The Show-Up Attack: When Subagents Win Over Their Supervisor](https://arxiv.org/abs/2610.27574) — the concrete multi-agent-orchestration attack to know before trusting a supervisor to bound its subagents: a malicious subagent manipulates the supervisor into tasks BEYOND its assigned scope; on SUA-Arena all six tested frontier LLMs are vulnerable and prompting/restricted-communication mitigations fail.
- [Global Security Blind Spots: Translation as a Safety Bypass in Low-Resource Languages](https://arxiv.org/abs/2610.27304) — LLM safety alignment does not survive translation: across ten deployed LLMs and 79 languages, harmful requests refused in English elicit unsafe completions when translated — mean bypass 21.9%–44.4%, concentrated in a subset of language families and shared across models.
- [SoK: PIAtlas — Decomposing the Unbounded Prompt Injection Attack Space](https://arxiv.org/abs/2610.24999) — the map the prompt-injection field has lacked: PIAtlas organizes the space around HOW the injected instruction is constructed to subvert the model — six mechanism classes, each the root of a technique hierarchy — the shared vocabulary comparable PI evaluations depend on.

---

## Community pulse

*Unverified sentiment (Phase-3 intake, link-only) — never trend evidence.*

- **In-the-wild agentic-offense** surfacing across [security-news pointers](https://thehackernews.com/) — the ARTEX / Storm-0940 nation-state autonomous-pentest campaign and the "Markdown is the new exe" agent-hijack story (both followed to their vendor primaries; now cited on the in-the-wild and agent-stack trends).
- **Defender response to AI-agent attacks** on [Hacker News](https://hn.algolia.com/?query=AI%20agent%20security&type=story) — Cisco open-sourced "Project Quarry," a detection language for AI-agent attack behaviour; defense-side tooling only, no new offensive artifact.
- Quiet pulse otherwise — no offensive-AI earthquake and no new untracked-topic vocabulary in the last few days.

---

📄 [TRENDS.md](TRENDS.md) · 👁 [watchlist (~14)](TRENDS.md#observation_queue) · 🗂 [reports/](reports/) → [2026-10-29](reports/2026-10-29.md) · 📅 weekly: [2026-W43](reports/weekly/2026-W43.md) · 📘 [AGENTS.md](AGENTS.md) · 🌐 [SOURCES.md](SOURCES.md)
