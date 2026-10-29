# Accessibility

Accessibility widens the audience and improves the game for everyone. Plan it from the
start: retrofitting costs more. The Last of Us Part II shipped about 60 accessibility options,
which the team attributed to planning them early. They also argued that **accessibility is
orthogonal to difficulty**: options remove barriers; they don't lower the challenge the
player chose.

## Frameworks

- **Game Accessibility Guidelines (GAG):** recommendations in three tiers.
  - *Basic:* easy to implement, wide reach, applies to most games.
  - *Intermediate:* needs some planning, often just good design.
  - *Advanced:* complex adaptations for profound impairments or niche mechanics.
  Weighted by reach, impact and cost; grouped by motor, cognitive, vision, hearing, speech
  and general.
- **Xbox Accessibility Guidelines (XAG):** best-practice guidelines across visual, audio,
  input, difficulty and pace, communication, and documentation and support. Each has goals,
  scoping questions and implementation guidance. Meant as idea generators and checklists, not
  legal compliance.
- **AbleGamers APX (Accessible Player Experiences):** design patterns drawn from research
  with players with disabilities, e.g. *Second Channel* (carry critical information through
  more than one sense).

## Basic-tier checklist (include in every GDD and UI spec)

**Motor**
- [ ] Full control remapping (including for gamepads)
- [ ] No required simultaneous button presses or rapid repeated tapping, or alternatives (toggle/hold)
- [ ] Adjustable sensitivity; no essential precision timing without an assist option

**Vision**
- [ ] Text size adjustable; default body text readable at the platform's viewing distance
- [ ] Contrast at least 4.5:1 for UI text
- [ ] Never color alone for meaning: add shape, icon, pattern or text
- [ ] Colorblind-friendly palettes for gameplay-critical colors. Red-green deficiency affects
      about 8% of men and 0.4% of women of European ancestry
- [ ] Options to reduce screen shake, flashing and motion blur

**Hearing**
- [ ] Subtitles on by default or offered at first launch, with speaker names and a size option
- [ ] Captions or visual indicators for gameplay-critical sounds
- [ ] Separate volume sliders (music, SFX, voice)

**Cognitive**
- [ ] Tutorials can be replayed; objectives stay accessible (journal, marker)
- [ ] No time pressure on reading; pause available in single-player
- [ ] Consistent UI patterns and clear language

**General**
- [ ] Accessibility options available before gameplay starts (first launch)
- [ ] Difficulty and assist options separated and clearly described
- [ ] Settings save per profile

## How to review a design for accessibility

1. List every **piece of information** the player needs (threat, objective, health, timing).
2. For each, list the **channels** that carry it (visual, audio, haptic). Only one channel is a
   barrier, so add a second.
3. List every **input demand** (precision, speed, simultaneous presses, holds). Offer an
   alternative for each demanding one.
4. Check **reading and memory load**: text speed, objective reminders, tutorial access.
5. Test with players with disabilities where possible. Community organizations can help
   recruit.

## Sources
- [D7] Game Accessibility Guidelines. https://gameaccessibilityguidelines.com/
- [D8] Microsoft, Xbox Accessibility Guidelines. https://learn.microsoft.com/en-us/gaming/accessibility/guidelines
- [D9] AbleGamers, APX. https://accessible.games/apx
- [D10] Schatz & Gallant (2020), *Accessibility in The Last of Us Part II* (GAConf).
- [D11] Birch (2012), *Worldwide prevalence of red-green color deficiency*, JOSA A 29(3). doi:10.1364/JOSAA.29.000313
- [D12] W3C (2023), WCAG 2.2.
- Full bibliography: `research/SOURCES.md` in the repository.
