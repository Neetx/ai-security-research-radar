# AI Radar

![trends](https://img.shields.io/badge/trends-6-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-4-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-25-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--07--13-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-07-13):**
- 🎯 **Cross-vendor coding-agent PI disclosure** surfaced via tldrsec #336: ["Comment and Control"](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot) — a single GitHub PR title / issue comment hijacks **Claude Code, Gemini CLI and Copilot** agents into leaking the repo's Actions secrets (coordinated Anthropic/Google/GitHub disclosure) → [queued](TRENDS.md#observation_queue) on [trend 001](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) as a strong rotate-candidate + study pick.
- 🧬 **3-group backdoor convergence** (Mon-07-13 cs.CR batch): +1 evidence on [trend 004](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) ([physical fault-injection feature-map backdoor](https://arxiv.org/abs/2607.09473), new embedded/hardware domain — 9th attack group), with an [availability-DoS SNN backdoor](https://arxiv.org/abs/2607.09115) queued and a [statistically-undetectable-backdoor theory result](https://arxiv.org/abs/2607.09532) shelved. Held accelerating/medium (no stage move).
- 🔎 **Two AI-for-offense vuln items** queued on [trend 002](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code): [VEXAIoT](https://arxiv.org/abs/2607.09653) (autonomous IoT exploitation agents) and [SeedSmith](https://arxiv.org/abs/2607.08949) (LLM seed-synthesis for directed fuzzing).
- 📡 **Watchlist 24→25** (−5 burndown of stale singletons); **OpenAI RSS healed** (tvly-extract), **huntr degraded** (page "sunsetting"); capture-leak sweep clean (95 ids / 0 leaks).

---

## Trends

🌱 1 · 📈 1 · 🚀 4 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-07-10](https://arxiv.org/abs/2607.09473) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-07-08](https://arxiv.org/abs/2607.07903) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-07-07](https://arxiv.org/abs/2607.05744) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-07-07](https://blog.zksecurity.xyz/posts/circl-bugs/) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-07-06](https://arxiv.org/abs/2607.06596) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 🌱 seed | [2026-07-05](https://arxiv.org/abs/2607.04339) |

---

## Worth studying

- [Statistically Undetectable Backdoors in Deep Neural Networks](https://arxiv.org/abs/2607.09532) — an adversarial trainer can plant backdoors in a broad class of feedforward NNs that are **statistically undetectable even white-box** (backdoored ≈ honest in total-variation given all weights), while the secret grants invariance-based adversarial examples for *every* input — provably impossible to generate without it under standard crypto assumptions. The theoretical ceiling on backdoor detection; context for the whole trend-004 cluster.
- [Comment and Control: PI to Credential Theft in Claude Code, Gemini CLI, and GitHub Copilot](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot) — first cross-vendor demo that GitHub-comment prompt injection (PR title, issue body/comment) hijacks three production GitHub-Actions coding agents into exfiltrating the repo's own Actions secrets, with GitHub as the C2 channel; coordinated Anthropic/Google/GitHub disclosure (Anthropic CVSS 9.3→9.4, then reclassified None). The real-world reference for coding-agent-PI-to-credential-theft (cf. trend 001).
- [ScopeJudge: Cost-Aware Pre-Execution Gating for Offensive Security Agents](https://arxiv.org/abs/2607.07774) — as LLM agents take on offensive-security work, a single out-of-scope tool call can breach an engagement or void a bounty, and the in/out-of-scope line is declared in the user's *request*, not any fixed policy. Releases a benchmark of 4,897 pentester-labeled tool calls and shows a static policy is request-blind (recall ~0). The dataset for real-time scope oversight of autonomous offensive-security agents (cf. trend 002).
- [Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents](https://arxiv.org/abs/2607.07474) — agentic red-team benchmarks report compromise as a single bit, discarding *how harmful* the action was. A reusable seven-level (L0–L6) severity rubric (deterministic oracle + 3-judge panel, α=0.91) applied to AgentDojo logs exposes cases binary ASR hides — e.g. a defense reporting **0% ASR while still leaking cross-scope** (cf. trend 003).
- [The Balkanization of Execution-Security Research for AI Coding Agents](https://arxiv.org/abs/2607.05743) — systematizes 39 scattered papers (2023–2026) on the execution layer around AI coding agents into 17 source-verified categories + 4 confirmed CVEs, surfacing 5 cross-cutting gaps. The reference map tying trends 001 and 002.
- [Beyond Refusal: Aligned vs Abliterated LLMs for Vulnerability Analysis](https://arxiv.org/abs/2607.05842) — isolates the effect of *safety state* (refusal intact vs. refusal-ablated) on defensive-security utility using same-lineage Gemma/Qwen pairs. The clean read on whether abliteration actually buys defensive vuln-analysis capability (cf. trend 005).
- [When Claws Remember but Do Not Tell (WhisperBench)](https://arxiv.org/abs/2607.05189) — full-cycle benchmark (108 cases) for *stealth memory injection* against persistent personal agents: a remote black-box adversary's single email must write poisoned long-term memory, stay hidden in the reply, and alter future behavior. Built on a real IMAP/SMTP email-agent skill.
- [Prompt Injection as Role Confusion](https://arxiv.org/abs/2603.12277) — Ye, Cui & Hadfield-Menell (MIT) trace prompt injection to ROLE CONFUSION: an LLM infers who is speaking from how text *sounds*, not its labeled role, so untrusted text in an authoritative voice reads as a trusted instruction; ships internal "role probes" (code released). The conceptual "theory of prompt injection" — also cited as evidence on trend 001.
- [Determinants and Limits of LLM Security-Tool Orchestration (HexStrike-AI)](https://arxiv.org/abs/2607.02873) — across 774 trials it disentangles how much of an offensive agent's capability comes from the model vs. the driving client, and where failure is reasoning-bound vs. missing-tool-bound. The reference for how far open-source autonomous offensive-security orchestration gets today.
- [Fast Multi-dimensional Refusal Subspaces via RFM-AGOP](https://arxiv.org/abs/2607.02396) — refutes the "refusal is one linear direction" assumption (it lives in a multi-dimensional subspace) and recovers that subspace in *seconds*, even on long-reasoning-trace models (Qwen 3). The reusable technique for refusal steering/monitoring — the same subspace drives both attack and defense.
- [More details on Fable 5's cyber safeguards and our jailbreak framework (Anthropic)](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework) — a four-category dual-use taxonomy for cybersecurity safety classifiers plus an early-draft cross-industry jailbreak-severity framework (with Amazon/Microsoft/Google) and a live HackerOne cyber-jailbreak bounty — the standards/taxonomy artifact this radar's scope has been missing.
- [Has This Checkpoint Been Abliterated? A Two-Signal Audit](https://arxiv.org/abs/2607.01854) — deployable pre-deployment check for whether an open-weight checkpoint has had its refusal mechanism stripped (abliteration): fuses an activation refusal-gap with a base→candidate weight-recovery energy, separating 57 abliterations from 37 benign fine-tunes across 273 checkpoints at AUROC 0.95.

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- A GitHub-Actions coding-agent PI surface is drawing independent researchers: alongside the (verified, opened) ["Comment and Control"](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot) disclosure, a 2nd researcher's "Trusting Claude With a Knife" (PI→RCE in Claude Code Action) is [queued unverified](TRENDS.md#observation_queue) pending an open.
- [Jailbreaker](TRENDS.md#observation_queue) — an open-source repeatable LLM-jailbreak-testing platform (PAIR/TAP/Crescendo/AutoDAN/GPTFuzz) surfaced via tldrsec #336 — [queued unverified](TRENDS.md#observation_queue) as offensive jailbreak tooling pending a look at the primary repo.
- The hallucination-squatting nucleus (still 2 groups) — attackers exploiting *predictable* LLM hallucinations of package/repo/skill/domain names — stays [queued](TRENDS.md#observation_queue) pending a 3rd independent group.
- Anthropic's Alibaba-distillation accusation (a private letter to US Senators, public via press ~06-24) is well-corroborated across outlets but still has no direct Anthropic/Alibaba primary — [queued unverified](TRENDS.md#observation_queue). No new HN/Reddit earthquake this pass.

---

[TRENDS.md](TRENDS.md) · [watchlist (25)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-07-13](reports/2026-07-13.md) · [weekly: 2026-W28](reports/weekly/2026-W28.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
