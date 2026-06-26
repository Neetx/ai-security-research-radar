# AI Security Radar

Autonomous radar tracking the **offensive AI-security frontier** — tools, releases and
research — on two coupled fronts: **AI for offense** (LLM red-teaming, autonomous
pentest/exploitation, AI-driven vulnerability discovery) and **offense against AI**
(jailbreaking, prompt injection, steering vectors, model extraction, agent/MCP attacks).
Primary-source trend ledger + study shelf, refreshed by a daily scan and a weekly
recalibration.

> This page is fully derived from [`TRENDS.md`](TRENDS.md) — regenerated each run, never
> hand-edited. Source of truth is the ledger.

![trends](https://img.shields.io/badge/trends-3-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-2-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-22-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--06--26-2f9e44?style=flat-square)

**Since last scan (2026-06-26):**
- [Agent / MCP attack surface](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) (🚀 accelerating) **+2 evidence**: [ShareLock](https://arxiv.org/abs/2606.27027) disperses a tool-poisoning payload across *multiple* cooperating MCP tools to evade TPA detectors, and [Embrace The Red's computer-use TOCTOU](https://embracethered.com/blog/posts/2026/toctou-agent-what-you-click-is-not-what-you-get/) turns a confirmed click into a different action via a race condition.
- [LLM vuln discovery & repair](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) (🚀 accelerating) **+1 evidence**: [Chai](https://arxiv.org/abs/2606.26933) pushes autonomous AI vuln discovery into *cryptographic misuse* — a class with no instrumentation to confirm bugs — via AI-augmented differential testing.
- [AI-security tooling unreliable](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) **promoted 🌱 seed → 📈 emerging**: a 4th group — [Inherited Circuits](https://arxiv.org/abs/2606.27091) shows a fine-tuned security classifier is evadable by behavior-preserving transformations *and* the failure is invisible to standard evaluation.
- **Watchlist 19 → 22** — added a 2nd diffusion-poisoning group (TEMPO-Diffusion), an agentic-RAG red-team (MIRROR), bandit-selected jailbreaks, and agent-skill runtime enforcement (VIGIL) → [observation_queue](TRENDS.md#observation_queue). **Worth studying +1**: [SoK on out-of-band prompt-injection defenses](https://arxiv.org/abs/2606.26479).

## Trends

🌱 0 · 📈 1 · 🚀 2 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Agent / MCP attack surface](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-06-25](https://arxiv.org/abs/2606.27027) |
| [LLM vuln discovery & repair](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-06-25](https://arxiv.org/abs/2606.26933) |
| [AI-security tooling unreliable](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-06-25](https://arxiv.org/abs/2606.27091) |

## Worth studying

- [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents](https://arxiv.org/abs/2606.26479) — organizes the 2024–2026 wave of out-of-band agent defenses (CaMeL, FIDES, Progent, RTBAS, FORGE) as classical Biba integrity / reference-monitor / least-privilege, then stress-tests them with adaptive attacks — the reference map for "enforce security outside the model" and how durable their near-100% AgentDojo numbers are.
- [SoK: AI Secure Code Generation (Patir, Guo, Cai, Hu)](https://arxiv.org/abs/2606.25195) — systematizes what today's models and coding agents can/cannot do for secure code via a three-level framework (NL understanding → secure generation → agentic workflows), mapping where prompting/fine-tuning/RL/agentic methods help and why failures persist — the map for the "(in)security of AI-written code" problem.
- [Mapping AI-enabled cyber threats: the LLM ATT&CK Navigator (Anthropic FRT)](https://www.anthropic.com/research/attack-navigator) — 832 real threat actors observed misusing models, mapped to MITRE ATT&CK: 69% used T1587 (Develop Capabilities), 560 on malware development — in-the-wild ground truth for the "AI for offense" axis.
- [Measuring LLMs' ability to develop exploits (Anthropic FRT)](https://www.anthropic.com/research/exploit-evals) — introduces SCONE-bench (open-sourced) and shows "Mythos Preview" chaining exploit primitives into full end-to-end attacks on widely-used software.
- [Measuring LLMs' impact on N-day exploits (Anthropic FRT)](https://www.anthropic.com/research/n-days) — frontier models turning public PoCs into working N-day exploits (21 Windows kernel LPE bugs, mechanically graded) — weaponizing already-disclosed CVEs at machine speed.
- [The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs](https://arxiv.org/abs/2606.22686) — argues refusal is a manipulable linear feature, not a deep semantic decision: the mechanistic basis behind refusal-direction / steering-vector jailbreaks.
- [AutoJack (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/) — canonical confused-deputy chain: a single attacker web page drives a browsing agent across the localhost boundary into AutoGen Studio's MCP control plane and gets host RCE.

## Community pulse

_Unverified intake — sentiment only, never evidence; links to threads, no individuals named._
- Quiet pass: HN front page was product-led (Apple pricing, an Obsidian/Notion clone); the only offensive-adjacent item was a low-rank "[2k people tried to hack my AI assistant](https://hn.algolia.com/?query=tried%20to%20hack%20my%20AI%20assistant)" write-up — no earthquake.
- Still-open intake from the week: [Anthropic↔Alibaba model-extraction](https://hn.algolia.com/?query=Anthropic%20Alibaba%20extracted%20Claude) claim, prompt injection as ["role confusion"](https://hn.algolia.com/?query=prompt%20injection%20role%20confusion), and a jqwik dependency reportedly injecting destructive instructions into AI coding agents — all held in the [observation_queue](TRENDS.md#observation_queue).

## Output map

- Source of truth: [`TRENDS.md`](TRENDS.md) — trends, [watchlist (22)](TRENDS.md#observation_queue), `strategy_notes`, `study_shelf`.
- Sources registry: [`SOURCES.md`](SOURCES.md) — the lists the radar sweeps.
- Reports: [`reports/`](reports/) — newest: [2026-06-26](reports/2026-06-26.md). Weekly: none yet.
- Coverage & self-eval logs: [`logs/`](logs/).
- Scope, rules and the autonomy contract: [`AGENTS.md`](AGENTS.md).
