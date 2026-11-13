# Roadmap Example — Industrial

Annual roadmap planning at **Northfield Automation** for the NFA-500 control platform.

**Why hardware changes roadmapping:** tooling has lead times measured in months, certification
windows are fixed by a third party, channel partners commit inventory a year out, and the previous
generation is still under service contract. The roadmap has to carry the *old* product's wind-down
alongside the new one's growth.

---

## Example: NFA-500 annual roadmap

**Context:** Second year of NFA-500 availability. The NFA-200 replacement play is underway — End of
Sale is set for March 2027 with service obligations running to December 2028. Eight channel partners
resell both.

---

**Phase 1 — Gather Inputs**

- **Business goals:** NFA-500 to 60% of new orders (from 35%); free the NFA-200 manufacturing line
  by Q2 2027; hold service margin through the wind-down
- **Customer problems:** field diagnosis time; firmware lag across the installed base; integrators
  carrying three controller families because the range doesn't cover their bid spread
- **Technical:** bootloader rollback for remote update; I/O module range gap at high channel counts
- **Regulatory:** UL 508A reassessment required if remote update alters the listing — **assessment
  pending, gates everything downstream**
- **Channel:** partners need last-time-buy quantities for the NFA-200 by Q1 2027 to plan inventory
- **Constraint nobody could move:** injection tooling for a new module housing is a 14-week lead
  time, and the tooling vendor's next open slot is August

**Phase 2 — Define Epics**

- **E1 — Remote firmware update** (fixes installed-base fragmentation; gated on UL)
- **E2 — On-unit fault isolation** (the diagnosis-time problem; validated in discovery)
- **E3 — High-channel-count I/O module** (closes the integrator range gap; needs new tooling)
- **E4 — NFA-200 End-of-Sale execution** (not a feature, but it consumes real product and channel
  capacity — see [`eol-checklist`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/eol-checklist/SKILL.md))
- **E5 — Integrator configuration reuse** (reduces commissioning time; software only)

**Phase 3 — Prioritize**

- Ran `prioritization-advisor`. RICE was abandoned within ten minutes: it kept ranking E3 highly
  while ignoring that missing the August tooling slot pushes it a full year
- Switched to **constraint-first sequencing** — order by what has an immovable external date, then
  prioritize what's left:
  - **E3 tooling decision** must be made by June regardless of its RICE score (14-week lead + August
    slot). Decide early or lose a year.
  - **E1 blocked** until the UL assessment returns. Cannot be scheduled, only reserved.
  - **E4 has a fixed external date** — EOS March 2027, and partners need numbers by Q1.
  - E2 and E5 are software-only and genuinely reschedulable. **They are the only real flexibility on
    the board.**

**Phase 4 — Sequence**

| Quarter | Committed | Notes |
|---|---|---|
| Q1 | E4 (partner last-time-buy, EOS comms) · E2 (fault isolation) | E4 is date-driven; E2 is the validated customer win |
| Q2 | E3 tooling decision + order · E2 ships | Tooling ordered by June or E3 slips to next year |
| Q3 | E1 (if UL clears) · E5 | E1 reserved, not committed |
| Q4 | E3 module launch · E4 (EOS execution) | Tooling arrives ~14 weeks post-order |

- **E1 is shown as reserved, not committed.** Sales was explicitly told "reserved" means it may not
  happen this year
- **E5 is the designated shock absorber.** When something slips — something always slips — E5 moves
  first, and everyone knows that in advance

**Phase 5 — Communicate**

- **Internal:** the constraint logic, not just the sequence. Engineering needed to know *why* the
  tooling decision outranks a higher-scoring epic
- **Channel partners:** E4 dates and last-time-buy windows, 25 days before public notice. They plan
  inventory on this
- **Customers:** E2 and E5 by quarter; E1 as "in development, no date," because promising a date
  gated on a third-party assessment is how you lose credibility
- **Explicitly not communicated:** E3's tooling risk. Internal decision, no customer-facing
  commitment until tooling is ordered

---

## What this example teaches that the SaaS roadmap can't

- **A scoring framework was tried and abandoned, on the record.** RICE ranked E3 highly while blind
  to the fact that a June decision date controls a Q4 delivery. When external lead times dominate,
  constraint-first sequencing beats scoring — and knowing *when* to drop the framework is the skill.
- **Some items can be reserved but not committed.** E1 depends on a regulatory answer nobody at
  Northfield controls. Putting it on the roadmap as committed would be fiction; leaving it off would
  hide real planned capacity.
- **The retiring product is on the roadmap.** E4 ships no features and consumes real capacity across
  product, channel, and service. Roadmaps that only show new work systematically under-plan the
  quarter a sunset lands in.
- **One epic is designated the shock absorber, publicly.** Naming E5 as the thing that moves first
  means slippage becomes a known plan rather than a renegotiation.
- **Different audiences get different roadmaps, deliberately.** Partners get dates they plan
  inventory against. Customers get "in development, no date" for the gated item. Nobody outside
  hears about the tooling risk. That isn't spin — it's matching commitment level to what each
  audience will act on.
