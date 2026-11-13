# Example: Feature Investment Advisor Conversation Flow

This shows a full conversation using the feature-investment-advisor skill.

---

## Scenario: Evaluating a Time Tracking Add-On

### Step 0: Initial Request

**User:**
"Should we build time tracking as a paid add-on to our project management tool?"

---

### Step 0: Context Gathering

**Agent:**
"Let's evaluate the financial impact of this feature investment. Please provide:

**Feature description:**
- What's the feature? (1-2 sentences)
- Target customer segment (SMB, mid-market, enterprise, all)

**Current business context:**
- Current MRR/ARR
- Current ARPU/ARPA
- Current monthly churn rate
- Gross margin %

**Constraints:**
- Development cost estimate (team size × time)
- Any ongoing COGS or OpEx implications?

You can provide estimates if you don't have exact numbers."

---

**User:**
"Here's our context:

**Feature:**
Time tracking add-on with start/stop timers, time reports, and invoice export. Target all segments.

**Business context:**
- MRR: $2M (1,000 customers)
- ARPA: $2,000/month
- ARPU: $200/month (average 10 users per account)
- Monthly churn: 3%
- Gross margin: 80%

**Development:**
- 2 engineers × 3 months = ~$100K dev cost
- No significant ongoing COGS (minimal compute cost)
- Might add 10-20 support tickets/month"

---

### Step 1: Revenue Connection

**Agent:**
"How does this feature impact revenue? Choose the option that best describes the revenue connection:

1. **Direct monetization (new revenue stream)** — We'll charge for this (new pricing tier, paid add-on, usage-based fee)
2. **Retention improvement (reduce churn)** — Addresses key churn reason; keeps customers from leaving
3. **Conversion improvement (trial-to-paid)** — Helps convert free/trial users to paid customers
4. **Expansion enabler (upsell/cross-sell)** — Creates upsell path or drives usage-based expansion
5. **No direct revenue impact** — Table stakes, platform improvement, or strategic value only

Choose a number, or describe a custom revenue connection."

---

**User:**
"1 — Direct monetization. We'll charge $5/user/month as an add-on."

---

**Agent:**
"Got it. You're planning to charge $5/user/month for time tracking.

**Follow-up questions:**

1. **How many users do you have total?**
   - Current: 1,000 accounts × 10 users/account = 10,000 users

2. **What adoption rate do you expect?**
   - Conservative (10-15%)
   - Base case (20-25%)
   - Optimistic (30-40%)
   - Or provide your own estimate

3. **Have you validated willingness-to-pay?**
   - Surveyed customers
   - Prototype tested
   - No validation yet"

---

**User:**
"We have 10,000 users total.

I'll go with base case: 20% adoption (2,000 users).

We've surveyed 50 customers and 30% said they'd pay $5-10/user for time tracking, so 20% feels conservative."

---

**Agent calculates:**
```
Total Users: 10,000
Adoption Rate: 20%
Users Adopting: 2,000
Price: $5/user/month

Monthly Revenue: 2,000 × $5 = $10,000/month
Annual Revenue: $120,000/year
Gross Profit: $120,000 × 80% = $96,000/year
```

**Agent:**
"Great! Based on 20% adoption at $5/user:

**Revenue Impact:**
- Monthly: $10,000 MRR
- Annual: $120,000 ARR
- Gross profit (80% margin): $96,000/year

Now let's look at costs."

---

### Step 2: Cost Structure

**Agent:**
"You mentioned:
- Dev cost: $100K (2 engineers × 3 months)
- COGS: Minimal
- Support: 10-20 tickets/month

Let me confirm the full cost picture:

**One-time development:** $100,000

**Ongoing monthly costs:**
- COGS (compute, storage): $___
- Support (est. 15 tickets/month × $50/ticket): $750/month = $9K/year
- Total ongoing: $9K/year

Does this look right?"

---

**User:**
"Yes, that's right. COGS is negligible (maybe $100/month for compute), and support is probably $750/month."

---

**Agent calculates:**
```
Development Cost (one-time): $100,000

Ongoing Annual Costs:
- COGS: $100/month × 12 = $1,200/year
- Support: $750/month × 12 = $9,000/year
- Total: $10,200/year

Net Annual Profit:
$120,000 revenue - $10,200 ongoing costs = $109,800/year gross profit
After initial dev cost recovery: $109,800 - $100,000 = $9,800 in year 1
```

**Agent:**
"Got it. Here's the cost structure:

**Costs:**
- One-time dev: $100,000
- Ongoing: $10,200/year (COGS + support)

**Net Impact:**
- Year 1: $109,800 revenue - $100,000 dev - $10,200 ongoing = -$200 (essentially breakeven)
- Year 2+: $109,800/year profit (no dev cost)

**Payback Period:** ~11 months"

---

### Step 3: Constraints

**Agent:**
"What constraints or timing considerations apply?

1. **Time-sensitive competitive threat** — Competitor launched this; we're losing deals
2. **Limited budget/team capacity** — We can only build one major feature this quarter
3. **Dependencies on other work** — Requires platform improvements or other features first
4. **No major constraints** — We have capacity and flexibility

Choose a number, or describe your constraints."

---

**User:**
"2 — We can only build one major feature this quarter. We're also considering a Gantt chart view (similar dev cost, but no monetization—retention play)."

---

**Agent:**
"Got it. You're choosing between:
- Time tracking (direct monetization, $120K ARR)
- Gantt chart (retention/competitive feature, indirect impact)

Let me calculate the trade-off to help you decide."

---

### Step 4: Recommendation

**Agent:**
"Based on your inputs, here's my analysis and recommendation:

---

## ✅ Recommendation: **Build Time Tracking Now**

### Financial Case: Strong

**Revenue Impact:**
- $10K MRR / $120K ARR
- 2,000 users × $5/user (20% adoption)
- Gross margin: 80%
- Net annual profit: $109,800 (after ongoing costs)

**Costs:**
- Development: $100,000 (one-time)
- Ongoing: $10,200/year (COGS + support)

**ROI:**
- Year 1: Essentially breakeven (-$200)
- Year 2: 2.2:1 ROI ($109,800 profit / $100K investment)
- Payback: 11 months

**Contribution Margin:**
- Revenue: $120K/year
- Variable costs: $10.2K/year
- Contribution margin: 91.5% (excellent)

---

### Why This Makes Sense

**1. Fast payback (11 months)**
- You recover the investment in under a year
- Low risk—if adoption is even 15% (not 20%), still profitable

**2. High-margin revenue**
- 80% gross margin on add-on revenue
- Minimal ongoing costs (only $10K/year)
- Scales well (more users = more revenue, same cost)

**3. Validated demand**
- 30% of surveyed customers said they'd pay $5-10/user
- 20% adoption is conservative

**4. Direct revenue > indirect retention (vs. Gantt chart)**
- Gantt chart = retention play (indirect, hard to measure)
- Time tracking = direct revenue (measurable, predictable)
- If you can only build one: choose measurable revenue

---

### Comparison: Time Tracking vs. Gantt Chart

| Metric | Time Tracking | Gantt Chart |
|--------|---------------|-------------|
| Revenue Impact | $120K ARR (measurable) | Indirect (churn reduction) |
| Development Cost | $100K | $100K (similar) |
| Payback Period | 11 months | Unknown (depends on churn impact) |
| ROI (Year 2) | 2.2:1 | Depends on retention improvement |
| Risk | Low (validated demand) | Medium (hypothesis, not validated) |

**Verdict:** Time tracking has clearer ROI. Build it first.

**BUT:** If churn interviews show Gantt charts are a top 3 churn reason, reconsider.

---

### Next Steps

1. **Build MVP (Weeks 1-8)**
   - Core time tracking (start/stop timers)
   - Time reports (basic)
   - Delay invoice export to v2 if scope is tight

2. **Beta Test (Weeks 9-10)**
   - Launch to 50-100 customers
   - Validate $5/user pricing
   - Measure adoption (target: 20%+)

3. **Broad Launch (Week 11)**
   - If beta adoption is >15%, launch broadly
   - If <15%, adjust pricing or positioning

4. **Monitor Metrics (Ongoing)**
   - Track adoption rate weekly (target: 20%)
   - Monitor support load (should stay <20 tickets/month)
   - Measure MRR growth from add-on

5. **Re-evaluate Gantt Chart (Q2)**
   - If time tracking hits 20% adoption: build Gantt next
   - If adoption is low: investigate why before building more features

---

### Decision Criteria to Proceed

**Build if:**
- Beta adoption >15%
- Support load manageable (<30 tickets/month)
- Pricing validated ($5/user is acceptable)

**Pause/pivot if:**
- Beta adoption <10% (pricing too high or low demand)
- Support costs >$2K/month (unsustainable)
- Churn increases (feature causes confusion)

---

### Sensitivity Analysis (What If?)

**If adoption is 15% (not 20%):**
- Revenue: $90K/year
- Payback: 14 months (still acceptable)
- ROI: 1.6:1 in year 2 (still positive)

**If adoption is 30% (optimistic):**
- Revenue: $180K/year
- Payback: 7 months (excellent)
- ROI: 3.6:1 in year 2 (very strong)

**If you can reduce dev cost to $75K:**
- Payback: 8 months (great)
- ROI: 2.9:1 in year 2

**Bottom line:** Even conservative scenarios are profitable. Build it.

---

## Want to explore further?

1. **See detailed math breakdown**
2. **Compare to Gantt chart (if you have churn data)**
3. **Adjust assumptions** (pricing, adoption, cost)
4. **Export this recommendation** (for stakeholder review)"

---

**User:**
"This is super helpful. Can you show me the detailed math?"

---

**Agent:**
"Sure! Here's the full financial breakdown:

### Detailed Calculations

**Revenue:**
```
Total Users: 10,000
Adoption Rate: 20%
Users Adopting: 10,000 × 20% = 2,000 users

Price per User: $5/month
Monthly Revenue: 2,000 × $5 = $10,000 MRR
Annual Revenue: $10,000 × 12 = $120,000 ARR
```

**Costs:**
```
Development (one-time):
  2 engineers × 3 months × $16,667/eng-month = $100,000

Ongoing Monthly Costs:
  COGS (compute): $100/month
  Support: 15 tickets/month × $50/ticket = $750/month
  Total: $850/month

Ongoing Annual Costs:
  $850 × 12 = $10,200/year
```

**Profit:**
```
Gross Margin: 80%
Gross Profit (Annual): $120,000 × 80% = $96,000/year

After Ongoing Costs:
  $120,000 revenue - $10,200 costs = $109,800 net profit/year

Year 1 (with dev cost):
  $109,800 - $100,000 dev = $9,800 net profit

Year 2+ (no dev cost):
  $109,800 net profit/year
```

**ROI:**
```
Year 1 ROI:
  $9,800 profit / $100,000 investment = 0.098:1 (basically breakeven)

Year 2 ROI:
  $109,800 profit / $100,000 investment = 1.098:1

Cumulative 2-Year Profit:
  Year 1: $9,800
  Year 2: $109,800
  Total: $119,600 profit on $100K investment = 2.2:1 ROI
```

**Payback Period:**
```
Monthly net profit = $109,800 / 12 = $9,150/month

Payback = $100,000 / $9,150 = 10.9 months (11 months)
```

**Contribution Margin:**
```
Revenue: $120,000/year
Variable Costs: $10,200/year (COGS + support)
Contribution Profit: $109,800/year
Contribution Margin: $109,800 / $120,000 = 91.5%
```

Does this breakdown help?"

---

**User:**
"Yes! One more question: what if we charge $10/user instead of $5/user?"

---

**Agent:**
"Great question! Let's recalculate at $10/user:

### Scenario: $10/user (double the price)

**Assumptions:**
- Higher price likely reduces adoption
- Conservative: 15% adoption (down from 20%)
- Optimistic: 20% adoption (same as $5/user base case)

**Conservative (15% adoption at $10/user):**
```
Users: 10,000 × 15% = 1,500 users
Revenue: 1,500 × $10 = $15,000 MRR = $180,000 ARR
Net Profit: $180,000 - $10,200 = $169,800/year
Year 1 Profit: $169,800 - $100,000 = $69,800
Payback: 7 months
ROI (Year 2): 2.7:1
```

**Optimistic (20% adoption at $10/user):**
```
Users: 10,000 × 20% = 2,000 users
Revenue: 2,000 × $10 = $20,000 MRR = $240,000 ARR
Net Profit: $240,000 - $10,200 = $229,800/year
Year 1 Profit: $229,800 - $100,000 = $129,800
Payback: 5 months
ROI (Year 2): 3.3:1
```

### Recommendation on Pricing

**$10/user is better IF:**
- Adoption stays >15% (survey data shows 30% would pay $5-10, so likely yes)
- Higher ARPU, same/similar adoption = better unit economics
- Faster payback (5-7 months vs. 11 months)

**Test Approach:**
1. Launch beta at $10/user with 50 customers
2. If adoption >15%, keep $10/user
3. If adoption <10%, drop to $7/user or $5/user

**My recommendation:** Start at $10/user. Easier to lower price than raise it later."

---

**User:**
"Perfect. I'm convinced. Let's build time tracking at $10/user."

---

**Agent:**
"Excellent decision! Here's a summary you can share with stakeholders:

---

## Feature Investment Decision: Time Tracking Add-On

**Decision:** ✅ Build now (Q1 priority)

**Pricing:** $10/user/month (test in beta, adjust if needed)

**Target:** 15-20% adoption (1,500-2,000 users)

**Financial Projections:**
- Year 1 Revenue: $180-240K ARR
- Year 1 Net Profit: $70-130K (after $100K dev cost)
- Payback: 5-7 months
- Year 2 ROI: 2.7-3.3:1

**Next Steps:**
1. Kickoff: Week 1 (2 engineers, 3 months)
2. Beta launch: Week 10 (50-100 customers, validate $10/user pricing)
3. Broad launch: Week 12 (if beta adoption >15%)
4. Monitor: Track adoption weekly, support load, MRR growth

**Success Criteria:**
- Adoption >15% within 3 months of launch
- Support <30 tickets/month
- $15K+ MRR within 6 months

Good luck with the build! 🚀

---

Want me to create a feature brief or PRD template for this?"

---

**User:**
"No, that's all I needed. Thanks!"

**Agent:**
"You're welcome! Good luck building time tracking. Feel free to come back if you need to evaluate other features."
