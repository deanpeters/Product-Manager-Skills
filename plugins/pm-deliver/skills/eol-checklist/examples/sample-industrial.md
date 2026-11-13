# EOL Checklist Example — Industrial

**Product:** NFA-200 series retrofit controller (Northfield Automation)
**Level:** 3 — Heavy · **Phases:** NSC, EOS, EOE, EOR, EOM, EOSRV — **EOL deliberately not scheduled**
**Context:** ~120 installations, 8 channel partners, service contracts running through 2028, UL 508A
and CE certified, spare parts inventory in the field. NFA-500 is the successor but needs a different
mounting bracket and a per-site retrofit.

**Why Level 3:** Four workstreams the lighter levels have no room for — inventory and spare parts,
eight channel partners, regulatory certification, and service contracts with terms running past the
sunset.

**Why EOL is not scheduled:** There is no drop-in migration path. Setting an EOL date would commit
to a day when 120 controllers stop being supportable, without knowing how those sites get off the
product. The checklist carries the precondition instead of a fictional date.

---

```markdown
## EOL Checklist: NFA-200 Series Retrofit Controller

**Level**: 3 -- Heavy
**Phases in scope**: NSC, EOS, EOE, EOR, EOM, EOSRV
**Phases not in scope**: EOL -- not scheduled; see precondition below
**Target EOL date**: Not scheduled
**Precondition to schedule EOL**: Validated NFA-500 retrofit path with
per-site cost, plus installed base below 20 units

### Lifecycle Phase Definitions

- **NSC (Notice of Status Change)**: Decision communicated; planning begins
- **EOS (End of Sale)**: No new units can be ordered
- **EOE (End of Expansion)**: No new I/O expansion modules
- **EOR (End of Renewal)**: Service agreements will not be renewed
- **EOM (End of Maintenance)**: Non-safety firmware updates stop
- **EOSRV (End of Service)**: Service, parts, and support obligations end

---

### Phase: NSC -- Target Date: March 31, 2026

#### Product and Strategy
- [ ] Confirm NFA-500 functional parity -- Owner: Product
- [ ] Document mounting incompatibility clearly -- Owner: Product
- [ ] Scope per-site retrofit assessment -- Owner: Product

#### Regulatory and Compliance
- [ ] Confirm UL and CE remain valid -- Owner: Regulatory
- [ ] Prepare change-control documentation package -- Owner: Regulatory
- [ ] Identify validated-process customers -- Owner: Regulatory

#### Legal and Contractual
- [ ] Audit all service agreement end dates -- Owner: Legal
- [ ] Identify agreements extending past 2028 -- Owner: Legal
- [ ] Review channel reseller agreement terms -- Owner: Legal

#### Inventory and Supply Chain
- [ ] Calculate spare parts coverage through 2028 -- Owner: Supply Chain
- [ ] Place final component buy orders -- Owner: Supply Chain
- [ ] Model last-time-buy demand forecast -- Owner: Supply Chain

#### Channel and Partner Management
- [ ] Brief eight partners before public notice -- Owner: Channel
- [ ] Define last-time-buy ordering window -- Owner: Channel

#### Financial Planning
- [ ] Model revenue through service wind-down -- Owner: Finance
- [ ] Budget spare parts carrying cost -- Owner: Finance

#### Internal Organizational Alignment
- [ ] Confirm manufacturing line reallocation plan -- Owner: Operations
- [ ] Align service org on support commitment -- Owner: Service

#### Engineering and Technical
- [ ] Freeze NFA-200 feature development -- Owner: Engineering

#### Support
- [ ] Draft field service holding guidance -- Owner: Service

### Phase: EOS -- Target Date: March 31, 2027

#### Sales
- [ ] Close last-time-buy order window -- Owner: Sales
- [ ] Remove NFA-200 from price book -- Owner: Sales Ops

#### Channel and Partner Management
- [ ] Confirm partner final order quantities -- Owner: Channel
- [ ] Publish approved partner messaging -- Owner: Channel

#### Marketing
- [ ] Issue customer status-change notice -- Owner: Marketing
- [ ] Update product pages and literature -- Owner: Marketing

#### Inventory and Supply Chain
- [ ] Reconcile final build against orders -- Owner: Supply Chain
- [ ] Transfer spares to service inventory -- Owner: Supply Chain

#### Customer Success
- [ ] Offer free retrofit assessments -- Owner: Account Management

### Phase: EOE -- Target Date: March 31, 2027

#### Product and Strategy
- [ ] Stop I/O expansion module sales -- Owner: Product

#### Support
- [ ] Confirm existing configurations stay supported -- Owner: Service

### Phase: EOR -- Target Date: December 31, 2027

#### Legal and Contractual
- [ ] Issue non-renewal notices per terms -- Owner: Legal
- [ ] Confirm each customer end date writing -- Owner: Legal

#### Financial Planning
- [ ] Reforecast service revenue decline -- Owner: Finance

#### Customer Success
- [ ] Review retrofit plans with each account -- Owner: Account Management

### Phase: EOM -- Target Date: December 31, 2028

#### Engineering and Technical
- [ ] Stop non-safety firmware releases -- Owner: Engineering
- [ ] Continue safety patches to EOSRV -- Owner: Engineering

#### Documentation and Training
- [ ] Publish final firmware and manuals -- Owner: Docs

### Phase: EOSRV -- Target Date: December 31, 2028

#### Support
- [ ] Conclude field service obligations -- Owner: Service
- [ ] Publish self-service repair documentation -- Owner: Service

#### Inventory and Supply Chain
- [ ] Offer remaining spares to customers -- Owner: Supply Chain
- [ ] Dispose or archive residual inventory -- Owner: Supply Chain

#### Regulatory and Compliance
- [ ] Archive certification records per retention -- Owner: Regulatory

#### Financial Planning
- [ ] Close service revenue recognition -- Owner: Finance

#### Data Management
- [ ] Export and archive telemetry records -- Owner: Data

---

### Phase Gate Criteria

#### NSC to EOS
- [ ] Legal confirms all agreement end dates -- Approver: General Counsel
- [ ] Spare parts coverage verified through 2028 -- Approver: VP Operations
- [ ] All eight partners briefed and acknowledged -- Approver: VP Channel
- [ ] Regulatory confirms certification unaffected -- Approver: Director Regulatory

#### EOS to EOR
- [ ] Final build reconciled against orders -- Approver: VP Operations
- [ ] Retrofit assessment offered to all sites -- Approver: VP Sales

#### EOR to EOM
- [ ] Every customer end date confirmed writing -- Approver: General Counsel
- [ ] Safety patch process documented -- Approver: VP Engineering

#### EOM to EOSRV
- [ ] No open safety issues outstanding -- Approver: VP Engineering
- [ ] Remaining spares offered to customers -- Approver: VP Operations

---

### Post-EOL Actions

- [ ] Archive design and certification records -- Owner: Engineering
- [ ] Run lessons-learned review -- Owner: Product
- [ ] Report installed base final disposition -- Owner: Service
- [ ] Reassess EOL scheduling precondition -- Owner: Product

### Assumptions to Validate
- Assumes no service agreements extend past December 2028
- Assumes component supply supports build through March 2027
- Assumes NFA-500 retrofit path is funded separately
- Partner count (8) assumes no new resellers signed before EOS
```

---

## What to notice

- **A phase can be legitimately absent.** EOL is listed as not scheduled, with an explicit
  precondition — validated retrofit path plus installed base below 20 units. That is more useful
  than a date invented to fill the blank, and it gives the next planner a trigger to watch.
- **EOR appears because contracts demanded it.** The default Level 3 set doesn't include End of
  Renewal; service agreements running past EOS pulled it in. Let the obligations shape the phases.
- **Partners are briefed before the public notice.** "Brief eight partners before public notice" is
  an NSC item and a gate criterion. Resellers learning about your EOL from their own customers is
  how you lose a channel.
- **Safety patches outlive maintenance.** EOM stops non-safety firmware while safety patches
  continue to EOSRV. Collapsing those two into one date is the kind of shortcut that ends up in a
  regulatory file.
- **Post-EOL includes re-checking the precondition.** Since EOL was never scheduled, someone has to
  own asking again — otherwise "not scheduled" quietly becomes "forgotten."
