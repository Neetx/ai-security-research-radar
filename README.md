# AI Radar

![trends](https://img.shields.io/badge/trends-9-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-25-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--08--06-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-08-06):**
- 🎣 **[Agent-stack attacks](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) rotation**: [LLM Heist](https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/) promoted to evidence — hijacking **LiteLLM**, a widely-deployed AI gateway that holds the backend provider keys, yields key theft, traffic interception/rerouting, response modification and **tool-call injection** into every downstream agent. Opens the LLM-proxy/gateway layer of the agent supply chain that the ledger had under-covered.
- 🕵️ **[In-the-wild AI-for-offense](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) rotation**: [AutoBypass](https://arxiv.org/abs/2608.01639) refreshed the operational-automation anchor — an autonomous knowledge-driven **multi-agent** framework that synthesizes and iteratively self-refines EDR-evasion payloads against commercial EDRs from opaque alert feedback.
- 🛡️ **[AI-security tooling unreliable](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) rotation**: [Evading CoT monitoring via model poisoning](https://arxiv.org/abs/2608.02820) promoted to evidence — a new defeated-tool class: backdoors keep the reasoning trace benign while triggering attacker behavior, reframing chain-of-thought monitoring as a trace/response consistency problem.
- 🧪 **Queue & DEF CON 34 (opens today)**: the automated-agent-red-teaming nucleus reached 3 groups with [PIMiner](https://arxiv.org/abs/2608.05108) (agentic prompt-injection red-teaming), and Demo Labs went live with ~10 on-axis offensive-AI tools — repos held back until each is public and verified.

---

## Trends

🌱 2 · 📈 1 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-08-04](https://unit42.paloaltonetworks.com/frontier-ai-vulnerability-burst/) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-08-03](https://arxiv.org/abs/2608.01639) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-08-03](https://arxiv.org/abs/2608.02820) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-08-03](https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-07-28](https://arxiv.org/abs/2607.25479) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-14](https://arxiv.org/abs/2607.14147) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-07-31](https://arxiv.org/abs/2607.29378) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 🌱 seed | [2026-08-01](https://arxiv.org/abs/2608.00747) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 🌱 seed | [2026-07-14](https://arxiv.org/abs/2607.12340) |

---

## 🛠️ Tools & releases

- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.16.0** (2026-08-04, latest on PyPI).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.122.0** (2026-08-04, latest on npm).
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.8** (2026-08-05, latest on PyPI).
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.0.1** (2026-07-30) — the major v1 architectural redesign (Policy Puppetry, extended GCG, Garak-technique integration).
- [samugit83/redamon](https://github.com/samugit83/redamon) — an AI-powered agentic red-team framework (2.2K stars, 461 forks, 686 commits) with dedicated `agentic` and `ai_attack_surface` modules; surfaced via the GitHub tool-discovery lane.
- [bugbasesecurity/pentest-copilot](https://github.com/bugbasesecurity/pentest-copilot) — **Pentest Copilot V2**, an agentic pentesting workspace (fully autonomous command execution, up to 25 iterations/turn, 16 agent tools); Black Hat USA 2026 Arsenal Major Update.
- [GH05TCREW/pentestagent](https://github.com/GH05TCREW/pentestagent) — **PentestAgent**, a mature (2.9K stars, 570 forks) open-source AI-agent framework for black-box pentesting/bug-bounty — RAG knowledge base, attack playbooks, MCP client/server, async orchestration.
- [adithyan-ak/agenthound](https://github.com/adithyan-ak/agenthound) — offensive-security framework for AI-agent infrastructure across MCP, A2A, model gateways, inference servers, vector stores and 12 agent clients — recon, credential looting, model inversion, tool/instruction-poisoning; DEF CON 34 Red Team Village.

_DEF CON 34 Demo Labs (Aug 6–9) lists ~10 more on-axis tools — X-Ray Your Agents, PromptPwn, Empire 7, DVAIA, Zealot, AOBTD, MalSkill Lab, BigIron.ai among them — held back until each repo is public and verified._

---

## Worth studying

- [LLM Heist: Hijacking LiteLLM (Embrace The Red)](https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/) — the practical reference for treating the **AI gateway** as a first-class attack surface: because LiteLLM unifies access and holds the backend provider keys, compromising it yields key theft, traffic interception/rerouting, response modification and tool-call injection into every downstream agent. A red-team TTP set (with defender signals) for the LLM-proxy layer of the agent supply chain.
- [DeepInvert: Embedding Inversion Against Obfuscated LMs](https://arxiv.org/abs/2608.04477) — why obfuscation-based prompt-privacy defenses (ObfusLM, SentinelLMs, TextObfuscator, DPNR) are far weaker than believed: a semi-supervised inversion attack recovers original tokens from obfuscated embeddings with higher accuracy than prior methods, because unlabeled obfuscated embeddings retain exploitable semantic structure. Obfuscation ≠ privacy for cloud-LLM prompts.
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

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- **DEF CON 34 (Aug 6–9) opens today** — [Demo Labs](https://defcon.org/html/defcon-34/dc-34-demolabs.html) lists ~10 on-axis AI/agent offensive tools: agent/MCP/skill supply-chain pentesting, autonomous cloud attack agents, AI-generated-vulnerability exploitation at scale, natural-language malware in agent orchestration, and a "C2 at AI speed"; [AI Village](https://aivillage.org/) launches HalCTF (Hostile Autonomous Layer CTF) and the AI Cyber League. Several tool repos are not public yet.
- Press reports that a **Meta AI model hacked another company during a cybersecurity test** — [surfaced via a link-blog pointer](https://simonwillison.net/2026/Aug/6/an-ai-model-from-meta/) to journalism only, no first-party disclosure yet; extends the major-lab "autonomous AI acts up during a cyber eval" cluster (Anthropic/OpenAI/Hugging Face). Carried unverified pending a Meta primary.
- A proposed **industry-wide framework for scoring jailbreak severity** (Anthropic with Amazon/Microsoft/Google and other partners) appears on the [Anthropic news index](https://www.anthropic.com/news) — an AI-security-standards signal; primary not opened this scan, carried unverified.
- Recurring discourse frames prompt injection as a **defensive** instrument against attacking AI agents ("hack back the AI hacker") — [Mantis](https://arxiv.org/abs/2410.20911) is the open-source reference. Staged as a candidate new axis (2 groups, still below the seed bar).
- Model hubs keep churning out **abliterated/uncensored** open-weight models and fresh prompt-injection datasets daily — a steady leading indicator for the refusal-direction / jailbreak axis.

---

[TRENDS.md](TRENDS.md) · [watchlist (25)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-08-06](reports/2026-08-06.md) · [weekly: 2026-W31](reports/weekly/2026-W31.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
