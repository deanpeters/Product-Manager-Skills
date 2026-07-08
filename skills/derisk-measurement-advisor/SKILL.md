---
name: derisk-measurement-advisor
description: Identify what to measure, test, or track to de-risk a product or AI idea. Use when stress-testing an idea across internal (DUFV) and external (PESTEL) dimensions.
compatibility: opencode
argument-hint: "[product or AI idea]"
metadata:
  best_for:
    - "Stress-testing an AI or product idea before putting it on the roadmap"
    - "Identifying the cheapest tests to run before committing teams and budget"
    - "Scanning for external forces that could blindside your product plans"
    - "Building a risk register with clear act-now vs. watch-and-track priorities"
  estimated_time: "15-20 min"
  intent: >-
    Guide product managers through a structured risk scan across **10 dimensions** — 4 internal
    (Desirability, Usability, Feasibility, Viability) and 6 external (Political, Economic, Social,
    Technological, Environmental, Legal) — to identify the most important things to measure, test,
    or track before committing to a product or AI idea. Each surfaced risk gets triaged into
    **act on immediately** or **start tracking**, producing a prioritized risk register with
    concrete next steps.
  scenarios:
    - "I have an AI product idea. What should I measure before we commit?"
    - "Help me figure out what risks to act on now vs. track over time"
    - "We're about to put this on the roadmap. What could go wrong internally and externally?"
    - "Is this idea worth the squeeze? What should we test first?"
  type: interactive
---

## Purpose

Guide product managers through identifying the most important things to measure, test, or track across 10 risk dimensions — 4 internal and 6 external — then triage each into **act on immediately** or **start tracking**. The output is a prioritized risk register that tells you what to do first, not just what could go wrong.

This is not a generic risk list. It's a guided scan tied to *your* specific product, customer, and market context. The question it answers: **is the orange worth the squeeze?**

## Input

**Works best with:** The product or AI idea you want to stress-test.
**Also useful:** Its stage (concept, prototype, in-market), what you've already validated, and any dimensions you already know are risky.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** The advisor opens by asking for the idea in a sentence or two, then scans the 10 risk dimensions against it.

**Example invocation:** `De-risk this: an AI agent that auto-drafts insurance claim responses for adjusters — prototype stage, no compliance review yet.`

## Key Concepts

### Two Lenses, One Question

Every product idea carries two kinds of risk. Most PMs check one and ignore the other.

**Internal risks** ask whether the product itself will work:
- **Product Outcome Metrics** (Desirability + Usability) = "What's in it for the customer/user?"
- **Business Outcome Metrics** (Feasibility + Viability) = "What's in it for our business/organization?"

**External risks** ask whether the world will let it work:
- **PESTEL forces** (Political, Economic, Social, Technological, Environmental, Legal) = "What could blindside us?"

The single triage question that applies to both sides: **Do I act on this now, or start tracking it?**

---

### The Internal Risk Framework (DUFV)

Adapted from Marty Cagan's four product risks, split into two measurement categories:

| Category | Dimension | Core Question |
|----------|-----------|---------------|
| **Product Outcome Metrics** | Desirability | Will customers value it enough to buy it? |
| **Product Outcome Metrics** | Usability | Will customers figure out how to use it? |
| **Business Outcome Metrics** | Feasibility | Can we build it? Can we sustain it at scale? |
| **Business Outcome Metrics** | Viability | Will it work as a viable business? |

**Product Outcome Metrics** answer: *What's in it for the customer/user?* They measure whether the product is solving meaningful problems and delivering value to its intended users.

**Business Outcome Metrics** answer: *What's in it for our business/organization?* They measure how effectively and reliably the product supports a seamless customer experience while remaining feasible to deliver.

The connection to positioning: Product Outcome Metrics validate your **Problem Positioning Statement** (the customer promise). Business Outcome Metrics validate your **Problem Framing Statement** (the business case).

---

### The External Risk Framework (PESTEL)

Six categories of forces outside your organization that can reshape, delay, or kill your product plans:

| Category | What It Covers | Example Risk |
|----------|---------------|--------------|
| **Political** | Government policies, trade regulations, political priorities | New AI safety rules for state contractors |
| **Economic** | Market conditions, funding, inequality, supply chains | VC AI funding dries up — focus shifts to profitability |
| **Social** | Demographics, sentiment, digital literacy, cultural shifts | AI accused of bias — can you prove fairness? |
| **Technological** | Platform dependencies, standards, competing tech | New AI model outdates yours — time for rapid innovation? |
| **Environmental** | Energy consumption, sustainability, carbon footprint | AI criticized for carbon footprint — how to go green? |
| **Legal** | Data privacy, compliance, IP, evolving regulations | AI deepfakes lawsuit crossfire — can you protect your product? |

**Key insight from the classroom:** Market conditions don't just change — they potentially change us, our business, and our products. PESTEL helps PMs categorize and respond to that change, not just observe it.

---

### The Act/Watch Triage

Every surfaced risk gets one of two labels:

- **Act on immediately:** This risk is present, material, and requires a response now — run a test, change a plan, mitigate a gap.
- **Start tracking:** This risk is real but not yet urgent — monitor it, set a trigger threshold, revisit on a cadence.

The triage applies equally to internal and external risks. A desirability gap you can't answer is an "act now" just as much as a regulatory deadline. A demographic trend you see coming is a "watch" just like a feasibility concern you've already partially mitigated.

**Anti-pattern:** Labeling everything "act now." If every risk is urgent, none of them are prioritized. Force yourself to split roughly 40/60 act/watch.

---

### When to Use This Skill

**Use this when:**
- You have a product or AI idea and need to decide whether to commit
- You're about to put something on the roadmap and want a structured risk check
- You've been focused on internal risks and haven't scanned external forces (or vice versa)
- Leadership asks "what could go wrong?" and you want a better answer than "nothing, we're good"

**Don't use this when:**
- You don't have a specific product idea yet (use `problem-framing-canvas` first)
- You need a deep PESTEL analysis with data and citations (use `pestel-analysis` component skill)
- You've already validated the idea and need to pick a validation method (use `pol-probe-advisor`)
- The idea is already in production and you're optimizing, not de-risking

---

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the default interaction protocol for this skill.

It defines:
- session heads-up + entry mode (Guided, Context dump, Best guess)
- one-question turns with plain-language prompts
- progress labels (for example, Context Qx/4 and Risk Scan Qx/6)
- interruption handling and pause/resume behavior
- numbered recommendations at decision points
- quick-select numbered response options for regular questions (include `Other (specify)` when useful)

This file defines the domain-specific assessment content. If there is a conflict, follow this file's domain logic.

## Application

This interactive skill uses **adaptive questioning** to scan your product idea across 10 risk dimensions (4 internal + 6 external), triage each surfaced risk into act/watch, and produce a prioritized risk register.

---

### Session Start: Heads-Up + Entry Mode (Mandatory)

**Agent opening prompt:**

"Quick heads-up before we start: this usually takes about 15-20 minutes. We'll cover 4 context questions, then scan 10 risk dimensions — 4 internal (will customers want it, can they use it, can we build it, does the business work) and 6 external (political, economic, social, technological, environmental, legal). For each risk that surfaces, we'll triage it: act now or track.

How do you want to do this?
1. **Guided mode:** I'll walk through each dimension one at a time.
2. **Context dump:** Paste what you know about the idea and I'll skip what's covered.
3. **Best guess mode:** Give me the idea in a sentence and I'll make reasonable assumptions, labeled."

---

### Step 0: Gather Context

**Agent asks the following questions, one per turn:**

**Context Q1/4:** "What's the product or AI idea you're evaluating? Describe it in 1-2 sentences — what it does and who it's for."

**Context Q2/4:** "What stage is this idea at?"
1. Concept — we're still exploring whether to pursue it
2. Prototype — we have something testable but uncommitted
3. Building — we've committed and are developing it
4. Scaling — it's live and we're growing it

**Context Q3/4:** "What's your primary concern right now?"
1. Will anyone actually want this? (demand/desirability risk)
2. Can users figure out how to use it? (usability risk)
3. Can we actually build and sustain this? (technical/feasibility risk)
4. Will this work as a business? (viability/business model risk)
5. Something external could disrupt our plans (regulatory, market, competitive)

**Context Q4/4:** "Who is the customer — the person who would use or buy this product? Give me a job title or role, not a company name."

**After Q4, agent summarizes:**

"Here's what I'm working with:
- **Idea:** [summary]
- **Stage:** [stage]
- **Primary concern:** [concern]
- **Customer:** [role]

Let's scan for risks. We'll start with internal risks (Product Outcome Metrics and Business Outcome Metrics), then move to external forces (PESTEL)."

---

### Step 1: Internal Risk Scan — Product Outcome Metrics (Desirability + Usability)

**Agent introduces:**

"First, let's check **Product Outcome Metrics** — what's in it for the customer? These measure whether the product will be valuable and usable for your customer. I'll present tests and metrics for two dimensions. For each, tell me which 2 are most critical for *your* product."

---

**Risk Scan Q1/10 — Desirability:** "Which of these tests or metrics matter most for validating that [customer role] will actually want [product idea]? Pick 2."

1. Use landing pages to gauge initial interest
2. Test engagement with explainer videos or ads
3. Analyze signup rates from ad campaigns
4. Observe feedback from storyboard demos
5. Measure session times during user interactions
6. Track feature adoption rates over time
7. Other (describe your own)

**For each selection, agent asks:** "Is this something you need to **act on immediately** (run the test, close the gap) or **start tracking** (monitor over time)?"

---

**Risk Scan Q2/10 — Usability:** "Which of these matter most for validating that [customer role] can actually use [product idea] without friction? Pick 2."

1. Watch how users interact with wireframes
2. Use Wizard of Oz tests for usability insights
3. Observe clarity issues from paper model feedback
4. Track rage clicks to identify frustration points
5. Measure drop-offs in task completion workflows
6. Analyze time-to-complete tasks for friction points
7. Other (describe your own)

**For each selection, agent asks:** "Act on immediately or start tracking?"

---

### Step 2: Internal Risk Scan — Business Outcome Metrics (Feasibility + Viability)

**Agent introduces:**

"Now let's check **Business Outcome Metrics** — what's in it for our business? These measure whether the business and technology can support this product."

---

**Risk Scan Q3/10 — Feasibility:** "Which of these matter most for confirming you can actually build and sustain [product idea]? Pick 2."

1. Measure system uptime and stability
2. Simulate user loads to ensure scalability
3. Track resource use and efficiency during testing
4. Monitor failure rates across environments
5. Evaluate costs via analogous systems
6. Test integration readiness with critical dependencies
7. Other (describe your own)

**For each selection, agent asks:** "Act on immediately or start tracking?"

---

**Risk Scan Q4/10 — Viability:** "Which of these matter most for confirming [product idea] will work as a business? Pick 2."

1. Examine analogous data from similar products
2. Analyze adjacent products for comparable insights
3. Estimate break-even points using simulation models
4. Test price sensitivity through customer research
5. Assess scalability of revenue vs. cost structures
6. Run trend analysis to evaluate long-term market potential
7. Other (describe your own)

**For each selection, agent asks:** "Act on immediately or start tracking?"

---

### Step 3: External Risk Scan — PESTEL

**Agent introduces:**

"Now let's scan for **external forces** — things outside your organization that could reshape, delay, or kill your plans. I'll walk through 6 categories. For each, I'll suggest risks relevant to your product and industry. Tell me which ones matter, and whether to act or watch."

---

**Risk Scan Q5/10 — Political:** "Given [product idea] and [customer role], which political forces could affect your plans?"

Starter prompts (agent adapts to context):
- Regulatory compliance requirements (existing or pending)
- Changing political priorities that affect your industry
- Regional policy mandates or jurisdictional differences
- Export restrictions or trade policy shifts

"Which of these (or others) are relevant? For each, act on immediately or start tracking?"

---

**Risk Scan Q6/10 — Economic:** "What economic forces could affect [product idea]?"

Starter prompts:
- Economic inequality affecting your customer segment's budget
- Supply chain disruptions impacting delivery or cost
- Funding environment changes (VC, enterprise budgets)
- Skills shortages in your hiring market

"Which are relevant? Act or watch?"

---

**Risk Scan Q7/10 — Social:** "What social or cultural shifts could affect adoption of [product idea]?"

Starter prompts:
- Shifting social sentiment toward AI or your product category
- Digital literacy gaps in your target customer population
- Demographic shifts in your target market
- Urbanization or remote-work trends affecting how customers work

"Which are relevant? Act or watch?"

---

**Risk Scan Q8/10 — Technological:** "What technology shifts could affect [product idea]?"

Starter prompts:
- Platform dependencies (APIs, cloud providers, AI model providers)
- Evolving industry standards that your product must meet
- Competing technology that could leapfrog your approach
- Spectrum allocations or infrastructure changes (if applicable)

"Which are relevant? Act or watch?"

---

**Risk Scan Q9/10 — Environmental:** "What environmental factors could affect [product idea]?"

Starter prompts:
- Energy consumption concerns (especially for AI/compute-heavy products)
- Sustainability requirements from customers or regulators
- Carbon footprint scrutiny from public or investors
- Resource scarcity affecting infrastructure or supply

"Which are relevant? For many products this category has low impact — if so, say 'minimal' and we'll move on. Act or watch for anything relevant?"

---

**Risk Scan Q10/10 — Legal:** "What legal risks could affect [product idea]?"

Starter prompts:
- Data privacy regulations (GDPR, state privacy laws, sector-specific rules)
- AI-specific liability or transparency requirements
- IP protection challenges (patents, trade secrets, open-source licensing)
- Employment or contractor classification laws (if product affects work)

"Which are relevant? Act or watch?"

---

### Step 4: Synthesize — Risk Register

**Agent compiles all selections into a risk register:**

"Here's your de-risking plan for [product idea]:

### Act on Immediately

| # | Dimension | Risk / Test | Recommended First Step |
|---|-----------|-------------|----------------------|
| 1 | [e.g., Desirability] | [e.g., Gauge initial interest via landing page] | [e.g., Launch a 1-week landing page test with email capture] |
| 2 | [e.g., Legal] | [e.g., Data privacy compliance for EU customers] | [e.g., Map GDPR requirements to your data architecture this week] |
| ... | | | |

### Start Tracking

| # | Dimension | Risk / Signal | What to Watch | Review Cadence |
|---|-----------|--------------|---------------|----------------|
| 1 | [e.g., Economic] | [e.g., VC funding contraction in AI] | [e.g., Quarterly VC reports, competitor funding rounds] | Quarterly |
| 2 | [e.g., Social] | [e.g., Shifting sentiment toward AI in healthcare] | [e.g., Industry surveys, media sentiment, customer interviews] | Monthly |
| ... | | | | |

### Summary

- **Total risks surfaced:** [N]
- **Act on immediately:** [N] — these are your next steps before committing further
- **Start tracking:** [N] — set calendar reminders for these review cadences
- **Biggest gap:** [the dimension with the most unresolved act-now items]"

**Agent then offers:**

"What would you like to do next?
1. **Dig deeper on an act-now item** — I'll help you design the specific test or measurement
2. **Run a full PESTEL analysis** — use the `pestel-analysis` skill for a deep external-forces dive
3. **Pick a validation method** — use the `pol-probe-advisor` to choose the cheapest test for your top risk
4. **Export this register** — I'll format it as a Markdown document you can share with your team"

---

## Examples

### Example: AI-Powered Clinical Trial Matching Tool

**Context:**
- **Idea:** AI tool that matches patients to clinical trials based on EHR data
- **Stage:** Concept
- **Primary concern:** External regulatory risk
- **Customer:** Clinical operations lead

**Internal Risk Scan Results:**

*Product Outcome Metrics:*
- Desirability: Observe feedback from storyboard demos (ACT) + Track feature adoption rates (WATCH)
- Usability: Measure drop-offs in task completion workflows (WATCH) + Analyze time-to-complete for friction (WATCH)

*Business Outcome Metrics:*
- Feasibility: Test integration readiness with EHR dependencies (ACT) + Monitor failure rates across environments (WATCH)
- Viability: Examine analogous data from similar products (ACT) + Assess scalability of revenue vs. cost (WATCH)

**External Risk Scan Results:**
- Political: FDA digital health guidance evolving (WATCH — quarterly)
- Economic: Hospital IT budget pressure post-pandemic (ACT — validate willingness to pay now)
- Social: Clinician trust in AI-driven patient matching (ACT — run trust interviews)
- Technological: EHR platform API stability and access policies (ACT — test integration this sprint)
- Environmental: Minimal impact
- Legal: HIPAA compliance for AI processing of PHI (ACT — legal review before prototype)

**Risk Register Output:**

Act on immediately (5 items):
1. Desirability — storyboard demos with 5 clinical ops leads
2. Feasibility — EHR integration spike (test API access and data format)
3. Viability — analogous product benchmarking (what do similar tools charge?)
4. Economic — validate budget authority with 3 hospital IT buyers
5. Legal — HIPAA compliance review for AI processing of PHI

Start tracking (5 items):
1. Desirability — feature adoption rates (post-launch metric)
2. Usability — task completion drop-offs and time-to-complete (post-prototype)
3. Feasibility — failure rates across environments (post-build)
4. Viability — revenue vs. cost scalability (post-pilot)
5. Political — FDA digital health guidance (quarterly review)

**Biggest gap:** Legal/compliance — HIPAA review must happen before any prototype touches real patient data.

---

## Common Pitfalls

### 1. Generic Risk Lists
**Failure Mode:** "Desirability is a risk. Feasibility is a risk. Regulation is a risk." No specifics, no connection to the actual product.

**Consequence:** Risk register that applies to every product — and therefore helps none.

**Fix:** Every risk must name the specific test or signal *for this product and this customer*. "Gauge initial interest" is generic. "Run a 1-week landing page targeting clinical ops leads with EHR integration messaging" is specific.

---

### 2. All Act, No Watch
**Failure Mode:** Every risk is labeled "act on immediately" because everything feels urgent when you're looking at it.

**Consequence:** No prioritization. Team tries to address 15 risks simultaneously and makes progress on none.

**Fix:** Force a split. If you have 10 risks, no more than 4-5 should be "act now." The rest are real risks — they just aren't today's problem. Set a review cadence and move on.

---

### 3. Internal-Only or External-Only
**Failure Mode:** PM runs a thorough DUFV scan but never checks PESTEL (or vice versa). "We validated demand and feasibility — ship it!" Then a regulation kills the product 6 months later.

**Consequence:** Blind spots in exactly the dimensions you didn't scan.

**Fix:** This skill exists precisely to prevent this. Both lenses, every time. If an external category has low impact (common for Environmental in SaaS), say "minimal" and move on — but don't skip the question.

---

### 4. Analysis Without Next Steps
**Failure Mode:** Beautiful risk register, no recommended first step. Sits in a Google Doc. Nobody acts on it.

**Consequence:** Risk theater — the appearance of diligence without the substance.

**Fix:** Every "act now" item must have a concrete next step: who does what, by when, and how you'll know the risk is addressed. "Run a test" is not a next step. "Launch a 1-week landing page with email capture targeting [customer role], measure signup rate, and decide go/no-go by [date]" is.

---

## References

### Related Skills
- **[pestel-analysis](../pestel-analysis/SKILL.md)** (Component) — Deep-dive PESTEL template with data-driven analysis across all 6 categories; use after this skill surfaces external risks worth investigating further
- **[pol-probe-advisor](../pol-probe-advisor/SKILL.md)** (Interactive) — Choose the cheapest validation method for your highest-priority act-now risk
- **[pol-probe](../pol-probe/SKILL.md)** (Component) — Document a Proof of Life probe for a specific risk
- **[recommendation-canvas](../recommendation-canvas/SKILL.md)** (Component) — Structure a go/no-go recommendation using risk register findings
- **[problem-framing-canvas](../problem-framing-canvas/SKILL.md)** (Interactive) — Frame the problem before scanning for risks

### External Frameworks
- **Marty Cagan** — *Inspired* (2018): The four product risks (Value, Usability, Feasibility, Viability) as the foundation for product discovery
- **Francis Joseph Aguilar** — *Scanning the Business Environment* (1967): Origin of PEST analysis, extended to PESTEL

### Dean's Work
- Productside AI Product Management course, Unit 07: "De-Risking Your AI Bets — Unpacking Unknowns and Assumptions"
- PESTel Risk Planning activity (external risks with act/watch triage)
- Measuring What Matters activity (internal risks with DUFV quadrant selection)
