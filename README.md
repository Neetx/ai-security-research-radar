# AI Radar

![trends](https://img.shields.io/badge/trends-9-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-24-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--08--05-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-08-05):**
- 🎣 **[Agent-stack attacks](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) rotation**: [AgentBaiting](https://www.island.io/blog/agentbaiting-how-800-fake-ai-skills-and-mcp-servers-delivered-malware) promoted to evidence — 800+ fake AI Skills/MCP servers among 7,600 malicious repos (14M+ downloads), and Claude Code, Gemini and ChatGPT each discovered and recommended them unprompted, with no link ever shown. An attack on the agent's **discovery layer**, before any code runs.
- 🕵️ **[In-the-wild AI-for-offense](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) rotation**: [DarkReasoning](https://jesta.ai/blog/darkreasoning) promoted to evidence — researchers fingerprinted the exact model driving a live 5-day autonomous attack from inside it, then steered the adversary's own agent into surrendering its 1,000+ victim list.
- 🔬 **[AI vuln discovery](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) new evidence**: Unit 42's [Frontier AI Vulnerability Burst](https://unit42.paloaltonetworks.com/frontier-ai-vulnerability-burst/) — a first-party account of AI industrializing autonomous zero-day discovery in open-source software, collapsing discovery→PoC→validation into a single agent loop and compressing months of review into days.
- 🧪 **New in the queue**: [SkillJack](https://arxiv.org/abs/2608.03509) — the first attack on the experience→skill pipeline of self-evolving agents (safety detection drops 98.5%→11.4% after extraction, 80% persist after deleting the source records); and [Evading CoT Monitoring via model poisoning](https://arxiv.org/abs/2608.02820) — backdoors that keep the reasoning trace benign while triggering attacker behavior.

---

## Trends

🌱 2 · 📈 1 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-08-04](https://unit42.paloaltonetworks.com/frontier-ai-vulnerability-burst/) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-08-03](https://jesta.ai/blog/darkreasoning) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-07-30](https://adversa.ai/blog/agent-skill-scanners-bypass-eight-tested/) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-28](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-07-28](https://arxiv.org/abs/2607.25479) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-14](https://arxiv.org/abs/2607.14147) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-07-31](https://arxiv.org/abs/2607.29378) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 🌱 seed | [2026-08-01](https://arxiv.org/abs/2608.00747) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 🌱 seed | [2026-07-14](https://arxiv.org/abs/2607.12340) |

---

## 🛠️ Tools & releases

- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.16.0** (2026-08-04, latest on PyPI, up from 0.15.1).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.122.0** (2026-08-04, latest on npm).
- [samugit83/redamon](https://github.com/samugit83/redamon) — an AI-powered agentic red-team framework (2.2K stars, 461 forks, 686 commits) with dedicated `agentic` and `ai_attack_surface` modules; surfaced via the GitHub tool-discovery lane.
- [bugbasesecurity/pentest-copilot](https://github.com/bugbasesecurity/pentest-copilot) — **Pentest Copilot V2**, an agentic pentesting workspace (fully autonomous command execution, up to 25 iterations/turn, 16 agent tools); Black Hat USA 2026 Arsenal Major Update.
- [GH05TCREW/pentestagent](https://github.com/GH05TCREW/pentestagent) — **PentestAgent**, a mature (2.9K stars, 570 forks) open-source AI-agent framework for black-box pentesting/bug-bounty — RAG knowledge base, attack playbooks, MCP client/server, async orchestration.
- [KeyValueSoftwareSystems/agent-opfor](https://github.com/KeyValueSoftwareSystems/agent-opfor) — open-source adversary-emulation ("OPFOR") framework for AI agents/LLM apps/MCP servers — OWASP LLM/Agentic/MCP/API Top-10 evaluators plus an autonomous `opfor hunt` campaign mode.
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.0.1** (2026-07-30) — the major v1 architectural redesign (Policy Puppetry, extended GCG, Garak-technique integration).
- [adithyan-ak/agenthound](https://github.com/adithyan-ak/agenthound) — offensive-security framework for AI-agent infrastructure across MCP, A2A, model gateways, inference servers, vector stores and 12 agent clients — recon, credential looting, model inversion, tool/instruction-poisoning; DEF CON 34 Red Team Village.

_DEF CON 34 Demo Labs (Aug 6–9) lists ~10 more on-axis tools — X-Ray Your Agents, PromptPwn, Empire 7, DVAIA, Zealot, AOBTD, MalSkill Lab, BigIron.ai among them — held back until each repo is public and verified._

---

## Worth studying

- [SkillJack: Persistent Skill Backdoors in Self-Evolving Agents](https://arxiv.org/abs/2608.03509) — why "delete the poisoned record" is not enough: the agent's own experience→skill distillation launders malicious intent (safety detection 98.5%→11.4% after extraction), the implanted skill persists after the source records are removed, and some even fire on benign queries. Code on Tencent AI-Infra-Guard.
- [Evading Chain-of-Thought Monitoring Through Model Poisoning](https://arxiv.org/abs/2608.02820) — CoT monitoring is not anomaly-detection-in-a-trace but a trace/response **consistency** question: simple fine-tuning implants backdoors that trigger attacker behavior while the reasoning trace stays entirely benign, routed through a trigger-conditioned pathway the visible reasoning never mentions.
- [AgentBaiting: 800+ fake AI Skills and MCP servers (Island)](https://www.island.io/blog/agentbaiting-how-800-fake-ai-skills-and-mcp-servers-delivered-malware) — the in-the-wild report on the AI capability supply chain: ~7,600 malicious repos, 800+ posing as Skills/MCP servers, 14M+ SmartLoader→StealC downloads, and — the part that matters — agents discovering and **recommending** the malicious repos themselves, treating attacker READMEs as documentation.
- [DarkReasoning (Jesta Security)](https://jesta.ai/blog/darkreasoning) — the first published case identifying the **exact model** behind a live attack (deepseek-v4-flash-free) from inside it, then steering the adversary's own agent into disclosing its operation and a 1,000+ victim list. A working template for interrogating an AI attacker rather than only doing forensics on it.
- [AI Threat Tracker (Google Threat Intelligence Group)](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) — Google's flagship 2026 AI-threat-intel report: self-modifying malware (PROMPTFLUX/PROMPTSPY), PRC-nexus actors using expert-persona prompting at scale, agentic pentest frameworks (Hexstrike/Strix) turned offensively, and a PyPI/GitHub-Actions supply-chain compromise (SANDCLOCK).
- [Capability Laundering in MCP 3: CVE-2026-27735](https://oddguan.com/blog/anthropic-mcp-server-git-add-path-traversal-credential-exfiltration-capability-laundering-cve-2026-27735) — Anthropic's own Git MCP Server let a single `git_add` call read SSH keys, kubeconfig and AWS credentials into Git history via an unsanitized path — invisible in the working directory. A tool's documented contract delivering an undocumented capability.
- ["Second Time, Same Sandbox" (Aonan Guan)](https://oddguan.com/blog/second-time-same-sandbox-anthropic-claude-code-network-allowlist-bypass-data-exfiltration) — the SOCKS5 hostname null-byte injection that left Claude Code's network sandbox bypassable for ~5.5 months across ~130 releases, silently fixed with no advisory or CVE (evidence on the agent-stack trend).
- [Jailbreaker (SpecterOps)](https://specterops.io/blog/2026/06/29/llm-jailbreak-testing-with-jailbreaker) — an open-source platform for **repeatable** LLM jailbreak testing: configurable targets plus built-in techniques (direct/indirect PI, roleplay/override, encoding/multilingual obfuscation, system-prompt extraction, PAIR/TAP/Crescendo/AutoDAN/GPTFuzz).
- [Protocol-Level Attacks on Agentic Commerce Platforms](https://arxiv.org/abs/2607.21824) — 33 structural, model-independent vulnerabilities (100% ASR wherever live-measured) across three production agentic-commerce platforms, three chaining into an end-to-end payment hijack. Why agentic-commerce security must be enforced at the **protocol layer**.
- [zkao 2.0 (zkSecurity)](https://blog.zksecurity.xyz/) — the AI-powered cryptography/zkVM bug-detection agent behind the "AI meets Cryptography" in-the-wild-discovery series (CIRCL, OpenVM zkVM, bron-crypto — all AI vuln discovery) reaches a major redesign: continuous scanning, pay-as-you-go pricing, improved triaging.
- [HijackKV: New Threat in Position-Independent KV Cache Reuse](https://arxiv.org/abs/2607.19957) — why an inference-serving optimization becomes an indirect-injection channel: position-independent KV-cache reuse lets an attacker encode a controlled prefix into the KV of a benign-looking chunk, so a later victim query reusing it is **silently hijacked with no attacker text in its own input**.
- [OpenAI + Hugging Face — security incident during model evaluation](https://openai.com/index/hugging-face-model-evaluation-security-incident) — OpenAI states the HF compromise "was driven by a combination of OpenAI models... all with reduced cyber refusals for evaluation purposes," calling it "an unprecedented cyber incident" (in-the-wild AI-for-offense).

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- **DEF CON 34 (Aug 6–9) is imminent** — Demo Labs lists ~10 on-axis AI/agent offensive tools: agent/MCP/skill supply-chain pentesting, autonomous cloud attack agents, AI-generated-vulnerability exploitation at scale, natural-language malware in agent orchestration, and a "C2 at AI speed". Several repos are not public yet.
- Recurring discourse frames prompt injection as a **defensive** instrument against attacking AI agents ("hack back the AI hacker") — [Mantis](https://arxiv.org/abs/2410.20911), verified this scan, is the open-source reference. Staged as a candidate new axis (2 groups, still below the seed bar).
- Model hubs keep churning out **abliterated/uncensored** open-weight models daily (Heretic-abliterated variants of recent 3B–large models) — a steady leading indicator for the refusal-direction / jailbreak axis.
- Hacker News surfaced a writeup on reaching code execution from an agent's `/init` path via indirect prompt injection — primary not opened this scan, carried unverified.

---

[TRENDS.md](TRENDS.md) · [watchlist (24)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-08-05](reports/2026-08-05.md) · [weekly: 2026-W31](reports/weekly/2026-W31.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
