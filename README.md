# AI Security Radar

Autonomous radar tracking the **offensive AI-security frontier** — tools, releases and
research — on two coupled fronts: **AI for offense** (LLM red-teaming, autonomous
pentest/exploitation, AI-driven vulnerability discovery) and **offense against AI**
(jailbreaking, prompt injection, steering vectors, model extraction, agent/MCP attacks).
Primary-source trend ledger + study shelf, refreshed by a daily scan and a weekly
recalibration.

> This page is fully derived from [`TRENDS.md`](TRENDS.md) — regenerated each run, never
> hand-edited. Source of truth is the ledger.

![trends](https://img.shields.io/badge/trends-3-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-2-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-19-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--06--25-2f9e44?style=flat-square)

**Since last scan (2026-06-25):**
- [Agent / MCP attack surface](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) **promoted emerging → 🚀 accelerating** (confidence → high): cadence held a 3rd day with the [ERC-8004 trustless-agent-economy](https://arxiv.org/abs/2606.26028) trust-infra attack surface plus 13 MCP-server CVEs in 10 days (Flowise Custom-MCP OS-command-injection, Jenkins MCP plugin, Apache Doris MCP SQLi…).
- [LLM vuln discovery & repair](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) **promoted emerging → 🚀 accelerating**: two frontier labs + ≥7 arXiv groups, now with [LLM web-pentest capability boundaries](https://arxiv.org/abs/2606.25332) and [RepBench](https://arxiv.org/abs/2606.25356) on program representations for LLM vuln reasoning.
- **New 🌱 seed:** [the AI-security tooling layer is itself unreliable/attackable](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) — [skill scanners don't work (Trail of Bits)](https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/), [prompt-injection detectors mis-calibrate under attack shift](https://arxiv.org/abs/2606.22659), and [jailbreak ASR judges are unreliable](https://arxiv.org/abs/2606.25487).
- **Watchlist 16 → 19** — added a federated-backdoor trigger-color study, RAG-poisoning detection (TRACE), an agent "Unfireable Safety Kernel", and an Anthropic↔Alibaba model-extraction intake → [observation_queue](TRENDS.md#observation_queue). **Worth studying +1**: [SoK on AI secure code generation](https://arxiv.org/abs/2606.25195).

## Trends

🌱 1 · 📈 0 · 🚀 2 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Agent / MCP attack surface](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-06-24](https://arxiv.org/abs/2606.26028) |
| [LLM vuln discovery & repair](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-06-24](https://arxiv.org/abs/2606.25332) |
| [AI-security tooling unreliable](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🌱 seed | [2026-06-24](https://arxiv.org/abs/2606.25487) |

## Worth studying

- [SoK: AI Secure Code Generation (Patir, Guo, Cai, Hu)](https://arxiv.org/abs/2606.25195) — systematizes what today's models and coding agents can/cannot do for secure code via a three-level framework (NL understanding → secure generation → agentic workflows), mapping where prompting/fine-tuning/RL/agentic methods help and why failures persist — the map for the "(in)security of AI-written code" problem.
- [Mapping AI-enabled cyber threats: the LLM ATT&CK Navigator (Anthropic FRT)](https://www.anthropic.com/research/attack-navigator) — 832 real threat actors observed misusing models, mapped to MITRE ATT&CK: 69% used T1587 (Develop Capabilities), 560 on malware development — in-the-wild ground truth for the "AI for offense" axis.
- [Measuring LLMs' ability to develop exploits (Anthropic FRT)](https://www.anthropic.com/research/exploit-evals) — introduces SCONE-bench (open-sourced) and shows "Mythos Preview" chaining exploit primitives into full end-to-end attacks on widely-used software.
- [Measuring LLMs' impact on N-day exploits (Anthropic FRT)](https://www.anthropic.com/research/n-days) — frontier models turning public PoCs into working N-day exploits (21 Windows kernel LPE bugs, mechanically graded) — weaponizing already-disclosed CVEs at machine speed.
- [The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs](https://arxiv.org/abs/2606.22686) — argues refusal is a manipulable linear feature, not a deep semantic decision: the mechanistic basis behind refusal-direction / steering-vector jailbreaks.
- [AutoJack (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/) — canonical confused-deputy chain: a single attacker web page drives a browsing agent across the localhost boundary into AutoGen Studio's MCP control plane and gets host RCE.

## Community pulse

_Unverified intake — sentiment only, never evidence; links to threads, no individuals named._
- Top offensive-adjacent HN item this pass: [Anthropic says Alibaba illicitly extracted Claude model capabilities](https://hn.algolia.com/?query=Anthropic%20Alibaba%20extracted%20Claude) (247 pts) — a model-extraction/distillation signal, held [unverified in the queue](TRENDS.md#observation_queue) pending a primary statement.
- Still-open intake from the week: prompt injection as ["role confusion"](https://hn.algolia.com/?query=prompt%20injection%20role%20confusion), a [Show-HN pen-test model](https://hn.algolia.com/?query=pen%20tests%20instead%20of%20refusing) (checked — commercial product page, not a research artifact), and a jqwik dependency reportedly injecting destructive instructions into AI coding agents — all held in the [observation_queue](TRENDS.md#observation_queue).

## Output map

- Source of truth: [`TRENDS.md`](TRENDS.md) — trends, [watchlist (19)](TRENDS.md#observation_queue), `strategy_notes`, `study_shelf`.
- Sources registry: [`SOURCES.md`](SOURCES.md) — the lists the radar sweeps.
- Reports: [`reports/`](reports/) — newest: [2026-06-25](reports/2026-06-25.md). Weekly: none yet.
- Coverage & self-eval logs: [`logs/`](logs/).
- Scope, rules and the autonomy contract: [`AGENTS.md`](AGENTS.md).
</content>
</invoke>
