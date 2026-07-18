# AI Radar

![trends](https://img.shields.io/badge/trends-9-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-4-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-25-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--07--18-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-07-18, weekly recalibration):**
- 🤖 **[Trend 009](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) promoted seed→emerging**: 4 independent groups now span both modalities (LLM malware/C2 code-generation — [TuxBot v3](https://unit42.paloaltonetworks.com/tuxbot-v3-evolution-iot-botnet/) — and operational-automation — [Automated Adversary Emulation via ATT&CK CTI](https://arxiv.org/abs/2607.14566)) with evidence on 2 consecutive days.
- 🔓 **[Trend 001](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) cap rotation**: ["Comment and Control"](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot) (now CVE-2026-47751-backed) finally took the cap slot it had been queued for since 07-13, rotating out SafeClawArena.
- 🔍 **Source registry grew**: promoted [Trend Micro Research](https://www.trendmicro.com/en_us/research.html) and [Oasis Security](https://www.oasis.security/blog) to swept primary sources — surfacing [PromptFiction](https://www.oasis.security/blog/claude-desktop-vulnerability) (a zero-click `claude://` deeplink PI in Claude Desktop, now the top next rotate-candidate for trend 001) and an in-the-wild [claude.ai shared-chat malvertising campaign](https://www.trendmicro.com/en_us/research/26/f/claudeai-shared-chat-abused-in-malvertising.html). Also healed Bishop Fox after weeks of unresolved extraction.
- 📡 **Watchlist steady at 25→25**; 7 non-packaged GitHub repos (llm-attacks, ai-exploits, PurpleLlama, agentdojo, cybench, intercode, L1B3RT4S) downgraded from "swept every run" to a best-effort quarterly check after being confirmed structurally unreachable for a second straight week.

---

## Trends

🌱 2 · 📈 3 · 🚀 4 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-16](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-07-14](https://arxiv.org/abs/2607.12316) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-14](https://arxiv.org/abs/2607.14147) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-07-10](https://arxiv.org/abs/2607.09473) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-07-16](https://arxiv.org/abs/2607.13075) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 📈 emerging | [2026-07-16](https://arxiv.org/abs/2607.14566) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-07-11](https://arxiv.org/abs/2607.10252) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 🌱 seed | [2026-07-14](https://arxiv.org/abs/2607.12340) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 🌱 seed | [2026-07-11](https://arxiv.org/abs/2607.10269) |

---

## 🛠️ Tools & releases

_No fresh GitHub tool-discovery sweep this session (weekly recalibration, not a daily scan) — versions carried from the last daily pass, unchanged since 2026-07-17. Watched tools:_

- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — watched (tool-discovery lane, 2026-07-14): production-ready, Dockerized collection of **38 offensive-security MCP servers / 300+ tools** (Nmap, Ghidra, Nuclei, SQLMap, Hashcat …) exposing classic offensive tooling to AI assistants for agent-driven recon, vuln scanning and binary analysis.
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.121.19** (2026-07-14, latest on npm).
- [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) — LLM red-team & scanning; v2.19.2 (2026-07-06, latest on PyPI).
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — LLM/agent red-teaming framework; v1.0.7 (2026-07-01, latest on PyPI).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — LLM vulnerability scanner; v0.15.1 (unchanged).
- [Azure/PyRIT](https://github.com/Azure/PyRIT) — Python Risk Identification Tool for generative AI; v0.14.0 (unchanged).

---

## Worth studying

- [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/abs/2607.15263) — measures security agents at **fixed cost** (offensive Cybench + defensive Splunk BOTS v1), decomposing inference- vs tool-spend and surfacing distinct red-team vs blue-team scaling regimes — the cost-axis complement to Baselines-Before-Architecture / ScopeJudge before trusting any headline autonomous-security-agent score.
- [Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing](https://arxiv.org/abs/2607.13085) — a reality-check on the autonomous-pentest race: on the 104-task XBOW benchmark, plain default coding-CLI agents (Codex/OpenCode/Pi) under matched model/budget/scoring rival multi-component security harnesses (MAPTA, PentestGPT-V2) — much of the reported gain is the **backbone**, not the bespoke harness.
- [Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation (SkillSec-Eval)](https://arxiv.org/abs/2607.13987) — a lifecycle-aware framework + threat taxonomy for reusable agent skills covering the whole lifecycle (admission → retrieval → planner selection → execution → evolution), run empirically over **327 real-world skills** — vulnerabilities arise at multiple stages beyond execution (cf. trends 001/003).
- [PromptFiction: a one-click flaw that made Claude Desktop act without consent (Oasis Security)](https://www.oasis.security/blog/claude-desktop-vulnerability) — the cleanest zero-click escalation yet on claude.ai/Claude Desktop: a crafted `claude://` deeplink hands the agent a full instruction set with **no send-button confirmation**, ranging from silent conversation exfiltration to code execution depending on config. Reported to and fixed by Anthropic (now the top rotate-candidate for trend 001's next cap slot).
- [The Memory Heist: How I tricked Claude into leaking your deepest secrets (Ayush Paul)](https://www.ayush.digital/blog/the-memory-heist) — the vivid demonstration of the **lethal trifecta** on a shipping consumer AI agent: production claude.ai's memory system (auto-injected daily summary + `conversation_search`) becomes an exfil target once paired with browsing; `web_fetch`'s exfiltration-avoidance allowlist is defeated by chaining its three criteria to reach an attacker URL encoding the stolen memories/PII (now evidence on trend 001).
- [Patriot Bait: One Man, One AI, One Fake Persona (Trend Micro / TrendAI)](https://www.trendmicro.com/en_us/research/26/e/inside-the-influence-and-fraud-patriot-bait-campaign.html) — the vivid in-the-wild reference for **AI-as-operational-infrastructure**: a single low-skilled actor ran a 5-year influence + crypto-fraud campaign by making a jailbroken Gemini / Gemini CLI do C&C setup, credential theft and stolen-key rotation; the jailbreak **persisted** via a poisoned GEMINI.md memory file (now also evidence on trend 009).
- [Antiproof: Synthesizing Vulnerability Detectors and Proofs of Exploitability](https://arxiv.org/abs/2607.12316) — end-to-end AI vuln discovery pairing neuro-symbolic detector **synthesis** (high recall) with proof-of-exploitability **oracles** (automatic validation). Detects **64/66** on BountyBench + a curated KEVBench, +60pp recall over static baselines (now evidence on trend 002).
- [Mako: A Self-Evolving Agentic OS for Autonomous Web Exploitation](https://arxiv.org/abs/2607.11288) — an autonomous exploitation agent that treats its exploit capability as a mutable, versioned **kernel** it extends at runtime, deployed as the LaunchSafe engine. Drives **every one of 104** XBOW CTF-style web targets to a cryptographically fresh flag — the landmark for where deployed autonomous web exploitation stands today.
- [Evaluating AI Models' Capability to Automate Voice Phishing Attacks](https://arxiv.org/abs/2607.09970) — large-scale human-susceptibility study (N=4100 + N=12): U.S. adults exposed to scam audio from leading voice models comply at up to **36%** ("relative-in-distress") / 16.5% overall — voice synthesis + LLMs remove the operator bottleneck that limited vishing to scale.
- [Statistically Undetectable Backdoors in Deep Neural Networks](https://arxiv.org/abs/2607.09532) — an adversarial trainer can plant backdoors that are **statistically undetectable even white-box**, while the secret grants invariance-based adversarial examples for *every* input. The theoretical ceiling on backdoor detection; context for the whole trend-004 cluster.
- [ScopeJudge: Cost-Aware Pre-Execution Gating for Offensive Security Agents](https://arxiv.org/abs/2607.07774) — a single out-of-scope tool call can breach an engagement or void a bounty, and the in/out-of-scope line lives in the user's *request*, not any fixed policy. A 4,897-call pentester-labeled benchmark showing static policy is request-blind (recall ~0). The dataset for real-time scope oversight of autonomous offensive agents.
- [Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents](https://arxiv.org/abs/2607.07474) — agentic red-team benchmarks report compromise as a single bit, discarding *how harmful* the action was. A seven-level (L0–L6) rubric applied to AgentDojo logs exposes cases binary ASR hides — e.g. a defense reporting **0% ASR while still leaking cross-scope** (cf. trend 003).

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- A [Black Hat Europe 2025 "MCP Unchained"](https://www.blackhat.com/eu-25/briefings/schedule/#mcp-unchained-compromising-the-ai-agent-ecosystem-via-its-universal-connector-49228) offensive briefing on compromising the AI-agent ecosystem through MCP stays [queued](TRENDS.md#observation_queue) as a trend-001 rotate-candidate (open the talk's abstract before citing).
- An [AI-agent-stack/memory-PI batch](TRENDS.md#observation_queue) from the Friday cs.CR window (Setup-Complete install-time supply chain, MemPoison, Bad Memory, LogInject, Stop-Means-Stop) remains queued below trend 001's cap.
- HN front page was quiet on offensive-AI this scan (top items were open-weights-model releases and dev tooling); Reddit intermittently reachable, only generic jailbreak/prompt-injection discussion — no earthquake.

---

[TRENDS.md](TRENDS.md) · [watchlist (25)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-07-17](reports/2026-07-17.md) · [weekly: 2026-W29](reports/weekly/2026-W29.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
