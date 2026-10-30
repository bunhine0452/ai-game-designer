# Game feel and juice

When individual moments feel weak, the problem is often feel, not pacing. A perfectly
ordered beat list still falls flat if hitting an enemy feels like clicking a spreadsheet.

## Swink's model

Swink defines game feel as the overlap of three things:
1. **Real-time control**: the player steers continuously and the game answers fast enough to
   feel like an extension of the body.
2. **Simulated space**: movement and collision in a 2D or 3D world give actions physical
   meaning.
3. **Polish**: animation, sound and effects that agree with input-driven motion and create
   an impression of physicality.

He notes that the functionality would be unchanged without polish, but the experience
would feel less convincing and less appealing. A later survey points out that the definition
doesn't cover every kind of game (turn-based, text, abstract), so treat "feel" more broadly
there (responsiveness and clarity of feedback).

## Tuning levers for control feel

| Lever | Effect | Typical starting points |
|---|---|---|
| Input latency | Responsiveness | As low as possible; response well under 100 ms |
| Acceleration / deceleration | Weight vs. snappiness | Short ramps for precision games; longer for heavy characters |
| Jump arc | Floaty vs. tight | Faster fall than rise; lower gravity near the apex for control |
| Animation canceling | Responsiveness vs. commitment | Allow cancels into movement or defense when you want responsiveness |
| Camera | Readability, speed sensation | Lead the camera in the movement direction; dampen small jitter |

## Forgiveness (Celeste's list)

Precise games feel fair when they quietly forgive near-misses:
- **Coyote time**: a jump still works for a short moment after leaving a ledge.
- **Jump buffering**: pressing jump slightly before landing still jumps on landing.
- **Halved gravity at the apex** while jump is held, for finer air control.
- **Corner correction**: nudge the player around a corner they barely clip.

Make them invisible and consistent. Players should feel skilled, not helped.

## Juice: feedback layering

"Juice it or lose it" showed live how a flat Breakout clone comes alive through layered
feedback:
- **Tweening and easing** instead of instant changes.
- **Squash and stretch** on impact and movement.
- **Particles** on hits, deaths and pickups.
- **Screen shake**, short and scaled to impact size.
- **Hitstop**: freezing a few frames on a heavy hit.
- **Sound** for every interaction, varied in pitch to avoid repetition.
- **Secondary motion** (wobble, trails, reacting environment).

Rule of thumb: the bigger the consequence, the bigger the feedback. Reserve the strongest
effects for the moments that matter most, or nothing will stand out.

## Cautions

- **Readability first.** Excess juice can hide information. A counter-talk ("Don't juice it
  or lose it") argued that over-polish can hurt immersion and clarity. Test whether players
  can still read threats during the busiest moments.
- **There is an optimal dose.** In an experiment with four versions of one action RPG, medium
  and high juice beat both no juice and extreme juice on player experience, motivation, play
  time and performance [A36]. Decoration not tied to actions raises visual appeal, not felt
  competence [A37]. Feedback that shows *how well* an action went also feeds curiosity [A35].
- **Accessibility.** Give options to reduce screen shake, flashes and motion blur. Provide
  visual alternatives to audio cues and the reverse ("second channel").
- **Juice doesn't fix design.** It makes good interactions feel great. It can't make a
  meaningless interaction interesting.

## Quick feel audit

1. Record 30 s of core play, then watch it muted and slowed down. Does every input produce a
   visible reaction within a frame or two?
2. Does every hit have anticipation, impact and follow-through?
3. Are the strongest effects reserved for the strongest moments?
4. With effects at maximum, can a first-time viewer still tell who is attacking whom?

## Sources

- [A11] Swink (2008), *Game Feel: A Game Designer's Guide to Virtual Sensation*.
- [A31] Pichlmair & Johansen (2020), *Designing Game Feel: A Survey*. https://arxiv.org/pdf/2011.09201
- [A12] Jonasson & Purho (2012), *Juice it or lose it*. · [A30] Kelly, *Don't Juice It or Lose It* (recap).
- [A13] Thorson (2020), *Celeste & Forgiveness*.
- [A35] Kao et al. (2024), CHI. · [A36] Kao (2020), *Entertainment Computing* 34. · [A37] Meiners, Hicks et al. (2025).
- [D9] AbleGamers APX: second channel. · [D7] Game Accessibility Guidelines.
- Full bibliography: `research/SOURCES.md` in the repository.
