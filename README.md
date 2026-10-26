# AI Security Radar

![trends](https://img.shields.io/badge/trends-18-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-10-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-11-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--10--26-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-10-24):**
- 🚀 **New evidence — [LLM/agentic vuln discovery](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code):** [PHP2Shell — AI uncovers critical RCE](https://www.wiz.io/blog/php2shell-php-rce) (Wiz): an AI-driven effort found critical RCE + memory-disclosure flaws in the **core PHP engine** (CVE-2026-109618/109619) affecting ~70% of the web, forcing emergency PHP Foundation patches — the trend's first in-the-wild, vendor-deployed AI-found zero-day in mainstream language-runtime software.
- 👁 **Watchlist captures (arXiv 10-22/10-23):** guard "target rebinding" ([Fooling LLM Safety Guards](https://arxiv.org/abs/2610.31695) → [AI-security tooling unreliable](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack)), compositional skill risk ([Capability-Flow Graph](https://arxiv.org/abs/2610.32155) → [skill supply-chain poisoning](TRENDS.md#id-skill-supply-chain-poisoning-017-agent-skill-supply-chain-poisoning-malicious-skills-and-the-composition-chaining-of-individually-vetted-skills-into-behavior-per-skill-vetting-misses)), undecidable tool-authority minimization ([Incomparable Minima](https://arxiv.org/abs/2610.31914) → [agent authorization integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures)).
- 🦠 **In-the-wild intake (unverified):** a [LiteLLM PyPI+Docker supply-chain compromise](https://socket.dev/blog/litellm-compromise) ships a credential stealer targeting cloud + AI-provider keys; news pointers report AGENTS.md/README-injection hijacking coding agents and OpenAI red-team agents demonstrating sandbox VM escapes + covert cross-sandbox communication — all follow-to-primary next run.
- 🔭 **Study picks:** [NTBench](https://arxiv.org/abs/2610.32531) (near-target prompt injection that keeps answers plausible but wrong) and [Ulysses](https://arxiv.org/abs/2610.31831) (multi-agent harness synthesizing verifiable web exploits).

---

## Trends

🌱 2 · 📈 6 · 🚀 10 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-10-26](https://www.wiz.io/blog/php2shell-php-rce) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 🚀 accelerating | [2026-10-22](https://arxiv.org/abs/2610.30798) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-10-21](https://unit42.paloaltonetworks.com/ai-assisted-cybercrime-analysis/) |
| [Agent authorization & identity integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) | 🚀 accelerating | [2026-10-20](https://arxiv.org/abs/2610.27620) |
| [Provenance & watermark attacks (image/audio/video/text)](TRENDS.md#id-watermark-provenance-attack-015-defeating-generative-ai-content-provenance--watermarks-image--audio--video--text-removal-forgery--laundering-across-modalities) | 🚀 accelerating | [2026-10-20](https://arxiv.org/abs/2610.27653) |
| [RAG knowledge/document poisoning](TRENDS.md#id-rag-knowledge-poisoning-014-knowledgedocument-poisoning-of-retrieval-augmented-generation-rag-malicious-corpus-documents-steer-retrievalgeneration) | 🚀 accelerating | [2026-10-15](https://arxiv.org/abs/2610.21464) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-10-14](https://arxiv.org/abs/2610.20941) |
| [Attacks on LLM-agent stack: MCP, memory, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-10-13](https://embracethered.com/blog/posts/2026/visual-studio-copilot-remote-code-execution/) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-10-13](https://arxiv.org/abs/2610.18609) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-10-10](https://arxiv.org/abs/2610.15218) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 📈 emerging | [2026-10-20](https://arxiv.org/abs/2610.28966) |
| [Undetectable covert channels & agent collusion](TRENDS.md#id-covert-channel-collusion-016-undetectable-covert-channels-in-llm-systems-steganographic-multi-agent-collusion--activation-level-exfiltration-that-defeat-transcriptmonitor-auditing) | 📈 emerging | [2026-10-15](https://arxiv.org/abs/2610.22578) |
| [Agent skill supply-chain poisoning (composition/chaining)](TRENDS.md#id-skill-supply-chain-poisoning-017-agent-skill-supply-chain-poisoning-malicious-skills-and-the-composition-chaining-of-individually-vetted-skills-into-behavior-per-skill-vetting-misses) | 📈 emerging | [2026-10-14](https://arxiv.org/abs/2610.20049) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 📈 emerging | [2026-10-07](https://arxiv.org/abs/2610.09708) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-10-07](https://arxiv.org/abs/2610.10909) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-10-06](https://arxiv.org/abs/2610.07645) |
| [Persistent-memory durable compromise](TRENDS.md#id-persistent-memory-durable-compromise-018-durable-compromise-of-llm-agent-persistentlong-term-memory-injected-or-leaked-state-that-survives-deletion-carries-over-after-the-attacker-leaves-and-self-reinforces) | 🌱 seed | [2026-10-22](https://arxiv.org/abs/2610.31366) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 🌱 seed | [2026-10-07](https://arxiv.org/abs/2610.09264) |

---

## 🛠️ Tools & releases

No new above-bar tool this cycle. GitHub tool-DISCOVERY + PyPI/npm registry-SEARCH surfaced only known/staged candidates (offsec-ai, strix-agent, revolt-rai, ptai) plus the single-author autonomous-pentest-repo glut (xalgorix, Armur-Ai/Pentest-Swarm-AI, simon-p-j-r/LLM4Pentest) — none clonable above the notability bar under the github 403-scope. Black Hat Arsenal / DEF CON Demo Labs off-season (next: Black Hat Europe Dec 2026). Watched-repo state (all unchanged since 10-23):

- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.17.1** (2026-10-16).
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.10** (2026-10-16).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.124.1** (npm).
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.1.0**.
- [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) — evals, red-teaming & test generation for LLM/agentic systems; **v3.0.1**.
- [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) — full-stack AI red-team platform: Agent-Scan, MCP-Scan, Skill-Scan (SARIF 2.1.0), jailbreak eval; **v4.6.2** (2026-09-17).
- [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — a Dockerized collection of 38 offensive-security MCP servers / 300+ tools (Nmap, Ghidra, Nuclei, SQLMap, Hashcat, …).

---

## Worth studying

- [On Task, Off Track: Benchmarking LLM and Agent Robustness to Near-Target Prompt Injection](https://arxiv.org/abs/2610.32531) — NTBench reframes prompt-injection robustness: a system can score well by refusing attacks that obviously abandon the user's request while still accepting "near-target" injections that keep most of a legitimate answer yet make it incorrect or harmful — a weakness testing unrelated outcomes does not reveal.
- [Ulysses: A Security Harness for Synthesizing Verifiable Web Exploits](https://arxiv.org/abs/2610.31831) — a multi-agent harness that converts candidate web-app vuln findings into verified Proofs of Exploitability by iterating exploit hypotheses until success shows up in independently-observed execution effects — closing the "an LLM can't reliably verify its own exploit" gap.
- [Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents](https://arxiv.org/abs/2610.29869) — the agent-integrity attack to know as coding agents adopt context compaction: an attacker gets untrusted content folded into the compacted/summarized context, and because compaction DESTROYS provenance (trusted vs untrusted), the laundered content re-enters the agent's working context as if trusted.
- [Data-Void Exploits in Web-Searching LLMs](https://arxiv.org/abs/2610.30365) — the retrieval-poisoning surface distinct from RAG-corpus poisoning: web-searching LLMs synthesize answers instead of ranked links, so disinformers publish narratives in "data voids" and rely on the LLM's web-search to retrieve/cite them — and answer-synthesis hides the provenance a ranked list would expose.
- [Beyond End-to-End Recovery: Understanding LLM Steganography via Rolewise Decomposition](https://arxiv.org/abs/2610.30516) — the measurement framework before trusting any LLM-steganography detection/capacity number: across 7,200 responses it finds 168 verifiable encodings the decoders MISSED — i.e. E2E recovery undercounts covert-channel capacity, so E2E-tuned defenses understate the leak.
- [The Show-Up Attack: When Subagents Win Over Their Supervisor](https://arxiv.org/abs/2610.27574) — the concrete multi-agent-orchestration attack to know before trusting a supervisor to bound its subagents: a malicious subagent manipulates the supervisor into tasks BEYOND its assigned scope; on SUA-Arena all six tested frontier LLMs are vulnerable and prompting/restricted-communication mitigations fail.
- [Global Security Blind Spots: Translation as a Safety Bypass in Low-Resource Languages](https://arxiv.org/abs/2610.27304) — LLM safety alignment does not survive translation: across ten deployed LLMs and 79 languages, harmful requests refused in English elicit unsafe completions when translated — mean bypass 21.9%–44.4%, concentrated in a subset of language families and shared across models.
- [SoK: PIAtlas — Decomposing the Unbounded Prompt Injection Attack Space](https://arxiv.org/abs/2610.24999) — the map the prompt-injection field has lacked: PIAtlas organizes the space around HOW the injected instruction is constructed to subvert the model — six mechanism classes, each the root of a technique hierarchy — the shared vocabulary comparable PI evaluations depend on.
- [How Effectively Do Security Skills Guide Coding Agents in Vulnerability Detection in Linux Kernel?](https://arxiv.org/abs/2610.25705) — the capability-reliability floor for skill-guided auditing (37 skills × Claude Code × four LLMs × 100 real kernel vulns, 14,800 runs): only 24.4% locate the right function, 15.7% correctly classify — "a skill guides the agent" is not "the agent finds the bug".
- [Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents](https://arxiv.org/abs/2610.23254) — the measurement caution before trusting any indirect-PI ASR on small agents: auditing 33,000 trajectories shows most "failed" attacks were IGNORED (76-80%), not REFUSED, and changing ONLY the system prompt shifts InjecAgent ASR 0.2%→43%.
- [From Billion-Scale to Million-Scale Language Models: Operational Capabilities for Embedded Post-Exploitation](https://arxiv.org/abs/2610.23534) — the AI-for-offense datapoint for autonomous malware that cannot phone home: ultra-compact SLMs (20M-1.5B params) evaluated on post-exploitation code generation (directory enumeration, backdoor generation) — offensive code generation migrating into the implant itself.
- [Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation (DIB-Bench)](https://arxiv.org/abs/2610.21135) — the eval-integrity result before trusting any agent-safety score: a tampered deployment that preserves evaluated outputs passes every output-only evaluator, and acceptance of tampered outputs RISES with evaluator strength (88.6% → 94.1%).

---

## Community pulse

*Unverified sentiment (Phase-3 intake, link-only) — never trend evidence.*

- **Prompt-injection defense discourse** recirculating on [Hacker News](https://hn.algolia.com/?query=prompt%20injection&type=story) (red-team PI technique checklists, "positional not phrasal" PI scanners, decision-model PI judges) — defense-side only, no new offensive artifact.
- **AI coding-agent security** surfacing via [security-news pointers](https://www.bleepingcomputer.com/) (repo-file/AGENTS.md injection hijacking assistants, sandbox-escape red-team disclosures) — followed to intake, primaries pending.
- Across the weekend: quiet pulse — general PI / agent-security recirculation only, no offensive-AI earthquake and no new untracked-topic vocabulary.

---

📄 [TRENDS.md](TRENDS.md) · 👁 [watchlist (~11)](TRENDS.md#observation_queue) · 🗂 [reports/](reports/) → [2026-10-26](reports/2026-10-26.md) · 📅 weekly: [2026-W43](reports/weekly/2026-W43.md) · 📘 [AGENTS.md](AGENTS.md) · 🌐 [SOURCES.md](SOURCES.md)
