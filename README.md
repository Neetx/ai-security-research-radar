# AI Radar

![trends](https://img.shields.io/badge/trends-12-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-25-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--08--29-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-08-29):** weekly recalibration — no stage changes, two dormancy saves, and a full week on fallback coverage.
- 🩺 **Weekly recalibration (W35): no new stage moves** — the week's two promotions ([automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) and [economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) → emerging) were logged by the dailies; [self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) reviewed and held emerging (6 independent groups, but still all-academic with no in-the-wild case).
- 🔎 **Dormancy averted twice by the targeted-axis check:** [physical-channel PI on embodied AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) held emerging (an embodied-agent security survey + a grid-agent defense landed inside its "silent" window), and [weaponized LLM hallucination](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) was kept off the archive shelf — two fresh slopsquatting papers ([Names Can Hurt](https://arxiv.org/abs/2608.23897), [Evaluating Inference-Time Defenses](https://arxiv.org/abs/2608.22652)) show the axis is alive, though still defense-side.
- 🛰️ **Coverage:** the [Tavily search plan](SOURCES.md) has been usage-capped 8 days running; every source ran on the curl/WebFetch fallback and was logged — nothing silently dropped — but restoring full coverage needs the curator to lift the plan cap.
- 🧹 **Housekeeping:** pruned 5 aged [study-shelf](TRENDS.md#study_shelf) picks (>30d, preserved in their day's reports) and retired two resolved [queue](TRENDS.md#observation_queue) husks; watchlist ~25.

---

## Trends

🌱 0 · 📈 5 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 1

| trend | stage | latest signal |
|---|---|---|
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-08-27](https://arxiv.org/abs/2608.27299) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-08-26](https://arxiv.org/abs/2608.25390) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-08-25](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-08-21](https://arxiv.org/abs/2608.20637) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-08-17](https://arxiv.org/abs/2608.16246) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-08-11](https://arxiv.org/abs/2608.10959) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 📈 emerging | [2026-08-27](https://arxiv.org/abs/2608.27439) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-08-26](https://arxiv.org/abs/2608.25776) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 📈 emerging | [2026-08-22](https://arxiv.org/abs/2608.21929) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-08-20](https://arxiv.org/abs/2608.20055) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 📈 emerging | [2026-08-06](https://arxiv.org/abs/2608.05715) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 💤 dormant | [2026-07-14](https://arxiv.org/abs/2607.12340) |

---

## 🛠️ Tools & releases

No brand-new discrete public tool surfaced from the discovery lane this scan — only known / awesome-list and already-staged candidates ([redamon](https://github.com/samugit83/redamon), [RedteamAgent](https://github.com/NeoTheCapt/RedteamAgent), [Offensive-MCP-AI](https://github.com/CyberSecurityUP/Offensive-MCP-AI)). Watched packaged tools unchanged since the last scan: giskard **3.0.0** (major release, 2026-08-26) remains the newest; promptfoo **0.122.1** (npm); garak / PyRIT / deepteam unchanged. The current on-axis tool set:

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

- [PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?](https://arxiv.org/abs/2608.26882) — the reference testbed for the cyber-to-**physical** frontier of autonomous-agent offense: the first real-PLC hardware-in-the-loop framework measuring whether a tool-using LLM agent can convert a network-reachable PLC into *sustained* adverse physical impact on an industrial process, with six diagnostic flags separating usable interaction / process-linked manipulation / sustained impact.
- [Breaking Claude Code Opus 5 Auto Mode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) — the practitioner reference that a coding agent's auto-approval mode is not a security boundary: a WebFetch→curl redirect + a malicious ZIP + a poisoned `struct.py` yields module-shadowing **RCE** at 60–80% success against Claude Code Opus 5 Auto Mode; Anthropic ruled it "Informative"/by-design (OS isolation + egress control are the real boundary).
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

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- The **"a VM won't contain a cyber-capable agent"** framing keeps circulating, now reinforced by a practitioner RCE against Claude Code's *Auto Mode* ruled "by design" — the discussed control boundary is shifting from prompt-filtering to OS isolation + egress control, *below* the model ([HN newest](https://news.ycombinator.com/newest)).
- **Physical-world agent** control is entering the discourse (a new vendor hardware standard for agents driving machines) just as academic work benchmarks whether autonomous agents can turn ICS/PLC access into sustained physical impact — an early indicator of an OT/OT-safety agent-security theme.
- The black-box jailbreak named **"sockpuppeting"** (abusing assistant-prefill support) resolved to the known assistant-prefill jailbreak — vendors patched hosted endpoints, but self-hosted Ollama/vLLM/TGI remain exposed by default.
- The **OWASP Agentic Skills Top 10** release keeps circulating as the community consolidates a shared vocabulary for agent-skill risk (malicious skills, supply-chain, over-privilege, poor scanning).
- Model hubs keep churning out **abliterated/uncensored** open-weight models and fresh prompt-injection datasets — a steady leading indicator for the refusal-direction / jailbreak axis.

---

[TRENDS.md](TRENDS.md) · [watchlist (25)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-08-28](reports/2026-08-28.md) · [weekly: 2026-W35](reports/weekly/2026-W35.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
