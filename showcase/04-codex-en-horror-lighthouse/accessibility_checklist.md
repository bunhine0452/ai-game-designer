# Low Tide — chapter accessibility checklist

Status: draft requirements, not implementation certification. Owner: accessibility/QA lead (role); delivery shared with level design, audio, VFX, UI and input teams. Updated: 2026-10-30. Applies to the revised 40 min PC/console chapter. All boxes are intentionally unchecked pending build verification. Any numbers below are proposed project acceptance targets unless attributed to a source.

Principle: water, keeper behavior and beacon logic stay legible through equivalent channels. Preserve uncertainty about the story without hiding information needed to act. Settings must not add spoilers before equivalent information is perceptible in ordinary play. Assist use must not remove story content or penalize rewards.

## Audio cues — audio, UI and level design owners

Use redundant sensory channels for critical cues, following [XAG 103](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/103). Haptics may supplement the visual alternative but cannot be the only substitute.

| Check | Chapter requirement | Acceptance test |
|---|---|---|
| [ ] | Keeper approach at 8, 16, 30 and 32 min: footsteps/scrape paired with an optional directional threat indicator and captions such as `[Heavy footsteps — behind, closing]`. | Complete each encounter with audio muted and vibration off; verify cue onset, direction and urgency are equivalent. No exact through-wall enemy marker unless separately enabled as an assist. |
| [ ] | Water rise, sluice open/closed and pump completion have distinct icons/text and readable physical state changes. Do not use pitch or color alone. | Muted play identifies every state; captions remain readable against moving water. |
| [ ] | Radio hook at 2 min conveys the anticipatory phrase through subtitles as well as voice. Display radio source and player reply in the same order as heard. | Muted player can explain what was impossible; subtitle does not reveal reply early. |
| [ ] | Shutter alignment and final tether sever at 28–38 min have stable progress/state indicators; the rescue call sign is written in the journal. | Solve with mono audio and then muted audio without guessing rhythm or remembering a pitch sequence. |
| [ ] | Separate master, dialogue, music, ambience and critical-effects volumes; mono output; dynamic-range choices including reduced peaks. Prevent ambience/stingers from masking instructions. | Test speakers, headphones, mono and low volume. Verify lowering music leaves threat cues and captions usable; volume preview is opt-in and starts gently. |
| [ ] | Optional haptics independently adjustable/off; no essential controller speaker cue. A visual or text alternative exists on keyboard/mouse. | Finish final escape with all vibration and controller speaker audio off. |

## Flashing, light and motion — VFX/rendering owners

[XAG 118](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/118) recommends avoiding harmful flashing and patterns and testing all games, including unintended triggers. A warning or reduced-flash toggle alone does not establish safety.

- [ ] Audit rotating beam reflections, lens shutters, lightning, sparks, water caustics, high-contrast stair rails and damage/death/reload transitions. Do not rely on a simple flash-frequency limit: area, luminance, saturated red, repeated exposure and spatial patterns matter.
- [ ] Replace mandatory strobing with steady state changes and gradual light ramps in the default presentation. The reduced-flashing setting additionally suppresses incidental lightning bursts, sparks and sharp beam glare without concealing keeper or puzzle information.
- [ ] Offer reduced flashing before any animated lighthouse intro. Menu previews must obey the selected mode immediately. Keep startup logos and loading screens within the same review scope.
- [ ] Capture and analyze worst-case gameplay and cinematics with a suitable photosensitivity analysis tool and qualified review. Record build, tool/version, settings, scene and findings; fix failures and recapture before approval. Test default and reduced modes across shipped HDR/SDR modes, frame-rate targets, brightness ranges and supported displays/platforms.
- [ ] Provide independent options to disable camera shake, head bob, motion blur, film grain, chromatic effects and forced lens sway. Offer adjustable field of view where supported, with platform-appropriate performance validation.
- [ ] Underwater distortion, rotating lens and rising stairs do not force camera roll. Offer a stable reticle and reduced water distortion. Test the full stair/chase route with these options, not just stationary scenes.
- [ ] Reduced effects retain equivalent threat and state cues: shutter status uses a persistent icon/label; keeper breach uses silhouette and directional cue; water danger uses marked tide rise. No timing information depends on a flashing light.

## Controls — input, gameplay and UI owners

Offer alternatives to demanding inputs as described by [XAG 107](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/107). Remapping alone does not address speed, hold or precision barriers.

- [ ] Fully remap keyboard/mouse and supported controller gameplay actions, including interact, sprint, crouch, journal, pause and lens manipulation. Update all prompts/tutorials after remapping; detect conflicts and offer a recoverable reset.
- [ ] Menus work with keyboard alone, mouse and controller D-pad/buttons, without requiring dragging or simultaneous presses. Keep focus visible; ensure no remap can strand the player in settings.
- [ ] Sprint, crouch and interaction offer toggle alternatives. Valves and winches use one press to begin/stop with clear progress; no compulsory mash, repeated rotation gesture or prolonged hold. No mandatory breath-hold input.
- [ ] Sluice, shutter and tether interactions have generous targets and an optional interaction snap/auto-align assist. Final tether cut is a single deliberate press; no surprise quick-time event or required multi-button chord.
- [ ] Provide separate camera X/Y sensitivity, axis inversion and controller dead-zone controls, plus a digital step alternative for lens rotation. Adaptive controllers can trigger all required actions without gyro, touchpad or analog-trigger precision.
- [ ] Optional extended reaction windows, slower pursuit, untimed puzzle operation and route guidance are separate, clearly explained assists. Changes apply during play and persist across checkpoints; allow bypassing a repeatedly failed chase after an explicit player choice.
- [ ] Controller disconnect pauses simulation and preserves progress; reconnecting and changing input mode refresh prompts without moving the player. Test suspend/resume on each target console and PC focus-loss behavior.
- [ ] Pause freezes water, threat and timed interactions, including the final escape. No time pressure on logs, tutorials or settings. Checkpoint reload restores already solved puzzles and required items.

## Subtitles and captions — narrative, localization and UI owners

Speech subtitles and non-speech captions cover different information; provide both. This follows [XAG 104](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/104).

- [ ] Subtitles are on by default and configurable before the first scene; offer full sound captions at setup. Cover radio, whispers, player speech, distant dialogue, cinematics and final rescue. Distortion never makes required words unreadable.
- [ ] Identify speakers and source (`Unknown voice — radio`) without naming the keeper or explaining the mystery before narrative discovery. Include direction for offscreen sounds when it matters to play.
- [ ] Support font size, background opacity, outline and positioning/safe-area adjustments. Test largest text without clipping or overlap with lens status, interaction prompts or directional indicators on every supported aspect ratio and language.
- [ ] Project target: default subtitle glyph height at least 32 px at 1080p, scalable to at least 48 px and proportionally with resolution. Validate actual readability at console couch distance and PC monitor distance with low-vision participants; adjust based on findings.
- [ ] Project target: text/background contrast at least 4.5:1 using a controllable backing panel, including against white beam glare and dark moving water. Speaker identity and urgency use words/icons as well as color.
- [ ] Break subtitles at meaningful phrases, synchronize with speech and avoid exposing unheard future lines. Prevent simultaneous radio/keeper captions from obscuring each other; prioritize actionable threat information and retain displaced dialogue in a replayable transcript.
- [ ] Keep logs/tutorial text player-paced and replayable. Journal contains pump lesson, rescue call sign and current objective. Optional dialogue history can be read while paused; it must not substitute for timely threat captions.
- [ ] Localization QA checks reading time, line wrapping, long names, right-to-left presentation where supported, glyph coverage and largest text. Verify captions survive death/reload without duplicated, skipped or stale threat notices.

## Supporting chapter basics — UI and level design owners

Based on the [Game Accessibility Guidelines checklist](https://gameaccessibilityguidelines.com/full-list/), include these alongside the four requested areas.

- [ ] All access settings are reachable before gameplay, previewable, saved per profile and available from pause. Changing assists does not erase progress or silently change other settings.
- [ ] Gameplay meaning never relies on color alone. Pump valves have symbols and labels; water hazard edges and tether remain distinguishable in glare and darkness. Include optional interactable/high-contrast outlines rather than relying on global color filters.
- [ ] HUD/body text scales; objectives and tutorials can be revisited. Mark current route state in a simple journal diagram; offer hints on demand rather than automatically spoiling exploration.
- [ ] Include a clear pre-chapter content description for drowning imagery, confinement and pursuit. Explain what reduced-flash/reduced-motion settings change without claiming the chapter is safe for everyone.
- [ ] Verify safe-room boundaries and checkpoint restores consistently. A player who pauses, uses captions or takes longer to read must not lose the intended recovery opportunity.

## Verification matrix and sign-off

| Pass | Coverage | Evidence to retain |
|---|---|---|
| Muted and mono | All critical scenes; vibration off for muted pass | Cue inventory, missed information, caption timing captures |
| Motor access | Keyboard-only menus, remapped pad, adaptive controller; toggle and assisted chase modes | Completion/blockers for valves, shutter, final cut; prompt captures |
| Low vision/readability | Largest text, high contrast, glare/water, couch and desktop distances | Clipping/overlap results, participant feedback, settings used |
| Sensory effects | Every beam/flash scene and transitions in supported render modes | Tool reports, reviewed captures, reviewer, fixed defect references |
| Persistence | Checkpoint reload, quit/resume, suspend, disconnect and input change | Settings/state comparison and any regressions |
| Combined settings | Muted + captions + largest text + reduced effects + remapped toggle controls | Whole-chapter completion and interface conflicts |

Track each unchecked item as a build ticket. Record owner, build/platform, test settings, result and linked evidence. Design review cannot close an implementation checkbox. Release candidate acceptance target: no unresolved progression blockers in these configurations, all critical cues have tested alternatives, and photosensitivity review has no outstanding failures. Recruit disabled players for usability sessions and incorporate findings; simulations alone do not establish accessibility. These references guide design and testing; this checklist is not a platform certification claim.

Change log: 2026-10-30 — initial chapter-specific requirements and QA plan, aligned to revised beats.
