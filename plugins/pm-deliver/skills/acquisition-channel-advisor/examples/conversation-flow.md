# Example: Channel Evaluation Conversation Flow

This shows a full conversation using the acquisition-channel-advisor skill.

---

## Scenario: Evaluating Content Marketing Channel

### Step 0: Initial Request

**User:**
"Should we scale our content marketing spend? We've been investing in SEO and blog content for 6 months."

---

### Step 0: Context Gathering

**Agent:**
"Let's evaluate your content marketing channel. Please provide:

**Channel details:**
- Channel name: Organic content (blog, SEO)
- How long: 6 months
- Current monthly spend: $___

**Customer acquisition:**
- Customers acquired per month (from this channel): ___
- CAC for this channel: $___ (if known)

**Business context:**
- Blended CAC (all channels): $___
- Blended LTV: $___
- Current MRR/ARR: $___
- Target growth rate: ___% MoM or YoY

You can provide estimates if you don't have exact numbers."

---

**User:**
"Here's our data:

**Channel:**
- Organic content (blog + SEO)
- 6 months running
- Monthly spend: $15K (2 content writers + SEO contractor)

**Acquisition:**
- ~75 customers/month from organic
- CAC: ~$200/customer

**Business context:**
- Blended CAC: $600 (across paid, outbound, organic)
- Blended LTV: $3,000 (24-month avg lifetime, $125 ARPU, 75% margin)
- Current ARR: $1.8M
- Target: 10% MoM growth ($15K MRR growth/month)"

---

### Step 1: Unit Economics

**Agent calculates:**
```
Channel CAC: $200
Blended CAC: $600
Channel is 3x more efficient than blended! ✅

Channel LTV: Need to confirm if similar to blended
Blended LTV: $3,000
```

**Agent:**
"Great! Your content channel has CAC of $200 vs. blended $600—that's 3x more efficient.

**Now let's confirm customer quality:**

**Do customers from organic content have similar LTV to other channels?**

1. **Similar** — They stick around ~24 months like blended average
2. **Higher** — They churn less or expand more (longer lifetime or higher ARPU)
3. **Lower** — They churn faster or are smaller deals
4. **Unknown** — We need to analyze cohort retention data

Choose a number."

---

**User:**
"2 — Higher. Content customers tend to be better educated about our product and have lower churn. I'd estimate 30-month avg lifetime instead of 24-month."

---

**Agent calculates:**
```
Channel LTV (adjusted):
- ARPU: $125/month
- Lifetime: 30 months (vs. 24 blended)
- Gross margin: 75%
- Channel LTV = $125 × 30 × 75% = $2,812

Wait, that's lower than $3,000 blended?
Let me recalculate using the LTV formula...

Actually, if lifetime is 30 months:
LTV = $125 × 30 = $3,750 gross revenue
LTV = $3,750 × 75% margin = $2,812 net LTV

Hmm, but blended LTV was $3,000. Let me ask for clarification.
```

**Agent:**
"Let me confirm: If content customers have 30-month lifetime vs. 24-month blended, and same $125 ARPU:

- Channel LTV = $125 × 30 × 75% = $2,812

But you said blended LTV is $3,000. Does blended include expansion (upsells/cross-sells) that content customers might not have as much of?"

---

**User:**
"Oh right, good catch. Blended LTV includes expansion. Content customers actually stick around longer (30mo vs. 24mo) BUT they expand less. So their total LTV is about $3,200—slightly higher than $3,000 blended."

---

**Agent calculates:**
```
Channel CAC: $200
Channel LTV: $3,200
LTV:CAC = $3,200 / $200 = 16:1 ✅✅✅ (exceptional!)

Payback Period:
Monthly ARPU: $125
Gross Margin: 75%
Monthly Gross Profit: $125 × 75% = $93.75

Payback = $200 / $93.75 = 2.1 months ✅✅✅ (extremely fast!)
```

**Agent:**
"Excellent! Here are your unit economics for organic content:

**Unit Economics:**
- CAC: $200
- LTV: $3,200
- **LTV:CAC: 16:1** ✅✅✅ (exceptional—well above 3:1 threshold)
- **Payback: 2.1 months** ✅✅✅ (extremely fast—well under 12-month target)

This channel has outstanding unit economics. Let's check customer quality next."

---

### Step 2: Customer Quality

**Agent:**
"You mentioned content customers stick around longer (30mo vs. 24mo). Let's confirm quality metrics:

**1. What's the churn rate for customers from organic content?**

1. **Lower than blended** — They stick around longer (you mentioned 30mo vs. 24mo, so this is likely)
2. **Same as blended** — No difference
3. **Higher than blended** — They churn faster
4. **Unknown** — Need cohort analysis

**2. What's the NRR for customers from this channel?**

1. **Higher than blended** — They expand more
2. **Same as blended** — No difference
3. **Lower than blended** — They expand less (you mentioned this earlier)
4. **Unknown**

**3. What's the customer profile?**

1. **Ideal customer profile (ICP)** — Perfect fit
2. **Close to ICP** — Mostly good fit
3. **Off ICP** — Many poor-fit customers
4. **Unknown**"

---

**User:**
"1. Lower churn—monthly churn is ~2% vs. blended 2.8%
2. Lower NRR—about 95% vs. blended 105% (they don't expand as much)
3. Close to ICP—mostly mid-market companies, which is our sweet spot"

---

**Agent analyzes:**
```
Customer Quality Assessment:

Retention: Lower churn (2% vs. 2.8%) ✅
- 30-month lifetime vs. 24-month blended
- They stick around longer = higher quality

NRR: Lower (95% vs. 105%) ⚠️
- Less expansion/upsell
- But still >90% (acceptable)
- Offset by better retention

ICP Fit: Close to ICP ✅
- Mid-market is sweet spot
- Good product-channel fit

Overall: High Quality ✅
```

**Agent:**
"**Customer Quality: High** ✅

**Retention:** Lower churn (2% vs. 2.8%) — content customers stick around 25% longer
**Expansion:** Lower NRR (95% vs. 105%) — less upsell, but acceptable
**ICP Fit:** Close to ICP (mid-market focus)

**Assessment:** High-quality customers. Better retention offsets lower expansion. Overall LTV is higher.

Now let's evaluate scalability."

---

### Step 3: Scalability

**Agent:**
"Can you scale this channel to meet your growth targets?

**1. What's the S&M efficiency (Magic Number) for this channel?**

Let me calculate:
- New MRR from channel per month: 75 customers × $125 ARPU = $9,375
- Channel S&M spend: $15,000/month
- Magic Number = ($9,375 × 4) / $15,000 = $37,500 / $15,000 = 2.5 ✅✅

That's exceptional (>0.75 is efficient).

**2. What's the addressable volume for this channel?**

1. **Large** — Can scale 10x+ (lots of keyword opportunities, TAM is huge)
2. **Medium** — Can scale 2-5x (some saturation risk)
3. **Small** — Near saturation, maybe 1.5x
4. **Unknown**

**3. What's the CAC trend?**

1. **Decreasing** — Getting more efficient (content compounds over time)
2. **Stable** — Consistent CAC around $200
3. **Increasing** — Diminishing returns
4. **Unknown**"

---

**User:**
"Addressable volume: 1 — Large. We've barely scratched the surface on keyword opportunities. SEO takes time but TAM is massive.

CAC trend: 1 — Decreasing. CAC was $300 in month 3, now $200 in month 6. Content compounds—old articles still drive traffic."

---

**Agent calculates:**
```
Scalability Assessment:

Magic Number: 2.5 ✅✅✅
- Well above 0.75 threshold
- For every $1 in content spend, $2.50 in new ARR
- Extremely efficient

Addressable Volume: Large ✅
- Keyword opportunities abundant
- TAM supports 10x+ scale

CAC Trend: Decreasing ✅✅
- $300 → $200 (33% improvement in 3 months)
- Content compounds (old posts keep working)
- Efficiency improving over time

Overall: Highly Scalable ✅✅✅
```

**Agent:**
"**Scalability: Highly Scalable** ✅✅✅

**Magic Number:** 2.5 (exceptional—way above 0.75 threshold)
**Addressable Volume:** Large (10x+ potential)
**CAC Trend:** Decreasing ($300 → $200 in 3 months)

**Key insight:** Content compounds. Old articles continue driving traffic without additional spend. CAC will likely keep decreasing as you scale.

Let me check your growth targets..."

---

**Agent calculates:**
```
Target Growth: 10% MoM
Current MRR: $150K ($1.8M ARR / 12)
Target MRR Growth: $15K/month

Current contribution from content:
75 customers × $125 ARPU = $9,375 MRR/month

Gap: $15,000 - $9,375 = $5,625 MRR needed from other channels

Content covers 62.5% of growth target!
```

**Agent:**
"**Growth Target Analysis:**

You need $15K MRR growth/month (10% of $150K MRR).
Content currently delivers $9.4K MRR/month.
**Content covers 62.5% of your growth target!**

Other channels need to deliver $5.6K MRR/month.

Ready for my recommendation?"

---

**User:**
"Yes! Should we scale content?"

---

### Step 4: Recommendation

**Agent:**
"## ✅ Recommendation: **Scale Content Aggressively**

---

### Why This Is a No-Brainer

**Unit Economics: Exceptional**
- LTV:CAC: 16:1 (5x better than 3:1 threshold)
- Payback: 2.1 months (6x faster than 12-month target)
- CAC: $200 (3x better than $600 blended)

**Customer Quality: High**
- Lower churn: 2% vs. 2.8% blended
- 30-month lifetime vs. 24-month blended
- Close to ICP (mid-market sweet spot)

**Scalability: Highly Scalable**
- Magic Number: 2.5 (exceptional S&M efficiency)
- Addressable volume: Large (10x+ potential)
- CAC decreasing: $300 → $200 (content compounds)

**Strategic Fit:**
- Covers 62.5% of growth target already
- Capital-efficient (low CAC, fast payback)
- Defensible (SEO moats build over time)

---

### How to Scale

**Phase 1: Double Spend (Month 1-3)**
- Current: $15K/month
- Target: $30K/month
- Hire 2 more content writers + expand SEO effort

**Expected Impact:**
- Customers/month: 75 → 150 (if linear scaling)
- MRR impact: $9.4K → $18.8K/month
- CAC: $200 → potentially $180 (economies of scale)

**Covers 125% of growth target! You'd overshoot by $3.8K MRR/month.**

---

**Phase 2: Triple Spend (Month 4-6)**
- Current: $15K/month
- Target: $45K/month
- Add video content, expand to new verticals

**Expected Impact:**
- Customers/month: 75 → 225
- MRR impact: $28K/month
- Covers 187% of growth target

---

### What to Monitor Weekly

**Must-track metrics:**
1. **CAC by month** — Should stay <$250
   - If CAC increases >20%, slow down scaling
2. **Magic Number** — Should stay >1.5
   - If drops <1.0, optimize before scaling further
3. **Customer quality** — Churn rate, NRR, ICP fit
   - Make sure quality doesn't degrade with scale
4. **Content ROI** — Track which topics/keywords drive best customers

**Warning signs to watch:**
- CAC increasing >20% month-over-month
- Magic Number dropping <1.0
- Churn rate for new content customers >3%
- Quality degradation (more off-ICP customers)

---

### Recommended Scaling Plan

| Month | Monthly Spend | New Customers | MRR Impact | CAC Target | Magic Number Target |
|-------|---------------|---------------|------------|------------|---------------------|
| Current | $15K | 75 | $9.4K | $200 | 2.5 |
| Month 1 | $20K | 100 | $12.5K | $200 | 2.5 |
| Month 2 | $25K | 125 | $15.6K | $200 | 2.5 |
| Month 3 | $30K | 150 | $18.8K | $200 | 2.5 |

**Gradual scaling minimizes risk while testing assumptions.**

---

### Budget Reallocation (Optional)

If you scale content 2x and it's working, consider:

**Reallocate from underperforming channels:**
- Example: If you have a channel with LTV:CAC <2:1
- Move that budget to content (LTV:CAC 16:1)

**Impact:**
- Reallocating $10K from a 1.5:1 channel to content (16:1)
- Frees up $10K → invest in content = ~50 more customers/month
- MRR impact: +$6.25K/month

---

### Risk Assessment

**Risk Level: Very Low** ✅

**Why:**
- Proven channel (6 months data, 450+ customers)
- Improving efficiency (CAC decreasing)
- Fast payback (2.1 months) = low cash risk
- High-quality customers (lower churn)

**Biggest risk:**
- Scaling too fast and diluting quality (hiring bad writers)
- Solution: Scale gradually (25-50% increase/month), not 100%

---

### Timeline & Milestones

**Month 1:**
- Increase spend $15K → $20K
- Hire 1 additional content writer
- Target: 100 customers, $12.5K MRR

**Month 2:**
- If Month 1 hits target: increase to $25K
- Expand SEO to new keywords
- Target: 125 customers, $15.6K MRR

**Month 3:**
- If Month 2 hits target: increase to $30K
- Test video content (blog posts → YouTube)
- Target: 150 customers, $18.8K MRR

**Month 6:**
- Re-evaluate: Are we still at 16:1 LTV:CAC?
- If yes: continue scaling to $50K/month
- If no: optimize before further scaling

---

### Comparison to Other Channels

Just for context, how does content compare to your other channels?

| Channel | CAC | LTV:CAC | Payback | Magic Number | Recommendation |
|---------|-----|---------|---------|--------------|----------------|
| **Content (Organic)** | **$200** | **16:1** | **2.1mo** | **2.5** | **Scale 2-3x** ✅ |
| Blended (All Channels) | $600 | 5:1 | 6.4mo | ? | Improve mix |
| [Other Channels?] | ? | ? | ? | ? | [Need data] |

**Content is your most efficient channel by far.**

If you have data on other channels (Google Ads, outbound, etc.), I can compare them and recommend budget reallocation.

---

## Summary

**Decision: Scale content spend from $15K → $30K/month over 3 months**

**Expected Outcome:**
- Customers/month: 75 → 150
- MRR impact: +$9.4K/month additional growth
- Total MRR from content: $18.8K/month
- **Covers 125% of your 10% MoM growth target**

**Why it works:**
- Best channel economics (16:1 LTV:CAC)
- Fastest payback (2.1 months)
- Content compounds (old posts keep working)
- High-quality, long-lived customers

**Risk: Very Low**

**Next step:** Approve budget increase and hire 1-2 content writers.

---

Want to discuss:
1. Budget reallocation from other channels?
2. Content strategy (topics, keywords, formats)?
3. How to compare this to other acquisition channels?"

---

**User:**
"This is perfect. One question: Should we also compare this to our Google Ads channel?"

**Agent:**
"Absolutely! Share your Google Ads metrics and I'll run a side-by-side comparison:

- Monthly spend
- Customers acquired/month
- CAC
- LTV (or similar to blended?)
- Churn/NRR (if different from blended)
- Magic Number (if known)

Then I'll recommend optimal budget allocation between content and Google Ads."

---

[Conversation could continue with multi-channel optimization...]
