# Activation Design Example: SaaS

**Product:** Route Optimizer add-on (Fieldlight) · **Customer:** dispatchers at 50-300 technician companies
**Why this example exists:** the team counted "tour finished" as activated. The redefinition changed
the onboarding from a tour to a short path.

---

```markdown
## The moment
**Customer's goal:** fix the day without hours of rework when it breaks.
**Activation (hypothesis):** a dispatcher optimizes a real day and keeps the result (does not
revert it) within 7 days.
**Evidence:** Prior add-on: accounts reaching its first real use retained at 82% vs 51%
(`[NEEDS SOURCE]` for this product; to confirm after 90 days).

## The path today (March trials, N = 212)
| Step | Owner | Median | Stopped here |
|---|---|---|---|
| Invite dispatcher | Customer | 1 day | 47 |
| Load a day | Customer | 2 days | 48 |
| Optimize first route | Customer | 1 day | 68 |
**Time to value:** median 4 days; the slowest quarter never arrive.

## Blockers
| Blocker | Evidence | Fix |
|---|---|---|
| Depot address not set | 31 of 68 stalled accounts | Pre-fill from the account (remove) |
| Day has no jobs in trial | Interviews (3) | Offer sample day data (do-for-them) |
| Large accounts need a skills mapping | 28 of 40 large trials stalled | Specialist call at day 2 |

## Designed path
| Checkpoint | Action | Owner | Stall handling |
|---|---|---|---|
| 1 | Confirm depot (pre-filled) | Product | none needed |
| 2 | Load today or the sample day | Product/customer | Day 2 nudge: offer sample day |
| 3 | Optimize and keep | Customer | Day 3: email; Day 5: specialist call if account > 100 techs |
**Handoff:** sales records the dispatcher's name, current process, and biggest rework pain in the CRM; onboarding opens the first call with it.

## Metric
**Reached activation within 7 days:** 49 of 212 (23%) March baseline · target `[NEEDS SOURCE]`.
**Median time to activate:** 4 days · **Guardrail:** support contacts per new account.
```

## What to learn from this

- **"Tour finished" was removed from the metric.** It rose while real use stayed flat.
- **The top blocker was a missing default,** fixed by pre-filling, not by teaching.
- **The activation moment is labeled a hypothesis,** with the check named.
