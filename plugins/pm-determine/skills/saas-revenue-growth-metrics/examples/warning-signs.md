# Example: Warning Signs (Leaky Bucket)

**Company:** MarketingFlow (SMB marketing automation SaaS)
**Stage:** Early growth, post-Seed
**Customer Base:** 2,000 accounts, 10,000 users
**Period:** Monthly snapshot

---

## Revenue Metrics

### MRR/ARR
```
Starting MRR: $500,000
+ New MRR: $100,000 (200 new accounts)
+ Expansion MRR: $5,000 (minimal upsells)
- Churned MRR: $50,000 (120 accounts churned)
- Contraction MRR: $10,000 (40 accounts downgraded)
Ending MRR: $545,000

MRR Growth Rate: 9% MoM (but driven entirely by new customer acquisition)
ARR: $6.5M
```

### ARPA/ARPU
```
ARPA = $545,000 / 2,000 accounts = $272/month
ARPU = $545,000 / 10,000 users = $54.50/month
Average seats per account = 5 users
```

### Revenue Components
```
New MRR: $100K (20% of base — very high)
Expansion MRR: $5K (1% of base — very low)
Churned MRR: $50K (10% of base — crisis level)
Contraction MRR: $10K (2% of base — concerning)
```

---

## Retention & Expansion Metrics

### Churn Rate
```
Logo Churn: 120 / 2,000 = 6% monthly (~50% annual)
Revenue Churn: $50K / $500K = 10% monthly (~69% annual)
```

**Analysis:** Revenue churn > logo churn = losing bigger customers. Crisis signal.

### NRR
```
Starting ARR: $6M
Expansion: $60K (annual)
Churned: $600K (annual)
Contraction: $120K (annual)
Ending ARR: $5.34M

NRR = $5.34M / $6M = 89%
```

**Analysis:** NRR <100% = contracting base. Losing revenue from existing customers faster than expanding them.

### Quick Ratio
```
Gains = $100K + $5K = $105K
Losses = $50K + $10K = $60K
Quick Ratio = $105K / $60K = 1.75
```

**Analysis:** Quick Ratio <2 = leaky bucket. Barely outpacing losses.

---

## Cohort Retention Trend (Negative Signal)

| Cohort | Month 3 Retention | Month 6 Retention | Month 12 Retention |
|--------|-------------------|-------------------|---------------------|
| 12 months ago | 82% | 75% | 68% |
| 6 months ago | 75% | 65% | TBD |
| Current | 68% (on track) | TBD | TBD |

**Analysis:** Newer cohorts churning FASTER than older cohorts. Product-market fit is degrading.

---

## Analysis

### 🚨 Critical Problems

**Unsustainable churn:**
- 6% monthly logo churn = ~50% annual (crisis level)
- 10% monthly revenue churn = ~69% annual (existential threat)
- Revenue churn > logo churn = losing high-value customers
- Churn rate increasing (was 4% six months ago)

**Cohort degradation:**
- Newer customers churn faster than older customers
- Month 6 retention: 75% → 65% → on track for 58%
- This signals product-market fit is getting WORSE, not better

**No expansion engine:**
- Expansion revenue only 1% of MRR (should be 10-30%)
- NRR at 89% (contracting, not expanding)
- Only 5% of customers have ever expanded

**Leaky bucket:**
- Quick Ratio 1.75 (barely exceeding losses)
- Losing $60K/month, only gaining $105K/month
- Running on a treadmill: need 200 new customers/month just to stay flat

**Revenue dependency:**
- 90% of growth from new customer acquisition
- If acquisition slows, revenue will shrink immediately
- Retention is broken—scaling will just accelerate the problem

---

### 📊 Root Cause Investigation Needed

**Why is churn increasing?**
- Product quality degrading?
- Wrong customer segment (poor fit)?
- Onboarding failures?
- Competitive pressure?
- Pricing too high for value delivered?

**Why are newer cohorts worse?**
- Customer acquisition quality degrading?
- Product changes breaking key use cases?
- Support quality declining as company scales?

**Why no expansion?**
- No upsell paths in packaging?
- Customers not reaching "aha moment" where they'd expand?
- Product doesn't grow with customer needs?

---

## Actions Recommended (URGENT)

### 🛑 STOP Scaling Acquisition

Do NOT increase marketing spend until retention is fixed. Scaling a leaky bucket just burns cash faster.

**Why:** At current churn rates, every dollar spent acquiring customers leaks out within 12 months. Fix the bucket first.

---

### 🔥 Priority 1: Fix Retention (Weeks 1-4)

**Investigate churn:**
1. Run churn interviews with 20-30 churned customers
2. Segment churn by cohort, use case, customer size
3. Identify top 3 churn reasons

**Quick wins:**
1. Improve onboarding (70% of churn happens in first 60 days)
2. Proactive support for at-risk accounts (identify usage drop-offs)
3. Re-engage dormant accounts before they churn

**Goal:** Reduce logo churn from 6% to 4% within 8 weeks, target 3% within 16 weeks.

---

### 🔥 Priority 2: Build Expansion Engine (Weeks 5-8)

**Create upsell paths:**
1. Introduce premium tier (advanced features)
2. Usage-based add-ons (additional seats, integrations)
3. Cross-sell complementary features

**Identify expansion candidates:**
1. Which customers use product heavily? (Target for upsell)
2. Which customers hit usage limits? (Offer expansion)

**Goal:** Increase expansion MRR from 1% to 5% of base within 12 weeks.

---

### 🔥 Priority 3: Improve Cohort Retention (Ongoing)

**Track cohorts rigorously:**
1. Weekly cohort retention dashboards
2. Compare new cohorts to baseline (75% at Month 6)
3. Don't scale until new cohorts retain BETTER than old cohorts

**Product improvements:**
1. Fix onboarding (time-to-value)
2. Improve core use cases (reduce churn reasons)
3. Add sticky features (integrations, data accumulation)

**Goal:** Reverse cohort degradation trend within 16 weeks. New cohorts should retain at 75%+ by Month 6.

---

### ✅ Success Criteria (Fix Before Scaling)

Do NOT scale acquisition until:
- [ ] Logo churn <4% monthly (ideally <3%)
- [ ] Revenue churn <5% monthly
- [ ] NRR >100% (expansion exceeds churn)
- [ ] Quick Ratio >2.5 (ideally >4)
- [ ] New cohorts retain same or better than old cohorts
- [ ] Expansion MRR >5% of total MRR

**Timeline:** 12-16 weeks to fix. Then reassess scaling.

---

## Financial Impact of Fixing Retention

**Current state (bad):**
- Need 200 new customers/month just to offset churn
- Net growth: only 80 customers/month after churn
- 90% of acquisition spend wasted on replacing churned customers

**If churn fixed to 3% (good):**
- Need 60 new customers/month to offset churn
- Net growth: 140 customers/month (75% more efficient)
- Acquisition budget goes 3x further

**If NRR fixed to 110% (great):**
- Existing base grows 10%/year without new customers
- All new acquisition is net growth
- Can afford higher CAC because LTV increases 2-3x

**Bottom line:** Fixing retention is worth 6-12 months of paused growth. Don't skip this.
