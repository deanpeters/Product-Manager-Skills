# Assumption Mapping Example: SaaS

**Idea:** Route Optimizer add-on (Fieldlight). **For:** dispatchers at 50-300 technician service companies.
**Decision:** commit one quarter of engineering. **Business case:** 15% attach in year one.

**Why this example exists:** the team's confidence sat on desirability. Walking by role surfaced a
legal assumption nobody had written down, and it outranked everything.

---

```markdown
## Assumptions
| # | Assumption | Type | Role | Imp. | Evidence | Strength |
|---|---|---|---|---|---|---|
| 1 | Dispatchers feel the rescheduling pain weekly | D | Dispatcher | H | 6 of 8 interviews, unprompted | Some-strong |
| 2 | A dispatcher can optimize a day in under 5 minutes unaided | U | Dispatcher | H | none (prototype untested) | None |
| 3 | 15% of eligible accounts will attach in year one | V | Sales | H | prior add-on reached 11% [FROM YOU] | Some |
| 4 | Resellers will demo and sell the add-on | V | Reseller | M | none | None |
| 5 | Routing runs under 2 seconds at peak | F | Engineering | H | load test not run | None |
| 6 | Technicians accept location data being used for routing | E | Technician | H | **none** | None |
| 7 | Customers' legal teams will approve location-data use under the current DPA | V | Customer legal | H | **none** `[AI-SUGGESTED, VALIDATE THIS]` | None |

## Map
**Test first (high importance, weak evidence):** 2, 5, 6, 7
**Monitor:** 1
**Park:** 4

## Top three
| # | Assumption | Kill condition | Test |
|---|---|---|---|
| 7 | Customer legal approves location use under current DPA | Two of five customers' counsel require a new addendum before pilot | Ask Legal and three customers' counsel; a week |
| 2 | Dispatcher optimizes a day in under 5 min unaided | More than 2 of 6 need help | Clickable prototype with 6 dispatchers ([`pol-probe-advisor`](../../pol-probe-advisor/SKILL.md)) |
| 5 | Routing under 2 seconds at peak | Over 4 seconds at 3x expected load | Load test |
```

## What to learn from this

- **Assumption 7 was a boring one,** written by walking the story as a customer's lawyer.
  It shipped no features and could still delay launch by weeks.
- **Desirability (#1) was monitored, not tested.** The team had enough to stop worrying about it.
- **Every top item has a kill condition,** so a test can change the plan.
