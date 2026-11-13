# Launch Plan Example: Industrial (Tier 1)

**Offering:** NFA-500 retrofit controller (Northfield Automation), successor to the NFA-200
**Fixed date:** Trade fair, April 21
**Context:** New hardware generation, 8 channel partners, ~120 installed NFA-200 sites that will
migrate over years, UL and CE certification, a mounting bracket that differs from the NFA-200.
This is the launch that follows the NFA-200 retirement thread.

**Why this example exists:** the SaaS example collapses four dates into one. Here they pull apart
by nine months, and the *gap between them* is the plan.

---

```markdown
## Launch Plan: NFA-500 Retrofit Controller

### 1. Tier assessment
| Criterion | Rating | Reason |
|---|---|---|
| Revenue and margin at stake | High | Successor to the base product line [FROM YOU] |
| Newness to the customer | Medium | Same job, new bracket and commissioning steps |
| Newness to the company | Medium | First controller with a connected-service tier |
| Regulatory and safety exposure | High | UL 508A re-evaluation; CE conformity for the new radio module |
| Installed-base impact | High | ~120 NFA-200 sites; every migration is a scoped site visit |
| Channel impact | High | Partners must stock a new bracket and learn new commissioning |

**Proposed tier:** 1 Full. Why: four High scores.
**A lighter tier would leave uncovered:** formal gates, partner stocking plan, spare parts coverage.

### 2. Four dates
| Moment | Date | Gap and why |
|---|---|---|
| Announce | Apr 21 (trade fair) | |
| Order opens | Jul 1 | 10 weeks: partners need price files and bracket stock; NFA-200 orders continue meanwhile |
| First delivery | Oct 15 | 15 weeks: certification and first-article build on the critical path |
| Full support | Jan 20 | 13 weeks: technician training and spares in all launch countries |

**Announce-to-deliver gap is 6 months.** Sales plan for NFA-200 deals during the gap: continue
selling, with a migration path and a price-protection clause. Owner: Sales director.

### 3. Checklist (selected rows)
| Function | Deliverable | Owner | Due | Status |
|---|---|---|---|---|
| Certification | UL 508A evaluation complete; EU declaration of conformity signed | Compliance lead | Sep 15 | At risk |
| Channel | 8 partners briefed under NDA; price files sent; bracket stock plan agreed | Channel manager | Jun 1 | On track |
| Service and spares | 40 technicians trained; spares for first 12 months of planned installed base stocked | Service director | Jan 5 | Not started `[NEEDS SOURCE]` |
| Production | Ramp plan sized to *realistic* forecast; first-article inspection passed | Plant manager | Sep 30 | On track |
| Documentation | Manuals and safety instructions in 5 languages | Tech publications | Sep 1 | At risk |
| Pricing | List price, discount bands, partner margin approved | Commercial lead | May 15 | On track |
| Marketing | Fair booth, live demo unit, data sheet | Marketing manager | Apr 1 | On track |

### 4. Go/no-go criteria (written Feb 10)
| # | Check | Threshold | Evidence | Owner | Type |
|---|---|---|---|---|---|
| 1 | Declaration of conformity | Signed for all launch countries | Document | Compliance | Must-pass (Gate 2) |
| 2 | Technicians trained | 40 of 40 in launch countries | Records | Service | Must-pass (Gate 2) |
| 3 | Spares stocked | 12 months of planned installed base | Warehouse report | Service | Must-pass (Gate 2) |
| 4 | Capacity | Ramp confirmed vs realistic forecast | Plan sign-off | Plant | Must-pass (Gate 1) |
| 5 | Translated manuals | 5 languages | Release | Tech pubs | Watch |

**Gate 1 (before order intake, Jul 1):** Approver: COO. **Gate 2 (before first shipment, Oct 15):** Approver: COO.

### 7. Premortem (excerpt)
| Failure story | Cause | L/I | Landed as |
|---|---|---|---|
| "First three sites were commissioned by partner crews we hadn't trained; two failed acceptance" | Training scheduled after first shipment | High/High | Partner crew training added to Gate 2 as must-pass criterion 2 |
| "A customer waited 5 weeks for a bracket" | Spares counted controllers, not brackets | Med/High | Criterion 3 rewritten to include brackets |

### Riskiest assumptions
1. Certification lead time is a planning estimate, not a quote from the assessment body.
2. Spares quantity depends on a migration forecast nobody has validated.
```

## What to learn from this

- **Three of five go/no-go criteria are Service's,** not Engineering's. That is typical, and it is
  why Service is on the forum.
- **The announce-to-deliver gap is a decision with an owner.** Without one, NFA-200 sales quietly
  stall for six months.
- **Premortem stories rewrote two criteria.** Brackets were nowhere on the original spares list.
