# Example: design brief for an original concept

**User prompt:** "I want to make a short-run roguelite where light is everything. Solo dev,
about 12 months, PC first."

---

**Lanternfall** (working title) · Action roguelite · PC, gamepad and keyboard/mouse ·
20-minute runs · Core action players who like Hades-style runs and readable combat ·
Stage: concept

**Fantasy:** You are the last lantern spirit, sinking through a drowned city, and every
spark you carry is both your life and your weapon.

**Target aesthetics (ranked):** 1. Challenge · 2. Discovery · 3. Fantasy

**Pillars**

| Pillar | Serves | Test question | Would reject |
|---|---|---|---|
| Light is the only resource | Challenge | Does this feature spend, risk or create light? | A separate mana bar |
| Every room is a readable puzzle-fight | Challenge | Can a player tell within 2 s what each enemy will do? | Enemies with hidden or random tells |
| The deep remembers | Discovery, Fantasy | Does a run leave something behind in the city above? | Meta progression that is only stat bonuses |

**Core loops**

- *Moment-to-moment (2–10 s):* dash / strike / flare → enemies flinch, light burst →
  light orbs drop → spend or keep the light.
- *Session (20-min run):* choose a district path → clear 4–6 rooms → pick a boon at a
  shrine → mid-boss → second district → final keeper → bank remembered light.
- *Meta (weeks):* banked light relights districts of the city above, which unlocks new
  starting lanterns, NPC stories and harder "darker" depths (opt-in difficulty).

**Reference games**

| Game | The one thing to learn |
|---|---|
| Hades | A narrative that advances on death, so failure is progress |
| Into the Breach | Fully telegraphed enemy intent makes every turn a fair puzzle |
| Dead Cells | Run-to-run variety from a small number of well-tuned rooms and weapons |

**Biggest risks**

1. *Fun:* light as health **and** currency may feel stingy (players hoard instead of
   fighting). **Cheapest test:** greybox 3 rooms with a light meter; does median light
   spent per room fall over 10 runs? Pass if players spend ≥ 40% of the light they pick up.
2. *Scope:* two districts × 15 rooms × 8 enemy types is a lot for one person.
   **Test:** build one district end to end with placeholder art and measure the hours.
3. *Market:* "roguelite with a twist" is crowded. **Test:** a 30-second capsule GIF of
   the light mechanic. Does it get wishlists or replies on two channels?

**Next step:** a 2-week greybox of one district (4 rooms + shrine + mini-boss) with the
light meter. Log light spent per room and run length. Then run the `fun-curve` skill on the
logged beats.

---

*Routing offered next:* `fun-curve` (draft the 20-minute run's interest curve),
`genre-design` (roguelite playbook: room pacing and boon design), `balance-economy` (light
income vs. spend model).
