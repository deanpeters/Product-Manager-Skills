---
name: acquisition-channel-advisor
description: Evaluate acquisition channels using unit economics, customer quality, and scalability. Recommends scale/test/kill decisions.
type: interactive
---


## Purpose

Guide product managers through evaluating whether to scale, test, or kill an acquisition channel based on unit economics (CAC, LTV, payback), customer quality (retention, NRR), and scalability (magic number, volume potential). Use this to make data-driven go-to-market decisions and optimize channel mix for sustainable growth.

This is not a channel strategy framework—it's a financial lens for channel evaluation that helps you avoid scaling unprofitable channels or killing channels with fixable problems. Use when deciding how to allocate marketing budget across channels.

## Key Concepts

### The Channel Evaluation Framework

A systematic approach to evaluate acquisition channels:

1. **Unit Economics** — What does it cost to acquire, and what's the return?
   - CAC (Customer Acquisition Cost)
   - LTV (Lifetime Value)
   - LTV:CAC ratio
   - Payback period

2. **Customer Quality** — Do customers from this channel stick around and expand?
   - Cohort retention rate (by channel)
   - Churn rate (by channel)
   - NRR (Net Revenue Retention by channel)
   - Expansion rate

3. **Scalability** — Can this channel sustain growth at the volume you need?
   - Magic Number (S&M efficiency)
   - Addressable volume (TAM of channel)
   - Saturation risk (diminishing returns)
   - CAC trend (increasing, stable, decreasing)

4. **Strategic Fit** — Does this channel align with your go-to-market strategy?
   - Customer segment match (SMB vs. enterprise)
   - Sales motion compatibility (PLG vs. sales-led)
   - Brand positioning alignment

### Decision Matrix

| LTV:CAC | Payback | Customer Quality | Scalability | Decision |
|---------|---------|------------------|-------------|----------|
| >3:1 | <12mo | Good retention | High volume | **Scale aggressively** |
| 2-3:1 | 12-18mo | Average retention | Medium volume | **Test & optimize** |
| <2:1 | >18mo | Poor retention | Low volume | **Kill or fix** |

### Anti-Patterns (What This Is NOT)

- **Not vanity metrics:** "We got 10,000 signups!" means nothing if they churn in 30 days
- **Not CAC-only thinking:** Low CAC with terrible retention is worse than high CAC with great retention
- **Not ignoring payback:** 5:1 LTV:CAC with 36-month payback is a cash trap
- **Not scaling broken channels:** Pouring money into inefficient channels accelerates failure

### When to Use This Framework

**Use this when:**
- Evaluating whether to scale a new channel (content, paid, events, etc.)
- Deciding how to allocate marketing budget across channels
- Assessing whether to kill an underperforming channel
- Comparing channels to optimize ROI
- Planning annual marketing budget allocation

**Don't use this when:**
- Channel is brand-new (<3 months, <100 customers) — not enough data
- You're testing channel fit (this is for evaluation, not experimentation)
- Strategic channels (e.g., enterprises require field sales regardless of CAC)
- You don't have channel-level data (need to track CAC, retention by source)

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

"Let's evaluate this acquisition channel. Please provide:

**Channel details:**
- Channel name (e.g., Google Ads, content marketing, outbound sales, partnerships)
- How long have you been using this channel? (months)
- Current monthly spend on this channel

**Customer acquisition:**
- Customers acquired per month (from this channel)
- CAC for this channel (if known, otherwise we'll calculate)

**Business context:**
- Blended CAC (across all channels)
- Blended LTV
- Current MRR/ARR
- Target growth rate (% MoM or YoY)

You can provide estimates if you don't have exact numbers."

---

### Step 1: Evaluate Unit Economics

**Agent calculates (if not provided):**
```
CAC = Monthly Spend / Customers Acquired per Month
```

**Agent asks:**

"Now let's compare this channel's unit economics to your blended metrics.

**Channel Unit Economics:**
- Channel CAC: $___
- Blended CAC (all channels): $___
- Channel LTV: $___ (if known; otherwise we'll use blended LTV as proxy)
- Blended LTV: $___

**Questions:**

1. **Do customers from this channel have similar LTV to other channels?**
   - Similar (use blended LTV)
   - Higher (they upgrade more, stick around longer)
   - Lower (they churn faster or are smaller deals)
   - Unknown (need to analyze cohort data)

2. **What's the payback period for this channel?**
   - We can calculate: CAC / (Monthly ARPU × Gross Margin %)
   - Or you can provide it"

**Based on answers, agent calculates:**
- LTV:CAC ratio for channel
- Payback period
- Comparison to blended metrics

**Agent flags:**
- ✅ If LTV:CAC >3:1 and payback <12 months: "Strong unit economics"
- ⚠️ If LTV:CAC 2-3:1 or payback 12-18 months: "Marginal unit economics"
- 🚨 If LTV:CAC <2:1 or payback >18 months: "Poor unit economics"

---

### Step 2: Assess Customer Quality

**Agent asks:**

"How do customers from this channel perform compared to other channels?

**Retention & Expansion:**

1. **What's the churn rate for customers from this channel?**
   - Lower than blended (they stick around longer)
   - Same as blended (no difference)
   - Higher than blended (they churn faster)
   - Unknown (need cohort analysis)

2. **What's the NRR for customers from this channel?**
   - Higher than blended (they expand more)
   - Same as blended (no difference)
   - Lower than blended (they contract or churn more)
   - Unknown (need cohort analysis)

3. **What's the customer profile from this channel?**
   - Ideal customer profile (ICP) — perfect fit
   - Close to ICP — mostly good fit
   - Off ICP — many poor-fit customers
   - Unknown"

**Based on answers, agent evaluates:**
- ✅ **High quality:** Lower churn, higher NRR, ICP match
- ⚠️ **Medium quality:** Similar to blended, mostly good fit
- 🚨 **Low quality:** Higher churn, lower NRR, off ICP

**Agent flags:**
- If high quality: "Premium channel—customers are better than average"
- If low quality: "Quality problem—customers aren't sticking or expanding"

---

### Step 3: Evaluate Scalability

**Agent asks:**

"Can this channel scale to meet your growth targets?

**Efficiency & Volume:**

1. **What's the S&M efficiency for this channel (Magic Number)?**
   - Calculate: (New MRR from channel × 4) / Channel S&M Spend
   - Or provide if known

2. **What's the addressable volume for this channel?**
   - Large (can scale 10x+ from current spend)
   - Medium (can scale 2-5x)
   - Small (near saturation, maybe 1.5x)
   - Unknown

3. **What's the CAC trend for this channel?**
   - Decreasing (getting more efficient over time)
   - Stable (consistent CAC)
   - Increasing (diminishing returns, saturation)
   - Unknown (too early to tell)

4. **How much growth do you need from acquisition?**
   - We'll calculate: Target growth - expansion/retention growth = acquisition gap"

**Based on answers, agent evaluates:**
- ✅ **Highly scalable:** Magic number >0.75, large volume, stable/decreasing CAC
- ⚠️ **Moderately scalable:** Magic number 0.5-0.75, medium volume, stable CAC
- 🚨 **Not scalable:** Magic number <0.5, small volume, increasing CAC

---

### Step 4: Deliver Recommendations

**Agent synthesizes:**
- Unit economics (LTV:CAC, payback)
- Customer quality (retention, NRR, ICP fit)
- Scalability (magic number, volume, CAC trend)
- Strategic fit

**Agent offers 3-4 recommendations:**

---

#### Recommendation Pattern 1: Scale Aggressively

**When:**
- LTV:CAC >3:1 AND
- Payback <12 months AND
- Customer quality good or better AND
- Magic Number >0.75 AND
- Addressable volume large

**Recommendation:**

"**Scale this channel aggressively** — Excellent economics + scalability

**Unit Economics:**
- CAC: $___
- LTV: $___
- LTV:CAC: ___:1 ✅ (>3:1 threshold)
- Payback: ___ months ✅ (<12 months)

**Customer Quality:**
- Retention: [Better than / Same as / Worse than] blended
- NRR: [Higher / Same / Lower]
- ICP Fit: [High / Medium / Low]

**Scalability:**
- Magic Number: ___ ✅ (>0.75 = efficient)
- Addressable Volume: Large
- CAC Trend: [Stable / Decreasing]

**Why this is a winner:**
- Every $1 spent returns $__ in LTV
- Payback in under a year = fast cash recovery
- [Customer quality insight]
- Can scale 5-10x from current spend

**How to scale:**
1. **Increase budget by 50-100% next month**
   - Current: $___ /month → Target: $___ /month
2. **Monitor key metrics weekly:**
   - CAC (should stay <$___)
   - Magic Number (should stay >0.75)
   - Customer quality (retention, NRR)
3. **Scale until:**
   - CAC increases >20% (saturation signal)
   - Magic Number drops <0.75 (efficiency declining)
   - Volume caps out

**Expected impact:**
- Current: ___ customers/month
- Target (2x spend): ___ customers/month
- MRR impact: +$___/month
- Payback: Still ~___ months even at 2x scale

**Risk:** Low. Strong unit economics support aggressive scaling."

---

#### Recommendation Pattern 2: Test & Optimize

**When:**
- LTV:CAC 2-3:1 OR
- Payback 12-18 months OR
- Customer quality average OR
- Magic Number 0.5-0.75

**Recommendation:**

"**Test & optimize before scaling** — Marginal economics, fixable

**Current State:**
- CAC: $___
- LTV: $___
- LTV:CAC: ___:1 ⚠️ (2-3:1 = marginal)
- Payback: ___ months ⚠️ (12-18 months)
- Magic Number: ___ ⚠️ (0.5-0.75 = acceptable, not great)

**Customer Quality:**
- Retention: [Same as blended / Slightly worse]
- NRR: [Same / Lower]
- Issue: [Specific problem, e.g., "Higher churn in first 90 days"]

**Diagnosis:**
[One of these:]
- **High CAC:** Spending too much to acquire
- **Low LTV:** Customers churn too fast or don't expand
- **Poor targeting:** Attracting off-ICP customers
- **Inefficient conversion:** High cost-per-click but low conversion rate

**How to optimize:**

**If CAC is the problem:**
1. Improve conversion rate (optimize landing pages, offer, onboarding)
2. Reduce cost-per-click (better targeting, ad creative)
3. Shorten sales cycle (faster qualification, better demos)

**If LTV is the problem:**
1. Improve onboarding for customers from this channel
2. Target higher-value segments within channel
3. Add expansion plays (upsell, cross-sell)

**If targeting is the problem:**
1. Narrow audience (exclude poor-fit segments)
2. Improve messaging (attract better-fit customers)
3. Add qualification step (reduce poor-fit signups)

**Timeline:**
- Spend 4-8 weeks optimizing
- Track CAC and LTV weekly
- Target: LTV:CAC >3:1, payback <12 months
- If you hit targets: scale
- If you can't fix it: consider killing

**Don't scale yet:** Current economics are break-even at best. Fix first, then scale."

---

#### Recommendation Pattern 3: Kill or Pause

**When:**
- LTV:CAC <1.5:1 AND
- No clear path to improvement

**Recommendation:**

"**Kill this channel (or pause)** — Economics don't support investment

**Why:**
- CAC: $___
- LTV: $___
- LTV:CAC: ___:1 🚨 (<2:1 = unsustainable)
- Payback: ___ months 🚨 (>18 months = cash trap)

**Problem:**
- You're spending $___ to acquire a customer worth $___
- [Losing money / Barely breaking even / Taking too long to recover cost]

**Customer Quality:**
- Retention: [Worse than blended]
- NRR: [Lower]
- ICP Fit: [Poor]

**What's broken:**
[Specific diagnosis:]
- CAC too high (spending $___ vs. blended $___)
- LTV too low (customers churn at ___% vs. blended ___%)
- Both (bad unit economics from both sides)

**Should you fix or kill?**

**Fix if:**
- You have a hypothesis to improve CAC by 50%+ (better targeting, conversion)
- You have a hypothesis to improve LTV by 50%+ (better onboarding, ICP focus)
- This is a strategically important channel (e.g., enterprise requires field sales)

**Kill if:**
- No clear path to 3:1 LTV:CAC
- Better channels available (reallocate budget there)
- Small addressable volume (not worth fixing)

**Recommendation: Kill and reallocate budget**

**Reallocate to:**
- Channel X (LTV:CAC = ___:1, can scale)
- Channel Y (Magic Number = ___, efficient)

**What to do with budget:**
- Current channel spend: $___/month
- Reallocate to [top-performing channel]
- Expected impact: [better CAC, better LTV, faster payback]

**Exception:** If this channel is <10% of total S&M spend, just pause it. Not worth fixing."

---

#### Recommendation Pattern 4: Invest to Learn (Strategic Channel)

**When:**
- Poor unit economics BUT
- Strategic importance (enterprise channel, brand building, long-term)

**Recommendation:**

"**Continue, but cap investment** — Strategic value > short-term ROI

**Financial Reality:**
- CAC: $___
- LTV: $___
- LTV:CAC: ___:1 (below 3:1 threshold)
- Payback: ___ months (long)

**Why continue despite poor economics:**
- [Strategic reason: e.g., "Enterprise segment requires field events, but deals are 12-month sales cycles"]
- [Brand building: e.g., "Conferences build brand awareness that drives inbound long-term"]
- [Market positioning: e.g., "Need to be present in this channel for credibility"]

**How to manage:**
1. **Cap spend** — Don't scale until economics improve
   - Current: $___/month
   - Cap at: $___/month (hold steady)
2. **Track leading indicators** — Don't just look at short-term CAC/LTV
   - Pipeline influence
   - Brand awareness lift
   - Referral rate from this channel
3. **Re-evaluate quarterly**
   - If economics improve (LTV:CAC >3:1): scale
   - If economics stay poor: reconsider strategy

**Timeline:**
- Give it [6-12 months] to show results
- If no improvement: kill or reduce drastically

**Risk:** You're subsidizing growth. Make sure it's worth it."

---

### Step 5: Compare Across Channels (Optional)

**If user has multiple channels, agent can generate:**

| Channel | CAC | LTV | LTV:CAC | Payback | Magic Number | Quality | Recommendation |
|---------|-----|-----|---------|---------|--------------|---------|----------------|
| Google Ads | $500 | $2,000 | 4:1 | 8mo | 0.9 | High | Scale |
| Content | $200 | $1,500 | 7.5:1 | 4mo | 1.2 | High | Scale |
| Outbound | $10K | $50K | 5:1 | 18mo | 0.6 | Medium | Optimize |
| Events | $15K | $30K | 2:1 | 24mo | 0.3 | Low | Kill |

**Budget allocation recommendation:**
1. Scale: Content (highest efficiency)
2. Scale: Google Ads (strong economics)
3. Optimize: Outbound (improve magic number)
4. Kill: Events (reallocate budget)

---

## Examples

See `examples/` folder for sample conversation flows. Mini examples below:

### Example 1: Scale (Content Marketing)

**Channel:** Organic content (blog, SEO)
- CAC: $200
- LTV: $3,000
- LTV:CAC: 15:1
- Payback: 3 months
- Magic Number: 1.8
- Customer quality: High (lower churn, higher NRR)

**Recommendation:** Scale aggressively. Exceptional unit economics, fast payback, high-quality customers. Increase content spend 2-3x.

---

### Example 2: Optimize (Paid Search)

**Channel:** Google Ads
- CAC: $800
- LTV: $2,000
- LTV:CAC: 2.5:1
- Payback: 14 months
- Magic Number: 0.6
- Customer quality: Lower (higher churn in first 90 days)

**Recommendation:** Test & optimize before scaling. CAC is high, onboarding is weak for this segment. Improve landing page, target higher-intent keywords, better onboarding for paid customers.

---

### Example 3: Kill (Trade Shows)

**Channel:** Industry events
- CAC: $20,000
- LTV: $30,000
- LTV:CAC: 1.5:1
- Payback: 30 months
- Magic Number: 0.2
- Customer quality: Low (off-ICP, many tire-kickers)

**Recommendation:** Kill. CAC too high, payback too long, poor customer quality. Reallocate budget to content and paid search.

---

## Common Pitfalls

### Pitfall 1: Scaling Broken Channels
**Symptom:** "Let's 10x our Google Ads spend!" (LTV:CAC is 1.5:1)

**Consequence:** You accelerate cash burn without improving unit economics. Lose money faster.

**Fix:** Only scale channels with LTV:CAC >3:1 and payback <12 months. Fix broken channels before scaling.

---

### Pitfall 2: Ignoring Customer Quality
**Symptom:** "CAC is only $100!" (but customers churn in 30 days)

**Consequence:** Low CAC means nothing if LTV is also low. You're acquiring churners, not customers.

**Fix:** Track cohort retention and NRR by channel. Low CAC + high churn = bad channel.

---

### Pitfall 3: Celebrating Vanity Metrics
**Symptom:** "We got 10,000 signups from this campaign!" (5% convert to paid)

**Consequence:** Signups don't pay bills. CAC is calculated on paid customers, not signups.

**Fix:** Track CAC on paid customers only. Ignore vanity metrics like signups, impressions, clicks.

---

### Pitfall 4: Averaging Across Channels
**Symptom:** "Blended CAC is $500" (but hiding that one channel is $10K CAC)

**Consequence:** Bad channels hide in blended metrics. You don't know which channels to kill.

**Fix:** Track CAC, LTV, payback by channel. Compare channels individually.

---

### Pitfall 5: Short-Term CAC Optimization
**Symptom:** "We reduced CAC 50%!" (by targeting low-intent, low-LTV customers)

**Consequence:** CAC dropped but so did LTV. Unit economics got worse, not better.

**Fix:** Optimize for LTV:CAC ratio, not CAC alone. Higher CAC with higher LTV is better.

---

### Pitfall 6: Ignoring Payback Period
**Symptom:** "LTV:CAC is 6:1, this channel is amazing!" (payback is 48 months)

**Consequence:** You run out of cash before recovering CAC. Great ratio, terrible cash flow.

**Fix:** Pair LTV:CAC with payback period. 3:1 with 8-month payback beats 6:1 with 36-month payback.

---

### Pitfall 7: Killing Channels Too Early
**Symptom:** "This channel didn't work after 2 weeks"

**Consequence:** Channels need time to optimize. Killing too early wastes learning.

**Fix:** Give channels 3-6 months and 100+ customers before evaluating. Track trends, not snapshots.

---

### Pitfall 8: Over-Relying on One Channel
**Symptom:** "90% of our customers come from Google Ads"

**Consequence:** Algorithm change, competitor outbids you, channel saturates = business grinds to halt.

**Fix:** Diversify channels. No single channel should be >50% of new customer acquisition.

---

### Pitfall 9: Forgetting Incrementality
**Symptom:** "This retargeting campaign has great ROI!" (but customers would've converted anyway)

**Consequence:** You're paying for conversions that would happen organically. Inflated ROI.

**Fix:** Test incrementality with holdout groups. Only count truly incremental conversions.

---

### Pitfall 10: Strategic Channels Without Limits
**Symptom:** "Enterprise events are strategic, we can't stop!" (losing $500K/year)

**Consequence:** "Strategic" becomes an excuse for burning cash indefinitely.

**Fix:** Cap spend on strategic channels. Set timeline for improvement (6-12 months). If no progress, kill.

---

## References

### Related Skills
- `saas-economics-efficiency-metrics` — CAC, LTV, payback, magic number calculations
- `saas-revenue-growth-metrics` — NRR, churn, cohort analysis by channel
- `finance-metrics-quickref` — Fast lookup for channel evaluation metrics
- `feature-investment-advisor` — Similar ROI framework for feature decisions
- `business-health-diagnostic` — Broader business health assessment

### External Frameworks
- **Brian Balfour (Reforge):** Channel-product fit framework
- **David Skok:** "SaaS Metrics" — CAC, LTV, and payback for channels
- **Tomasz Tunguz:** SaaS channel benchmarking
- **First Round Review:** "How to Find and Scale Your Growth Channels"

### Provenance
- Adapted from `research/finance/Finance_For_PMs.Putting_It_Together_Synthesis.md` (Decision Framework #2)
- Channel economics from `research/finance/Finance for Product Managers.md`
