# AI Radar

![trends](https://img.shields.io/badge/trends-4-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-2-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-21-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--06--29-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-06-27):**
- 🛒 **In-the-wild malicious agent skills**: Palo Alto Unit 42 found 5 evasive skills on OpenClaw's ClawHub marketplace bypassing VirusTotal + ClawScan — infostealers with live C2 plus novel agentic-fraud techniques — first vendor confirmation of the malicious-skill-marketplace threat; added to [`agentic-attack-surface-001`](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain).
- 🧬 **Backdoor cluster grows to 5 groups**: a data-free [federated-LLM-QA backdoor](https://arxiv.org/abs/2606.27511) (malicious aggregator recovers samples from client gradients, ~100% ASR) extends [`adversarial-trigger-backdoor-004`](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) to federated LLMs.
- 📚 **Study shelf**: a proof that [perfect prompt-injection prevention is mathematically impossible](https://arxiv.org/abs/2606.27567) in shared-embedding models — the theory behind "every PI defense gets broken."
- 📡 **Source coverage**: Unit 42 promoted candidate→swept (W27 priority); GTIG feed degraded, Protect AI blog stale. Queue +2 intakes ([mechanistic jailbreak](https://arxiv.org/abs/2606.28153), [agentic re-identification](https://arxiv.org/abs/2606.27936)).

---

## Trends

🌱 1 · 📈 1 · 🚀 2 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-06-25](https://arxiv.org/abs/2606.27027) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-06-25](https://arxiv.org/abs/2606.26933) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-06-25](https://arxiv.org/abs/2606.27091) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🌱 seed | [2026-06-25](https://arxiv.org/abs/2606.27511) |

---

## Worth studying

- [On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models](https://arxiv.org/abs/2606.27567) — proves perfect prompt-injection prevention is mathematically impossible in shared-embedding architectures (provenance-recovery impossibility + control-path exposure + finite-coverage invariance gap) — the theoretical why behind "every PI defense gets broken."
- [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents](https://arxiv.org/abs/2606.26479) — organizes the 2024–2026 out-of-band agent defenses (CaMeL, FIDES, Progent, RTBAS, FORGE) as Biba integrity / reference-monitor instances and stress-tests them with adaptive attacks — the reference map for "enforce security outside the model."
- [SoK: AI Secure Code Generation](https://arxiv.org/abs/2606.25195) — three-level framework mapping where prompting / fine-tuning / RL / agentic methods help secure-code generation and why substantial failures persist — the map for the "(in)security of AI-written code" problem.
- [The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs](https://arxiv.org/abs/2606.22686) — refusal is a manipulable linear feature, not a deep semantic decision: the mechanistic basis behind refusal-direction / steering-vector jailbreaks.
- [AutoJack (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/) — canonical confused-deputy chain: one attacker web page drives a browsing agent across the localhost boundary into AutoGen Studio's MCP control plane and gets host RCE.
- [Measuring LLMs' impact on N-day exploits (Anthropic FRT)](https://www.anthropic.com/research/n-days) — frontier models turning public PoCs into working N-day exploits for 21 Windows kernel LPE bugs — weaponizing already-disclosed CVEs at machine speed.
- [Mapping AI-enabled cyber threats: the LLM ATT&CK Navigator (Anthropic FRT)](https://www.anthropic.com/research/attack-navigator) — 832 real actors mapped to MITRE ATT&CK: 69% on T1587 Develop-Capabilities — in-the-wild ground truth for the AI-for-offense axis.
- [Measuring LLMs' ability to develop exploits (Anthropic FRT)](https://www.anthropic.com/research/exploit-evals) — SCONE-bench (open-sourced) + "Mythos Preview" chains exploit primitives into full end-to-end exploits on widely-used software.

---

## Community pulse

_Unverified intake — never evidence; follow to primary sources before acting._

- Quiet scan (2026-06-29) — no new community earthquake; the Mythos / GPT-5.6 Sol restriction signals from 06-26 are still circulating but off the HN front page.
- US government reportedly restricting Mythos and GPT-5.6 Sol on offensive-capability grounds (~1315 HN pts, 2026-06-26); [queued unverified](TRENDS.md#observation_queue).
- Anthropic Mythos reportedly found vulnerabilities in classified US systems during red-team testing (~850 HN pts, AP News 2026-06-26); [queued unverified](TRENDS.md#observation_queue).

---

[TRENDS.md](TRENDS.md) · [watchlist (21)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-06-29](reports/2026-06-29.md) · [weekly: 2026-W26](reports/weekly/2026-W26.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
