---
name: problem-statement
description: Write a user-centered problem statement with who is blocked, what they are trying to do, why it matters, and how it feels. Use when framing discovery, prioritization, or a PRD.
intent: >-
  Articulate a problem from the user's perspective using an empathy-driven framework that captures who they are, what they're trying to do, what's blocking them, why, and how it makes them feel. Use this to align stakeholders on the problem before jumping to solutions, and to frame product work around user outcomes rather than feature requests.
type: component
---


## Purpose
Articulate a problem from the user's perspective using an empathy-driven framework that captures who they are, what they're trying to do, what's blocking them, why, and how it makes them feel. Use this to align stakeholders on the problem before jumping to solutions, and to frame product work around user outcomes rather than feature requests.

## Key Concepts

### The Problem Framing Framework
Based on Jobs-to-be-Done and empathy mapping, the framework structures problems as:

**Problem Framing Narrative:**
- **I am:** [Describe the persona experiencing the problem]
- **Trying to:** [Desired outcomes the persona cares about]
- **But:** [Barriers preventing the outcomes]
- **Because:** [Root cause of the problem]
- **Which makes me feel:** [Emotional impact]

**Context & Constraints:**
- [Geographic, technological, time-based, demographic factors]

**Final Problem Statement:**
- [Single, concise, empathetic summary]

### Anti-Patterns (What This Is NOT)
- **Not a solution in disguise:** "The problem is we lack AI-powered analytics" = sneaking in a solution
- **Not a business problem:** "Our revenue is down" isn't a user problem (it's a symptom)
- **Not a feature request:** "Users need a dashboard" isn't a problem (what are they trying to do?)
- **Not generic:** "Users want better UX" is too vague to be actionable

---

## Application

Use `template.md` for the full fill-in structure.

### Step 1: Gather User Context
Before drafting, ensure you have:
- **User interviews or research:** Direct quotes, observed behaviors, pain points
- **Jobs-to-be-Done insights:** What users are "hiring" your product to do (reference `skills/jobs-to-be-done/SKILL.md`)
- **Persona clarity:** Who specifically experiences this problem (reference `skills/proto-persona/SKILL.md`)
- **Constraints data:** Geographic, tech, time, demographic limitations

**If missing context:** Run discovery interviews, contextual inquiries, or user shadowing. Don't fabricate problems.

---

### Step 2: Draft the Problem Framing Narrative

Fill in the template from the persona's point of view:

```markdown
## Problem Framing Narrative

**I am:** [Describe the key persona, highlighting 3-4 key characteristics]
- [Key pain point or characteristic 1]
- [Key pain point or characteristic 2]
- [Key pain point or characteristic 3]

**Trying to:**
- [Single sentence listing the desired outcomes the persona cares most about]

**But:**
- [Describe the barriers preventing the persona from achieving outcomes]
- [Job-to-be-done or outcome obstruction 1]
- [Job-to-be-done or outcome obstruction 2]
- [Job-to-be-done or outcome obstruction 3]

**Because:**
- [Describe the root cause empathetically]

**Which makes me feel:**
- [Describe the emotions from the persona's perspective]
```

**Quality checks:**
- **"I am" specificity:** Can you picture this person? Or is it generic ("busy professionals")?
- **"Trying to" clarity:** Is this an outcome (measurable) or a task (activity)?
- **"But" depth:** Are these real barriers or just inconveniences?
- **"Because" honesty:** Is this the root cause or just a symptom?
- **"Makes me feel" authenticity:** Do these emotions come from research or assumptions?

---

### Step 3: Document Context & Constraints

```markdown
## Context & Constraints

- [Enumerate geographic, technological, time-based, or demographic factors]
- [e.g., "Must work offline in rural areas with limited connectivity"]
- [e.g., "Used by non-technical users unfamiliar with complex software"]
- [e.g., "Time-sensitive: decisions must be made within 24 hours"]
```

**Quality checks:**
- **Relevance:** Do these constraints directly impact the problem?
- **Specificity:** Are they concrete enough to inform design decisions?

---

### Step 4: Craft the Final Problem Statement

Synthesize the narrative into one powerful sentence:

```markdown
## Final Problem Statement

[Single, concise statement that provides a powerful and empathetic summary]
```

**Formula:** `[Persona] needs a way to [desired outcome] because [root cause], which currently [emotional/practical impact].`

**Example:** "Enterprise IT admins need a way to provision user accounts in under 5 minutes because current processes take 2+ hours with manual approvals, which causes project delays and frustrated end-users."

**Quality checks:**
- **One sentence:** If it requires multiple sentences, the problem isn't crisp yet
- **Measurable:** Can you tell if you've solved it?
- **Empathetic:** Does it resonate emotionally?
- **Shareable:** Could you say this in a meeting and have stakeholders nod?

---

### Step 5: Validate and Socialize

- **Test with users:** Read it aloud to people who experience the problem. Do they say "Yes, exactly!"?
- **Share with stakeholders:** Product, engineering, design, exec. Does it align everyone?
- **Iterate based on feedback:** If anyone says "I don't think that's the real problem," dig deeper.

---

## Examples

See `examples/sample.md` for full examples (good and bad problem statements).

Mini example excerpt:

```markdown
**I am:** A software developer on a distributed team
**Trying to:** Communicate in real-time with my team without losing context
**But:** Email is too slow and IM is ephemeral
**Because:** No tool combines real-time chat with searchable history
**Which makes me feel:** Frustrated and disconnected
```

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Solution smuggling | "The problem is we don't have [specific feature]" | Reframe around the user's desired outcome. Ask "What are they trying to achieve?" |
| Business problem disguised as user problem | "Users want to increase our revenue" or "The problem is our churn rate" | Dig into *why* users churn. Frame from their perspective, not your metrics. |
| Generic personas | "I am a busy professional trying to be more productive" | Get specific: "I am a sales rep managing 50+ leads in spreadsheets" |
| Symptom instead of root cause | "Because the UI is confusing" | Keep asking "why" until you hit root cause (e.g., "users have no mental model for how the system works") |
| Fabricated emotions | "Which makes me feel empowered and delighted" | Use actual quotes from user interviews. Real emotions: "frustrated," "overwhelmed," "stuck" |

---

## References

### Related Skills
- `skills/jobs-to-be-done/SKILL.md` — Informs the "Trying to" and "But" sections
- `skills/proto-persona/SKILL.md` — Defines the "I am" persona
- `skills/positioning-statement/SKILL.md` — Problem statement informs positioning
- `skills/user-story/SKILL.md` — Problem statement guides story prioritization

### External Frameworks
- Clayton Christensen, *Jobs to Be Done* — Origin of outcome-focused problem framing
- Osterwalder & Pigneur, *Value Proposition Canvas* — Customer pains/gains/jobs
- Dave Gray, *Empathy Mapping* — Emotional framing techniques

### Dean's Work
- [Link to relevant Dean Peters' Substack articles if applicable]

### Provenance
- Adapted from `prompts/framing-the-problem-statement.md` in the `https://github.com/deanpeters/product-manager-prompts` repo.

---

**Skill type:** Component
**Suggested filename:** `problem-statement.md`
**Suggested placement:** `/skills/components/`
**Dependencies:** References `skills/jobs-to-be-done/SKILL.md`, `skills/proto-persona/SKILL.md`
