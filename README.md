# AI Radar

![trends](https://img.shields.io/badge/trends-5-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-2-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-25-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--07--02-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-07-01):**
- 🧭 **New trend — the mechanics of jailbreaks**: seeded [`refusal-direction-mechanics-005`](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) from a 3-group convergence — [Geometry of Refusal](https://arxiv.org/abs/2606.22686), [Robust Harmful Features](https://arxiv.org/abs/2606.28153) and new [HARC](https://arxiv.org/abs/2607.00572): safety alignment lives on manipulable linear directions in the residual stream, and jailbreaks are direction *suppression*, not prompt trickery.
- 📈 **Backdoors promoted to emerging**: [`adversarial-trigger-backdoor-004`](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) hits its 6th independent attack group with [ReShift](https://arxiv.org/abs/2607.00361) — an aha-moment-driven *reasoning-level* backdoor that redirects a VLM's chain-of-thought while keeping surface coherence.
- 🕵️ **Agent-stack + vuln-discovery cadence holds**: [`001`](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) +[KidnapRAG](https://arxiv.org/abs/2607.00422) (first *black-box* poisoning of "robust" agentic RAG); [`002`](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) +[Antaeus](https://arxiv.org/abs/2607.01138) (repo-level *logic*-vulnerability discovery).
- 📚 **Study shelf** +1: [SoK: Mobile On-device AI Systems](https://arxiv.org/abs/2607.00362) — first systematization of MoAI attack/defense, pairing with fresh mobile-agent attack work as a forming nucleus.

---

## Trends

🌱 1 · 📈 2 · 🚀 2 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-01](https://arxiv.org/abs/2607.00422) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-07-01](https://arxiv.org/abs/2607.01138) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-06-25](https://arxiv.org/abs/2606.27091) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 📈 emerging | [2026-07-01](https://arxiv.org/abs/2607.00361) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🌱 seed | [2026-07-01](https://arxiv.org/abs/2607.00572) |

---

## Worth studying

- [SoK: Attack and Defense Landscape of Mobile On-device AI Systems](https://arxiv.org/abs/2607.00362) — first systematization of MoAI security (locally-deployed models fused with mobile software): pillars, attack landscape (incl. local-model-storage threats), defenses, open gaps. The reference map for on-device inference moving the model into an attacker-reachable environment.
- [A Lifecycle and Application-Stack Survey of LLM Vulnerabilities](https://arxiv.org/abs/2606.31639) — eight-stage systematization (data → pretraining → alignment → supply-chain → retrieval/memory → prompting → tool/agent execution → deployment) of where trust boundaries fail and how untrusted data becomes executable instruction; the reference map for "the risk is the app stack, not the weights."
- [AI-Infra-Guard](https://arxiv.org/abs/2606.31227) — open-source framework matching a detection paradigm to each agent layer (infra→protocol/tool→behavior→model): rules over 75+ components / 1,400+ vuln rules, agentic MCP-server + agent-skill auditing, and a jailbreak harness (26+ operators, 16 datasets).
- [Capability Gates Are Not Authorization (2606.28679)](https://arxiv.org/abs/2606.28679) — LangChain/LangGraph, LlamaIndex and the Stripe Agent Toolkit all gate tool exposure but none re-authorizes each model-emitted call against its concrete arguments; ships ScopeGate (fail-closed PDP/PEP: scope → auth → money ceiling → idempotency → default-deny). The practical reference + fix for per-call agent-tool authorization.
- [On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models](https://arxiv.org/abs/2606.27567) — proves perfect prompt-injection prevention is mathematically impossible in shared-embedding architectures (provenance-recovery impossibility + control-path exposure + finite-coverage invariance gap) — the theoretical why behind "every PI defense gets broken."
- [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents](https://arxiv.org/abs/2606.26479) — organizes the 2024–2026 out-of-band agent defenses (CaMeL, FIDES, Progent, RTBAS, FORGE) as Biba integrity / reference-monitor instances and stress-tests them with adaptive attacks — the reference map for "enforce security outside the model."
- [SoK: AI Secure Code Generation](https://arxiv.org/abs/2606.25195) — three-level framework mapping where prompting / fine-tuning / RL / agentic methods help secure-code generation and why substantial failures persist — the map for the "(in)security of AI-written code" problem.
- [The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs](https://arxiv.org/abs/2606.22686) — refusal is a manipulable linear feature, not a deep semantic decision: the mechanistic basis behind refusal-direction / steering-vector jailbreaks (now anchoring trend 005).
- [AutoJack (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/) — canonical confused-deputy chain: one attacker web page drives a browsing agent across the localhost boundary into AutoGen Studio's MCP control plane and gets host RCE.
- [Measuring LLMs' impact on N-day exploits (Anthropic FRT)](https://www.anthropic.com/research/n-days) — frontier models turning public PoCs into working N-day exploits for 21 Windows kernel LPE bugs — weaponizing already-disclosed CVEs at machine speed.
- [Mapping AI-enabled cyber threats: the LLM ATT&CK Navigator (Anthropic FRT)](https://www.anthropic.com/research/attack-navigator) — 832 real actors mapped to MITRE ATT&CK: 69% on T1587 Develop-Capabilities — in-the-wild ground truth for the AI-for-offense axis.

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- Quiet scan (2026-07-02) — no offensive-AI research earthquake on HN; top offensive-adjacent items were community tools/benchmarks (Senior-SWE-Bench, a prompt-injection-detector benchmark, "Prompt Injection as Role Confusion") — nothing new to queue.
- US Dept. of Commerce reportedly *lifted* export controls on Claude Fable 5 and Mythos (~487 HN pts, 2026-07-01) — the governance flip-side of the earlier restriction signal; no primary opened, [queued unverified](TRENDS.md#observation_queue).
- Anthropic Mythos reportedly found vulnerabilities in classified US systems during red-team testing (~850 HN pts, AP News 2026-06-26); [queued unverified](TRENDS.md#observation_queue).

---

[TRENDS.md](TRENDS.md) · [watchlist (25)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-07-02](reports/2026-07-02.md) · [weekly: 2026-W26](reports/weekly/2026-W26.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
