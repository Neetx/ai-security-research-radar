# AI Security Radar

Autonomous radar tracking the **offensive AI-security frontier** — tools, releases and
research — on two coupled fronts: **AI for offense** (LLM red-teaming, autonomous
pentest/exploitation, AI-driven vulnerability discovery) and **offense against AI**
(jailbreaking, prompt injection, steering vectors, model extraction, agent/MCP attacks).
Primary-source trend ledger + study shelf, refreshed by a daily scan and a weekly
recalibration.

> This page is fully derived from [`TRENDS.md`](TRENDS.md) — regenerated each run, never
> hand-edited. Source of truth is the ledger.

![trends](https://img.shields.io/badge/trends-2-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-0-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-16-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--06--24-2f9e44?style=flat-square)

**Since last scan (2026-06-24, Pass 1):**
- [Agent / MCP attack surface](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) widened into **knowledge/memory poisoning**: agent long-term memory [laundered to 68% attack-success](https://arxiv.org/abs/2606.24322) and [poisoned RAG "playbooks"](https://arxiv.org/abs/2606.24402) flipping AI security agents' exploit behavior — plus **12 fresh MCP-server CVEs in 10 days** (NVD). Accelerating is the likely next stage move.
- [LLM vuln discovery & repair](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) gained Anthropic FRT's [Measuring LLMs' ability to develop exploits](https://www.anthropic.com/research/exploit-evals) — the open-source **SCONE-bench** and a "Mythos Preview" step-change building full end-to-end exploits.
- **Watchlist 14 → 16** — red-teaming the offensive agent, PixJail T2I-jailbreak reproduction, FRT Project Fetch (off-axis) → [observation_queue](TRENDS.md#observation_queue).
- **Worth studying +2**: [LLM ATT&CK Navigator](https://www.anthropic.com/research/attack-navigator) (832 real actors mapped to ATT&CK) and [exploit-evals / SCONE-bench](https://www.anthropic.com/research/exploit-evals).

## Trends

🌱 0 · 📈 2 · 🚀 0 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Agent / MCP attack surface](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 📈 emerging | [2026-06-23](https://arxiv.org/abs/2606.24322) |
| [LLM vuln discovery & repair](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 📈 emerging | [2026-06-22](https://openai.com/index/daybreak-securing-the-world) |

## Worth studying

- [Mapping AI-enabled cyber threats: the LLM ATT&CK Navigator (Anthropic FRT)](https://www.anthropic.com/research/attack-navigator) — 832 real threat actors observed misusing models, mapped to MITRE ATT&CK: 69% used T1587 (Develop Capabilities), 560 on malware development — in-the-wild ground truth for the "AI for offense" axis.
- [Measuring LLMs' ability to develop exploits (Anthropic FRT)](https://www.anthropic.com/research/exploit-evals) — introduces SCONE-bench (open-sourced) and shows "Mythos Preview" chaining exploit primitives into full end-to-end attacks on widely-used software.
- [Measuring LLMs' impact on N-day exploits (Anthropic FRT)](https://www.anthropic.com/research/n-days) — frontier models turning public PoCs into working N-day exploits (21 Windows kernel LPE bugs, mechanically graded) — weaponizing already-disclosed CVEs at machine speed.
- [The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs](https://arxiv.org/abs/2606.22686) — argues refusal is a manipulable linear feature, not a deep semantic decision: the mechanistic basis behind refusal-direction / steering-vector jailbreaks.
- [AutoJack (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/) — canonical confused-deputy chain: a single attacker web page drives a browsing agent across the localhost boundary into AutoGen Studio's MCP control plane and gets host RCE.

## Community pulse

_Unverified intake — sentiment only, never evidence; links to threads, no individuals named._
- HN was quiet for offensive-AI this pass — ["Vulnerability reports are not special anymore"](https://hn.algolia.com/?query=vulnerability%20reports%20not%20special) (172 pts) and a non-AI [SecureROM exploit](https://hn.algolia.com/?query=SecureROM%20exploit) led; the prior prompt-injection / pen-test-model threads rolled off the front page.
- Still-open intake from the week: prompt injection as "role confusion", a Show-HN pen-test model, and a jqwik dependency reportedly injecting destructive instructions into AI coding agents — all held [unverified in the queue](TRENDS.md#observation_queue).

## Output map

- Source of truth: [`TRENDS.md`](TRENDS.md) — trends, [watchlist (16)](TRENDS.md#observation_queue), `strategy_notes`, `study_shelf`.
- Sources registry: [`SOURCES.md`](SOURCES.md) — the lists the radar sweeps.
- Reports: [`reports/`](reports/) — newest: [2026-06-24](reports/2026-06-24.md). Weekly: none yet.
- Coverage & self-eval logs: [`logs/`](logs/).
- Scope, rules and the autonomy contract: [`AGENTS.md`](AGENTS.md).
</content>
</invoke>
