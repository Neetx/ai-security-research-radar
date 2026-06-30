# AI Radar

![trends](https://img.shields.io/badge/trends-4-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-2-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-24-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--06--30-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-06-29):**
- 🔓 **Agent frameworks fail-open on tool arguments**: [Capability Gates Are Not Authorization](https://arxiv.org/abs/2606.28679) audits LangChain/LangGraph, LlamaIndex and the Stripe Agent Toolkit — all gate tool exposure but none re-authorizes each call against its concrete arguments before execution; added to [`agentic-attack-surface-001`](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain). A same-week cluster on agent-runtime authorization (MCP-invariants, formal protocol analysis, [sensory-vector PI on ROS 2 robots](https://arxiv.org/abs/2606.28649)) sits in the queue.
- 🎚️ **Quantization-conditioned LLM backdoors**: two independent defenses ([QuantGuard](https://arxiv.org/abs/2606.29239), [FlipGuard](https://arxiv.org/abs/2606.28962)) confirm QCB as a live threat — malicious behavior dormant in full precision, activating only after quantized deployment, bypassing pre-deployment audits; a new LLM-specific sub-theme of [`adversarial-trigger-backdoor-004`](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types).
- 📚 **Study shelf**: [Capability Gates Are Not Authorization](https://arxiv.org/abs/2606.28679) — why "the agent has the tool" ≠ "may use it on these arguments," with a deployable fail-closed PDP/PEP (ScopeGate).
- 📡 **Source coverage**: huntr.com access verified (hacktivity HTTP 200, Tavily-extract; no RSS); NVIDIA cybersec feed degraded again. Queue 21→24 (+8 lines / 9 papers, −5 stale burndown).

---

## Trends

🌱 1 · 📈 1 · 🚀 2 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-06-27](https://arxiv.org/abs/2606.28679) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-06-25](https://arxiv.org/abs/2606.26933) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-06-25](https://arxiv.org/abs/2606.27091) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🌱 seed | [2026-06-25](https://arxiv.org/abs/2606.27511) |

---

## Worth studying

- [Capability Gates Are Not Authorization (2606.28679)](https://arxiv.org/abs/2606.28679) — LangChain/LangGraph, LlamaIndex and the Stripe Agent Toolkit all gate tool exposure but none re-authorizes each model-emitted call against its concrete arguments; ships ScopeGate (fail-closed PDP/PEP: scope → auth → money ceiling → idempotency → default-deny). The practical reference + fix for per-call agent-tool authorization.
- [On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models](https://arxiv.org/abs/2606.27567) — proves perfect prompt-injection prevention is mathematically impossible in shared-embedding architectures (provenance-recovery impossibility + control-path exposure + finite-coverage invariance gap) — the theoretical why behind "every PI defense gets broken."
- [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents](https://arxiv.org/abs/2606.26479) — organizes the 2024–2026 out-of-band agent defenses (CaMeL, FIDES, Progent, RTBAS, FORGE) as Biba integrity / reference-monitor instances and stress-tests them with adaptive attacks — the reference map for "enforce security outside the model."
- [SoK: AI Secure Code Generation](https://arxiv.org/abs/2606.25195) — three-level framework mapping where prompting / fine-tuning / RL / agentic methods help secure-code generation and why substantial failures persist — the map for the "(in)security of AI-written code" problem.
- [The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs](https://arxiv.org/abs/2606.22686) — refusal is a manipulable linear feature, not a deep semantic decision: the mechanistic basis behind refusal-direction / steering-vector jailbreaks.
- [AutoJack (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/) — canonical confused-deputy chain: one attacker web page drives a browsing agent across the localhost boundary into AutoGen Studio's MCP control plane and gets host RCE.
- [Measuring LLMs' impact on N-day exploits (Anthropic FRT)](https://www.anthropic.com/research/n-days) — frontier models turning public PoCs into working N-day exploits for 21 Windows kernel LPE bugs — weaponizing already-disclosed CVEs at machine speed.
- [Mapping AI-enabled cyber threats: the LLM ATT&CK Navigator (Anthropic FRT)](https://www.anthropic.com/research/attack-navigator) — 832 real actors mapped to MITRE ATT&CK: 69% on T1587 Develop-Capabilities — in-the-wild ground truth for the AI-for-offense axis.

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- Quiet scan (2026-06-30) — no new community earthquake; HN front page was model-release news (Ornith self-improving agentic-coding models, LongCat-2.0), nothing offensive-AI.
- US government reportedly restricting Mythos and GPT-5.6 Sol on offensive-capability grounds (~1315 HN pts, 2026-06-26); [queued unverified](TRENDS.md#observation_queue).
- Anthropic Mythos reportedly found vulnerabilities in classified US systems during red-team testing (~850 HN pts, AP News 2026-06-26); [queued unverified](TRENDS.md#observation_queue).

---

[TRENDS.md](TRENDS.md) · [watchlist (24)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-06-30](reports/2026-06-30.md) · [weekly: 2026-W26](reports/weekly/2026-W26.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
