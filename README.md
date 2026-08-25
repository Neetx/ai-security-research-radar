# AI Radar

![trends](https://img.shields.io/badge/trends-12-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-6-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-27-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--08--25-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-08-25):** one stage move, two study picks, a new standards taxonomy.
- 📈 **[Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) promoted seed→emerging:** **[SkillBloat](https://arxiv.org/abs/2608.21929)** (2026-08-22) — a malicious agent skill abuses the trusted-instruction channel purely to inflate token consumption **5.4×–10.1×** with output correctness preserved. The 4th independent group (skill-channel token amplification) past the detour-hijack / MoE-router / persona-conditioning vectors already tracked.
- 🛠️ **Study shelf +2:** **[AI Grinding for Cryptanalysis](https://arxiv.org/abs/2608.21986)** — an autonomous cryptanalysis agent lands **eight** published-construction breaks with exact witnesses (AI-for-offense reaches the crypto domain); and **[DarkBot](https://arxiv.org/abs/2608.23185)** — the first multi-agent LLM system for **active** CTI elicitation, deployed live on real underground forums.
- 📐 **Standards:** the **[OWASP Agentic Skills Top 10](https://owasp.org/www-project-agentic-skills-top-10/)** (AST01 Malicious Skills → AST10 Cross-Platform Reuse) codifies the agent-skill/supply-chain and skill-scanner axes the radar already tracks (public-review v1 draft).
- 🛰️ **[In-the-wild AI-for-offense](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) at 22 days — HELD, not downgraded:** the in-the-wild lane is now fully checkable ([Trend Micro reached](https://www.trendmicro.com/en_us/research/26/g/autonomous-ransomware.html) — newest autonomous-AI-offense research is 07-24, pre-window), no new primary; the formal dormant-vs-hold call is reserved for weekly W35.

---

## Trends

🌱 1 · 📈 4 · 🚀 6 · 🌊 0 · 🏔 0 · 📉 0 · 💤 1

| trend | stage | latest signal |
|---|---|---|
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-08-21](https://arxiv.org/abs/2608.20637) |
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-08-20](https://adversa.ai/blog/cryptographic-context-injection-grok-data-theft/) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 🚀 accelerating | [2026-08-17](https://arxiv.org/abs/2608.16246) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🚀 accelerating | [2026-08-11](https://arxiv.org/abs/2608.10959) |
| [Mechanistic basis of jailbreaks: refusal & harmfulness directions](TRENDS.md#id-refusal-direction-mechanics-005-the-mechanisticrepresentation-basis-of-jailbreaks-refusal--harmfulness-as-manipulable-linear-directions) | 🚀 accelerating | [2026-08-06](https://arxiv.org/abs/2608.05578) |
| [In-the-wild AI-for-offense: LLM malware dev & C2](TRENDS.md#id-ai-offensive-operations-009-in-the-wild-ai-for-offense-llms-weaponized-to-develop-malware-and-automate-offensive-operations-c2) | 🚀 accelerating | [2026-08-03](https://arxiv.org/abs/2608.01639) |
| [Economic/availability DoS on LLM systems](TRENDS.md#id-llm-resource-exhaustion-dos-012-economicavailability-dos-on-llm-systems-resource-amplification--cost-inflation-attacks-that-preserve-output-correctness) | 📈 emerging | [2026-08-22](https://arxiv.org/abs/2608.21929) |
| [Model extraction, distillation & fingerprinting](TRENDS.md#id-model-extraction-fingerprinting-006-model-extraction-capability-distillation--fingerprinting-under-restrictive-apis) | 📈 emerging | [2026-08-20](https://arxiv.org/abs/2608.20055) |
| [Self-evolving-agent skill poisoning](TRENDS.md#id-self-evolving-agent-poisoning-010-poisoning-the-experienceskill-promotion-pipeline-of-self-evolving-agents-untrusted-experience-laundered-into-trusted-persistent-skills) | 📈 emerging | [2026-08-07](https://arxiv.org/abs/2608.06862) |
| [Physical-channel PI on embodied & wearable AI](TRENDS.md#id-embodied-physical-injection-007-physical--perception-channel-prompt-injection-against-embodied--wearable-ai-agents) | 📈 emerging | [2026-08-06](https://arxiv.org/abs/2608.05715) |
| [Automated red-teaming of AI agents](TRENDS.md#id-automated-agent-redteam-011-autonomousagentic-red-teaming-systems-that-recon-and-attack-other-production-ai-agents-building-reusable-attack-knowledge) | 🌱 seed | [2026-08-12](https://arxiv.org/abs/2608.11878) |
| [Weaponized LLM hallucination (slopsquatting supply chain)](TRENDS.md#id-hallucination-squatting-008-weaponized-llm-hallucination-predictable-resource-name-hallucination-pre-registered-as-an-ai-supply-chain-attack-slopsquatting) | 💤 dormant | [2026-07-14](https://arxiv.org/abs/2607.12340) |

---

## 🛠️ Tools & releases

**No new verified tool this scan.** The 08-24-staged [Offensive-MCP-AI](https://github.com/CyberSecurityUP/Offensive-MCP-AI) was verified (27★ / 10 commits, early-stage PoC) → below the notability bar, not promoted. Newly surfaced on the automated-agent-redteam axis and staged for verification: [Decepticon](https://github.com/PurpleAILAB/Decepticon), [RedteamAgent](https://github.com/NeoTheCapt/RedteamAgent). Watched packaged tools all unchanged (garak 0.16.0 / PyRIT 1.0.1 / deepteam 1.0.9 / giskard 2.19.2 / promptfoo 0.122.0). The current on-axis tool set:

- [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) — autonomous-pentest harness (13+ agents, 176 MCP tools, Ed25519-signed skills, OWASP/MITRE/CIS-aligned); 1.9k★, npm `@cyberstrike-io/cyberstrike`.
- [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) — full-stack AI red-team platform: Agent-Scan, MCP-Scan, Skill-Scan (SARIF 2.1.0), jailbreak eval (26+ methods); **v4.5.2** (2026-08-17).
- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) — framework to red-team LLMs and AI agents; **v1.0.9** (latest on PyPI, 2026-08-12).
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — the LLM vulnerability scanner; **v0.16.0** (latest on PyPI).
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — prompt/agent/RAG red-teaming & pentesting; **v0.122.0** (latest on npm).
- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) — Python Risk Identification Tool for generative AI; **v1.0.1** — the major v1 architectural redesign.
- [airtasystems/DVAIA-Damn-Vulnerable-AI-Application](https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application) — a DVWA-style deliberately-vulnerable LLM/agent lab (prompt injection, jailbreaks, indirect injection, RAG poisoning, tool-use vulns).
- [GH05TCREW/pentestagent](https://github.com/GH05TCREW/pentestagent) — **PentestAgent**, a mature open-source AI-agent framework for black-box pentesting/bug-bounty — RAG knowledge base, attack playbooks, MCP client/server.

---

## Worth studying

- [DarkBot: Automated CTI Elicitation in Underground Forums](https://arxiv.org/abs/2608.23185) — AI moving from passive monitoring to **active** deceptive engagement of adversaries: 11 specialized agents (engagement-gating, MITRE-ATT&CK-driven question generation, linguistic style adaptation) recover 72.8% of validated ATT&CK techniques from only the initial post, and in a live matched deployment across 104 real conversations accumulate +3.85 more CTI entities than controls with no moderator interventions.
- [AI Grinding for Fun and Cryptanalysis](https://arxiv.org/abs/2608.21986) — the reference for autonomous AI as a working cryptanalysis collaborator: an agent workflow returns reproducible candidates with exact witnesses/controls/code, landing **eight** published constructions failing at their stated parameters (a Ring-LWR commitment opening to every message w.p. 1, a lattice e-voting protocol losing receipt-freeness, a colliding signature hash, and more).
- [GhostTac: Manipulating Tactile Sensors without Physical Contact](https://arxiv.org/abs/2608.20817) — a new physical-layer attack surface on embodied AI: the first **contactless** attack on robotic tactile sensing, using electromagnetic interference to imprint persistent DC offsets that bypass onboard filtering and force harmful robot behavior. Demonstrated across 15 sensors / 10 modules / two dexterous hands.
- [MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection](https://arxiv.org/abs/2608.19901) — the consolidated dataset to test malicious-Skill detection against: 9,740 Skills across 4,588 structural families and 11 attack categories. Learned detectors fall from 0.88–0.93 Macro-F1 to **0.65** under source-disjoint evaluation — the empirical reference for why current skill-scanning is unreliable.
- [CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing Skills](https://arxiv.org/abs/2608.16246) — the reference for why per-skill certification of agent marketplaces is structurally insufficient: composition risk is a *path*-level property, so a skill that passes its own scanner still forms a harmful chain — up to 80.6% Chain-Formation-Rate while scanners block only a fraction.
- [Beyond Direct Access: Resource Hijacking in LLM Agents](https://arxiv.org/abs/2608.15108) — the clean statement of an overlooked agent attack surface: attackers needn't steal a resource or its credentials, only induce the agent to invoke/consume/transfer the high-value resources it already reaches. ResourceHijackBench: OpenClaw 84% avg ASR, strongest defense still 55%.
- [MazeRunner: Nonlinear Task & Clue Orchestration for LLM-driven Black-Box Automated Pentesting](https://arxiv.org/abs/2608.14216) — how much *structure* the autonomous-pentest frontier still needs: a three-agent design with persistent state completes 47.7% of HackTheBox subtasks (vs 36.2% PentestGPT-V2, 34.2% Claude Code) and reaches root where same-model baselines never do.
- [Finding Vulnerabilities via LLM-Augmented Semantics-Aware Type-Checking (SETYPE)](https://arxiv.org/abs/2608.14533) — the clean reference for LLM-as-static-analyzer that finds **real** bugs: PYSETYPE hits 87%/88% precision/accuracy on real Python web apps and surfaced 15 potential zero-days, **nine confirmed by developers**.
- [ATOBench: How Autonomous Pentest Agents Verify Vulnerabilities When Target Evidence Lies](https://arxiv.org/abs/2608.12996) — the reference for a blind spot in every autonomous-pentest agent: because its next action, stop decision, and final claim all rest on target responses, a *deceptive* response can silently redirect both attack and verification.
- [SRE-Bench: A Realistic, Contamination-Free Reverse Engineering Benchmark](https://arxiv.org/abs/2608.11469) — the rigorous testbed on the limits of AI for offensive binary analysis: 19 private, real-world-scale programs → 1,572 graded tasks. The strongest of five frontier LLMs scores only 61.4% — source-code security capability does **not** transfer to binaries.
- [MarkNull: Model-Agnostic Watermark Removal in AI-Generated Images](https://arxiv.org/abs/2608.10166) — the USENIX-2026 anchor for why AI-image provenance/watermarking is not yet a reliable integrity control: on-manifold latent decorrelation drops watermark bit-accuracy to ~53% with no visible degradation, defeats Google SynthID-Image, and transfers to video.
- [Stealing Reasoning Traces from Proprietary LLM APIs](https://arxiv.org/abs/2608.09867) — why client-side encrypted chain-of-thought does not protect reasoning IP: the encrypted CoT blocks are interchangeable across sessions/users/models within one provider, so injecting a foreign trace becomes a scalable decryption jailbreak.

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- Black Hat USA 34 retrospectives frame **AI-agent offense** as the dominant 2026 theme (~29% of briefings AI-security-relevant) — "prompt injection as a curiosity → agent exploitation as a discipline" ([HN newest](https://news.ycombinator.com/newest)).
- The **OWASP Agentic Skills Top 10** release is circulating as the community consolidates on a shared vocabulary for agent-skill risk (malicious skills, supply-chain, over-privilege, poor scanning).
- The major-lab **"autonomous / near-autonomous AI agents act in a real intrusion"** cluster continues, on top of the [UK AISI incident report](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) already tracked.
- A recurring **prompt-injection-defense tradeoff** debate (deterministic blocking vs. false-positive cost) rather than a new attack primary.
- Model hubs keep churning out **abliterated/uncensored** open-weight models and fresh prompt-injection datasets — a steady leading indicator for the refusal-direction / jailbreak axis.

---

[TRENDS.md](TRENDS.md) · [watchlist (27)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-08-25](reports/2026-08-25.md) · [weekly: 2026-W34](reports/weekly/2026-W34.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
