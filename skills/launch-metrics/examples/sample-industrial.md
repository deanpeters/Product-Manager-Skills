# Launch Metrics Example: Industrial

**Offering:** NFA-500 retrofit controller (Northfield Automation), order intake Jul 1, first delivery Oct 15
**Sales cycle:** 6-9 months from quote to order; migration sales are scoped site visits
**Context:** Plan from the Tier 1 launch plan. Eight partners; distributors stock the controller and the bracket.

**Why this example exists:** it shows the **sell-in mirage**: partner stocking orders read as
demand. It also shows that in hardware the operational metrics are the fastest signal.

---

```markdown
## Launch Metrics: NFA-500

### Draft dashboard (critiqued first)
"Trade-fair leads, units shipped to distributors, press mentions." The second is **sell-in**. The
others are activity.

### Metric set
| # | Category | Metric | Lead/Lag | Guardrail | Baseline | Target | System | Owner |
|---|---|---|---|---|---|---|---|---|
| 1 | Adoption | Quotes issued to NFA-200 base sites | Lead | | `[NEEDS SOURCE]` | `[NEEDS SOURCE]` | CRM | Sales director |
| 2 | Adoption | Units **commissioned** (installed and passing acceptance) | Lead | | NFA-200 launch: 14 in first 90 days | `[NEEDS SOURCE]` | Service system | Service director |
| 3 | Adoption | Partner **sell-through** to end customers vs sell-in | Lead | **Yes** | NFA-200: 70% of sell-in sold through by day 120 | Escalate below 50% | Partner reports | Channel manager |
| 4 | Commercial | Win rate on migration quotes | Lag | | NFA-200: 31% | Business case: 35% | CRM | Sales director |
| 5 | Commercial | Price realization (pocket price / list) | Lead | **Yes** | NFA-200: 91% | Escalate below 85% | ERP | Commercial lead |
| 6 | Operational | On-time delivery to promised date | Lead | **Yes** | NFA-200: 94% | `[NEEDS SOURCE]` | ERP | Plant manager |
| 7 | Operational | First-time-right commissioning | Lead | | `[NEEDS SOURCE]` | `[NEEDS SOURCE]` | Service system | Service director |
| 8 | Operational | Early-life failures per 100 units, by failure mode | Lead | **Yes** | NFA-200 first 6 months: 3.2 | Escalate above 2x baseline | Warranty database | Quality lead |
| 9 | Customer | Satisfaction at commissioning | Lead | | `[NEEDS SOURCE]` | `[NEEDS SOURCE]` | Survey | Service director |
| 10 | Customer | Service-contract attach at 12 months | Lag | | NFA-200: 62% | Business case: 70% | ERP | Service director |

### The mirage
At day 60, distributors had ordered 80 units. Metric 3 showed 18 sold through (22%). Partners had
stocked ahead of the price protection deadline. Counting sell-in, the launch was 2x its plan. The
real demand was the 18.

### 90-day review (rundown excerpt)
| Metric | Expected | Actual | Why (hypothesis) | Change |
|---|---|---|---|---|
| 3: sell-through | 70% by day 120 (trending to 40%) | 22% at day 60 | Partners stocked for the price deadline, not demand (untested) | Channel manager interviews 4 partners; no new stocking incentive until sell-through reads |
| 8: early-life failures | ≤ 2x baseline | 2.6x on bracket fastener | Torque spec not in partner install guide (seen in 5 reports) | Quality issues bulletin; Tech pubs corrects guide (owner: Quality lead) |

**Premortem check:** drivers "partner crews untrained" and "bracket spares short" both started to
appear. Both were already in the Gate 2 criteria, but crew training reached only 6 of 8 partners.

**Thorn:** brackets back-ordered at two partners. **Bud:** partners ask for a bracket-only SKU.
**Rose:** the commissioning checklist partners like.
```

## What to learn from this

- **Sell-in beat plan while sell-through missed it.** Without metric 3 the 180-day review would
  have discovered the stall after distributor orders stopped.
- **The fastest signal was a failure mode,** not a sales number. A torque spec fixed in week 9
  protects every later cohort.
- **The premortem paid off at the review,** not just at the gate.
