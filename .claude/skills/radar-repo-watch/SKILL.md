---
name: radar-repo-watch
description: |
  Watch GitHub every daily run for behind-the-scenes movement — across watched REPOS (releases, merged PRs, hot issues), watched PROFILES/USERS (what a key author ships next), and FORK TREES (notable forks up to depth 3, scored by a notability metric). Releases and merges are citable artifacts; profile/issue/fork movement is a queue signal until it lands. Default to GitHub's public Atom feeds + Tavily; the REST API is optional. Use during the daily scan, after the lab sweep. Source lists live in SOURCES.md → "GitHub watch".
---

# GitHub watch — repos, profiles, and fork trees

In big projects, important changes show up as PR/issue/fork activity well before
the headline release. Watching repos, the people behind them, and their fork
trees surfaces that build-up early.

## How to fetch (feeds first, no auth, no rate-limit worries)

Prefer GitHub's public Atom feeds and plain pages — the same RSS pattern as the
lab sweep, readable via `tvly` with no API key and no rate limit:
- Releases: `https://github.com/<o>/<r>/releases.atom`
- Tags: `https://github.com/<o>/<r>/tags.atom`
- Commits on default branch: `https://github.com/<o>/<r>/commits.atom`
- A user's public activity: `https://github.com/<u>.atom`
- PR list / issues / a fork's page: extract the HTML via `tvly` (no feed exists).

The REST API (`api.github.com`) is OPTIONAL — use it only if it is reachable
and authenticated in this environment (it may not be: the network often routes
through Tavily only, and unauthenticated API is 60 req/hr). When available it
gives cleaner structured data (exact `ahead_by`, merged_at); when not, the feeds
and page extraction above are sufficient. Never let the watch block on the API.

Check activity since the last scan (previous date in `logs/source_rotation.md`).
Log the watch every run, even when quiet ("github-watch: no movement").

## 1. Watched repositories

For each repo in SOURCES.md → "Watched repositories":
- **Releases / tags** (releases.atom / tags.atom) — a new release is a citable
  artifact (evidence-eligible against a trend).
- **Merged PRs** — extract the PRs page (`/<o>/<r>/pulls?q=is:pr+is:merged`);
  a notable merge (feature, format, kernel, model support) is a citable artifact.
- **Hot issues / discussions** — extract `/<o>/<r>/issues?q=is:open+sort:comments`;
  a suddenly high-activity thread is a QUEUE signal until it lands.

## 2. Watched profiles / users

For each user in SOURCES.md → "Watched profiles/users", read their activity feed
(`https://github.com/<u>.atom`) to see where they're heading: brand-new repos, a
repo getting heavy pushes, a new release on any of their repos. New repos/releases
are citable; early push activity on an unreleased repo is a queue signal
("watch <user>/<repo>, pre-release").

## 3. Fork-tree analysis (depth 3) + Fork Notability Score

For each project in SOURCES.md → "Fork-tree analysis", walk the fork tree up to
depth 3 (the repo's forks page / `/network/members`, then forks of the active
ones, etc.). Prune aggressively: only descend into a fork that is itself active
(updated in the last ~30 days) — dead forks have no live children worth chasing.

Compute the **Fork Notability Score (FNS)** per fork. Read the values from the
fork's page ("This branch is N commits ahead", star count, Releases tab) — or
from the REST API if it's available:

```
gate:   updated within last 30 days          (else skip — stale)
FNS  =  commits_ahead_of_upstream            (the "N commits ahead" figure)
      + 2 × (fork's own stars)
      + 20 if the fork has its own releases/tags
      + 15 if the fork has an open PR back to upstream
```

**Surface a fork under the project's trend when FNS ≥ 50 AND commits_ahead ≥ 20.**
- A fork that clears the bar AND ships a release/artifact → citable evidence
  under that project's trend (cite the fork repo/release).
- A fork that clears the bar but is still pre-release (just diverging fast) →
  `observation_queue` signal ("fork <o>/<r> diverging, N commits ahead").
- Name the fork in the trend's notes/evidence ("fork X carries feature Y not yet
  upstream"). Tune the threshold over time and log changes in the report.

Rationale: in this ecosystem the real innovation often lives in an active,
far-ahead fork (performance/quant variants) months before it merges upstream —
FNS is meant to catch exactly those, not the thousands of bookmark forks.

## Self-maintenance (agent owns this)

Add repos/users/projects that become central to a tracked trend; drop ones that
go silent or off-scope (one-line reason in the report). Adjust the FNS weights
and threshold as you learn what they surface — record any change. Keep all lists
in `SOURCES.md`.
