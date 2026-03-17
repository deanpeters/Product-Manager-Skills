---
name: saas-economics-efficiency-metrics
description: Evaluate SaaS unit economics and capital efficiency. Use when deciding whether the business can scale efficiently or needs correction.
intent: >-
  Determine whether your SaaS business model is fundamentally viable and capital-efficient. Use this to calculate unit economics, assess profitability, manage cash runway, and decide when to scale vs. optimize. Essential for fundraising, board reporting, and making smart investment trade-offs.
type: component
best_for:
  - "Checking whether a SaaS model is financially viable"
  - "Reviewing CAC, LTV, payback, burn, and Rule of 40 together"
  - "Preparing efficiency analysis for a board or leadership review"
scenarios:
  - "Evaluate our SaaS unit economics before we scale paid acquisition"
  - "Help me analyze CAC payback, LTV, and burn for our product"
  - "I need a SaaS efficiency check for our board deck"
---


## Purpose

Determine whether your SaaS business model is fundamentally viable and capital-efficient. Use this to calculate unit economics, assess profitability, manage cash runway, and decide when to scale vs. optimize. Essential for fundraising, board reporting, and making smart investment trade-offs.

## Key Concepts

### Unit Economics Family

Metrics that measure profitability at the customer level—the foundation of sustainable SaaS.

**Gross Margin** — Percentage of revenue remaining after direct costs (COGS).
- **Why PMs care:** A feature that generates $1M revenue at 80% margin is worth far more than $1M at 30% margin. Margin determines which features to prioritize.
- **Formula:** `(Revenue - COGS) / Revenue × 100`
- **COGS includes:** Hosting, infrastructure, payment processing, customer onboarding costs
- **Benchmark:** SaaS 70-85% good; <60% concerning

**CAC (Customer Acquisition Cost)** — Total cost to acquire one customer.
- **Why PMs care:** Shapes entire go-to-market strategy. Determines which channels are viable and how much you can invest in product-led growth.
- **Formula:** `Total Sales & Marketing Spend / New Customers Acquired`
- **Benchmark:** Varies by model—Enterprise $10K+ ok; SMB <$500 target
- **Include:** Marketing spend, sales salaries, tools, commissions

**LTV (Lifetime Value)** — Total revenue expected from one customer over their lifetime.
- **Why PMs care:** Tells you what you can afford to spend on acquisition. Higher LTV enables premium channels and longer payback periods.
- **Formula (simple):** `ARPU × Average Customer Lifetime (months)`
- **Formula (better):** `ARPU × Gross Margin % / Churn Rate`
- **Formula (advanced):** Account for expansion, discount rates, cohort-specific retention
- **Benchmark:** Must be 3x+ CAC; varies by segment

**LTV:CAC Ratio** — Efficiency of customer acquisition spending.
- **Why PMs care:** Is growth sustainable or are you buying revenue at a loss? Determines when to scale vs. optimize.
- **Formula:** `LTV / CAC`
- **Benchmark:** 3:1 healthy; <1:1 unsustainable; >5:1 might be underinvesting
- **Note:** This ratio alone doesn't tell the full story—also need payback period

**Payback Period** — Months to recover CAC from customer revenue.
- **Why PMs care:** Cash efficiency. Faster payback = reinvest sooner. Slow payback can kill growth even with good LTV:CAC.
- **Formula:** `CAC / (Monthly ARPU × Gross Margin %)`
- **Benchmark:** <12 months great; 12-18 ok; >24 months concerning
- **Critical:** Must have cash to sustain payback period

**Contribution Margin** — Revenue remaining after ALL variable costs (not just COGS).
- **Why PMs care:** True unit profitability. Includes support, processing fees, variable OpEx.
- **Formula:** `(Revenue - All Variable Costs) / Revenue × 100`
- **Variable costs:** COGS + support + payment processing + variable customer success
- **Benchmark:** 60-80% good for SaaS; <40% concerning

**Gross Margin Payback** — Payback period using actual profit, not revenue.
- **Why PMs care:** More accurate than simple payback. Shows true cash recovery time.
- **Formula:** `CAC / (Monthly ARPU × Gross Margin %)`
- **Benchmark:** Typically 1.5-2x longer than simple revenue payback

**CAC Payback by Channel** — Compare payback across acquisition channels.
- **Why PMs care:** Not all channels are created equal. Optimize channel mix based on payback efficiency.
- **Formula:** Calculate CAC and payback separately for each channel
- **Use:** Allocate budget to faster-payback channels when cash-constrained

---

### Capital Efficiency Family

Metrics that measure how efficiently you use cash to grow the business.

**Burn Rate** — Cash consumed per month.
- **Why PMs care:** Determines what you can build and when you need funding. High burn requires aggressive revenue growth.
- **Formula (Gross Burn):** `Monthly Cash Spent (all expenses)`
- **Formula (Net Burn):** `Monthly Cash Spent - Monthly Revenue`
- **Benchmark:** Net burn <$200K manageable for early stage; >$500K needs clear path to revenue

**Runway** — Months until cash runs out.
- **Why PMs care:** Literal survival metric. Dictates timeline for milestones, fundraising, profitability.
- **Formula:** `Cash Balance / Monthly Net Burn`
- **Benchmark:** 12+ months good; 6-12 manageable; <6 months crisis mode
- **Rule:** Raise when you have 6-9 months runway, not 3 months

**OpEx (Operating Expenses)** — Costs to run the business (excluding COGS).
- **Why PMs care:** Your team's salaries live here. Where "efficiency" cuts happen during downturns.
- **Categories:** Sales & Marketing (S&M), Research & Development (R&D), General & Administrative (G&A)
- **Benchmark:** Should grow slower than revenue as you scale (operating leverage)

**Net Income (Profit Margin)** — Actual profit or loss after all expenses.
- **Why PMs care:** True bottom line. Are you making money? Can you self-fund growth?
- **Formula:** `Revenue - All Expenses (COGS + OpEx)`
- **Benchmark:** Early SaaS often negative (growth mode); mature should be 10-20%+ margin

**Working Capital Impact** — Cash timing differences between revenue recognition and cash collection.
- **Why PMs care:** Annual contracts paid upfront boost cash. Monthly billing delays cash. Affects runway calculations.
- **Example:** $1M annual contract paid upfront = $1M cash now, not $83K/month
- **Use:** Understand cash vs. revenue timing when planning runway

---

### Efficiency Ratios Family

Composite metrics that measure growth vs. profitability trade-offs.

**Rule of 40** — Growth rate + profit margin should exceed 40%.
- **Why PMs care:** Framework for balancing growth vs. efficiency. Guides when to prioritize profitability over growth.
- **Formula:** `Revenue Growth Rate % + Profit Margin %`
- **Benchmark:** >40 healthy; 25-40 acceptable; <25 concerning
- **Example:** 60% growth + (-20%) margin = 40 (healthy growth-mode SaaS)
- **Example:** 20% growth + 25% margin = 45 (healthy mature SaaS)

**Magic Number** — Sales & marketing efficiency.
- **Why PMs care:** Is your GTM engine working? Should you scale spend or optimize first?
- **Formula:** `(Current Quarter Revenue - Previous Quarter Revenue) × 4 / Previous Quarter S&M Spend`
- **Benchmark:** >0.75 efficient; 0.5-0.75 ok; <0.5 fix before scaling
- **Note:** "× 4" annualizes quarterly revenue change

**Operating Leverage** — How revenue growth compares to cost growth.
- **Why PMs care:** Are you scaling efficiently? Revenue should grow faster than costs.
- **Measure:** Revenue growth rate vs. OpEx growth rate over time
- **Good:** Revenue growth 50%, OpEx growth 30% (positive leverage)
- **Bad:** Revenue growth 20%, OpEx growth 40% (negative leverage)

**Unit Economics** — General term for profitability of each "unit" (customer, seat, transaction).
- **Why PMs care:** Is the business model fundamentally viable at the unit level?
- **Calculate:** Revenue per unit - Cost per unit
- **Requirement:** Positive contribution required; aim for >$0 after all variable costs

---

---

## Application

### Step 1: Calculate Unit Economics

Use the templates in `template.md` to calculate your unit economics metrics.

#### Gross Margin
```
Gross Margin = (Revenue - COGS) / Revenue × 100

COGS includes:
- Hosting & infrastructure costs
- Payment processing fees
- Customer onboarding costs
- Direct delivery costs
```

**Example:**
- Revenue: $1,000,000
- COGS: $200,000 (hosting $120K, processing $50K, onboarding $30K)
- Gross Margin = ($1M - $200K) / $1M = 80%

**Quality checks:**
- Is gross margin improving as you scale? (Should benefit from economies of scale)
- Which products/features have highest margins? (Prioritize those)
- Are margins >70%? (SaaS should be high-margin)

---

#### CAC (Customer Acquisition Cost)
```
CAC = Total Sales & Marketing Spend / New Customers Acquired

Include in S&M spend:
- Marketing salaries & tools
- Sales salaries & commissions
- Advertising & paid channels
- SDR/BDR team costs
```

**Example:**
- Sales & Marketing Spend: $500,000/month
- New Customers: 100/month
- CAC = $500,000 / 100 = $5,000

**Quality checks:**
- Is CAC consistent across channels? (Calculate by channel)
- Is CAC increasing or decreasing over time? (Should decrease with scale)
- Does CAC vary by customer segment? (SMB vs. Enterprise)

---

#### LTV (Lifetime Value)
```
LTV (Simple) = ARPU × Average Customer Lifetime (months)

LTV (Better) = ARPU × Gross Margin % / Monthly Churn Rate

LTV (Advanced) = Account for expansion, cohort-specific retention, discount rate
```

**Example (Simple):**
- ARPU: $500/month
- Average Lifetime: 36 months
- LTV = $500 × 36 = $18,000

**Example (Better):**
- ARPU: $500/month
- Gross Margin: 80%
- Monthly Churn: 2%
- LTV = ($500 × 80%) / 2% = $400 / 0.02 = $20,000

**Quality checks:**
- Is LTV growing over time? (From expansion, improved retention)
- Does LTV vary by cohort? (Are new customers more/less valuable?)
- Does LTV vary by segment? (Enterprise vs. SMB)

---

#### LTV:CAC Ratio
```
LTV:CAC Ratio = LTV / CAC
```

**Example:**
- LTV: $20,000
- CAC: $5,000
- LTV:CAC = $20,000 / $5,000 = 4:1

**Quality checks:**
- Is ratio >3:1? (Minimum for sustainable growth)
- Is ratio >5:1? (Might be underinvesting in growth)
- Is ratio improving or degrading over time?

**Interpretation:**
- **<1:1** = Losing money on every customer (unsustainable)
- **1-3:1** = Marginal economics (optimize before scaling)
- **3-5:1** = Healthy (scale confidently)
- **>5:1** = Potentially underinvesting (could grow faster)

---

#### Payback Period
```
Payback Period (months) = CAC / (Monthly ARPU × Gross Margin %)
```

**Example:**
- CAC: $5,000
- Monthly ARPU: $500
- Gross Margin: 80%
- Payback = $5,000 / ($500 × 80%) = $5,000 / $400 = 12.5 months

**Quality checks:**
- Is payback <12 months? (Excellent)
- Is payback <18 months? (Acceptable)
- Do you have cash runway to sustain payback period?

**Critical insight:** 4:1 LTV:CAC with 36-month payback is a cash trap. 3:1 LTV:CAC with 8-month payback is better for growth.

---

#### Contribution Margin
```
Contribution Margin = (Revenue - All Variable Costs) / Revenue × 100

Variable Costs include:
- COGS
- Support costs (variable component)
- Payment processing
- Variable customer success costs
```

**Example:**
- Revenue: $1,000,000
- COGS: $200,000
- Variable Support: $50,000
- Payment Processing: $30,000
- Contribution Margin = ($1M - $280K) / $1M = 72%

**Quality checks:**
- Is contribution margin >60%? (Good for SaaS)
- Are certain products/segments lower margin? (Consider sunsetting)
- Does margin improve with scale?

---

### Step 2: Calculate Capital Efficiency

#### Burn Rate
```
Gross Burn Rate = Total Monthly Cash Spent
Net Burn Rate = Total Monthly Cash Spent - Monthly Revenue
```

**Example:**
- Monthly Expenses: $800,000
- Monthly Revenue: $400,000
- Gross Burn: $800,000/month
- Net Burn: $400,000/month

**Quality checks:**
- Is net burn decreasing over time? (Path to profitability)
- Is burn rate sustainable given runway?
- What's the burn rate relative to revenue? (Burn multiple)

---

#### Runway
```
Runway (months) = Cash Balance / Monthly Net Burn
```

**Example:**
- Cash Balance: $6,000,000
- Net Burn: $400,000/month
- Runway = $6M / $400K = 15 months

**Quality checks:**
- Do you have >12 months runway? (Healthy)
- Do you have <6 months runway? (Crisis—raise now or cut burn)
- Can you reach next milestone before runway ends?

**Rule:** Start fundraising at 6-9 months runway, not 3 months.

---

#### Operating Expenses (OpEx)
```
OpEx = Sales & Marketing + R&D + General & Administrative

Track as % of Revenue:
S&M as % of Revenue
R&D as % of Revenue
G&A as % of Revenue
```

**Example:**
- Revenue: $10M/year
- S&M: $5M (50% of revenue)
- R&D: $3M (30% of revenue)
- G&A: $1M (10% of revenue)
- Total OpEx: $9M (90% of revenue)

**Quality checks:**
- Are OpEx categories growing slower than revenue? (Operating leverage)
- Is S&M spend efficient? (Check magic number)
- Is G&A <15% of revenue? (Should stay low)

---

#### Net Income (Profit Margin)
```
Net Income = Revenue - COGS - OpEx
Profit Margin % = Net Income / Revenue × 100
```

**Example:**
- Revenue: $10M
- COGS: $2M
- OpEx: $9M
- Net Income = $10M - $2M - $9M = -$1M (loss)
- Profit Margin = -10%

**Quality checks:**
- Is profit margin improving over time? (Path to profitability)
- At current growth rate, when will you break even?
- Are you investing losses in growth? (Acceptable if LTV:CAC is healthy)

---

### Step 3: Calculate Efficiency Ratios

#### Rule of 40
```
Rule of 40 = Revenue Growth Rate % + Profit Margin %
```

**Example 1 (Growth Mode):**
- Revenue Growth: 80% YoY
- Profit Margin: -30%
- Rule of 40 = 80% + (-30%) = 50 ✅ Healthy

**Example 2 (Mature):**
- Revenue Growth: 25% YoY
- Profit Margin: 20%
- Rule of 40 = 25% + 20% = 45 ✅ Healthy

**Example 3 (Problem):**
- Revenue Growth: 30% YoY
- Profit Margin: -35%
- Rule of 40 = 30% + (-35%) = -5 🚨 Unhealthy

**Quality checks:**
- Is Rule of 40 >40? (Healthy balance)
- Is Rule of 40 >25? (Acceptable)
- Is Rule of 40 <25? (Burning cash without sufficient growth)

**Trade-offs:**
- Early stage: Maximize growth, accept losses (60% growth, -20% margin = 40)
- Growth stage: Balance (40% growth, 5% margin = 45)
- Mature: Prioritize profitability (20% growth, 25% margin = 45)

---

#### Magic Number
```
Magic Number = (Current Quarter Revenue - Previous Quarter Revenue) × 4 / Previous Quarter S&M Spend
```

**Example:**
- Q2 Revenue: $2.5M
- Q1 Revenue: $2.0M
- Q1 S&M Spend: $800K
- Magic Number = ($2.5M - $2.0M) × 4 / $800K = $2M / $800K = 2.5

**Quality checks:**
- Is magic number >0.75? (Efficient—scale S&M spend)
- Is magic number 0.5-0.75? (Acceptable—optimize before scaling)
- Is magic number <0.5? (Inefficient—fix GTM before spending more)

**Interpretation:**
- **>1.0** = For every $1 in S&M, you get $1+ in new ARR (excellent)
- **0.75-1.0** = Efficient, scale confidently
- **0.5-0.75** = Marginal, optimize before scaling
- **<0.5** = Inefficient, fix before investing more

---

#### Operating Leverage
Track over time to see if you're scaling efficiently.

**Example:**
| Quarter | Revenue | YoY Growth | OpEx | YoY Growth | Leverage |
|---------|---------|------------|------|------------|----------|
| Q1 2024 | $8M | - | $6M | - | - |
| Q2 2024 | $10M | 25% | $7M | 17% | Positive ✅ |
| Q3 2024 | $12M | 20% | $9M | 29% | Negative ⚠️ |

**Quality checks:**
- Is revenue growing faster than OpEx? (Positive leverage)
- Are you scaling OpEx too fast relative to revenue?
- Which OpEx category is growing fastest? (R&D, S&M, G&A)

---

### Step 4: Analyze by Segment and Channel

**Unit economics vary dramatically by segment:**

| Segment | CAC | LTV | LTV:CAC | Payback | Gross Margin |
|---------|-----|-----|---------|---------|--------------|
| SMB | $500 | $2,000 | 4:1 | 8 months | 75% |
| Mid-Market | $5,000 | $25,000 | 5:1 | 12 months | 80% |
| Enterprise | $50,000 | $300,000 | 6:1 | 24 months | 85% |

**Quality checks:**
- Which segment has best unit economics?
- Which segment has fastest payback? (Prioritize when cash-constrained)
- Which segment has highest LTV? (Invest in retention/expansion)

---

## Examples

See `examples/` folder for detailed scenarios. Mini examples below:

### Example 1: Healthy Unit Economics

**Company:** CloudAnalytics (mid-market analytics SaaS)

**Unit Economics:**
- CAC: $8,000
- LTV: $40,000
- LTV:CAC: 5:1 ✅
- Payback Period: 10 months ✅
- Gross Margin: 82% ✅

**Capital Efficiency:**
- Monthly Net Burn: $300K
- Runway: 18 months ✅
- Rule of 40: 55 (40% growth + 15% margin) ✅
- Magic Number: 0.9 ✅

**Analysis:**
- Strong unit economics (5:1 LTV:CAC, 10-month payback)
- Efficient GTM (0.9 magic number)
- Healthy balance (Rule of 40 = 55)
- Sufficient runway (18 months)

**Action:** Scale acquisition aggressively. Economics support growth.

---

### Example 2: Good LTV:CAC, Bad Payback (Cash Trap)

**Company:** EnterpriseCRM (enterprise sales motion)

**Unit Economics:**
- CAC: $80,000
- LTV: $400,000
- LTV:CAC: 5:1 ✅ (looks great!)
- Payback Period: 36 months 🚨 (terrible!)
- Gross Margin: 85%

**Capital Efficiency:**
- Monthly Net Burn: $2M
- Runway: 9 months 🚨
- Average Customer Lifetime: 48 months
- Average Contract: $100K/year

**Analysis:**
- ⚠️ Great LTV:CAC ratio (5:1) masks cash problem
- 🚨 36-month payback with 9-month runway = cash trap
- 🚨 Takes 3 years to recover CAC, but only 9 months of cash
- ⚠️ Customers stay 4 years, so economics work IF you have cash

**Problem:** You'll run out of cash before recovering acquisition costs.

**Actions:**
1. Negotiate upfront annual payments (reduce payback to 12 months)
2. Raise capital to extend runway (need 36+ months to sustain growth)
3. Reduce CAC (shorten sales cycle, improve conversion)
4. Target smaller deals with faster payback (mid-market vs. enterprise)

---

### Example 3: Scaling Too Fast (Negative Operating Leverage)

**Company:** SocialScheduler (SMB social media tool)

**Quarter-over-Quarter Trend:**
| Quarter | Revenue | OpEx | Net Income | Revenue Growth | OpEx Growth |
|---------|---------|------|------------|----------------|-------------|
| Q1 | $1.0M | $800K | -$800K | - | - |
| Q2 | $1.3M | $1.2M | -$1.2M | 30% | 50% 🚨 |
| Q3 | $1.6M | $1.8M | -$1.8M | 23% | 50% 🚨 |

**Analysis:**
- 🚨 OpEx growing FASTER than revenue (50% vs. 23-30%)
- 🚨 Losses accelerating ($800K → $1.8M in 2 quarters)
- 🚨 Negative operating leverage (should be positive)
- ⚠️ Scaling S&M and R&D without corresponding revenue growth

**Problem:** Burning cash faster while revenue growth is slowing.

**Actions:**
1. Freeze headcount until revenue catches up
2. Cut inefficient S&M spend (magic number likely <0.5)
3. Focus on improving unit economics before scaling
4. Aim for OpEx growth <revenue growth

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| High LTV Without Checking Payback | "LTV:CAC 6:1, amazing!" but 48-month payback | Pair LTV:CAC with payback. 3:1 at 10mo beats 6:1 at 36mo |
| Ignoring Margin in LTV | "LTV = $100 x 36 = $3,600" using revenue not profit | Use `ARPU x Margin % / Churn Rate` |
| Scaling S&M with Low Magic Number | "Double S&M spend!" at Magic Number 0.3 | Only scale when >0.75. Fix GTM first if <0.5 |
| Simplistic LTV Formulas | "LTV = ARPU x Lifetime" ignoring expansion/discounting | Use sophisticated models for big decisions |
| Forgetting Time Value of Money | "$10K today = $10K in 5 years" | Discount future cash flows for LTV >24 months via NPV |
| Comparing CAC Without Payback | "Channel A $5K CAC < Channel B $8K" | Compare CAC + payback together. Faster payback may win |
| Rule of 40 With No Runway | "Rule of 40 = 50!" but 3mo runway | Pair Rule of 40 with burn rate and runway |
| Blended Unit Economics | "Blended CAC $2K, LTV $10K" | Calculate by segment. One segment may be deeply unprofitable |
| Gross vs. Contribution Margin | "Gross margin 80%!" | Track both. Contribution margin (all variable costs) is the real number |
| Ignoring Working Capital Timing | "12 months runway" but all monthly billing | Cash-based runway differs from revenue-based. Account for payment timing |

---

## References

### Related Skills
- `saas-revenue-growth-metrics` — Revenue, retention, and growth metrics that feed into LTV
- `finance-metrics-quickref` — Fast lookup for all metrics
- `feature-investment-advisor` — Uses margin and contribution calculations for feature ROI
- `acquisition-channel-advisor` — Uses CAC, LTV, payback for channel evaluation
- `business-health-diagnostic` — Uses efficiency metrics for health checks

### External Frameworks
- **David Skok (Matrix Partners):** "SaaS Metrics" blog — Definitive guide to CAC, LTV, payback
- **Bessemer Venture Partners:** "SaaS Metrics 2.0" — Rule of 40, magic number benchmarks
- **Ben Murray:** *The SaaS CFO* — Advanced unit economics modeling
- **Jason Lemkin (SaaStr):** SaaS benchmarking research
- **Brad Feld:** *Venture Deals* — Understanding investor perspective on unit economics

### Provenance
- Adapted from `research/finance/Finance for Product Managers.md`
- Consolidated from `research/finance/Finance_QuickRef.md`
- Common mistakes from `research/finance/Finance_Metrics_Additions_Reference.md`
