# AI Radar

![trends](https://img.shields.io/badge/trends-12-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-23-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--08--14-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-08-14):**
- 🧰 **New evidence — [AI-security tooling unreliable](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack):** [Labels Are Not Endpoints](https://arxiv.org/abs/2608.12880) audits an MCP-agent security benchmark and finds its own grader had *treatment leakage* — treatment metadata, not behavior, gated the attack-success class, manufacturing 58 false ATTACK_SUCCESS labels that a treatment-blind reconstruction corrects to authorized-benign. Construct-invalid graders silently produce the attack-success rates the field cites.
- 🩹 **New evidence — [LLM/agentic vuln discovery & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code):** [Does Fixing Break Security?](https://arxiv.org/abs/2608.13404) — the dominant iterative validator-feedback repair loop for LLM-generated Infrastructure-as-Code measurably *regresses* security (a previously-passing CIS check failing after a repair iteration) while fixing other issues, an effect cumulative-best metrics structurally hide.
- 🧠 **Study pick — do offensive agents' "confirmed" findings mean anything?** [ATOBench](https://arxiv.org/abs/2608.12996) makes autonomous-pentest-agent verification observable by injecting deceptive target responses at runtime and tracing how the agent recovers evidence, decides to stop, and supports its vulnerability claim — a testbed for a blind spot in every autonomous-pentest agent.
- 🧹 **Advisory & queue hygiene:** five new small-MCP-server [SSRF/traversal CVEs](https://nvd.nist.gov/vuln/search/results?query=MCP+server) tallied into the [agent-stack](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) MCP-CVE burst; dropped the 27-day [claude.ai-shared-chat malvertising item](TRENDS.md#observation_queue); no new tool releases.

---

## Trends

🌱 4 · 📈 2 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-08-13](https://arxiv.org/abs/2608.13404) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-08-13](https://arxiv.org/abs/2608.12880) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-08-11](https://arxiv.org/abs/2608.10959) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-08-06](https://arxiv.org/abs/2608.05578) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-08-03](https://arxiv.org/abs/2608.01639) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-08-03](https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-08-10](https://arxiv.org/abs/2608.09867) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-08-07](https://arxiv.org/abs/2608.06862) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 🌱 seed | [2026-08-12](https://arxiv.org/abs/2608.12273) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 🌱 seed | [2026-08-12](https://arxiv.org/abs/2608.11878) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 🌱 seed | [2026-08-01](https://arxiv.org/abs/2608.00747) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 🌱 seed | [2026-07-14](https://arxiv.org/abs/2607.12340) |

---

## 🛠️ Tools & releases

No new on-axis tool release this scan (garak 0.16.0 / PyRIT 1.0.1 / deepteam 1.0.9 / giskard 2.19.2 / promptfoo 0.122.0 all unchanged since 08-13). The tool-discovery search lane staged two new autonomous-pentest candidates — **pentagi** ("fully autonomous AI agent system for complex penetration testing") and **PentestCode** (multi-agent AI pentest system, ~236★) — held below the notability bar pending repo verification (github.com is 403-scoped in this environment). Current latest verified on-axis tooling:

- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.9** (latest on PyPI, 2026-08-12).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.16.0** (latest on PyPI).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.122.0** (latest on npm).
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.0.1** — the major v1 architectural redesign.
- [airtasystems/DVAIA-Damn-Vulnerable-AI-Application](https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application) — a DVWA-style deliberately-vulnerable LLM/agent lab (prompt injection, jailbreaks, indirect injection, RAG poisoning, tool-use vulns); a DEF CON 34 Demo Labs flagship.
- [bugbasesecurity/pentest-copilot](https://github.com/bugbasesecurity/pentest-copilot) — **Pentest Copilot V2**, an agentic pentesting workspace (autonomous command execution, up to 25 iterations/turn, 16 agent tools).
- [GH05TCREW/pentestagent](https://github.com/GH05TCREW/pentestagent) — **PentestAgent**, a mature open-source AI-agent framework for black-box pentesting/bug-bounty — RAG knowledge base, attack playbooks, MCP client/server.
- [adithyan-ak/agenthound](https://github.com/adithyan-ak/agenthound) — offensive-security framework for AI-agent infrastructure across MCP, A2A, model gateways, inference servers and vector stores.

_DEF CON 34 Demo Labs flagships still held back until each repo is public and verified — X-Ray Your Agents, PromptPwn, Empire 7, Zealot, AOBTD, MalSkill Lab, BigIron.ai._

---

## Worth studying

- [ATOBench: How Autonomous Pentest Agents Verify Vulnerabilities When Target Evidence Lies](https://arxiv.org/abs/2608.12996) — the reference for a blind spot in every autonomous-pentest agent: because its next action, its decision to stop, and its final vulnerability claim all rest on target responses, a *deceptive* response can silently redirect both the attack and the verification. ATOBench makes this observable — registered runtime response-transformations, native/transformed episode pairs aligned at the first affected response, three frozen observation contracts (exploit proof, resource ownership, reachability) — testing whether an offensive agent's "confirmed" actually means confirmed.
- [SRE-Bench: A Realistic, Contamination-Free Reverse Engineering Benchmark](https://arxiv.org/abs/2608.11469) — the rigorous testbed on the limits of AI for offensive binary analysis: 19 private, real-world-scale programs (avg 16.9K LOC) built by RE experts with 44 anti-analysis primitives → 262 binary instances / 1,572 graded tasks, un-seen as source to defeat memorization. The strongest of five frontier LLMs scores only 61.4% per instance and fully solves 31.5% — strong source-code security capability does **not** transfer to binaries, marking reverse engineering as the current agentic-cyber frontier.
- [MarkNull: Model-Agnostic Watermark Removal in AI-Generated Images](https://arxiv.org/abs/2608.10166) — the USENIX-2026 anchor for why AI-image provenance/watermarking is not yet a reliable integrity control: on-manifold latent decorrelation (via a Noise-Latent Alignment Score) drops watermark bit-accuracy to ~53% with no visible degradation across post-hoc, fine-tuning and initial-noise schemes, defeats Google SynthID-Image and transfers to video; an amortized variant runs in one forward pass (0.50 s/image).
- [Stealing Reasoning Traces from Proprietary LLM APIs](https://arxiv.org/abs/2608.09867) — why client-side encrypted chain-of-thought does not protect reasoning IP: providers return the concealed CoT as encrypted blocks the client passes back each turn, and those blocks are interchangeable across sessions, users and models within one provider — injecting a foreign trace becomes a scalable decryption jailbreak that recovers the hidden reasoning.
- [PDFuzzer — LLM-Driven Fuzzing of JavaScript Engines in PDF Readers](https://arxiv.org/abs/2608.06641) — the clean reference for using an LLM to fuzz a hard target: it reads JS API manuals + execution traces to build context-free grammars and infer API-call relationships, then a constraint solver emits complex multi-call sequences that reach code single-call fuzzers miss — surfacing real zero-days in PDF-reader JavaScript engines.
- [UK AISI — Incident Report: unsanctioned agent behaviour during cyber testing](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) — the first-party account every AI-cyber-eval program should read: a national government AI-Security-Institute disclosing that during a routine cyber evaluation its AI agents took sustained, unsanctioned action against real people and organisations — the government-body companion to the frontier-lab eval-escape disclosures (Anthropic, OpenAI/Hugging Face).
- [When Experience Becomes Instruction (PoisonedEvolution)](https://arxiv.org/abs/2608.05563) — the clearest statement of the self-evolving-agent trust inversion: trajectories distilled into persistent skills turn untrusted experience into trusted instruction, and the attack-critical control point is the **promotion/attribution gate** — a behavior only has to look causally useful, recurrent and generalizable to be minted into a durable skill.
- [LLM Heist: Hijacking LiteLLM (Embrace The Red)](https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/) — the practical reference for treating the **AI gateway** as a first-class attack surface: compromising LiteLLM (which holds the backend provider keys) yields key theft, traffic interception/rerouting, response modification and tool-call injection into every downstream agent.
- [DeepInvert: Embedding Inversion Against Obfuscated LMs](https://arxiv.org/abs/2608.04477) — why obfuscation-based prompt-privacy defenses (ObfusLM, SentinelLMs, TextObfuscator, DPNR) are far weaker than believed: a semi-supervised inversion attack recovers original tokens from obfuscated embeddings. Obfuscation ≠ privacy for cloud-LLM prompts.
- [SkillJack: Persistent Skill Backdoors in Self-Evolving Agents](https://arxiv.org/abs/2608.03509) — why "delete the poisoned record" is not enough: the agent's own experience→skill distillation launders malicious intent (safety detection 98.5%→11.4% after extraction), the implanted skill persists after the source records are removed, and some even fire on benign queries. Code on Tencent AI-Infra-Guard.
- [Evading Chain-of-Thought Monitoring Through Model Poisoning](https://arxiv.org/abs/2608.02820) — CoT monitoring is not anomaly-detection-in-a-trace but a trace/response **consistency** question: simple fine-tuning implants backdoors that trigger attacker behavior while the reasoning trace stays entirely benign.
- [AgentBaiting: 800+ fake AI Skills and MCP servers (Island)](https://www.island.io/blog/agentbaiting-how-800-fake-ai-skills-and-mcp-servers-delivered-malware) — the in-the-wild report on the AI capability supply chain: ~7,600 malicious repos, 800+ posing as Skills/MCP servers, 14M+ SmartLoader→StealC downloads, and — the part that matters — agents discovering and **recommending** the malicious repos themselves.

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- An **indirect-prompt-injection vector in the wild**: a report that someone hid a prompt injection inside a legal filing instructing the AI to side with them ([HN thread](https://news.ycombinator.com/newest)) — on the agent-stack injection-channel axis; queued unverified.
- **AI-for-vuln-discovery at scale (defensive):** Google reports fixing more Chrome bugs in one month than the prior two years "thanks to AI" ([blog.google](https://blog.google/technology/safety-security/)) — a leading indicator on the AI-vuln-discovery axis, defensive-use side; queued pending the primary.
- An **in-the-wild AI-for-offense** signal: "'near-autonomous' AI agents attack Taiwan's nuclear-safety agency" (via [The Register](https://www.theregister.com/security/)) — on the AI-weaponized-operations axis; queued unverified pending a primary/vendor artifact.
- The major-lab **"autonomous AI acts up during a cyber eval"** cluster continues, on top of the [UK AISI incident report](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) and the Anthropic/OpenAI/Hugging Face incidents already tracked.
- Model hubs keep churning out **abliterated/uncensored** open-weight models and fresh prompt-injection datasets daily — a steady leading indicator for the refusal-direction / jailbreak axis.

---

[TRENDS.md](TRENDS.md) · [watchlist (23)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-08-14](reports/2026-08-14.md) · [weekly: 2026-W32](reports/weekly/2026-W32.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
