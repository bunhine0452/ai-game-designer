# Rhythm

Gameplay synchronized to music: note-highway games, rhythm action (combat on the beat),
rhythm-roguelikes, dance and VR rhythm games.

## Core loop
Hear and see the beat → anticipate the next note or pattern → input on time → instant timing
feedback (perfect, great, miss) and audiovisual reward → build a combo or multiplier → the
song's climax → score and grade.

## Signature mechanics
- Timing windows (judgment tiers) and input calibration (audio and video latency offsets).
- Charts: note patterns authored per song and difficulty.
- Combos, multipliers, health or groove meters.
- Rhythm action: attacks and movement on the beat, with bonuses for being in sync rather
  than hard failure.
- Visual feedback timed to the music.

## Pacing shape
The **song's structure is the pacing**: intro (teach the pattern) → verses → chorus peaks →
bridge (a variation or break) → final chorus (climax). Charts should follow the music's
energy. Across the game, song difficulty and BPM rise, and mechanics are introduced per
world.

## Progression model
Song unlocks, difficulty tiers, score and grade mastery, leaderboards. Rhythm action adds
character upgrades.

## Balancing levers
- Timing window sizes per difficulty; how harsh misses are.
- Note density, pattern complexity, BPM.
- Chart readability (note speed and spacing).
- Assist options (wider windows, auto-play of some lanes, no-fail modes).
- Calibration UX, which is critical. Bad calibration feels like bad design.

## Failure modes
- **Latency:** uncalibrated audio and video offset makes perfect play impossible.
- **Charts that ignore the music:** notes that don't match what players hear.
- **Hard fail states** that stop the song; players lose the music they came for.
- **Difficulty cliffs** between tiers.
- **Licensing scope:** music rights drive the budget and the risk.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Hi-Fi Rush | Designed backwards from the feeling of action on the beat; the whole world moves to the music, and staying on beat is rewarded rather than missing being punished |
| Thumper | "Rhythm violence": intense audiovisual feedback turns a note highway into a horror ride |
| Crypt of the NecroDancer | Movement on the beat in a roguelike; rhythm adds pressure to tactics |
| Guitar Hero / Rock Band | Instrument-like controllers plus well-known songs give a performance fantasy |
| Beat Saber | Full-body input in VR; slashing in a direction turns timing into physical expression |

## Talks and postmortems
- Johanas, *Developing Hi-Fi RUSH Backwards and Finding Our Positive Gameplay Loop* (GDC 2024).
- Flury, *Thumper* GDC session (custom engine, design, VR adaptation).

## Design questions
1. What happens when the player is off-beat: punishment, or less reward?
2. Does the chart's intensity curve match the song's?
3. How does a new player calibrate latency in the first minute?
4. What is the music budget, and does the design depend on licensed tracks?

## Sources
- [B27] Johanas (2024). https://gdcvault.com/play/1034256/Developing-Hi-Fi-RUSH-Backwards
- [B28] Flury, *Thumper* GDC session.
- [A11] Swink: real-time feedback.
- Full bibliography: `research/SOURCES.md` in the repository.
