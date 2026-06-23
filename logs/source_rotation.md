# source_rotation — AI Security Radar coverage log

Append-only daily log of which sources were covered on which dates. Daily runs APPEND
one dated line here and read only the recent tail (last ~7 days). Never edit or reorder
past lines. Each entry names every swept source as opened or `degraded: <reason>`.
