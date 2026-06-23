# Trend ledger — AI Security Radar

Last updated: 2026-06-23

Stage legend: `seed` (first signal) → `emerging` (multi-source, forming) →
`accelerating` (broad, fast) → `mainstreaming` (standard practice) ; `dormant`
(21+ days quiet) ; `declining` (the field moved on). Confidence: `low | medium | high`.
Trend bar: ≥3 independent sources (different orgs/author groups) + ≥1 concrete artifact.

## Active trends

_No trends yet — this is a fresh radar. Trends are seeded from the daily scan as
evidence accumulates (≥3 independent sources + an artifact). Single strong tools or
papers land on the `study_shelf` or `observation_queue` until they clear the bar._

## observation_queue

Signals not yet promoted to a trend. Format: `date — description — link if available`
(marked unverified unless the primary was opened this session).

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

## calibration

Append-only self-evaluation log MOVED to `logs/calibration.md` (see the `radar-self-eval`
skill). Weekly runs APPEND there, never here.
