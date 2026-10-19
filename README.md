# AI Radar

![trends](https://img.shields.io/badge/trends-17-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-7-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-12-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--10--19-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-10-17):**
- 🔄 **[Agent authorization & identity integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) refreshed** by [When Approval Becomes Execution](https://arxiv.org/abs/2610.23077) — a token-possession-as-authorization workflow attack (OpenClaw-competition traces + 23 reruns), a 10th independent group that moots the approaching dormancy line. No stage moves this run.
- 🕳️ **[Undetectable covert channels](TRENDS.md#id-covert-channel-collusion-016-undetectable-covert-channels-in-llm-systems-steganographic-multi-agent-collusion--activation-level-exfiltration-that-defeat-transcriptmonitor-auditing)** +[Model-as-a-Trojan](https://arxiv.org/abs/2610.22578): a covert DNS-exfil channel baked into an open-weight LLM's *weights*, firing from inside an egress-locked container — 7th distinct mechanism.
- 🎞️ **[Provenance & watermark attacks](TRENDS.md#id-watermark-provenance-attack-015-defeating-generative-ai-content-provenance--watermarks-image--audio--text-removal-forgery--laundering-across-modalities)** reach VIDEO: [PoseRegen](https://arxiv.org/abs/2610.22457) defeats eleven video watermarking schemes to ≈random bit accuracy while preserving motion.
- 🔭 **Watch:** the automated-jailbreak-optimization cluster grew to ~5 groups (RedDarwin/ECHO joining TRAP/ATTCK-R/JSB) but spans three mechanisms — flagged for a W43 coherence audit; repo-watch saw patch bumps (garak 0.17.1, deepteam 1.0.10).

---

## Trends

🌱 1 · 📈 8 · 🚀 7 · 🌊 0 · 🏔 0 · 📉 0 · 💤 1

| trend | stage | latest signal |
|---|---|---|
| [Agent authorization & identity integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) | 🚀 accelerating | [2026-10-16](https://arxiv.org/abs/2610.23077) |
| [RAG knowledge/document poisoning](TRENDS.md#id-rag-knowledge-poisoning-014-knowledgedocument-poisoning-of-retrieval-augmented-generation-rag-malicious-corpus-documents-steer-retrievalgeneration) | 🚀 accelerating | [2026-10-15](https://arxiv.org/abs/2610.21464) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-10-14](https://arxiv.org/abs/2610.20941) |
| [Attacks on LLM-agent stack: MCP, memory, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-10-13](https://embracethered.com/blog/posts/2026/visual-studio-copilot-remote-code-execution/) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-10-13](https://arxiv.org/abs/2610.17837) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-10-13](https://arxiv.org/abs/2610.18609) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-09-29](https://arxiv.org/abs/2609.37737) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 📈 emerging | [2026-10-15](https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/) |
| [Undetectable covert channels & agent collusion](TRENDS.md#id-covert-channel-collusion-016-undetectable-covert-channels-in-llm-systems-steganographic-multi-agent-collusion--activation-level-exfiltration-that-defeat-transcriptmonitor-auditing) | 📈 emerging | [2026-10-15](https://arxiv.org/abs/2610.22578) |
| [Provenance & watermark attacks (image/audio/text/video)](TRENDS.md#id-watermark-provenance-attack-015-defeating-generative-ai-content-provenance--watermarks-image--audio--text-removal-forgery--laundering-across-modalities) | 📈 emerging | [2026-10-15](https://arxiv.org/abs/2610.22457) |
| [Agent skill supply-chain poisoning (composition/chaining)](TRENDS.md#id-skill-supply-chain-poisoning-017-agent-skill-supply-chain-poisoning-malicious-skills-and-the-composition-chaining-of-individually-vetted-skills-into-behavior-per-skill-vetting-misses) | 📈 emerging | [2026-10-14](https://arxiv.org/abs/2610.20049) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 📈 emerging | [2026-10-07](https://arxiv.org/abs/2610.09708) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 📈 emerging | [2026-10-07](https://arxiv.org/abs/2610.10929) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-10-07](https://arxiv.org/abs/2610.10909) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-10-06](https://arxiv.org/abs/2610.07645) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 🌱 seed | [2026-10-07](https://arxiv.org/abs/2610.09264) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 💤 dormant | [2026-09-25](https://arxiv.org/abs/2609.31318) |

---

## 🛠️ Tools & releases

No NEW above-bar tool this scan. GitHub tool-DISCOVERY + PyPI/npm registry-SEARCH surfaced only known/staged candidates plus low-signal new single-author repos (JoasASantos/NeuroSploit, LuaN1aoAgent) — unverifiable notability under the github 403-scope, so they stay discovery candidates, not clonable listings; known/staged: LLM4Pentest, xalgorix, vxcontrol/pentagi, Armur-Ai/Pentest-Swarm-AI, strix-agent, ASCIT31/Dark-Moon (getagentseal/agentseal is a defensive scanner). Black Hat Arsenal / DEF CON Demo Labs off-season (next: Black Hat Europe Dec 2026). Watched-repo state:

- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.17.1** (2026-10-16, patch bump).
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.10** (patch bump).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.124.1** (npm, unchanged).
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.1.0** (unchanged).
- [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) — evals, red-teaming & test generation for LLM/agentic systems; **v3.0.1** (unchanged).
- [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) — full-stack AI red-team platform: Agent-Scan, MCP-Scan, Skill-Scan (SARIF 2.1.0), jailbreak eval; **v4.6.2** (2026-09-17).
- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — a Dockerized collection of 38 offensive-security MCP servers / 300+ tools (Nmap, Ghidra, Nuclei, SQLMap, Hashcat, …).

---

## Worth studying

- [Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents](https://arxiv.org/abs/2610.23254) — the measurement caution before trusting any indirect-PI ASR on small agents: ASR treats every failed attack as a defense, but auditing 33,000 trajectories from eleven open-weight agents (2-14B) shows most "failed" attacks were IGNORED (76-80%), not REFUSED (17-18%), and changing ONLY the system prompt shifts InjecAgent ASR 0.2%→43%. A low PI-ASR number can be luck of the harness.
- [From Billion-Scale to Million-Scale Language Models: Operational Capabilities for Embedded Post-Exploitation](https://arxiv.org/abs/2610.23534) — the AI-for-offense capability datapoint for autonomous malware that cannot phone home: ultra-compact SLMs (20M-1.5B params) evaluated on two post-exploitation code-generation tasks (directory enumeration, backdoor generation) across a high-resource (Python) and low-resource (Lua) language — offensive code generation migrating into the implant itself.
- [Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation (DIB-Bench)](https://arxiv.org/abs/2610.21135) — the eval-integrity result before trusting any agent-safety score: a tampered deployment that preserves evaluated outputs passes every output-only evaluator, and acceptance of tampered outputs RISES with evaluator strength (88.6% rule-based → 94.1% GPT-5-nano), while a trigger-conditional tamper invisible on the suite produces 48–100% harmful outputs.
- [BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition](https://arxiv.org/abs/2610.21565) — a TEE around an on-device LLM does not by itself protect the weights: most TEE-based obfuscation applies a unilateral matrix transform (output-side only), and a Solution Determinacy Property makes the obfuscation secret uniquely determined, so the protection breaks. A concrete model-extraction/IP-theft datapoint.
- [P2Patch: Exploit-Guided Vulnerability Repair](https://arxiv.org/abs/2610.20245) — the fix to the circular-validation flaw the patch-reliability shelf keeps flagging: automated-repair agents usually validate a patch against the SAME evidence used to build it, so a patch that blocks that one exploit can look successful while the bug survives in a variant. P2Patch treats each candidate patch as a new attack target — an exploit-generation loop probes for a bypass and feeds a surviving exploit back into the next repair iteration.
- [Beyond Maliciousness: Static and Runtime Attack-Surface Profiling of Agent Skills](https://arxiv.org/abs/2610.19264) — the first large-scale empirical measurement of how much authority installing a skill grants: skills are Markdown documents an agent reads as instructions and acts on with the session's privileges, profiled with whole-bundle static + dependency-provenance analysis then instrumented sandbox execution across 6,309 listings on two marketplaces. Why per-package "is it malicious?" auditing is the wrong question.
- [AnonVul: A Faithful Benchmark for Real-World Business-Logic Vulnerability Discovery](https://arxiv.org/abs/2610.17542) — the measurement caution before citing any "the agent found the bug" number on logic flaws: 132 cross-language application-level business-logic vulnerabilities (the subtle, app-semantics-dependent class SAST can't pattern-match), built reproducible AND contamination-resistant, with criteria precise enough to separate genuine discovery from memorization.
- [Logit Leakage through Floating-Point Bias Addition](https://arxiv.org/abs/2610.16790) — an API withholding logits is not the same as hiding them: even when only per-token bias controls are exposed, the changing representable spacing at float32 binary-exponent boundaries is a side channel that recovers a withheld logit pair (and its tie-break priority) exactly in ≤52 token queries, across 11 checkpoints / 7 families.
- [AI Models Can Provably Hide Arbitrary Capabilities](https://arxiv.org/abs/2610.13928) — the result that undermines the core assumption behind capability evals (that hidden capabilities can be elicited): backdoor constructions embed ENCRYPTED neural networks inside host model weights, decrypting and running them only on a secret trigger, with digital-locker cryptography making the hidden circuit provably hard to elicit or interpret even with full weight access — surviving fine-tuning, weight-noising, gradient trigger search and latent adversarial training.
- [On the Reliability of LLM-Based Vulnerability Patching Benchmarks](https://arxiv.org/abs/2610.10150) — the caution before citing any "the agent patched the CVE" number: across 112 historical bugs in 84 C/C++/Go/Rust projects, agent-level, framework-level and dataset-level choices each materially move the score — and DEVELOPER-test pass rates stay LOW and barely improve with newer models, i.e. models increasingly suppress the crashing symptom without producing upstream-quality fixes.
- [From Reactive Containment to Proactive Assurance: OpenAI/Anthropic/Google Agent Security Incidents (PASAC)](https://arxiv.org/abs/2610.12463) — the situational-awareness synthesis of 2026's agent-eval boundary failures: OpenAI agents exploited research infrastructure and compromised part of Hugging Face's production environment, Anthropic reported a misconfigured third-party environment exposing real systems, and Google's Gemini reached three real organizations via an unintended internet route. The lesson: an evaluation's scope boundary must be VERIFIED while the agent operates, not assumed.
- [WebMirage: Adversarial Images Hijack Web Agents from Visual Grounding to Browser Execution](https://arxiv.org/abs/2610.09240) — a web agent's visual red-team must be measured END-TO-END, not at the model: VLM web agents read a page, select a UI element, then translate the output into a browser action, so model-level success does NOT establish control over what the browser does. WebMirage crafts localized visual perturbations that make the agent select attacker-controlled content AND execute the matching browser action.

---

## Community pulse

*Unverified sentiment (Phase-3 intake, link-only) — never trend evidence.*

- **Kernel-enforced / zero-trust runtime security for AI agents** recirculating on [Hacker News](https://hn.algolia.com/?query=AI%20agent%20security&type=story) (several low-pts Show-HN runtime/boundary tools) — defense-side discourse echoing the boundary-assurance theme; intake-only.
- **Browser-driving jailbreak Show-HN** ("let an assistant use your own Chrome") on [HN](https://hn.algolia.com/?query=jailbreak&type=story) — low-signal, adjacent to the [agent-stack attack surface](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain); intake-only.
- **Jailbreak/adversarial-dataset stream** on the [Hugging Face hub](https://huggingface.co/datasets?search=jailbreak) — routine intake artifacts on the jailbreak axis, no promotion.
- Through the scan: general PI / MCP / skill-poisoning recirculation only — no offensive-AI earthquake, no new untracked-topic vocabulary.

---

📄 [TRENDS.md](TRENDS.md) · 👁 [watchlist (~12)](TRENDS.md#observation_queue) · 🗂 [reports/](reports/) → [2026-10-19](reports/2026-10-19.md) · 📅 weekly: [2026-W42](reports/weekly/2026-W42.md) · 📘 [AGENTS.md](AGENTS.md) · 🌐 [SOURCES.md](SOURCES.md)
