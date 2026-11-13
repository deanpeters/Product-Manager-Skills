# Decision Rights Matrix Example: SaaS

**Context:** Fieldlight. Sales keeps granting add-on discounts the product team set limits on; roadmap
items get re-opened every Monday. 40 people across product, sales, CS, and finance.
**Why this example exists:** "both" was the answer to every question, and splitting each decision was
the whole job.

---

```markdown
## Decisions that hurt
1. Add-on discount limits (sales overrides weekly)
2. What goes on next quarter's roadmap (reopened every Monday)
3. Customer-specific commitments (a promised feature for one deal)
4. Launch go/no-go for the Route Optimizer

## Matrix
| Decision | Driver | **Approver** | Consulted | Informed | Veto |
|---|---|---|---|---|---|
| Discount band for add-ons | PM (pricing) | **VP Product** | Finance, Sales VP | Reps, CS | Finance if margin below floor |
| Quarterly roadmap | PM | **VP Product** | Engineering, Sales, CS | Company | none |
| Deal-specific commitments | Account exec | **VP Sales** (within bands) / **VP Product** (outside) | PM, Engineering | CS | none |
| Launch go/no-go | PM | **VP Product** | Support, Sales, Legal, Engineering | Company | Legal if a must-pass fails |

*Note: "Deal-specific commitments" was "both" in the first draft; split by whether it is inside the agreed bands.*

## Forums
| Forum | Decides | Does not | Attends | Cadence |
|---|---|---|---|---|
| Pricing council | Discount bands, exceptions above band | List price | VP Product, VP Sales, Finance | Fortnightly, 30 min |
| Roadmap review | Quarter's roadmap | Individual deals | VP Product, Eng lead, Sales, CS | Monthly |

## Escalation
Pricing disputes go to the COO within 3 working days, with a one-page brief (deal size, margin impact).

## Decision log (first entries)
| Date | Decision | By | Evidence | Supersedes |
|---|---|---|---|---|
| Nov 4 | Add-on discount band 0-12%; above needs council | VP Product | Margin model, 11 deals | none |

All approvers confirmed individually before circulation. COO endorsed the escalation path.
```

## What to learn from this

- **"Both" was split into inside-the-band and outside-the-band,** which gave each side a real zone.
- **Finance's veto is stated with a reason** (margin floor), so it can't become a general block.
- **The matrix was confirmed individually** before it went to a group, so nobody learned of their role in a meeting.
