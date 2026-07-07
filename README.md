# AI Radar

![trends](https://img.shields.io/badge/trends-6-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-3-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-26-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--07--07-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-07-07):**
- 🧠 **Agent-memory poisoning surged in the post-holiday arXiv backlog**: a same-batch convergence on trend [001](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) — [Agent Data Injection](https://arxiv.org/abs/2607.05120) (a **new IPI category**: malicious *data* disguised as trusted metadata/context, evading instruction-injection defenses) added as evidence, plus [FARMA](https://arxiv.org/abs/2607.05029) forged-*reasoning* memory poisoning, [WhisperBench](https://arxiv.org/abs/2607.05189) single-email stealth memory injection, and [KB-poisoning of policy-aware RAG](https://arxiv.org/abs/2607.04379) queued.
- 🔓 **Refusal-removal goes operational at scale**: [+1 evidence on trend 005](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) — ["Not All Refusals Are Equal"](https://arxiv.org/abs/2607.02714) demonstrates *domain-specific* abliteration across 24 open LLMs incl. a 1T-param MoE (Kimi K2), stripping refusal to unblock offensive-cyber tasks (held accelerating/medium — abliteration at new scale, not yet a novel steering-vector tool).
- 🤖 **Backdoors reach embodied robotics**: [+1 evidence on trend 004](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) — [!Imperio/smolVLA](https://arxiv.org/abs/2607.04146) shows 3 poisoned episodes in 320 embed a trigger-word backdoor that DoS-locks a real VLA robot (8th independent attack group, new domain).
- 📡 **Watchlist 25 → 26** (+3 captured, −2 stale press/community); capture-leak sweep clean (76 ids checked / 0 leaks). No new AI-MCP-server CVE; vendor blogs, tool releases and HN/Reddit pulse quiet.

---

## Trends

🌱 1 · 📈 2 · 🚀 3 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-06](https://arxiv.org/abs/2607.05120) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-02](https://arxiv.org/abs/2607.01854) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-07-01](https://arxiv.org/abs/2607.01138) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 📈 emerging | [2026-07-05](https://arxiv.org/abs/2607.04146) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-07-02](https://arxiv.org/abs/2607.02357) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 🌱 seed | [2026-07-01](https://arxiv.org/abs/2607.01313) |

---

## Worth studying

- [When Claws Remember but Do Not Tell (WhisperBench)](https://arxiv.org/abs/2607.05189) — full-cycle benchmark (108 cases) for *stealth memory injection* against persistent personal agents: a remote black-box adversary's single email must write poisoned long-term memory, stay hidden in the reply, and alter future behavior. Built on a real IMAP/SMTP email-agent skill — the reusable eval behind this batch's agent-memory-poisoning wave.
- [Determinants and Limits of LLM Security-Tool Orchestration (HexStrike-AI)](https://arxiv.org/abs/2607.02873) — across 774 trials (86 picoCTF challenges × tool-access regimes × model/client configs) it disentangles how much of an offensive agent's capability comes from the model vs. the driving client, and where failure is reasoning-bound vs. missing-tool-bound. The reference for how far open-source autonomous offensive-security orchestration actually gets today.
- [Fast Multi-dimensional Refusal Subspaces via RFM-AGOP](https://arxiv.org/abs/2607.02396) — refutes the "refusal is one linear direction" assumption (it lives in a multi-dimensional subspace) and makes finding that subspace cheap: an RFM adaptation with a probe-informed init recovers it in *seconds*, even on long-reasoning-trace models (Qwen 3). The reusable technique for refusal steering/monitoring — the same subspace drives both a steering attack and a monitoring defense.
- [More details on Fable 5's cyber safeguards and our jailbreak framework (Anthropic)](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework) — a four-category dual-use taxonomy for cybersecurity safety classifiers plus an early-draft cross-industry jailbreak-severity framework (with Amazon/Microsoft/Google), and a live HackerOne bounty for cyber jailbreaks — the standards/taxonomy artifact this radar's scope has been missing a concrete instance of.
- [Has This Checkpoint Been Abliterated? A Two-Signal Audit](https://arxiv.org/abs/2607.01854) — deployable pre-deployment check for whether an open-weight checkpoint has had its refusal mechanism stripped (abliteration): fuses an activation refusal-gap with a base→candidate weight-recovery energy, separating 57 abliterations from 37 benign fine-tunes across 273 checkpoints at AUROC 0.95. Runtime output-guards can't catch it — they score generations, not the artifact.
- [SoK: Attack and Defense Landscape of Mobile On-device AI Systems](https://arxiv.org/abs/2607.00362) — first systematization of MoAI security (locally-deployed models fused with mobile software): pillars, attack landscape (incl. local-model-storage threats), defenses, open gaps. The reference map for on-device inference moving the model into an attacker-reachable environment.
- [A Lifecycle and Application-Stack Survey of LLM Vulnerabilities](https://arxiv.org/abs/2606.31639) — eight-stage systematization (data → pretraining → alignment → supply-chain → retrieval/memory → prompting → tool/agent execution → deployment) of where trust boundaries fail and how untrusted data becomes executable instruction; the reference map for "the risk is the app stack, not the weights."
- [AI-Infra-Guard](https://arxiv.org/abs/2606.31227) — open-source framework matching a detection paradigm to each agent layer (infra→protocol/tool→behavior→model): rules over 75+ components / 1,400+ vuln rules, agentic MCP-server + agent-skill auditing, and a jailbreak harness (26+ operators, 16 datasets).
- [Capability Gates Are Not Authorization (2606.28679)](https://arxiv.org/abs/2606.28679) — LangChain/LangGraph, LlamaIndex and the Stripe Agent Toolkit all gate tool exposure but none re-authorizes each model-emitted call against its concrete arguments; ships ScopeGate (fail-closed PDP/PEP: scope → auth → money ceiling → idempotency → default-deny). The practical reference + fix for per-call agent-tool authorization.
- [On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models](https://arxiv.org/abs/2606.27567) — proves perfect prompt-injection prevention is mathematically impossible in shared-embedding architectures (provenance-recovery impossibility + control-path exposure + finite-coverage invariance gap) — the theoretical why behind "every PI defense gets broken."
- [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents](https://arxiv.org/abs/2606.26479) — organizes the 2024–2026 out-of-band agent defenses (CaMeL, FIDES, Progent, RTBAS, FORGE) as Biba integrity / reference-monitor instances and stress-tests them with adaptive attacks — the reference map for "enforce security outside the model."
- [SoK: AI Secure Code Generation](https://arxiv.org/abs/2606.25195) — three-level framework mapping where prompting / fine-tuning / RL / agentic methods help secure-code generation and why substantial failures persist — the map for the "(in)security of AI-written code" problem.

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- HN/Reddit quiet this pass — no offensive-AI research earthquake; the day's top AI thread (a "GLM 5.2 and the coming AI margin collapse" market piece) is off-axis.
- HN front page earlier surfaced ["Meta's Un-Stable Signature"](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html) (~80 pts) — a forensics researcher's claim that Meta's *Stable Signature* AI-image watermark is removable/forgeable; [queued unverified](TRENDS.md#observation_queue) as an off-axis AI-content-provenance-attack signal, watch for a 2nd group before seeding.
- Anthropic's Alibaba distillation accusation (a private letter to US Senators, made public via press ~06-24) is well-corroborated across multiple outlets but still has no direct Anthropic/Alibaba primary naming Alibaba specifically — [queued unverified](TRENDS.md#observation_queue).

---

[TRENDS.md](TRENDS.md) · [watchlist (26)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-07-07](reports/2026-07-07.md) · [weekly: 2026-W27](reports/weekly/2026-W27.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
