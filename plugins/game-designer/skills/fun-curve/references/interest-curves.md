# Interest curves

## The model

Schell treats any designed experience as a line of the player's **interest over time** and
judges the experience by the shape of that line. A typical strong shape:

1. **Hook**: an early high point that promises what the experience offers and earns the
   player's attention.
2. **Dip**: interest settles while the player learns. That's fine as long as the hook created
   enough anticipation to carry them.
3. **Rising peaks and valleys**: a series of peaks, each a little higher, separated by
   valleys that give relief and build anticipation.
4. **Climax**: the highest point, near the end.
5. **Resolution**: a short fall to rest, where the player takes in what happened.

The curve isn't a formula. It's a way to ask questions: Where does interest fall? Is the
first impression strong? Does each peak beat the last? Does the ending land?

## Nested curves

Interest curves nest like fractals. A good game-level curve can be made of badly shaped
sessions, and a good level can contain a flat encounter. Plot the scale that matches the
complaint:

| Scale | Typical span | Typical units | Example complaint |
|---|---|---|---|
| Encounter | 30 s – 3 min | seconds | "Boss phase 2 drags" |
| Level / room set | 3 – 20 min | minutes | "The sewer level is boring" |
| Run / session | 5 – 60 min | minutes | "Runs feel samey after biome 1" |
| Chapter | 1 – 5 h | minutes | "Act 2 loses people" |
| Whole game | 5 – 100+ h | hours or sessions | "Players quit around hour 8" |
| Live game | weeks – years | days or events | "Retention dips between seasons" |

At the whole-game scale, intensity is better read as *novelty plus stakes*: new mechanics,
new places, story turns and milestones. Moment-to-moment excitement matters less there.

## Reading a curve

| Pattern | Usually means | First fix to try |
|---|---|---|
| Low start, slow rise | No hook; first-session churn | Move a strong, legible moment into the first 10%: a taste of the core fantasy |
| Long flat stretch | Repetition with no new information | Add a twist on the current mechanic, a new threat, a reveal or a choice |
| Plateau at high intensity | Fatigue; peaks stop feeling special | Split into two peaks with a short release between |
| Peaks don't rise | Mid-game feels "the same but longer" | Escalate the kind of challenge (combinations, constraints, stakes), not just the numbers |
| Highest point early | Anticlimax; the ending is forgettable | Move the set piece later, or tone down the early one |
| Ends on the peak | Abrupt ending; no space to reflect | Add a brief resolution: results, story button, reward reveal |
| Long tail after the climax | Trailing chores after the high | Cut, or give the tail its own small arc |
| Regular, identical sawtooth | Predictable rhythm | Vary valley length and peak type; add one surprise |

## Valleys are not downtime

A valley is low *intensity*, not low *interest*. Good valleys do work:
- **Anticipation**: the player sees the next threat coming (a boss door, a storm on the
  horizon).
- **Reward and reflection**: loot, upgrades, story.
- **Planning**: shops, loadouts, map choices.
- **Recovery**: lets the body and mind reset so the next peak feels big.

A valley becomes a problem when it does none of these: backtracking, unskippable text,
menus with no decisions.

## Drawing curves with designers

1. List beats in order with rough times.
2. Score each beat 0–10 by predicted *felt* intensity (see `beat-list-format.md`).
3. Plot it, then mark the hook, every peak, the climax and every valley's purpose.
4. Compare with a reference shape for the genre (`pacing-models.md`).
5. After playtests, plot the *observed* curve (quit points, deaths, self-reports) over the
   predicted one. The gaps between them are the design problems.

## Sources

- [A1] Schell, *The Art of Game Design* (3rd ed., 2019), chapter on interest curves.
- [A4] Booth (2009), *The AI Systems of Left 4 Dead*: intensity-driven pacing in practice.
- [A10] Koster, *A Theory of Fun*: novelty and learning as the source of interest.
- Full bibliography: `research/SOURCES.md` in the repository.
