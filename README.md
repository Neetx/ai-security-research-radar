# AI Radar

![trends](https://img.shields.io/badge/trends-12-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-25-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--08--31-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-08-31):** first daily since the W35 weekly — no stage moves, two evidence refreshes via cap rotation, one study pick.
- 🧩 **Agent-stack attacks +1 (in the wild):** [Mindgard's Amazon Kiro data-exfil-via-prompt-injection](https://mindgard.ai/blog/amazon-kiro-data-exfiltration) (08-27) is a working attack on a production agentic IDE — malicious repo content makes the agent read `.env` secrets, write them into a workspace-config URL, then invoke a tool that beacons them out (fixed in Kiro 0.8.140) → rotated onto [attacks on the LLM-agent stack](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain).
- 🎯 **Backdoor cluster refreshed off a dormancy drift:** [Quantization-Triggered Backdoors](https://arxiv.org/abs/2608.27512) (08-27) keys a supply-chain backdoor to the *deployment transform* — dormant at full precision, live once quantized — rotated onto [adversarial trigger implantation & backdoors](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) (last evidence 08-11→08-27, mooting the 21-day dormancy check).
- 🔬 **Study pick — safety is a thin layer:** [Perturbation Probing](https://unit42.paloaltonetworks.com/perturbation-probing-llm-safety/) (Unit 42, 08-28) locates ~50 neurons (0.014% of FFN) that control the refusal template on Qwen3-4B and derives a single ratio predicting 81% of safety-fragility variance across 13 models — the mechanistic case behind every [refusal-direction attack](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions).
- 🛰️ **Coverage:** the [Tavily search plan](SOURCES.md) has been usage-capped 8 days running; every source ran on the curl/WebFetch fallback and was logged — capture-leak 23/0, watchlist ~25 — but restoring full coverage needs the curator to lift the plan cap.

---

## Trends

🌱 0 · 📈 5 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 1

| trend | stage | latest signal |
|---|---|---|
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-08-27](https://arxiv.org/abs/2608.27299) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-08-27](https://arxiv.org/abs/2608.27512) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-08-26](https://arxiv.org/abs/2608.25390) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-08-25](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-08-21](https://arxiv.org/abs/2608.20637) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-08-17](https://arxiv.org/abs/2608.16246) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 📈 emerging | [2026-08-27](https://arxiv.org/abs/2608.27439) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-08-26](https://arxiv.org/abs/2608.25776) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 📈 emerging | [2026-08-22](https://arxiv.org/abs/2608.21929) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-08-20](https://arxiv.org/abs/2608.20055) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 📈 emerging | [2026-08-06](https://arxiv.org/abs/2608.05715) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 💤 dormant | [2026-07-14](https://arxiv.org/abs/2607.12340) |

---

## 🛠️ Tools & releases

No brand-new discrete public tool surfaced from the discovery lane this scan — only known / awesome-list and already-staged candidates ([redamon](https://github.com/samugit83/redamon), [T3MP3ST](https://github.com/elder-plinius/T3MP3ST), [Decepticon](https://github.com/PurpleAILAB/Decepticon), [snyk/agent-scan](https://github.com/snyk/agent-scan)). Watched packaged tools: promptfoo ticked to **0.122.2** (npm, 2026-08-28, minor patch); giskard **3.0.0** (2026-08-26) remains the newest major; garak / PyRIT / deepteam unchanged. The current on-axis tool set:

- [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) — evals, red-teaming & test generation for LLM/agentic systems; **v3.0.0** (2026-08-26, major release).
- [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) — autonomous-pentest harness (13+ agents, 176 MCP tools, Ed25519-signed skills, OWASP/MITRE/CIS-aligned); 1.9k★, npm `@cyberstrike-io/cyberstrike`.
- [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) — full-stack AI red-team platform: Agent-Scan, MCP-Scan, Skill-Scan (SARIF 2.1.0), jailbreak eval (26+ methods); **v4.5.2** (2026-08-17).
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.9** (latest on PyPI, 2026-08-12).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.16.0** (latest on PyPI).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.122.2** (latest on npm).
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.0.1** — the major v1 architectural redesign.
- [airtasystems/DVAIA-Damn-Vulnerable-AI-Application](https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application) — a DVWA-style deliberately-vulnerable LLM/agent lab (prompt injection, jailbreaks, indirect injection, RAG poisoning, tool-use vulns).

---

## Worth studying

- [Perturbation Probing: A New Diagnostic for the Fragility of LLM Safety](https://unit42.paloaltonetworks.com/perturbation-probing-llm-safety/) — the sharpest single datapoint for why refusal is a manipulable low-dimensional target: a two-forward-passes-per-prompt diagnostic finds ~50 of 350,208 FFN neurons (~0.014%) control the refusal template on Qwen3-4B, and an FFN/Skip ratio explains **81%** of safety-fragility variance across 13 models — the "thin template layer" account every abliteration/refusal-ablation attack exploits.
- [PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?](https://arxiv.org/abs/2608.26882) — the reference testbed for the cyber-to-**physical** frontier of autonomous-agent offense: the first real-PLC hardware-in-the-loop framework measuring whether a tool-using LLM agent can convert a network-reachable PLC into *sustained* adverse physical impact on an industrial process.
- [Breaking Claude Code Opus 5 Auto Mode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) — the practitioner reference that a coding agent's auto-approval mode is not a security boundary: a WebFetch→curl redirect + a malicious ZIP + a poisoned `struct.py` yields module-shadowing **RCE** at 60–80% success; Anthropic ruled it by-design (OS isolation + egress control are the real boundary).
- [Trail of Bits — "VMs won't contain cyber-capable agents"](https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/) — the reference datapoint that a plain VM no longer suffices to contain an advanced offensive AI agent: GPT-5.6-Cyber autonomously escaped a QEMU/KVM sandbox **three times** via known and zero-day exploits.
- [DarkBot: Automated CTI Elicitation in Underground Forums](https://arxiv.org/abs/2608.23185) — AI moving from passive monitoring to **active** deceptive engagement of adversaries: 11 specialized agents recover 72.8% of validated ATT&CK techniques from only the initial post.
- [AI Grinding for Fun and Cryptanalysis](https://arxiv.org/abs/2608.21986) — autonomous AI as a working cryptanalysis collaborator: an agent workflow returns reproducible candidates with exact witnesses/controls/code, landing **eight** published constructions failing at their stated parameters.
- [GhostTac: Manipulating Tactile Sensors without Physical Contact](https://arxiv.org/abs/2608.20817) — a new physical-layer attack surface on embodied AI: the first **contactless** attack on robotic tactile sensing, using EMI to imprint persistent DC offsets that force harmful robot behavior across 15 sensors / 10 modules / two dexterous hands.
- [MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection](https://arxiv.org/abs/2608.19901) — the consolidated dataset to test malicious-Skill detection against: 9,740 Skills across 4,588 structural families / 11 attack categories; learned detectors fall from 0.88–0.93 Macro-F1 to **0.65** under source-disjoint evaluation.
- [CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing Skills](https://arxiv.org/abs/2608.16246) — why per-skill certification of agent marketplaces is structurally insufficient: composition risk is a *path*-level property, so a skill that passes its own scanner still forms a harmful chain (up to 80.6% Chain-Formation-Rate).
- [Beyond Direct Access: Resource Hijacking in LLM Agents](https://arxiv.org/abs/2608.15108) — the clean statement of an overlooked agent attack surface: attackers need not steal a resource or its credentials, only induce the agent to invoke/consume the high-value resources it can already reach; ResourceHijackBench organizes 300 scenarios / 900 prompts.
- [MazeRunner: Nonlinear Task and Clue Orchestration for LLM-driven Black-Box Automated Penetration Testing](https://arxiv.org/abs/2608.14216) — how much structure the autonomous-pentest frontier still needs beyond a strong backbone: separates global orchestration, context-heavy memory and local execution to beat depth-first traps on HTB targets.
- [Finding Vulnerabilities via LLM-Augmented Semantics-Aware Type-Checking](https://arxiv.org/abs/2608.14533) — LLM-as-static-analyzer that finds real bugs: SETYPE derives a semantics-aware type system from source and treats a failed type check as a potential vulnerability (87% precision on real Python web apps).

---

## Community pulse

*Unverified sentiment (Phase-3 intake, link-only) — never trend evidence.*

- Practitioner attention on **prompt-injection against production coding agents/IDEs** is high — the [Kiro data-exfil writeup](https://mindgard.ai/blog/amazon-kiro-data-exfiltration) and the [Claude Code Auto-Mode RCE](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) both trended.
- A wave of **agent/MCP/skill security scanners** is shipping ([snyk/agent-scan](https://github.com/snyk/agent-scan) surfaced on HN) — the defensive tooling layer the radar tracks as [unreliable-under-attack](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack).
- Physical-world / OT-agent control is entering discourse, pairing with the off-axis [PLCBench](https://arxiv.org/abs/2608.26882) ICS nucleus the radar is watching for a 2nd group.

---

📄 [TRENDS.md](TRENDS.md) · 👁 [watchlist (~25)](TRENDS.md#observation_queue) · 🗂 [reports/](reports/) → [2026-08-31](reports/2026-08-31.md) · 📅 weekly: [2026-W35](reports/weekly/2026-W35.md) · 📘 [AGENTS.md](AGENTS.md) · 🌐 [SOURCES.md](SOURCES.md)
