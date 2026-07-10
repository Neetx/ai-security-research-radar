# AI Radar

![trends](https://img.shields.io/badge/trends-6-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-3-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-25-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--07--10-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-07-10):**
- 🧠 **A graph-level causal account of jailbreaks lands on trend 005**: [+1 evidence](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) — [Mechanistic Interpretability of LLM Jailbreaks via Internal Attribution Graphs](https://arxiv.org/abs/2607.07903) aligns paired internal **computation graphs** for clean vs. attacked prompts, showing attacks **suppress safety components, spawn attack-specific features, and reroute computation paths** (validated by causal interventions). A **7th independent group**, generalizing the linear refusal/harmfulness-direction account to circuits.
- 🛡️ **The agent runtime keeps sprouting defenses**: two fresh agent-prompt-injection guards — [Prismata](https://arxiv.org/abs/2607.08147) (contextual-least-privilege confinement of cross-site PI in web agents) and [TokenWall](https://arxiv.org/abs/2607.08395) (a semantic runtime firewall over an agent's token flows, ASR→12.5%) — [folded into trend 001's](TRENDS.md#observation_queue) growing authorization/execution-integrity defense cluster.
- 🔧 **New capability & attack signals queued**: [REFORGE](https://arxiv.org/abs/2607.07738) builds an honest substrate for measuring LLM **reverse-engineering** capability (binary function naming); [CodeTracer](https://arxiv.org/abs/2607.08011) does forensic attribution of **backdoored code completions**; and adversarial examples transfer onto [LLM-based network-IDS classifiers](https://arxiv.org/abs/2607.07739) — all [queued](TRENDS.md#observation_queue).
- 📡 **Watchlist held 25** (+4 REFORGE / CodeTracer / LLM-NIDS-evasion / in-the-wild-T2I-unsafe-gen, −4 stale burndown); +4 AI-agent/MCP CVEs folded into 001's tally; capture-leak sweep clean (96 ids / 0 leaks); **no stage moves**.

---

## Trends

🌱 1 · 📈 2 · 🚀 3 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-07](https://arxiv.org/abs/2607.05744) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-07-07](https://blog.zksecurity.xyz/posts/circl-bugs/) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-08](https://arxiv.org/abs/2607.07903) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-07-06](https://arxiv.org/abs/2607.06596) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 📈 emerging | [2026-07-05](https://arxiv.org/abs/2607.04146) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 🌱 seed | [2026-07-01](https://arxiv.org/abs/2607.01313) |

---

## Worth studying

- [ScopeJudge: Cost-Aware Pre-Execution Gating for Offensive Security Agents](https://arxiv.org/abs/2607.07774) — as LLM agents take on offensive-security work, one out-of-scope tool call can breach an engagement boundary, and the in/out-of-scope line is declared in the user's *request*, not any fixed policy. Releases a benchmark of 4,897 pentester-labeled tool calls (7.7% violations, expert F1=0.78) and shows a static policy is request-blind (recall collapses to ~0). The released dataset for real-time scope oversight of autonomous offensive-security agents (cf. trend 002 / HexStrike-AI below).
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

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- HN/Reddit quiet this pass — no offensive-AI research earthquake; the day's top threads were the [GPT-5.6 launch](https://openai.com/index/gpt-5-6/) (product) and non-AI security items ([Cloudflare's "build your own vulnerability harness"](https://blog.cloudflare.com/build-your-own-vulnerability-harness/) fuzzing tutorial, an [npm supply-chain scanner](https://github.com/lateos-ai/npm-scan)).
- The hallucination-squatting nucleus (still 2 groups) is exactly the kind of AI-for-offense supply-chain vector worth watching on the social lane — attackers exploit *predictable* LLM hallucinations of package/repo/skill/domain names; [queued](TRENDS.md#observation_queue) pending a 3rd independent group.
- Earlier HN surfaced ["Meta's Un-Stable Signature"](https://hackerfactor.com/blog/index.php?/archives/1098-Metas-Un-Stable-Signature.html) — a claim that Meta's *Stable Signature* AI-image watermark is removable/forgeable; [queued unverified](TRENDS.md#observation_queue) as an off-axis AI-content-provenance-attack signal, watch for a 2nd group.
- Anthropic's Alibaba distillation accusation (a private letter to US Senators, public via press ~06-24) is well-corroborated across outlets but still has no direct Anthropic/Alibaba primary — [queued unverified](TRENDS.md#observation_queue).

---

[TRENDS.md](TRENDS.md) · [watchlist (25)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-07-10](reports/2026-07-10.md) · [weekly: 2026-W27](reports/weekly/2026-W27.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
