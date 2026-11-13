# Launch Plan Example: SaaS (Tier 2)

**Offering:** Route Optimizer, a new module in Fieldlight (field service SaaS)
**Fixed date:** General availability June 12 (the customer conference keynote)
**Context:** Existing customers, existing channels, a new add-on price. Product leadership is
excited. Support has not seen it. This is the plan a PM builds in one sitting, once the tier is
agreed.

**Why this example exists:** it shows a Tier 2 plan where the work is *not* engineering. Four of
the eight functions hold rows the build schedule never mentioned.

---

```markdown
## Launch Plan: Route Optimizer

### 1. Tier assessment
| Criterion | Rating | Reason |
|---|---|---|
| Revenue and margin at stake | Medium | Add-on priced at a share of seat price; ~15% attach in year 1 [FROM YOU] |
| Newness to the customer | Medium | New capability, same users |
| Newness to the company | Low | Same channel, same billing |
| Regulatory and safety exposure | Medium | Uses technician GPS traces: privacy review needed |
| Installed-base impact | Low | Optional, off by default |
| Channel impact | Low | Resellers sell add-ons already |

**Proposed tier:** 2 Standard. Why: one new exposure (location data), nothing else new.
**A lighter tier would leave uncovered:** privacy review and reseller briefing.
**Confirmed by:** Launch forum, May 5

### 2. Four dates
| Moment | Date | Gap |
|---|---|---|
| Announce | Jun 12 (keynote) | 0 days to GA by design |
| Order opens | Jun 12 | Reseller price file due May 29 |
| First delivery | Jun 12 (tenants enabled on request) | Self-serve on Jul 8 |
| Full support | Jun 12 for tier-1 help; Jul 8 for advanced routing issues | 26-day gap accepted: advanced issues escalate to a named engineer |

### 3. Checklist (selected rows)
| Function | Deliverable | Owner | Due | Status |
|---|---|---|---|---|
| Support | 12 agents complete a 90-minute session and pass 5 sample tickets | Dana (Support lead) | Jun 2 | At risk [FROM YOU] |
| Support | Runbook and escalation path live in help center | Dana | Jun 5 | On track |
| Sales and channel | Resellers briefed; price file sent | Marco (Channel) | May 29 | On track |
| Legal | Privacy review of GPS trace use closed; DPA addendum text approved | Priya (Legal) | May 22 | Not started `[NEEDS SOURCE]` |
| Pricing | Add-on SKU, billing plan, quote template live | Lee (RevOps) | Jun 1 | On track |
| Marketing | Keynote demo script, data sheet, web page | Sam (PMM) | Jun 8 | On track |
| Operations | Routing service load-tested to 3x projected day-one traffic | Ravi (Eng lead) | May 30 | `[AI-SUGGESTED, VALIDATE THIS]` |
| Internal | Customer success has the FAQ and a rollback script | Jo (CS lead) | Jun 5 | Not started |

### 4. Go/no-go criteria (written May 5)
| # | Check | Threshold | Evidence | Owner | Type |
|---|---|---|---|---|---|
| 1 | Privacy review | Closed, addendum published | Legal sign-off | Priya | Must-pass |
| 2 | Support readiness | All tier-1 agents certified | Roster | Dana | Must-pass |
| 3 | Load test | 3x day-one traffic, error rate under threshold `[NEEDS SOURCE]` | Test report | Ravi | Must-pass |
| 4 | Reseller price file | Delivered | Sent receipt | Marco | Watch |
| 5 | Demo reliability | 3 clean runs on conference network | Rehearsal log | Sam | Watch |

**Gate:** Jun 5. Approver: VP Product (one person). DACI: Driver PM; Contributors function owners.

### 7. Premortem (excerpt)
| Failure story | Cause | L/I | Landed as |
|---|---|---|---|
| "The keynote demo timed out and Support got 200 tickets we couldn't answer" | Demo env not load-tested; agents untrained | High/High | Criteria 2 and 3 (added) |
| "A customer's counsel asked how we store technician locations" | Privacy review slipped behind the keynote | Med/High | Criterion 1 (promoted to must-pass) |

### Riskiest assumptions
1. Load test threshold is `[NEEDS SOURCE]`: if it is set too low, criterion 3 passes and it fails live.
2. The 26-day support gap assumes advanced issues are rare. Nobody has measured that.
```

## What to learn from this

- **The build was done in April.** Every open row is a business function. That is the whole lesson
  of "a launch is not a ship date."
- **The premortem changed the plan twice.** Privacy review moved from "nice to have" to must-pass,
  because a function owner (Legal) wrote the failure story, not the PM.
- **The 26-day support gap is a decision, written down,** with a named engineer on escalation.
  It is not an accident someone discovers in July.
