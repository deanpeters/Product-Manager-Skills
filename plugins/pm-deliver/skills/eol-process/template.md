# EOL Process Template

A one-page tracker for a sunset in flight. Fill the level first — it sizes everything below.
Quality checks at the bottom.

## Provenance
Orchestrates the EOL prompt series in the
`https://github.com/deanpeters/product-manager-prompts` repo.

---

## Set the level first

| | Level 1 — Light | Level 2 — Standard | Level 3 — Heavy |
|---|---|---|---|
| Scope | Feature, internal tool, API | Commercial product, active customers | Revenue-critical, hardware, regulated |
| Elapsed time | Days to weeks | 6-12 months | 12-24 months |
| Phases 2-4 | Often one sitting | Distinct, sequential | Separate workstreams |

**Most sunsets are Level 2.** Never default to Level 3.

---

## Template

```markdown
## EOL Process Tracker: [Product Name]

**Level**: [1-Light / 2-Standard / 3-Heavy]
**Landing place**: [Replacement / Migration / Graceful exit] -- [Ready / Gap / Not started]
**Current phase**: [1-6]
**Target announcement date**: [date]
**Target EOL date**: [date / TBD / Not scheduled]

---

### Phase 1: Decide                        Status: [ ] Not started [ ] In progress [ ] Done
**Skill**: eol-readiness-advisor

- Trigger: [what actually prompted this]
- Verdict: [Go / Go-with-conditions / Hold / Harvest]
- Condition (if any): [what must be true before announcing]
- Obligations to check: [contracts, SLAs, regulatory, lifetime promises]

**DP1**: Go, and is the landing place real?
- [ ] Verdict is Go or Go-with-conditions
- [ ] Landing place named and readiness assessed
- [ ] If landing place is not ready: Phase 5 is blocked -- noted

---

### Phase 2: Align                         Status: [ ] Not started [ ] In progress [ ] Done
**Skill**: eol-stakeholder-sequence

| # | Stop | Held? | What it surfaced |
|---|---|---|---|
| 1 | [Legal] | [ ] | [finding] |
| 2 | [Finance] | [ ] | [finding] |
| 3 | [Sales] | [ ] | [field commitments found] |
| ... | | | |

**DP2**: Did anything invalidate the decision?
- [ ] No blocking contract, regulation, or commitment
- [ ] Landing place still holds after the difficult-customer stop
- [ ] If either failed: returned to Phase 1 -- date/scope/verdict revised

---

### Phase 3: Plan                          Status: [ ] Not started [ ] In progress [ ] Done
**Skill**: eol-checklist

- Gates in scope: [list]
- Gates deliberately excluded: [list + why]
- Enablement complete by: [date]  <-- must precede announcement
- Announcement date: [date]

**DP3**: Every item owned, every date real?
- [ ] No unowned items
- [ ] No invented dates (TBD or Not scheduled + precondition instead)
- [ ] Data, contracts, access, money all covered
- [ ] Phase 6 review on the checklist with an owner

---

### Phase 4: Prepare                       Status: [ ] Not started [ ] In progress [ ] Done
**Skill**: eol-internal-enablement

- Materials built: [FAQ / sales points / objections / escalation / channel / training]
- Escalation owners: L1 [name] L2 [name] L3 [name] Exec [name]
- Partners briefed on: [date] (L3)

**DP4**: Enablement complete? THIS GATES THE ANNOUNCEMENT
- [ ] A rep can name who to call about a churn threat
- [ ] A rep can answer the hardest objection out loud
- [ ] Every offer in the pack is pre-approved with a limit
- [ ] Support has the pack before customers hear anything

---

### Phase 5: Announce                      Status: [ ] Not started [ ] In progress [ ] Done
**Skill**: eol-message

- Size: [Brief / Standard / Full]
- Path: [Replacement / Migration / Graceful exit]
- Segments: [list variants sent]
- Comms calendar: [dates across gates, not one send]

**DP5**: Does it survive contact?
- [ ] Legal has read it
- [ ] Consistent with field commitments found in Phase 2
- [ ] Support received it first, with lead time
- [ ] Passes the sticky-note test

---

### Phase 6: Close                         Status: [ ] Not started [ ] In progress [ ] Done

- Gates closed: [list with sign-off dates]
- Transition/migration final: [X of Y accounts]
- Retention vs. forecast: [actual vs. target]

**Closure items**
- [ ] Data exports honored; deletion scheduled
- [ ] Contracts settled, non-renewals confirmed in writing
- [ ] Revenue recognition closed
- [ ] Infrastructure decommissioned; documentation archived
- [ ] **Lessons-learned review written**
- [ ] Deferred decisions (e.g. unscheduled EOL) owned with a review date

**DP6**: Is this actually closed?
- [ ] Data settled, contracts closed, money recognized, review written

---

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
```

---

## Quality checks

Any "no" is a rewrite, not a nitpick.

**Sequence**
- [ ] Phase 5 was not the first artifact built
- [ ] DP2 was treated as a real gate — findings changed the plan or were explicitly cleared
- [ ] DP4 gates DP5 on the plan, with separate dates

**Proportion**
- [ ] Level set in Phase 1 and used to size every later phase
- [ ] Level 1 sunsets did not get Level 3 ceremony
- [ ] Skipped phases were skipped deliberately, with a reason recorded

**Honesty**
- [ ] No EOL date was invented to fill a blank
- [ ] The landing place status is recorded truthfully, including "not ready"
- [ ] Field commitments from Phase 2 are reflected in the Phase 5 message

**Closure**
- [ ] Phase 6 has an owner named back in Phase 3
- [ ] The lessons-learned review is written, not just scheduled
- [ ] Any unscheduled EOL has a precondition and a named owner

**The outcome that matters**
- [ ] Retention is tracked as the success measure — not checklist completion
- [ ] You can answer: did we lose the product without losing the customer?
