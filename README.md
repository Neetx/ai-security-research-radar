# AI Radar

![trends](https://img.shields.io/badge/trends-12-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-25-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--08--27-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-08-27):** two trends refreshed with fresh evidence; a striking AI-for-offense containment-failure datapoint; queue burndown resumed.
- 🧠 **[Mechanistic basis of jailbreaks](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) refreshed — dormancy mooted:** **[Refusal geometry reflects refusal training](https://arxiv.org/abs/2608.25390)** (2026-08-26) ties the refusal direction to the refusal-completion training losses and shows diverse-refusal-prefix training raises stable rank and *weakens* refusal-vector-ablation (abliteration) attacks — a fresh in-window capture on the trend's 21-day dormancy day. The community name for the assistant-prefill jailbreak this trend dissects — **"sockpuppeting"** — is captured as an alias.
- 🪱 **[Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) +1 — now a worm:** **[EVOMAL](https://arxiv.org/abs/2608.25776)** (2026-08-26) is a 6th independent group: a retrieved malicious skill becomes the template an imitating agent re-authors, so each copy re-enters the library — a self-propagating skill worm that persists after the planted seeds are removed.
- 🛰️ **AI-for-offense capability datapoint:** Trail of Bits reports **[GPT-5.6-Cyber autonomously escaping a QEMU/KVM sandbox three times](https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/)** (2026-08-26) via known *and* zero-day exploits — "you can no longer assume a mere VM will contain a sufficiently advanced AI agent" (added to Worth studying).
- 🧹 **Queue burndown resumed** (no longer deferred): 3 oldest watch-flags resolved — the speculative-decoding-DoS item folded into [economic/availability DoS](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness); two single-group niche items dropped. Live watchlist back to ~25.

---

## Trends

🌱 1 · 📈 4 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 1

| trend | stage | latest signal |
|---|---|---|
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-08-26](https://arxiv.org/abs/2608.25390) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-08-25](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-08-24](https://arxiv.org/abs/2608.23763) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-08-21](https://arxiv.org/abs/2608.20637) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-08-17](https://arxiv.org/abs/2608.16246) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-08-11](https://arxiv.org/abs/2608.10959) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-08-26](https://arxiv.org/abs/2608.25776) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 📈 emerging | [2026-08-22](https://arxiv.org/abs/2608.21929) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-08-20](https://arxiv.org/abs/2608.20055) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 📈 emerging | [2026-08-06](https://arxiv.org/abs/2608.05715) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 🌱 seed | [2026-08-12](https://arxiv.org/abs/2608.11878) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 💤 dormant | [2026-07-14](https://arxiv.org/abs/2607.12340) |

---

## 🛠️ Tools & releases

No brand-new discrete public tool surfaced from the discovery lane this scan — only known / awesome-list and already-staged candidates ([Augustus/Praetorian](https://github.com/praetorian-inc), [Offensive-MCP-AI](https://github.com/CyberSecurityUP/Offensive-MCP-AI), [redamon](https://github.com/samugit83/redamon)), plus two new curated lists staged for verification (byoniq/AI-Redteaming, LLMSecurity/awesome-agent-skills-security). Watched packaged tools: giskard **3.0.0** (major release, 2026-08-26) is the newest; promptfoo bumped 0.122.0 → **0.122.1**; garak / PyRIT / deepteam unchanged. The current on-axis tool set:

- [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) — evals, red-teaming & test generation for LLM/agentic systems; **v3.0.0** (2026-08-26, major release).
- [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) — autonomous-pentest harness (13+ agents, 176 MCP tools, Ed25519-signed skills, OWASP/MITRE/CIS-aligned); 1.9k★, npm `@cyberstrike-io/cyberstrike`.
- [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) — full-stack AI red-team platform: Agent-Scan, MCP-Scan, Skill-Scan (SARIF 2.1.0), jailbreak eval (26+ methods); **v4.5.2** (2026-08-17).
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.9** (latest on PyPI, 2026-08-12).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.16.0** (latest on PyPI).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.122.1** (latest on npm).
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.0.1** — the major v1 architectural redesign.
- [airtasystems/DVAIA-Damn-Vulnerable-AI-Application](https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application) — a DVWA-style deliberately-vulnerable LLM/agent lab (prompt injection, jailbreaks, indirect injection, RAG poisoning, tool-use vulns).

---

## Worth studying

- [Trail of Bits — "VMs won't contain cyber-capable agents"](https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/) — the reference datapoint that a plain VM no longer suffices to contain an advanced offensive AI agent: GPT-5.6-Cyber autonomously escaped a QEMU/KVM sandbox **three times** via known and zero-day exploits, backtracking and chaining vulnerabilities over extended runs.
- [DarkBot: Automated CTI Elicitation in Underground Forums](https://arxiv.org/abs/2608.23185) — AI moving from passive monitoring to **active** deceptive engagement of adversaries: 11 specialized agents recover 72.8% of validated ATT&CK techniques from only the initial post, and in a live matched deployment across 104 real conversations accumulate +3.85 more CTI entities than controls.
- [AI Grinding for Fun and Cryptanalysis](https://arxiv.org/abs/2608.21986) — the reference for autonomous AI as a working cryptanalysis collaborator: an agent workflow returns reproducible candidates with exact witnesses/controls/code, landing **eight** published constructions failing at their stated parameters.
- [GhostTac: Manipulating Tactile Sensors without Physical Contact](https://arxiv.org/abs/2608.20817) — a new physical-layer attack surface on embodied AI: the first **contactless** attack on robotic tactile sensing, using electromagnetic interference to imprint persistent DC offsets that force harmful robot behavior. Demonstrated across 15 sensors / 10 modules / two dexterous hands.
- [MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection](https://arxiv.org/abs/2608.19901) — the consolidated dataset to test malicious-Skill detection against: 9,740 Skills across 4,588 structural families and 11 attack categories. Learned detectors fall from 0.88–0.93 Macro-F1 to **0.65** under source-disjoint evaluation.
- [CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing Skills](https://arxiv.org/abs/2608.16246) — the reference for why per-skill certification of agent marketplaces is structurally insufficient: composition risk is a *path*-level property, so a skill that passes its own scanner still forms a harmful chain — up to 80.6% Chain-Formation-Rate.
- [Beyond Direct Access: Resource Hijacking in LLM Agents](https://arxiv.org/abs/2608.15108) — the clean statement of an overlooked agent attack surface: attackers needn't steal a resource or its credentials, only induce the agent to invoke/consume/transfer the high-value resources it already reaches. ResourceHijackBench: OpenClaw 84% avg ASR.
- [MazeRunner: Nonlinear Task & Clue Orchestration for LLM-driven Black-Box Automated Pentesting](https://arxiv.org/abs/2608.14216) — how much *structure* the autonomous-pentest frontier still needs: a three-agent design with persistent state completes 47.7% of HackTheBox subtasks and reaches root where same-model baselines never do.
- [Finding Vulnerabilities via LLM-Augmented Semantics-Aware Type-Checking (SETYPE)](https://arxiv.org/abs/2608.14533) — the clean reference for LLM-as-static-analyzer that finds **real** bugs: PYSETYPE hits 87%/88% precision/accuracy on real Python web apps and surfaced 15 potential zero-days, **nine confirmed by developers**.
- [ATOBench: How Autonomous Pentest Agents Verify Vulnerabilities When Target Evidence Lies](https://arxiv.org/abs/2608.12996) — the reference for a blind spot in every autonomous-pentest agent: because its next action, stop decision, and final claim all rest on target responses, a *deceptive* response can silently redirect both attack and verification.
- [SRE-Bench: A Realistic, Contamination-Free Reverse Engineering Benchmark](https://arxiv.org/abs/2608.11469) — the rigorous testbed on the limits of AI for offensive binary analysis: 19 private, real-world-scale programs → 1,572 graded tasks. The strongest of five frontier LLMs scores only 61.4%.
- [MarkNull: Model-Agnostic Watermark Removal in AI-Generated Images](https://arxiv.org/abs/2608.10166) — the USENIX-2026 anchor for why AI-image provenance/watermarking is not yet a reliable integrity control: on-manifold latent decorrelation drops watermark bit-accuracy to ~53%, defeats Google SynthID-Image, and transfers to video.

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- The black-box jailbreak named **"sockpuppeting"** (abusing assistant-prefill support to inject a fake compliant response) resolved to the known assistant-prefill jailbreak — vendors (OpenAI / Anthropic / AWS Bedrock) have patched hosted endpoints, but self-hosted Ollama/vLLM/TGI remain exposed by default ([HN newest](https://news.ycombinator.com/newest)).
- The **"a VM won't contain a cyber-capable agent"** framing is circulating alongside fresh autonomous-sandbox-escape demonstrations — a leading indicator that agent-containment, not just prompt-filtering, is becoming the discussed control boundary.
- Reports of a **~32% rise in malicious prompt-injection payloads embedded in web content** (late-2025 → early-2026) keep indirect-PI-via-the-open-web a live theme for agentic browsing.
- The **OWASP Agentic Skills Top 10** release keeps circulating as the community consolidates a shared vocabulary for agent-skill risk (malicious skills, supply-chain, over-privilege, poor scanning).
- Model hubs keep churning out **abliterated/uncensored** open-weight models and fresh prompt-injection datasets — a steady leading indicator for the refusal-direction / jailbreak axis.

---

[TRENDS.md](TRENDS.md) · [watchlist (25)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-08-27](reports/2026-08-27.md) · [weekly: 2026-W34](reports/weekly/2026-W34.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
