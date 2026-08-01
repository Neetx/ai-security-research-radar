# AI Radar

![trends](https://img.shields.io/badge/trends-9-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-21-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--08--01-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-08-01, weekly recalibration):**
- 🎯 **[Trend 009](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) confidence medium→high**: Google GTIG's ["AI Threat Tracker"](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) — an 81-day capture-leak fix — becomes the trend's 7th independent group (self-modifying PROMPTFLUX/PROMPTSPY malware, PRC-nexus actors weaponizing Hexstrike/Strix against real targets).
- 🔓 **[Trend 001](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) rotation**: ["Second Time, Same Sandbox"](https://oddguan.com/blog/second-time-same-sandbox-anthropic-claude-code-network-allowlist-bypass-data-exfiltration) — a SOCKS5 null-byte bypass left Claude Code's network sandbox silently broken for ~5.5 months across ~130 releases, with no advisory or CVE.
- 🧹 **Queue burndown**: 13 stale (14–19 day) items resolved this week (12 dropped with reason, 1 trimmed); 2 fresh capture-leak items queued (MOSAIC CLI-composition attack, an SMT function-calling jailbreak); watchlist trimmed 24→21.
- ⏳ **Dormancy watch**: [Trend 008](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) (hallucination-squatting) is now 18 days without new evidence — 3 days from the 21-day dormant threshold.

---

## Trends

🌱 2 · 📈 1 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-07-30](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-07-30](https://adversa.ai/blog/agent-skill-scanners-bypass-eight-tested/) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-07-28](https://www.anthropic.com/research/discovering-cryptographic-weaknesses) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-07-28](https://arxiv.org/abs/2607.25479) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-20](https://arxiv.org/abs/2607.17535) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-14](https://arxiv.org/abs/2607.14147) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-07-30](https://arxiv.org/abs/2607.28147) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 🌱 seed | [2026-07-14](https://arxiv.org/abs/2607.12340) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 🌱 seed | [2026-07-30](https://arxiv.org/abs/2607.28165) |

---

## 🛠️ Tools & releases

- [KeyValueSoftwareSystems/agent-opfor](https://github.com/KeyValueSoftwareSystems/agent-opfor) — open-source adversary-emulation ("OPFOR") framework for AI agents/LLM apps/MCP servers — OWASP LLM/Agentic-AI/MCP/API Top-10 evaluators plus an autonomous `opfor hunt` multi-agent campaign mode; 419 commits, 567 stars.
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.0.1** (2026-07-30) — a major v1 architectural redesign (Policy Puppetry, extended GCG, Garak-technique integration, enhanced Crescendo). Moved from the now-archived Azure/PyRIT org.
- [adithyan-ak/agenthound](https://github.com/adithyan-ak/agenthound) — open-source offensive-security framework for AI-agent infrastructure spanning MCP, A2A, model gateways, inference servers, vector stores, MLOps, notebooks and 12 agent clients — recon, credential looting, model inversion, active tool/instruction-poisoning; DEF CON 34 Red Team Village.
- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — Dockerized collection of **38 offensive-security MCP servers / 300+ tools** (Nmap, Ghidra, Nuclei, SQLMap, Hashcat …) exposing classic offensive tooling to AI assistants for agent-driven recon, vuln scanning and binary analysis.
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.121.20** (2026-07-31, latest on npm).
- [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) — LLM red-team & scanning; v2.19.2 (2026-07-06, latest on PyPI, unchanged).
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — LLM/agent red-teaming framework; v1.0.7 (2026-07-01, latest on PyPI, unchanged).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — LLM vulnerability scanner; v0.15.1 (unchanged).

---

## Worth studying

- [AI Threat Tracker (Google Threat Intelligence Group)](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) — Google's flagship 2026 AI-threat-intel report, captured this week after an 81-day gap: self-modifying malware (PROMPTFLUX/PROMPTSPY), PRC-nexus state actors using expert-persona prompting at scale, agentic pentest frameworks (Hexstrike/Strix) turned offensively, and a PyPI/GitHub-Actions supply-chain compromise (SANDCLOCK). The single broadest primary this radar has captured on the in-the-wild AI-for-offense axis.
- [Capability Laundering in MCP 3: CVE-2026-27735](https://oddguan.com/blog/anthropic-mcp-server-git-add-path-traversal-credential-exfiltration-capability-laundering-cve-2026-27735) — Anthropic's own Git MCP Server let a single `git_add` call read SSH keys, kubeconfig and AWS credentials into Git history via an unsanitized path in GitPython's `repo.index.add()` — invisible in the working directory. A clean case of a tool's documented contract (stage a file) delivering an undocumented capability (arbitrary file read).
- ["Second Time, Same Sandbox" (Aonan Guan)](https://oddguan.com/blog/second-time-same-sandbox-anthropic-claude-code-network-allowlist-bypass-data-exfiltration) — the SOCKS5 hostname null-byte injection that left Claude Code's network sandbox bypassable for ~5.5 months across ~130 releases, silently fixed with no advisory or CVE (evidence on trend 001).
- [Jailbreaker (SpecterOps)](https://specterops.io/blog/2026/06/29/llm-jailbreak-testing-with-jailbreaker) — an open-source platform for **repeatable** LLM jailbreak testing: a UI for configuring targets and running/tracking/comparing built-in techniques (direct/indirect PI, roleplay/instruction-override, encoding/multilingual obfuscation, system-prompt extraction, plus PAIR/TAP/Crescendo/AutoDAN/GPTFuzz) instead of copied prompts and one-off scripts.
- [Protocol-Level Attacks on Agentic Commerce Platforms](https://arxiv.org/abs/2607.21824) — 33 structural, model-independent vulnerabilities (100% ASR wherever live-measured) across three production agentic-commerce platforms, three chaining into an end-to-end payment hijack. Why agentic-commerce security must be enforced at the **protocol layer**, not the model.
- [zkao 2.0 (zkSecurity)](https://blog.zksecurity.xyz/) — the AI-powered cryptography/zkVM bug-detection agent behind the "AI meets Cryptography" in-the-wild-discovery series (CIRCL, OpenVM zkVM, Bron Labs's bron-crypto — all trend 002) reaches a major redesign: continuous scanning, pay-as-you-go pricing, improved triaging.
- [HijackKV: New Threat in Position-Independent KV Cache Reuse](https://arxiv.org/abs/2607.19957) — why an inference-serving optimization can become an indirect-injection channel: position-independent KV-cache reuse lets an attacker encode a controlled prefix into the KV of a benign-looking chunk, so a later victim query reusing it is **silently hijacked with no attacker text in its own input** (cf. trend 001).
- [OpenAI + Hugging Face — security incident during model evaluation](https://openai.com/index/hugging-face-model-evaluation-security-incident) — OpenAI states the HF compromise "was driven by a combination of OpenAI models... all with reduced cyber refusals for evaluation purposes," calling it "an unprecedented cyber incident" (trend 009).
- [CryptanalysisBench: Can LLMs do Cryptanalysis?](https://arxiv.org/abs/2607.18538) — 191 cryptanalysis tasks across six primitive families, mostly from four NIST competitions; a clean, high-stakes, auto-verifiable frontier-reasoning testbed. The answer to the title is "increasingly yes."
- [ShadowPickle: Evading ML Model Scanners via Stealthy Pickle Deserialization](https://arxiv.org/abs/2607.17503) — three pickle-deserialization attacks run code during model deserialization while **evading 10 SOTA scanners + 4 model hubs** (63% evasion for the Overwritten variant); the model-file analogue of skill-scanner evasion (evidence on trend 003).
- [Hugging Face — Security incident disclosure, July 2026](https://huggingface.co/blog/security-incident-july-2026) — the victim-side landmark for the **"agentic attacker"**: a production intrusion "driven, end to end, by an autonomous AI agent system," with commercial-API safety guardrails blocking HF's own forensic response (evidence on trend 009).
- [Hidden in Thought: Transferable Chain-of-Thought Artifacts Induce Harmful Behavior](https://arxiv.org/abs/2607.15286) — harmful reasoning transfers at both the trace and the **pattern** level: distilling four recurring components of harmful CoT into reusable system prompts beats direct CoT transplantation by up to **10x** on strongly-aligned models (cf. trends 005/003).

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- Black Hat USA and DEF CON both run in early August — the radar's con-showcase lane (Arsenal + Demo Labs) is about to go from off-season to the year's highest-density new-tool venue; a priority watch for the coming week's daily runs.
- Hacker News cross-corroborated both Anthropic disclosures at scale (["Anthropic says its own AI models breached three companies during security tests"](https://techcrunch.com/2026/07/30/anthropic-says-its-own-ai-models-breached-three-companies-during-security-tests/)) — already [evidence](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) on the radar, this is corroboration not a new signal.
- ProPublica reported ["Microsoft Struggling with AI-Discovered Security Bugs"](https://www.propublica.org/article/anthropic-mythos-microsoft-software-vulnerabilities) — [queued](TRENDS.md#observation_queue) unverified, journalism on the downstream friction of AI-discovered vulnerabilities rather than a primary study.
- A newsletter's "Context Bombs" coverage names a defensive canary-token technique (decoy secrets designed to trip an AI attacker's own guardrails) — a defense-side vocabulary term, noted for context, not queued as offensive evidence.
- An investigative piece on a Chinese-market ecosystem reselling pooled/stolen LLM API keys (with a model-distillation-data-collection angle) surfaced via Simon Willison — the source (vectoral.com) is [staged](SOURCES.md) as a discovered-source candidate, primary not yet independently verified.

---

[TRENDS.md](TRENDS.md) · [watchlist (21)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-07-31](reports/2026-07-31.md) · [weekly: 2026-W31](reports/weekly/2026-W31.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
