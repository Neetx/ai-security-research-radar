# Trend ledger — AI Security Radar

Last updated: 2026-06-25

Stage legend: `seed` (first signal) → `emerging` (multi-source, forming) →
`accelerating` (broad, fast) → `mainstreaming` (standard practice) ; `dormant`
(21+ days quiet) ; `declining` (the field moved on). Confidence: `low | medium | high`.
Trend bar: ≥3 independent sources (different orgs/author groups) + ≥1 concrete artifact.

## Active trends

### [id: agentic-attack-surface-001] Attacks on the LLM-agent stack: prompt-injection→RCE, malicious skills, agent supply chain
alias: agent-attack-surface, agentic-security, mcp-attacks
stage: accelerating
confidence: high
first_observed: 2026-06-23
last_evidence: 2026-06-24
evidence:
  - 2026-06-23 — https://arxiv.org/abs/2606.24322 — "Securing LLM-Agent Long-Term Memory Against Poisoning" (TMA-NM): memory-poisoning attack on agents — an adversary launders an untrusted origin through the agent's own summarization, a trusted-tool echo, and manufactured corroboration; up to 68% laundering attack-success across 8 frontier models (proves content/lineage defenses are malleable).
  - 2026-06-23 — https://arxiv.org/abs/2606.24402 — "Poisoned Playbooks": a single crafted poisoned write-up injected into public-style security-knowledge sources systematically alters RAG-based AI security agents' exploit behavior across 11 CTF challenges, 11 real CVEs and 3 frontier LLM families — knowledge-poisoning of action-taking agents.
  - 2026-06-18 — https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/ — Microsoft: "AutoJack" exploit chain — untrusted web page rendered by a browsing agent reaches AutoGen Studio's local MCP WebSocket and spawns arbitrary processes on the host (confused-deputy across the localhost trust boundary).
  - 2026-06-22 — https://arxiv.org/abs/2606.23416 — "Detecting Malicious Agent Skills in the Wild": third-party file-based agent skills run with the user's privileges; a single malicious skill can exfiltrate data — attack surface of skill marketplaces.
  - 2026-06-22 — https://arxiv.org/abs/2606.23075 — "Safety in Self-Evolving LLM Agent Systems": agents that update their own params/memory/tools let adversarial influence become permanently encoded and self-amplify across updates.
  - 2026-06-21 — https://arxiv.org/abs/2606.22504 — "Lingering Authority": coding agents keep over-broad tool capabilities after the subgoal that justified them, expanding the agent attack surface.
  - 2026-06-20 — https://arxiv.org/abs/2606.21842 — "Agent-Assisted Side-Channel Attacks on Non-Prefix KV Cache in RAG": cross-tenant side channel in modern RAG/KV-cache-fusion serving engines.
  - 2026-06-17 — https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/ — Microsoft: npm supply-chain compromise of the Mastra AI-agent framework (Sapphire Sleet) — postinstall payload in the agent toolchain.
  - 2026-06-11 — https://nvd.nist.gov/vuln/detail/CVE-2026-46519 — CVE-2026-46519 (CVSS 8.8 HIGH): mcp-server-kubernetes' documented tool-restriction env vars (ALLOW_ONLY_READONLY_TOOLS etc.) do not actually gate destructive tools — broken MCP capability controls. One of 27 MCP-related CVEs published in NVD in June 2026, signalling MCP server implementations as a fast-growing CVE surface.
  - 2026-06-24 — https://arxiv.org/abs/2606.26028 — "Can Trustless Agents Be Trusted?": first empirical study of the ERC-8004 permissionless trust layer for AI-agent economies (on-chain Identity/Reputation/Validation registries across Ethereum, BSC and Base) — finds the recorded trust signals are not a reliable basis for agent-to-agent decisions, exposing the agent-economy trust infrastructure itself as a new attack surface.
notes: Created emerging on day one — six independent groups (Microsoft x2, NVIDIA, multiple arXiv author groups) converging on the agent/MCP/skills attack surface in the same week clears the trend bar. 2026-06-23 (Pass 2): added a concrete advisory artifact (CVE-2026-46519, mcp-server-kubernetes, CVSS 8.8) plus the volume signal of 27 MCP CVEs in June; confidence held at medium pending breadth. Watch for promotion to accelerating if the cadence holds. NVIDIA "Mitigating Indirect AGENTS.md Injection" (2026-04-20) is a related earlier signal held in the queue. 2026-06-24: cadence held into day 2 — added two more independent groups attacking the agent stack, now via knowledge/memory POISONING (TMA-NM memory-laundering 68% ASR; Poisoned Playbooks RAG-poisoning of security agents). NVD shows 12 fresh MCP-server CVEs in the last 10 days alone (OpenClaw, Windows-MCP, MCP-Toolbox auth-bypass, litellm, etc.) — the MCP CVE surface keeps widening. Breadth now spans RCE, supply chain, skills, self-evolving agents, lingering authority, KV side-channel, MCP CVEs, memory poisoning and RAG poisoning: ACCELERATING is the likely next stage move — held one more pass for calibration (trend is only on day 2). 2026-06-25: PROMOTED emerging→accelerating (confidence medium→high). Cadence held a third day: +ERC-8004 trustless-agent-economy attack surface (2606.26028), plus sustained MCP-server CVE volume (13 in the last 10 days incl. Flowise Custom-MCP OS-command-injection CVE-2026-56274, Jenkins MCP-plugin CVE-2026-57300, Apache Doris MCP SQLi, foreman-mcp). Breadth now spans RCE, supply chain, skills, self-evolving agents, lingering authority, KV side-channel, the standing MCP-CVE surface, memory/RAG poisoning and the agent-economy trust layer across Microsoft, NVIDIA and many independent groups — broad + fast = accelerating. Evidence at the 10-item cap; rotate oldest on next append.

### [id: ai-vuln-discovery-002] LLM/agentic vulnerability discovery, repair & the (in)security of AI-written code
alias: ai-vuln-discovery, llm-vuln-finding, autonomous-pentest, vibe-coding-security
stage: accelerating
confidence: high
first_observed: 2026-06-23
last_evidence: 2026-06-24
evidence:
  - 2026-06-22 — https://openai.com/index/daybreak-securing-the-world — OpenAI "Daybreak": frontier models navigate large codebases, reason through attack paths, validate hypotheses and surface vulns; frames AI as having "changed the physics" of vuln discovery (bottleneck now patching, not finding).
  - 2026-05-22 — https://www.anthropic.com/research/exploit-evals — Anthropic FRT "Measuring LLMs' ability to develop exploits": Claude Mythos Preview is a step-change — it turns vulnerabilities into exploit primitives and chains them into full end-to-end exploits on the world's most widely-used software; benchmarked on 12 post-cutoff exploits (DefiHackLabs smart contracts, dollar-valued). Open-sources the SCONE-bench harness + dataset. (Opened 2026-06-24; previously a queue watch.)
  - 2026-06-08 — https://www.anthropic.com/research/n-days — Anthropic Frontier Red Team "Measuring LLMs' impact on N-day exploits": frontier models turn public PoCs into working exploits for 21 post-cutoff Windows kernel LPE bugs (mechanically graded via whoami), measuring end-to-end exploit time — a second frontier lab quantifying offensive exploit-development capability.
  - 2026-06-22 — https://arxiv.org/abs/2606.23130 — "Understanding the (In)Security of Vibe-Coded Applications": systematic insecurity of apps built primarily via natural-language interaction with AI coding agents.
  - 2026-06-21 — https://arxiv.org/abs/2606.22647 — "RAVEN: Agentic RAG for Automated Vulnerability Repair": LLM-agent pipeline for repairing software vulnerabilities at scale.
  - 2026-06-20 — https://arxiv.org/abs/2606.22263 — "Revelio": cost-efficient agentic memory-safety vulnerability detection at repository scale.
  - 2026-06-19 — https://arxiv.org/abs/2606.21397 — "Evaluating LLMs for Real-World Web Vulnerability Detection": benchmarks six frontier models (incl. Claude Opus 4.6, Codex) on web-specific vuln finding.
  - 2026-06-24 — https://arxiv.org/abs/2606.25332 — "Decoupling Reconnaissance and Exploitation": a two-stage decoupled evaluation (ground-truth injection + knowledge-driven ablation across 70 high-fidelity web-vuln testbeds) that isolates exploit-execution from reconnaissance noise — measures the true capability boundaries of five open-source LLM penetration-testing agents and shows early-recon failure masks an agent's real exploitation ability.
  - 2026-06-24 — https://arxiv.org/abs/2606.25356 — "Representation Matters" (RepBench): empirical benchmark showing the program representation fed to the model (raw source vs AST/CFG/PDG and combinations) materially changes LLM vulnerability-reasoning accuracy on real C/C++ testcases — how you represent code, not just which model, drives LLM vuln-finding.
notes: Confidence raised medium→high on 2026-06-23 (Pass 2): two independent frontier labs (OpenAI Daybreak + Anthropic Frontier Red Team N-days) now quantify offensive vuln-discovery/exploit-development capability, alongside five independent arXiv groups in the same week, all on LLM/agentic vuln finding, exploitation & repair. Stage held at emerging (created today). Dual-use: same capability that "turbocharges defenders" is offensive vuln discovery. Anthropic also lists "Measuring LLMs' ability to develop exploits" (2026-05-22) and an LLM ATT&CK Navigator (2026-06-03) — held in queue (index seen, not individually opened). Trail of Bits "Patch the Planet" (2026-06-22) corroborates the AI-patching push but is a partner of Daybreak (not independent), so held as context. 2026-06-24: opened the queued Anthropic FRT "exploit-evals" (2026-05-22) and added it as evidence — a concrete open-source offensive benchmark (SCONE-bench) plus the "Mythos Preview" step-change claim that end-to-end exploit development is becoming commoditized in 6–12 months. The companion FRT "LLM ATT&CK Navigator" (2026-06-03) — real-world data on 832 actors misusing models, 69% on ATT&CK T1587 Develop-Capabilities — went to study_shelf (threat-intel/taxonomy artifact, not vuln-discovery per se). Stage held emerging (day 2); confidence remains high. 2026-06-25: PROMOTED emerging→accelerating. The base is now both broad (two frontier labs — OpenAI Daybreak + Anthropic FRT — plus ≥7 independent arXiv groups) and fast (new independent evidence every pass): today +LLM web-pentest capability-boundary measurement (2606.25332) and +RepBench program-representation effect on LLM vuln reasoning (2606.25356). Corroborating but NOT independent: Trail of Bits "Patch the Planet" first-week results (hundreds of bugs, 64 PRs, 51 issues across 19 projects via GPT-5.5-Cyber) — a Daybreak partner, so held as reinforcement of the OpenAI evidence line, not a separate source. Evidence at the 10-item cap; rotate oldest on next append. Also queued a SoK on AI secure-code-generation to study_shelf.

### [id: ai-defense-tooling-unreliable-003] The AI-security tooling layer itself is unreliable/attackable: skill scanners, prompt-injection detectors & jailbreak judges fail under attack
alias: ai-security-tooling-failure, guard-reliability, eval-reliability
stage: seed
confidence: medium
first_observed: 2026-06-25
last_evidence: 2026-06-24
evidence:
  - 2026-06-03 — https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/ — Trail of Bits tested the new family of "skill scanners" meant to catch malicious agent skills before install — they don't work; the trust model is broken at the root (arbitrary code+data+NL is the broadest possible attack surface, inference cost forces weak/truncated models, and the same instruction is benign or malicious depending on environment). Releases trailofbits/overtly-malicious-skills.
  - 2026-06-22 — https://arxiv.org/abs/2606.22659 — "Confidently Wrong": three released prompt-injection detectors (ProtectAI-v2 and two Prompt-Guard-2 checkpoints) become severely mis-calibrated at a frozen source-calibrated threshold when the attack distribution shifts off the clean benchmark — the guard stays confident while wrong (severity-aware calibration metric across five shifts).
  - 2026-06-24 — https://arxiv.org/abs/2606.25487 — "How Reliable Is Your Jailbreak Judge?": the automated ASR judges nearly every jailbreak/prompt-injection paper relies on are rarely checked; against 596 human-labeled HarmBench completions the dedicated classifier over-flags (recall 0.974, precision 0.835) while LLM-as-judge recall is erratic (0.06–0.65) and the judges are themselves attackable — the field's measurement layer is unreliable.
notes: Seeded 2026-06-25 from a 3-independent-group queue cluster (Trail of Bits + two arXiv author groups) on an explicit scope axis ("attacks on AI-security standards/tooling"). Coherent theme: the detection and evaluation tools the ecosystem leans on — skill scanners, prompt-injection guards, and jailbreak ASR judges — all fail under adversarial/distribution shift, so both deployed defenses and reported attack-success numbers rest on unverified tooling. Pulled 2606.22659 and 2606.25487 out of observation_queue to seed this. Watch for a 4th independent group and for work that ACTIVELY attacks these guards (not just measures miscalibration) to justify emerging.

## observation_queue

Signals not yet promoted to a trend. Format: `date — description — link if available`
(marked unverified unless the primary was opened this session).

- 2026-06-21 — Jailbreak via refusal-direction steering: refusal shown to be a manipulable linear feature in safety-aligned LLMs (activation/steering-vector attack) — https://arxiv.org/abs/2606.22686 [verified, opened] — also on study_shelf; nucleus of a possible jailbreak/steering trend.
- 2026-06-21 — Network censorship/traffic evasion via generative diffusion models (one-prompt) — https://arxiv.org/abs/2606.22717 [verified, opened] — censorship-circumvention axis.
- 2026-06-22 — Data poisoning / backdoors in diffusion models at ultra-low poison rate with imperceptible trigger ("TooBad") — https://arxiv.org/abs/2606.23362 [verified, opened] — poisoning/backdoor axis.
- 2026-06-19 — Open-weight models separating public vs private capabilities (capability-gating / uncensoring relevance) — https://arxiv.org/abs/2606.21638 [verified, abstract opened 2026-06-23].
- 2026-06-22 — White-box model inversion: anyone holding an intermediate latent can invert public diffusion checkpoints to reconstruct the original input image ("Key-Controlled Inversion") — model-inversion/reconstruction axis — https://arxiv.org/abs/2606.22988 [verified, abstract opened].
- 2026-06-22 — Oracle-level integrity attacks on imagine-then-act VLA/world-action models: the "trusted imagination" latent is the exposed surface, defeating downstream safety gates — agent/embodied attack surface — https://arxiv.org/abs/2606.22966 [verified, abstract opened].
- 2026-06-22 — "Illusion of Erasure": knowledge-editing/unlearning in LLMs does not fully erase facts; edited knowledge resurfaces under adversarial elicitation — unlearning/uncensoring axis — https://arxiv.org/abs/2606.23276 [verified, abstract opened].
- 2026-06-22 — CLIP-guided diffusion backdoor generation in sensor-based HAR — adds a 2nd independent group to the poisoning/backdoor cluster (with TooBad 2606.23362); below the ≥3 promotion bar for now — https://arxiv.org/abs/2606.22837 [verified, abstract opened].
- 2026-06-23 — "Red-Teaming the Agentic Red-Team": as agentic offensive-security systems become commoditized, the SECURITY of those offensive agents themselves is understudied — attack surface of the red-team agent — https://arxiv.org/abs/2606.24496 [verified, abstract opened] — straddles agentic-attack-surface-001 and ai-vuln-discovery-002; watch for a 2nd/3rd group on "attacking the offensive agent".
- 2026-06-23 — PixJail: self-evolving paper-to-pipeline agent that reproduces T2I (text-to-image) jailbreak methods at the pipeline level (prompt-transform → generate → filter → judge); recovers 11 prior attacks at ~2.1% error — jailbreak-eval tooling — https://arxiv.org/abs/2606.24081 [verified, abstract opened].
- 2026-06-18 — (off-axis) Anthropic FRT "Project Fetch: Phase two" — whether LLMs uplift non-experts operating a robot dog (autonomous/embodied systems, not cyber); noted for completeness, off the offensive AI-security cyber axis — https://www.anthropic.com/research/project-fetch-phase-two [verified, opened].
- 2026-04-20 — NVIDIA: mitigating indirect AGENTS.md injection attacks in agentic environments — https://developer.nvidia.com/blog/ [verified via feed] — earlier signal feeding agentic-attack-surface-001.
- 2026-06-24 — Federated-learning backdoor where ONLY the trigger color is varied (semantic accessories — masks/sunglasses, black vs white) materially changes attack success — adds a 3rd independent group to the visual-trigger poisoning/backdoor cluster (with TooBad 2606.23362 diffusion, CLIP-HAR 2606.22837 sensor-HAR) — https://arxiv.org/abs/2606.25858 [verified, opened]. Cluster now 3 groups but heterogeneous (diffusion / sensor-HAR / federated); seed candidate only if a 4th tightens the threat model.
- 2026-06-24 — TRACE: lightweight detection of RAG corpus-poisoning via token-influence attribution (recurrent high-influence keywords, secondary verification) — defense on the RAG/agent-knowledge-poisoning axis (cf. agentic-attack-surface-001) — https://arxiv.org/abs/2606.25721 [verified, opened].
- 2026-06-24 — "Unfireable Safety Kernel": argues in-runtime agent guardrails (system prompts, output filters, guardrail libraries) are reachable by inputs that influence the agent ("escapable AI systems") and proposes out-of-process, fail-closed, pre-action authorization — defense framing of the agent attack surface — https://arxiv.org/abs/2606.26057 [verified, opened].
- 2026-06-24 — (intake/HN, unverified) Anthropic statement that Alibaba "illicitly extracted Claude model capabilities" (HN front page, 247 pts) — model-extraction/distillation signal on the offense-against-AI axis; find Anthropic's primary statement/disclosure before any promotion.
- 2026-06-20 — (intake/HN, unverified) "Show HN: post-trained a model that pen tests instead of refusing" (argusred.com/cli) — offensive-model claim; checked 2026-06-25, source is a commercial product page, no published research artifact → stays intake, not promotable.
- 2026-06-22 — (intake/HN, unverified) "Prompt Injection as Role Confusion" — high-engagement community framing of prompt-injection; chase to a primary.
- 2026-05-29 — (intake/HN, unverified) jqwik dependency shipped hidden instructions telling AI coding agents to delete data — agent supply-chain/injection signal; verify the disclosure.

## source_rotation

Append-only coverage log MOVED to `logs/source_rotation.md` (it grows ~1 KB/day;
inlining it bloats this ledger). Each run APPENDS one dated line THERE and reads only
the recent tail (~7 days) to decide coverage — do not write scans into TRENDS.md.

## strategy_notes

Corrections to the source-coverage strategy.
- 2026-06-23 — Scope (curator input): track the OFFENSIVE AI-security frontier on two
  fronts — (A) AI FOR OFFENSE: LLM red-team / autonomous pentest & exploitation agents,
  AI vuln discovery (LLM fuzzing, SAST→exploit, reversing), AI recon/social-eng/phishing
  research, AI malware/evasion research, offensive-agent benchmarks; (B) OFFENSE AGAINST
  AI: jailbreaking & guardrail bypass, direct/indirect prompt injection, steering/
  activation-vector attacks, censorship/alignment circumvention, data poisoning &
  backdoors, model extraction/inversion/membership inference, attacks on agents/MCP/
  tool-use/skills & supply chain, attacks on AI-security standards/tooling. The agent
  owns and evolves these axes; promote a forming sub-theme to a trend at ≥3 independent
  groups + an artifact.

## study_shelf

Single strong tools / papers / techniques worth knowing, newest first
(format: `date — [name](url) — one line of why`). The trend bar does NOT apply here;
opened primary sources only.

- 2026-06-24 — [SoK: AI Secure Code Generation (Patir, Guo, Cai, Hu)](https://arxiv.org/abs/2606.25195) — systematizes what today's models and coding agents can and cannot do for secure code via a three-level framework (natural-language understanding of secure-coding principles → secure generation → agentic workflows), mapping where prompting / fine-tuning / RL / agentic methods actually help and why substantial security failures persist — the reference map for the "(in)security of AI-written code" problem.
- 2026-06-03 — [Mapping AI-enabled cyber threats: the LLM ATT&CK Navigator (Anthropic FRT)](https://www.anthropic.com/research/attack-navigator) — empirical mapping of 832 real threat actors observed misusing models onto MITRE ATT&CK: 69% used T1587 (Develop Capabilities), 560 on T1587.001 (Malware Development) — the in-the-wild ground truth behind the "AI for offense" axis, plus Anthropic's CVP/Glasswing safeguard framing.
- 2026-05-22 — [Measuring LLMs' ability to develop exploits (Anthropic FRT)](https://www.anthropic.com/research/exploit-evals) — introduces SCONE-bench (open-sourced harness + dataset) and shows "Mythos Preview" building full end-to-end exploits on widely-used software from primitives — the capability-trajectory companion to the N-days weaponization work.
- 2026-06-08 — [Measuring LLMs' impact on N-day exploits (Anthropic FRT)](https://www.anthropic.com/research/n-days) — concrete methodology and results for frontier models turning public PoCs into working N-day exploits (21 Windows kernel LPE bugs, mechanically graded) — the offensive counterpart to the "find the bug" literature: weaponizing already-disclosed CVEs at machine speed.
- 2026-06-21 — [The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs](https://arxiv.org/abs/2606.22686) — argues refusal is a manipulable linear feature, not a deep semantic decision: the mechanistic basis behind refusal-direction / steering-vector jailbreaks.
- 2026-06-18 — [AutoJack (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/) — canonical confused-deputy chain: a single attacker web page drives a browsing agent across the localhost boundary into AutoGen Studio's MCP control plane and gets host RCE.

## calibration

Append-only self-evaluation log MOVED to `logs/calibration.md` (see the `radar-self-eval`
skill). Weekly runs APPEND there, never here.
