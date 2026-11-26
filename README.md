# AI Security Radar

![trends](https://img.shields.io/badge/trends-20-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-9-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-31-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--11--26-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-11-26):**
- 🔎 **Fingerprint the model behind an agent, then attack it** — a remote service can identify an agent's backend LLM black-box, purely from the agent's tool/API responses, to aim model-specific prompt injection at it ([CAPTA](https://arxiv.org/abs/2611.32686)) → [model extraction & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) (held off dormancy).
- 🛡 **Poisoning a self-evolving *defense* into self-DoS** — one prompt-injection episode makes a learning defense adopt an over-broad policy that then refuses legitimate requests, transferring across models ([Poisoning Self-Evolving Security Policies](https://arxiv.org/abs/2611.33385)) → [self-evolving-agent poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) (held off dormancy).
- 🧬 **Hardware bit-flip backdoors are clustering** — three independent groups in two days implant backdoors or misclassification into LLM/VLM/DNN weights at inference via rowhammer, EMFI and supply-chain layout tricks ([FlipVLA](https://arxiv.org/abs/2611.33810), [BridgeHammer](https://arxiv.org/abs/2611.34684), [RegionAlign](https://arxiv.org/abs/2611.33370)) — watch-listed as a convergence candidate.
- 📚 **New vuln-discovery benchmark for closed-source binaries** — DeepBinary measures frontier models on open-ended vulnerability discovery in the Windows kernel, not just known CVEs in open source ([DeepBinary](https://arxiv.org/abs/2611.33486)).

---

## Trends

🌱 1 · 📈 9 · 🚀 9 · 🌊 1 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Agent authorization & identity integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) | 🚀 accelerating | [2026-11-24](https://arxiv.org/abs/2611.32195) |
| [Attacks on LLM-agent stack: MCP, memory, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-11-21](https://arxiv.org/abs/2611.28763) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-11-20](https://arxiv.org/abs/2611.27567) |
| [RAG knowledge/document poisoning](TRENDS.md#id-rag-knowledge-poisoning-014-knowledgedocument-poisoning-of-retrieval-augmented-generation-rag-malicious-corpus-documents-steer-retrievalgeneration) | 🚀 accelerating | [2026-11-20](https://arxiv.org/abs/2611.27460) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-11-19](https://research.checkpoint.com/2026/30-years-of-gatekeeper-asymmetry-doom-the-paradox-that-makes-powerful-llms-more-vulnerable/) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 🚀 accelerating | [2026-11-19](https://arxiv.org/abs/2611.26117) |
| [Provenance & watermark attacks (image/audio/video/text)](TRENDS.md#id-watermark-provenance-attack-015-defeating-generative-ai-content-provenance--watermarks-image--audio--video--text-removal-forgery--laundering-across-modalities) | 🚀 accelerating | [2026-11-17](https://arxiv.org/abs/2611.22345) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-11-16](https://www.crowdstrike.com/en-us/blog/supply-chain-risk-from-backdoored-lora-models/) |
| [Agent skill supply-chain poisoning (composition/chaining)](TRENDS.md#id-skill-supply-chain-poisoning-017-agent-skill-supply-chain-poisoning-malicious-skills-and-the-composition-chaining-of-individually-vetted-skills-into-behavior-per-skill-vetting-misses) | 🚀 accelerating | [2026-11-15](https://arxiv.org/abs/2611.19764) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-11-24](https://arxiv.org/abs/2611.32686) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-11-24](https://arxiv.org/abs/2611.33385) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 📈 emerging | [2026-11-23](https://arxiv.org/abs/2611.30004) |
| [Agent-security benchmark-verdict reliability](TRENDS.md#id-agent-security-eval-reliability-021-the-reliability-of-llm-agent-security-benchmark-verdicts-attackdefense-success-rates-that-are-not-reproducible-not-attributable-to-the-system-under-test-or-gameable-by-the-grader) | 📈 emerging | [2026-11-23](https://arxiv.org/abs/2611.31541) |
| [LLM serving-infra / prompt-theft attacks](TRENDS.md#id-llm-serving-infra-attack-019-attacks-on-the-llm-servinginference-infrastructure-kv-cache-confidentiality-fault-injection--cross-tenant-isolation-failures-in-the-paged-serving-layer) | 📈 emerging | [2026-11-22](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 📈 emerging | [2026-11-20](https://arxiv.org/abs/2611.27426) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 📈 emerging | [2026-11-18](https://arxiv.org/abs/2611.24313) |
| [Undetectable covert channels & agent collusion](TRENDS.md#id-covert-channel-collusion-016-undetectable-covert-channels-in-llm-systems-steganographic-multi-agent-collusion--activation-level-exfiltration-that-defeat-transcriptmonitor-auditing) | 📈 emerging | [2026-11-16](https://arxiv.org/abs/2611.16928) |
| [Persistent-memory durable compromise](TRENDS.md#id-persistent-memory-durable-compromise-018-durable-compromise-of-llm-agent-persistentlong-term-memory-injected-or-leaked-state-that-survives-deletion-carries-over-after-the-attacker-leaves-and-self-reinforces) | 📈 emerging | [2026-11-06](https://arxiv.org/abs/2611.09721) |
| [LLM-authored weight-space backdoors](TRENDS.md#id-weight-space-backdoor-programming-020-llmagent-authored-backdoors-via-weight-space-programming-a-model-reads-and-rewrites-another-networks-weights-from-a-natural-language-spec-implanting-persistent-backdoors-with-no-gradient-training) | 🌱 seed | [2026-11-20](https://arxiv.org/abs/2611.27425) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🌊 mainstreaming | [2026-11-24](https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/) |

---

## 🛠️ Tools & releases

- [oritera/Cairn](https://github.com/oritera/Cairn) — open-source "AI state-space search engine, validated first on autonomous penetration testing" (AGPLv3; blackboard/fact-intent-graph coordination, Docker dispatcher, Claude Code/Codex/Pi backends); the framework China-nexus actors used to autonomously find a zero-day in the wild and the one Unit 42 keeps tracking across campaigns.
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.126.0** (npm, 2026-11-18).
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI (offensive red-team framework); **v1.2.1** (PyPI, 2026-11-16).
- [0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) — autonomous MCP/AI red-team framework: an MCP server exposing 150+ offensive tools to AI agents (MIT, 12.8k★/2.6k forks); named by GTIG among frameworks seen in real intrusions.
- [AntiFox-AI/antifox](https://github.com/AntiFox-AI/antifox) — multi-agent autonomous-pentest platform (ARTEX-derivative; recon→exploitation→report, ~474★); tied by Arctic Wolf Labs to a real AWS production-secret theft.
- [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) — open-source AI-powered offensive-security harness (Go; LLM attack-orchestrator + built-in C2, 176+ MCP tools, ~1.9k★, **v1.1.14**), in-the-wild validated by [Kaspersky](https://securelist.com/cyberstrikeai-attacks/121715/) and now [Unit 42](https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.17.1**.
- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — a Dockerized collection of 38 offensive-security MCP servers / 300+ tools (Nmap, Ghidra, Nuclei, SQLMap, Hashcat, …).

*No new on-axis tool this scan — GitHub tool-discovery surfaced only the already-tracked single-author pentest-agent set; watched PyPI versions unchanged.*

---

## Worth studying

- [Benchmarking Open-Ended Vulnerability Discovery in Windows Kernel Binaries (DeepBinary)](https://arxiv.org/abs/2611.33486) — the first benchmark to measure frontier models on OPEN-ENDED vuln discovery in CLOSED-SOURCE production binaries (the Windows kernel), where existing benchmarks almost all use known CVEs in open-source code — the closest proxy yet for "can a model find a real 0-day in a shipped binary."
- [When Answering Is Administering: Permission Replies That Rewrite Coding-Agent Policy](https://arxiv.org/abs/2611.32195) — a plugin/service allowed only to answer a permission prompt can attach an update that DELETES the operator's deny rule (Claude Code checks only additions of allow rules), so one approval strips the deny rule protecting secrets and the agent reads them even inside the strict sandbox, via relays that already exist. The right to answer a prompt is the right to administer.
- ["I Do Intend to Deliver": Will LLMs Run a Marketplace Advance-Fee Scam?](https://arxiv.org/abs/2611.32957) — the AI-for-offense economics datapoint: fraud was bounded by the human labor of talking to victims, and ten off-the-shelf models (no jailbreak) playing the "free item, just pay delivery" seller closed 61% of 1,200 conversations with the buyer paying, 8/10 models playing almost every time, at ~2.5¢ per payment.
- [Who Is Prompt-Injecting Coding Agents? An Empirical Study of Hidden AI-Directed Text on GitHub](https://arxiv.org/abs/2611.28763) — the in-the-wild-prevalence study for the agent-injection axis: ~145M issues/PRs/comments/READMEs analyzed for text GitHub does not render to humans but agents receive in full, measuring who deploys hidden AI-directed text and why — moving the GitHub-PI surface from controlled proofs to a field study.
- [Chinese-nexus actor's Cairn AI agents found a zero-day on their own](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/) — the in-the-wild autonomous-ZERO-DAY-DISCOVERY datapoint: a China-linked operator gave the open-source Cairn AI-pentest framework only a goal; the agents found a novel path-traversal flaw in MONAI Label on their own, wrote files in ~11 minutes, then planted a startup file a training job ran, reaching root on a university server.
- [AI supply-chain security: canary tokens for LLM prompts](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens) — the in-the-wild datapoint on serving-layer prompt confidentiality: ~2M prompts seeded with canary links/credentials, and real prompt theft measured inside three inference providers, marketplace request-logging, and a lab fetching seeded secrets from >half of prompts. The LLM inference-provider layer leaks tenant prompts at scale.
- [Meta Muse credential exposure / Inside Meta Muse](https://nebusec.ai/research/meta-muse-credential-exposure/) — the deployed-agent exploit chain to internalize: a malicious webpage an agent opens exfiltrates and alters chat memory with no approval, then chains a built-in-browser flaw with a Linux-kernel flaw to fully own the user's cloud machine and bypass its outbound-traffic monitor. Indirect prompt injection reaches RCE on a shipped personal AI agent.
- [SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research](https://arxiv.org/abs/2611.26601) — the map to keep for the AI-vuln-discovery axis: claims that LLM agents find/validate/patch real vulnerabilities are scattered and rarely comparable. This SoK rates them on an AUTONOMY scale (modeled on driving-automation levels) and qualifies each by correctness, availability and strength of evidence.
- [When Shuffling Fails: Token Recovery from Obfuscated KV Caches](https://arxiv.org/abs/2611.24276) — the LLM-serving-confidentiality result to internalize: production systems store, offload and SHARE KV caches, exposing token-level representations to operators and co-tenants, and a popular defense shuffles them claiming security from the b! permutations. Input symmetry invalidates the bound — it recovers tokens anyway.
- [Living off the Local Model: Abusing Browser-Embedded LLMs for Post-Exploitation](https://arxiv.org/abs/2611.25086) — the new post-exploitation primitive: browsers ship local LLMs (Gemini Nano in Chrome), and each is a vendor-SIGNED, already-installed, network-invisible "living-off-the-land" engine an attacker drives from the host — no new binary to flag and no C2 traffic.
- [Stopping Is Not the Limit: Eliciting Agent Capability in Long-Horizon Vulnerability Exploitation](https://arxiv.org/abs/2611.22888) — on ExploitBench, LM agents that develop working exploits routinely STOP with test-time budget remaining, and eliciting continued execution past the first stop yields additional verified exploits — a reported exploitation ceiling is partly a function of the agent's stopping behavior, not the model.
- [Can LLMs Write Backdoors? An Empirical Security Study of Weight-Space Programming](https://arxiv.org/abs/2611.17395) — the model-weight-integrity escalation: weight-space programming lets an LLM directly EDIT another network's weights from natural-language instructions with no gradient training, and this shows a general-purpose LLM can exploit it to INJECT backdoors with no task-specific data or gradients. (Seeds the weight-space-backdoor trend.)

---

## Community pulse

*Unverified sentiment (Phase-3 intake, link-only) — never trend evidence.*

- A practitioner PoC circulated — [prompt injection in a job application makes AI recruiting agents leak salaries](https://vortner.de/blog/prompt-injection-job-application) — an intake note on the indirect-injection-against-hiring-agents surface, no primary artifact yet.
- The day's on-axis thread remained the [autonomous-AI-agent 0-day story](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/) — community echo of an already-captured in-the-wild primary, not new discourse-evidence.
- A dev-tooling observation trended — [most prompt injections a triage bot saw came from dev tools, not attackers](https://www.docsgpt.cloud/blog/github-triage-agents) — context for the hidden-AI-directed-text-on-GitHub study, intake only.
- The curated digests ([tldr sec](https://tldrsec.com/), [Simon Willison](https://simonwillison.net/)) surfaced no new offensive primary this scan; no new attack-class vocabulary coined.

---

📄 [TRENDS.md](TRENDS.md) · 👁 [watchlist (31)](TRENDS.md#observation_queue) · 🗂 [reports/](reports/) → [2026-11-26](reports/2026-11-26.md) · 📅 weekly: [2026-W47](reports/weekly/2026-W47.md) · 📘 [AGENTS.md](AGENTS.md) · 🌐 [SOURCES.md](SOURCES.md)
