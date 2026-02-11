---
name: finance-based-pricing-advisor
description: Evaluate pricing changes using financial impact analysis - ARPU/ARPA, conversion, churn risk, NRR, and payback. Recommends go/no-go on pricing decisions.
type: interactive
---


## Purpose

Evaluate the **financial impact** of pricing changes (price increases, new tiers, add-ons, discounts) using ARPU/ARPA analysis, conversion impact, churn risk, NRR effects, and CAC payback implications. Use this to make data-driven go/no-go decisions on proposed pricing changes with supporting math and risk assessment.

**What this is:** Financial impact evaluation for pricing decisions you're already considering.

**What this is NOT:** Comprehensive pricing strategy design, value-based pricing frameworks, willingness-to-pay research, competitive positioning, psychological pricing, packaging architecture, or monetization model selection. For those topics, see the future `pricing-strategy-suite` skills.

This skill assumes you have a specific pricing change in mind and need to evaluate its financial viability.

## Key Concepts

### The Pricing Impact Framework

A systematic approach to evaluate pricing changes financially:

1. **Revenue Impact** — How does this change ARPU/ARPA?
   - Direct revenue lift from price increase
   - Revenue loss from reduced conversion or increased churn
   - Net revenue impact

2. **Conversion Impact** — How does this affect trial-to-paid or sales conversion?
   - Higher prices may reduce conversion rate
   - Better packaging may improve conversion
   - Test assumptions

3. **Churn Risk** — Will existing customers leave due to price change?
   - Grandfathering strategy (protect existing customers)
   - Churn risk by segment (SMB vs. enterprise)
   - Churn elasticity (how sensitive are customers to price?)

4. **Expansion Impact** — Does this create or block expansion opportunities?
   - New premium tier = upsell path
   - Usage-based pricing = expansion as customers grow
   - Add-ons = cross-sell opportunities

5. **CAC Payback Impact** — Does pricing change affect unit economics?
   - Higher ARPU = faster payback
   - Lower conversion = higher effective CAC
   - Net effect on LTV:CAC ratio

### Pricing Change Types

**Direct monetization changes:**
- Price increase (raise prices for all customers or new customers only)
- New premium tier (create upsell path)
- Paid add-on (monetize previously free feature)
- Usage-based pricing (charge for consumption)

**Discount strategies:**
- Annual prepay discount (improve cash flow)
- Volume discounts (larger deals)
- Promotional pricing (temporary price reduction)

**Packaging changes:**
- Feature bundling (combine features into tiers)
- Unbundling (separate features into add-ons)
- Pricing metric change (seats → usage, or vice versa)

### Anti-Patterns (What This Is NOT)

- **Not value-based pricing:** This evaluates a proposed change, not "what should we charge?"
- **Not WTP research:** This analyzes impact, not "what will customers pay?"
- **Not competitive positioning:** This is financial analysis, not market positioning
- **Not packaging architecture:** This evaluates one change, not redesigning all tiers

### When to Use This Framework

**Use this when:**
- You have a specific pricing change to evaluate (e.g., "Should we raise prices 20%?")
- You need to quantify revenue, churn, and conversion trade-offs
- You're deciding between pricing change options (test A vs. B)
- You need to present pricing change impact to leadership or board

**Don't use this when:**
- You're designing pricing strategy from scratch (use value-based pricing frameworks)
- You haven't validated willingness-to-pay (do customer research first)
- You don't have baseline metrics (ARPU, churn, conversion rates)
- Change is too small to matter (<5% price change, <10% of customers affected)

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

"Let's evaluate the financial impact of your pricing change. Please provide:

**Current pricing:**
- Current ARPU or ARPA
- Current pricing tiers (if applicable)
- Current monthly churn rate
- Current trial-to-paid conversion rate (if relevant)

**Proposed pricing change:**
- What change are you considering? (price increase, new tier, add-on, etc.)
- New pricing (if known)
- Affected customer segment (all, new only, specific tier)

**Business context:**
- Total customers (or MRR/ARR)
- CAC (to assess payback impact)
- NRR (to assess expansion context)

You can provide estimates if you don't have exact numbers."

---

### Step 1: Identify Pricing Change Type

**Agent asks:**

"What type of pricing change are you considering?

1. **Price increase** — Raise prices for new customers, existing customers, or both
2. **New premium tier** — Add higher-priced tier with additional features
3. **Paid add-on** — Monetize a new or existing feature separately
4. **Usage-based pricing** — Charge for consumption (seats, API calls, storage, etc.)
5. **Discount strategy** — Annual prepay discount, volume pricing, or promotional pricing
6. **Packaging change** — Rebundle features, change pricing metric, or tier restructure

Choose a number, or describe your specific pricing change."

**Based on selection, agent adapts questions:**

---

#### If Option 1 (Price Increase):

**Agent asks:**

"**Price increase details:**

- Current price: $___
- New price: $___
- Increase: ___%

**Who is affected?**
1. New customers only (grandfather existing)
2. All customers (existing + new)
3. Specific segment (e.g., SMB only, new plan only)

**When would this take effect?**
- Immediately
- Next billing cycle
- Gradual rollout (test first)"

---

#### If Option 2 (New Premium Tier):

**Agent asks:**

"**Premium tier details:**

- Current top tier price: $___
- New premium tier price: $___
- Key features in premium tier: [list]

**Expected adoption:**
- What % of current customers might upgrade? ___%
- What % of new customers might choose premium? ___%

**Cannibalization risk:**
- Will premium tier cannibalize current top tier?"

---

#### If Option 3 (Paid Add-On):

**Agent asks:**

"**Add-on details:**

- Add-on name: ___
- Price: $___ /month or /user
- Currently free or new feature?

**Expected adoption:**
- What % of customers would pay for this? ___%
- Is this feature currently used (if free)?
- Will making it paid hurt retention?"

---

#### If Option 4 (Usage-Based Pricing):

**Agent asks:**

"**Usage pricing details:**

- Usage metric: (seats, API calls, storage, transactions, etc.)
- Pricing: $___ per [unit]
- Free tier or minimum? (e.g., first 1,000 API calls free)

**Expected impact:**
- Average customer usage: ___ units/month
- Expected ARPU change: $current → $new

**Expansion potential:**
- As customers grow usage, will ARPU increase?"

---

#### If Option 5 (Discount Strategy):

**Agent asks:**

"**Discount details:**

- Discount type: (annual prepay, volume, promotional)
- Discount amount: ___% off
- Duration: (ongoing, limited time)

**Trade-off:**
- Lower price vs. improved cash flow (annual prepay)
- Lower price vs. larger deal size (volume)
- Lower price vs. urgency (promotional)"

---

#### If Option 6 (Packaging Change):

**Agent asks:**

"**Packaging change details:**

- What are you changing? (bundling, unbundling, pricing metric)
- Current packaging: [describe]
- New packaging: [describe]

**Expected impact:**
- ARPU change: $current → $new
- Conversion change: ___% → ___%
- Churn risk: (low, medium, high)"

---

### Step 2: Assess Expected Impact

**Agent asks:**

"Now let's quantify the impact. Based on your pricing change, estimate:

**Revenue impact:**
- Current ARPU: $___
- Expected new ARPU: $___
- ARPU lift: ___%

**Conversion impact:**
- Current conversion rate: ___%
- Expected new conversion rate: ___%
- Conversion change: [increase / decrease / no change]

**Churn risk:**
- Current monthly churn: ___%
- Expected churn after change: ___%
- Churn risk: [low / medium / high]

**Expansion impact:**
- Does this create expansion opportunities? (new tier to upgrade to, usage growth)
- Expected NRR change: ___% → ___%

You can provide estimates. We'll model scenarios (conservative, base, optimistic)."

---

### Step 3: Evaluate Current State

**Agent asks:**

"To assess whether this pricing change makes sense, I need your current baseline:

**Current metrics:**
- MRR or ARR: $___
- Number of customers: ___
- ARPU/ARPA: $___
- Monthly churn rate: ___%
- NRR: ___%
- CAC: $___
- LTV: $___

**Growth context:**
- Current growth rate: ___% MoM or YoY
- Target growth rate: ___%

**Competitive context:**
- Are you priced below, at, or above market?
- Competitive pressure: (low, medium, high)"

---

### Step 4: Deliver Recommendations

**Agent synthesizes:**
- Revenue impact (ARPU lift × customer base)
- Conversion impact (new customers affected)
- Churn impact (existing customers affected)
- Net revenue impact
- CAC payback impact
- Risk assessment

**Agent offers 3-4 recommendations:**

---

#### Recommendation Pattern 1: Implement Broadly

**When:**
- Net revenue impact clearly positive (>10% ARPU lift, <5% churn risk)
- Minimal conversion impact
- Strong value justification

**Recommendation:**

"**Implement this pricing change** — Strong financial case

**Revenue Impact:**
- Current MRR: $___
- ARPU lift: ___% ($current → $new)
- Expected MRR increase: +$___/month (+___%)

**Churn Risk: Low**
- Expected churn increase: ___% → ___% (+___% points)
- Churn-driven MRR loss: -$___/month
- **Net MRR impact: +$___/month** ✅

**Conversion Impact:**
- Current conversion: ___%
- Expected conversion: ___% (___% change)
- Impact on new customer acquisition: [minimal / manageable]

**CAC Payback Impact:**
- Current payback: ___ months
- New payback: ___ months (faster due to higher ARPU)

**Why this works:**
[Specific reasoning based on numbers]

**How to implement:**
1. **Grandfather existing customers** (if raising prices)
   - Protect current base from churn
   - New pricing for new customers only
2. **Communicate value**
   - Emphasize features, outcomes, ROI
   - Justify price with value delivered
3. **Monitor metrics (first 30-60 days)**
   - Conversion rate (should stay within ___%)
   - Churn rate (should stay <___%)
   - Customer feedback

**Expected timeline:**
- Month 1: +$___ MRR from new customers
- Month 3: +$___ MRR (cumulative)
- Month 6: +$___ MRR
- Year 1: +$___ ARR

**Success criteria:**
- Conversion rate stays >___%
- Churn rate stays <___%
- NRR improves to >___%"

---

#### Recommendation Pattern 2: Test First (A/B Test)

**When:**
- Uncertain impact (wide range between conservative and optimistic)
- Moderate churn or conversion risk
- Large customer base (can test with subset)

**Recommendation:**

"**Test with a segment before broad rollout** — Impact is uncertain

**Why test:**
- ARPU lift estimate: ___% (wide confidence interval)
- Churn risk: Medium (___% → ___%)
- Conversion impact: Uncertain (___% → ___% estimated)

**Test design:**

**Cohort A (Control):**
- Current pricing: $___
- Size: ___% of new customers (or ___ customers)

**Cohort B (Test):**
- New pricing: $___
- Size: ___% of new customers (or ___ customers)

**Duration:** 60-90 days (need statistical significance)

**Metrics to track:**
- Conversion rate (A vs. B)
- ARPU (A vs. B)
- 30-day retention (A vs. B)
- 90-day churn (A vs. B)
- NRR (A vs. B)

**Decision criteria:**

**Roll out broadly if:**
- Conversion rate (B) >___% of control (A)
- Churn rate (B) <___% higher than control
- Net revenue (B) >___% higher than control

**Don't roll out if:**
- Conversion drops >___%
- Churn increases >___%
- Net revenue impact negative

**Expected timeline:**
- Week 1-2: Launch test
- Week 8-12: Enough data for statistical significance
- Month 3: Decision to roll out or kill

**Risk:** Medium. Test mitigates risk before broad rollout."

---

#### Recommendation Pattern 3: Modify Approach

**When:**
- Original proposal has significant risk
- Better alternative exists
- Need to adjust pricing change to improve outcomes

**Recommendation:**

"**Modify your approach** — Original proposal has risks

**Original Proposal:**
- [Price increase / New tier / Add-on / etc.]
- Expected ARPU lift: ___%
- Churn risk: High (___% → ___%)
- Net revenue impact: Uncertain or negative

**Problem:**
[Specific issue: e.g., "20% price increase will likely cause 10% churn, wiping out revenue gains"]

**Alternative Approach:**

**Option 1: Smaller price increase**
- Instead of ___% increase, try ___%
- Lower churn risk (___% vs. ___%)
- Still positive net revenue: +$___/month

**Option 2: Grandfather existing, raise for new only**
- Protect current base (zero churn risk)
- Higher prices for new customers only
- Gradual ARPU improvement over time

**Option 3: Value-based pricing (charge more for high-value segments)**
- Keep SMB pricing flat
- Raise enterprise pricing ___%
- Lower churn risk (enterprise is stickier)

**Recommended:**
[Specific option with reasoning]

**Why this is better:**
- Lower churn risk
- Comparable revenue upside
- Easier to communicate

**How to implement:**
[Specific steps for alternative approach]"

---

#### Recommendation Pattern 4: Don't Change Pricing

**When:**
- Net revenue impact negative or marginal
- High churn risk without offsetting gains
- Competitive or strategic reasons to hold pricing

**Recommendation:**

"**Don't change pricing** — Risks outweigh benefits

**Why:**
- Expected revenue lift: +$___/month (___%)
- Expected churn impact: -$___/month (___%)
- **Net revenue impact: -$___/month** 🚨 or marginal

**Problem:**
[Specific issue: e.g., "Churn-driven revenue loss exceeds price increase gains"]

**What would need to change:**

**For price increase to work:**
- Churn rate must stay below ___% (currently ___%)
- OR conversion rate must stay above ___% (currently ___%)
- OR you need to reduce CAC to offset lower conversion

**Alternative strategies:**

**Instead of raising prices:**
1. **Improve retention** — Reduce churn from ___% to ___% (same revenue impact as price increase, lower risk)
2. **Expand within base** — Increase NRR from ___% to ___% via upsells
3. **Reduce CAC** — More efficient acquisition (better than pricing)

**When to revisit pricing:**
- After improving retention (churn <___%)
- After validating willingness-to-pay (WTP research)
- After competitive landscape changes

**Decision:** Hold pricing for now, focus on [retention / expansion / acquisition efficiency]."

---

### Step 5: Sensitivity Analysis (Optional)

**Agent offers:**

"Want to see what-if scenarios?

1. **Optimistic case** — Higher ARPU lift, lower churn
2. **Pessimistic case** — Lower ARPU lift, higher churn
3. **Breakeven analysis** — What churn rate makes this neutral?

Or ask any follow-up questions."

**Agent can provide:**
- Scenario modeling (optimistic/pessimistic/breakeven)
- Sensitivity tables (if churn is X%, revenue impact is Y)
- Comparison to alternative pricing strategies

---

## Examples

See `examples/` folder for sample conversation flows. Mini examples below:

### Example 1: Price Increase (Good Case)

**Scenario:** 20% price increase for new customers only

**Current state:**
- ARPU: $100/month
- Customers: 1,000
- MRR: $100K
- Churn: 3%/month
- New customers/month: 50

**Proposed change:**
- New customer pricing: $120/month (+20%)
- Existing customers: Grandfathered at $100

**Impact:**
- New customer ARPU: $120 (+20%)
- Churn risk: Low (existing protected)
- Conversion impact: Minimal (<5% drop estimated)

**Recommendation:** Implement. Net revenue impact +$12K/year with low risk.

---

### Example 2: Price Increase (Risky)

**Scenario:** 30% price increase for all customers

**Current state:**
- ARPU: $50/month
- Customers: 5,000
- MRR: $250K
- Churn: 5%/month (already high)

**Proposed change:**
- All customers: $65/month (+30%)

**Impact:**
- ARPU lift: +30% = +$75K MRR
- Churn risk: High (5% → 8% estimated)
- Churn-driven loss: 3% × 5,000 × $65 = -$9.75K MRR/month

**Net impact:** +$75K - $9.75K = +$65K MRR (but accelerating churn problem)

**Recommendation:** Don't change. Fix retention first (reduce 5% churn), then raise prices.

---

### Example 3: New Premium Tier

**Scenario:** Add $500/month premium tier

**Current state:**
- Top tier: $200/month (500 customers)
- ARPA: $200

**Proposed change:**
- New tier: $500/month with advanced features
- Expected adoption: 10% of current top tier (50 customers)

**Impact:**
- Upsell revenue: 50 × ($500 - $200) = +$15K MRR
- Cannibalization risk: Low (features justify premium)
- NRR impact: Increases from 105% to 110%

**Recommendation:** Implement. Creates expansion path, minimal cannibalization risk.

---

## Common Pitfalls

### Pitfall 1: Ignoring Churn Impact
**Symptom:** "We'll raise prices 30% and make $X more!" (no churn modeling)

**Consequence:** Churn wipes out revenue gains. Net impact negative.

**Fix:** Model churn scenarios (conservative, base, optimistic). Factor churn-driven revenue loss into net impact.

---

### Pitfall 2: Not Grandfathering Existing Customers
**Symptom:** "We're raising prices for everyone effective immediately"

**Consequence:** Massive churn spike from existing customers who feel betrayed.

**Fix:** Grandfather existing customers. Raise prices for new customers only.

---

### Pitfall 3: Testing Without Statistical Power
**Symptom:** "We tested on 10 customers and it worked!"

**Consequence:** 10 customers isn't statistically significant. Results are noise.

**Fix:** Test with large enough sample (100+ customers per cohort) for 60-90 days.

---

### Pitfall 4: Pricing Changes Without Value Justification
**Symptom:** "We're raising prices because we need more revenue"

**Consequence:** Customers see price increase without corresponding value increase. Churn.

**Fix:** Tie price increases to value improvements (new features, better support, outcomes delivered).

---

### Pitfall 5: Ignoring CAC Payback Impact
**Symptom:** "Higher ARPU is always better!"

**Consequence:** If conversion drops 30%, effective CAC increases dramatically. Payback period explodes.

**Fix:** Calculate CAC payback impact. Higher ARPU with lower conversion might make payback worse, not better.

---

### Pitfall 6: Annual Discounts That Hurt Margin
**Symptom:** "30% discount for annual prepay!" (improves cash but destroys LTV)

**Consequence:** Customers lock in low prices for a year. Revenue per customer decreases.

**Fix:** Limit annual discounts to 10-15%. Balance cash flow improvement with LTV protection.

---

### Pitfall 7: Copycat Pricing (Competitor-Based)
**Symptom:** "Competitor raised prices, so should we"

**Consequence:** Your customers, value prop, and cost structure are different. What works for them may not work for you.

**Fix:** Use competitors as data points, not decisions. Make pricing decisions based on your unit economics.

---

### Pitfall 8: Premature Optimization
**Symptom:** "Let's A/B test 47 different price points!"

**Consequence:** Analysis paralysis. Spending months on 5% pricing optimizations while missing 50% growth opportunities elsewhere.

**Fix:** Big pricing changes (tiers, packaging, add-ons) matter more than micro-optimizations. Start there.

---

### Pitfall 9: Forgetting Expansion Revenue
**Symptom:** "We're maximizing ARPU at acquisition"

**Consequence:** High upfront pricing prevents landing customers. Miss expansion opportunities.

**Fix:** Consider "land and expand" strategy. Lower entry price, higher expansion revenue via upsells.

---

### Pitfall 10: No Pricing Change Communication Plan
**Symptom:** "We're raising prices next month" (no customer communication)

**Consequence:** Surprised customers churn. Poor reviews. Reputation damage.

**Fix:** Communicate pricing changes 30-60 days in advance. Emphasize value, not just price.

---

## References

### Related Skills
- `saas-revenue-growth-metrics` — ARPU, ARPA, churn, NRR metrics used in pricing analysis
- `saas-economics-efficiency-metrics` — CAC payback impact of pricing changes
- `finance-metrics-quickref` — Quick lookup for pricing-related formulas
- `feature-investment-advisor` — Evaluates whether to build features that enable pricing changes
- `business-health-diagnostic` — Broader business context for pricing decisions

### External Frameworks (Comprehensive Pricing Strategy)
These are OUTSIDE the scope of this skill but relevant for broader pricing work:

- **Value-Based Pricing** — Price based on value delivered, not cost
- **Van Westendorp Price Sensitivity** — WTP research methodology
- **Conjoint Analysis** — Feature-to-price trade-off research
- **Good-Better-Best Packaging** — Tier architecture design
- **Price Anchoring & Decoy Pricing** — Psychological pricing tactics
- **Patrick Campbell (ProfitWell):** Pricing research and benchmarks

### Future Skills (Comprehensive Pricing)
For topics NOT covered here, see future `pricing-strategy-suite`:
- `value-based-pricing-framework` — How to price based on value
- `willingness-to-pay-research` — WTP research methods
- `packaging-architecture-advisor` — Tier and bundle design
- `pricing-psychology-guide` — Anchoring, decoys, framing
- `monetization-model-advisor` — Seat-based vs. usage vs. outcome pricing

### Provenance
- Adapted from `research/finance/Finance_For_PMs.Putting_It_Together_Synthesis.md` (Decision Framework #3)
- Pricing scenarios from `research/finance/Finance for Product Managers.md`
