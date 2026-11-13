# EOL Process Example — SaaS

**Product:** Fieldlight Classic Dispatch
**Level:** 2 — Standard · **Elapsed:** ~12 months, decision to closure
**Context:** ~800 accounts, $2.4M ARR, annual contracts, sold direct. Replaced by Fieldlight Next
Scheduling. ~30 accounts use custom dispatch rules that don't carry over.

This example runs all six phases in order — the clean case. The industrial example shows what
happens when Phase 2 sends you backwards.

---

```markdown
## EOL Process Tracker: Fieldlight Classic Dispatch

**Level**: 2 -- Standard
**Landing place**: Replacement (Fieldlight Next) -- Gap: custom dispatch rules
**Current phase**: 6 (complete)
**Target announcement date**: March 1, 2026
**Target EOL date**: December 31, 2026

---

### Phase 1: Decide                        Status: [x] Done  (Nov 2025)

- Trigger: Support cost. Classic drove ~40% of support volume on ~15% of revenue
- Verdict: Go-with-conditions
- Condition: the ~30 custom-rule accounts need a named plan before announcement
- Obligations to check: 800 annual contracts, renewal date language, platform SLA scope

**DP1**: Go, and is the landing place real?
- [x] Verdict is Go-with-conditions
- [x] Landing place named: Fieldlight Next, at parity except custom rules
- [x] Landing place gap noted -- Phase 5 gated on the custom-rule plan

---

### Phase 2: Align                         Status: [x] Done  (Dec 2025 - Jan 2026)

| # | Stop | Held? | What it surfaced |
|---|---|---|---|
| 1 | Legal | [x] | No Classic-specific terms. SLA is platform-wide. Date cleared |
| 2 | Finance | [x] | Classic ARR is $2.4M. Retention target set at 90% |
| 3 | Sales | [x] | Two accounts told "Classic supported indefinitely" -- unwind needed |
| 4 | Marketing | [x] | Q1 webinar featured Classic. Pulled |
| 5 | CS | [x] | 6 of the 30 custom-rule accounts already at renewal risk |
| 6 | Difficult customers (3) | [x] | Two undocumented v1 API integrations found |
| 7 | Engineering | [x] | Internal billing job reads Classic dispatch data |
| 8 | Support | [x] | Needs 2 temp headcount for the March-June window |

**DP2**: Did anything invalidate the decision?
- [x] No blocking contract, regulation, or commitment
- [x] Landing place still holds -- gap is real but bounded and funded
- [x] Two field commitments logged for individual handling
- Decision unchanged. Date held.

---

### Phase 3: Plan                          Status: [x] Done  (Jan 2026)

- Gates in scope: NSC, EOS, EOE, EOM, EOL
- Gates deliberately excluded: EOR (annual contracts expire naturally);
  EOSRV (SaaS -- no post-EOL service obligations)
- Enablement complete by: February 20, 2026  <-- precedes announcement
- Announcement date: March 1, 2026

**DP3**: Every item owned, every date real?
- [x] No unowned items
- [x] All dates defensible; none invented
- [x] Data (90-day export window), contracts (Legal cleared), access (v1 API
      consumers inventoried), money (Q4 reforecast) all covered
- [x] Phase 6 review on the checklist -- Owner: Product

---

### Phase 4: Prepare                       Status: [x] Done  (Feb 2026)

- Materials built: Support FAQ, sales talking points, objection handling,
  escalation playbook
- Escalation owners: L1 Support team, L2 Priya, L3 Marcus, Exec Dana
- Partners briefed: n/a (sold direct)

**DP4**: Enablement complete?
- [x] Reps could name the escalation owner unprompted
- [x] Role-played the "we just renewed" and "no custom rules" objections
- [x] Offers pre-approved: priority slots, 1-on-1 rebuilds, exec call over $25K ARR
- [x] Support had the pack Feb 20, nine days before announcement

---

### Phase 5: Announce                      Status: [x] Done  (March 1, 2026)

- Size: Standard
- Path: Replacement
- Segments: all-accounts email; separate note to the 30 custom-rule accounts
  sent 48 hours earlier by their CSMs
- Comms calendar: Mar 1 announcement, May 15 EOE reminder, Sep 1 EOM reminder,
  Nov 15 final export notice, Dec 15 last call

**DP5**: Does it survive contact?
- [x] Legal reviewed the contract and refund language
- [x] Consistent with Phase 2 findings -- the two "indefinite support" accounts
      were called individually before the blast
- [x] Support had it first
- [x] Passes the sticky-note test: migrate at fieldlight.com/next-migration
      before December 31

---

### Phase 6: Close                         Status: [x] Done  (March 2027)

- Gates closed: EOS Mar 1, EOE Jun 1, EOM Oct 1, EOL Dec 31 -- all signed off
- Transition final: 781 of 800 accounts migrated
- Retention vs. forecast: 94% ARR retained against a 90% target

**Closure items**
- [x] Exports available through March 31, 2027; deletion scheduled April 2027
- [x] Contracts settled; no disputes
- [x] Revenue recognition closed December 31
- [x] Classic infrastructure decommissioned January 2027
- [x] Lessons-learned review written -- Owner: Product
- [x] No deferred decisions

**DP6**: Is this actually closed?
- [x] Data settled, contracts closed, money recognized, review written

---

### Lessons learned (excerpt)

- The difficult-customer stop paid for the whole process. Two undocumented v1
  API integrations would have broken at EOE and generated a public incident.
- We under-invested in Phase 4 sales enablement. Sales asked for the comparison
  table twice before we produced one with the gaps included; the first version
  had no gaps and they stopped trusting it.
- 19 accounts never migrated and churned. 11 of them were in the custom-rule
  segment. The 1-on-1 rebuild offer went out too late -- it should have been in
  the March 1 announcement, not the May reminder.
- Next time: start the custom-segment outreach before the general announcement,
  not 48 hours before.

### Assumptions to Validate (from Phase 1, resolved)
- Support volume estimate of 40% -- measured at 37%, close enough
- Custom-rule account count of ~30 -- actual was 34
```

---

## What to notice

- **DP2 cleared explicitly rather than silently.** The tracker records "Decision unchanged. Date
  held." Even when nothing blocks, saying so is what makes the gate real rather than decorative.
- **The gap survived all the way to the outcome.** Custom dispatch rules appear in Phase 1 as a
  condition, Phase 2 as a risk (6 of 30 at renewal risk), Phase 4 as an objection with a pre-approved
  offer, Phase 5 as a segmented send — and in Phase 6 as 11 of the 19 churned accounts. The thing
  most likely to hurt you should be traceable through every phase.
- **Retention is the reported outcome, not completion.** 94% against a 90% target. Checklist
  completion would have read as 100% and taught nobody anything.
- **The lessons-learned review is critical of the process that produced it.** Naming the late
  1-on-1 offer as the cause of 11 churned accounts is the entire value of Phase 6. A review that
  concludes "went well" is a review that didn't happen.
