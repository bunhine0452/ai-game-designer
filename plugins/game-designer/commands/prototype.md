---
description: Build a tested, playable browser prototype from a design document
argument-hint: "[path to a one-pager, GDD, card list, or economy config]"
---

Build a playable prototype from: $ARGUMENTS

Follow the `playable-prototype` skill end to end:

1. Read the design documents and name the riskiest assumption the prototype will test.
2. Copy the design's numbers verbatim, with provenance comments, and start from the skill's
   `assets/template.html`.
3. Clear the presentation bar in `references/assets-and-feel.md`. The result must look and feel
   like a game, not a dashboard.
4. Write the self-tests with the game: fidelity, rules, bots and balance probes.
5. Run `scripts/check.py` on the result, open the screenshot, and fix what you see. If a browser
   tool is available, play it by mouse from the title screen to the end screen.
6. Report what the prototype tests, where each number came from, any placeholders, the test
   results, how to play, and the next playtest question with a pass criterion.

If no design document was given, ask for one (or offer to write a brief with
`/game-designer:new-game`) and stop.
