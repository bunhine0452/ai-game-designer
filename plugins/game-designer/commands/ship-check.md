---
description: Pre-release design review covering pacing, onboarding, accessibility, monetization ethics and scope
argument-hint: "[path to the GDD, build notes, or playtest notes]"
---

Run a pre-release design check on: $ARGUMENTS

Use the `design-review` skill as the frame, and pull in the others where they apply:

1. **Pacing and onboarding** (`fun-curve`): does the first session hook within its first minutes?
   Are there flat stretches or difficulty walls?
2. **Accessibility** (`gdd-art-direction` accessibility checklist): list each item as met,
   missing, or not applicable, with the cheapest fix for each missing item.
3. **Monetization and retention ethics** (`design-review` dark-pattern pass): flag anything
   that pressures, obscures odds or costs, or exploits loss aversion, and offer a healthy
   alternative.
4. **Scope**: what to cut or defer so that what ships is finished.

Output a prioritized table (severity, finding, evidence, fix, effort) followed by a
go / go-with-fixes / not-yet verdict and its reasons. If an independent read would help, hand
the material to the `design-critic` agent and merge its findings, marking which came from it.

If no material was given, ask for the document or notes to review and stop.
