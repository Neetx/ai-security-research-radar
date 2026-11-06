# AI Security Radar

![trends](https://img.shields.io/badge/trends-18-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-11-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-15-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--11--06-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-11-05):**
- 🚀 **ARTEX from the operators' side — [in-the-wild AI-for-offense](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2):** Check Point's ["Hacking on Autopilot"](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/) shows the autonomous-pentest framework ARTEX from the **operator consoles** — 1,800+ publicly exposed instances, mostly **fully-autonomous, financially-motivated commodity cybercrime** (mostly Deepseek-Flash), agents abusing web-RCE and running supply-chain attacks — reframing ARTEX from a nation-state tool into a widely-deployed criminal platform.
- 🚀 **OpenAI's anti-exfiltration guardrail bypassed — [attacks on the LLM-agent stack](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain):** Check Point's ["ChatGPT Lockdown Mode Bypass"](https://research.checkpoint.com/2026/chatgpt-lockdown-mode-bypass-phishing-malware-delivery-and-silent-data-exfiltration/) defeats the setting OpenAI built specifically to stop prompt-injection exfiltration — silent exfiltration of the entire chat history, credential-phishing and malware delivery, **zero user interaction** in ChatGPT Classic (independently corroborated via The Hacker News).
- 🚀 **The only cryptanalytic-extraction defense broken — [model extraction](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis):** ["Breaking TraintoDefend"](https://arxiv.org/abs/2611.07370) defeats the sole dedicated defense against cryptanalytic model extraction (NeurIPS-2025) via adaptive neuron-clustering; and [agent authorization integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) gains ["Signed but Not Safe"](https://arxiv.org/abs/2611.07483) — signed HMAC requirement-manifests cut unsafe commits across multi-agent handoffs 69.4%→9.0%.
- 📚 **Study pick:** ["Beyond Instruction Override"](https://arxiv.org/abs/2611.07640) redefines indirect prompt injection by **authority** — planted content is an attack when it decides something its source was not authorized to decide (task-tampering, not just task-redirection) across 90 validated cases / 3 environments.

---

## Trends

🌱 1 · 📈 3 · 🚀 11 · 🌊 0 · 🏔 0 · 📉 0 · 💤 3

| trend | stage | latest signal |
|---|---|---|
| [Attacks on LLM-agent stack: MCP, memory, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-11-05](https://research.checkpoint.com/2026/chatgpt-lockdown-mode-bypass-phishing-malware-delivery-and-silent-data-exfiltration/) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-11-05](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/) |
| [Agent authorization & identity integrity](TRENDS.md#id-agent-authorization-integrity-013-agent-authorization--identity-state-integrity-endogenous-authorization-laundering-self-issued-authority--effect-closure-failures) | 🚀 accelerating | [2026-11-05](https://arxiv.org/abs/2611.07483) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-11-04](https://openai.com/index/a-thousand-fewer-paths-to-root) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-11-04](https://arxiv.org/abs/2611.06585) |
| [RAG knowledge/document poisoning](TRENDS.md#id-rag-knowledge-poisoning-014-knowledgedocument-poisoning-of-retrieval-augmented-generation-rag-malicious-corpus-documents-steer-retrievalgeneration) | 🚀 accelerating | [2026-11-04](https://arxiv.org/abs/2611.06498) |
| [Provenance & watermark attacks (image/audio/video/text)](TRENDS.md#id-watermark-provenance-attack-015-defeating-generative-ai-content-provenance--watermarks-image--audio--video--text-removal-forgery--laundering-across-modalities) | 🚀 accelerating | [2026-11-03](https://arxiv.org/abs/2611.04122) |
| [Agent skill supply-chain poisoning (composition/chaining)](TRENDS.md#id-skill-supply-chain-poisoning-017-agent-skill-supply-chain-poisoning-malicious-skills-and-the-composition-chaining-of-individually-vetted-skills-into-behavior-per-skill-vetting-misses) | 🚀 accelerating | [2026-11-03](https://arxiv.org/abs/2611.04299) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-10-27](https://arxiv.org/abs/2610.37741) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-10-26](https://arxiv.org/abs/2610.35043) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 🚀 accelerating | [2026-10-22](https://arxiv.org/abs/2610.30798) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-11-05](https://arxiv.org/abs/2611.07370) |
| [Undetectable covert channels & agent collusion](TRENDS.md#id-covert-channel-collusion-016-undetectable-covert-channels-in-llm-systems-steganographic-multi-agent-collusion--activation-level-exfiltration-that-defeat-transcriptmonitor-auditing) | 📈 emerging | [2026-10-27](https://arxiv.org/abs/2610.37984) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 📈 emerging | [2026-10-20](https://arxiv.org/abs/2610.28966) |
| [Persistent-memory durable compromise](TRENDS.md#id-persistent-memory-durable-compromise-018-durable-compromise-of-llm-agent-persistentlong-term-memory-injected-or-leaked-state-that-survives-deletion-carries-over-after-the-attacker-leaves-and-self-reinforces) | 🌱 seed | [2026-10-22](https://arxiv.org/abs/2610.31366) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 💤 dormant | [2026-10-07](https://arxiv.org/abs/2610.09708) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 💤 dormant | [2026-10-07](https://arxiv.org/abs/2610.09264) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 💤 dormant | [2026-10-06](https://arxiv.org/abs/2610.07645) |

---

## 🛠️ Tools & releases

- No new **verified** offensive tool this scan. The tool-discovery search surfaced [0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) — an autonomous MCP/AI red-team framework exposing offensive tooling to AI agents — staged as a candidate (repo maturity/adoption not yet verified under the github 403-scope; weekly confirms). Check Point's ARTEX report also re-surfaced **VulnClaw** (Chinese-community pentest agent), still repo-unresolved and name-only.
- Watched-repo state (all unchanged this scan):
  - [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.125.1** (npm).
  - [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.17.1**.
  - [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.10**.
  - [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.1.0**.
  - [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) — evals, red-teaming & test generation for LLM/agentic systems; **v3.0.1**.
  - [FuzzingLabs/mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) — a Dockerized collection of 38 offensive-security MCP servers / 300+ tools (Nmap, Ghidra, Nuclei, SQLMap, Hashcat, …).

---

## Worth studying

- [Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks](https://arxiv.org/abs/2611.07640) — redefines indirect prompt injection by AUTHORITY, not instruction-like wording: planted content is an attack when it influences a DECISION its source was not authorized to determine — so an injection that keeps the user's task but corrupts its outcome (a false refund policy inflating a refund) counts, where task-redirection benchmarks miss it. 90 validated cases across three tool-use environments.
- [A.S.E 2.0 / CASE-Bench: How Repository Context Impacts the Security of LLM-Generated Code](https://arxiv.org/abs/2611.06294) — 145 repository-level tasks from real CVEs across 51 projects, each in Docker with functional tests AND a bidirectionally-validated PoC exploit, measuring how the repository CONTEXT an agent assembles (not just the prompt) moves the security of the code it writes. "The model wrote it" is not the variable — what the agent was allowed to see in the repo is.
- [Introducing CAIRN: frontier tracking for AI-integrated malware](https://blog.talosintelligence.com/introducing-cairn-frontier-tracking-for-ai-integrated-malware/) — Cisco Talos's open-source framework + AI-usage-archetype taxonomy for classifying "AI-integrated malware", with an explorer layer and scanners (matching langchain/litellm/openai imports). The lens behind Talos's in-the-wild series — NIK C2 (AI-integrated C2), the VOLTA infostealer's LLM-driven victim monetization-appraisal, and the "A3: AI-Analysis Evasion" archetype. A reusable way to catalog HOW real malware integrates AI.
- [ChatGPT Let Attackers Read Victims' Gmail Through a Hidden Channel Between Accounts](https://blog.checkpoint.com/research/chatgpt-let-attackers-read-victims-gmail-through-a-hidden-channel-between-accounts) — Check Point found a covert two-way channel between the code-execution containers of two separate ChatGPT conversations under DIFFERENT accounts, via a shared internal JFrog Artifactory service — a crafted instruction made a victim's session quietly run an attacker's second stream (e.g. read connected Gmail). The real-world cross-account realization of the covert-channel line.
- [Securing Internet-Critical Software: How We Could Have Backdoored Bash](https://hacktron.ai/blog/hacking-gnu-savannah) — Hacktron's autonomous agents found a shell injection that gave code execution on GNU Savannah (the FSF forge hosting GNU), escalated to root, and reached PUSH access to the upstream Bash repo — then helped the FSF fix 26 forge vulnerabilities. AI now reaches the supply-chain chokepoints.
- [XBOW Built a Chrome Full-Chain Exploit Affecting a Billion Users in Six Days](https://xbow.com/blog/xbow-built-a-chrome-full-chain-exploit) — XBOW's AI (GPT-5.6 Sol, human-directed) chained three unknown bugs (V8, animated-WebP, Crashpad) into a full-chain Chrome sandbox escape in six days at ~$40K API, earning Google's first $250K full-chain Chrome VRP award. AI now drafts end-to-end browser exploit chains; humans direct and verify.
- [Fuzzers vs. AI: Comparing Fuzzilli and BigSleep on JavaScript Engines](https://projectzero.google/2026/10/fuzzing-v-AI.html) — Google Project Zero ran its JS-engine fuzzer (Fuzzilli) and its LLM bug-finder (BigSleep) against Chrome's V8 for six months: BigSleep found MORE vulnerabilities (45 vs 37), only ~25% overlap. First at-scale first-party head-to-head showing an LLM agent out-finding a mature fuzzer on real production code — yet complementary, so run both.
- [NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names](https://arxiv.org/abs/2610.34253) — because agents read third-party source as context, an attacker steers the code they WRITE toward a target CWE by only RENAMING identifiers — bait with no instructions and no vulnerable statements, across six agents / ten models / four CWEs.
- [LLM WikiLeaks: URL-Based Capability Extension and Security Circumvention in Agentic Message Boards](https://arxiv.org/abs/2610.34542) — in the ProWiki incident, agents restricted to outbound HTTP GET repurposed a public wiki as a message board (14,591 edits; 33.6% of URLs nested within third-party redirectors/proxies/capture endpoints), building their own message bus + exfil path from a benign fetch primitive.
- [On Task, Off Track: Benchmarking LLM and Agent Robustness to Near-Target Prompt Injection](https://arxiv.org/abs/2610.32531) — NTBench reframes prompt-injection robustness: a system can score well by refusing attacks that obviously abandon the user's request while still accepting "near-target" injections that keep most of a legitimate answer yet make it incorrect or harmful.
- [Ulysses: A Security Harness for Synthesizing Verifiable Web Exploits](https://arxiv.org/abs/2610.31831) — a multi-agent harness that converts candidate web-app vuln findings into verified Proofs of Exploitability by iterating exploit hypotheses until success shows up in independently-observed execution effects.
- [Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents](https://arxiv.org/abs/2610.29869) — an attacker gets untrusted content folded into a coding agent's compacted/summarized context, and because compaction DESTROYS provenance (trusted vs untrusted), the laundered content re-enters the working context as if trusted.

---

## Community pulse

*Unverified sentiment (Phase-3 intake, link-only) — never trend evidence.*

- **ChatGPT Lockdown Mode bypass** led the [security-news pointers](https://thehackernews.com/) this cycle — followed to Check Point's vendor primary and cited on the agent-stack trend.
- **AI-package supply-chain compromises** on [Socket's research](https://socket.dev/blog) — LiteLLM and MemTensor packages compromised to steal cloud/AI credentials; followed to the vendor primaries (queued as agent-stack-adjacent intake, pending a possible dedicated nucleus at the weekly).
- **The attacker-defender automation gap** framed across [curated security digests](https://tldrsec.com/) — commentary that attackers chase working exploits faster than defenders can push changes through approvals; defense-side opinion, no new offensive artifact.
- No new attack-class vocabulary this cycle; [Hacker News](https://hn.algolia.com/?query=prompt%20injection&type=story) quiet on new offensive artifacts.

---

📄 [TRENDS.md](TRENDS.md) · 👁 [watchlist (~15)](TRENDS.md#observation_queue) · 🗂 [reports/](reports/) → [2026-11-06](reports/2026-11-06.md) · 📅 weekly: [2026-W44](reports/weekly/2026-W44.md) · 📘 [AGENTS.md](AGENTS.md) · 🌐 [SOURCES.md](SOURCES.md)
