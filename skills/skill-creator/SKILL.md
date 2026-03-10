---
name: skill-creator
description: Design a new PM skill through guided conversation. Use when you have raw content or an idea and want to shape it into a compliant skill.
intent: >-
  Walk through the full skill design process interactively — from raw idea or content to a structured, repo-compliant SKILL.md draft. Asks adaptive questions to determine skill type, scope, structure, and content, then generates a ready-to-validate draft.
type: interactive
theme: meta-authoring
best_for:
  - "Turning a rough idea or framework into a structured PM skill"
  - "Deciding whether raw content should be a component, interactive, or workflow skill"
  - "Getting from blank page to a complete SKILL.md draft through guided conversation"
scenarios:
  - "I have notes from a workshop and want to turn them into a skill"
  - "Help me create a new skill — I know the topic but not the structure"
  - "I have a PM framework I want to formalize as a repo skill"
estimated_time: "10-15 min"
---

## Purpose

Walk through the full skill design process interactively — from raw idea or content to a structured, repo-compliant SKILL.md draft. Asks adaptive questions to determine skill type, scope, structure, and content, then generates a ready-to-validate draft.

This skill is the conversational complement to `skill-authoring-workflow`. That skill defines the process and validation gates. This one sits with you and figures out what to build before you build it.

## Key Concepts

### When to Use This vs. Other Authoring Tools

| Tool | Best When |
|------|-----------|
| **This skill (skill-creator)** | You have an idea or raw content and need help shaping it into the right structure through conversation |
| `skill-authoring-workflow` | You already know what to build and need the process checklist and validation steps |
| `scripts/build-a-skill.sh` | You know the structure and want a terminal wizard to collect sections |
| `scripts/add-a-skill.sh` | You have a source document and want AI-assisted generation end-to-end |

### The Three Skill Types (Decision Criteria)

- **Component**: One artifact or template. Self-contained. Gets referenced by other skills. Ask: "Is this a thing someone creates?"
- **Interactive**: Guided conversation with adaptive questions and enumerated recommendations. Ask: "Does this require back-and-forth to be useful?"
- **Workflow**: Multi-phase orchestration referencing other skills. Ask: "Does this coordinate multiple activities across steps?"

### Skill Anatomy (Non-Negotiable Sections)

Every skill requires these sections in order:
1. **Purpose** — What it does + when to use it (outcome-focused)
2. **Key Concepts** — Frameworks, definitions, mental models
3. **Application** — Step-by-step instructions an agent can follow
4. **Examples** — At least one concrete, specific example
5. **Common Pitfalls** — Named failure modes with consequences and fixes
6. **References** — Related skills, external frameworks, source material

### Metadata Constraints

- `name`: lowercase kebab-case, ≤ 64 characters
- `description`: ≤ 200 characters, must include trigger cue ("Use when...")
- `intent`: longer repo-facing summary (no character limit)
- `type`: one of `component`, `interactive`, `workflow`

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the default interaction protocol for this skill.

It defines:
- Session heads-up + entry mode (Guided, Context dump, Best guess)
- One-question turns with plain-language prompts
- Progress labels (e.g., Context Q1/5)
- Interruption handling and pause/resume behavior
- Numbered recommendations at decision points
- Quick-select numbered response options (include `Other (specify)` when useful)

This file defines the domain-specific content. If there is a conflict, follow this file's domain logic.

## Application

This interactive skill asks **up to 5 adaptive questions**, then delivers a **complete SKILL.md draft** with frontmatter, all required sections, and repo-compliant structure.

---

### Step 0: Session Start

**Agent says:**

"I'll help you design a new PM skill from scratch. This takes about 10-15 minutes and up to 5 questions. How do you want to start?

1. **Guided** — I'll ask questions one at a time and build the skill from your answers (recommended)
2. **Context dump** — Paste your raw content, notes, or framework and I'll propose a skill structure
3. **Best guess** — Tell me just the topic and I'll draft a skill you can refine"

---

### Question 1: What's the Raw Material? (Q1/5)

**Agent asks:**

"What are we turning into a skill? Give me whatever you have."

1. **A framework or mental model** — A structured way of thinking about a PM problem (e.g., prioritization matrix, decision tree)
2. **A template or artifact** — A deliverable PMs create (e.g., PRD section, positioning statement, epic format)
3. **A process or workflow** — A multi-step method for completing a PM task (e.g., discovery sprint, roadmap planning)
4. **A coaching or advisory topic** — A domain where PMs need guided, adaptive help (e.g., stakeholder navigation, pricing decisions)

**Or describe what you have in your own words.**

**Agent note:** If the user pastes raw content instead of choosing an option, analyze the content and infer the answer. Confirm your interpretation before proceeding.

---

### Question 2: Skill Type Decision (Q2/5)

**Based on Q1 answer, agent recommends a type and confirms:**

*If Q1 = Framework or Template:*

"This sounds like a **component skill** — a self-contained artifact or reference. It would include a template, quality criteria, and examples. Does that fit, or is there a conversational/adaptive element I'm missing?

1. **Yes, component** — It's a standalone deliverable or reference
2. **Actually, it needs conversation** — Users need guided questions to use it well (→ interactive)
3. **It's bigger than one artifact** — It orchestrates multiple steps or other skills (→ workflow)"

*If Q1 = Process or Workflow:*

"This sounds like a **workflow skill** — a multi-phase process. Does it reference or orchestrate other discrete skills/artifacts, or is it more of a guided conversation?

1. **Yes, workflow** — It has distinct phases and may reference other skills
2. **It's more conversational** — The value comes from adaptive questions and recommendations (→ interactive)
3. **It's simpler than I described** — Really it's one artifact with steps (→ component)"

*If Q1 = Coaching or Advisory:*

"This sounds like an **interactive skill** — guided questions that adapt based on answers, ending with enumerated recommendations. Sound right?

1. **Yes, interactive** — It needs back-and-forth to be useful
2. **It's more of a reference** — Users just need the framework, not a conversation (→ component)
3. **It's a full process** — Multiple phases, orchestrates other skills (→ workflow)"

---

### Question 3: Scope and Naming (Q3/5)

**Agent asks:**

"What should we call this skill? I need two things:

**a) A working name** — lowercase-kebab-case, max 64 characters (e.g., `feature-investment-advisor`, `user-story`, `discovery-process`)

**b) A one-sentence description** — What it does + when to use it. Must fit in 200 characters and start with a verb or 'Use when...'

Give me your best attempt and I'll tighten it if needed. Or just describe the skill's purpose and I'll propose both."

**Agent note:** Validate the name format (kebab-case, ≤ 64 chars) and description length (≤ 200 chars) before proceeding. If either fails, suggest a fix.

---

### Question 4: Key Content (Q4/5)

**This question adapts based on skill type from Q2:**

*For component skills:*

"What are the core elements of this artifact or framework? I need:
1. **The template or structure** — What sections/fields does it contain?
2. **Quality criteria** — What separates a good one from a bad one?
3. **One concrete example** — A filled-in version showing it done well

Give me whatever you have — bullet points, rough notes, or a full draft."

*For interactive skills:*

"Walk me through the conversation flow:
1. **What's the opening question?** — What does the user need to tell you first?
2. **What are the 2-4 branching paths?** — How do answers change what comes next?
3. **What recommendations emerge?** — What are the 3-5 outcomes you'd offer?

Give me the decision tree as you see it — even if it's rough."

*For workflow skills:*

"Map out the phases:
1. **What are the major steps?** (Usually 3-6 phases)
2. **What's the input and output of each phase?**
3. **Which existing skills does this reference?** (Check with `scripts/find-a-skill.sh --keyword <topic>`)
4. **Where are the decision points?**

Give me the flow — sequential, branching, or both."

---

### Question 5: Pitfalls and Edge Cases (Q5/5)

**Agent asks:**

"What goes wrong when people do this badly? I need 2-3 failure modes:

1. **Name the failure** — Give it a label (e.g., 'Metrics Theater', 'Hero Syndrome')
2. **Describe the consequence** — What happens when someone falls into this trap?
3. **State the fix** — What's the corrective action?

If you're not sure, tell me the most common mistake you've seen and I'll help structure it."

---

### Draft Generation

After collecting answers to Q1-Q5, the agent generates a complete SKILL.md draft including:

1. **YAML frontmatter** — `name`, `description`, `intent`, `type`, `best_for`, `scenarios`, `estimated_time`
2. **Purpose** — Synthesized from Q1 + Q3
3. **Key Concepts** — Structured from Q4 content
4. **Application** — Step-by-step instructions derived from Q4
5. **Examples** — Concrete example from Q4 (or generated if not provided)
6. **Common Pitfalls** — Structured from Q5
7. **References** — Related skills identified during conversation + source material

**Agent says after generating:**

"Here's your draft SKILL.md. Before we call it done:

1. **Review the draft** — Does it capture your intent?
2. **Run validation** — `python3 scripts/check-skill-metadata.py skills/<name>/SKILL.md`
3. **Check triggers** — `python3 scripts/check-skill-triggers.py skills/<name>/SKILL.md --show-cases`
4. **Smoke test** — `./scripts/test-a-skill.sh --skill <name> --smoke`

Want me to adjust anything, or are you ready to validate?"

## Examples

### Example: Framework → Component Skill

**Q1:** "1 — A framework. It's a 2x2 matrix for evaluating build-vs-buy decisions."
**Q2:** "1 — Yes, component."
**Q3:** "Name: `build-vs-buy-matrix`. Description: 'Evaluate build-vs-buy decisions using a 2x2 matrix of strategic value and implementation complexity. Use when choosing between building internally and buying a solution.'"
**Q4:** "The axes are strategic differentiation (low/high) and implementation complexity (low/high). Four quadrants: Buy (low/low), Partner (low/high), Build (high/low), Invest (high/high). Quality criteria: each quadrant has a clear decision rule and one example."
**Q5:** "Biggest mistake: treating it as a one-time decision. Consequence: you build something, market shifts, and you're stuck maintaining undifferentiated tech. Fix: revisit quarterly."

**Output:** Complete component skill with template, filled example, and the quarterly-review pitfall.

---

### Example: Advisory Topic → Interactive Skill

**Q1:** "4 — Coaching topic. Helping PMs navigate their first pricing conversation with leadership."
**Q2:** "1 — Yes, interactive."
**Q3:** "Name: `pricing-conversation-advisor`. Description: 'Prepare for your first pricing conversation with leadership. Use when presenting pricing changes or new monetization to executives.'"
**Q4:** "Opening question: What's the pricing change? Branches: new product pricing, price increase on existing, freemium-to-paid conversion, usage-based transition. Recommendations: data to bring, objection handling, framing strategies."
**Q5:** "Failure mode: 'Leading with the Number.' Consequence: executives fixate on the price point instead of the strategy. Fix: always lead with the business case and customer impact before revealing the number."

**Output:** Complete interactive skill with 3-question flow, 4 branches, and enumerated recommendations per branch.

---

### Anti-Pattern: Scope Creep

**Q1:** "I want a skill that covers all of product strategy — vision, roadmaps, OKRs, prioritization, stakeholder alignment, and metrics."

**Agent response:** "That's 4-6 separate skills, not one. Let's pick the one that matters most right now and build that. Which piece is most urgent?

1. Vision → component skill
2. Roadmap planning → workflow skill (already exists: `roadmap-planning`)
3. Prioritization → interactive skill (already exists: `prioritization-advisor`)
4. Something else

Start with one. We can build the others after."

## Common Pitfalls

### Pitfall 1: Type Confusion
**Symptom:** Calling something a "workflow" when it's really a template with numbered steps.

**Consequence:** Over-engineered skill that references non-existent sub-skills and confuses users.

**Fix:** Apply the type decision questions from Q2 honestly. If it doesn't orchestrate other skills or have distinct phases with different inputs/outputs, it's probably a component.

### Pitfall 2: Description That Doesn't Trigger
**Symptom:** Description says what the skill is ("A framework for pricing decisions") but not when to use it.

**Consequence:** Claude can't match user requests to the skill. It sits unused.

**Fix:** Every description must answer "Use when..." — e.g., "Evaluate pricing decisions using a structured framework. Use when choosing between pricing models or preparing a pricing proposal."

### Pitfall 3: Skipping Validation
**Symptom:** "The draft looks good, let's ship it."

**Consequence:** Broken frontmatter, missing sections, failed cross-references, inconsistent catalog counts.

**Fix:** Always run `check-skill-metadata.py` and `check-skill-triggers.py` before considering the skill done. No exceptions.

### Pitfall 4: Kitchen Sink Scope
**Symptom:** Trying to pack an entire domain into one skill.

**Consequence:** A 500-line monster that does nothing well. Too broad to trigger accurately, too long to be useful.

**Fix:** One skill = one job. If you need more than 6 application steps or more than 4 branches, you probably need multiple skills.

## References

### Related Skills
- [`skill-authoring-workflow`](../skill-authoring-workflow/SKILL.md) — The process checklist and validation gates; use after this skill generates a draft
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md) — Facilitation protocol for this interactive skill

### Repo Tools
- `scripts/build-a-skill.sh` — Terminal wizard for section-by-section skill creation
- `scripts/add-a-skill.sh` — Content-first automated skill generator
- `scripts/check-skill-metadata.py` — Structural validation
- `scripts/check-skill-triggers.py` — Trigger-readiness audit
- `scripts/test-a-skill.sh` — Full quality gate
- `scripts/find-a-skill.sh` — Check for overlapping skills before creating

### Documentation
- `CLAUDE.md` — Master skill distillation protocol and quality standards
- `docs/Building PM Skills.md` — Manual skill creation guide
- `docs/Add-a-Skill Utility Guide.md` — Automated creation guide
