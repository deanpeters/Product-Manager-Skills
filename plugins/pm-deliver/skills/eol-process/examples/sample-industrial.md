# EOL Process Example — Industrial

**Product:** NFA-200 series retrofit controller (Northfield Automation)
**Level:** 3 — Heavy · **Elapsed:** ~30 months and still running
**Context:** ~120 installations, 8 channel partners, service contracts through 2028, UL 508A and CE
certified. NFA-500 is the successor but needs a different mounting bracket — every migration is a
scoped site visit.

**Why this example exists:** the SaaS example runs the six phases in order. This one shows the loop
— **Phase 2 sent the process back to Phase 1, and the outcome changed** from "retire the NFA-200"
to "stop selling it, keep servicing it, and fund the retrofit path first." That backwards step is
the process working.

---

```markdown
## EOL Process Tracker: NFA-200 Series Retrofit Controller

**Level**: 3 -- Heavy
**Landing place**: Replacement (NFA-500) -- NOT READY: no drop-in retrofit path
**Current phase**: 6 (in progress -- service obligations run to Dec 2028)
**Target announcement date**: March 31, 2026
**Target EOL date**: Not scheduled

---

### Phase 1: Decide  (first pass)          Status: [x] Superseded  (Oct 2025)

- Trigger: Internal only. Manufacturing wanted the NFA-200 line reallocated
- Verdict (first pass): Go -- retire the NFA-200, migrate the base to NFA-500
- Obligations to check: service agreements, UL/CE certification, spare parts,
  8 channel partner agreements

**DP1**: Go, and is the landing place real?
- [x] Verdict is Go
- [ ] Landing place readiness -- ASSUMED ready, not verified
- Note: this assumption is what Phase 2 broke

---

### Phase 2: Align                         Status: [x] Done  (Nov 2025 - Feb 2026)

| # | Stop | Held? | What it surfaced |
|---|---|---|---|
| 1 | Legal (contracts) | [x] | Service agreements run to Dec 2028. Not terminable |
| 2 | Regulatory | [x] | Certification unaffected, but 14 sites run validated processes |
| 3 | Finance | [x] | Service revenue through 2028 is material. Spares carry cost modest |
| 4 | Operations / Supply Chain | [x] | Spares coverage to 2028 feasible with one final buy |
| 5 | Executives | [x] | See DP2 -- the ask changed here |
| 6 | Sales | [x] | Three customers mid-standardization on NFA-200 across sites |
| 7 | Channel partners (8) | [x] | Two partners holding stock; one mid-bid on a project |
| 8 | Service org | [x] | Can staff to 2028; two techs retire in 2027 |
| 9 | Key accounts (3) | [x] | Retrofit needs a production shutdown at 2 of 3 sites |
| 10 | Engineering | [x] | Retrofit bracket designable, ~9 months, unfunded |
| 11 | Marketing | [x] | Held pending decision |

**DP2**: Did anything invalidate the decision?
- [ ] No blocking contract, regulation, or commitment  <-- FAILED
- [ ] Landing place still holds                        <-- FAILED
- **Returned to Phase 1.** Two findings broke the original verdict:
  1. Service agreements to Dec 2028 cannot be terminated (obligation lock)
  2. NFA-500 is not a drop-in -- 120 site visits, 2 of 3 sampled sites need a
     production shutdown, and the bracket work is unfunded (no landing place)

---

### Phase 1: Decide  (second pass)         Status: [x] Done  (Feb 2026)

- Trigger restated honestly: manufacturing capacity, not customer need
- Verdict: **Hold on EOL. Go on End of Sale.**
- Reasoning: EOS returns the manufacturing line -- which was the actual ask --
  without committing to a shutdown date we cannot keep
- Condition: fund the retrofit bracket work as the precondition to ever
  scheduling an EOL
- Precondition to schedule EOL: validated retrofit path with per-site cost,
  plus installed base below 20 units

**DP1 (second pass)**: Go, and is the landing place real?
- [x] Verdict is Go-with-conditions, scoped to End of Sale only
- [x] Landing place honestly recorded as NOT READY
- [x] Phase 5 permitted for an EOS announcement; an EOL announcement is blocked

---

### Phase 3: Plan                          Status: [x] Done  (Mar 2026)

- Gates in scope: NSC, EOS, EOE, EOR, EOM, EOSRV
- Gates deliberately excluded: EOL -- not scheduled; precondition recorded
- EOR included because service agreements run past EOS (contract-driven)
- Enablement complete by: March 13, 2026 (partners March 6)
- Announcement date: March 31, 2026

**DP3**: Every item owned, every date real?
- [x] No unowned items
- [x] No invented dates -- EOL carries "Not scheduled" plus its precondition
- [x] Data (telemetry retention), contracts (per-account end dates), access
      (n/a), money (service wind-down model) all covered
- [x] Phase 6 review on the checklist -- Owner: Product
- [x] Post-EOL item added: reassess the EOL precondition -- Owner: Product

---

### Phase 4: Prepare                       Status: [x] Done  (Mar 2026)

- Materials built: Support/field FAQ, sales talking points, objection handling,
  escalation playbook, channel partner brief, 90-minute training with role-play
- Escalation owners: L1 Field service desk, L2 Ravi, L3 Elena, Exec Tom
- Partners briefed: March 6, 2026 -- 25 days before public notice

**DP4**: Enablement complete?
- [x] Field techs could answer "when does my controller stop working?" correctly
      ("it doesn't") without hedging
- [x] Role-played the bricking, mounting, and audit objections
- [x] Offers pre-approved; two explicitly forbidden (no parts past 2028, no
      NFA-500 drop-in claims)
- [x] Partners had the brief and forbidden-claims list before customers

---

### Phase 5: Announce                      Status: [x] Done  (March 31, 2026)

- Size: Full
- Path: Replacement, with channel and regulatory obligations
- Segments: customer notice, partner pack, validated-process customers received
  the change-control documentation package
- Comms calendar: Mar 31 status change, Sep 2026 last-time-buy reminder,
  Jan 2027 final order window, Dec 2027 non-renewal notices

**DP5**: Does it survive contact?
- [x] Legal reviewed service, refund, and certification language
- [x] Consistent with Phase 2 -- the three mid-standardization accounts were
      called before the notice and given reserved last-time-buy quantities
- [x] Field service and partners had it first
- [x] Passes the sticky-note test: "your units are unaffected; last order
      March 31, 2027"

---

### Phase 6: Close                         Status: [ ] In progress  (through Dec 2028)

- Gates closed: NSC Mar 2026, EOS Mar 2027, EOE Mar 2027 -- signed off
- Gates pending: EOR Dec 2027, EOM Dec 2028, EOSRV Dec 2028
- Transition progress: 31 of 120 sites retrofitted to NFA-500
- Retention vs. forecast: 100% of service agreements retained to date

**Closure items**
- [x] Manufacturing line reallocated (the original ask) -- April 2027
- [x] Interim lessons-learned review written after EOS -- Owner: Product
- [ ] Telemetry export and archive (due Dec 2028)
- [ ] Contracts settled; non-renewals confirmed in writing (in progress)
- [ ] Revenue recognition closed (due Dec 2028)
- [ ] **Reassess the EOL precondition** -- Owner: Product, review each Q4

**DP6**: Is this actually closed?
- [ ] Not yet -- service obligations run to December 2028

---

### Interim lessons learned (excerpt, written after EOS)

- The first-pass Phase 1 verdict was wrong because we assumed the landing place
  was ready without checking. One question -- "is the NFA-500 a drop-in for the
  installed base?" -- would have caught it in October instead of February.
- Going back to Phase 1 cost four months and saved us from announcing a
  shutdown date for 120 controllers we had no way to migrate.
- Executives asked for an EOL and accepted an EOS because we arrived at Stop 5
  with four conversations' worth of evidence. Sequencing them fifth, not first,
  is what made that possible.
- Briefing partners 25 days early cost nothing and surfaced a partner mid-bid on
  an NFA-200 project we would have torpedoed.

### Assumptions to Validate
- Assumes no service agreement extends past December 2028 (Legal confirmed)
- Assumes component supply supported the final build (held)
- Assumes retrofit bracket funding stays approved (at risk -- re-check each Q4)
```

---

## What to notice

- **Phase 1 appears twice, and the first pass is marked Superseded rather than deleted.** The
  record of the wrong verdict — and specifically the unchecked box next to "landing place readiness"
  — is the most instructive line in the tracker.
- **DP2 is the gate that earned its keep.** Both of its checks failed, and the process looped. Four
  months looked like a delay and was actually the avoidance of announcing a shutdown date for 120
  controllers with no migration path.
- **The verdict got cheaper, not smaller.** EOS returned the manufacturing line, which was the
  actual internal ask, without committing to an EOL nobody could deliver. Separating the presenting
  problem from the underlying one is what Phase 1 is for.
- **Phase 6 is legitimately open for two more years.** Closure is the obligation end date, not the
  announcement. Note the interim review written after EOS — waiting until 2028 to capture lessons
  would have lost them.
- **A deferred decision has a named owner and a recurring review.** "Reassess the EOL precondition
  — Owner: Product, review each Q4." Without that line, "not scheduled" quietly becomes "forgotten,"
  and the next PM inherits a product with no plan and no explanation.
