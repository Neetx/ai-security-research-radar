# calibration — AI Security Radar self-evaluation log

Append-only self-evaluation log (see the `radar-self-eval` skill). Weekly runs APPEND one
dated line here. Weekly line: `W<nn>: queue +a/→p/−d/stale s · evidence +e · moves m ·
exploration c/r · off-axis o/a · lag expl Xd / backfill Yd (Z%) · coverage <opened>/<listed>
(miss n, degr d) · routing-leak n`.

W26 (2026-06-27): queue +3/→6p/−2d/stale 0 · evidence +8 (001+4, 002+3, 003+1) · stage-moves 5 (001 emerging→accel, 002 emerging→accel, 003 seed→emerging, 003 seed created, 004 seed created) · exploration arXiv cs.CR only/5 days · off-axis 0 new seeds (backstop: social-eng/phishing and AI-malware axes forming but below bar) · lag: all evidence 0–4d from publication (no backfill needed) · coverage ~14/22 registered sources opened (miss: GTIG/ProtectAI/Unit42/Meta/NCC candidate lanes, Reddit, YouTube curators, OWASP/ATLAS change-check; degr: MSRC SPA, tldrsec 403, MLSecOps fail, NVIDIA article-URL blocked = 4 degraded) · routing-leak 0 (all named primaries either evidenced or queued; no primary left in prose-only). Notes: First week of operation — radar infrastructure built and validated. Coverage miss on candidate primary lanes (GTIG/ProtectAI/Unit42) is the top gap to close next week. Degraded source count (4) is high; heal workload identified. No anchoring flagged but 100% evidence concentration on existing 4 axes warrants active off-axis probing next week.
