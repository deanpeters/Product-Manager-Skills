# PRD Example — Industrial

A PRD excerpt for **Northfield Automation's** NFA-500 remote firmware update capability, written
during the platform's development.

**Why hardware changes the PRD:** you cannot patch a decision after tooling. Certification is a
gate, not a task. And "we'll fix it in the next release" doesn't exist when the release is a
physical unit already bolted into a customer's panel.

That pushes rigor forward. The assumptions and open questions that a SaaS PRD can resolve during
build have to be resolved *before* it.

---

### Section 2 — Problem Statement

**Who Has This Problem?**

Northfield field service technicians supporting installed NFA-500 units, and the plant maintenance
staff who wait for them. A typical tech covers 40+ installations across a multi-state territory.

**What Is the Problem?**

Firmware updates require an on-site visit. A 20-minute patch costs a day of travel, so non-critical
updates get deferred indefinitely. As of March 2026, **62% of installed units are more than two
firmware revisions behind** `[EVIDENCE: service database export, 2026-03-01]`.

The consequence isn't only cost. Deferred updates mean the installed base fragments, so every
support call starts with "which firmware are you on?" and reproduction becomes guesswork.

**Why Does It Matter Now?**

The NFA-500 is the successor platform for the NFA-200 line, and the installed base will grow ~4x
over three years `[ASSUMPTION: based on the replacement plan's adoption curve — not yet validated
against actual order rates]`. The manual-update model does not scale to that base.

---

### Section 3 — Goals and Non-Goals

**Goals**
1. Apply a firmware update to an enrolled unit without an on-site visit
2. Reduce median firmware lag from 2+ revisions to under 1
3. Preserve the safety property that a failed update never leaves a line un-runnable

**Non-Goals**
- Automatic or unattended updates. Every update is operator-initiated. `[DECISION: plants must
  control when their line's controller changes state — automatic updates were rejected in review]`
- Updates to units not enrolled in remote management
- Configuration changes over the same channel. Firmware only, this release.

**Open Question**
`[OPEN: does remote firmware update affect UL 508A listing? Regulatory review requested
2026-03-12, blocking — see Section 8]`

---

### Section 5 — Requirements

**R1 — Operator-initiated update during a maintenance window**
The console shall permit a firmware push only when the target unit reports a scheduled maintenance
window or a stopped line. Pushing to a running line shall be refused with the next available window
shown.

**R2 — Automatic rollback on failure**
If an update fails to complete or connectivity drops mid-apply, the unit shall restore the previous
firmware and resume normal operation without manual intervention.
`[This is the requirement the feature exists to satisfy. A controller that bricks mid-update stops a
production line, and there is no undo from a service console 400 miles away.]`

**R3 — Audit trail**
Each update shall record operator identity, timestamp, prior version, and new version, retained and
exportable. `[EVIDENCE: three of five pilot customers operate under quality systems requiring change
records — customer interviews, Feb 2026]`

**R4 — Offline units are not blocked**
Units without connectivity shall remain updatable by the existing on-site method with no change to
that path. `[ASSUMPTION: ~35% of installations will never have panel-level connectivity — needs
validation against the site survey]`

---

### Section 8 — Dependencies and Gates

| Gate | Owner | Status | Blocks |
|---|---|---|---|
| UL 508A impact assessment | Regulatory | **Open** | All firmware work |
| Bootloader rollback support | Firmware Eng | In progress | R2 |
| Console enrollment flow | Platform | Not started | R1 |
| Site connectivity survey | Field Service | In progress | R4 assumption |

**Hard sequencing note:** the UL assessment gates everything. If remote update alters the listing,
the design changes materially and the schedule resets. **No engineering beyond the bootloader
spike until that assessment returns.**

---

### Section 9 — Success Metrics

- **Primary:** median firmware lag under 1 revision across enrolled units, 12 months post-release
- **Secondary:** on-site visits attributable to firmware drop by 70%
- **Guardrail:** zero units rendered un-runnable by a remote update. **Any occurrence halts the
  feature**, regardless of the primary metric.

---

## What this example teaches that the SaaS PRD can't

- **A regulatory gate can stop all work, and the PRD says so in bold.** The UL assessment isn't a
  task in a backlog — it's a condition that determines whether the feature is legal to ship. Burying
  it in a dependency list would have let engineering start and waste the spend.
- **The rollback requirement carries a rationale in-line.** R2 explains *why* it's non-negotiable,
  because a reviewer skimming requirements would otherwise read it as ordinary error handling.
- **A non-goal encodes a rejected decision, with the reason.** "Automatic updates were rejected in
  review" prevents the idea returning every quarter as a fresh suggestion.
- **R4 protects the users you're not building for.** ~35% of sites will never have connectivity;
  the PRD guarantees their path doesn't regress. In SaaS everyone gets the new version — in the
  field, most of your installed base may not.
- **The guardrail is absolute, not weighed.** "Any occurrence halts the feature." When failure means
  a stopped production line, the guardrail outranks the goal.
- **Assumptions carry validation plans, not just tags.** `[ASSUMPTION: ~35%...]` names the survey
  that will resolve it, because on hardware timelines an unresolved assumption becomes a tooling
  decision.
