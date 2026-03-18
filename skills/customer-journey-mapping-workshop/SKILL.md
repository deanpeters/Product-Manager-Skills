---
name: customer-journey-mapping-workshop
description: Run a customer journey mapping workshop with adaptive questions and outputs. Use when you need to map stages, actions, emotions, pain points, and opportunities for a persona and scenario.
intent: >-
  Guide product managers through creating a customer journey map by asking adaptive questions about the actor (persona), scenario/goal, journey phases, actions/emotions, and opportunities for improvement. Use this to visualize the end-to-end customer experience, identify pain points, and create a shared mental model across teams—avoiding surface-level feature lists and ensuring discovery work focuses on real customer problems, not assumed solutions.
type: interactive
best_for:
  - "Running a workshop to map an end-to-end customer experience"
  - "Finding pain points across a user's journey"
  - "Aligning teams on the stages, emotions, and breakdowns in an experience"
scenarios:
  - "Help me run a journey mapping workshop for new customer onboarding"
  - "Map the experience of a buyer from trial signup to first value"
  - "Facilitate a workshop on the support journey for churn-risk customers"
---


## Purpose
Guide product managers through creating a customer journey map by asking adaptive questions about the actor (persona), scenario/goal, journey phases, actions/emotions, and opportunities for improvement. Use this to visualize the end-to-end customer experience, identify pain points, and create a shared mental model across teams—avoiding surface-level feature lists and ensuring discovery work focuses on real customer problems, not assumed solutions.

## Key Concepts

### Five Key Components (NNGroup Framework)

1. **Actor** — A specific persona or user whose perspective anchors the map
2. **Scenario + Expectations** — The situational context and associated goals
3. **Journey Phases** — High-level stages organizing the experience (e.g., discover, try, buy, use, seek support)
4. **Actions, Mindsets, and Emotions** — User behaviors, thoughts, and emotional responses throughout phases
5. **Opportunities** — Insights identifying where experience can improve

### Journey Map Structure

```
Actor: [Persona Name]
Scenario: [Goal/Context]

Phase 1: Discover → Phase 2: Try → Phase 3: Buy → Phase 4: Use → Phase 5: Support
   ↓                  ↓                ↓               ↓               ↓
Actions:           Actions:         Actions:        Actions:        Actions:
Thoughts:          Thoughts:        Thoughts:       Thoughts:       Thoughts:
Emotions: 😊😐😞    Emotions:        Emotions:       Emotions:       Emotions:
   ↓                  ↓                ↓               ↓               ↓
Opportunities:     Opportunities:   Opportunities:  Opportunities:  Opportunities:
```

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

This interactive skill asks **up to 5 adaptive questions**, offering **3-4 enumerated options** at each step.

Interaction pattern: Pair with `skills/workshop-facilitation/SKILL.md` when you want a one-step-at-a-time flow with numbered recommendations at decision points and quick-select options for regular questions. If the user asks for a single-shot output, skip the multi-turn facilitation.

---

### Step 0: Gather Context (Before Questions)

**Agent suggests:**

Before we create your journey map, let's gather context:

**Customer Research:**
- User interviews, discovery notes, support tickets
- Churn reasons, exit surveys, NPS feedback
- Analytics data (drop-off points, feature usage)
- Personas or proto-personas

**Product Context:**
- Website copy, product descriptions, positioning
- Competitor journey maps or reviews (G2, Capterra)
- Existing journey documentation (if any)

**You can paste this content directly, or describe the customer experience briefly.**

---

### Question 1: Identify Actor (Persona)

**Agent asks:**
"Who is the actor for this journey map? (Which persona or user segment?)"

**Offer 4 enumerated options:**

1. **Primary persona** — "Your main target customer (e.g., 'small business owner')" (Most common starting point)
2. **Secondary persona** — "A secondary user segment with different needs (e.g., 'enterprise admin' vs. 'end user')" (Use if primary persona already mapped)
3. **High-churn persona** — "User segment with highest churn rate (e.g., 'trial users who don't convert')" (Good for retention initiatives)
4. **Newly discovered persona** — "Emerging user segment from recent research (e.g., 'remote teams' post-COVID)" (Good for market expansion)

**Or describe your specific persona.**

**Adaptation:** Use personas from context (proto-personas, JTBD research, etc.)

**User response:** [Selection or custom]

---

### Question 2: Define Scenario + Goal

**Agent asks:**
"What's the scenario and goal for this journey? (What is the actor trying to accomplish?)"

**Offer 4 enumerated options:**

1. **First-time use** — "New user onboarding, from discovery to activation" (Common for SaaS, apps)
2. **Core workflow** — "Recurring task the user does regularly (e.g., 'create invoice,' 'run report')" (Common for established products)
3. **Problem resolution** — "User encounters issue and seeks help (e.g., 'forgot password,' 'billing question')" (Good for support/retention)
4. **Upgrade/expansion** — "Free user considering paid plan, or existing customer expanding usage" (Good for growth initiatives)

**Or describe your specific scenario.**

**User response:** [Selection or custom]

**Agent extracts:**
- **Actor:** [Persona from Q1]
- **Scenario:** [Context from Q2]
- **Goal:** [What actor is trying to accomplish]

---

### Question 3: Identify Journey Phases

**Agent says:**
"Let's break the journey into high-level phases (typically 4-6 phases from start to end)."

**Agent generates 4-6 journey phases** based on scenario (Q2).

**Example (if Scenario = "First-time use"):**

```
Journey Phases (left to right):

1. Discover — User learns about product
2. Evaluate — User researches, compares alternatives
3. Try — User signs up, starts onboarding
4. Activate — User reaches "aha moment," experiences value
5. Use — User integrates product into workflow
6. Expand — User considers upgrading or inviting team
```

**Agent asks:**
"Do these phases capture the full journey? Should we add, remove, or rename phases?"

**User response:** [Approve or modify]

---

### Question 4: Map Actions, Thoughts, Emotions per Phase

**Agent says:**
"Now let's map what the actor does, thinks, and feels in each phase."

**Agent generates 3-5 actions, thoughts, and emotions per phase** based on context (Step 0) and scenario (Q2).

**Example (for Phase 3: "Try — User signs up, starts onboarding"):**

```
Phase 3: Try (Onboarding)

Actions:
- Signs up with email
- Receives welcome email
- Logs in for the first time
- Sees empty dashboard
- Searches for "getting started" guide

Thoughts:
- "This looks promising, but I'm not sure where to start"
- "Do I need to watch a tutorial video?"
- "What's the first step?"

Emotions:
- Curious but uncertain 🤔
- Slightly frustrated (no clear next step) 😕
- Hopeful it will get easier 🙂

Pain Points:
- No onboarding checklist or guided tour
- Empty state doesn't suggest next action
- Too many options in navigation (overwhelming)
```

**Agent repeats for all journey phases**, showing full map.

**Agent asks:**
"Does this capture the customer experience accurately? Should we adjust actions, thoughts, or emotions?"

**User response:** [Approve or modify]

---

### Question 5: Identify Opportunities (Pain Points to Address)

**Agent says:**
"Based on the journey map, let's identify opportunities for improvement—ranked by impact."

**Agent generates 5-7 opportunities** (pain points with highest emotional intensity or drop-off rates).

**Example:**

```
# Opportunities (Ranked by Impact)

## 1. Onboarding lacks guided first steps (Phase 3: Try)
**Pain Point:** Users see empty dashboard, don't know what to do first
**Evidence:** 60% of signups don't complete first action within 24 hours
**Opportunity:** Add interactive onboarding checklist ("Create your first project," "Invite a teammate")
**Impact:** HIGH — Directly affects activation rate

---

## 2. Pricing page is confusing (Phase 2: Evaluate)
**Pain Point:** Users don't understand which plan fits their needs
**Evidence:** High bounce rate on pricing page (70% leave without signing up)
**Opportunity:** Add plan comparison tool or "Which plan is right for me?" quiz
**Impact:** HIGH — Directly affects trial conversion

---

## 3. Support is hard to find (Phase 5: Use)
**Pain Point:** Users encounter issues, struggle to find help
**Evidence:** Support tickets often say "I couldn't find an answer in docs"
**Opportunity:** Add in-app help widget, contextual tooltips
**Impact:** MEDIUM — Affects retention, but fewer users hit this phase

---

## 4. Email confirmations lack context (Phase 1: Discover)
**Pain Point:** Marketing emails don't explain value clearly
**Evidence:** Low click-through rate on email campaigns (5% vs. industry avg 15%)
**Opportunity:** Rewrite emails with customer language, clear CTAs
**Impact:** MEDIUM — Affects top-of-funnel awareness

---

## 5. Upgrade prompts feel pushy (Phase 6: Expand)
**Pain Point:** Users perceive upgrade prompts as sales-y, not helpful
**Evidence:** Negative sentiment in NPS comments ("too many upgrade popups")
**Opportunity:** Show upgrade value contextually (when user hits free plan limit)
**Impact:** LOW — Affects smaller user subset
```

**Agent asks:**
"Do these opportunities align with your priorities? Which should we focus on first?"

**User response:** [Selection or custom]

---

### Output: Customer Journey Map + Opportunity List

After completing the flow, the agent outputs:

```markdown
# Customer Journey Map: [Scenario from Q2]

**Actor:** [Persona from Q1]
**Scenario:** [Context from Q2]
**Goal:** [What actor is trying to accomplish]
**Date:** [Today's date]

---

## Journey Phases

[Phase 1] → [Phase 2] → [Phase 3] → [Phase 4] → [Phase 5] → [Phase 6]

---

## Full Journey Map

### Phase 1: [Name]

**Actions:**
- [Action 1]
- [Action 2]
- [Action 3]

**Thoughts:**
- "[Quote 1]"
- "[Quote 2]"

**Emotions:**
- [Emotion 1] 😊
- [Emotion 2] 😐

**Pain Points:**
- [Pain point 1]
- [Pain point 2]

---

### Phase 2: [Name]

[...repeat structure for all phases...]

---

## Opportunities (Prioritized)

### Opportunity 1: [Name] (HIGH IMPACT)
**Phase:** [Journey phase]
**Pain Point:** [Description]
**Evidence:** [Data/research]
**Proposed Solution:** [How to address]
**Impact:** HIGH — [Rationale]

---

### Opportunity 2: [Name] (HIGH IMPACT)
**Phase:** [Journey phase]
**Pain Point:** [Description]
**Evidence:** [Data/research]
**Proposed Solution:** [How to address]
**Impact:** HIGH — [Rationale]

---

[...continue for all opportunities...]

---

## Next Steps

1. **Validate opportunities:** Use `discovery-interview-prep.md` to test hypotheses with customers
2. **Prioritize fixes:** Use `prioritization-advisor.md` to choose which opportunities to tackle first
3. **Create problem statements:** Use `problem-statement.md` to frame top opportunities
4. **Build experiments:** Use `opportunity-solution-tree.md` to design solutions and POCs

---

**Ready to start addressing opportunities? Let me know if you'd like to refine the map or dive into a specific pain point.**
```

---

## Examples

### Example 1: Good Journey Map (SaaS Onboarding)

**Q1 Response:** "Primary persona — Small business owner"

**Q2 Response:** "First-time use — New user onboarding, from discovery to activation"

**Q3 - Phases Generated:**
```
Discover → Evaluate → Try → Activate → Use → Expand
```

**Q4 - Phase 3 (Try) Mapped:**

```
Actions:
- Signs up via Google SSO
- Receives welcome email
- Logs in, sees empty dashboard
- Clicks "Help" button, watches 5-min tutorial
- Attempts to create first project, gets stuck on form

Thoughts:
- "This looks easy enough"
- "Wait, what's a 'workspace' vs. 'project'?"
- "Do I need to fill out all these fields?"

Emotions:
- Excited initially 😊
- Confused by terminology 😕
- Frustrated by unclear form 😞

Pain Points:
- No guided onboarding checklist
- Terminology not explained (workspace vs. project)
- Form has too many required fields upfront
```

**Q5 - Opportunities Identified:**
1. Add onboarding checklist (HIGH — affects activation)
2. Simplify terminology (MEDIUM — affects understanding)
3. Reduce required form fields (MEDIUM — affects completion rate)

---

### Example 2: Bad Journey Map (Too Generic)

**Phase: "Use Product"**

**Actions:**
- Uses product
- Does tasks

**Thoughts:**
- "This is good"

**Emotions:**
- Happy 😊

**Fix:** Get specific ("User creates invoice → sends to client → tracks payment status"), include real customer quotes, and show emotional highs AND lows.

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Mapping Internal Process | Phases = "Lead generated → Qualified → Demo → Closed" | Map from customer POV: "Discovers → Researches → Tries → Adopts" |
| No Emotions or Pain Points | Journey lists actions only | Add customer quotes, emotional states (frustrated, delighted, confused) |
| Too Many Personas | Trying to map "all users" in one journey | One map per persona. Create separate maps for each |
| Opportunities Not Prioritized | 20 opportunities with no ranking | Rank by impact (HIGH/MEDIUM/LOW) based on evidence and emotional intensity |
| Map Created in Isolation | PM creates journey map alone | Facilitate workshop with cross-functional team |

---

## References

### Related Skills
- `customer-journey-map.md` — Component skill with journey map template
- `proto-persona.md` — Defines actor for journey mapping
- `problem-statement.md` — Converts opportunities into problem statements
- `discovery-interview-prep.md` — Gathers research input for mapping
- `opportunity-solution-tree.md` — Designs solutions for journey opportunities

### External Frameworks
- Nielsen Norman Group, "Journey Mapping 101" (2016) — Definitive guide to journey mapping
- Adaptive Path, "Guide to Experience Mapping" (2013) — Experience vs. journey maps

### Dean's Work
- [If Dean has journey mapping resources, link here]

