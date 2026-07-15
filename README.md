# AI Radar

![trends](https://img.shields.io/badge/trends-8-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-4-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-26-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--07--15-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-07-15):**
- 🌱 **New seed — weaponized LLM hallucination (slopsquatting)**: [trend 008](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) formed on the pre-registered 3rd group — [Unit 42 "Phantom Squatting"](https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/) (in-the-wild registration of hallucinated **domains**) + [Beware of Agentic Botnets](https://arxiv.org/abs/2607.07433) (hallucinated **repo/skill** names → promptware botnet) + [Skills That Don't Exist](https://arxiv.org/abs/2607.12340) (15k-prompt measurement of hallucinated-**skill** installs). Shared mechanism: an LLM's *predictable* resource-name hallucination, pre-registered, becomes a supply-chain delivery channel.
- 🕵️ **In-the-wild AI-as-offensive-infrastructure**: [Trend Micro "Patriot Bait"](https://www.trendmicro.com/en_us/research/26/e/inside-the-influence-and-fraud-patriot-bait-campaign.html) — a solo actor ran a jailbroken **Gemini CLI as C2 / credential-theft infrastructure** (memory-file jailbreak persistence, ~6-min C&C migration at ~11% human effort). [Queued](TRENDS.md#observation_queue) + study pick; Trend Micro staged as a discovered source.
- 🔎 **AI-for-offense vuln discovery** → [trend 002](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) rotate-candidates queued: [Antiproof](https://arxiv.org/abs/2607.12316) (detector synthesis + proof-of-exploitability oracles, **64/66** on BountyBench) leads a batch also incl. AutoTrace, "Trust but Verify?" (**38.9%** of agent PRs carry security misconfigs) and a reverse-engineering [representation-confusion attack](https://arxiv.org/abs/2607.12507).
- 📡 **Watchlist 27→26**: −2 promoted into trend 008, −1 stale drop (Alibaba-distillation intake, no primary in 3 weeks), +2 (the 002 batch; Patriot Bait). New watched-tool release: [promptfoo v0.121.19](https://github.com/promptfoo/promptfoo) (2026-07-14). capture-leak clean (118 ids / 0).

---

## Trends

🌱 2 · 📈 2 · 🚀 4 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-07-13](https://arxiv.org/abs/2607.11288) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-07-10](https://arxiv.org/abs/2607.09473) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-08](https://arxiv.org/abs/2607.07903) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-07](https://arxiv.org/abs/2607.05744) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-07-13](https://arxiv.org/abs/2607.11086) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-07-11](https://arxiv.org/abs/2607.10252) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 🌱 seed | [2026-07-11](https://arxiv.org/abs/2607.10269) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 🌱 seed | [2026-07-14](https://arxiv.org/abs/2607.12340) |

---

## 🛠️ Tools & releases

- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — watched (tool-discovery lane, 2026-07-14): production-ready, Dockerized collection of **38 offensive-security MCP servers / 300+ tools** (Nmap, Ghidra, Nuclei, SQLMap, Hashcat …) exposing classic offensive tooling to AI assistants for agent-driven recon, vuln scanning and binary analysis.
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.121.19** (2026-07-14, latest on npm).
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — LLM/agent red-teaming framework; v1.0.7 (2026-07-01, latest on PyPI).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — LLM vulnerability scanner; v0.15.1 (unchanged).
- [Azure/PyRIT](https://github.com/Azure/PyRIT) — Python Risk Identification Tool for generative AI; v0.14.0 (unchanged).

---

## Worth studying

- [Patriot Bait: One Man, One AI, One Fake Persona (Trend Micro / TrendAI)](https://www.trendmicro.com/en_us/research/26/e/inside-the-influence-and-fraud-patriot-bait-campaign.html) — the vivid in-the-wild reference for **AI-as-operational-infrastructure**: a single low-skilled actor ran a 5-year influence + crypto-fraud campaign by making a jailbroken Gemini / Gemini CLI do C&C setup and migration, credential theft, stolen-API-key rotation and content generation. The jailbreak **persisted** by poisoning the agent's own GEMINI.md memory file (auto-reloaded each session). ~17k subscribers, 73 stolen keys, 29 hacked WordPress admins, ≥1 drained wallet; a follow-on log analysis clocks a full C&C migration in ~6 min at ~11% human effort.
- [Antiproof: Synthesizing Vulnerability Detectors and Proofs of Exploitability](https://arxiv.org/abs/2607.12316) — end-to-end AI vuln discovery pairing neuro-symbolic detector **synthesis** (high recall) with proof-of-exploitability **oracles** (automatic validation). Detects **64/66** on BountyBench + a curated KEVBench, +60pp recall over static baselines — where automatic discovery *with self-validation* stands (cf. trend 002).
- [Mako: A Self-Evolving Agentic OS for Autonomous Web Exploitation](https://arxiv.org/abs/2607.11288) — an autonomous exploitation agent that treats its exploit capability as a mutable, versioned **kernel** it extends at runtime, deployed as the LaunchSafe engine. Drives **every one of 104** XBOW CTF-style web targets to a cryptographically fresh flag — the landmark for where deployed autonomous web exploitation stands today.
- [Evaluating AI Models' Capability to Automate Voice Phishing Attacks](https://arxiv.org/abs/2607.09970) — large-scale human-susceptibility study (N=4100 + N=12): U.S. adults exposed to scam audio from leading voice models comply at up to **36%** ("relative-in-distress") / 16.5% overall — voice synthesis + LLMs remove the operator bottleneck that limited vishing to scale.
- [Statistically Undetectable Backdoors in Deep Neural Networks](https://arxiv.org/abs/2607.09532) — an adversarial trainer can plant backdoors that are **statistically undetectable even white-box**, while the secret grants invariance-based adversarial examples for *every* input. The theoretical ceiling on backdoor detection; context for the whole trend-004 cluster.
- [Comment and Control: PI to Credential Theft in Claude Code, Gemini CLI, and GitHub Copilot](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot) — first cross-vendor demo that GitHub-comment prompt injection hijacks three production GitHub-Actions coding agents into exfiltrating the repo's own Actions secrets, with GitHub as the C2 channel; coordinated Anthropic/Google/GitHub disclosure (cf. trend 001).
- [ScopeJudge: Cost-Aware Pre-Execution Gating for Offensive Security Agents](https://arxiv.org/abs/2607.07774) — a single out-of-scope tool call can breach an engagement or void a bounty, and the in/out-of-scope line lives in the user's *request*, not any fixed policy. A 4,897-call pentester-labeled benchmark showing static policy is request-blind (recall ~0). The dataset for real-time scope oversight of autonomous offensive agents.
- [Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents](https://arxiv.org/abs/2607.07474) — agentic red-team benchmarks report compromise as a single bit, discarding *how harmful* the action was. A seven-level (L0–L6) rubric applied to AgentDojo logs exposes cases binary ASR hides — e.g. a defense reporting **0% ASR while still leaking cross-scope** (cf. trend 003).
- [The Balkanization of Execution-Security Research for AI Coding Agents](https://arxiv.org/abs/2607.05743) — systematizes 39 scattered papers (2023–2026) on the execution layer around AI coding agents into 17 categories + 4 confirmed CVEs, surfacing 5 cross-cutting gaps. The reference map tying trends 001 and 002.
- [When Claws Remember but Do Not Tell (WhisperBench)](https://arxiv.org/abs/2607.05189) — full-cycle benchmark (108 cases) for *stealth memory injection* against persistent personal agents: a remote adversary's single email must write poisoned long-term memory, stay hidden in the reply, and alter future behavior. Built on a real IMAP/SMTP email-agent skill.
- [Prompt Injection as Role Confusion](https://arxiv.org/abs/2603.12277) — Ye, Cui & Hadfield-Menell (MIT) trace prompt injection to ROLE CONFUSION: an LLM infers who is speaking from how text *sounds*, not its labeled role; ships internal "role probes" (code released) — the conceptual "theory of prompt injection" (also evidence on trend 001).

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- **Jailbroken Gemini run as live offensive infrastructure**: surfaced via HN → The Register (07-14) → a Trend Micro / TrendAI "Patriot Bait" report — a real Russian-speaking actor drove a jailbroken Gemini CLI for C&C setup/migration, credential theft and stolen-key rotation, persisting the jailbreak via a poisoned GEMINI.md memory file. [Queued](TRENDS.md#observation_queue) as in-the-wild AI-for-offense operational misuse; Trend Micro staged as a discovered source.
- A [Black Hat Europe 2025 "MCP Unchained"](https://www.blackhat.com/eu-25/briefings/schedule/#mcp-unchained-compromising-the-ai-agent-ecosystem-via-its-universal-connector-49228) offensive briefing on compromising the AI-agent ecosystem through MCP (the "Universal Connector") stays [queued](TRENDS.md#observation_queue) as a strong trend-001 rotate-onto-evidence candidate (open the talk's full abstract before citing).
- A GitHub-Actions coding-agent PI surface keeps drawing independent researchers: alongside the (verified) ["Comment and Control"](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot) disclosure, a 2nd researcher's "Trusting Claude With a Knife" (PI→RCE in Claude Code Action) is [queued unverified](TRENDS.md#observation_queue) pending an open.
- [Jailbreaker](TRENDS.md#observation_queue) — an open-source repeatable LLM-jailbreak-testing platform (PAIR/TAP/Crescendo/AutoDAN/GPTFuzz) surfaced via tldrsec #336 — [queued unverified](TRENDS.md#observation_queue) pending a look at the primary repo.

---

[TRENDS.md](TRENDS.md) · [watchlist (26)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-07-15](reports/2026-07-15.md) · [weekly: 2026-W28](reports/weekly/2026-W28.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
