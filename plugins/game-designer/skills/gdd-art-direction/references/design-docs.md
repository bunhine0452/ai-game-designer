# Modern design documentation

## Why heavy GDDs fail

The classic 200-page GDD written up front is rarely read, goes stale as soon as the
prototype teaches something, and hides the important decisions under the trivial ones.
Librande's GDC talk on **one-page designs** argued for single, visual pages, built with
diagrams, layout and whitespace, that a team can pin to a wall, read in a minute, and update.
He later applied the format to SimCity's simulation systems.

## The modern stack

| Layer | What | When | Owner |
|---|---|---|---|
| Pillars + design brief | 1 page: fantasy, aesthetics, pillars, loops, risks | Concept | Creative lead |
| One-page designs | 1 page per system or feature (combat, economy, a level) | Concept → pre-production | System owner |
| Living GDD hub | An index page linking every one-pager, spec, decision and open question | Pre-production onward | Design lead |
| Feature specs | Buildable detail per feature: rules, edge cases, UI, telemetry, acceptance criteria | Before implementation | Feature designer |
| Decision log | Dated decisions with the reason and the alternatives rejected | Always | Everyone |
| Style guides | Art and audio direction | Once a visual target exists | Art and audio leads |

## Writing principles

1. **Decide, don't describe.** Every section answers a question the team needs answered.
2. **Pillars as filters.** Each feature names its pillar; features without one are candidates
   for cutting.
3. **Visual first.** Loop diagrams, flowcharts, annotated mockups, tables. A diagram the team
   argues over is worth more than paragraphs nobody reads.
4. **Status per section:** `draft` / `agreed` / `built` / `cut`, so readers know what's real.
5. **Open questions in the open:** list them with options and a deadline.
6. **Prototype-driven.** Fullerton's playcentric process alternates concept, prototype and
   playtest, with documents recording what the prototypes taught.
7. **Short shelf life is fine.** Delete or archive pages for cut features. Stale docs are
   worse than no docs.

## Feature spec essentials

A buildable spec covers: purpose (pillar and player problem), player-facing description,
rules and formulas, states and edge cases, UI and feedback, content needs, telemetry events,
acceptance criteria (testable), dependencies, and open questions. See
`templates/feature-spec.md`.

## Pitch vs. production documents

- **Pitch:** sells the *experience* (fantasy, hook, references, the visual target, why now, why
  this team). Short and emotional.
- **Production:** enables *building* (rules, numbers, edge cases). Precise and modular.
  Don't mix the two.

## Sources
- [D1] Librande (2010), *One-Page Designs* (GDC). https://www.gdcvault.com/play/1012356
- [D2] Librande (2013), *Simulating a City, One Page at a Time* (GDC).
- [D3] Fullerton (2018), *Game Design Workshop* (4th ed.).
- [B16] Cleveland (2019): pillars in Subnautica. · [B27] Johanas (2024): core pillars in Hi-Fi Rush.
- [B21] Dallas (2018): many small prototypes in Edith Finch.
- Full bibliography: `research/SOURCES.md` in the repository.
