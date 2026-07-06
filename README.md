# AI Radar

![trends](https://img.shields.io/badge/trends-6-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-3-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-25-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--07--06-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-07-06):**
- 😴 **Quiet pass, no stage moves**: arXiv is paused over the US July-4 holiday weekend — no new announce batch (cs.CR still 2607.02451, cs.AI still 2607.02514) — and every vendor/lab feed (Trail of Bits, Microsoft, OpenAI, Unit 42, Anthropic, AI Village, Embrace The Red) + watched tool release is unchanged. All six trends held.
- 🧩 **One new MCP-server CVE**: [CVE-2026-14748](https://nvd.nist.gov/vuln/detail/CVE-2026-14748) — SSRF via the `url` arg in AIAnytime *Awesome-MCP-Server* (mcp-wiki), CVSS 6.3, public PoC (07-05) — folded into trend [001](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain)'s running MCP-CVE volume tally (below the per-item evidence bar).
- 📡 **Watchlist held at 25**: no signal cleared the bar or needed adding; capture-leak sweep clean (66 arXiv ids checked / 0 leaks).
- 🩹 **Project Zero degraded a 2nd pass**: feed + HTML index both return empty via curl *and* `tvly` — on heal-watch; its content is consistently off-axis (kernel/mobile), so citable risk is low.

---

## Trends

🌱 1 · 📈 2 · 🚀 3 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-02](https://arxiv.org/abs/2607.01854) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-01](https://arxiv.org/abs/2607.00422) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-07-01](https://arxiv.org/abs/2607.01138) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-07-02](https://arxiv.org/abs/2607.02357) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 📈 emerging | [2026-07-02](https://arxiv.org/abs/2607.01702) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 🌱 seed | [2026-07-01](https://arxiv.org/abs/2607.01313) |

---

## Worth studying

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
- [Prompt Injection as Role Confusion](https://arxiv.org/abs/2603.12277) — MIT: traces prompt injection to *role confusion* — an LLM infers who is speaking from how text *sounds*, not its labeled `<user>`/`<tool>` role, so untrusted text in an authoritative voice is read as a trusted instruction; builds internal "role probes" for who's speaking. The conceptual "theory of PI" complementing the instruction/data-inseparability impossibility result — a science-of-roles framing for why every content-based PI defense leaks.
- [The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs](https://arxiv.org/abs/2606.22686) — refusal is a manipulable linear feature, not a deep semantic decision: the mechanistic basis behind refusal-direction / steering-vector jailbreaks (anchors trend 005).

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- HN front page surfaced ["Meta's Un-Stable Signature"](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html) (~80 pts) — a forensics researcher's claim that Meta's *Stable Signature* AI-image watermark is removable/forgeable; [queued unverified](TRENDS.md#observation_queue) as an off-axis AI-content-provenance-attack signal, watch for a 2nd group before seeding.
- Anthropic's Alibaba distillation accusation (a private letter to US Senators, made public via press ~06-24) is well-corroborated across multiple outlets but still has no direct Anthropic/Alibaba primary naming Alibaba specifically — [queued unverified](TRENDS.md#observation_queue).
- Otherwise quiet on HN/Reddit — no offensive-AI research earthquake beyond what's already tracked above.

---

[TRENDS.md](TRENDS.md) · [watchlist (25)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-07-06](reports/2026-07-06.md) · [weekly: 2026-W27](reports/weekly/2026-W27.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
