# Launch Metrics Example: SaaS add-on

**Offering:** Route Optimizer, a self-serve add-on in Fieldlight (field service SaaS), GA June 12
**Sales cycle:** 30-day trial for existing customers; ~6 weeks to first renewal signal
**Context:** Plan from the Tier 2 launch plan. The team's draft dashboard is "trials started,
web visits, keynote views, blog mentions."

**Why this example exists:** it shows a dashboard rebuilt from activity to results, and that
"seats purchased" is the SaaS version of sell-in.

---

```markdown
## Launch Metrics: Route Optimizer

### Critique of the draft dashboard (first)
- Trials started, web visits, keynote views, blog mentions are **activity**: all four can rise while
  no one adopts the module.
- No operational or customer metric. No guardrail. No triggers.

### Metric set
| # | Category | Metric | Lead/Lag | Guardrail | Baseline | Target | System | Owner |
|---|---|---|---|---|---|---|---|---|
| 1 | Adoption | Trials where a dispatcher optimizes a real day within 7 days | Lead | | Prior add-on: 38% [FROM YOU] | `[NEEDS SOURCE]` | Product analytics | PM |
| 2 | Adoption | Seats **activated** (used in last 14 days) / seats purchased | Lead | | `[NEEDS SOURCE]` | `[NEEDS SOURCE]` | Billing + analytics | RevOps |
| 3 | Commercial | Trial-to-paid conversion | Lead | | Prior add-on: 21% | `[NEEDS SOURCE]` | Billing | RevOps |
| 4 | Commercial | Attach rate among eligible accounts at 180 days | Lag | | n/a (new) | Business case: 15% | Billing | PM |
| 5 | Commercial | Discount depth on add-on deals | Lead | **Yes** | Standard add-on: 8% | Escalate above 20% | CRM | Sales |
| 6 | Operational | Support tickets per 100 active seats, first 30 days | Lead | **Yes** | Prior add-on: 9 | `[NEEDS SOURCE]` | Support tool | Support lead |
| 7 | Operational | Routing job failures per 1,000 runs | Lead | **Yes** | `[NEEDS SOURCE]` | `[NEEDS SOURCE]` | Service logs | Eng lead |
| 8 | Customer | Satisfaction at day 30 of use | Lead | | Prior add-on: 4.1/5 | `[NEEDS SOURCE]` | In-app survey | CS |
| 9 | Customer | Renewal of add-on at first term | Lag | | n/a | `[NEEDS SOURCE]` | Billing | CS |

### Triggers (excerpt)
| # | Stay | Adjust | Escalate | Data needed |
|---|---|---|---|---|
| 2 | ≥ 60% activated | 40-59%: CS onboarding campaign (CS) | < 40% for 2 weeks: forum reviews value and pricing | 100 seats |
| 5 | < 12% | 12-20%: Sales coaching | > 20%: pricing review with VP | 15 deals |
| 7 | Within baseline +1x | 1-2x: Eng hotfix plan | > 2x for 3 days: pause new enablement | 5,000 runs |

### The mirage this set prevents
Seats purchased was strong in week 2 (a few large customers bought 400 seats up front). Metric 2
shows 22% activated. **Purchased is not adopted.** The team ran a CS onboarding campaign in week 3
instead of celebrating.

### 90-day review (rundown excerpt)
| Metric | Expected | Actual | Why (hypothesis) | Change |
|---|---|---|---|---|
| 2: activation | 60% | 47% | Large accounts have no dispatcher champion (untested) | CS names a champion per 100+ seat account (owner: Jo) |
| 6: tickets/100 seats | 9 | 14 | Setup docs lack the depot-address step (seen in 11 tickets) | Doc fix by Jun 30 (owner: Dana) |

**Rose:** the in-app tour. **Bud:** customers asking for multi-depot routing (roadmap input, not
yet validated). **Thorn:** reseller-sold accounts get no onboarding call.
```

## What to learn from this

- **Four of nine metrics are leading.** The 180-day attach rate will not exist until December.
- **The guardrails are the ones people forget.** Discount depth would have hidden a weak product
  behind a cheap one.
- **"Why" stayed a hypothesis.** The champion explanation is untested, so it drove an *experiment*,
  not a conclusion.
