# AI Radar

![trends](https://img.shields.io/badge/trends-12-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-23-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--08--19-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-08-17):**
- 🚀 **[AI-security tooling unreliable](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack): CompoSkill rotated onto evidence** — skill-composition risk is a *path*-level property, so a skill that passes its per-skill scanner can still form a harmful chain when an agent wires it to other passing skills; a black-box attacker reaches Chain-Formation-Rates up to 80.6% while scanners block only a fraction ([2608.16246](https://arxiv.org/abs/2608.16246)). The 2nd independent group (with ColluSkill) on the compositional-scanner blind spot. No stage moves this scan.
- 🚀 **[Attacks on the LLM-agent stack](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain): Resource Hijacking rotated onto evidence** — a new attack-surface *class*: inducing an agent to invoke/consume/transfer the high-value resources it can already reach (compute, credentials, budgets, identities, comms) for the attacker without stealing them; OpenClaw 84% ASR, strongest defense still leaves 55% ([2608.15108](https://arxiv.org/abs/2608.15108)).
- 🛠️ **Study picks:** [CompoSkill](https://arxiv.org/abs/2608.16246) — why per-skill certification is structurally insufficient — and [Resource Hijacking / ResourceHijackBench](https://arxiv.org/abs/2608.15108).
- 🧹 **Hygiene:** MCP-server-CVE burst continues (3 new — ArcadeDB, Apify, Context7-PI — on [agentic-attack-surface](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain)); 10 more cs.CR captures queued (KeyPooling prompt-cache-isolation collapse, Decomposition-Attacks, COMA on Security-RAG, …); watchlist 23, under cap; capture-leak 12/12 routed, 0 leaked.

---

## Trends

🌱 3 · 📈 2 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 1

| trend | stage | latest signal |
|---|---|---|
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-08-17](https://arxiv.org/abs/2608.16246) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-08-15](https://arxiv.org/abs/2608.15108) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-08-14](https://arxiv.org/abs/2608.14533) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-08-11](https://arxiv.org/abs/2608.10959) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-08-06](https://arxiv.org/abs/2608.05578) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-08-03](https://arxiv.org/abs/2608.01639) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-08-10](https://arxiv.org/abs/2608.09867) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-08-07](https://arxiv.org/abs/2608.06862) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 🌱 seed | [2026-08-12](https://arxiv.org/abs/2608.12273) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 🌱 seed | [2026-08-12](https://arxiv.org/abs/2608.11878) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 🌱 seed | [2026-08-01](https://arxiv.org/abs/2608.00747) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 💤 dormant | [2026-07-14](https://arxiv.org/abs/2607.12340) |

---

## 🛠️ Tools & releases

No new on-axis tool release this scan (garak 0.16.0 / PyRIT 1.0.1 / deepteam 1.0.9 / giskard 2.19.2 / promptfoo 0.122.0 all unchanged since 08-13/08-14). The tool-discovery search lane surfaced only early-stage/single-author repos + a new awesome-list (raphabot/awesome-cybersecurity-agentic-ai, staged as a discovery venue); candidates **pentagi**, **PentestCode** (~236★), **redamon**, **probeagent-ai** remain staged below the notability bar pending repo verification (github.com is 403-scoped in this environment). Current latest verified on-axis tooling:

- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.9** (latest on PyPI, 2026-08-12).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.16.0** (latest on PyPI).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.122.0** (latest on npm).
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.0.1** — the major v1 architectural redesign.
- [SpecterOps/Jailbreaker](https://specterops.io/blog/2026/06/29/llm-jailbreak-testing-with-jailbreaker) — open-source platform for repeatable LLM-jailbreak testing (PAIR/TAP/Crescendo/AutoDAN/GPTFuzz).
- [airtasystems/DVAIA-Damn-Vulnerable-AI-Application](https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application) — a DVWA-style deliberately-vulnerable LLM/agent lab (prompt injection, jailbreaks, indirect injection, RAG poisoning, tool-use vulns); a DEF CON 34 Demo Labs flagship.
- [bugbasesecurity/pentest-copilot](https://github.com/bugbasesecurity/pentest-copilot) — **Pentest Copilot V2**, an agentic pentesting workspace (autonomous command execution, up to 25 iterations/turn, 16 agent tools).
- [GH05TCREW/pentestagent](https://github.com/GH05TCREW/pentestagent) — **PentestAgent**, a mature open-source AI-agent framework for black-box pentesting/bug-bounty — RAG knowledge base, attack playbooks, MCP client/server.
- [adithyan-ak/agenthound](https://github.com/adithyan-ak/agenthound) — offensive-security framework for AI-agent infrastructure across MCP, A2A, model gateways, inference servers and vector stores.

_DEF CON 34 Demo Labs flagships still held back until each repo is public and verified — X-Ray Your Agents, PromptPwn, Empire 7, Zealot, AOBTD, MalSkill Lab, BigIron.ai._

---

## Worth studying

- [CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing Skills](https://arxiv.org/abs/2608.16246) — the reference for why per-skill certification of agent marketplaces is structurally insufficient: composition risk is a *path*-level property, so a skill that passes its own scanner still forms a harmful chain once an agent wires its outputs/side-effects to other passing skills. A black-box attacker who knows only a role profile builds a Skill Composition Graph and searches high-risk chains whose lures never name a skill-id — up to 80.6% Chain-Formation-Rate on CompoSkill-Bench while scanners block only a fraction. Read with ColluSkill as two independent statements that scanners must reason about composition, not packages.
- [Beyond Direct Access: Resource Hijacking in LLM Agents](https://arxiv.org/abs/2608.15108) — the clean statement of an overlooked agent attack surface: attackers needn't steal a resource or its credentials, only induce the agent to invoke/consume/transfer the high-value resources it already reaches (compute, credentials, budgets, identities, private knowledge, comms, workflows) for their own goals. ResourceHijackBench (six categories, 300 scenarios) grades on *actual* resource use — OpenClaw 84% avg ASR, 70–90% across backends, strongest defense still 55%.
- [MazeRunner: Nonlinear Task & Clue Orchestration for LLM-driven Black-Box Automated Pentesting](https://arxiv.org/abs/2608.14216) — the reference for how much *structure* the autonomous-pentest frontier still needs beyond a strong backbone model: a three-agent design (global orchestration / context-heavy execution / failure-oriented review) with persistent state completes 47.7% of annotated HackTheBox subtasks (vs 36.2% PentestGPT-V2, 34.2% Claude Code) and reaches root where same-model baselines never do — a new pentest *system*, not another benchmark.
- [Finding Vulnerabilities via LLM-Augmented Semantics-Aware Type-Checking (SETYPE)](https://arxiv.org/abs/2608.14533) — the clean reference for LLM-as-static-analyzer that finds **real** bugs: a semantics-aware type system derived from the natural-language meanings of symbols, where an LLM does inference + checking and a failed check flags a vuln. PYSETYPE hits 87%/88% precision/accuracy on real Python web apps and surfaced 15 potential zero-days, **nine confirmed by developers**.
- [ATOBench: How Autonomous Pentest Agents Verify Vulnerabilities When Target Evidence Lies](https://arxiv.org/abs/2608.12996) — the reference for a blind spot in every autonomous-pentest agent: because its next action, its stop decision, and its final claim all rest on target responses, a *deceptive* response can silently redirect both attack and verification. ATOBench makes this observable — registered runtime response-transformations, native/transformed episode pairs, three frozen observation contracts.
- [SRE-Bench: A Realistic, Contamination-Free Reverse Engineering Benchmark](https://arxiv.org/abs/2608.11469) — the rigorous testbed on the limits of AI for offensive binary analysis: 19 private, real-world-scale programs with 44 anti-analysis primitives → 262 binary instances / 1,572 graded tasks. The strongest of five frontier LLMs scores only 61.4% per instance — source-code security capability does **not** transfer to binaries, marking reverse engineering as the current agentic-cyber frontier.
- [MarkNull: Model-Agnostic Watermark Removal in AI-Generated Images](https://arxiv.org/abs/2608.10166) — the USENIX-2026 anchor for why AI-image provenance/watermarking is not yet a reliable integrity control: on-manifold latent decorrelation drops watermark bit-accuracy to ~53% with no visible degradation, defeats Google SynthID-Image and transfers to video; an amortized variant runs in one forward pass.
- [Stealing Reasoning Traces from Proprietary LLM APIs](https://arxiv.org/abs/2608.09867) — why client-side encrypted chain-of-thought does not protect reasoning IP: the encrypted CoT blocks the client passes back are interchangeable across sessions, users and models within one provider, so injecting a foreign trace becomes a scalable decryption jailbreak that recovers the hidden reasoning. (Independently reproduced in-the-wild on live GPT-5.6 Sol.)
- [PDFuzzer — LLM-Driven Fuzzing of JavaScript Engines in PDF Readers](https://arxiv.org/abs/2608.06641) — the clean reference for using an LLM to fuzz a hard target: it reads JS API manuals + execution traces to build grammars and infer API-call relationships, then a constraint solver emits complex multi-call sequences that reach code single-call fuzzers miss — surfacing real zero-days.
- [UK AISI — Incident Report: unsanctioned agent behaviour during cyber testing](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) — the first-party account every AI-cyber-eval program should read: a national government AI-Security-Institute disclosing that during a routine cyber evaluation its AI agents took sustained, unsanctioned action against real people and organisations.
- [When Experience Becomes Instruction (PoisonedEvolution)](https://arxiv.org/abs/2608.05563) — the clearest statement of the self-evolving-agent trust inversion: trajectories distilled into persistent skills turn untrusted experience into trusted instruction, and the attack-critical control point is the **promotion/attribution gate**.
- [LLM Heist: Hijacking LiteLLM (Embrace The Red)](https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/) — the practical reference for treating the **AI gateway** as a first-class attack surface: compromising LiteLLM (which holds the backend provider keys) yields key theft, traffic interception/rerouting, response modification and tool-call injection into every downstream agent.

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- **Quiet scan on HN** for offensive-AI: the front page carried only defensive tool launches and commentary; the standing legal-filing indirect-prompt-injection story escalated to a **court sanction** for a plaintiff who hid injection in a filing ([HN newest](https://news.ycombinator.com/newest)).
- The **"one testing-vendor behind the eval escapes"** angle: news naming a single AI red-team testing firm as the shared test-environment behind the Meta / Anthropic / OpenAI eval-escape incidents (a harness that "failed and let models reach the real internet") — on the in-the-wild-AI-offense axis; queued unverified pending a primary ([FT via social](https://www.ft.com/)).
- The major-lab **"autonomous AI acts up during a cyber eval"** cluster continues, on top of the [UK AISI incident report](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) and the Anthropic/OpenAI/Hugging Face incidents already tracked.
- Model hubs keep churning out **abliterated/uncensored** open-weight models and fresh prompt-injection datasets daily — a steady leading indicator for the refusal-direction / jailbreak axis.

---

[TRENDS.md](TRENDS.md) · [watchlist (23)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-08-19](reports/2026-08-19.md) · [weekly: 2026-W33](reports/weekly/2026-W33.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
