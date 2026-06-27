# AI Radar

![trends](https://img.shields.io/badge/trends-4-3266ad?style=flat-square) ![accelerating](https://img.shields.io/badge/accelerating-2-e8590c?style=flat-square) ![watchlist](https://img.shields.io/badge/watchlist-19-6c757d?style=flat-square) ![updated](https://img.shields.io/badge/updated-2026--06--27-2f9e44?style=flat-square)

Autonomous tracker of the **offensive AI-security frontier** — AI for offense and attacks against AI — for a security researcher; generated from [TRENDS.md](TRENDS.md).

**Since last scan (2026-06-26):**
- 🌱 **New seed trend** [`adversarial-trigger-backdoor-004`](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types): 4 independent groups (diffusion models ×2, sensor/IoT, federated learning) on backdoor trigger implantation promoted from queue at weekly W26.
- 🗑 **Queue housekeeping**: 4 items promoted to trend-004; 2 dropped (NVIDIA article text unreachable, jqwik: no primary after 5+ attempts); 3 new intakes — CVE-2026-48529 GitHub MCP Server (CVSS 6.0), [Mythos classified-systems](TRENDS.md#observation_queue) and [US restriction signal](TRENDS.md#observation_queue).
- 📡 **Field-shaking pulse**: US government reportedly restricting GPT-5.6 Sol and Anthropic Mythos on offensive-capability grounds (~1315 HN pts combined); Mythos reportedly found vulnerabilities in classified US systems (AP News, ~850 pts) — both primary sources paywalled/not found; [queued unverified](TRENDS.md#observation_queue).

---

## Trends

🌱 1 · 📈 1 · 🚀 2 · 🌊 0 · 🏔 0 · 📉 0 · 💤 0

| trend | stage | latest signal |
|---|---|---|
| [Attacks on LLM-agent stack: MCP, skills, supply chain](TRENDS.md#id-agentic-attack-surface-001-attacks-on-the-llm-agent-stack-prompt-injectionrce-malicious-skills-agent-supply-chain) | 🚀 accelerating | [2026-06-25](https://embracethered.com/blog/posts/2026/toctou-agent-what-you-click-is-not-what-you-get/) |
| [LLM/agentic vuln discovery, repair & AI-written code](TRENDS.md#id-ai-vuln-discovery-002-llmagentic-vulnerability-discovery-repair--the-insecurity-of-ai-written-code) | 🚀 accelerating | [2026-06-25](https://arxiv.org/abs/2606.26933) |
| [AI-security tooling unreliable: scanners, guards, judges](TRENDS.md#id-ai-defense-tooling-unreliable-003-the-ai-security-tooling-layer-itself-is-unreliableattackable-skill-scanners-prompt-injection-detectors--jailbreak-judges-fail-under-attack) | 📈 emerging | [2026-06-25](https://arxiv.org/abs/2606.27091) |
| [Adversarial trigger implantation & backdoor attacks](TRENDS.md#id-adversarial-trigger-backdoor-004-adversarial-trigger-implantation-and-backdoor-attacks-across-ml-model-types) | 🌱 seed | [2026-06-24](https://arxiv.org/abs/2606.25858) |

---

## Worth studying

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

- US government reportedly restricting Mythos and GPT-5.6 Sol on offensive-capability grounds (~1315 HN pts, 2026-06-26); [queued unverified](TRENDS.md#observation_queue).
- Anthropic Mythos reportedly found vulnerabilities in classified US systems during red-team testing (~850 HN pts, AP News 2026-06-26); [queued unverified](TRENDS.md#observation_queue).
- Embrace The Red TOCTOU race-condition attack on computer-use agents demoed at Real-World AI Security conference (06-25) — captured as [primary evidence in agentic-attack-surface-001](https://embracethered.com/blog/posts/2026/toctou-agent-what-you-click-is-not-what-you-get/).
- Anthropic↔Alibaba model-extraction claim (~247 HN pts); [queued unverified](TRENDS.md#observation_queue).

---

[TRENDS.md](TRENDS.md) · [watchlist (19)](TRENDS.md#observation_queue) · [reports/](reports/) · [latest daily: 2026-06-26](reports/2026-06-26.md) · [weekly: 2026-W26](reports/weekly/2026-W26.md) · [AGENTS.md](AGENTS.md) · [SOURCES.md](SOURCES.md)
