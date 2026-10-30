# Example: review of a fictional mobile concept

## The pitch (as submitted)

> **Sky Harbor**, a mobile idle trading game. You run an airship harbor. Ships fly trade
> routes automatically and earn coins. Captains (from a gacha) boost route income; legendary
> captains are 0.5% per pull with no pity, on a limited 7-day banner. Voyages cost energy
> (5 per day, refill for 50 gems). Log in daily for streak rewards; missing a day resets the
> streak. A weekly PvP leaderboard ranks harbors by income, and the top 100 get exclusive
> captains. Audience: "everyone". Monetization: gems.

---

## Verdict

The fantasy (a cozy sky harbor with characterful captains) and the idle structure suit short
mobile sessions. But the core loop has almost no decisions, and the monetization stacks
several dark patterns: an un-pitied limited gacha that decides PvP, streak resets and an
energy paywall. This creates legal exposure in several markets and will erode trust. **Fix
the monetization ethics first (P0), then give the routes real decisions.** Next step: a paper
prototype of route planning with trade-offs.

## Strengths (keep these)

- **A clear, cozy fantasy.** Airships and captains read instantly and suit Submission and
  Fantasy aesthetics.
- **Fits mobile sessions.** Idle routes support 2–5 minute check-ins.
- **Captains as characters.** They have collection appeal, and could also serve Story
  motivation.

## Issues

| ID | Sev | Lens | Issue | Evidence | Why it matters | Fix | Cost | Verify by |
|---|---|---|---|---|---|---|---|---|
| R1 | **P0** | Ethics | Paid random captains with no pity and no stated disclosure | "0.5% per pull with no pity" | Expected 200 pulls; 10% of payers need ~460+. Odds disclosure is required in Korea and China and by Apple §3.1.1; restricted for minors in Brazil and Australia | Hard pity (e.g. 80) plus a token path; disclose base, consolidated and pity rates; age gating | M | Disclosure screen exists; `economy_sim.py` shows p99 ≤ hard pity |
| R2 | **P0** | Ethics | Gacha power decides PvP rewards (monetized rivalry) | "Captains boost income … leaderboard ranks by income … top 100 get exclusive captains" | Pay-to-win plus chance is the most harmful combination; a spending feedback loop | Leaderboard by *skill metrics* (route efficiency ratio), brackets by harbor level, cosmetic rewards | M | Top-100 correlation with spend < 0.3 |
| R3 | **P1** | Ethics / motivation | Streak resets on a missed day (playing by appointment) | "Missing a day resets the streak" | Turns play into an obligation and punishes absence (it undermines autonomy) | Streaks that pause; claimable rewards accumulate for 7 days | S | D7 retention holds and complaints drop |
| R4 | **P1** | Loop / decisions | Few interesting decisions: routes run themselves | "Ships fly trade routes automatically" | Idle games still need choices (Meier); without them there's nothing to learn and engagement fades | Route planning with trade-offs: weather risk vs. speed, cargo demand shifts, captain traits that favor certain routes | M | Playtest: players can describe 2+ strategies |
| R5 | **P1** | Economy | Energy refill sold for gems caps play and sells removal of designed friction (pay to skip) | "5 voyages/day, refill 50 gems" | In an idle game, energy also blocks the core loop the player came for | Remove energy; let idle income cap at offline-time limits instead, and sell cosmetics or convenience | S | Session count per day rises without lower revenue per payer |
| R6 | **P2** | Ethics | 7-day limited banners in sequence (FOMO pressure) | "limited 7-day banner" | Repeated urgency pushes rushed spending | A published rotation schedule; banners return | S | Banner schedule visible in game |
| R7 | **P2** | Audience | Audience "everyone" | Pitch | Unfocused audience hurts tuning and marketing | Pick a core audience (e.g. cozy collectors: Completion, Fantasy, Design) | S | Persona plus top-3 motivations documented |
| R8 | **P2** | Progression | No sink stated for coins | No coin sinks in the pitch | Idle economies inflate without scaling sinks | Harbor upgrades with exponential cost; prestige ("found a new harbor") | M | `economy_sim.py` late In/Out about 1.0–1.2 |

**Quick wins (cost S):** R3, R5, R6, R7.

## Ethics and dark-pattern check

| Pattern | Status | Where | Healthy alternative |
|---|---|---|---|
| Undisclosed or misleading odds | **Present** | Captain gacha | Disclose base, consolidated and pity rates before purchase |
| Monetized rivalry (pay-to-win) | **Present** | PvP leaderboard by income | Skill-based ranking, brackets, cosmetic rewards |
| Playing by appointment | **Present** | Streak reset | Pausing streaks; accumulating claims |
| Pay to skip | **Present** | Energy refill | Remove energy; sell convenience that isn't required |
| FOMO pressure | **At risk** | 7-day limited banners | A published rotation; returning banners |
| Obfuscated pricing | **At risk** | Gems only, no real-money price shown | Show real-money prices; packs that match item prices |
| Grinding | Absent | — | — |
| Social pyramid scheme | Absent | — | — |

**Compliance notes:** before any soft launch, add probability disclosure (Korea, China,
Apple), an age gate with no paid random items for minors (Brazil from 2026; Australia M
rating), real-money pricing, a confirmation step on purchases, and the ESRB/PEGI random-items
labels.

## Questions for the designer

1. Is PvP essential to the fantasy, or would co-op harbor events serve it better?
2. What is the target session pattern: 3 check-ins of 3 minutes, or one 15-minute session?
3. Which captain traits could create route *decisions* rather than flat income boosts?
4. What revenue model would you accept if gacha power were removed from PvP?

## Next test

Paper-prototype 6 routes × 3 captain traits × 2 weather events. Pass if 5 of 8 playtesters
choose different route plans and can explain why.
