# What makes it fun: the evidence

The frameworks in this skill (interest curves, flow, MDA, game feel) say how to shape an
experience. This file covers the experiments and large datasets on *what players actually
enjoy*. Use it to choose between design options and to word fixes as testable predictions.

"Fun" is not one thing. The findings below cover separate drivers. A game can be strong on one
and weak on another, so diagnose each one separately (see `design-review` →
`references/fun-diagnosis.md`).

## Evidence at a glance

Strength: **Strong** = large or pre-registered studies, or replicated. **Moderate** = one good
experiment or a few consistent studies. **Emerging** = recent or mixed evidence. **Practice** =
documented studio practice, not experiments.

| Driver | Finding | Strength | Source |
|---|---|---|---|
| Challenge | Enjoyment rises with challenge that feels *enjoyably* hard. Stronger opponents and close games beat easy wins | Moderate | [A32], [A33] |
| Outcome uncertainty | Close contests are more fun than blowouts. Winning big raises felt competence but lowers enjoyment; suspense explains the gap | Moderate | [A34] |
| Curiosity | Curiosity was the strongest predictor of enjoyment and the only predictor of play time, and *uncertain* success drove it | Strong (n = 1,699, pre-registered) | [A35] |
| Feedback dose | Medium and high juice beat both none and extreme. Decoration that isn't tied to actions raises appeal, not competence | Moderate | [A36], [A37] |
| Needs, both ways | Need *frustration* (autonomy, competence, relatedness) is separate from low satisfaction, and both shape experience | Strong (5 studies, n = 1,246) | [A38] |
| Why, not how long | Hours played barely relate to well-being. Playing because you want to relates positively; feeling you have to relates negatively | Strong (telemetry, n = 38,935) | [A39] |
| Hidden difficulty tuning | Dynamic difficulty adjustment (DDA) improves performance, but results on enjoyment are mixed, and noticing it can feel bad | Emerging | [A40], [A41] |
| Playing together | Shared, co-located play raises enjoyment through social presence | Moderate | [A42] |
| Meaningful choice | Choices raise felt agency when the options lead to noticeably different outcomes | Emerging | [A43] |
| Meaning | Moving, reflective and socially connecting experiences ("appreciation") are a second kind of reward, beside pleasure | Moderate (82-study review) | [A44] |
| Systems that make fun | Rules that act on each other (fire burns grass, wind carries fire) produce play nobody scripted | Practice | [A45] |
| Audience | Interest in competition falls more with age than any other motivation; age matters more than gender | Strong (survey data, 239k players) | [A8] |

## 1. Challenge: hard, but enjoyably so

- In online chess, players enjoyed games against stronger opponents, and close games, more than
  lopsided ones. Challenge raised enjoyment for games, sports and hobbies, not for chores.
- In a first-person shooter study, whether the challenge *felt pleasant* predicted a good
  experience better than how hard it was.

**Design rules**
- Aim each new challenge slightly above the player's current skill (the sawtooth in
  `flow-and-difficulty.md`), and make sure failure reads as fair. Legibility is what turns
  "hard" into "enjoyably hard".
- Optional difficulty belongs in hobby-like content (side challenges, mastery goals). Chore-like
  tasks (inventory sorting, travel) should be easy.

## 2. Outcome uncertainty: keep the result in doubt

- When score parity was manipulated in a competitive game, closer games were more enjoyable, and
  suspense carried the effect. Crushing the opponent felt competent but less fun.
  The sample was small (72 students), so treat the size of the effect as unknown.

**Design rules**
- Design for close finishes: late swings, last-moment decisions, and bosses whose final phase
  is the hardest. Avoid outcomes decided long before the end.
- Matchmaking and difficulty should aim at about even odds, not at guaranteed wins.
- Comeback mechanics help when players can see and understand them. Hidden rubber-banding can
  feel unfair once it's noticed (see DDA below).
- **Measure it:** log the final margin of each contest and look at the distribution
  (`playtest_report.py` reports close and one-sided outcomes per level).

## 3. Curiosity: uncertain success, unanswered questions

- In a pre-registered experiment with 1,699 players, curiosity predicted enjoyment more strongly
  than competence did, and it was the only predictor of how long people kept playing. Feedback
  that left the *size* of success uncertain (graded, variable results) fed curiosity.
- Learning-progress theory fits this: progress in understanding is rewarding in itself. The
  theory is still debated, but it agrees with Koster's "fun is learning" [A10].

**Design rules**
- Prefer graded outcomes (how well, not just whether) and some variability in results.
- Introduce a new rule, enemy or combination at a steady rhythm, and leave visible things that
  are not explained yet: a locked door, a mural, a strange plant.
- A curiosity peak is a valid beat type in the interest curve. Plan reveals the way you plan
  fights.

## 4. Feedback dose: legible beats loud

- Four versions of one action RPG differed only in juice (none, medium, high, extreme). Medium
  and high beat both none and extreme on player experience, intrinsic motivation, play time and
  performance.
- Non-interactive visual embellishment raised audiovisual appeal but not felt competence.

**Design rules**
- Juice should carry information: it confirms the action, shows the outcome, and scales with
  the outcome's size. Pure decoration is polish, not feel.
- Stop well before the screen is hard to read. If players miss what happened, there is too much.
  See `game-feel.md` for layering and the cautions.

## 5. Needs: check satisfaction and frustration

The Basic Needs in Games Scale (BANGS) measures satisfaction and frustration of each need
separately. A game can satisfy competence and still frustrate it.

| Need | Satisfied by | Frustrated by (look for these) |
|---|---|---|
| Autonomy | Real options, self-chosen goals, expressive play | Forced grinds, mandatory dailies, "you must play now" pressure, a single correct build |
| Competence | Clear goals, fair challenge, visible improvement | Unreadable deaths, spikes, punishing input lag, losses blamed on luck or pay-to-win |
| Relatedness | Co-operation, shared moments, being recognized | Toxicity, being left out, matchmaking that strands newcomers, forced social obligations |

## 6. Why players play matters more than how long

Linked play logs from seven games and 38,935 players showed almost no effect of hours played on
well-being. Intrinsic motivation related positively to well-being and extrinsic motivation
("I have to") negatively.

**Design rules**
- Retention and session length are not measures of fun. Read them together with "want to" vs
  "have to" questions (the playtest kit's `pressure` item).
- Treat pressure mechanics (expiring rewards, streaks, FOMO events) as costs to justify. The
  ethics pass in `design-review` covers them.

## 7. Difficulty tuning: transparent beats hidden

Performance-based DDA reliably helps players perform better, but experiments disagree on
whether it makes games more enjoyable, and some players dislike discovering it.

**Design rules**
- Prefer assists the player chooses and can see (Celeste-style options), then pacing levers
  (more checkpoints), and only then hidden tuning, as ordered in `flow-and-difficulty.md`.
- If you tune in secret, tune *opportunities* (pickup drops, enemy spawn timing) rather than
  outcomes the player can audit (hit chances, damage).

## 8. Others, choice and meaning

- **Together:** playing in the same room raises enjoyment through social presence. Couch co-op,
  spectating and shared reactions are fun multipliers, not extras.
- **Meaningful choice:** options must lead somewhere noticeably different, soon enough to be
  felt. Autonomy is not the same as freedom: a narrow game can still feel self-directed.
- **Meaning:** some of the most remembered moments are moving rather than pleasant. Plan room for
  reflection after peaks (the relief beats in `pacing-models.md`).

## 9. Build systems that make fun

Breath of the Wild's team prototyped rules that act on each other (physics plus a "chemistry"
of fire, ice and wind on materials) in a 2D mock-up first. They let players invent solutions and
removed puzzles with only one answer. When the fun should come from player invention, test the
rule interactions in a greybox before building content.

## 10. Claims to avoid

- **"Dopamine design."** A 1998 PET study found striatal dopamine release during a video game
  [A46], but its authors later noted confounds. Design from observed behavior and experience,
  not neurotransmitter stories.
- **"They played 3 hours, so it's fun."** See §6.
- **"Players want it easy."** See §1–2: they want it fair and in doubt.

## Quick check (use in reviews and playtests)

1. Where is the next challenge slightly above the player's skill, and is failing there fair?
2. How many contests are decided long before they end?
3. What will the player be curious about in the next five minutes?
4. Does every effect tell the player something? Is anything unreadable?
5. Which need could this feature frustrate, and for whom?
6. Would players keep playing if every streak, timer and expiring reward were removed?
7. Are assists visible and chosen by the player?
8. Does any moment invite players to share it or to reflect?

## Sources
- [A32] Abuhamdeh & Csikszentmihalyi (2012), challenge and enjoyment. · [A33] Corcos (2018), enjoyable challenge in an FPS.
- [A34] Abuhamdeh, Csikszentmihalyi & Jalal (2014/15), outcome uncertainty and suspense.
- [A35] Kao, Ballou, Gerling, Breitsohl & Deterding (2024), juicy feedback, curiosity and competence. CHI '24.
- [A36] Kao (2020), the effects of juiciness in an action RPG. · [A37] Meiners, Hicks et al. (2025), lushness.
- [A38] Ballou et al. (2024), Basic Needs in Games Scale. · [A39] Vuorre, Johannes, Magnusson & Przybylski (2022).
- [A40] Robb & Zhang (2022), performance-based DDA. · [A41] Denisova & Cairns (2015), adaptation and immersion.
- [A42] Gajadhar, de Kort & IJsselsteijn (2008), shared fun. · [A43] Cardona-Rivera et al. (2014), meaningful choices.
- [A44] Daneels et al. (2021), eudaimonic experiences in games. · [A45] Fujibayashi, Dohta & Takizawa (GDC 2017), BotW.
- [A46] Koepp et al. (1998), dopamine release during a video game. · [A8] Quantic Foundry. · [A10] Koster.
- Full bibliography: `research/SOURCES.md` in the repository.
