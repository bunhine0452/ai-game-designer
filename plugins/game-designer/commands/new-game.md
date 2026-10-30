---
description: Turn a game idea into a starter design pack (brief, genre fit, first-session curve, risks) in one pass
argument-hint: "[one or two sentences about the game idea]"
---

Build a starter design pack for this idea: $ARGUMENTS

If no idea was given, ask for one sentence about the game and stop.

Work through these steps in order, using the plugin's skills. Answer in the user's language and
follow each skill's language rules.

1. **Brief** (`game-design`): player fantasy, 3 pillars with test questions, core loops,
   MDA notes, target audience and platform. Assume sensible defaults and list them instead of
   asking several questions first.
2. **Genre fit** (`genre-design`): name the core genre and any hybrid, then list 3 conventions
   to honor and 1–2 to break deliberately, each tied to a pillar.
3. **First-session curve** (`fun-curve`): list 8–12 beats for the first 15–30 minutes, with
   intensity values. If the scripts are available, save them as a CSV and run `fun_curve.py`.
   Report the diagnosis.
4. **Risks** (`design-review`): name the three riskiest assumptions, the cheapest test for
   each, and a pass criterion.

Write everything to `design/<game-slug>/` (one Markdown file per step, plus the CSV and chart)
unless the user asked for chat-only output. End with a short summary and the single most
valuable next step, for example `/game-designer:prototype design/<game-slug>/01-brief.md`.
