---
name: radar-explore
description: |
  Discover important work the radar does NOT yet track, by iterating the discovery-venue list in SOURCES.md every run — significance-first: read the top / most-attention items in each venue REGARDLESS of topic, not by searching tracked axes. Surfaces off-axis significance and candidate new axes. Use for the daily exploration slot, after the sweeps.
---

# Explore — find what we SHOULD be tracking, not only confirm what we do

The sweeps (`radar-lab-sweep`, `radar-pulse`, `radar-repo-watch`) CHECK known
sources for new items on the axes we already track. This skill does the opposite
job: it finds work we do NOT yet track but that is important — the candidate next
axis, the off-axis result the field is about to care about.

It is list-driven exactly like the lab sweep: the venues live in `SOURCES.md` and
you iterate ALL of them. You do not "explore something" by vibe — you execute a
list of WHERE new work surfaces. WHAT to look for is never enumerated here (that
is the trap that makes the search narrow); WHERE to look is the contract.

## Method (significance over topic-match)

1. ITERATE the venues in `SOURCES.md` → "Discovery / exploration venues" (see the
   list contract there: cross-category attention venues every run; one rotating
   arXiv category as supplement). For each venue, read its TOP / most-attention
   items — HF daily papers by upvotes, an arXiv category's newest listing, a
   trending feed's lead items — REGARDLESS of whether they match a tracked axis.
2. ADVANCE THE WINDOW: read items NEWER than the last time you covered THAT venue
   (its previous date in `logs/source_rotation.md`); record the range. A venue
   that returns "same batch already mined" did not advance — move the window
   forward or take the next venue in rotation. Never re-mine the same listing.
3. Assess each top item on its OWN merits, NOT the trend bar: does it claim to
   solve a known hard problem, is it highly ranked / from a serious venue, are
   multiple groups already on it? Significance is topic-agnostic — a result OFF
   every current axis can still be the most important thing you see today.
4. ROUTE every find per `routines/daily.md` §4 and `radar-ledger-update`: on a
   tracked axis → evidence; a queue cluster of ≥3 independent groups → a seed
   trend; else → `observation_queue` (a genuinely significant OFF-axis single
   artifact still gets queued, marked "significant, off-axis"). A named primary is
   NEVER left in report prose only.
5. Recurring off-axis significance is a candidate NEW AXIS — propose it at the
   weekly. The radar's job is to discover what it SHOULD track, not only confirm
   what it already does.

## Venue list

Lives in `SOURCES.md` → "Discovery / exploration venues" (agent-owned: ADD a
venue when it repeatedly surfaces significant work, drop dead ones — a new venue
goes INTO that list so it is iterated next run, never just into this prose).
Cross-category, attention-ranked venues are PRIMARY every run — they show a theme
forming across categories that a single arXiv category cannot. Single arXiv
categories are a supplementary rotation with an advancing window.

## Log

Record in `logs/source_rotation.md` which venues you covered and the date range
each run, even when nothing cleared assessment ("explore: <venues>, nothing new").
A venue you skipped is a discovery gap, not a lean pass.
