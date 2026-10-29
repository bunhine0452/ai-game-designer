# Audio direction

Audio carries emotion **and** information. Define both in the design pillars.

## Audio pillars

Mirror the visual pillars. For example:

```
Audio pillar: "Hear the danger before you see it"
Serves: gameplay pillar "Every room is a readable fight"
Rules: every enemy has a unique wind-up sound 0.4 s before attacking; enemy cues
sit above music in the mix; off-screen threats are spatialized
Test: blindfolded, can a playtester say which enemy is attacking and from where?
```

Overwatch's audio team worked to the director's goal of "play by sound". With 12 players
and many abilities, they needed a clean mix, precisely locatable sounds, audio that carries
gameplay information, and distinct ally vs. enemy sounds (footsteps especially).

## Mix hierarchy

Rank sound categories and use ducking or priority so the critical ones are never masked:

1. Gameplay-critical cues (threat wind-ups, low health, objective alerts)
2. Player feedback (hits, pickups, UI confirms)
3. Dialogue / VO
4. Music
5. Ambience and decoration

## Music behavior

| Technique | What it does | Good for |
|---|---|---|
| Vertical layering | Add or remove stems with intensity | Combat ramps, exploration → threat |
| Horizontal re-sequencing | Switch sections at musical boundaries | Phase changes, boss phases |
| Stingers | Short cues on events | Discoveries, kills, reveals |
| Silence | Removing music on purpose | Horror dread, emotional beats |

Tie music intensity to the interest curve (`fun-curve`): music layers rise with peaks and
drop in valleys, so music reinforces the pacing.

## Sound as game feel

Every interaction needs a sound. Vary pitch and sample (round-robin) to avoid repetition
fatigue. Scale impact sounds with consequence. Use audio hitstop alongside visual hitstop.

## Accessibility

- Pair every critical audio cue with a visual cue ("second channel"): subtitles with speaker
  names and directional captions for important sounds.
- Separate volume sliders (music, SFX, voice, UI) and a mono option.
- Avoid information carried only by stereo or pitch differences.

## Audio style guide checklist

- [ ] Audio pillars (≤ 3) with tests
- [ ] Mix hierarchy and ducking rules
- [ ] Music behavior per game state (explore, combat, boss, menu)
- [ ] Sound families and their shared character (materials, enemy factions)
- [ ] Voice direction (tone, casting notes, line-count budget)
- [ ] Technical: formats, loudness targets, voice limits, middleware
- [ ] Accessibility: captions, visual equivalents, sliders

## Sources
- [D13] Lawlor & Neumann (2016), *Overwatch: The Elusive Goal: Play by Sound* (GDC). https://gdcvault.com/play/1023010/Overwatch-The-Elusive-Goal-Play
- [D9] AbleGamers APX: second channel. · [D7] Game Accessibility Guidelines.
- [A12] Jonasson & Purho (2012): sound as part of juice.
- Full bibliography: `research/SOURCES.md` in the repository.
