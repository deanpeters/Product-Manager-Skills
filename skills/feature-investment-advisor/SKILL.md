---
name: feature-investment-advisor
description: Evaluate feature investments using revenue impact, cost structure, ROI, and strategy. Use when deciding whether a feature deserves investment.
intent: >-
  Guide product managers through evaluating whether to build a feature based on financial impact analysis. Use this to make data-driven prioritization decisions by assessing revenue connection (direct or indirect), cost structure (dev + COGS + OpEx), ROI calculation, and strategic value—then deliver actionable build/don't build recommendations with supporting math.
type: interactive
best_for:
  - "Assessing whether a feature should be built now"
  - "Comparing ROI and strategic value of feature ideas"
  - "Pressure-testing roadmap requests with financial logic"
scenarios:
  - "Should we build SSO for mid-market customers this quarter?"
  - "Evaluate whether an AI assistant feature is worth the investment"
  - "Help me decide if this roadmap request has enough ROI to build"
---


## Purpose

Guide product managers through evaluating whether to build a feature based on financial impact analysis. Use this to make data-driven prioritization decisions by assessing revenue connection (direct or indirect), cost structure (dev + COGS + OpEx), ROI calculation, and strategic value—then deliver actionable build/don't build recommendations with supporting math.

## Key Concepts

### The Feature Investment Framework

A systematic approach to evaluate features financially:

1. **Revenue Connection** — How does this feature impact revenue?
   - Direct monetization (new tier, add-on, usage charges)
   - Indirect monetization (retention, conversion, expansion enablement)

2. **Cost Structure** — What does it cost to build and run?
   - Development cost (one-time investment)
   - COGS impact (ongoing infrastructure, processing)
   - OpEx impact (ongoing support, maintenance)

3. **ROI Calculation** — Is the return worth the investment?
   - Direct monetization: Revenue impact / Development cost
   - Retention features: LTV impact across customer base / Development cost
   - Factor in gross margin, not just revenue

4. **Strategic Value** — Non-financial value that might override pure ROI
   - Competitive moat (prevents churn to competitor)
   - Platform enabler (unlocks future features)
   - Market positioning (needed for enterprise deals)
   - Risk reduction (compliance, security)

---

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

This interactive skill asks **up to 4 adaptive questions**, offering **3-5 enumerated options** at decision points.

---

### Step 0: Gather Context

**Agent asks:**

"Let's evaluate the financial impact of this feature investment. Please provide:

**Feature description:**
- What's the feature? (1-2 sentences)
- Target customer segment (SMB, mid-market, enterprise, all)

**Current business context:**
- Current MRR/ARR (or customer count if pre-revenue)
- Current ARPU/ARPA
- Current monthly churn rate
- Gross margin %

**Constraints:**
- Development cost estimate (team size × time)
- Any ongoing COGS or OpEx implications?

You can provide estimates if you don't have exact numbers."

---

### Step 1: Identify Revenue Connection

**Agent asks:**

"How does this feature impact revenue? Choose the option that best describes the revenue connection:

1. **Direct monetization (new revenue stream)** — We'll charge for this (new pricing tier, paid add-on, usage-based fee)
2. **Retention improvement (reduce churn)** — Addresses key churn reason; keeps customers from leaving
3. **Conversion improvement (trial-to-paid)** — Helps convert free/trial users to paid customers
4. **Expansion enabler (upsell/cross-sell)** — Creates upsell path or drives usage-based expansion
5. **No direct revenue impact** — Table stakes, platform improvement, or strategic value only

Choose a number, or describe a custom revenue connection."

**Based on selection, agent adapts:**

**If 1 (Direct monetization):**
- "What pricing are you considering?"
- "What % of customers do you expect to adopt this?" (conservative, base, optimistic)
- Calculate: `Potential Monthly Revenue = Customer Base × Adoption Rate × Price`

**If 2 (Retention improvement):**
- "What % of churn does this feature address?" (e.g., "30% of churned customers cited this gap")
- "What churn reduction do you expect?" (e.g., "5% → 4% monthly churn")
- Calculate: `LTV Impact = Increase in Customer Lifetime × Customer Base × ARPU × Margin`

**If 3 (Conversion improvement):**
- "Current trial-to-paid conversion rate?"
- "Expected conversion lift?" (e.g., "20% → 25% conversion")
- Calculate: `Additional MRR = Trial Users × Conversion Lift × ARPU`

**If 4 (Expansion enabler):**
- "What expansion opportunity does this create?" (upsell tier, usage growth, add-on)
- "What % of customers will expand?"
- Calculate: `Expansion MRR = Customer Base × Expansion Rate × ARPU Increase`

**If 5 (No direct revenue impact):**
- Skip to strategic value assessment

---

### Step 2: Assess Cost Structure

**Agent asks:**

"What's the cost structure for this feature?

**Development cost (one-time):**
- Team size: ___ engineers
- Time estimate: ___ weeks/months
- Estimated dev cost: $___

**Ongoing costs (if any):**
- COGS impact: $___ /month (hosting, infrastructure, processing)
- OpEx impact: $___ /month (support, maintenance)

If no ongoing costs, enter $0."

**Agent calculates:**
- One-time investment: Development cost
- Ongoing monthly cost: COGS + OpEx
- Contribution margin impact: `(Revenue - COGS) / Revenue`

**Agent flags:**
- If COGS is >20% of projected revenue: "⚠️ This feature significantly dilutes margins"
- If ongoing costs are high relative to revenue: "⚠️ Consider if this is sustainable"

---

### Step 3: Evaluate Constraints and Timing

**Agent asks:**

"What constraints or timing considerations apply?

1. **Time-sensitive competitive threat** — Competitor launched this; we're losing deals
2. **Limited budget/team capacity** — We can only build one major feature this quarter
3. **Dependencies on other work** — Requires platform improvements or other features first
4. **No major constraints** — We have capacity and flexibility

Choose a number, or describe your constraints."

**Based on selection:**

**If 1 (Competitive threat):**
- Strategic value increases (churn prevention)
- Urgency factor in recommendation

**If 2 (Limited capacity):**
- Compare ROI against other features in backlog
- Recommend stack ranking

**If 3 (Dependencies):**
- Flag dependency risk
- Suggest sequencing

**If 4 (No constraints):**
- Proceed to recommendations

---

### Step 4: Deliver Recommendations

**Agent synthesizes:**
- Revenue impact (from Step 1)
- Cost structure (from Step 2)
- Constraints (from Step 3)
- ROI calculation
- Strategic value assessment

**Agent offers 3-4 recommendations:**

---

#### Recommendation Pattern 1: Strong Financial Case

**When:**
- ROI >3:1 (direct monetization) or LTV impact >10:1 (retention/expansion)
- Positive contribution margin
- No major red flags

**Recommendation:**

"**Build now** — Strong financial case

**Revenue Impact:**
- [Direct/Indirect revenue impact calculation]
- Conservative estimate: $___/month
- Optimistic estimate: $___/month

**Cost:**
- Development: $___
- Ongoing COGS/OpEx: $___/month
- Net margin impact: ___%

**ROI:**
- Year 1 ROI: ___:1
- Payback period: ___ months

**Why this makes sense:**
[Specific reasoning based on numbers]

**Next steps:**
1. Validate pricing/adoption assumptions with customer research
2. Build MVP to test core value prop
3. Monitor [specific metric] to measure impact"

---

#### Recommendation Pattern 2: Weak Financial Case, Build Anyway (Strategic)

**When:**
- ROI <2:1 or marginal financial impact
- But high strategic value (competitive, platform, compliance)

**Recommendation:**

"**Build for strategic reasons (financial case is marginal)**

**Financial Reality:**
- Revenue impact: $___/month (modest)
- Development cost: $___
- ROI: ___:1 (below 3:1 threshold)

**Strategic Value:**
- [Competitive moat / Platform enabler / Market requirement]
- Prevents churn to competitor X
- Required for enterprise segment (30% of pipeline)

**Recommendation:**
Build, but monitor closely:
1. Track adoption vs. projections
2. Measure churn impact (target: reduce churn by ___%)
3. Re-evaluate after 6 months if adoption is low

**Risk:**
Opportunity cost—other features may have better ROI"

---

#### Recommendation Pattern 3: Don't Build (Poor ROI)

**When:**
- ROI <1:1 (direct monetization) or negative LTV impact
- Margin-diluting
- No compelling strategic value

**Recommendation:**

"**Don't build** — Financial case doesn't support investment

**Why:**
- Revenue impact: $___/month
- Development cost: $___
- ROI: ___:1 (below breakeven)
- Margin impact: Dilutes gross margin from ___% to ___%

**Alternative approaches:**
1. **Reduce scope** — Can we build a simpler version at 50% cost?
2. **Change monetization** — Can we charge more or differently?
3. **Deprioritize** — Focus on higher-ROI features like [alternative]

**What would need to change:**
- If adoption rate increases from ___% to ___%, ROI becomes viable
- If we can reduce dev cost to $___, payback becomes acceptable"

---

#### Recommendation Pattern 4: Build Later / Need More Data

**When:**
- Assumptions are highly uncertain
- Revenue impact depends on unvalidated hypotheses
- Medium strategic value

**Recommendation:**

"**Build later** — Validate assumptions first

**Current uncertainty:**
- Adoption rate assumption: ___% (needs validation)
- Churn impact: ___% reduction (hypothesis, not proven)
- Pricing unknown

**What to validate:**
1. Run feature demand survey with 50+ customers
2. Prototype and test willingness-to-pay
3. Interview churned customers to confirm this addresses churn reason

**Decision criteria:**
- If ___% of customers say they'd pay $___, build
- If churn interviews confirm this is top 3 reason, build
- Otherwise, deprioritize

**Timeline:**
- Spend 2-4 weeks validating
- Re-evaluate with real data"

---

### Step 5: Allow Follow-Up Questions

**Agent offers:**

"Do you want to:
1. See the detailed math breakdown
2. Compare this to another feature
3. Adjust assumptions (pricing, adoption, cost)
4. Export recommendation summary

Or, ask any follow-up questions."

**Agent can:**
- Show detailed calculations
- Sensitivity analysis (what if adoption is 2x? 0.5x?)
- Compare multiple features side-by-side
- Export summary for stakeholders

---

## Examples

See `examples/` folder for sample conversation flows. Mini examples below:

### Example 1: Direct Monetization (Time Tracking Add-On)

**User:** "We're considering building time tracking as a paid add-on."

**Agent:** [Gathers context]

**User provides:**
- Current: 1,000 customers, $500 ARPU, 80% gross margin
- Feature: Time tracking add-on, $10/user/month
- Dev cost: $100K (2 engineers × 3 months)
- Adoption estimate: 20% of customers

**Agent calculates:**
- Customers with 10 users/account avg = 1,000 accounts × 10 users = 10,000 users
- Adoption: 20% of users = 2,000 users
- Revenue: 2,000 × $10 = $20K/month = $240K/year
- Margin: $240K × 80% = $192K gross profit/year
- ROI: $192K / $100K = 1.92:1 in year 1
- Payback: $100K / $20K = 5 months

**Agent recommends:**

"**Build now** — Positive ROI with fast payback

**Revenue Impact:** $240K/year (conservative 20% adoption)
**ROI:** 1.92:1 in year 1, 3.8:1 in year 2
**Payback:** 5 months

**Why this works:**
- Fast payback (5 months) means low risk
- 80% gross margin on add-on revenue
- 20% adoption is conservative (test willingness-to-pay)

**Next steps:**
1. Survey customers: who would pay $10/user for time tracking?
2. Build MVP with core time tracking only
3. Beta with 50 customers before broad launch
4. Track adoption rate vs. 20% target"

---

### Example 2: Retention Feature (Data Export)

**User:** "We're losing customers because they can't export their data easily. Should we build a comprehensive export feature?"

**Agent:** [Gathers context]

**User provides:**
- Current: $2M MRR, 500 customers, $4K ARPA, 5% monthly churn
- Feature: Full data export (CSV, API, scheduled exports)
- Dev cost: $150K (3 engineers × 2 months)
- Churn context: 30% of churned customers cited data export as a reason

**Agent calculates:**
- Current annual churn: ~46% (5% monthly compounded)
- Customers churned annually: 500 × 46% = 230 customers
- Customers churned due to export issue: 230 × 30% = 69 customers
- MRR lost: 69 × $4K = $276K MRR lost/year = $3.3M ARR

**If feature reduces this by 50%:**
- Churn prevented: 35 customers/year
- MRR saved: $140K/year
- LTV impact (assuming 24-month lifetime): $140K × 24 = $3.36M

**Agent calculates ROI:**
- Investment: $150K
- LTV saved: $3.36M (conservative 50% reduction)
- ROI: $3.36M / $150K = 22.4:1 🚀

**Agent recommends:**

"**Build immediately** — Exceptional ROI on retention

**Impact:**
- Prevents ~35 customer churns/year
- Saves $140K MRR annually
- LTV impact: $3.36M over customer lifetime
- ROI: 22:1 (exceptional)

**Why this is a no-brainer:**
- 30% of churn cites this gap (validated problem)
- Even if you only prevent 25% (not 50%), ROI is still 11:1
- Retention improvements compound (reduces future churn too)

**Next steps:**
1. Interview churned customers to validate export was primary reason
2. Build core export (CSV, API) first
3. Measure churn rate change after launch (target: 5% → 4.5%)
4. Add scheduled exports if adoption is high"

---

### Example 3: Poor ROI Feature (Dark Mode)

**User:** "Users are requesting dark mode. Should we prioritize it?"

**Agent:** [Gathers context]

**User provides:**
- Current: $500K MRR, 2,000 customers, $250 ARPA, 3% monthly churn, 75% gross margin
- Feature: Full dark mode across product
- Dev cost: $80K (2 designers + 2 engineers × 1 month)
- Revenue connection: Indirect—may improve retention slightly

**Agent asks:** "What evidence do you have that dark mode will reduce churn?"

**User:** "Feature requests from 50 users. No data on churn impact."

**Agent calculates:**
- 50 feature requests out of 2,000 customers = 2.5% of base
- No validated churn impact
- Dev cost: $80K
- Optimistic scenario: Prevents 5 churns/year (2.5% of base)
- MRR saved: 5 × $250 = $1,250/month = $15K/year
- LTV impact (24-month lifetime): $15K × 24 = $360K

**ROI: $360K / $80K = 4.5:1** (looks okay, but based on weak assumptions)

**Agent recommends:**

"**Build later** — Weak evidence for ROI

**Current case:**
- Revenue impact: $15K/year (optimistic)
- Development cost: $80K
- ROI: 4.5:1 (assumes dark mode prevents churn)

**Problem:**
- Only 50 users requested this (2.5% of base)
- No evidence dark mode reduces churn
- Churn interviews don't mention this as a top reason

**Alternative approach:**
1. **Survey churned customers** — Is dark mode in top 5 churn reasons?
2. **Test demand** — Ask trial users: "Would dark mode affect your decision to convert?"
3. **Reduce scope** — Build basic dark mode (20% cost) as experiment

**Better features to consider:**
- If retention is priority: Interview churned customers, find top 3 churn drivers
- If revenue is priority: Focus on expansion features (upsell, add-ons)

**Decision criteria to build:**
- If churn interviews show dark mode is top 3 reason → build
- If conversion research shows 10%+ impact → build
- Otherwise → deprioritize"

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Confusing Revenue with Profit | "$1M revenue!" ignoring $800K COGS | Always calculate contribution margin: `Revenue x Margin %` |
| Ignoring Payback Period | "ROI 5:1!" but 36-month payback, 24-month customer lifetime | Payback must be shorter than average customer lifetime |
| Overestimating Adoption | "100% will use this add-on!" | Use conservative estimates (10-20%). Validate with WTP research |
| Building Without Validation | "We think this reduces churn" — no interviews | Interview churned customers first. Validate top 3 churn reasons |
| Ignoring Opportunity Cost | "2:1 ROI, let's build!" while 10:1 options exist | Compare ROI across features. Build highest-ROI first |
| Strategic Value as Excuse | "ROI is bad but it's strategic!" | Define "strategic" concretely: moat, platform enabler, compliance |
| Margin Dilution Blindness | "$500K revenue!" but $400K COGS | If margin <50%, reconsider or charge a premium |
| Celebrating Vanity Metrics | "Increases engagement!" but not revenue/retention | Tie features to revenue or retention outcomes |
| Forgetting Time Value of Money | "Pays back in 5 years" | Use NPV for payback >24 months |
| Building for Loud Minorities | "50 requested this!" out of 10,000 | Weight by revenue impact/segment, not request count |

---

## References

### Related Skills
- `saas-revenue-growth-metrics` — Revenue, ARPU, churn, NRR metrics used in impact calculations
- `saas-economics-efficiency-metrics` — ROI, payback, contribution margin calculations
- `finance-metrics-quickref` — Quick lookup for formulas and benchmarks
- `acquisition-channel-advisor` — Similar ROI framework for channel decisions
- `finance-based-pricing-advisor` — Pricing impact analysis for monetization features

### External Frameworks
- **RICE Prioritization** — Combines Reach, Impact, Confidence, Effort (this skill adds financial lens)
- **Value vs. Effort Matrix** — This skill quantifies "value" financially
- **Jobs-to-be-Done** — Understand customer problems before evaluating financial impact
- **Opportunity Solution Tree (Teresa Torres)** — Map opportunities before calculating ROI

### Provenance
- Adapted from `research/finance/Finance_For_PMs.Putting_It_Together_Synthesis.md` (Decision Framework #1)
- Quiz scenarios from `research/finance/Finance for Product Managers.md`
