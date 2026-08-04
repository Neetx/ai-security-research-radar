# AI Radar

![trends](https://img.shields.io/badge/trends-9-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-23-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--08--04-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-08-04):**
- 🪱 **[Trend 001](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) rotation**: the first public [document-borne self-replicating AI worm](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word) — Copilot for Word copies an attacker's hidden instructions into the documents it writes, so each output becomes a new carrier. Disclosed to MSRC over 144 days; no fix covers the full class.
- 💤 **[Trend 008](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) dormancy REVERSED**: the check run to confirm yesterday's pre-announced `dormant` move instead found two uncaptured primaries — [127 package names every frontier model invents](https://arxiv.org/abs/2605.17062) (53 still registrable) and the [first counter-result](https://doi.org/10.5281/zenodo.21199427) showing hallucinated names are essentially never claimed. The axis was active; the radar was blind to it.
- 🔬 **[Trend 002](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) rotation**: an [automated research pipeline](https://embracethered.com/blog/posts/2026/pipewire-flatpak-linux-sandbox-escape-cve-2026-5674) run by one researcher found CVE-2026-5674 — a Flatpak sandbox escape via PipeWire's never-validated auth cookie, in a daemon shipped by default on Fedora/Ubuntu/Debian.
- 🎣 **In the wild**: [AgentBaiting](https://www.island.io/blog/agentbaiting-how-800-fake-ai-skills-and-mcp-servers-delivered-malware) — 800+ fake AI Skills and MCP servers among 7,600 malicious repos, and Claude Code, Gemini and ChatGPT each discovered and recommended them unprompted, with no link ever shown.

---

## Trends

🌱 2 · 📈 1 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-07-30](https://embracethered.com/blog/posts/2026/pipewire-flatpak-linux-sandbox-escape-cve-2026-5674) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-07-30](https://adversa.ai/blog/agent-skill-scanners-bypass-eight-tested/) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-07-30](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-28](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-07-28](https://arxiv.org/abs/2607.25479) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-14](https://arxiv.org/abs/2607.14147) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-07-31](https://arxiv.org/abs/2607.29378) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 🌱 seed | [2026-08-01](https://arxiv.org/abs/2608.00747) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 🌱 seed | [2026-07-14](https://arxiv.org/abs/2607.12340) |

---

## 🛠️ Tools & releases

- [samugit83/redamon](https://github.com/samugit83/redamon) — **new to the radar**: an AI-powered agentic red-team framework (2.2K stars, 461 forks, 686 commits) with dedicated `agentic` and `ai_attack_surface` modules; surfaced this scan via the GitHub tool-discovery lane.
- [bugbasesecurity/pentest-copilot](https://github.com/bugbasesecurity/pentest-copilot) — **Pentest Copilot V2**, an agentic pentesting workspace (fully autonomous command execution, up to 25 iterations/turn, 16 agent tools); showcased as a Major Update at Black Hat USA 2026 Arsenal.
- [GH05TCREW/pentestagent](https://github.com/GH05TCREW/pentestagent) — **PentestAgent**, a mature (2.9K stars, 570 forks) open-source AI-agent framework for black-box pentesting/bug-bounty workflows — RAG knowledge base, attack playbooks, MCP client/server, async task orchestration.
- [KeyValueSoftwareSystems/agent-opfor](https://github.com/KeyValueSoftwareSystems/agent-opfor) — open-source adversary-emulation ("OPFOR") framework for AI agents/LLM apps/MCP servers — OWASP LLM/Agentic-AI/MCP/API Top-10 evaluators plus an autonomous `opfor hunt` multi-agent campaign mode; 419 commits, 567 stars.
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.0.1** (2026-07-30) — a major v1 architectural redesign (Policy Puppetry, extended GCG, Garak-technique integration, enhanced Crescendo). Moved from the now-archived Azure/PyRIT org.
- [adithyan-ak/agenthound](https://github.com/adithyan-ak/agenthound) — open-source offensive-security framework for AI-agent infrastructure spanning MCP, A2A, model gateways, inference servers, vector stores, MLOps, notebooks and 12 agent clients — recon, credential looting, model inversion, active tool/instruction-poisoning; DEF CON 34 Red Team Village.
- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — Dockerized collection of **38 offensive-security MCP servers / 300+ tools** (Nmap, Ghidra, Nuclei, SQLMap, Hashcat …) exposing classic offensive tooling to AI assistants for agent-driven recon, vuln scanning and binary analysis.
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.121.20** (2026-07-31, latest on npm).

_DEF CON 34 Demo Labs (Aug 6–9) lists ~10 more on-axis tools — X-Ray Your Agents, PromptPwn, DVAIA, Zealot, AOBTD, MalSkill Lab among them — held back until each repo is public and verified._

---

## Worth studying

- [AgentBaiting: 800+ fake AI Skills and MCP servers (Island)](https://www.island.io/blog/agentbaiting-how-800-fake-ai-skills-and-mcp-servers-delivered-malware) — the in-the-wild report on the AI capability supply chain: ~7,600 malicious repos, 800+ posing as Skills/MCP servers, 600+ registry listings, 14M+ SmartLoader→StealC downloads. The mechanism that matters is **AgentBaiting** — agents discovering and recommending the malicious repos themselves, treating attacker READMEs as documentation, with no link ever shown to them.
- [DarkReasoning (Jesta Security)](https://jesta.ai/blog/darkreasoning) — the first published case identifying the **exact model** behind a live attack (deepseek-v4-flash-free) from inside the attack, then steering the adversary's own agent into disclosing its operation and a 1,000+ victim list. A working template for interrogating an AI attacker rather than only doing forensics on it.
- [AI Threat Tracker (Google Threat Intelligence Group)](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) — Google's flagship 2026 AI-threat-intel report: self-modifying malware (PROMPTFLUX/PROMPTSPY), PRC-nexus state actors using expert-persona prompting at scale, agentic pentest frameworks (Hexstrike/Strix) turned offensively, and a PyPI/GitHub-Actions supply-chain compromise (SANDCLOCK).
- [Capability Laundering in MCP 3: CVE-2026-27735](https://oddguan.com/blog/anthropic-mcp-server-git-add-path-traversal-credential-exfiltration-capability-laundering-cve-2026-27735) — Anthropic's own Git MCP Server let a single `git_add` call read SSH keys, kubeconfig and AWS credentials into Git history via an unsanitized path — invisible in the working directory. A tool's documented contract delivering an undocumented capability.
- ["Second Time, Same Sandbox" (Aonan Guan)](https://oddguan.com/blog/second-time-same-sandbox-anthropic-claude-code-network-allowlist-bypass-data-exfiltration) — the SOCKS5 hostname null-byte injection that left Claude Code's network sandbox bypassable for ~5.5 months across ~130 releases, silently fixed with no advisory or CVE (evidence on trend 001).
- [Jailbreaker (SpecterOps)](https://specterops.io/blog/2026/06/29/llm-jailbreak-testing-with-jailbreaker) — an open-source platform for **repeatable** LLM jailbreak testing: configurable targets plus built-in techniques (direct/indirect PI, roleplay/instruction-override, encoding/multilingual obfuscation, system-prompt extraction, PAIR/TAP/Crescendo/AutoDAN/GPTFuzz) instead of copied prompts and one-off scripts.
- [Protocol-Level Attacks on Agentic Commerce Platforms](https://arxiv.org/abs/2607.21824) — 33 structural, model-independent vulnerabilities (100% ASR wherever live-measured) across three production agentic-commerce platforms, three chaining into an end-to-end payment hijack. Why agentic-commerce security must be enforced at the **protocol layer**, not the model.
- [zkao 2.0 (zkSecurity)](https://blog.zksecurity.xyz/) — the AI-powered cryptography/zkVM bug-detection agent behind the "AI meets Cryptography" in-the-wild-discovery series (CIRCL, OpenVM zkVM, bron-crypto — all trend 002) reaches a major redesign: continuous scanning, pay-as-you-go pricing, improved triaging.
- [HijackKV: New Threat in Position-Independent KV Cache Reuse](https://arxiv.org/abs/2607.19957) — why an inference-serving optimization becomes an indirect-injection channel: position-independent KV-cache reuse lets an attacker encode a controlled prefix into the KV of a benign-looking chunk, so a later victim query reusing it is **silently hijacked with no attacker text in its own input**.
- [OpenAI + Hugging Face — security incident during model evaluation](https://openai.com/index/hugging-face-model-evaluation-security-incident) — OpenAI states the HF compromise "was driven by a combination of OpenAI models... all with reduced cyber refusals for evaluation purposes," calling it "an unprecedented cyber incident" (trend 009).
- [CryptanalysisBench: Can LLMs do Cryptanalysis?](https://arxiv.org/abs/2607.18538) — 191 cryptanalysis tasks across six primitive families, mostly from four NIST competitions; a clean, high-stakes, auto-verifiable frontier-reasoning testbed. The answer to the title is "increasingly yes."
- [ShadowPickle: Evading ML Model Scanners via Stealthy Pickle Deserialization](https://arxiv.org/abs/2607.17503) — three pickle-deserialization attacks run code during model deserialization while **evading 10 SOTA scanners + 4 model hubs**; the model-file analogue of skill-scanner evasion (evidence on trend 003).

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- **DEF CON 34 Demo Labs is live** (Aug 6–9) with ~10 on-axis AI/agent offensive tools — agent/MCP/skill supply-chain pentesting, autonomous cloud attack agents, AI-generated-vulnerability exploitation at scale, and natural-language malware in agent orchestration. Several repos are not public yet.
- A Reddit thread pointed at a claim that researchers had steered an attacking LLM agent into surrendering a 1,000+ victim list — [followed to the primary](https://jesta.ai/blog/darkreasoning) and verified this scan.
- Hacker News surfaced a writeup on reaching code execution from an agent's `/init` path via indirect prompt injection — primary not opened this scan, carried unverified.
- Recurring discourse frames prompt injection as a **defensive** instrument against attacking AI agents (a "hack back the AI hacker" framing). Staged as a candidate new axis; the underlying primaries are not yet verified.

---

[TRENDS.md](TRENDS.md) · [watchlist (23)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-08-04](reports/2026-08-04.md) · [weekly: 2026-W31](reports/weekly/2026-W31.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
