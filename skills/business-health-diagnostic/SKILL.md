---
name: business-health-diagnostic
description: Diagnose SaaS business health across growth, retention, efficiency, and capital. Use when preparing a business review or prioritizing urgent fixes.
intent: >-
  Diagnose overall SaaS business health by analyzing growth, retention, unit economics, and capital efficiency metrics together. Use this to identify problems early, prioritize actions by urgency, and deliver a comprehensive health scorecard for board meetings, quarterly reviews, or fundraising preparation.
type: interactive
theme: finance-metrics
best_for:
  - "Getting a complete read on your SaaS business health across all dimensions"
  - "Identifying which metrics are red flags vs. leading indicators"
  - "Preparing for a board meeting or investor review"
scenarios:
  - "Our growth is strong but we're burning cash fast — I need to understand our unit economics before the board meeting"
  - "I'm preparing for a Series A board meeting and need to assess our business health across growth, retention, and efficiency"
estimated_time: "20-30 min"
---


## Purpose

Diagnose overall SaaS business health by analyzing growth, retention, unit economics, and capital efficiency metrics together. Use this to identify problems early, prioritize actions by urgency, and deliver a comprehensive health scorecard for board meetings, quarterly reviews, or fundraising preparation.

## Key Concepts

### The Business Health Framework

A SaaS business is healthy when four dimensions work together:

1. **Growth & Retention** — Are you growing and keeping customers?
   - Revenue growth rate
   - NRR (Net Revenue Retention)
   - Churn rate
   - Quick Ratio

2. **Unit Economics** — Is the business model profitable at the customer level?
   - CAC (Customer Acquisition Cost)
   - LTV (Lifetime Value)
   - LTV:CAC ratio
   - Payback period
   - Gross margin

3. **Capital Efficiency** — Are you using cash efficiently?
   - Burn rate
   - Runway
   - Rule of 40
   - Magic Number

4. **Strategic Position** — Are you positioned for sustainable success?
   - Market positioning (below, at, above market pricing)
   - Competitive moat (network effects, data, brand)
   - Revenue concentration risk
   - Operating leverage

### Stage-Specific Benchmarks

**Early Stage (Pre-$10M ARR):**
- Focus: Product-market fit, unit economics
- Growth: >50% YoY
- LTV:CAC: >3:1
- Gross Margin: >70%
- Runway: >12 months
- Acceptable: Negative margins, high burn (if unit economics work)

**Growth Stage ($10M-$50M ARR):**
- Focus: Scaling efficiently
- Growth: >40% YoY
- NRR: >100%
- Rule of 40: >40
- Magic Number: >0.75
- Acceptable: Moderate burn if growth is strong

**Scale Stage ($50M+ ARR):**
- Focus: Profitability, efficiency
- Growth: >25% YoY
- NRR: >110%
- Rule of 40: >40
- Profit Margin: >10%
- Required: Positive or near-positive cash flow

### Red Flag Categories

**Critical (Fix immediately):**
- Runway <6 months
- LTV:CAC <1.5:1
- Churn accelerating cohort-over-cohort
- NRR <90%
- Magic Number <0.3

**High Priority (Fix within quarter):**
- Rule of 40 <25
- Payback >24 months
- Quick Ratio <2
- Gross margin <60%
- Revenue concentration >50% in top 10 customers

**Medium Priority (Address within 6 months):**
- NRR 90-100% (flat, not growing)
- Magic Number 0.3-0.5
- Operating leverage negative
- Churn rate stable but high (>5% monthly)

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the default interaction protocol for this skill.

It defines:
- session heads-up + entry mode (Guided, Context dump, Best guess)
- one-question turns with plain-language prompts
- progress labels (for example, Context Qx/8 and Scoring Qx/5)
- interruption handling and pause/resume behavior
- numbered recommendations at decision points
- quick-select numbered response options for regular questions (include `Other (specify)` when useful)

This file defines the domain-specific assessment content. If there is a conflict, follow this file's domain logic.

## Application

This interactive skill asks **up to 4 adaptive questions**, then delivers a comprehensive diagnostic with prioritized recommendations.

---

### Step 0: Gather Context

**Agent asks:**

"Let's diagnose your business health. I'll need metrics across four dimensions: growth, retention, unit economics, and capital efficiency.

**Company context:**
- Stage: (Pre-$10M ARR, $10M-$50M ARR, $50M+ ARR)
- Business model: (PLG, sales-led, hybrid)
- Target market: (SMB, mid-market, enterprise, mixed)

**Why this matters:** Benchmarks vary by stage. Early-stage optimizes for growth; scale-stage optimizes for efficiency.

Please provide the following metrics. Use 'unknown' if you don't have a metric."

---

### Step 1: Growth & Retention Metrics

**Agent asks:**

"**Growth & Retention:**

1. **Revenue:**
   - Current MRR or ARR: $___
   - Revenue growth rate: ___% (MoM or YoY)

2. **Retention:**
   - Monthly churn rate: ___%
   - NRR (Net Revenue Retention): ___%
   - Quick Ratio: ___ (or I can calculate it)

3. **Expansion:**
   - Expansion revenue as % of total MRR: ___%

4. **Cohort trends:**
   - Are recent cohorts retaining better or worse than older cohorts?
     1. Better (improving)
     2. Same (stable)
     3. Worse (degrading)
     4. Unknown"

**Based on answers, agent evaluates:**
- ✅ **Healthy growth:** Growth >40% YoY (growth stage) or >25% (scale stage)
- ✅ **Healthy retention:** NRR >100%, churn <5% monthly, Quick Ratio >2
- 🚨 **Growth problems:** Growth <20% YoY
- 🚨 **Retention problems:** NRR <100%, churn >5%, cohort degradation

---

### Step 2: Unit Economics Metrics

**Agent asks:**

"**Unit Economics:**

1. **Acquisition:**
   - CAC (Customer Acquisition Cost): $___
   - Blended or by channel? (If by channel, what's your best channel CAC?)

2. **Value:**
   - LTV (Lifetime Value): $___
   - LTV:CAC ratio: ___ (or I can calculate it)
   - Payback period: ___ months (or I can calculate it)

3. **Margins:**
   - Gross margin: ___%
   - Contribution margin (if known): ___%

4. **Trends:**
   - Is CAC increasing, stable, or decreasing over time?
     1. Decreasing (improving efficiency)
     2. Stable
     3. Increasing (diminishing returns)
     4. Unknown"

**Based on answers, agent evaluates:**
- ✅ **Healthy economics:** LTV:CAC >3:1, payback <12 months, gross margin >70%
- ⚠️ **Marginal economics:** LTV:CAC 2-3:1, payback 12-18 months
- 🚨 **Poor economics:** LTV:CAC <2:1, payback >24 months, gross margin <60%

---

### Step 3: Capital Efficiency Metrics

**Agent asks:**

"**Capital Efficiency:**

1. **Cash:**
   - Cash balance: $___
   - Monthly net burn rate: $___
   - Runway: ___ months (or I can calculate it)

2. **Efficiency ratios:**
   - Rule of 40: ___ (Growth % + Profit Margin %) (or I can calculate it)
   - Magic Number: ___ (S&M efficiency) (or I can calculate it)

3. **Operating expenses:**
   - S&M as % of revenue: ___%
   - R&D as % of revenue: ___%
   - Is OpEx growing faster than revenue?
     1. No (positive operating leverage)
     2. Yes (negative operating leverage)
     3. Unknown

4. **Profitability:**
   - Profit margin: ___%
   - Path to profitability: (already profitable, 6-12 months, 12-24 months, >24 months, unknown)"

**Based on answers, agent evaluates:**
- ✅ **Healthy efficiency:** Rule of 40 >40, magic number >0.75, runway >12 months
- ⚠️ **Acceptable efficiency:** Rule of 40 25-40, magic number 0.5-0.75, runway 6-12 months
- 🚨 **Poor efficiency:** Rule of 40 <25, magic number <0.5, runway <6 months

---

### Step 4: Deliver Comprehensive Diagnostic

**Agent synthesizes all metrics and delivers:**

1. **Overall Health Score** — Healthy / Moderate / Concerning / Critical
2. **Dimension Scores** — Growth, Retention, Economics, Efficiency
3. **Red Flags** — Critical, High Priority, Medium Priority
4. **Prioritized Recommendations** — Top 3-5 actions with expected impact
5. **Stage-Appropriate Benchmarks** — How you compare to peers

---

#### Diagnostic Pattern 1: Healthy Business

**When:**
- Growth, retention, economics, and efficiency all meet stage-appropriate benchmarks
- No critical red flags
- Improving trends

**Output:**

"## ✅ Overall Health: **Healthy**

Your business shows strong fundamentals across all dimensions.

---

### Health Scorecard

| Dimension | Score | Status |
|-----------|-------|--------|
| **Growth & Retention** | ✅ Healthy | Growth ___% YoY, NRR ___%, Churn ___% |
| **Unit Economics** | ✅ Healthy | LTV:CAC ___:1, Payback ___ months |
| **Capital Efficiency** | ✅ Healthy | Rule of 40: ___, Runway ___ months |
| **Overall** | ✅ **Healthy** | Strong position for scaling |

---

### Key Strengths

1. **[Specific strength 1]**
   - Metric: [e.g., NRR 120%]
   - Why it matters: [Expanding within base without new logos]

2. **[Specific strength 2]**
   - Metric: [e.g., LTV:CAC 5:1]
   - Why it matters: [Sustainable unit economics support scaling]

3. **[Specific strength 3]**
   - Metric: [e.g., Rule of 40 = 65]
   - Why it matters: [Excellent balance of growth and efficiency]

---

### Opportunities for Optimization

Even healthy businesses can improve. Here are your top opportunities:

**1. [Opportunity 1]**
- Current: [e.g., Magic Number 0.9]
- Opportunity: [Could scale S&M spend 2x and maintain efficiency]
- Impact: [+$___ MRR/month]

**2. [Opportunity 2]**
- Current: [e.g., Expansion revenue 15% of total]
- Opportunity: [Build upsell paths, target 25% expansion revenue]
- Impact: [NRR 110% → 120%]

**3. [Opportunity 3]**
- Current: [e.g., CAC $500, stable]
- Opportunity: [Improve conversion, reduce CAC to $400]
- Impact: [Faster payback, better LTV:CAC]

---

### Recommended Actions (Next Quarter)

**Priority 1: Scale what's working**
- [e.g., Double content marketing budget (best channel)]
- Expected impact: [+___ customers/month, +$___ MRR]

**Priority 2: Expand within base**
- [e.g., Launch premium tier for 20% of customers]
- Expected impact: [NRR 110% → 115%]

**Priority 3: Improve efficiency**
- [e.g., Optimize paid acquisition (reduce CAC 10%)]
- Expected impact: [Payback 8mo → 7mo]

---

### Monitor These Metrics

**Weekly:**
- NRR (should stay >___%)
- Churn rate (should stay <___%)
- Quick Ratio (should stay >___)

**Monthly:**
- Rule of 40 (should stay >___)
- Magic Number (should stay >___)
- LTV:CAC (should stay >___:1)

**Quarterly:**
- Cohort retention trends
- Revenue concentration risk
- Operating leverage

---

### Benchmarks (Your Stage: [Growth/Scale])

| Metric | Your Performance | Benchmark | Status |
|--------|------------------|-----------|--------|
| Growth Rate | ___% | >40% (growth) / >25% (scale) | ✅ |
| NRR | ___% | >100% | ✅ |
| LTV:CAC | ___:1 | >3:1 | ✅ |
| Rule of 40 | ___ | >40 | ✅ |
| Gross Margin | ___% | >70% | ✅ |

You're performing at or above benchmarks across the board."

---

#### Diagnostic Pattern 2: Moderate Health (Fixable Issues)

**When:**
- Most metrics acceptable, but 1-2 dimensions have problems
- Medium-priority red flags
- Solvable with focus

**Output:**

"## ⚠️ Overall Health: **Moderate** (Fixable Issues)

Your business has good fundamentals but needs attention in [specific dimension].

---

### Health Scorecard

| Dimension | Score | Status |
|-----------|-------|--------|
| **Growth & Retention** | [✅ / ⚠️ / 🚨] | [Details] |
| **Unit Economics** | [✅ / ⚠️ / 🚨] | [Details] |
| **Capital Efficiency** | [✅ / ⚠️ / 🚨] | [Details] |
| **Overall** | ⚠️ **Moderate** | [Primary issue area] needs attention |

---

### Red Flags Identified

**High Priority** 🚨
1. **[Specific red flag]**
   - Metric: [e.g., NRR 95%]
   - Threshold: [Should be >100%]
   - Impact: [Base is contracting, not expanding]
   - Fix by: [End of quarter]

**Medium Priority** ⚠️
1. **[Specific issue]**
   - Metric: [e.g., Magic Number 0.6]
   - Threshold: [Should be >0.75]
   - Impact: [S&M spend moderately efficient, room for improvement]
   - Fix by: [6 months]

---

### Root Cause Analysis

**Primary Issue: [e.g., Retention & Expansion]**

**Symptoms:**
- NRR 95% (should be >100%)
- Churn rate 5% monthly (should be <3%)
- Expansion revenue only 10% of MRR (should be 20-30%)

**Diagnosis:**
[e.g., Customers are churning before they expand. Onboarding is weak, no clear upsell paths.]

**Impact:**
- Lost MRR: [Calculate churn impact]
- Missed expansion: [Calculate expansion opportunity]
- Total impact: [Combined revenue loss]

---

### Prioritized Action Plan

**Immediate (Next 30 days):**

**1. Fix [Primary Issue]**
- Action: [Specific step, e.g., "Launch onboarding improvement program"]
- Owner: [PM, Customer Success]
- Target: [Reduce churn 5% → 4%]
- Impact: [Save $___K MRR/month]

**Short-term (Next Quarter):**

**2. [Secondary Action]**
- Action: [e.g., "Build premium tier for upsell"]
- Target: [NRR 95% → 105%]
- Impact: [+$___K expansion MRR]

**3. [Tertiary Action]**
- Action: [e.g., "Optimize S&M spend, improve magic number"]
- Target: [Magic Number 0.6 → 0.8]
- Impact: [More efficient growth]

---

### What Success Looks Like (90 Days)

**Target metrics:**
- NRR: 95% → 105% (+10pp)
- Churn: 5% → 3.5% (-30%)
- Magic Number: 0.6 → 0.8 (+33%)

**Impact:**
- Monthly revenue saved from churn: +$___K
- Expansion revenue: +$___K
- More efficient S&M: [details]

**If you hit these targets, you'll be in 'Healthy' territory.**

---

### Monitor Weekly

**Must-track metrics:**
- Churn rate (track to ensure it's decreasing)
- NRR (track to ensure it's improving)
- Customer feedback (are improvements working?)

**Leading indicators:**
- Onboarding completion rate
- Time-to-value
- Usage metrics (activation, engagement)

---

### What Not to Do

**Don't:**
- Scale acquisition until retention is fixed (you'll just churn faster)
- Ignore expansion (it's easier than new acquisition)
- Wait too long (retention problems compound)"

---

#### Diagnostic Pattern 3: Concerning Health (Urgent Action Required)

**When:**
- Multiple critical red flags
- 2+ dimensions problematic
- Requires immediate intervention

**Output:**

"## 🚨 Overall Health: **Concerning** (Urgent Action Required)

Your business has multiple critical issues that need immediate attention.

---

### Health Scorecard

| Dimension | Score | Status |
|-----------|-------|--------|
| **Growth & Retention** | 🚨 Concerning | [Details] |
| **Unit Economics** | 🚨 Concerning | [Details] |
| **Capital Efficiency** | 🚨 Critical | [Details] |
| **Overall** | 🚨 **Concerning** | Multiple urgent issues |

---

### Critical Red Flags 🚨

**1. [Critical Issue 1 - e.g., Runway]**
- Current: [6 months runway]
- Threshold: [<6 months = crisis]
- Impact: [Survival risk]
- Action: [Raise capital OR cut burn immediately]
- Timeline: [30 days]

**2. [Critical Issue 2 - e.g., Unit Economics]**
- Current: [LTV:CAC 1.2:1]
- Threshold: [<1.5:1 = unsustainable]
- Impact: [Losing money on every customer]
- Action: [Reduce CAC OR increase LTV]
- Timeline: [60 days]

**3. [Critical Issue 3 - e.g., Cohort Degradation]**
- Current: [Newer cohorts churning 2x faster than old]
- Threshold: [Degrading PMF]
- Impact: [Scaling makes problem worse]
- Action: [Stop scaling, fix retention]
- Timeline: [90 days]

---

### Survival Plan (Next 90 Days)

**Week 1-2: Triage**

**Immediate actions:**
1. **Extend runway** (if <6 months)
   - Option A: Raise bridge round ($___K)
   - Option B: Cut burn by ___%
   - Option C: Combination
   - Decision by: [Date]

2. **Stop scaling broken channels**
   - Pause S&M spend on channels with LTV:CAC <2:1
   - Reallocate budget to [best-performing channel]

3. **Assemble crisis team**
   - Daily standups on key metrics
   - Weekly progress reviews

---

**Month 1: Stop the Bleeding**

**Priority 1: Fix Unit Economics**
- Current: LTV:CAC ___:1 (unsustainable)
- Actions:
  1. Reduce CAC: [Specific tactics]
  2. Increase LTV: [Improve retention, add expansion]
- Target: LTV:CAC >2:1 within 30 days

**Priority 2: Improve Retention**
- Current: Churn ___% (too high)
- Actions:
  1. Interview churned customers (identify top 3 reasons)
  2. Fix onboarding (reduce early churn)
  3. Proactive outreach to at-risk accounts
- Target: Reduce churn by 20% within 30 days

---

**Month 2-3: Stabilize**

**Milestone 1: Positive Unit Economics**
- LTV:CAC >2:1 ✅
- Payback <18 months ✅
- Gross margin >60% ✅

**Milestone 2: Slowing Churn**
- Churn decreasing month-over-month
- Cohort degradation stopped
- NRR improving toward 100%

**Milestone 3: Runway Extended**
- 12+ months runway (via fundraise or burn reduction)
- Clear path to next milestone

---

### What Success Looks Like (Day 90)

**Metrics:**
- Runway: ___ months → 12+ months ✅
- LTV:CAC: ___:1 → >2:1 ✅
- Churn: ___% → reduced by 30% ✅
- NRR: ___% → improving toward 100%

**Position:**
- Out of crisis mode
- Stable foundation to rebuild growth
- Clear plan for next 6-12 months

---

### What to Avoid

**Don't:**
- Try to grow your way out of this (fix unit economics first)
- Ignore the data (hope is not a strategy)
- Scale before you fix retention (accelerates failure)
- Wait until runway <3 months to fundraise (too late)

**Do:**
- Focus ruthlessly on retention and unit economics
- Cut costs to extend runway
- Be honest with board/investors about problems
- Move fast (you don't have time to waste)"

---

#### Diagnostic Pattern 4: Critical Health (Existential Crisis)

**When:**
- Runway <3 months OR
- Multiple critical failures (LTV:CAC <1:1, massive churn, no path to profitability)

**Output:**

"## 🚨🚨 Overall Health: **Critical** (Existential Crisis)

Your business is in survival mode. Immediate drastic action required.

[Similar structure to Pattern 3, but more urgent tone, shorter timelines, more drastic measures]

**Immediate Actions (This Week):**
1. Emergency board meeting
2. Fundraise immediately OR cut burn 50%+
3. Stop all non-essential spend
4. Fix top 1-2 critical issues (runway, unit economics)"

---

## Examples

See `examples/` folder. Mini examples below:

### Example 1: Healthy Growth-Stage SaaS

**Metrics:**
- ARR: $20M, Growth: 60% YoY
- NRR: 115%, Churn: 2.5%
- LTV:CAC: 4:1, Payback: 10 months
- Rule of 40: 50, Runway: 18 months

**Diagnosis:** Healthy. Scale aggressively.

---

### Example 2: Moderate Health (Retention Issue)

**Metrics:**
- ARR: $15M, Growth: 40% YoY
- NRR: 95%, Churn: 5%
- LTV:CAC: 3.5:1, Payback: 12 months
- Rule of 40: 38, Runway: 12 months

**Diagnosis:** Moderate. Fix retention before scaling further.

---

### Example 3: Concerning (Multiple Issues)

**Metrics:**
- ARR: $8M, Growth: 25% YoY (slowing)
- NRR: 88%, Churn: 7% (increasing)
- LTV:CAC: 1.8:1, Payback: 20 months
- Rule of 40: 15, Runway: 8 months

**Diagnosis:** Concerning. Urgent action on retention and unit economics required.

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| **Celebrating single metrics** | "Revenue growing 50%!" (ignoring burn, churn) | Look at all four dimensions together |
| **Ignoring stage-specific benchmarks** | "We're not profitable yet, is that bad?" (early-stage) | Use stage-appropriate benchmarks |
| **Focusing on lagging indicators only** | "Churn is 5%, let's watch it" | Track leading indicators (usage, engagement, onboarding) |
| **Not acting on red flags** | "NRR <100% for 3 quarters, we'll fix it eventually" | Set clear timelines; escalate if no improvement |
| **Trying to fix everything at once** | Improving growth, retention, CAC, and efficiency simultaneously | Prioritize top 1-3 issues; fix sequentially |

---

## References

### Related Skills
- `saas-revenue-growth-metrics` — Detailed growth and retention metrics
- `saas-economics-efficiency-metrics` — Detailed unit economics and capital efficiency
- `finance-metrics-quickref` — Fast lookup for all metrics and benchmarks
- `feature-investment-advisor` — Uses health diagnostic to inform feature priorities
- `acquisition-channel-advisor` — Uses health diagnostic to inform channel priorities
- `finance-based-pricing-advisor` — Uses health diagnostic to inform pricing decisions

### External Frameworks
- **Bessemer Venture Partners:** "SaaS Metrics 2.0" — Comprehensive benchmarks
- **David Skok:** "SaaS Metrics" — Unit economics benchmarks
- **OpenView Partners:** SaaS benchmarking reports
- **Battery Ventures:** "State of SaaS" annual report

### Provenance
- Adapted from `research/finance/Finance_QuickRef.md` (Red flags table)
- Decision frameworks from `research/finance/Finance_For_PMs.Putting_It_Together_Synthesis.md`
- Benchmarks from `research/finance/Finance for Product Managers.md`
