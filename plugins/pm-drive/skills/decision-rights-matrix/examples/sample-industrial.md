# Decision Rights Matrix Example: Industrial

**Context:** Northfield Automation: product management, plant operations, regional sales, and
service each run a P&L slice. The NFA-500 launch exposed that nobody knew who called go/no-go.
**Why this example exists:** in a matrix organization with regional leaders, the veto question and
escalation matter more than the RACI.

---

```markdown
## Decisions that hurt
1. Launch go/no-go (twice, Gate 1 and Gate 2)
2. List price and partner margin
3. Customer-specific engineering commitments
4. Last-time-buy and end-of-sale for the NFA-200

## Matrix
| Decision | Driver | **Approver** | Consulted | Informed | Veto |
|---|---|---|---|---|---|
| Launch Gate 1 (order intake) | PM | **COO** | Plant, Sales, Service, Compliance | Partners | Compliance if certification gaps |
| Launch Gate 2 (first shipment) | PM | **COO** | same | same | Service if technicians not trained |
| List price and partner margin | PM | **Commercial director** | Regional sales, Finance | Partners | none |
| Special engineering commitment | Regional sales | **Engineering director** | PM, Plant | Service | none |
| NFA-200 end of sale | PM | **GM, Controls** | Finance, Service, Sales, Legal | Partners, customers | Legal if contracts bar it |

## Forums
| Forum | Decides | Does not | Cadence |
|---|---|---|---|
| Launch forum | Gate 1, Gate 2 | Price | At each gate; monthly in the quarter before |
| Commercial council | Price, partner margin | Engineering commitments | Monthly |

## Escalation
Disagreement between a regional head and the approver goes to the GM within 5 working days, with a
one-page brief covering revenue at stake, risk, and what each side wants.

## Notes
- **Service holds a veto at Gate 2.** The first draft gave "consult" and the last launch shipped
  with untrained technicians.
- **Gate 1 and Gate 2 have the same approver** (COO) on purpose: two deciders would have recreated
  the problem.
```

## What to learn from this

- **Veto is stated with a reason and a gate.** Service's veto applies only to untrained technicians.
- **Escalation has a number of days.** A regional head disagreeing with an approver has a path that isn't going around.
- **The previous launch's failure turned "consulted" into a veto,** with the evidence on the page.
