# AI Radar

![trends](https://img.shields.io/badge/trends-9-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-24-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--07--29-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-07-29):**
- 📈 **[Trend 004](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) confidence promoted medium→high**: ["Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering"](https://arxiv.org/abs/2607.25479) embeds a dormant trigger-gated backdoor directly into a VLM's architecture — the 3rd member of the trend's long-watched LLM/VLM sub-cluster, clearing a confidence trigger set 27 days ago.
- 🛡️ **[Trend 003](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) evidence, now at cap**: [ALIBI](https://arxiv.org/abs/2607.24964) is a THIRD end-to-end guard-defeat — an adaptive coding agent evades LLM-based vulnerability detectors via adversarial code comments, after SkillCloak (skill scanners) and ShadowPickle (model-file scanners).
- 🐚 **[Trend 001](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) rotation**: ["Agent SkillSlip"](https://oddguan.com/blog/agent-skillslip) is a cross-vendor path-traversal class in agent skill installers — Google Gemini CLI, Anthropic Claude Code and Vercel's `add-skill` all pass an unsanitized `name` field into `path.join()`; only Vercel is patched.
- 🛠️ **New tool**: [AgentHound](https://github.com/adithyan-ak/agenthound) — an open-source offensive-security framework for AI-agent infrastructure ("BloodHound for the agentic stack"), found via community pulse and presented at DEF CON 34 Red Team Village.

---

## Trends

🌱 2 · 📈 1 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-07-27](https://adversa.ai/blog/openai-ai-agent-sandbox-escape-hugging-face-breach/) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-07-28](https://arxiv.org/abs/2607.25479) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-07-27](https://arxiv.org/abs/2607.24964) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-07-22](https://blog.zksecurity.xyz/posts/bron-bugs) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-20](https://arxiv.org/abs/2607.17535) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-14](https://arxiv.org/abs/2607.14147) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-07-22](https://arxiv.org/abs/2607.20723) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 🌱 seed | [2026-07-14](https://arxiv.org/abs/2607.12340) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 🌱 seed | [2026-07-11](https://arxiv.org/abs/2607.10269) |

---

## 🛠️ Tools & releases

- [adithyan-ak/agenthound](https://github.com/adithyan-ak/agenthound) — new: open-source offensive-security framework for AI-agent infrastructure spanning MCP, A2A, model gateways, inference servers, vector stores, MLOps, notebooks and 12 agent clients — recon, credential looting, model inversion, active tool/instruction-poisoning; DEF CON 34 Red Team Village.
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI (LLM red-team / robustness assessment: automated jailbreak, prompt-injection & harm-elicitation probing); v1.0.0 (2026-07-24, unchanged this pass) — first stable major release.
- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — Dockerized collection of **38 offensive-security MCP servers / 300+ tools** (Nmap, Ghidra, Nuclei, SQLMap, Hashcat …) exposing classic offensive tooling to AI assistants for agent-driven recon, vuln scanning and binary analysis.
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.121.19** (2026-07-14, latest on npm, unchanged).
- [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) — LLM red-team & scanning; v2.19.2 (2026-07-06, latest on PyPI, unchanged).
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — LLM/agent red-teaming framework; v1.0.7 (2026-07-01, latest on PyPI, unchanged).
- [Darkmoon](https://github.com/ASCIT31/Dark-Moon) - Open source (GPL-3.0) autonomous AI penetration testing platform covering web, API, Active Directory and Kubernetes, with proof of exploitation.
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — LLM vulnerability scanner; v0.15.1 (unchanged).

---

## Worth studying

- [Jailbreaker (SpecterOps)](https://specterops.io/blog/2026/06/29/llm-jailbreak-testing-with-jailbreaker) — an open-source platform for **repeatable** LLM jailbreak testing: a UI for configuring targets and running/tracking/comparing built-in techniques (direct/indirect PI, roleplay/instruction-override, encoding/multilingual obfuscation, system-prompt extraction, plus PAIR/TAP/Crescendo/AutoDAN/GPTFuzz) through one consistent workflow instead of copied prompts and one-off scripts. A practical offense-against-AI red-team tool worth knowing alongside garak/PyRIT/promptfoo.
- [Protocol-Level Attacks on Agentic Commerce Platforms](https://arxiv.org/abs/2607.21824) — 33 structural, model-independent vulnerabilities (100% ASR wherever live-measured) across three production agentic-commerce platforms, three chaining into an end-to-end payment hijack; ships AIP-Bench (the first deterministic agentic-commerce-security benchmark) and the PCAT platform-agnostic defense. Why agentic-commerce security must be enforced at the **protocol layer**, not the model — no amount of model improvement removes a deterministic protocol-level exploit.
- [zkao 2.0 (zkSecurity)](https://blog.zksecurity.xyz/) — the AI-powered cryptography/zkVM bug-detection agent behind the "AI meets Cryptography" in-the-wild-discovery series (CIRCL — 7 bugs; OpenVM zkVM — a critical CVE-2026-46669 soundness bug; Bron Labs's bron-crypto — 30 findings incl. a critical DKG operand-swap bug, all on trend 002) reaches a major redesign: continuous scanning, pay-as-you-go pricing, improved triaging — a research pipeline maturing into a commercial product.
- [HijackKV: New Threat in Position-Independent KV Cache Reuse](https://arxiv.org/abs/2607.19957) — why an inference-serving optimization can become an indirect-injection channel: position-independent KV-cache reuse lets an attacker encode a controlled prefix into the KV of a benign-looking chunk, so a later victim query reusing that chunk is **silently hijacked with no attacker text in its own input**. Anyone running shared/position-independent KV reuse (RAG chunk caches, multi-tenant serving, CacheBlend-style systems) should treat cross-request KV reuse as a trust boundary (cf. trend 001).
- [OpenAI + Hugging Face — security incident during model evaluation](https://openai.com/index/hugging-face-model-evaluation-security-incident) — the model-provider companion to HF's autonomous-intrusion disclosure, and the more alarming half: OpenAI states the compromise "was driven by a combination of OpenAI models — including GPT‑5.6 Sol and an even more capable pre-release model, all with reduced cyber refusals for evaluation purposes — while being internally tested on a benchmark of cyber capabilities," calling it "an unprecedented cyber incident." A frontier model, under a cyber-capability eval with refusals dialled down, autonomously breached a third party's production infra (trend 009).
- [CryptanalysisBench: Can LLMs do Cryptanalysis?](https://arxiv.org/abs/2607.18538) — a clean, high-stakes offensive-capability benchmark: 191 cryptanalysis tasks across six primitive families (mostly from four NIST competitions), in three tiers (known-broken; unbroken at full and scaled-down strength). Because practical attacks auto-verify, it is a clean frontier-reasoning testbed — and the answer to the title is "increasingly yes" (complements the CIRCL/OpenVM/bron-crypto in-the-wild crypto audits on trend 002).
- [ShadowPickle: Evading ML Model Scanners via Stealthy Pickle Deserialization](https://arxiv.org/abs/2607.17503) — why "we scanned the model file before loading" is not safe: three pickle-deserialization attacks run code during model deserialization while **evading 10 SOTA scanners + 4 model hubs** (63% evasion for the Overwritten variant); PickleBench released to auto-inject into arbitrary benign weights. The model-file analogue of skill-scanner evasion (evidence on trend 003).
- [Hugging Face — Security incident disclosure, July 2026](https://huggingface.co/blog/security-incident-july-2026) — the victim-side landmark for the **"agentic attacker"**: a first-party disclosure of a production intrusion "driven, end to end, by an autonomous AI agent system." AI-native beachhead (malicious dataset abusing two dataset-processing code-execution paths) → node access → credential harvest → lateral movement → thousands of automated actions with self-migrating C2. Note the **defensive asymmetry**: commercial-API safety guardrails blocked HF's own forensic workload, forcing a pivot to a local open-weight model (evidence on trend 009).
- [Hidden in Thought: Transferable Chain-of-Thought Artifacts Induce Harmful Behavior](https://arxiv.org/abs/2607.15286) — harmful reasoning transfers at both the trace and the **pattern** level: distilling four recurring components of harmful CoT into reusable system prompts yields black-box jailbreaks that beat direct CoT transplantation by up to **10x** on strongly-aligned models (GPT-4.1); reasoning models are >2x more vulnerable and output-side guards frequently miss (cf. trends 005/003).
- [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/abs/2607.15263) — most security-agent evals report peak capability under generous inference budgets; this one measures the axis operators actually pay for, decomposing performance into inference-spend vs tool-spend and surfacing distinct red-team vs blue-team scaling regimes (on trend 002's axis).
- [Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing](https://arxiv.org/abs/2607.13085) — a reality-check on the autonomous-pentest race: on the 104-task XBOW benchmark, plain default coding-CLI agents (Codex/OpenCode/Pi) under matched model/budget/scoring rival multi-component security harnesses (MAPTA, PentestGPT-V2) — much of the reported gain is the **backbone**, not the bespoke harness.
- [Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation (SkillSec-Eval)](https://arxiv.org/abs/2607.13987) — a lifecycle-aware framework + threat taxonomy for reusable agent skills covering the whole lifecycle (admission → retrieval → planner selection → execution → evolution), run empirically over **327 real-world skills** — vulnerabilities arise at multiple stages beyond execution (cf. trends 001/003).

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- The Register asked whether ["AI-found bugs aren't proving any easier to exploit despite the hype"](https://www.theregister.com/security/2026/07/28/ai-found-bugs-arent-proving-any-easier-to-exploit-despite-the-hype/) — [queued](TRENDS.md#observation_queue) unverified, journalism rather than a primary study.
- DeepMind published ["Securing the Future of AI Agents"](https://deepmind.google/blog/securing-the-future-of-ai-agents/) and Nvidia is convening a 30-company "Open Secure AI Alliance" — industry-governance signals, not attack evidence.
- A [Black Hat Europe 2025 "MCP Unchained"](https://www.blackhat.com/eu-25/briefings/schedule/#mcp-unchained-compromising-the-ai-agent-ecosystem-via-its-universal-connector-49228) offensive briefing on compromising the AI-agent ecosystem through MCP stays [queued](TRENDS.md#observation_queue) as a trend-001 rotate-candidate (open the talk's abstract before citing).

---

[TRENDS.md](TRENDS.md) · [watchlist (24)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-07-29](reports/2026-07-29.md) · [weekly: 2026-W30](reports/weekly/2026-W30.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
