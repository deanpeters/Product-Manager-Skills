# Competitive Analysis Process — Worked Example

All companies, products, URLs, and figures are **fictional**. This example shows the umbrella
doing its actual job — **orchestration decisions**, not research mechanics. The research itself
lives in the worked examples of the delegated skills, which share this same scenario: Fieldlight,
a scheduling tool for trades businesses, deciding how to expand into field service management.
Follow the links to see each step's artifact in full.

**Invocation:** `Run the competitive analysis process on mid-market FSM software — decision:
whether Fieldlight expands into full FSM, and what the first module is. We have nothing yet.`

---

## The orchestration transcript (condensed)

**Step 0 — Scope.** The decision is two-part (enter? and with what module?), the competitor set is
unknown, and no prior intelligence exists. The orchestrator recommended:

> Based on your decision, here's the plan I recommend:
>
> 1. **Full six-step pass** — you're making an entry decision with no existing intelligence; skipping steps here means guessing (Recommended)
> 2. Steps 1, 2, 6 only — faster read if the deadline is this week, at the cost of the customer-voice and perception layers
> 3. Steps 1 and 2 only, decide, then backfill — fastest, riskiest
> 4. Something else
>
> Choose a number, or tell me your deadline and I'll re-scope.

User chose 1, with a note: "board meeting in three weeks." The orchestrator sequenced Steps 1-2 in
week one, 3-4 in week two, 5-6 plus outputs in week three.

**Step 1 — Landscape.** Delegated to `market-landscape-scan`
([its worked example](../../market-landscape-scan/examples/sample.md) is this run's artifact).
**Decision point resolved:** deep-dive on Wrenchline (the incumbent we'd collide with) and
DispatchCrow (running our playbook two years ahead). Vantiga FSM added at snapshot time for its
downmarket move. *Orchestration note:* the scan's vendor/buyer segmentation disagreement
(dispatcher-employment, not trade vertical) reframed the whole engagement — every later step
inherited that segment language.

**Step 2 — Product comparison.** Delegated to `competitive-research-snapshot`
([artifact](../../competitive-research-snapshot/examples/sample.md)). The JTBD lens earned its
mention: Wrenchline and DispatchCrow both "have scheduling," but a capability map by job showed
they serve different jobs — running a dispatcher's board vs. getting an owner off paper. Feature
parity theater, exposed.

**Step 3 — Customer-need fulfillment.** Delegated to `voice-of-customer-miner`
([artifact](../../voice-of-customer-miner/examples/sample.md)). The promise-delivery gap for
Step 5: Wrenchline promises "the operating system for the trades" while its own users' techs
resist the app that operating system runs on.

**Step 4 — Business baseline.** Delegated to `company-intel` per deep-dive competitor. *Orchestration
decision:* ran it on Wrenchline only — DispatchCrow's baseline was adequately covered by funding
coverage in the snapshot, and Vantiga's evidence quality was already flagged low; two more
eleven-section deep dives would have blown the three-week budget for one board slide. Skips are
recorded, not silent.

**Step 5 — Perception & positioning.** Contrasted Step 2's stated positioning against Step 3's
customer language. The uncontested space: nobody's *promise* speaks to the technician — every
vendor positions to the owner or dispatcher, while app stores prove the tech decides adoption.
Counter-move drafted with `positioning-statement`: Fieldlight as "the FSM your techs won't fight."

**Step 6 — Strategic direction.** Fused signals per the disciplines compendium: DispatchCrow's two
ex-Wrenchline dispatch hires (HUMINT) + "coming to Pro" capacity-view note (SIGINT) + payments
gate moved down-tier (SIGINT) = a committed bet on going upmarket while monetizing via payments —
three signals, one story, briefed as *act*. Wrenchline's Essentials tier + backfill-only hiring +
slowed changelog = margin defense, briefed as *monitor*. Cadence installed:
`competitive-intel-watch` monthly ([its worked example](../../competitive-intel-watch/examples/sample.md)
is run one).

**Step 7 — Outputs.**

| Output | Built | Owner / consumer | Fed by steps |
|---|---|---|---|
| Battle card: Fieldlight vs Wrenchline | ✅ ([artifact](../../battle-card-builder/examples/sample.md)) | sales | 2, 3, 5 |
| Executive comparison matrix | ✅ (Step 2's matrix, lifted for the board deck) | exec staff | 2 |
| Positioning counter-move | ✅ ("the FSM your techs won't fight") | PMM | 3, 5 |
| Threat assessment brief | ✅ (DispatchCrow: act; Wrenchline: monitor; Vantiga: ignore-with-tripwire) | leadership | 6 |

**Maintenance cadence installed:** monthly `competitive-intel-watch`; `pricing-packaging-tracker`
monthly on the same set; quarterly direction re-read.

---

## Why this example works

- **The value shown is orchestration, not research.** Every research artifact lives in a delegated
  skill's own example; what this document adds is the sequencing, the scoping menu, and the skips.
- **Skips are decisions with reasons.** Step 4 ran on one competitor, not three — recorded with the
  budget logic. "Permission to skip" is the orchestrator's gift; silent skipping is its failure mode.
- **Findings compound across steps.** The scan's segmentation insight renamed Step 2's comparison
  axes; Step 3's app-store voice became Step 5's uncontested space; Step 6 stacked three disciplines
  into one "act" call. Six lenses, one narrative.
- **It ended by installing a cadence.** The engagement closes with watches scheduled — the
  difference between a process that ended and one that just stopped.
