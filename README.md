# AI Radar

![trends](https://img.shields.io/badge/trends-7-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-4-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-27-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--07--14-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-07-14):**
- 🌱 **New seed — physical-channel injection on embodied AI**: [trend 007](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) formed on the pre-registered 3rd group — [RIPA](https://arxiv.org/abs/2606.28649) (sensory PI on ROS 2 robots) + [overthink-slowdown](https://arxiv.org/abs/2607.01518) (scene-text DoS on LVLM robots) + [Devil in the Lens](https://arxiv.org/abs/2607.10269) (physical PI on VLM smart-glasses): indirect PI delivered through the physical **perception channel** of embodied/wearable agents, bypassing text filters and human review.
- 🚀 **Deployed autonomous web exploitation** → [trend 002](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) evidence: [Mako](https://arxiv.org/abs/2607.11288), a self-evolving agentic OS that extends its own exploit kernel at runtime and drives **all 104 XBOW CTF-style web targets** to a fresh flag (rotated out Revelio; also a study pick).
- 📈 **Model-fingerprinting promoted seed→emerging**: [trend 006](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) +1 evidence [One Token Is Enough](https://arxiv.org/abs/2607.10252) (single-token behavioral fingerprint IDs 165 opaque-serving endpoints) — the 4th core group. Plus [trend 003](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) +1 [MCPZoo](https://arxiv.org/abs/2607.11086) (MCP security-scanner reliability, 7th group).
- 📡 **Watchlist 25→27** (Pass 1: −2 promoted into trend 007, −3 stale burndown, +6 incl. an [AI-vishing automation study](https://arxiv.org/abs/2607.09970) → study pick + AI-social-eng nucleus). **Pass 2** (Black Hat + tool-discovery feeds that were empty at Pass 1 recovered): +1 queued — a new [Black Hat EU-25 "MCP Unchained"](https://www.blackhat.com/eu-25/briefings/schedule/#mcp-unchained-compromising-the-ai-agent-ecosystem-via-its-universal-connector-49228) offensive MCP-attack briefing (strong trend-001 rotate-candidate) — and a new watched tool, [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub). **huntr degraded 2nd pass** (heal-flag); capture-leak clean.

---

## Trends

🌱 1 · 📈 2 · 🚀 4 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-07-13](https://arxiv.org/abs/2607.11288) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-07-10](https://arxiv.org/abs/2607.09473) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-08](https://arxiv.org/abs/2607.07903) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-07](https://arxiv.org/abs/2607.05744) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-07-13](https://arxiv.org/abs/2607.11086) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-07-11](https://arxiv.org/abs/2607.10252) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 🌱 seed | [2026-07-11](https://arxiv.org/abs/2607.10269) |

---

## 🛠️ Tools & releases

- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — **NEW to the watchlist** (tool-discovery lane, 2026-07-14): production-ready, Dockerized collection of **38 offensive-security MCP servers / 300+ tools** (Nmap, Ghidra, Nuclei, SQLMap, Hashcat …) that expose classic offensive tooling to AI assistants for agent-driven recon, vuln scanning and binary analysis.
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — LLM/agent red-teaming framework; **v1.0.7** (2026-07-01, latest on PyPI).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.121.18** (latest on npm).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — LLM vulnerability scanner; v0.15.1 (unchanged).
- [Azure/PyRIT](https://github.com/Azure/PyRIT) — Python Risk Identification Tool for generative AI; v0.14.0 (unchanged).

---

## Worth studying

- [Mako: A Self-Evolving Agentic OS for Autonomous Web Exploitation](https://arxiv.org/abs/2607.11288) — an autonomous exploitation agent that treats its exploit capability as a mutable, versioned **kernel** it extends at runtime (observes its own failures, synthesizes new capabilities, proves them against a live target, hot-loads them back), deployed as the LaunchSafe engine. Drives **every one of 104** XBOW CTF-style web targets to a cryptographically fresh flag — the landmark for where deployed autonomous web exploitation stands today.
- [Evaluating AI Models' Capability to Automate Voice Phishing Attacks](https://arxiv.org/abs/2607.09970) — a large-scale human-susceptibility study (N=4100 + N=12 interviews): U.S. adults exposed to scam audio from leading voice models vs. human baselines comply at up to **36%** ("relative-in-distress") / 16.5% overall, showing voice synthesis + LLMs remove the operator bottleneck that limited vishing to scale. The empirical reference on AI-powered social-engineering effectiveness.
- [Statistically Undetectable Backdoors in Deep Neural Networks](https://arxiv.org/abs/2607.09532) — an adversarial trainer can plant backdoors in a broad class of feedforward NNs that are **statistically undetectable even white-box**, while the secret grants invariance-based adversarial examples for *every* input — provably impossible to generate without it. The theoretical ceiling on backdoor detection; context for the whole trend-004 cluster.
- [Comment and Control: PI to Credential Theft in Claude Code, Gemini CLI, and GitHub Copilot](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot) — first cross-vendor demo that GitHub-comment prompt injection (a PR title / issue comment) hijacks three production GitHub-Actions coding agents into exfiltrating the repo's own Actions secrets, with GitHub as the C2 channel; coordinated Anthropic/Google/GitHub disclosure. The real-world reference for coding-agent-PI-to-credential-theft (cf. trend 001).
- [ScopeJudge: Cost-Aware Pre-Execution Gating for Offensive Security Agents](https://arxiv.org/abs/2607.07774) — a single out-of-scope tool call can breach an engagement or void a bounty, and the in/out-of-scope line is declared in the user's *request*, not any fixed policy. Releases a benchmark of 4,897 pentester-labeled tool calls and shows a static policy is request-blind (recall ~0). The dataset for real-time scope oversight of autonomous offensive agents (cf. trend 002).
- [Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents](https://arxiv.org/abs/2607.07474) — agentic red-team benchmarks report compromise as a single bit, discarding *how harmful* the action was. A reusable seven-level (L0–L6) severity rubric applied to AgentDojo logs exposes cases binary ASR hides — e.g. a defense reporting **0% ASR while still leaking cross-scope** (cf. trend 003).
- [The Balkanization of Execution-Security Research for AI Coding Agents](https://arxiv.org/abs/2607.05743) — systematizes 39 scattered papers (2023–2026) on the execution layer around AI coding agents into 17 categories + 4 confirmed CVEs, surfacing 5 cross-cutting gaps. The reference map tying trends 001 and 002.
- [Beyond Refusal: Aligned vs Abliterated LLMs for Vulnerability Analysis](https://arxiv.org/abs/2607.05842) — isolates the effect of *safety state* (refusal intact vs. refusal-ablated) on defensive-security utility using same-lineage Gemma/Qwen pairs. The clean read on whether abliteration actually buys defensive vuln-analysis capability (cf. trend 005).
- [When Claws Remember but Do Not Tell (WhisperBench)](https://arxiv.org/abs/2607.05189) — full-cycle benchmark (108 cases) for *stealth memory injection* against persistent personal agents: a remote black-box adversary's single email must write poisoned long-term memory, stay hidden in the reply, and alter future behavior. Built on a real IMAP/SMTP email-agent skill.
- [Prompt Injection as Role Confusion](https://arxiv.org/abs/2603.12277) — Ye, Cui & Hadfield-Menell (MIT) trace prompt injection to ROLE CONFUSION: an LLM infers who is speaking from how text *sounds*, not its labeled role; ships internal "role probes" (code released). The conceptual "theory of prompt injection" — also cited as evidence on trend 001.
- [Determinants and Limits of LLM Security-Tool Orchestration (HexStrike-AI)](https://arxiv.org/abs/2607.02873) — across 774 trials it disentangles how much of an offensive agent's capability comes from the model vs. the driving client, and where failure is reasoning-bound vs. missing-tool-bound. The reference for how far open-source autonomous offensive orchestration gets today.
- [Fast Multi-dimensional Refusal Subspaces via RFM-AGOP](https://arxiv.org/abs/2607.02396) — refutes the "refusal is one linear direction" assumption (it lives in a multi-dimensional subspace) and recovers that subspace in *seconds*, even on long-reasoning-trace models. The reusable technique for refusal steering/monitoring — the same subspace drives both attack and defense.

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- Surfaced via the Black Hat pointer lane (Pass 2): a [Black Hat Europe 2025 "MCP Unchained"](https://www.blackhat.com/eu-25/briefings/schedule/#mcp-unchained-compromising-the-ai-agent-ecosystem-via-its-universal-connector-49228) offensive briefing on compromising the AI-agent ecosystem through MCP (the "Universal Connector") — [queued](TRENDS.md#observation_queue) as a strong trend-001 rotate-onto-evidence candidate (open the talk's full abstract before citing).
- A GitHub-Actions coding-agent PI surface keeps drawing independent researchers: alongside the (verified) ["Comment and Control"](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot) disclosure, a 2nd researcher's "Trusting Claude With a Knife" (PI→RCE in Claude Code Action) is [queued unverified](TRENDS.md#observation_queue) pending an open.
- [Jailbreaker](TRENDS.md#observation_queue) — an open-source repeatable LLM-jailbreak-testing platform (PAIR/TAP/Crescendo/AutoDAN/GPTFuzz) surfaced via tldrsec #336 — [queued unverified](TRENDS.md#observation_queue) as offensive jailbreak tooling pending a look at the primary repo.
- The hallucination-squatting nucleus (still 2 groups) — attackers exploiting *predictable* LLM hallucinations of package/repo/skill/domain names — stays [queued](TRENDS.md#observation_queue) pending a 3rd independent group.
- Anthropic's Alibaba-distillation accusation (a private letter to US Senators, public via press ~06-24) is well-corroborated across outlets but still has no direct Anthropic/Alibaba primary — [queued unverified](TRENDS.md#observation_queue). No new HN/Reddit earthquake this pass.

---

[TRENDS.md](TRENDS.md) · [watchlist (27)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-07-14](reports/2026-07-14.md) · [weekly: 2026-W28](reports/weekly/2026-W28.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
