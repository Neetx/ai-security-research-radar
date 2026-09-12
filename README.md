# AI Radar

![trends](https://img.shields.io/badge/trends-14-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-12-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--09--12-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-09-12) — weekly W37 recalibration:** one new seed, one convergence decided against on an author-independence check, a queue burndown, and one applied amendment. No promotions among existing trends.
- 🌱 **New seed — RAG knowledge/document poisoning:** three independent attack groups on distinct retrieval surfaces — [CamoDocs](https://arxiv.org/abs/2608.28389) (QA-RAG document camouflage), [CodePoisonRAG](https://arxiv.org/abs/2609.02774) (code-RAG poisoning), [ToxicRAG](https://arxiv.org/abs/2609.11082) (single-doc narrative knowledge-update) — clear the bar for a new [RAG-poisoning](TRENDS.md#id-rag-knowledge-poisoning-014-knowledgedocument-poisoning-of-retrieval-augmented-generation-rag-malicious-corpus-documents-steer-retrievalgeneration) axis, distinct from agent-stack indirect PI and in-model backdoors.
- 🔭 **Agentic-commerce — flagged as "3 groups", decided NOT to seed:** the author check collapses it to two — Yedidel Louck first-authored BOTH [Protocol-Level Attacks](https://arxiv.org/abs/2607.21824) and [Whisper/AP2](https://arxiv.org/abs/2609.11757) — so the only independent commerce group is the [AP2 security analysis](https://arxiv.org/abs/2608.23858) team; that analysis is absorbed into [agent authorization & identity integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) (which now spans 7 independent groups) rather than splitting a redundant trend.
- 🧹 **Ledger hygiene:** [hallucination-squatting](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) held dormant (targeted axis check found no fresh primary; archive-watch ~10-08); the [watchlist](TRENDS.md#observation_queue) burned down 10 husks older than 14 days (28→12) and the study shelf shed nine picks older than 30 days.
- 🛠️ **No new watched-tool releases** since the 09-10 daily (garak 0.17.0 / promptfoo 0.123.0 / PyRIT 1.1.0 / deepteam 1.0.9 / giskard 3.0.0 all unchanged).

---

## Trends

🌱 1 · 📈 6 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 1

| trend | stage | latest signal |
|---|---|---|
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-09-09](https://arxiv.org/abs/2609.09793) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-09-09](https://arxiv.org/abs/2609.10537) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-09-03](https://arxiv.org/abs/2609.04522) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-09-02](https://unit42.paloaltonetworks.com/ai-assisted-cyber-attack-inside-a-unit-42-investigation/) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-08-27](https://arxiv.org/abs/2608.27512) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-08-27](https://arxiv.org/abs/2608.27092) |
| [Agent authorization & identity integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) | 📈 emerging | [2026-09-10](https://arxiv.org/abs/2609.11757) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 📈 emerging | [2026-09-08](https://arxiv.org/abs/2609.08280) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-09-07](https://arxiv.org/abs/2609.07131) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 📈 emerging | [2026-09-05](https://arxiv.org/abs/2609.05889) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 📈 emerging | [2026-08-31](https://arxiv.org/abs/2608.30207) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-08-26](https://arxiv.org/abs/2608.25776) |
| [RAG knowledge/document poisoning](TRENDS.md#id-rag-knowledge-poisoning-014-knowledgedocument-poisoning-of-retrieval-augmented-generation-rag-malicious-corpus-documents-steer-retrievalgeneration) | 🌱 seed | [2026-09-10](https://arxiv.org/abs/2609.11082) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 💤 dormant | [2026-07-14](https://arxiv.org/abs/2607.12340) |

---

## 🛠️ Tools & releases

No new watched-tool releases this cycle (garak 0.17.0, promptfoo 0.123.0, PyRIT 1.1.0, deepteam 1.0.9, giskard 3.0.0 all unchanged since 09-10). Tool-discovery staged [msaleme/red-team-blue-team-agent-fabric](https://github.com/msaleme/red-team-blue-team-agent-fabric) (an agent adversarial-test harness spanning MCP / A2A / skill-supply-chain, mapped to OWASP-Agentic v1.1) — on-axis, stars/adoption unconfirmed, pending verification. Other staged candidates: [gangj277/hack-your-agent](https://github.com/gangj277/hack-your-agent), [cyproxio/mcp-for-security](https://github.com/cyproxio/mcp-for-security), [snyk/agent-scan](https://github.com/snyk/agent-scan), [simon-p-j-r/LLM4Pentest](https://github.com/simon-p-j-r/LLM4Pentest). The current on-axis tool set:

- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.17.0** (2026-09-09).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.123.0** (2026-09-10).
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.1.0** (2026-09-04).
- [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) — full-stack AI red-team platform: Agent-Scan, MCP-Scan, Skill-Scan (SARIF 2.1.0), jailbreak eval (26+ methods); **v4.6.0** (2026-08-26).
- [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) — evals, red-teaming & test generation for LLM/agentic systems; **v3.0.0** (2026-08-26).
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.9** (latest on PyPI).
- [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) — autonomous-pentest harness (13+ agents, 176 MCP tools, Ed25519-signed skills, OWASP/MITRE/CIS-aligned); 1.9k★, npm `@cyberstrike-io/cyberstrike`.
- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — a Dockerized collection of 38 offensive-security MCP servers / 300+ tools (Nmap, Ghidra, Nuclei, SQLMap, Hashcat, …).

---

## Worth studying

- [Big Enough to Break Out: Tracking the Rising Capability of LLM Penetration-Testing Agents](https://arxiv.org/abs/2609.10780) — the datapoint to watch the autonomous-pentest capability curve with: a PentestGPT on Claude Opus 4.8 solves all three public targets (incl. two a legacy human-in-the-loop system never finishes), adding a coverage-memory layer helps neither, and in stalled runs the limiter looked like planning/commitment, not lost long-horizon memory — so capability may advance with planning. The same subtask scoring is available to defenders to measure the rise as it happens.
- [How Fragile Is Safety Alignment at Frontier Scale? A Single-Direction Attack on a 320B MoE](https://arxiv.org/abs/2609.09793) — training-free single-"refusal-direction" abliteration, previously shown only on dense ≤70B models, survives to a frontier 320B mixture-of-experts model (GLM-5.3-Flash; 288 routed experts, block-FP8 quantized) — but the refusal direction becomes *distributed* across a four-wide hyper-connected residual, so editing attention/dense/expert writers removes almost nothing until you ablate across all of them. Open-weight MoE scale + quantization does not, by itself, buy alignment robustness against the canonical white-box removal primitive.
- [PrivEscalate: LLM-Automated Linux Privilege Escalation](https://arxiv.org/abs/2609.09087) — the benchmark to measure autonomous post-exploitation with: 531 Dockerized privesc scenarios (14 sub-categories) + 329 parameterized distractor variants, the first at a scale that supports executable-verified model comparison. Capability is heterogeneous by vulnerability class and successes are fragile to environmental perturbation — so configuration rotation is a practical disruption lever.
- [Repeat-After-Me: Black-Box Adaptive Visual Prompt Injection](https://arxiv.org/abs/2609.04522) — the reference that the IMAGE channel is now a viable prompt-injection vector against frontier VLMs where textual PI defenses do not reach: a black-box adaptive attack that emits exact, parseable native tool calls from an injected image (>80% open-weight / 47% commercial ASR, cross-model transfer) and, in a live OpenClaw Discord agent, overwrites `TOOLS.md` from one untrusted image → future RCE + secret exfiltration.
- [When LLM Decompilers Recompile More and Preserve Less](https://arxiv.org/abs/2609.05370) — the caution before trusting an LLM decompiler for security work (vuln detection / malware analysis): recompilability and re-executability metrics can reward the wrong path — a function may pass every shipped test yet diverge on other inputs, and a disclosed vulnerability can vanish from the recompiled code with no visible trace, neither failure caught by existing suites.
- [A Blind Trust, the Bloody Thrust — HookPry: attacker-controlled hook updates steer AI agent harnesses](https://arxiv.org/abs/2609.03884) — the reference that a harness's lifecycle-hook **update path** is a first-class supply-chain attack surface: hooks bind shell commands to runtime events that run with host privileges and can fire when the LLM never observes them, so an attacker who controls only plugin metadata + hook config trojanizes a benign versioned plugin → host-side privilege escalation. HookPry (open-source) compromises **all 7 harnesses** across 1,000 runs (up to 92.5%) while Defender catches 0%.
- [PatchBench: Evaluating AI Agents for Vulnerability Patching](https://arxiv.org/abs/2609.04075) — why "the agent fixed the CVE" is often an illusion: validating a patch only by re-running the crash PoC inflates the measured solve rate **1.83×** on average, because ~25% of agent patches memorize the historical developer fix and agents patch the crash stack-trace to suppress the symptom rather than fix the root cause.
- [PrimSynth: Agentic Discovery/Validation/Synthesis of Linux-Kernel Exploit Primitives](https://arxiv.org/abs/2609.02647) — the reference on closing the "abstract strategy → concrete operation" gap in autonomous **kernel** exploitation: it formalizes six classes of exploit primitives and a primitive-path code-synthesis representation, then wires them into a multi-agent framework — AI-for-offense at the exploitation layer, not just discovery.
- [Agent Memory Is a Surface for Endogenous Authorization Laundering](https://arxiv.org/abs/2609.01836) — a long-running agent can grant itself authority nobody gave it, with **no external attacker**: when persistent memory misrepresents an evolving authorization state, the agent's own records "launder" spurious permissions. EAL-Bench measures the propagation to unauthorized actions — the founding artifact of the [agent-authorization-integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) axis.
- [What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness](https://arxiv.org/abs/2609.01222) — why the HARNESS (not the model) is where instruction-privilege breaks: the first systematic analysis of how vendor-proprietary AI-agent harnesses *assemble* context, naming **M-CPE** and **Cross-Scope CPE**.
- [AKRASIA: Stealthy Backdoor Attack on Reasoning-based Code LLMs](https://arxiv.org/abs/2609.01023) — why a reasoning trace is not evidence of trustworthiness: an inference-time in-context backdoor for reasoning Code LLMs that exploits model UNFAITHFULNESS to hide the trigger — up to **99.34%** ASR, retaining up to 98.82% in 14/18 defense settings.
- [Beyond the Payload / CIPR — how user invocation shapes coding-agent vulnerability to repository poisoning](https://arxiv.org/abs/2608.30686) — why coding-agent repo-poisoning risk is not the attacker's payload alone: CIPR (1,920 instances / 20 real poisoned repos) shows the developer's own prompt-level configurations measurably raise or lower whether a poisoned repo compromises the agent.

---

## Community pulse

*Unverified sentiment (Phase-3 intake, link-only) — never trend evidence.*

- Practitioner attention on **prompt-injection against production coding agents/IDEs** stays high — recirculating "Google: attackers are using prompt injection against coding agents" framing plus general jailbreak how-tos on r/ClaudeAIJailbreak.
- **Embodied / physical prompt injection** keeps its community name — "kinetic prompt injection" (robot-dogs / sleeper-agent framing) is still circulating; captured as an alias on the [embodied-physical-injection](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) trend (which took a fresh robot attack this week).
- HN/Reddit through the week: general PI/jailbreak recirculation only (ASCII-smuggling→phishing crossover, a jailbreak-impossibility pdf, sandbox Show-HNs) — no offensive-AI earthquake, no new vocabulary.

---

📄 [TRENDS.md](TRENDS.md) · 👁 [watchlist (~12)](TRENDS.md#observation_queue) · 🗂 [reports/](reports/) → [2026-09-11](reports/2026-09-11.md) · 📅 weekly: [2026-W37](reports/weekly/2026-W37.md) · 📘 [AGENTS.md](AGENTS.md) · 🌐 [SOURCES.md](SOURCES.md)
