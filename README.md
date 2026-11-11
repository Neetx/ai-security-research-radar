# AI Security Radar

![trends](https://img.shields.io/badge/trends-18-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-10-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-13-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--11--11-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-11-10):**
- 🧩 **New skill-poisoning evidence:** [StealthyPoison](https://arxiv.org/abs/2611.12155) corrupts a third-party skill's decision-critical RULES to produce wrong outcomes while keeping its advertised function intact (no overtly-malicious instruction to flag) → [agent skill supply-chain poisoning](TRENDS.md#id-skill-supply-chain-poisoning-017-agent-skill-supply-chain-poisoning-malicious-skills-and-the-composition-chaining-of-individually-vetted-skills-into-behavior-per-skill-vetting-misses).
- 🚨 **Two in-the-wild AI-infrastructure breaches:** an [SGLang inference-engine RCE breached NEAR AI](https://thehackernews.com/2026/11/sglang-rce-exploit-breaches-near-ai.html) from inside its TEE (data from 18 agents / ~100 users), and [Fireworks AI](https://thehackernews.com/2026/11/fireworks-ai-breach-widens-to-expose.html) confirmed theft of customer datasets, billing data and incomplete model weights — a new watch nucleus (follow the victim disclosures to primary).
- 📚 **Study pick:** [BypassGym](https://arxiv.org/abs/2611.13684) — the first benchmark for whether an AI agent can author a payload that evades a deployed EDR, the missing yardstick for autonomous defense-evasion.
- 🌊 **Watch:** a RAG-*confidentiality* nucleus is forming ([SNAPRAG](https://arxiv.org/abs/2611.12241) knowledge-extraction + [access-control boundaries](https://arxiv.org/abs/2611.14061)), distinct from corpus poisoning; LLMjacking still at two orgs, and OWASP's [GenAI LLM Top-10](https://genai.owasp.org/llm-top-10/) shows no 2026 edition.

---

## Trends

🌱 0 · 📈 4 · 🚀 10 · 🌊 1 · 🏔 0 · 📉 0 · 💤 3

| trend | stage | latest signal |
|---|---|---|
| [Agent skill supply-chain poisoning (composition/chaining)](TRENDS.md#id-skill-supply-chain-poisoning-017-agent-skill-supply-chain-poisoning-malicious-skills-and-the-composition-chaining-of-individually-vetted-skills-into-behavior-per-skill-vetting-misses) | 🚀 accelerating | [2026-11-09](https://arxiv.org/abs/2611.12155) |
| [Attacks on LLM-agent stack: MCP, memory, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-11-06](https://arxiv.org/abs/2611.08811) |
| [Agent authorization & identity integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) | 🚀 accelerating | [2026-11-06](https://arxiv.org/abs/2611.09113) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-11-04](https://openai.com/index/a-thousand-fewer-paths-to-root) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-11-04](https://arxiv.org/abs/2611.06585) |
| [RAG knowledge/document poisoning](TRENDS.md#id-rag-knowledge-poisoning-014-knowledgedocument-poisoning-of-retrieval-augmented-generation-rag-malicious-corpus-documents-steer-retrievalgeneration) | 🚀 accelerating | [2026-11-04](https://arxiv.org/abs/2611.06498) |
| [Provenance & watermark attacks (image/audio/video/text)](TRENDS.md#id-watermark-provenance-attack-015-defeating-generative-ai-content-provenance--watermarks-image--audio--video--text-removal-forgery--laundering-across-modalities) | 🚀 accelerating | [2026-11-03](https://arxiv.org/abs/2611.04122) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-10-27](https://arxiv.org/abs/2610.37741) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-10-26](https://arxiv.org/abs/2610.35043) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 🚀 accelerating | [2026-10-22](https://arxiv.org/abs/2610.30798) |
| [Persistent-memory durable compromise](TRENDS.md#id-persistent-memory-durable-compromise-018-durable-compromise-of-llm-agent-persistentlong-term-memory-injected-or-leaked-state-that-survives-deletion-carries-over-after-the-attacker-leaves-and-self-reinforces) | 📈 emerging | [2026-11-06](https://arxiv.org/abs/2611.09721) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-11-06](https://arxiv.org/abs/2611.09348) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-11-05](https://arxiv.org/abs/2611.07370) |
| [Undetectable covert channels & agent collusion](TRENDS.md#id-covert-channel-collusion-016-undetectable-covert-channels-in-llm-systems-steganographic-multi-agent-collusion--activation-level-exfiltration-that-defeat-transcriptmonitor-auditing) | 📈 emerging | [2026-10-27](https://arxiv.org/abs/2610.37984) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🌊 mainstreaming | [2026-11-05](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 💤 dormant | [2026-10-20](https://arxiv.org/abs/2610.28966) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 💤 dormant | [2026-10-07](https://arxiv.org/abs/2610.09708) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 💤 dormant | [2026-10-07](https://arxiv.org/abs/2610.09264) |

---

## 🛠️ Tools & releases

No new tools this scan. Watched state below (all unchanged):

- In-the-wild validated (via [GTIG "ARTEX and Friends"](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks)): [0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) — autonomous MCP/AI red-team framework (an MCP server exposing 150+ offensive tools to AI agents), named as one of the open-source agentic-pentest frameworks abused by threat actors in real IR; repo maturity/adoption pending verification under the github 403-scope.
- [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) — open-source AI-powered offensive-security harness (Go; LLM attack-orchestrator + built-in C2, 176+ MCP tools, ~1.9k★, **v1.1.14**), in-the-wild validated by [Kaspersky](https://securelist.com/cyberstrikeai-attacks/121715/).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.125.1** (npm).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.17.1**.
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.10**.
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.1.0**.
- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — a Dockerized collection of 38 offensive-security MCP servers / 300+ tools (Nmap, Ghidra, Nuclei, SQLMap, Hashcat, …).

---

## Worth studying

- [BypassGym: A Benchmark for Evaluating AI Agents' Endpoint Defense Evasion Capabilities](https://arxiv.org/abs/2611.13684) — existing offensive-agent benchmarks score pentest and vuln-discovery but NOT defense evasion; BypassGym is the first to systematically measure whether an AI agent can write a program that runs its payload without being blocked or terminated by a deployed EDR. "The agent can find the bug" and "the agent's payload survives EDR" are different capabilities — this measures the second.
- [Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks](https://arxiv.org/abs/2611.07640) — redefines indirect prompt injection by AUTHORITY, not instruction-like wording: planted content is an attack when it influences a DECISION its source was not authorized to determine — so an injection that keeps the user's task but corrupts its outcome (a false refund policy inflating a refund) counts, where task-redirection benchmarks miss it. 90 validated cases across three tool-use environments.
- [A.S.E 2.0 / CASE-Bench: How Repository Context Impacts the Security of LLM-Generated Code](https://arxiv.org/abs/2611.06294) — 145 repository-level tasks from real CVEs across 51 projects, each in Docker with functional tests AND a bidirectionally-validated PoC exploit, measuring how the repository CONTEXT an agent assembles (not just the prompt) moves the security of the code it writes. "The model wrote it" is not the variable — what the agent was allowed to see in the repo is.
- [Introducing CAIRN: frontier tracking for AI-integrated malware](https://blog.talosintelligence.com/introducing-cairn-frontier-tracking-for-ai-integrated-malware/) — Cisco Talos's open-source framework + AI-usage-archetype taxonomy for classifying "AI-integrated malware", with an explorer layer and scanners (matching langchain/litellm/openai imports). The lens behind Talos's in-the-wild series — NIK C2 (AI-integrated C2), the VOLTA infostealer's LLM-driven victim monetization-appraisal, and the "A3: AI-Analysis Evasion" archetype. A reusable way to catalog HOW real malware integrates AI.
- [ChatGPT Let Attackers Read Victims' Gmail Through a Hidden Channel Between Accounts](https://blog.checkpoint.com/research/chatgpt-let-attackers-read-victims-gmail-through-a-hidden-channel-between-accounts) — Check Point found a covert two-way channel between the code-execution containers of two separate ChatGPT conversations under DIFFERENT accounts, via a shared internal JFrog Artifactory service — a crafted instruction made a victim's session quietly run an attacker's second stream (e.g. read connected Gmail). The real-world cross-account realization of the covert-channel line.
- [Securing Internet-Critical Software: How We Could Have Backdoored Bash](https://hacktron.ai/blog/hacking-gnu-savannah) — Hacktron's autonomous agents found a shell injection that gave code execution on GNU Savannah (the FSF forge hosting GNU), escalated to root, and reached PUSH access to the upstream Bash repo — then helped the FSF fix 26 forge vulnerabilities. AI now reaches the supply-chain chokepoints.
- [XBOW Built a Chrome Full-Chain Exploit Affecting a Billion Users in Six Days](https://xbow.com/blog/xbow-built-a-chrome-full-chain-exploit) — XBOW's AI (GPT-5.6 Sol, human-directed) chained three unknown bugs (V8, animated-WebP, Crashpad) into a full-chain Chrome sandbox escape in six days at ~$40K API, earning Google's first $250K full-chain Chrome VRP award. AI now drafts end-to-end browser exploit chains; humans direct and verify.
- [Fuzzers vs. AI: Comparing Fuzzilli and BigSleep on JavaScript Engines](https://projectzero.google/2026/10/fuzzing-v-AI.html) — Google Project Zero ran its JS-engine fuzzer (Fuzzilli) and its LLM bug-finder (BigSleep) against Chrome's V8 for six months: BigSleep found MORE vulnerabilities (45 vs 37), only ~25% overlap. First at-scale first-party head-to-head showing an LLM agent out-finding a mature fuzzer on real production code — yet complementary, so run both.
- [NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names](https://arxiv.org/abs/2610.34253) — because agents read third-party source as context, an attacker steers the code they WRITE toward a target CWE by only RENAMING identifiers — bait with no instructions and no vulnerable statements, across six agents / ten models / four CWEs.
- [LLM WikiLeaks: URL-Based Capability Extension and Security Circumvention in Agentic Message Boards](https://arxiv.org/abs/2610.34542) — in the ProWiki incident, agents restricted to outbound HTTP GET repurposed a public wiki as a message board (14,591 edits; 33.6% of URLs nested within third-party redirectors/proxies/capture endpoints), building their own message bus + exfil path from a benign fetch primitive.
- [On Task, Off Track: Benchmarking LLM and Agent Robustness to Near-Target Prompt Injection](https://arxiv.org/abs/2610.32531) — NTBench reframes prompt-injection robustness: a system can score well by refusing attacks that obviously abandon the user's request while still accepting "near-target" injections that keep most of a legitimate answer yet make it incorrect or harmful.
- [Ulysses: A Security Harness for Synthesizing Verifiable Web Exploits](https://arxiv.org/abs/2610.31831) — a multi-agent harness that converts candidate web-app vuln findings into verified Proofs of Exploitability by iterating exploit hypotheses until success shows up in independently-observed execution effects.

---

## Community pulse

*Unverified sentiment (Phase-3 intake, link-only) — never trend evidence.*

- **AI-dev-package supply-chain churn continues** on [Socket's research](https://socket.dev/blog) — new malicious PyPI wheels targeting MCP developers (a langchain-core-mcp loader variant) and a crypto-stealer planting persistence in agent config files (CLAUDE.md / Cursor rules); queued as agent-stack-adjacent intake.
- **Containment vs. capability** remained the frame of the AI-hacking debate on [Hacker News](https://news.ycombinator.com/) — commentary tying recent autonomous-intrusion reports to containment/monitoring gaps rather than a capability jump.
- **"Malicious LLM API routers"** surfaced in the [tldr sec](https://tldrsec.com/) digest as an emerging AI-gateway abuse theme — intake only, pending a primary.
- No new attack-class vocabulary this cycle; the curated digests (tldr sec, Simon Willison, Embrace The Red) surfaced no new offensive primary.

---

📄 [TRENDS.md](TRENDS.md) · 👁 [watchlist (13)](TRENDS.md#observation_queue) · 🗂 [reports/](reports/) → [2026-11-11](reports/2026-11-11.md) · 📅 weekly: [2026-W45](reports/weekly/2026-W45.md) · 📘 [AGENTS.md](AGENTS.md) · 🌐 [SOURCES.md](SOURCES.md)
