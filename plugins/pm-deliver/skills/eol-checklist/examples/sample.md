# EOL Checklist Example — SaaS

**Product:** Fieldlight Classic Dispatch (legacy dispatch module, Fieldlight FSM platform)
**Level:** 2 — Standard · **Phases:** NSC, EOS, EOE, EOM, EOL
**Context:** ~800 accounts, $2.4M ARR, annual contracts, no regulatory constraint, no hardware,
sold direct. Replaced by Fieldlight Next Scheduling. ~30 accounts use custom dispatch rules that
don't carry over.

**Why Level 2:** Real customers with contracts and revenue, so Legal, Finance, and the
customer-facing functions are all in play — but there's no inventory, no channel, and no
regulator, so the three Level 3 areas are out.

---

```markdown
## EOL Checklist: Fieldlight Classic Dispatch

**Level**: 2 -- Standard
**Phases in scope**: NSC, EOS, EOE, EOM, EOL
**Phases not in scope**: EOR (annual contracts expire naturally before EOL);
EOSRV (SaaS -- no post-EOL service obligations)
**Target EOL date**: December 31, 2026

### Lifecycle Phase Definitions

- **NSC (Notice of Status Change)**: Decision communicated; planning begins
- **EOS (End of Sale)**: No new customers can purchase
- **EOE (End of Expansion)**: Existing customers cannot add capacity
- **EOM (End of Maintenance)**: Bug fixes and patches stop
- **EOL (End of Life)**: Product is fully retired

---

### Phase: NSC -- Target Date: January 15, 2026

#### Product and Strategy
- [ ] Confirm Next reaches dispatch parity -- Owner: Product
- [ ] Document custom-rule gap explicitly -- Owner: Product

#### Engineering and Technical
- [ ] Inventory all Classic API consumers -- Owner: Engineering
- [ ] Scope automated rule migration tool -- Owner: Engineering

#### Legal and Contractual
- [ ] Review 800 contracts for commitments -- Owner: Legal
- [ ] Confirm no multi-year Classic terms -- Owner: Legal

#### Financial Planning
- [ ] Model ARR retention scenarios -- Owner: Finance
- [ ] Budget migration support headcount -- Owner: Finance

#### Sales
- [ ] Freeze Classic in new quotes -- Owner: Sales Ops
- [ ] Identify Classic deals in pipeline -- Owner: Sales

#### Customer Success
- [ ] Tag 30 custom-rule accounts -- Owner: CS
- [ ] Score churn risk per account -- Owner: CS

#### Support
- [ ] Draft internal holding response -- Owner: Support Lead

#### Documentation and Training
- [ ] Draft migration guide outline -- Owner: Docs

### Phase: EOS -- Target Date: March 1, 2026

#### Product and Strategy
- [ ] Remove Classic from signup flow -- Owner: Product

#### Sales
- [ ] Retire Classic SKU and pricing -- Owner: Sales Ops
- [ ] Convert open Classic deals to Next -- Owner: Sales

#### Marketing
- [ ] Publish announcement to all accounts -- Owner: Marketing
- [ ] Update site and pricing pages -- Owner: Marketing
- [ ] Halt Classic demand-gen spend -- Owner: Marketing

#### Customer Success
- [ ] Begin outreach to custom-rule accounts -- Owner: CS

#### Support
- [ ] Publish support FAQ and macros -- Owner: Support Lead

#### Documentation and Training
- [ ] Ship migration guide and video -- Owner: Docs

#### Engineering and Technical
- [ ] Release rule migration wizard -- Owner: Engineering

### Phase: EOE -- Target Date: June 1, 2026

#### Product and Strategy
- [ ] Block new dispatch board creation -- Owner: Product

#### Engineering and Technical
- [ ] Deprecate v1 dispatch API writes -- Owner: Engineering
- [ ] Notify identified API consumers -- Owner: Engineering

#### Customer Success
- [ ] Report migration progress weekly -- Owner: CS
- [ ] Escalate accounts with zero progress -- Owner: CS

#### IT Systems
- [ ] Audit internal Classic dependencies -- Owner: IT

### Phase: EOM -- Target Date: October 1, 2026

#### Engineering and Technical
- [ ] Stop non-security Classic fixes -- Owner: Engineering
- [ ] Maintain security patching only -- Owner: Engineering

#### Support
- [ ] Shift Support to migration assistance -- Owner: Support Lead

#### Customer Success
- [ ] Run save plays on holdouts -- Owner: CS

#### Financial Planning
- [ ] Reforecast Q4 based on migration -- Owner: Finance

### Phase: EOL -- Target Date: December 31, 2026

#### Engineering and Technical
- [ ] Disable Classic Dispatch access -- Owner: Engineering
- [ ] Retire v1 dispatch API endpoints -- Owner: Engineering

#### Data Management
- [ ] Publish final export deadline -- Owner: Data
- [ ] Retain exports ninety days post-EOL -- Owner: Data
- [ ] Schedule Classic data deletion -- Owner: Data

#### Financial Planning
- [ ] Close Classic revenue recognition -- Owner: Finance

#### IT Systems
- [ ] Decommission Classic infrastructure -- Owner: IT

#### Documentation and Training
- [ ] Archive Classic documentation -- Owner: Docs

---

### Phase Gate Criteria

#### NSC to EOS
- [ ] Legal confirms no blocking contract terms -- Approver: General Counsel
- [ ] Migration wizard passes internal testing -- Approver: VP Engineering
- [ ] Announcement approved and scheduled -- Approver: CPO

#### EOS to EOE
- [ ] All API consumers identified and notified -- Approver: VP Engineering
- [ ] Custom-rule accounts contacted individually -- Approver: VP CS

#### EOE to EOM
- [ ] Migration above 60 percent of accounts -- Approver: CPO
- [ ] No unresolved P1 migration defects -- Approver: VP Engineering

#### EOM to EOL
- [ ] Migration above 95 percent of accounts -- Approver: CPO
- [ ] Every remaining account personally contacted -- Approver: VP CS
- [ ] Export tooling verified working -- Approver: VP Engineering

---

### Post-EOL Actions

- [ ] Archive Classic code and configs -- Owner: Engineering
- [ ] Run lessons-learned review -- Owner: Product
- [ ] Report final retention against forecast -- Owner: Finance

### Assumptions to Validate
- Support volume figure (40 percent) is estimated, not measured
- Custom-rule account count (~30) needs a query to confirm
- Assumes no Classic-specific terms in enterprise contracts
```

---

## What to notice

- **The gate criteria carry the real risk management.** "Migration above 95 percent" before EOL is
  what prevents shutting the product off on 200 accounts that never moved. Dates alone wouldn't
  catch that.
- **Phases not in scope are named with reasons.** EOR and EOSRV are stated as deliberately excluded
  rather than silently omitted — a reader can check the reasoning instead of wondering.
- **The hard segment appears in three phases.** The ~30 custom-rule accounts get tagged at NSC,
  contacted at EOS, and gate the EOE transition. The thing most likely to go wrong is tracked
  across the whole plan rather than mentioned once.
- **Downstream readers are on the list.** "Inventory all Classic API consumers" at NSC and "Audit
  internal Classic dependencies" at EOE catch the dashboards and jobs nobody remembers.
- **The lessons-learned review is owned.** It's the first item teams drop; naming Product as the
  owner is what makes it survive.
