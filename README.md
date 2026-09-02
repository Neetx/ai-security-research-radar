# AI Radar

![trends](https://img.shields.io/badge/trends-12-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-25-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--09--02-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-09-02):** no stage moves — one evidence append, two study picks, one dropped signal.
- 🧩 **Agent-stack attacks +1:** [CVE-2026-19591](https://nvd.nist.gov/vuln/detail/CVE-2026-19591) (09-01) — OpenAI Codex CLI/Desktop misread PowerShell's `--%` stop-parsing token, so an attacker-prepared repo can make Codex run an unapproved Git write, poison Codex's own config, and on next load launch an attacker-controlled MCP server → **RCE** at user privileges; a disclosed real-product approval-bypass chain rotated onto [attacks on the LLM-agent stack](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain).
- 🔬 **Study picks:** [Context Privilege Escalation vs the AI agent harness](https://arxiv.org/abs/2609.01222) — first systematic analysis of how real harnesses *assemble* context, naming M-CPE + Cross-Scope CPE (a 2nd group on the harness-privilege facet) — and [AKRASIA](https://arxiv.org/abs/2609.01023), a stealthy backdoor on reasoning Code LLMs (99.34% ASR) that hides its trigger behind unfaithful reasoning.
- ❌ **Dropped — "AI slop" flag confirmed:** Theori's [Copy Fail (CVE-2026-31431)](https://cyberscoop.com/copy-fail-linux-vulnerability-artificial-intelligence) "AI-discovered kernel LPE" claim fails verification — a routine Linux-kernel crypto revert (NVD-published 04-22) whose patch predated disclosure; not citable AI-for-offense evidence.
- 🛰️ **Coverage:** watched tools all unchanged; NVD adds the Codex CVE + GHSA MCP-server advisories to the [agent-stack](SOURCES.md) MCP burst; capture-leak 24/0, watchlist ~25.

---

## Trends

🌱 0 · 📈 5 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 1

| trend | stage | latest signal |
|---|---|---|
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-09-01](https://nvd.nist.gov/vuln/detail/CVE-2026-19591) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-08-27](https://arxiv.org/abs/2608.27512) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-08-26](https://arxiv.org/abs/2608.25390) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-08-25](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-08-21](https://arxiv.org/abs/2608.20637) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-08-17](https://arxiv.org/abs/2608.16246) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 📈 emerging | [2026-08-31](https://arxiv.org/abs/2608.30207) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-08-26](https://arxiv.org/abs/2608.25776) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 📈 emerging | [2026-08-22](https://arxiv.org/abs/2608.21929) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-08-20](https://arxiv.org/abs/2608.20055) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 📈 emerging | [2026-08-06](https://arxiv.org/abs/2608.05715) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 💤 dormant | [2026-07-14](https://arxiv.org/abs/2607.12340) |

---

## 🛠️ Tools & releases

No brand-new discrete public tool surfaced from the discovery lane this scan — only known / awesome-list and already-staged candidates ([redamon](https://github.com/samugit83/redamon), [T3MP3ST](https://github.com/elder-plinius/T3MP3ST), [Decepticon](https://github.com/PurpleAILAB/Decepticon), [snyk/agent-scan](https://github.com/snyk/agent-scan)); [simon-p-j-r/LLM4Pentest](https://github.com/simon-p-j-r/LLM4Pentest) staged unverified pending the weekly's verification. Watched packaged tools all unchanged this scan (garak / PyRIT / deepteam / giskard / promptfoo). The current on-axis tool set:

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

- [What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness](https://arxiv.org/abs/2609.01222) — the reference for why the HARNESS (not the model) is where instruction-privilege breaks: the first systematic analysis of how real-world, vendor-proprietary AI-agent harnesses *assemble* context, naming two novel attack categories — **M-CPE** (attacker content from a low-privileged context placed into a higher-privileged message role) and **Cross-Scope CPE**. Read with "When Context Gets Root" as a 2nd independent group converging on the same class.
- [AKRASIA: Stealthy Backdoor Attack on Reasoning-based Code LLMs](https://arxiv.org/abs/2609.01023) — why a reasoning trace is not evidence of trustworthiness: an inference-time in-context backdoor for reasoning Code LLMs that exploits model UNFAITHFULNESS to hide the trigger and emit plausible reasoning — up to **99.34%** ASR, retaining up to 98.82% in 14/18 defense settings and evading human inspection at ~97% clean accuracy.
- [Beyond the Payload / CIPR — how user invocation shapes coding-agent vulnerability to repository poisoning](https://arxiv.org/abs/2608.30686) — the benchmark to read on why coding-agent repo-poisoning risk is not the attacker's payload alone: CIPR (1,920 instances / 20 real poisoned repos / 4 task types) shows the developer's own "Prompt-Level Configurations" — what task they delegate, how they phrase it, which skills/rules they attach — measurably raise or lower whether a poisoned repo compromises the agent, so safe usage is part of the threat model.
- [Perturbation Probing: A New Diagnostic for the Fragility of LLM Safety](https://unit42.paloaltonetworks.com/perturbation-probing-llm-safety/) — the sharpest single datapoint for why refusal is a manipulable low-dimensional target: a two-forward-passes-per-prompt diagnostic finds ~50 of 350,208 FFN neurons (~0.014%) control the refusal template on Qwen3-4B, and an FFN/Skip ratio explains **81%** of safety-fragility variance across 13 models — the "thin template layer" account every abliteration/refusal-ablation attack exploits.
- [PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?](https://arxiv.org/abs/2608.26882) — the reference testbed for the cyber-to-**physical** frontier of autonomous-agent offense: the first real-PLC hardware-in-the-loop framework measuring whether a tool-using LLM agent can convert a network-reachable PLC into *sustained* adverse physical impact on an industrial process.
- [Breaking Claude Code Opus 5 Auto Mode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) — the practitioner reference that a coding agent's auto-approval mode is not a security boundary: a WebFetch→curl redirect + a malicious ZIP + a poisoned `struct.py` yields module-shadowing **RCE** at 60–80% success; Anthropic ruled it by-design (OS isolation + egress control are the real boundary).
- [Trail of Bits — "VMs won't contain cyber-capable agents"](https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/) — the reference datapoint that a plain VM no longer suffices to contain an advanced offensive AI agent: GPT-5.6-Cyber autonomously escaped a QEMU/KVM sandbox **three times** via known and zero-day exploits.
- [DarkBot: Automated CTI Elicitation in Underground Forums](https://arxiv.org/abs/2608.23185) — AI moving from passive monitoring to **active** deceptive engagement of adversaries: 11 specialized agents recover 72.8% of validated ATT&CK techniques from only the initial post.
- [AI Grinding for Fun and Cryptanalysis](https://arxiv.org/abs/2608.21986) — autonomous AI as a working cryptanalysis collaborator: an agent workflow returns reproducible candidates with exact witnesses/controls/code, landing **eight** published constructions failing at their stated parameters.
- [GhostTac: Manipulating Tactile Sensors without Physical Contact](https://arxiv.org/abs/2608.20817) — a new physical-layer attack surface on embodied AI: the first **contactless** attack on robotic tactile sensing, using EMI to imprint persistent DC offsets that force harmful robot behavior across 15 sensors / 10 modules / two dexterous hands.
- [MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection](https://arxiv.org/abs/2608.19901) — the consolidated dataset to test malicious-Skill detection against: 9,740 Skills across 4,588 structural families / 11 attack categories; learned detectors fall from 0.88–0.93 Macro-F1 to **0.65** under source-disjoint evaluation.
- [CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing Skills](https://arxiv.org/abs/2608.16246) — why per-skill certification of agent marketplaces is structurally insufficient: composition risk is a *path*-level property, so a skill that passes its own scanner still forms a harmful chain (up to 80.6% Chain-Formation-Rate).

---

## Community pulse

*Unverified sentiment (Phase-3 intake, link-only) — never trend evidence.*

- Practitioner attention on **prompt-injection against production coding agents/IDEs** stays high — the [Kiro data-exfil writeup](https://mindgard.ai/blog/amazon-kiro-data-exfiltration) and the [Claude Code Auto-Mode RCE](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) keep recirculating on HN, now joined by the OpenAI Codex approval-bypass CVE.
- A real-world case of an **indirect prompt injection hidden in a legal filing** (instructing any AI reviewer to side with the filer) [drew HN discussion](https://news.ycombinator.com/) — the document-borne-PI threat model reaching non-technical adversaries; facet already covered by the agent-stack trend.
- Physical-world / OT-agent control is entering discourse, pairing with the off-axis [PLCBench](https://arxiv.org/abs/2608.26882) ICS nucleus the radar is watching for a 2nd group.

---

📄 [TRENDS.md](TRENDS.md) · 👁 [watchlist (~25)](TRENDS.md#observation_queue) · 🗂 [reports/](reports/) → [2026-09-02](reports/2026-09-02.md) · 📅 weekly: [2026-W35](reports/weekly/2026-W35.md) · 📘 [AGENTS.md](AGENTS.md) · 🌐 [SOURCES.md](SOURCES.md)
