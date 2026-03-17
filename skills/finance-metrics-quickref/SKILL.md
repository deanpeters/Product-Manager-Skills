---
name: finance-metrics-quickref
description: Look up SaaS finance metrics, formulas, and benchmarks fast. Use when you need a quick metric definition, formula, or benchmark during analysis.
intent: >-
  Quick reference for any SaaS finance metric without deep teaching. Use this when you need a fast formula lookup, benchmark check, or decision framework reminder. For detailed explanations, calculations, and examples, see the related deep-dive skills.
type: component
best_for:
  - "Quick metric lookups during product or finance reviews"
  - "Checking formulas and benchmarks without reading a long explainer"
  - "Refreshing decision rules for common SaaS metrics"
scenarios:
  - "What is the formula for NRR and what is a good benchmark?"
  - "Give me a quick reference for CAC payback and Rule of 40"
  - "I need a fast SaaS metrics cheat sheet for a business review"
---


## Purpose

Quick reference for any SaaS finance metric without deep teaching. Use this when you need a fast formula lookup, benchmark check, or decision framework reminder. For detailed explanations, calculations, and examples, see the related deep-dive skills.

## Key Concepts

## Application

### All Metrics Reference Table

| **Metric** | **Formula** | **What It Measures** | **Good Benchmark** | **Red Flag** |
|------------|-------------|----------------------|-------------------|--------------|
| **Revenue** | Total sales before expenses | Top-line money earned | Growth rate >20% YoY (varies by stage) | Revenue growing slower than costs |
| **ARPU** | Total Revenue / Total Users | Revenue per individual user | Varies by model; track trend | ARPU declining cohort-over-cohort |
| **ARPA** | MRR / Active Accounts | Revenue per customer account | SMB: $100-$1K; Mid: $1K-$10K; Ent: $10K+ | High ARPA + low ARPU (undermonetized seats) |
| **ACV** | Annual Recurring Revenue per Contract | Annualized contract value | SMB: $5K-$25K; Mid: $25K-$100K; Ent: $100K+ | ACV declining (moving downmarket unintentionally) |
| **MRR/ARR** | MRR × 12 = ARR | Predictable recurring revenue | Growth + quality matter; track components | New MRR declining while churn stable/growing |
| **Churn Rate** | Customers Lost / Starting Customers | % of customers who cancel | Monthly <2% great, <5% ok; Annual <10% great | Churn increasing cohort-over-cohort |
| **NRR** | (Start ARR + Expansion - Churn - Contraction) / Start ARR × 100 | Revenue retention + expansion | >120% excellent; 100-120% good; 90-100% ok | NRR <100% (base is contracting) |
| **Expansion Revenue** | Upsells + Cross-sells + Usage Growth | Additional revenue from existing customers | 20-30% of total revenue | Expansion <10% of MRR |
| **Quick Ratio** | (New MRR + Expansion MRR) / (Churned MRR + Contraction) | Revenue gains vs. losses | >4 excellent; 2-4 healthy; <2 leaky bucket | Quick Ratio <2 (leaky bucket) |
| **Gross Margin** | (Revenue - COGS) / Revenue × 100 | % of revenue after direct costs | SaaS: 70-85% good; <60% concerning | Gross margin <60% or declining |
| **CAC** | Total S&M Spend / New Customers | Cost to acquire one customer | Varies: Ent $10K+ ok; SMB <$500 | CAC increasing while LTV flat |
| **LTV** | ARPU × Gross Margin % / Churn Rate | Total revenue from one customer | Must be 3x+ CAC; varies by segment | LTV declining cohort-over-cohort |
| **LTV:CAC** | LTV / CAC | Unit economics efficiency | 3:1 healthy; <1:1 unsustainable; >5:1 underinvesting | LTV:CAC <1.5:1 |
| **Payback Period** | CAC / (Monthly ARPU × Gross Margin %) | Months to recover CAC | <12 months great; 12-18 ok; >24 concerning | Payback >24 months (cash trap) |
| **Contribution Margin** | (Revenue - All Variable Costs) / Revenue × 100 | True contribution after variable costs | 60-80% good for SaaS; <40% concerning | Contribution margin <40% |
| **Burn Rate** | Monthly Cash Spent - Revenue | Cash consumed per month | Net burn <$200K manageable early; <$500K growth | Net burn accelerating |
| **Runway** | Cash Balance / Monthly Net Burn | Months until money runs out | 12+ months good; 6-12 ok; <6 crisis | Runway <6 months |
| **OpEx** | S&M + R&D + G&A | Costs to run the business | Should grow slower than revenue | OpEx growing faster than revenue |
| **Net Income** | Revenue - All Expenses | Actual profit/loss | Early negative ok; mature 10-20%+ margin | Losses accelerating without growth |
| **Rule of 40** | Revenue Growth % + Profit Margin % | Balance of growth vs. efficiency | >40 healthy; 25-40 ok; <25 concerning | Rule of 40 <25 |
| **Magic Number** | (Q Revenue - Prev Q Revenue) × 4 / Prev Q S&M | S&M efficiency | >0.75 efficient; 0.5-0.75 ok; <0.5 fix GTM | Magic Number <0.5 |
| **Operating Leverage** | Revenue Growth vs. OpEx Growth | Scaling efficiency | Revenue growth > OpEx growth | OpEx growing faster than revenue |
| **Gross vs. Net Revenue** | Net = Gross - Discounts - Refunds - Credits | What you actually keep | Refunds <10%; discounts <20% | Refunds >10% (product problem) |
| **Revenue Concentration** | Top N Customers / Total Revenue | Dependency on largest customers | Top customer <10%; Top 10 <40% | Top customer >25% (existential risk) |
| **Revenue Mix** | Product/Segment Revenue / Total Revenue | Portfolio composition | No single product >60% ideal | Single product >80% (no diversification) |
| **Cohort Analysis** | Group customers by join date; track behavior | Whether business improving or degrading | Recent cohorts same/better than old | Newer cohorts perform worse |
| **CAC Payback by Channel** | CAC / Monthly Contribution (by channel) | Payback by acquisition channel | Compare across channels | One channel far worse than others |
| **Gross Margin Payback** | CAC / (Monthly ARPU × Gross Margin %) | Payback using actual profit | Typically 1.5-2x simple payback | Payback using margin >36 months |
| **Unit Economics** | Revenue per unit - Cost per unit | Profitability of each "unit" | Positive contribution required | Negative contribution margin |
| **Segment Payback** | CAC / Monthly Contribution (by segment) | Payback by customer segment | Compare to allocate resources | One segment unprofitable |
| **Incrementality** | Revenue caused by action - Baseline | True impact of marketing/promo | Measure with holdout tests | Celebrating revenue that would've happened anyway |
| **Working Capital** | Cash timing between revenue and collection | Cash vs. revenue timing | Annual upfront > monthly billing | Long payment terms killing runway |

---

### Quick Decision Frameworks

Use these frameworks to combine metrics for common PM decisions.

#### Framework 1: Should We Build This Feature?

**Ask:**
1. **Revenue impact?** Direct (pricing, add-on) or indirect (retention, conversion)?
2. **Margin impact?** What's the COGS? Does it dilute margins?
3. **ROI?** Revenue impact / Development cost

**Build if:**
- ROI >3x in year one (direct monetization), OR
- LTV impact >10x development cost (retention), OR
- Strategic value overrides short-term ROI

**Don't build if:**
- Negative contribution margin even with optimistic adoption
- Payback period exceeds average customer lifetime

**Metrics to check:** Revenue, Gross Margin, LTV, Contribution Margin

---

#### Framework 2: Should We Scale This Acquisition Channel?

**Ask:**
1. **Unit economics?** CAC, LTV, LTV:CAC ratio
2. **Cash efficiency?** Payback period
3. **Customer quality?** Cohort retention, NRR by channel
4. **Scalability?** Magic Number, addressable volume

**Scale if:**
- LTV:CAC >3:1 AND
- Payback <18 months AND
- Customer quality meets/beats other channels AND
- Magic Number >0.75

**Don't scale if:**
- LTV:CAC <1.5:1 AND
- No clear path to improvement

**Metrics to check:** CAC, LTV, LTV:CAC, Payback Period, NRR, Magic Number

---

#### Framework 3: Should We Change Pricing?

**Ask:**
1. **ARPU/ARPA impact?** Will revenue per customer increase?
2. **Conversion impact?** Help or hurt trial-to-paid conversion?
3. **Churn impact?** Create churn risk or reduce it?
4. **NRR impact?** Enable expansion or create contraction?

**Implement if:**
- Net revenue impact positive after churn risk
- Can test with segment before broad rollout

**Don't change if:**
- High churn risk without offsetting expansion
- Can't test hypothesis before committing

**Metrics to check:** ARPU, ARPA, Churn Rate, NRR, CAC Payback

---

#### Framework 4: Is the Business Healthy?

**Check by stage:**

**Early Stage (Pre-$10M ARR):**
- Growth Rate >50% YoY
- LTV:CAC >3:1
- Gross Margin >70%
- Runway >12 months

**Growth Stage ($10M-$50M ARR):**
- Growth Rate >40% YoY
- NRR >100%
- Rule of 40 >40
- Magic Number >0.75

**Scale Stage ($50M+ ARR):**
- Growth Rate >25% YoY
- NRR >110%
- Rule of 40 >40
- Profit Margin >10%

**Metrics to check:** Revenue Growth, NRR, LTV:CAC, Rule of 40, Magic Number, Gross Margin

---

### Red Flags by Category

#### Revenue & Growth Red Flags
| **Red Flag** | **What It Means** | **Action** |
|--------------|-------------------|------------|
| Churn increasing cohort-over-cohort | Product-market fit degrading | Stop scaling acquisition; fix retention first |
| NRR <100% | Base is contracting | Fix expansion or reduce churn before scaling |
| Revenue churn > logo churn | Losing big customers | Investigate why high-value customers leave |
| Quick Ratio <2 | Leaky bucket (barely outpacing losses) | Fix retention before scaling acquisition |
| Expansion revenue <10% of MRR | No upsell/cross-sell engine | Build expansion paths |
| Revenue concentration >50% in top 10 customers | Existential dependency risk | Diversify customer base |

#### Unit Economics Red Flags
| **Red Flag** | **What It Means** | **Action** |
|--------------|-------------------|------------|
| LTV:CAC <1.5:1 | Buying revenue at a loss | Reduce CAC or increase LTV before scaling |
| Payback >24 months | Cash trap (long cash recovery) | Negotiate annual upfront or reduce CAC |
| Gross margin <60% | Low profitability per dollar | Increase prices or reduce COGS |
| CAC increasing while LTV flat | Unit economics degrading | Optimize conversion or reduce sales cycle |
| Contribution margin <40% | Unprofitable after variable costs | Cut variable costs or increase prices |

#### Capital Efficiency Red Flags
| **Red Flag** | **What It Means** | **Action** |
|--------------|-------------------|------------|
| Runway <6 months | Survival crisis | Raise capital immediately or cut burn |
| Net burn accelerating without revenue growth | Burning faster without results | Cut costs or increase revenue urgency |
| OpEx growing faster than revenue | Negative operating leverage | Freeze hiring; optimize spend |
| Rule of 40 <25 | Burning cash without growth | Improve growth or cut to profitability |
| Magic Number <0.5 | S&M engine broken | Fix GTM efficiency before scaling spend |

---

### When to Use Which Metric

**Prioritizing features:**
- Revenue impact → Revenue, ARPU, Expansion Revenue
- Margin impact → Gross Margin, Contribution Margin
- ROI → LTV impact, Development cost

**Evaluating channels:**
- Acquisition cost → CAC, CAC by Channel
- Customer value → LTV, NRR by Channel
- Payback → Payback Period, CAC Payback by Channel
- Scalability → Magic Number

**Pricing decisions:**
- Monetization → ARPU, ARPA, ACV
- Impact → Churn Rate, NRR, Expansion Revenue
- Efficiency → CAC Payback (will pricing change affect it?)

**Business health:**
- Growth → Revenue Growth, MRR/ARR Growth
- Retention → Churn Rate, NRR, Quick Ratio
- Economics → LTV:CAC, Payback Period, Gross Margin
- Efficiency → Rule of 40, Magic Number, Operating Leverage
- Survival → Burn Rate, Runway

**Board/investor reporting:**
- Key metrics: ARR, Revenue Growth %, NRR, LTV:CAC, Rule of 40, Magic Number, Burn Rate, Runway
- Stage-specific: Early stage emphasize growth + unit economics; Growth stage emphasize Rule of 40 + Magic Number; Scale stage emphasize profitability + efficiency

---

## Examples

### Example 1: Feature Investment Sanity Check

You are deciding whether to build a premium export feature.

1. Use Framework 1 (Should We Build This Feature?)
2. Pull baseline metrics: ARPU, Gross Margin, LTV, Contribution Margin
3. Model optimistic, base, and downside adoption
4. Reject if contribution margin turns negative in downside case

Quick output:
- Base case ROI: 3.8x
- Contribution margin impact: +4 points
- Decision: Build now, with a 90-day post-launch check on churn and expansion

### Example 2: Channel Scale Decision

Paid social is generating many signups but weak retention.

1. Use Framework 2 (Should We Scale This Acquisition Channel?)
2. Check CAC, LTV:CAC, Payback Period, and NRR by channel
3. Compare against best-performing channel, not company average

Quick output:
- LTV:CAC: 1.6:1
- Payback: 26 months
- NRR: 88%
- Decision: Do not scale; cap spend and run targeted optimization tests

---

## Common Pitfalls

- Using blended company averages instead of cohort or channel-level metrics
- Scaling acquisition when Quick Ratio is weak and retention is deteriorating
- Treating high LTV:CAC as sufficient without checking payback and runway impact
- Raising prices based on ARPU lift alone without modeling churn and contraction
- Comparing benchmarks across mismatched company stages or business models
- Tracking many metrics without a clear decision question

---

## References

### Related Skills (Deep Dives)
- `saas-revenue-growth-metrics` — Detailed guidance on revenue, retention, and growth metrics (13 metrics)
- `saas-economics-efficiency-metrics` — Detailed guidance on unit economics and capital efficiency (17 metrics)
- `feature-investment-advisor` — Uses these metrics to evaluate feature ROI
- `acquisition-channel-advisor` — Uses these metrics to evaluate channel viability
- `finance-based-pricing-advisor` — Uses these metrics to evaluate pricing changes
- `business-health-diagnostic` — Uses these metrics to diagnose business health

### External Resources
- **Bessemer Venture Partners:** "SaaS Metrics 2.0" — Comprehensive SaaS benchmarking
- **David Skok (Matrix Partners):** "SaaS Metrics" blog series — Deep dive on unit economics
- **Tomasz Tunguz (Redpoint):** SaaS benchmarking research and blog
- **ChartMogul, Baremetrics, ProfitWell:** SaaS analytics platforms with metric definitions
- **SaaStr:** Annual SaaS benchmarking surveys

### Provenance
- Adapted from `research/finance/Finance_QuickRef.md`
- Formulas from `research/finance/Finance for Product Managers.md`
- Decision frameworks from `research/finance/Finance_For_PMs.Putting_It_Together_Synthesis.md`
