---
name: problem-framing-canvas
description: "Guide PMs through MITRE's Problem Framing Canvas with structured questions across Look Inward, Look Outward, and Reframe to produce a clear, bias-resistant problem statement."
type: interactive
---


## Purpose
Guide product managers through the MITRE Problem Framing Canvas process by asking structured questions across three phases: Look Inward (examine your own assumptions and biases), Look Outward (understand who experiences the problem and who doesn't), and Reframe (synthesize insights into an actionable problem statement and "How Might We" question). Use this to ensure you're solving the right problem before jumping to solutions—avoiding confirmation bias, overlooked stakeholders, and solution-first thinking.

This is not a solution brainstorm—it's a problem framing tool that broadens perspective, challenges assumptions, and produces a clear, equity-driven problem statement.

## Key Concepts

### What is the MITRE Problem Framing Canvas?

The Problem Framing Canvas (MITRE Innovation Toolkit, v3) is a structured framework that helps teams explore a problem space comprehensively before proposing solutions. It's partitioned into **three areas**:

1. **Look Inward** — Examine your own assumptions, biases, and how you might be part of the problem
2. **Look Outward** — Understand who experiences the problem, who benefits from it, and who's been left out
3. **Reframe** — Synthesize insights into a clear, actionable problem statement and "How Might We" question

### Canvas Structure

```
┌─────────────────────────────────────────────────────────────────┐
│ LOOK INWARD                                                     │
│ - What is the problem? (symptoms)                              │
│ - Why haven't we solved it? (new, hard, low priority, etc.)   │
│ - How are we part of the problem? (assumptions, biases)       │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ LOOK OUTWARD                                                    │
│ - Who experiences the problem? When/where/consequences?        │
│ - Who else has it? Who doesn't have it?                       │
│ - Who's been left out?                                        │
│ - Who benefits when problem exists/doesn't exist?             │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ REFRAME                                                         │
│ - Stated another way, the problem is: [restatement]           │
│ - How might we [action] as we aim to [objective]?             │
└─────────────────────────────────────────────────────────────────┘
```

### Why This Works
- **Broadens perspective:** Forces you to look beyond your own assumptions
- **Equity-driven:** Centers marginalized voices and asks "who's been left out?"
- **Challenges biases:** Requires explicit examination of assumptions before framing problem
- **Actionable output:** Produces HMW statement ready for solution exploration

### Anti-Patterns (What This Is NOT)
- **Not a solution brainstorm:** Canvas frames the problem; solutions come later
- **Not a feature request list:** Focuses on underlying problems, not surface symptoms
- **Not a one-person exercise:** Requires diverse perspectives to challenge groupthink

### When to Use This
- Starting discovery for a new initiative
- Reframing an existing problem (suspect you're solving the wrong thing)
- Challenging assumptions before building solutions
- Aligning cross-functional teams on problem definition

### When NOT to Use This
- When the problem is already well-understood and validated
- For tactical bug fixes or technical debt (no deep framing needed)
- When stakeholders have already committed to a solution (address alignment first)

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

Use `template.md` for the full fill-in structure.

This interactive skill follows a **three-phase process**, asking **adaptive questions** in each phase.

---

### Step 0: Gather Context (Before Questions)

**Agent suggests:**

Before we frame your problem, let's gather context:

**Problem Context:**
- Initial problem statement or stakeholder request
- Symptoms you've observed (support tickets, churn data, user complaints)
- Existing research (user interviews, surveys, analytics)
- Assumptions you're making about the problem

**Stakeholder Context:**
- Who's affected by this problem? (users, customers, internal teams)
- Who's asking for this to be solved? (execs, sales, customers)
- Who might have been overlooked?

**You can paste this content directly, or describe the problem briefly.**

---

## Phase 1: Look Inward

**Goal:** Examine your own assumptions, biases, and how you might be part of the problem.

---

### Question 1: What is the problem? (Describe symptoms)

**Agent asks:**
"What is the problem as you currently understand it? Describe the symptoms."

**Offer 4 enumerated options:**

1. **Customer pain point** — "Customers struggle with [specific task/outcome]" (e.g., "Customers can't find features they need")
2. **Business metric problem** — "We're seeing [metric decline]" (e.g., "Churn increased 15% last quarter")
3. **Stakeholder request** — "Stakeholders say we need [feature/change]" (e.g., "Sales team says we need better reporting")
4. **Observed behavior** — "We've noticed [pattern/trend]" (e.g., "Users abandon onboarding at step 3")

**Or describe your problem/symptoms.**

**User response:** [Selection or custom]

**Agent extracts:**
- **Problem (initial framing):** [Description from user]

---

### Question 2: Why haven't we solved it?

**Agent asks:**
"Why hasn't this problem been solved yet?"

**Offer 6 enumerated options (can select multiple):**

1. **It's new** — "Problem recently emerged"
2. **It's hard** — "Technically complex or resource-intensive"
3. **It's low priority** — "Other initiatives took precedence"
4. **Lack of resources** — "Not enough budget, people, or time"
5. **Lack of authority** — "Can't make the decision or get buy-in"
6. **A systemic inequity** — "Problem disproportionately affects marginalized groups, overlooked"

**Or describe your own reason.**

**User response:** [Selection or custom]

**Agent captures:**
- **Barriers to solving:** [List of reasons]

---

### Question 3: How are we part of the problem? (Assumptions & biases)

**Agent asks:**
"How might you (or your team) be part of the problem? What assumptions or biases are you bringing?"

**Offer 4 enumerated options:**

1. **Assuming we know what customers want** — "We haven't validated with real users" (Confirmation bias)
2. **Optimizing for ourselves, not users** — "Building what's easy for us, not what's valuable for them" (Internal bias)
3. **Overlooking specific user segments** — "Focused on majority users, ignored edge cases or marginalized groups" (Survivorship bias)
4. **Solution-first thinking** — "Jumped to 'we need [feature X]' before understanding root problem" (Premature convergence)

**Or describe your specific assumptions/biases.**

**User response:** [Selection or custom]

**Agent captures:**
- **Assumptions to challenge:** [List of biases]

---

## Phase 2: Look Outward

**Goal:** Understand who experiences the problem, who benefits from it, and who's been left out.

---

### Question 4: Who experiences the problem? (When, where, consequences)

**Agent asks:**
"Who experiences this problem? When and where do they experience it? What consequences do they face?"

**Agent prompts user to describe:**
- **Who:** Specific personas, user segments, or roles
- **When:** Triggering events or contexts (e.g., "during onboarding," "at month-end close")
- **Where:** Physical or digital locations (e.g., "mobile app," "enterprise deployments")
- **Consequences:** Impact on users (e.g., "waste 2 hours/week," "miss deadlines," "churn")

**Adaptation:** Use personas from context (proto-personas, JTBD, customer research)

**User response:** [Detailed description]

**Agent captures:**
- **Who experiences it:** [Personas/segments]
- **When/where:** [Context]
- **Consequences:** [Impact]

---

### Question 5: Who else has this problem? Who doesn't have it?

**Agent asks:**
"Who else has this problem? (Colleagues, competitors, other domains?) And who doesn't have it?"

**Agent prompts:**
- **Who else has it:** Other companies, industries, or domains with similar problems
- **How do they deal with it:** Workarounds, solutions, or adaptations
- **Who doesn't have it:** Users/companies that avoid the problem (what's different about them?)

**User response:** [Detailed description]

**Agent captures:**
- **Who else has it:** [Examples]
- **Who doesn't have it:** [Counter-examples]

---

### Question 6: Who's been left out? Who benefits?

**Agent asks:**
"Who's been left out of the conversation so far? And who benefits when this problem exists or doesn't exist?"

**Agent prompts:**
- **Who's been left out:** Marginalized voices, edge cases, overlooked stakeholders
- **Who benefits when problem exists:** Who gains from the status quo?
- **Who benefits when problem doesn't exist:** Who loses if problem is solved?

**Example:**
- "Who benefits when onboarding is broken?" → "Sales team doesn't have to support complex workflows; engineering doesn't have to build guided flows"
- "Who's been left out?" → "Non-technical users, international customers (onboarding in English only)"

**User response:** [Detailed description]

**Agent captures:**
- **Who's been left out:** [List]
- **Who benefits (problem exists):** [List]
- **Who benefits (problem solved):** [List]

---

## Phase 3: Reframe

**Goal:** Synthesize insights into a clear, actionable problem statement and "How Might We" question.

---

### Question 7: Restate the problem

**Agent says:**
"Based on everything we've explored, let's restate the problem in a new way."

**Agent generates a refined problem statement** using insights from Phases 1-2:

**Template:**
"The problem is: [Who] struggles to [accomplish what] because [root cause], which leads to [consequence]. This affects [specific segments] and has been overlooked because [bias/assumption from Phase 1]."

**Example (SaaS onboarding):**
"The problem is: Non-technical small business owners struggle to activate our product during onboarding because we use jargon-heavy UI and lack guided workflows, which leads to 60% abandonment within 24 hours. This disproportionately affects solopreneurs without technical support, and has been overlooked because our team optimizes for enterprise users who have IT departments."

**Agent asks:**
"Does this restatement capture the core problem? Should we refine it?"

**User response:** [Approve or modify]

---

### Question 8: Create "How Might We" statement

**Agent says:**
"Now let's make it actionable with a 'How Might We' statement."

**Template:**
"How might we [action that addresses the problem] as we aim to [objective/desired condition]?"

**Example (SaaS onboarding):**
"How might we guide non-technical users through onboarding with plain-language prompts as we aim to increase activation from 40% to 70%?"

**Agent asks:**
"Does this HMW statement set up the right solution space? Should we adjust?"

**User response:** [Approve or modify]

---

### Output: Problem Framing Canvas + HMW Statement

After completing the flow, the agent outputs:

```markdown
# Problem Framing Canvas: [Problem Name]

**Date:** [Today's date]

---

## Phase 1: Look Inward

### What is the problem? (Symptoms)
[Description from Q1]

### Why haven't we solved it?
- [Barrier 1 from Q2]
- [Barrier 2]
- [Barrier 3]

### How are we part of the problem? (Assumptions & biases)
- [Assumption 1 from Q3]
- [Assumption 2]
- [Assumption 3]

**Which of these might be redesigned, reframed, or removed?**
[Reflection on biases to challenge]

---

## Phase 2: Look Outward

### Who experiences the problem?
**Who:** [Personas/segments from Q4]
**When/Where:** [Context]
**Consequences:** [Impact on users]
**Lived experience varies:** [How different users experience it differently]

### Who else has this problem?
**Who else:** [Examples from Q5]
**How they deal with it:** [Workarounds]

### Who doesn't have it?
[Counter-examples from Q5]

### Who's been left out?
[Marginalized voices from Q6]

### Who benefits?
**When problem exists:** [Beneficiaries of status quo]
**When problem doesn't exist:** [Who loses if solved]

---

## Phase 3: Reframe

### Stated another way, the problem is:
[Refined problem statement from Q7]

### How Might We...
**How might we** [action from Q8] **as we aim to** [objective from Q8]?

---

## Next Steps

1. **Validate with users:** Use `skills/discovery-interview-prep/SKILL.md` to test reframed problem with customers
2. **Generate solutions:** Use `skills/opportunity-solution-tree/SKILL.md` to explore solution space
3. **Create problem statement:** Use `skills/problem-statement/SKILL.md` to formalize for PRD/roadmap
4. **Identify opportunities:** Use HMW statement to brainstorm solution ideas

---

**Ready to explore solutions? Let me know if you'd like to refine the problem framing or move to solution generation.**
```

---

## Examples

See `examples/sample.md` for full problem framing examples.

Mini example excerpt:

```markdown
**Look Inward:** Churn spiked after onboarding change
**Look Outward:** New SMB users are most affected
**Reframe:** How might we reduce onboarding friction for first-time users?
```

## Common Pitfalls

### Pitfall 1: Skipping "Look Inward" (Assuming You're Neutral)
**Symptom:** Team jumps straight to "Look Outward" without examining biases

**Consequence:** Groupthink persists, assumptions unchallenged

**Fix:** Force explicit discussion of assumptions and biases (Q2-Q3)

---

### Pitfall 2: Ignoring "Who Benefits" Question
**Symptom:** Canvas completed without exploring who benefits from problem existing

**Consequence:** Miss political dynamics, resistance to change

**Fix:** Always ask "Who loses if this problem is solved?" (Q6)

---

### Pitfall 3: Generic Problem Statement
**Symptom:** Reframed problem is vague ("Improve user experience")

**Consequence:** HMW statement isn't actionable

**Fix:** Make problem specific (who, what, when, consequence, root cause)

---

### Pitfall 4: HMW Statement Is Too Narrow
**Symptom:** "How might we add a mobile app?"

**Consequence:** Constrains solution space to one idea

**Fix:** Keep HMW broad: "How might we enable mobile-first users to access core workflows on any device?"

---

### Pitfall 5: Solo Exercise (No Diverse Perspectives)
**Symptom:** PM fills out canvas alone

**Consequence:** Biases persist, marginalized voices still left out

**Fix:** Facilitate canvas workshop with cross-functional team + customer input

---

## References

### Related Skills
- `skills/problem-statement/SKILL.md` — Converts reframed problem into formal problem statement
- `skills/opportunity-solution-tree/SKILL.md` — Uses HMW statement to generate solution options
- `skills/discovery-interview-prep/SKILL.md` — Validates reframed problem with customers

### External Frameworks
- MITRE Innovation Toolkit, "Problem Framing Canvas v3" (2021) — Origin of canvas, equity-driven design thinking
- Stanford d.school, "How Might We" statements — Actionable problem framing

### Dean's Work
- [If Dean has problem framing resources, link here]

---

**Skill type:** Interactive
**Suggested filename:** `problem-framing-canvas.md`
**Suggested placement:** `/skills/interactive/`
**Dependencies:** Uses `skills/problem-statement/SKILL.md`
