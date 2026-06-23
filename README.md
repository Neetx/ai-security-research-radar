# AI Security Radar

Autonomous radar tracking the **offensive AI-security frontier** — tools, releases and
research — on two coupled fronts: **AI for offense** (LLM red-teaming, autonomous
pentest/exploitation, AI-driven vulnerability discovery) and **offense against AI**
(jailbreaking, prompt injection, steering vectors, model extraction, agent/MCP attacks).
Primary-source trend ledger + study shelf, refreshed by a daily scan and a weekly
recalibration.

> This page is fully derived from [`TRENDS.md`](TRENDS.md) — regenerated each run, never
> hand-edited. Source of truth is the ledger.

![trends](https://img.shields.io/badge/trends-2-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-0-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-14-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--06--23-2f9e44?style=flat-square)

**Since last scan (2026-06-23, Pass 2):**
- [LLM vuln discovery & repair](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) raised to **high confidence** — a second frontier lab, Anthropic's Frontier Red Team, now quantifies offensive capability with [Measuring LLMs' impact on N-day exploits](https://www.anthropic.com/research/n-days) (working exploits for 21 Windows-kernel LPE bugs).
- [Agent / MCP attack surface](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) gained a concrete advisory artifact — [CVE-2026-46519](https://nvd.nist.gov/vuln/detail/CVE-2026-46519) (mcp-server-kubernetes, CVSS 8.8; broken tool-restriction controls), one of **27 MCP CVEs** in NVD this June.
- **Watchlist +6 → 14** — prompt-injection-detector evasion, white-box diffusion model inversion, world-model/VLA attacks, knowledge-editing erasure illusion, a 2nd poisoning/backdoor group → [observation_queue](TRENDS.md#observation_queue).
- **Worth studying +1**: [Measuring LLMs' impact on N-day exploits](https://www.anthropic.com/research/n-days).

## Trends

🌱 0 · 📈 2 · 🚀 0 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Agent / MCP attack surface](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 📈 emerging | [2026-06-22](https://arxiv.org/abs/2606.23416) |
| [LLM vuln discovery & repair](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 📈 emerging | [2026-06-22](https://openai.com/index/daybreak-securing-the-world) |

## Worth studying

- [Measuring LLMs' impact on N-day exploits (Anthropic FRT)](https://www.anthropic.com/research/n-days) — concrete methodology and results for frontier models turning public PoCs into working N-day exploits (21 Windows kernel LPE bugs, mechanically graded) — weaponizing already-disclosed CVEs at machine speed.
- [The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs](https://arxiv.org/abs/2606.22686) — argues refusal is a manipulable linear feature, not a deep semantic decision: the mechanistic basis behind refusal-direction / steering-vector jailbreaks.
- [AutoJack (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/) — canonical confused-deputy chain: a single attacker web page drives a browsing agent across the localhost boundary into AutoGen Studio's MCP control plane and gets host RCE.

## Community pulse

_Unverified intake — sentiment only, never evidence; links to threads, no individuals named._
- Prompt injection framed as "role confusion" drew heavy [HN discussion](https://hn.algolia.com/?query=prompt%20injection%20role%20confusion) (199 pts).
- A Show HN claimed a model post-trained to pen-test instead of refusing — [HN](https://hn.algolia.com/?query=post-trained%20model%20pen%20tests) (92 pts, offensive-model claim, unverified).
- A jqwik dependency reportedly shipped hidden instructions telling AI coding agents to delete data — [HN](https://hn.algolia.com/?query=jqwik%20AI%20coding%20agents) (agent supply-chain signal).

## Output map

- Source of truth: [`TRENDS.md`](TRENDS.md) — trends, [watchlist (14)](TRENDS.md#observation_queue), `strategy_notes`, `study_shelf`.
- Sources registry: [`SOURCES.md`](SOURCES.md) — the lists the radar sweeps.
- Reports: [`reports/`](reports/) — newest: [2026-06-23](reports/2026-06-23.md). Weekly: none yet.
- Coverage & self-eval logs: [`logs/`](logs/).
- Scope, rules and the autonomy contract: [`AGENTS.md`](AGENTS.md).
</content>
