# Trend ledger — AI Security Radar

Last updated: 2026-06-23

Stage legend: `seed` (first signal) → `emerging` (multi-source, forming) →
`accelerating` (broad, fast) → `mainstreaming` (standard practice) ; `dormant`
(21+ days quiet) ; `declining` (the field moved on). Confidence: `low | medium | high`.
Trend bar: ≥3 independent sources (different orgs/author groups) + ≥1 concrete artifact.

## Active trends

### [id: agentic-attack-surface-001] Attacks on the LLM-agent stack: prompt-injection→RCE, malicious skills, agent supply chain
alias: agent-attack-surface, agentic-security, mcp-attacks
stage: emerging
confidence: medium
first_observed: 2026-06-23
last_evidence: 2026-06-22
evidence:
  - 2026-06-18 — https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/ — Microsoft: "AutoJack" exploit chain — untrusted web page rendered by a browsing agent reaches AutoGen Studio's local MCP WebSocket and spawns arbitrary processes on the host (confused-deputy across the localhost trust boundary).
  - 2026-06-22 — https://arxiv.org/abs/2606.23416 — "Detecting Malicious Agent Skills in the Wild": third-party file-based agent skills run with the user's privileges; a single malicious skill can exfiltrate data — attack surface of skill marketplaces.
  - 2026-06-22 — https://arxiv.org/abs/2606.23075 — "Safety in Self-Evolving LLM Agent Systems": agents that update their own params/memory/tools let adversarial influence become permanently encoded and self-amplify across updates.
  - 2026-06-21 — https://arxiv.org/abs/2606.22504 — "Lingering Authority": coding agents keep over-broad tool capabilities after the subgoal that justified them, expanding the agent attack surface.
  - 2026-06-20 — https://arxiv.org/abs/2606.21842 — "Agent-Assisted Side-Channel Attacks on Non-Prefix KV Cache in RAG": cross-tenant side channel in modern RAG/KV-cache-fusion serving engines.
  - 2026-06-17 — https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/ — Microsoft: npm supply-chain compromise of the Mastra AI-agent framework (Sapphire Sleet) — postinstall payload in the agent toolchain.
  - 2026-06-11 — https://nvd.nist.gov/vuln/detail/CVE-2026-46519 — CVE-2026-46519 (CVSS 8.8 HIGH): mcp-server-kubernetes' documented tool-restriction env vars (ALLOW_ONLY_READONLY_TOOLS etc.) do not actually gate destructive tools — broken MCP capability controls. One of 27 MCP-related CVEs published in NVD in June 2026, signalling MCP server implementations as a fast-growing CVE surface.
notes: Created emerging on day one — six independent groups (Microsoft x2, NVIDIA, multiple arXiv author groups) converging on the agent/MCP/skills attack surface in the same week clears the trend bar. 2026-06-23 (Pass 2): added a concrete advisory artifact (CVE-2026-46519, mcp-server-kubernetes, CVSS 8.8) plus the volume signal of 27 MCP CVEs in June; confidence held at medium pending breadth. Watch for promotion to accelerating if the cadence holds. NVIDIA "Mitigating Indirect AGENTS.md Injection" (2026-04-20) is a related earlier signal held in the queue.

### [id: ai-vuln-discovery-002] LLM/agentic vulnerability discovery, repair & the (in)security of AI-written code
alias: ai-vuln-discovery, llm-vuln-finding, autonomous-pentest, vibe-coding-security
stage: emerging
confidence: high
first_observed: 2026-06-23
last_evidence: 2026-06-22
evidence:
  - 2026-06-22 — https://openai.com/index/daybreak-securing-the-world — OpenAI "Daybreak": frontier models navigate large codebases, reason through attack paths, validate hypotheses and surface vulns; frames AI as having "changed the physics" of vuln discovery (bottleneck now patching, not finding).
  - 2026-06-08 — https://www.anthropic.com/research/n-days — Anthropic Frontier Red Team "Measuring LLMs' impact on N-day exploits": frontier models turn public PoCs into working exploits for 21 post-cutoff Windows kernel LPE bugs (mechanically graded via whoami), measuring end-to-end exploit time — a second frontier lab quantifying offensive exploit-development capability.
  - 2026-06-22 — https://arxiv.org/abs/2606.23130 — "Understanding the (In)Security of Vibe-Coded Applications": systematic insecurity of apps built primarily via natural-language interaction with AI coding agents.
  - 2026-06-21 — https://arxiv.org/abs/2606.22647 — "RAVEN: Agentic RAG for Automated Vulnerability Repair": LLM-agent pipeline for repairing software vulnerabilities at scale.
  - 2026-06-20 — https://arxiv.org/abs/2606.22263 — "Revelio": cost-efficient agentic memory-safety vulnerability detection at repository scale.
  - 2026-06-19 — https://arxiv.org/abs/2606.21397 — "Evaluating LLMs for Real-World Web Vulnerability Detection": benchmarks six frontier models (incl. Claude Opus 4.6, Codex) on web-specific vuln finding.
  - 2026-06-22 — https://arxiv.org/abs/2606.23138 — "Rising From the Ashes: How Agentic AI is Unblocking Challenges in Cybersecurity": agentic AI clearing labor-intensive defensive bottlenecks (dual-use offensive capability).
notes: Confidence raised medium→high on 2026-06-23 (Pass 2): two independent frontier labs (OpenAI Daybreak + Anthropic Frontier Red Team N-days) now quantify offensive vuln-discovery/exploit-development capability, alongside five independent arXiv groups in the same week, all on LLM/agentic vuln finding, exploitation & repair. Stage held at emerging (created today). Dual-use: same capability that "turbocharges defenders" is offensive vuln discovery. Anthropic also lists "Measuring LLMs' ability to develop exploits" (2026-05-22) and an LLM ATT&CK Navigator (2026-06-03) — held in queue (index seen, not individually opened). Trail of Bits "Patch the Planet" (2026-06-22) corroborates the AI-patching push but is a partner of Daybreak (not independent), so held as context.

## observation_queue

Signals not yet promoted to a trend. Format: `date — description — link if available`
(marked unverified unless the primary was opened this session).

- 2026-06-21 — Jailbreak via refusal-direction steering: refusal shown to be a manipulable linear feature in safety-aligned LLMs (activation/steering-vector attack) — https://arxiv.org/abs/2606.22686 [verified, opened] — also on study_shelf; nucleus of a possible jailbreak/steering trend.
- 2026-06-21 — Network censorship/traffic evasion via generative diffusion models (one-prompt) — https://arxiv.org/abs/2606.22717 [verified, opened] — censorship-circumvention axis.
- 2026-06-22 — Data poisoning / backdoors in diffusion models at ultra-low poison rate with imperceptible trigger ("TooBad") — https://arxiv.org/abs/2606.23362 [verified, opened] — poisoning/backdoor axis.
- 2026-06-19 — Open-weight models separating public vs private capabilities (capability-gating / uncensoring relevance) — https://arxiv.org/abs/2606.21638 [verified, abstract opened 2026-06-23].
- 2026-06-21 — Released prompt-injection DETECTORS (ProtectAI-v2, Prompt-Guard-2) become mis-calibrated / "confidently wrong" under attack-distribution shift — attack on AI-security tooling — https://arxiv.org/abs/2606.22659 [verified, abstract opened].
- 2026-06-22 — White-box model inversion: anyone holding an intermediate latent can invert public diffusion checkpoints to reconstruct the original input image ("Key-Controlled Inversion") — model-inversion/reconstruction axis — https://arxiv.org/abs/2606.22988 [verified, abstract opened].
- 2026-06-22 — Oracle-level integrity attacks on imagine-then-act VLA/world-action models: the "trusted imagination" latent is the exposed surface, defeating downstream safety gates — agent/embodied attack surface — https://arxiv.org/abs/2606.22966 [verified, abstract opened].
- 2026-06-22 — "Illusion of Erasure": knowledge-editing/unlearning in LLMs does not fully erase facts; edited knowledge resurfaces under adversarial elicitation — unlearning/uncensoring axis — https://arxiv.org/abs/2606.23276 [verified, abstract opened].
- 2026-06-22 — CLIP-guided diffusion backdoor generation in sensor-based HAR — adds a 2nd independent group to the poisoning/backdoor cluster (with TooBad 2606.23362); below the ≥3 promotion bar for now — https://arxiv.org/abs/2606.22837 [verified, abstract opened].
- 2026-06-08 — Anthropic Frontier Red Team offensive-capability series beyond N-days: "Measuring LLMs' ability to develop exploits" (2026-05-22) and "Mapping AI-enabled cyber threats / LLM ATT&CK Navigator" (2026-06-03) — https://www.anthropic.com/research [index seen 2026-06-23; individual articles not yet opened — verify before citing].
- 2026-04-20 — NVIDIA: mitigating indirect AGENTS.md injection attacks in agentic environments — https://developer.nvidia.com/blog/ [verified via feed] — earlier signal feeding agentic-attack-surface-001.
- 2026-06-20 — (intake/HN, unverified) "Show HN: post-trained a model that pen tests instead of refusing" — offensive-model claim; find the primary artifact before any promotion.
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

- 2026-06-08 — [Measuring LLMs' impact on N-day exploits (Anthropic FRT)](https://www.anthropic.com/research/n-days) — concrete methodology and results for frontier models turning public PoCs into working N-day exploits (21 Windows kernel LPE bugs, mechanically graded) — the offensive counterpart to the "find the bug" literature: weaponizing already-disclosed CVEs at machine speed.
- 2026-06-21 — [The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs](https://arxiv.org/abs/2606.22686) — argues refusal is a manipulable linear feature, not a deep semantic decision: the mechanistic basis behind refusal-direction / steering-vector jailbreaks.
- 2026-06-18 — [AutoJack (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/) — canonical confused-deputy chain: a single attacker web page drives a browsing agent across the localhost boundary into AutoGen Studio's MCP control plane and gets host RCE.

## calibration

Append-only self-evaluation log MOVED to `logs/calibration.md` (see the `radar-self-eval`
skill). Weekly runs APPEND there, never here.
