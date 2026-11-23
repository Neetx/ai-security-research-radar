# AI Security Radar

![trends](https://img.shields.io/badge/trends-19-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-9-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-17-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--11--23-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-11-23):**
- 🌱 **New seed — LLM-authored weight-space backdoors** — three independent groups show an LLM editing another model's weights straight from a natural-language spec to implant a persistent backdoor with no gradient training: [TrojanMaxxing](https://arxiv.org/abs/2611.27425) (VLMs), [Autonomous Parameter Surgery](https://arxiv.org/abs/2611.27920) and the founding [weight-space-programming study](https://arxiv.org/abs/2611.17395) → [weight-space backdoor programming](TRENDS.md#id-weight-space-backdoor-programming-020-llmagent-authored-backdoors-via-weight-space-programming-a-model-reads-and-rewrites-another-networks-weights-from-a-natural-language-spec-implanting-persistent-backdoors-with-no-gradient-training).
- 📈 **Serving-infrastructure attacks promoted seed → emerging** — the first in-the-wild confirmation that the inference-provider layer leaks tenant prompts ([Dragos canary tokens](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens), prompt theft measured at three providers), plus a prefill-timing defence ([Isonomy](https://arxiv.org/abs/2611.27596)) and a TensorRT-LLM integrity advisory ([CVE-2026-24205](https://nvd.nist.gov/vuln/detail/CVE-2026-24205)) → [LLM serving-infra / prompt-theft attacks](TRENDS.md#id-llm-serving-infra-attack-019-attacks-on-the-llm-servinginference-infrastructure-kv-cache-confidentiality-fault-injection--cross-tenant-isolation-failures-in-the-paged-serving-layer).
- 🧩 **Deployed-agent exploit chain** — a single malicious webpage drives Meta's shipped personal agent from chat-memory tampering to full cloud-machine RCE, bypassing its outbound monitor ([NebuSec](https://nebusec.ai/research/meta-muse-credential-exposure/)) → added to [agent-stack attacks](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain).
- 🛰 **Fresh evidence on three accelerating trends** — agentic vuln discovery reaches root-of-trust firmware/RTL ([Mjolnir](https://arxiv.org/abs/2611.27567)), a training-free weight-edit strips open-weight guardrails ([Cleave](https://arxiv.org/abs/2611.27426)), and [LightRAG poisoning](https://arxiv.org/abs/2611.27460) succeeds on a safety-critical knowledge base.

---

## Trends

🌱 1 · 📈 8 · 🚀 9 · 🌊 1 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-11-20](https://arxiv.org/abs/2611.27567) |
| [Attacks on LLM-agent stack: MCP, memory, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-11-20](https://nebusec.ai/research/meta-muse-credential-exposure/) |
| [RAG knowledge/document poisoning](TRENDS.md#id-rag-knowledge-poisoning-014-knowledgedocument-poisoning-of-retrieval-augmented-generation-rag-malicious-corpus-documents-steer-retrievalgeneration) | 🚀 accelerating | [2026-11-20](https://arxiv.org/abs/2611.27460) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-11-19](https://research.checkpoint.com/2026/30-years-of-gatekeeper-asymmetry-doom-the-paradox-that-makes-powerful-llms-more-vulnerable/) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 🚀 accelerating | [2026-11-19](https://arxiv.org/abs/2611.26117) |
| [Agent authorization & identity integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) | 🚀 accelerating | [2026-11-19](https://arxiv.org/abs/2611.25821) |
| [Provenance & watermark attacks (image/audio/video/text)](TRENDS.md#id-watermark-provenance-attack-015-defeating-generative-ai-content-provenance--watermarks-image--audio--video--text-removal-forgery--laundering-across-modalities) | 🚀 accelerating | [2026-11-17](https://arxiv.org/abs/2611.22345) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-11-16](https://www.crowdstrike.com/en-us/blog/supply-chain-risk-from-backdoored-lora-models/) |
| [Agent skill supply-chain poisoning (composition/chaining)](TRENDS.md#id-skill-supply-chain-poisoning-017-agent-skill-supply-chain-poisoning-malicious-skills-and-the-composition-chaining-of-individually-vetted-skills-into-behavior-per-skill-vetting-misses) | 🚀 accelerating | [2026-11-15](https://arxiv.org/abs/2611.19764) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 📈 emerging | [2026-11-20](https://arxiv.org/abs/2611.27426) |
| [LLM serving-infra / prompt-theft attacks](TRENDS.md#id-llm-serving-infra-attack-019-attacks-on-the-llm-servinginference-infrastructure-kv-cache-confidentiality-fault-injection--cross-tenant-isolation-failures-in-the-paged-serving-layer) | 📈 emerging | [2026-11-20](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 📈 emerging | [2026-11-19](https://arxiv.org/abs/2611.25695) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 📈 emerging | [2026-11-18](https://arxiv.org/abs/2611.24313) |
| [Undetectable covert channels & agent collusion](TRENDS.md#id-covert-channel-collusion-016-undetectable-covert-channels-in-llm-systems-steganographic-multi-agent-collusion--activation-level-exfiltration-that-defeat-transcriptmonitor-auditing) | 📈 emerging | [2026-11-16](https://arxiv.org/abs/2611.16928) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-11-06](https://arxiv.org/abs/2611.09348) |
| [Persistent-memory durable compromise](TRENDS.md#id-persistent-memory-durable-compromise-018-durable-compromise-of-llm-agent-persistentlong-term-memory-injected-or-leaked-state-that-survives-deletion-carries-over-after-the-attacker-leaves-and-self-reinforces) | 📈 emerging | [2026-11-06](https://arxiv.org/abs/2611.09721) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-11-05](https://arxiv.org/abs/2611.07370) |
| [LLM-authored weight-space backdoors](TRENDS.md#id-weight-space-backdoor-programming-020-llmagent-authored-backdoors-via-weight-space-programming-a-model-reads-and-rewrites-another-networks-weights-from-a-natural-language-spec-implanting-persistent-backdoors-with-no-gradient-training) | 🌱 seed | [2026-11-20](https://arxiv.org/abs/2611.27425) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🌊 mainstreaming | [2026-11-16](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold) |

---

## 🛠️ Tools & releases

No new public offensive-AI tool surfaced this scan (tool-discovery search + watched-repo release check both clean). Current standing roster:

- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.126.0** (npm, 2026-11-18).
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI (offensive red-team framework); **v1.2.1** (PyPI, 2026-11-16).
- [0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) — autonomous MCP/AI red-team framework: an MCP server exposing 150+ offensive tools to AI agents (MIT, 12.8k★/2.6k forks); named by [GTIG](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold) among frameworks seen in real intrusions.
- [AntiFox-AI/antifox](https://github.com/AntiFox-AI/antifox) — multi-agent autonomous-pentest platform (ARTEX-derivative; recon→exploitation→report, ~474★); tied by Arctic Wolf Labs to a real AWS production-secret theft.
- [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) — open-source AI-powered offensive-security harness (Go; LLM attack-orchestrator + built-in C2, 176+ MCP tools, ~1.9k★, **v1.1.14**), in-the-wild validated by [Kaspersky](https://securelist.com/cyberstrikeai-attacks/121715/).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.17.1**.
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.10**.
- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — a Dockerized collection of 38 offensive-security MCP servers / 300+ tools (Nmap, Ghidra, Nuclei, SQLMap, Hashcat, …).

---

## Worth studying

- [AI supply-chain security: canary tokens for LLM prompts](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens) — the in-the-wild datapoint on serving-layer prompt confidentiality: ~2M prompts seeded with canary links/credentials, and real prompt theft measured inside three inference providers, marketplace request-logging, and a lab fetching seeded secrets from >half of prompts. The LLM inference-provider layer leaks tenant prompts at scale.
- [Meta Muse credential exposure / Inside Meta Muse](https://nebusec.ai/research/meta-muse-credential-exposure/) — the deployed-agent exploit chain to internalize: a malicious webpage an agent opens exfiltrates and alters chat memory with no approval, then chains a built-in-browser flaw with a Linux-kernel flaw to fully own the user's cloud machine and bypass its outbound-traffic monitor. Indirect prompt injection reaches RCE on a shipped personal AI agent.
- [SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research](https://arxiv.org/abs/2611.26601) — the map to keep for the AI-vuln-discovery axis: claims that LLM agents find/validate/patch real vulnerabilities are scattered and rarely comparable. This SoK rates them on an AUTONOMY scale (modeled on driving-automation levels) and qualifies each by correctness, availability and strength of evidence.
- [When Shuffling Fails: Token Recovery from Obfuscated KV Caches](https://arxiv.org/abs/2611.24276) — the LLM-serving-confidentiality result to internalize: production systems store, offload and SHARE KV caches, exposing token-level representations to operators and co-tenants, and a popular defense shuffles them claiming security from the b! permutations. Input symmetry invalidates the bound — it recovers tokens anyway.
- [Living off the Local Model: Abusing Browser-Embedded LLMs for Post-Exploitation](https://arxiv.org/abs/2611.25086) — the new post-exploitation primitive: browsers ship local LLMs (Gemini Nano in Chrome), and each is a vendor-SIGNED, already-installed, network-invisible "living-off-the-land" engine an attacker drives from the host — no new binary to flag and no C2 traffic.
- [Stopping Is Not the Limit: Long-Horizon Vulnerability Exploitation](https://arxiv.org/abs/2611.22888) — the offensive-agent-capability datapoint: on ExploitBench, LM agents that develop working exploits routinely STOP with budget remaining, and eliciting continued execution yields additional VERIFIED exploits — a measured exploitation ceiling is partly a function of the agent's stopping behavior.
- [Can LLMs Write Backdoors? An Empirical Security Study of Weight-Space Programming](https://arxiv.org/abs/2611.17395) — the model-weight-integrity escalation: weight-space programming lets an LLM directly EDIT another network's weights from natural-language instructions with no gradient training, and this shows a general-purpose LLM can exploit it to INJECT backdoors with no task-specific data or gradients. (Now seeds the weight-space-backdoor trend.)
- [Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents](https://arxiv.org/abs/2611.15118) — the agent-integrity result: a capable model can be turned into a trigger-gated sleeper agent by editing FEWER THAN TEN "dormant" neurons in the final feed-forward block, with NO training and no data poisoning — model-weight integrity is a supply-chain concern even for internally-developed agents.
- [BypassGym: A Benchmark for Evaluating AI Agents' Endpoint Defense Evasion Capabilities](https://arxiv.org/abs/2611.13684) — existing offensive-agent benchmarks score pentest and vuln-discovery but NOT defense evasion; BypassGym is the first to measure whether an AI agent can write a program that runs its payload without being blocked or terminated by a deployed EDR.
- [OWASP Top 10 for LLM Applications 2026 + Agent Control Standard](https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members) — the flagship LLM-security standard's first major revision, published alongside a NEW Agent Control Standard — the first OWASP artifact aimed specifically at the agentic surface the agent-stack / authorization / skill-poisoning trends cover.
- [Introducing CAIRN: frontier tracking for AI-integrated malware](https://blog.talosintelligence.com/introducing-cairn-frontier-tracking-for-ai-integrated-malware/) — Cisco Talos's open-source framework + AI-usage-archetype taxonomy for classifying "AI-integrated malware", the lens behind Talos's in-the-wild series (NIK C2, the VOLTA infostealer's LLM-driven victim appraisal). A reusable way to catalog HOW real malware integrates AI.
- [ChatGPT Let Attackers Read Victims' Gmail Through a Hidden Channel Between Accounts](https://blog.checkpoint.com/research/chatgpt-let-attackers-read-victims-gmail-through-a-hidden-channel-between-accounts) — Check Point found a covert two-way channel between the code-execution containers of two ChatGPT conversations under DIFFERENT accounts, via a shared internal service — the real-world cross-account realization of the covert-channel line.

---

## Community pulse

*Unverified sentiment (Phase-3 intake, link-only) — never trend evidence.*

- The cycle's loudest AI-security thread followed the Chinese-nexus "Cairn" campaign — [AI agents that found and exploited a zero-day on their own](https://aws.amazon.com/blogs/security/) — tracked to its vendor primary (corroborates the in-the-wild AI-for-offense trend, not new evidence).
- Shadow-MCP discourse surfaced ("[43 MCP servers on one laptop, 9 in no config file](https://news.ycombinator.com/)") — an intake note on the agent/skill supply-chain attack surface, no artifact.
- The curated digests ([tldr sec](https://tldrsec.com/), [Simon Willison](https://simonwillison.net/)) surfaced no new offensive primary this scan; no new attack-class vocabulary coined.

---

📄 [TRENDS.md](TRENDS.md) · 👁 [watchlist (17)](TRENDS.md#observation_queue) · 🗂 [reports/](reports/) → [2026-11-23](reports/2026-11-23.md) · 📅 weekly: [2026-W47](reports/weekly/2026-W47.md) · 📘 [AGENTS.md](AGENTS.md) · 🌐 [SOURCES.md](SOURCES.md)
