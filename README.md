# AI Radar

![trends](https://img.shields.io/badge/trends-6-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-3-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-25-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--07--09-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-07-09):**
- 🧠 **A named agent-memory-poisoning attack lands on trend 001**: [+1 evidence](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) — [GhostWriter](https://arxiv.org/abs/2607.06595) poisons a personal tool-using agent's long-term memory store via a hidden payload (~98% injection / ~60% activation), giving the trend's most-active sub-cluster a pure evidence representative; rotated out the oldest facet (Meta AI Agent ATO).
- 🔍 **The AI-security *measurement* layer keeps failing — now for AI-control monitors**: [+1 evidence on trend 003](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) — [Calibration-Family Overfit](https://arxiv.org/abs/2607.06596) (6th group) shows trusted sabotage monitors overfit to model *lineage*: an off-lineage monitor catches **19%** of attacks vs **41%** in-lineage at the same 1% audit budget, so single-pairing accuracy overstates safety.
- 🎣 **Hallucination-squatting is now a 2-group nucleus** (off the current axes): [Agentic Botnets / adversarial HalluSquatting](https://arxiv.org/abs/2607.07433) pre-registers LLM-hallucinated repo/skill names (up to 85–100% hit, transferable across models) to serve adversarial prompts → RCE + botnet, joining Unit 42's in-the-wild [Phantom Squatting](https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/) ([queued](TRENDS.md#observation_queue), seed on a 3rd group).
- 📡 **Watchlist held 25** (+3 HalluSquatting / multi-agent-reframing / biased-judge, −3 stale/non-independent burndown); +2 AI-agent/MCP CVEs folded into 001's tally; capture-leak sweep clean (89 ids / 0 leaks); **no stage moves**.

---

## Trends

🌱 1 · 📈 2 · 🚀 3 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-07](https://arxiv.org/abs/2607.05744) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-07-07](https://blog.zksecurity.xyz/posts/circl-bugs/) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-02](https://arxiv.org/abs/2607.01854) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-07-06](https://arxiv.org/abs/2607.06596) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 📈 emerging | [2026-07-05](https://arxiv.org/abs/2607.04146) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 🌱 seed | [2026-07-01](https://arxiv.org/abs/2607.01313) |

---

## Worth studying

- [Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents](https://arxiv.org/abs/2607.07474) — agentic red-team benchmarks report compromise as a single bit, discarding *how harmful* the action was. A reusable, trace-grounded seven-level (L0–L6) severity rubric (deterministic oracle + 3-judge panel, α=0.91) applied to AgentDojo logs exposes cases binary ASR hides — e.g. a defense reporting **0% ASR while still leaking cross-scope**. The instrument for measuring agent-attack harm beyond ASR (cf. trend 003).
- [The Balkanization of Execution-Security Research for AI Coding Agents](https://arxiv.org/abs/2607.05743) — systematizes 39 scattered papers (2023–2026) on the execution layer around AI coding agents (sandbox isolation, access control, TOCTOU races, MCP threats, identity delegation, egress control, static analysis) into 17 source-verified categories + 4 confirmed CVEs, and surfaces 5 cross-cutting gaps. The reference map tying trends 001 and 002.
- [Beyond Refusal: Aligned vs Abliterated LLMs for Vulnerability Analysis](https://arxiv.org/abs/2607.05842) — isolates the effect of *safety state* (refusal intact vs. refusal-ablated) on defensive-security utility using same-lineage Gemma/Qwen pairs, instead of cross-family comparisons that conflate safety with architecture/scale. The clean read on whether abliteration actually buys defensive vuln-analysis capability (cf. trend 005).
- [When Claws Remember but Do Not Tell (WhisperBench)](https://arxiv.org/abs/2607.05189) — full-cycle benchmark (108 cases) for *stealth memory injection* against persistent personal agents: a remote black-box adversary's single email must write poisoned long-term memory, stay hidden in the reply, and alter future behavior. Built on a real IMAP/SMTP email-agent skill — the reusable eval behind this batch's agent-memory-poisoning wave.
- [Determinants and Limits of LLM Security-Tool Orchestration (HexStrike-AI)](https://arxiv.org/abs/2607.02873) — across 774 trials (86 picoCTF challenges × tool-access regimes × model/client configs) it disentangles how much of an offensive agent's capability comes from the model vs. the driving client, and where failure is reasoning-bound vs. missing-tool-bound. The reference for how far open-source autonomous offensive-security orchestration actually gets today.
- [Fast Multi-dimensional Refusal Subspaces via RFM-AGOP](https://arxiv.org/abs/2607.02396) — refutes the "refusal is one linear direction" assumption (it lives in a multi-dimensional subspace) and makes finding that subspace cheap: an RFM adaptation with a probe-informed init recovers it in *seconds*, even on long-reasoning-trace models (Qwen 3). The reusable technique for refusal steering/monitoring — the same subspace drives both a steering attack and a monitoring defense.
- [More details on Fable 5's cyber safeguards and our jailbreak framework (Anthropic)](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework) — a four-category dual-use taxonomy for cybersecurity safety classifiers plus an early-draft cross-industry jailbreak-severity framework (with Amazon/Microsoft/Google), and a live HackerOne bounty for cyber jailbreaks — the standards/taxonomy artifact this radar's scope has been missing a concrete instance of.
- [Has This Checkpoint Been Abliterated? A Two-Signal Audit](https://arxiv.org/abs/2607.01854) — deployable pre-deployment check for whether an open-weight checkpoint has had its refusal mechanism stripped (abliteration): fuses an activation refusal-gap with a base→candidate weight-recovery energy, separating 57 abliterations from 37 benign fine-tunes across 273 checkpoints at AUROC 0.95. Runtime output-guards can't catch it — they score generations, not the artifact.
- [SoK: Attack and Defense Landscape of Mobile On-device AI Systems](https://arxiv.org/abs/2607.00362) — first systematization of MoAI security (locally-deployed models fused with mobile software): pillars, attack landscape (incl. local-model-storage threats), defenses, open gaps. The reference map for on-device inference moving the model into an attacker-reachable environment.
- [A Lifecycle and Application-Stack Survey of LLM Vulnerabilities](https://arxiv.org/abs/2606.31639) — eight-stage systematization (data → pretraining → alignment → supply-chain → retrieval/memory → prompting → tool/agent execution → deployment) of where trust boundaries fail and how untrusted data becomes executable instruction; the reference map for "the risk is the app stack, not the weights."
- [AI-Infra-Guard](https://arxiv.org/abs/2606.31227) — open-source framework matching a detection paradigm to each agent layer (infra→protocol/tool→behavior→model): rules over 75+ components / 1,400+ vuln rules, agentic MCP-server + agent-skill auditing, and a jailbreak harness (26+ operators, 16 datasets).
- [Capability Gates Are Not Authorization (2606.28679)](https://arxiv.org/abs/2606.28679) — LangChain/LangGraph, LlamaIndex and the Stripe Agent Toolkit all gate tool exposure but none re-authorizes each model-emitted call against its concrete arguments; ships ScopeGate (fail-closed PDP/PEP: scope → auth → money ceiling → idempotency → default-deny). The practical reference + fix for per-call agent-tool authorization.

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- HN/Reddit quiet this pass — no offensive-AI research earthquake; the day's top threads were non-AI ([obfuscated bash on a Uniqlo t-shirt](https://hn.algolia.com/api/v1/search?tags=front_page), [OpenMandriva distribution-sabotage attempt](https://hn.algolia.com/api/v1/search?tags=front_page)) or model launches (Grok 4.5, TypeScript 7).
- The hallucination-squatting nucleus (now 2 groups) is exactly the kind of AI-for-offense supply-chain vector worth watching on the social lane — attackers exploit *predictable* LLM hallucinations of package/repo/skill/domain names; [queued](TRENDS.md#observation_queue) pending a 3rd independent group.
- Earlier HN surfaced ["Meta's Un-Stable Signature"](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html) — a claim that Meta's *Stable Signature* AI-image watermark is removable/forgeable; [queued unverified](TRENDS.md#observation_queue) as an off-axis AI-content-provenance-attack signal, watch for a 2nd group.
- Anthropic's Alibaba distillation accusation (a private letter to US Senators, public via press ~06-24) is well-corroborated across outlets but still has no direct Anthropic/Alibaba primary — [queued unverified](TRENDS.md#observation_queue).

---

[TRENDS.md](TRENDS.md) · [watchlist (25)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-07-09](reports/2026-07-09.md) · [weekly: 2026-W27](reports/weekly/2026-W27.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
