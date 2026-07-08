---
name: organic-growth-advisor
description: "Identify which organic growth path to pursue — new segments, geographies, channels, or products. Use when diagnosing where a growth constraint lives and which McKinsey growth level to act\
  \ on next."
compatibility: opencode
argument-hint: "[product and growth context]"
metadata:
  best_for:
    - "Choosing which organic growth motion to pursue when multiple seem viable"
    - "Diagnosing whether the constraint is in reach, access, market context, or product value"
    - "Setting up an AI-assisted growth experiment with the right starting hypothesis"
  intent: >-
    Guide product managers through a fast triage to identify which of four organic growth paths fits their current constraint: new customer segments (L2), new geographies (L3), new distribution channels
    (L4), or new products or services (L5). Uses a 2x2 diagnostic based on customer/market context familiarity and degree of product change required. Outputs a growth path recommendation with rationale
    and immediate next steps.
  scenarios:
    - "We need to grow but aren't sure if we should go after new customer segments or new geographies"
    - "Help me figure out which McKinsey growth level we should focus on"
    - "We have strong product-market fit but growth is stalling. Where should we look?"
    - "Which organic growth path fits our current situation?"
  type: interactive
---


## Purpose

Help product managers identify which organic growth path to pursue by diagnosing where the constraint actually lives. This is not a comprehensive strategy tool. It is a fast triage that puts you in the right lane before you start building hypotheses or running experiments.

The four growth paths covered here are drawn from the McKinsey Growth Pyramid (Levels 2 through 5). Levels 1, 6, and 7 are out of scope: Level 1 (existing products to existing customers) is a retention and optimization problem, not a growth motion. Levels 6 and 7 (new industry structure, new arenas) require capital and executive mandate beyond typical product team scope.

This skill does three things and nothing more:
1. Diagnoses where your growth constraint lives using two questions
2. Places your situation on the Growth Path Matrix (customer/market context vs. degree of product change)
3. Recommends one growth path with rationale, a diagnostic question, and a first experiment

### Anti-Patterns (What This Is NOT)

- **Not a rigorous diagnostic instrument:** A fast triage tool, not a scoring model
- **Not a maturity model or rubric:** No stages, no grades, no weighted criteria
- **Not a substitute for customer discovery:** It points you in a direction; discovery validates it
- **Not a guarantee:** If the recommendation does not feel right, that tension is worth exploring

### When to Use This Skill

- Growth is stalling and you are unsure which lever to pull next
- Multiple growth paths seem viable and you need to choose one to test first
- You want to set up an AI-assisted experiment with a clear hypothesis
- A team or stakeholder debate about growth direction needs a fast resolution

### When NOT to Use This Skill

- You have not yet achieved core product-market fit (fix L1 first)
- You already have a validated growth path in motion (do not switch lanes mid-experiment)
- You need a rigorous strategic planning tool (this is triage, not strategy)
- You lack basic context about your current customers and their problems (gather that first)

---

## Input

**Works best with:** Your product and where growth feels stuck, in a sentence or two.
**Also useful:** Which customers/markets you serve today, what you've already tried, and any paths leadership is pushing (new segments, geos, channels, products).

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** The advisor opens with Q1 of the 3-question triage to place you on the Growth Path Matrix.

**Example invocation:** `Growth triage: B2B payroll tool, strong in US mid-market, plateaued — CEO wants Europe, sales wants an SMB tier.`

## Key Concepts

### The Growth Path Matrix

Two questions place your situation on the matrix:

**X axis: Customer/Market Context**
How familiar is the next customer or market you want to reach?
- **Known:** Same market, same type of buyer, familiar problem context
- **Less Known:** Different geography, unfamiliar cultural or regulatory context, buyer type you have not served before

**Y axis: Degree of Product Change**
How much does the product itself need to change to unlock the next wave of growth?
- **Low:** The product mostly works. What needs to change is how customers find or access it, or which customer you go after next.
- **High:** The product needs to evolve. New capabilities or an entirely new product line is required to solve the next job.

### The Four Growth Paths

**L2: New Customer Segments** (Known context + Low product change)
You already solve a real problem. A nearby buyer may need it too.

**L4: New Distribution Channels** (Known context + High product change)
Product offers same value. People need a better way to find or access it.

**L3: New Geographies** (Less Known context + Low product change)
The product may travel. The market context does not come with it automatically.

**L5: New Products or Services** (Less Known context + High product change)
Customers are pulling you toward adjacent jobs your offer does not fully solve.

### Why This Order Matters

Risk scales with distance from your core. L2 is closest: same market, same product. L5 is furthest: new product, less familiar context. Most teams overinvest in L5 before they have exhausted L2 and L4. If your core product-market fit is strong and your current market is not saturated, L2 or L4 is almost always the right move first.

### The Knowledge Principle

Innovation at any level is downstream of accumulated contextual knowledge. The teams that succeed at L3 are not the ones who moved fastest. They are the ones who studied how value actually travels in the new market before they tried to scale it. The teams that succeed at L5 are not the most creative. They built the adjacent product their existing customers were already asking for, in language they already understood.

---

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the default interaction protocol for this skill.

It defines:
- session heads-up + entry mode (Guided, Context dump, Best guess)
- one-question turns with plain-language prompts
- progress labels (for example, Context Q1/3 and Recommendation)
- interruption handling and pause/resume behavior
- numbered recommendations at decision points
- quick-select numbered response options for regular questions (include `Other (specify)` when useful)

This file defines the domain-specific assessment content. If there is a conflict, follow this file's domain logic.

---

## Application

This interactive skill asks **3 adaptive questions**, offering **3 enumerated options** at each diagnostic step.

---

### Question 1: Current Situation

**Agent asks:**

"Let's identify your best organic growth path. To start:

- What does your product do, and who is your current core customer?
- Where is growth stalling right now?
- What have you already tried?"

Accept a brief answer. Two to four sentences is enough. The goal is to establish baseline context before asking the diagnostic questions.

---

### Question 2: Customer/Market Context

**Agent asks:**

"Think about the next customer or market you want to reach: the one who would unlock your next wave of growth.

How familiar is that context to you?"

**Offer 3 enumerated options:**

1. **Well known** — Same market, same type of buyer, familiar problem and context. You have served customers like this before.
2. **Somewhat known** — Adjacent buyer or market. You have a hypothesis about who they are, but limited direct experience with them.
3. **Less known** — New geography, new industry, new buyer profile. Their context, norms, and decision-making process are meaningfully different from what you know.

---

### Question 3: Degree of Product Change

**Agent asks:**

"To reach that customer and grow, how much does your product need to change?

What does the constraint actually require?"

**Offer 3 enumerated options:**

1. **Low change** — The product mostly works for this next customer. What needs to change is how they find it, access it, or how you reach them.
2. **High change** — The product does not fully solve what this customer needs. New capabilities or a new product line is required.
3. **Somewhere in between** — Describe what feels more pressing. That will determine the path.

---

### Output: Growth Path Recommendation

After three questions, the agent delivers a recommendation using the pattern below.

---

#### Recommendation Pattern

```markdown
## Your Growth Path: [L2 / L3 / L4 / L5] — [Name]

**Where you sit on the matrix:**
- Customer/market context: [Known / Less Known]
- Degree of product change: [Low / High]

**Why this path fits your situation:**
[2 to 3 sentences connecting their specific context to the growth path. Be direct. Reference what they told you.]

**The diagnostic question to keep asking:**
[One sharp question: the one that will tell them if they are right about this path]

**What innovation looks like here:**
[Concrete description of what real innovation looks like at this level. Not a feature list, but a pattern.]

**A first experiment to run this week:**
[One specific, low-cost action they can take in the next 5 to 7 days to test whether this path is real]

**Watch out for:**
[One trap that kills teams pursuing this path: the most common mistake at this level]
```

---

#### Path-Specific Guidance

**L2: New Customer Segments**

Diagnostic question: Who else has the problem we already solve?

What innovation looks like: Finding adjacent buyers inside your existing market whose context is similar enough that your current product mostly works for them. Not rebuilding value. Improving how you reach, message, and onboard a slightly different buyer.

First experiment: Identify three companies or individuals who match a buyer profile adjacent to your ICP. Reach out directly. Ask them to describe their version of the problem you solve. Do not pitch. Listen for what is the same and what is different.

Watch out for: Assuming adjacent buyers need the same onboarding and messaging as your core ICP. They are close enough to reach, but different enough to misunderstand. Word of mouth travels within segments, not across them.

---

**L4: New Distribution Channels**

Diagnostic question: Where else could customers discover or access our value?

What innovation looks like: Turning product output into a distribution surface. Placing the product where buyers already spend time. Creating a free tier or embedded entry point that removes the signup barrier. The product does not change. The front door does.

First experiment: Identify one place where your product output is already being shared or seen by non-users. Map what a non-user sees when they encounter it. Ask whether that moment creates curiosity or stops there. Design one change to that moment that makes curiosity easier to act on.

Watch out for: Confusing marketing campaigns with distribution innovation. A campaign gets attention once. A distribution channel compounds. The test is whether the mechanism works without ongoing spend behind it.

---

**L3: New Geographies**

Diagnostic question: Where is demand already showing up that we do not yet serve well?

What innovation looks like: Studying how word of mouth actually travels in the target market before scaling anything. Building local trust signals: content, partners, language. Doing that before investing in paid growth. Pacing expansion to match local product-market fit signals, not a global launch calendar.

First experiment: Look at your current inbound data. Is there organic traffic, signups, or inquiries from a market you have not targeted? If yes, reach out to three of those users and ask why they found you and what they were hoping to get. That is your signal.

Watch out for: Assuming what worked at home works everywhere. Trust is built differently across markets. The product may translate. The growth loop almost never does without adaptation.

---

**L5: New Products or Services**

Diagnostic question: What adjacent jobs are customers already trying to solve around us?

What innovation looks like: Building something new that extends the core workflow customers already live in. Not a pivot, but an expansion. The new product retains existing customers by absorbing more of their workflow and attracts new buyers who need that job done.

First experiment: Ask five current customers what they do immediately before or after using your product to complete the job it helps with. Look for a consistent adjacent step they take with a different tool or manual process. That gap is your L5 hypothesis.

Watch out for: Building new before the core is strong. L5 requires more knowledge, more resources, and more risk than any other path. If you have not saturated L2 and L4 first, you are probably moving too early.

---

## Examples

### Example 1: L2 Recommendation

**Context:** B2B SaaS project management tool. Core ICP is engineering teams. Growth has slowed. They have tried paid ads and a PLG free tier. Both underperforming.

**Q2 response:** Well known — same buyer type, familiar context.

**Q3 response:** Low change — the product mostly works, the constraint is reach.

**Recommendation: L2 — New Customer Segments**

The product solves a coordination problem engineering teams have. Design and product teams inside the same companies have a nearly identical coordination problem. Word of mouth from engineering is already warm. It just stops at the team boundary. The growth path is not a new channel. It is a new segment inside the same market.

First experiment: Pull a list of your best engineering team customers. Identify which ones also have active design or product teams. Reach out to those adjacent teams directly with a message that references the engineering team's usage. Ask what their coordination problem looks like.

---

### Example 2: L4 Recommendation

**Context:** SaaS tool for creating short-form video explainers. Strong product-market fit with marketing teams. Growth plateau after initial viral push faded.

**Q2 response:** Well known — same buyer type, familiar context.

**Q3 response:** Low change — the product works, the front door is the problem.

**Recommendation: L4 — New Distribution Channels**

Every video created is a distribution surface. Non-users see finished videos but have no low-friction path to act on their curiosity. The growth constraint is not that the product lacks value. It is that the moment of maximum curiosity (watching a video) has no conversion mechanism attached to it.

First experiment: Add a subtle "Made with [Product]" watermark or link to the bottom of every exported video. Track whether inbound signups increase from referral source. If yes, the output is already a channel. Design the next step from there.

---

### Example 3: L3 Recommendation

**Context:** HR software built for US mid-market companies. Starting to see inbound from UK and Australia. No localization done yet.

**Q2 response:** Less known — different regulatory and hiring norms.

**Q3 response:** Low change — the core product mostly works, local context adaptation is needed.

**Recommendation: L3 — New Geographies**

Organic inbound from the UK and Australia is a signal, not a coincidence. Moving directly to paid expansion without understanding local context is a common mistake. UK hiring law, data residency requirements, and HR norms differ enough to create friction at the point of sale and in onboarding, not in the product itself.

First experiment: Talk to the five most active UK or Australian users you already have. Ask what friction they hit when signing up and getting started. Ask what the product does not understand about their context. That conversation maps the localization investment before you make it.

---

### Example 4: L5 Recommendation

**Context:** B2B analytics tool for e-commerce teams. Strong retention, high NPS. Customers keep asking for forecasting and inventory planning features the product does not currently offer.

**Q2 response:** Somewhat known — same buyer type, but the adjacent job pulls toward a different workflow.

**Q3 response:** High change — the product does not yet solve what customers are pulling toward.

**Recommendation: L5 — New Products or Services**

Customers are not just asking for more reports. They are asking you to absorb a workflow step that currently lives in a separate tool. That is an L5 signal. The adjacent job (forecasting and planning) is close enough to your core that building it extends retention and opens a new buyer without requiring a new go-to-market motion.

First experiment: Interview eight current customers who have requested forecasting features. Ask them to walk you through exactly what they do today to handle that job. What tools do they use? Where does it break down? What would good enough look like? You are not scoping the feature. You are validating that the job is real and consistent enough to build toward.

---

## Common Pitfalls

### Pitfall 1: Pursuing L5 before L2 and L4 are exhausted
**Symptom:** The team is excited about building something new while existing market penetration is still below 30%.

**Consequence:** L5 requires the most knowledge, the most capital, and the most time. Starting there before the core is strong usually produces a distraction, not a second product.

**Fix:** Ask honestly whether you have fully exploited L2 and L4 before committing to L5. If not, start there.

---

### Pitfall 2: Confusing a marketing campaign with a distribution channel
**Symptom:** "We launched on Product Hunt and got 2,000 signups" counted as a distribution channel win.

**Consequence:** Campaigns generate attention once. Channels compound without ongoing spend. If the mechanism stops working when you stop paying or promoting, it is not a channel.

**Fix:** Test whether the distribution mechanism works without active investment. If yes, it is a channel. If not, it is a campaign.

---

### Pitfall 3: Expanding geographically before local word of mouth is understood
**Symptom:** Team translates the website, runs paid ads in the new market, and wonders why conversion is poor.

**Consequence:** Paid spend in a market where you have no local trust signals burns budget and produces low-quality leads.

**Fix:** Find organic inbound from the target market first. Talk to those users before spending anything. Understand how trust travels locally before trying to manufacture it.

---

### Pitfall 4: Treating adjacent segments as identical to the core ICP
**Symptom:** "They have the same problem, so the same messaging should work."

**Consequence:** Adjacent buyers are close enough to reach but different enough to misunderstand. They share the problem but not always the language, urgency, or buying process.

**Fix:** Run discovery with the new segment before assuming your existing onboarding and messaging transfers. Small differences in framing compound into large differences in conversion.

---

### Pitfall 5: Using this matrix as a precision instrument
**Symptom:** Team debates which quadrant they belong in for two hours.

**Consequence:** The matrix is a triage tool. Spending more time on placement than on experiments defeats the purpose.

**Fix:** Make a best-guess placement in five minutes. Use the first experiment to validate or invalidate. The matrix points you in a direction. It does not make the decision for you.

---

## References

### Related Skills
- `acquisition-channel-advisor` — Evaluate unit economics for a specific distribution channel once L4 path is chosen
- `discovery-interview-prep` — Prepare discovery interviews for new segment or geography validation
- `pol-probe` — Define a Proof of Life experiment for the recommended growth path
- `epic-hypothesis` — Frame the growth initiative as a testable hypothesis before roadmap commitment
- `jobs-to-be-done` — Identify adjacent jobs for L5 hypothesis development

### Framework Source
- McKinsey Growth Pyramid (Baghai, Coley, White — "The Alchemy of Growth," 1999)
- Levels 2 through 5 only. L1 is retention. L6 and L7 are out of scope for product team execution.

### Provenance
- Developed for Productside webinar: "Driving Organic Growth through Innovation" (May 20, 2026)
- Growth Path Matrix axes: Customer/Market Context (Known to Less Known) and Degree of Product Change (Low to High)
