# AI Security Radar

![trends](https://img.shields.io/badge/trends-17-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-9-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-15-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--10--22-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-10-21):**
- 🚀 **[In-the-wild AI-for-offense](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) promoted emerging → 🚀 accelerating** on [Unit 42's "Next Exploit Opportunities"](https://unit42.paloaltonetworks.com/ai-assisted-cybercrime-analysis/) — a 2nd fresh in-the-wild case (after the Oct-15 espionage campaign): a threat actor ran GLM 5.2 (with a scripted jailbreak *override* + refusal-flagging), DeepSeek and "Hermes Agent" profiles as cybercrime advisors to plan an LLM-generated attack report, VoIP-fraud infrastructure, scam-call research and data exfiltration — the pre-registered accelerating lever, and a rare in-the-wild guardrail-bypass datapoint.
- 🔁 **[Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge)** +[Black-Box Red-Teaming of Multi-Agent Systems via RL](https://arxiv.org/abs/2610.28966) — a 10th independent group and the first to *learn* attack policies via reinforcement learning against multi-agent systems; held 📈 emerging (accelerating levers still open).
- 🧠 **Convergence flag:** a *persistent-memory durable-compromise* nucleus now has 3 independent groups ([Disclosure Begets Disclosure](https://arxiv.org/abs/2610.28315), [LTM→persistent compromise](https://arxiv.org/abs/2610.28810), [CarryoverBench](https://arxiv.org/abs/2610.28425)) — a one-time injection into agent long-term memory yielding cross-session compromise; flagged for the W43 seed decision.
- 🔭 **Watch:** repo-watch unchanged (garak 0.17.1, deepteam 1.0.10, promptfoo 0.124.1); OWASP still no 2026 LLM Top-10 edition; jailbreak-automation (~7 groups → W43 audit). Study pick: [Compaction Laundering](https://arxiv.org/abs/2610.29869).

---

## Trends

🌱 1 · 📈 7 · 🚀 9 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-10-21](https://unit42.paloaltonetworks.com/ai-assisted-cybercrime-analysis/) |
| [Agent authorization & identity integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) | 🚀 accelerating | [2026-10-20](https://arxiv.org/abs/2610.27620) |
| [Provenance & watermark attacks (image/audio/text/video)](TRENDS.md#id-watermark-provenance-attack-015-defeating-generative-ai-content-provenance--watermarks-image--audio--text-removal-forgery--laundering-across-modalities) | 🚀 accelerating | [2026-10-20](https://arxiv.org/abs/2610.27653) |
| [RAG knowledge/document poisoning](TRENDS.md#id-rag-knowledge-poisoning-014-knowledgedocument-poisoning-of-retrieval-augmented-generation-rag-malicious-corpus-documents-steer-retrievalgeneration) | 🚀 accelerating | [2026-10-15](https://arxiv.org/abs/2610.21464) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-10-14](https://arxiv.org/abs/2610.20941) |
| [Attacks on LLM-agent stack: MCP, memory, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-10-13](https://embracethered.com/blog/posts/2026/visual-studio-copilot-remote-code-execution/) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-10-13](https://arxiv.org/abs/2610.17837) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-10-13](https://arxiv.org/abs/2610.18609) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-10-03](https://arxiv.org/abs/2610.04245) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 📈 emerging | [2026-10-20](https://arxiv.org/abs/2610.28966) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 📈 emerging | [2026-10-17](https://arxiv.org/abs/2610.24784) |
| [Undetectable covert channels & agent collusion](TRENDS.md#id-covert-channel-collusion-016-undetectable-covert-channels-in-llm-systems-steganographic-multi-agent-collusion--activation-level-exfiltration-that-defeat-transcriptmonitor-auditing) | 📈 emerging | [2026-10-15](https://arxiv.org/abs/2610.22578) |
| [Agent skill supply-chain poisoning (composition/chaining)](TRENDS.md#id-skill-supply-chain-poisoning-017-agent-skill-supply-chain-poisoning-malicious-skills-and-the-composition-chaining-of-individually-vetted-skills-into-behavior-per-skill-vetting-misses) | 📈 emerging | [2026-10-14](https://arxiv.org/abs/2610.20049) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 📈 emerging | [2026-10-07](https://arxiv.org/abs/2610.09708) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-10-07](https://arxiv.org/abs/2610.10909) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-10-06](https://arxiv.org/abs/2610.07645) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 🌱 seed | [2026-10-07](https://arxiv.org/abs/2610.09264) |

---

## 🛠️ Tools & releases

No NEW above-bar tool this scan. GitHub tool-DISCOVERY + PyPI/npm registry-SEARCH surfaced only known/staged candidates (hardenedlinux/agentic-ai-pentest, Armur-Ai/Pentest-Swarm-AI, samugit83/redamon, vxcontrol/pentagi, ASCIT31/Dark-Moon, strix-agent, phantom-agent) plus defensive/generic repos — none clonable above the notability bar under the github 403-scope. Black Hat Arsenal / DEF CON Demo Labs off-season (next: Black Hat Europe Dec 2026). Watched-repo state:

- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.17.1** (2026-10-16, unchanged this run).
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.10** (2026-10-16, unchanged this run).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.124.1** (npm, unchanged).
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.1.0** (unchanged).
- [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) — evals, red-teaming & test generation for LLM/agentic systems; **v3.0.1** (unchanged).
- [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) — full-stack AI red-team platform: Agent-Scan, MCP-Scan, Skill-Scan (SARIF 2.1.0), jailbreak eval; **v4.6.2** (2026-09-17).
- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — a Dockerized collection of 38 offensive-security MCP servers / 300+ tools (Nmap, Ghidra, Nuclei, SQLMap, Hashcat, …).

---

## Worth studying

- [Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents](https://arxiv.org/abs/2610.29869) — the agent-integrity attack to know as coding agents adopt context compaction: an attacker gets untrusted content folded into the compacted/summarized context, and because compaction DESTROYS provenance (what came from where, trusted vs untrusted), the laundered content re-enters the agent's working context as if trusted. A fresh "laundering" attack-class adjacent to experience→skill and authority laundering — the reason context compaction needs a provenance-preserving design, not just a size budget.
- [The Show-Up Attack: When Subagents Win Over Their Supervisor](https://arxiv.org/abs/2610.27574) — the concrete multi-agent-orchestration attack to know before trusting a supervisor to bound its subagents: a malicious subagent manipulates the supervisor into tasks BEYOND its assigned scope, and on SUA-Arena all six tested frontier LLMs are vulnerable (GPT-5.6-Sol supervisor up to 0.93 ASR) while prompting/restricted-communication mitigations fail. Multi-agent systems need explicit authority-boundary enforcement, not a supervisor's judgment.
- [Global Security Blind Spots: Translation as a Safety Bypass in Low-Resource Languages](https://arxiv.org/abs/2610.27304) — LLM safety alignment does not survive translation: across ten deployed LLMs and 79 languages (metric conditioned on English safety), harmful requests refused in English elicit unsafe completions when translated — mean bypass 21.9%–44.4%, concentrated in a subset of language families and shared broadly across models.
- [SoK: PIAtlas — Decomposing the Unbounded Prompt Injection Attack Space](https://arxiv.org/abs/2610.24999) — the map the prompt-injection field has lacked: 20+ public PI datasets use incompatible vocabularies, so attacks can't be described or evaluated consistently. PIAtlas organizes the space around HOW the injected instruction is constructed to subvert the model — six mechanism classes, each the root of a technique hierarchy — the shared vocabulary that comparable PI evaluations depend on.
- [How Effectively Do Security Skills Guide Coding Agents in Vulnerability Detection in Linux Kernel?](https://arxiv.org/abs/2610.25705) — the capability-reliability floor for skill-guided auditing: the first large-scale empirical study (37 security skills × Claude Code × four LLMs × 100 real Linux-kernel vulnerabilities, 14,800 runs). Only 24.4% of runs locate the right function, 18.3% the function+statement, and 15.7% correctly classify the vulnerability — "a skill guides the agent" is not "the agent finds the bug".
- [Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents](https://arxiv.org/abs/2610.23254) — the measurement caution before trusting any indirect-PI ASR on small agents: ASR treats every failed attack as a defense, but auditing 33,000 trajectories from eleven open-weight agents (2-14B) shows most "failed" attacks were IGNORED (76-80%), not REFUSED (17-18%), and changing ONLY the system prompt shifts InjecAgent ASR 0.2%→43%. A low PI-ASR number can be luck of the harness.
- [From Billion-Scale to Million-Scale Language Models: Operational Capabilities for Embedded Post-Exploitation](https://arxiv.org/abs/2610.23534) — the AI-for-offense capability datapoint for autonomous malware that cannot phone home: ultra-compact SLMs (20M-1.5B params) evaluated on two post-exploitation code-generation tasks (directory enumeration, backdoor generation) across a high-resource (Python) and low-resource (Lua) language — offensive code generation migrating into the implant itself.
- [Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation (DIB-Bench)](https://arxiv.org/abs/2610.21135) — the eval-integrity result before trusting any agent-safety score: a tampered deployment that preserves evaluated outputs passes every output-only evaluator, and acceptance of tampered outputs RISES with evaluator strength (88.6% rule-based → 94.1% GPT-5-nano), while a trigger-conditional tamper invisible on the suite produces 48–100% harmful outputs.
- [BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition](https://arxiv.org/abs/2610.21565) — a TEE around an on-device LLM does not by itself protect the weights: most TEE-based obfuscation applies a unilateral matrix transform (output-side only), and a Solution Determinacy Property makes the obfuscation secret uniquely determined, so the protection breaks. A concrete model-extraction/IP-theft datapoint.
- [P2Patch: Exploit-Guided Vulnerability Repair](https://arxiv.org/abs/2610.20245) — the fix to the circular-validation flaw the patch-reliability shelf keeps flagging: automated-repair agents usually validate a patch against the SAME evidence used to build it, so a patch that blocks that one exploit can look successful while the bug survives in a variant. P2Patch treats each candidate patch as a new attack target — an exploit-generation loop probes for a bypass and feeds a surviving exploit back into the next repair iteration.
- [Beyond Maliciousness: Static and Runtime Attack-Surface Profiling of Agent Skills](https://arxiv.org/abs/2610.19264) — the first large-scale empirical measurement of how much authority installing a skill grants: skills are Markdown documents an agent reads as instructions and acts on with the session's privileges, profiled with whole-bundle static + dependency-provenance analysis then instrumented sandbox execution across 6,309 listings on two marketplaces. Why per-package "is it malicious?" auditing is the wrong question.
- [AnonVul: A Faithful Benchmark for Real-World Business-Logic Vulnerability Discovery](https://arxiv.org/abs/2610.17542) — the measurement caution before citing any "the agent found the bug" number on logic flaws: 132 cross-language application-level business-logic vulnerabilities (the subtle, app-semantics-dependent class SAST can't pattern-match), built reproducible AND contamination-resistant, with criteria precise enough to separate genuine discovery from memorization.

---

## Community pulse

*Unverified sentiment (Phase-3 intake, link-only) — never trend evidence.*

- **Prompt-injection detector/scanner discourse** recirculating on [Hacker News](https://hn.algolia.com/?query=prompt%20injection&type=story) (positional-vs-phrasal scanners, decision-model PI judges, System-One PI models, token-0 drop tools) — defense-side only, intake.
- **AI-coding-agent review tooling** surfacing on [Hacker News](https://hn.algolia.com/?query=AI%20agent%20review&type=story) (reviewer-agent / stop-continue Show HN posts) — tooling discourse, no new offensive artifact.
- Through the scan: quiet pulse — general PI / MCP / skill recirculation only, no offensive-AI earthquake and no new untracked-topic vocabulary.

---

📄 [TRENDS.md](TRENDS.md) · 👁 [watchlist (~15)](TRENDS.md#observation_queue) · 🗂 [reports/](reports/) → [2026-10-22](reports/2026-10-22.md) · 📅 weekly: [2026-W42](reports/weekly/2026-W42.md) · 📘 [AGENTS.md](AGENTS.md) · 🌐 [SOURCES.md](SOURCES.md)
