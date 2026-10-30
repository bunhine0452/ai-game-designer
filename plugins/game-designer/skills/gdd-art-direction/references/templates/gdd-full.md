# Living GDD template (hub plus linked pages)

The GDD is a **hub**: a short index page linking to one-pagers, feature specs, style guides
and the decision log. Each section has an owner and a status. Keep the hub under ~3 screens.

```
# <Title> — Game Design Document (hub)
Version: 0.x · Updated: YYYY-MM-DD · Owner: ___ · Status legend: draft / agreed / built / cut

## 1. Vision                                   [status]
- One-sentence fantasy
- Target aesthetics (ranked) and audience motivations
- Pillars (with test questions)
- Reference games (lessons)
- Unique selling points (max 3)

## 2. Game overview                            [status]
- Genre(s): core + wrapper
- Platform, input, session length, business model
- Core loops (diagram) — link: /onepagers/core-loop

## 3. Systems                                  [status per row]
| System | One-pager | Spec | Owner | Status |
|---|---|---|---|---|
| Movement / controls | link | link | | |
| Combat / core verb | | | | |
| Progression | | | | |
| Economy | | | | |
| AI / enemies | | | | |
| Level / world structure | | | | |
| Narrative | | | | |
| UI / UX | | | | |
| Multiplayer / social | | | | |
| Monetization (+ ethics review) | | | | |

## 4. Content                                  [status]
- World / level list with pacing goals (link fun-curve charts)
- Characters, enemies, items (link asset list)
- Narrative outline

## 5. Balance and data                         [status]
- Progression tables, economy model, cost curves (link CSVs and reports)
- Tuning ownership: who changes which numbers

## 6. Art and audio direction                  [status]
- Link: style guide (visual pillars, palette, readability rules)
- Link: audio style guide

## 7. Accessibility                            [status]
- Basic-tier checklist status; planned options list

## 8. Technical constraints                    [status]
- Engine, performance budgets, save system, platforms, localization

## 9. Production                               [status]
- Milestones (prototype → vertical slice → alpha → beta → soft launch)
- Scope: asset list totals vs. capacity
- Risks register (risk, likelihood, impact, mitigation, owner)

## 10. Telemetry and playtesting               [status]
- Key questions, events, KPIs per milestone; playtest schedule

## 11. Decision log
| Date | Decision | Why | Alternatives rejected | Owner |
|---|---|---|---|---|

## 12. Open questions
| Question | Options | Recommendation | Decide by | Owner |
|---|---|---|---|---|
```

Sources: [D1] Librande (2010); [D3] Fullerton (2018). Full bibliography: `research/SOURCES.md`.
