# Assumption Mapping Example: Industrial

**Idea:** a bracket kit that lets NFA-200 sites migrate to the NFA-500 in one shift.
**Decision:** fund tooling for the bracket kit (long lead time, hard to reverse).

**Why this example exists:** in hardware the decision is hard to undo, so evidence weighs more, and
the riskiest beliefs are about the plant floor and the channel, not the product.

---

```markdown
## Assumptions
| # | Assumption | Type | Role | Imp. | Evidence | Strength |
|---|---|---|---|---|---|---|
| 1 | Plants can't give up a weekend of production | D | Plant manager | H | 6 of 9 interviews | Some-strong |
| 2 | The bracket kit makes the swap fit a single 8-hour shift | U | Technician | H | one pilot site | Weak |
| 3 | Existing programs import without rewriting | F | Engineer | H | test report T-114 (partial) | Some |
| 4 | Partners will stock the kit | V | Distributor | M | one partner said so | Weak |
| 5 | Plants will pay for the kit on top of the controller | V | Procurement | H | **none** | None |
| 6 | The kit keeps UL listing unchanged | V | Compliance | H | **not assessed** | None |
| 7 | Installers will follow the torque spec | U | Partner crew | M | observed twice | Weak |

## Map
**Test first:** 2, 5, 6
**Monitor:** 1, 3 (some evidence; check at pilot)
**Park:** 4, 7 (revisit after tooling decision)

## Top three
| # | Assumption | Kill condition | Test |
|---|---|---|---|
| 6 | Bracket kit keeps UL listing | Assessor says re-evaluation is required | Ask the assessment body before tooling |
| 5 | Plants pay for the kit | Fewer than 3 of 6 plants will quote it separately | Quote the kit to six plants (procurement included) |
| 2 | Swap fits 8 hours | Two of three pilot swaps exceed 8 hours | Three timed pilot swaps |
```

## What to learn from this

- **The listing assumption (#6) could void the whole kit,** and it had no evidence at all. It outranks
  every desirability question.
- **Evidence from one pilot is weak.** One site is a story, not a sample.
- **Test order follows reversibility:** the cheapest, most fatal question (the assessor) goes first,
  before tooling money is committed.
