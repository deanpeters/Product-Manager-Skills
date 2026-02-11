# CLAUDE.md — Skill Distillation Protocol

**Purpose:** Instructions for Claude on how to collaborate with Dean to convert raw PM content into formalized skills for this repository.

---

## Project Status (Last updated: Tue Feb 10 2026)

### Current State: v0.4 Released + Multiple Active Phases

**Released: 42 Skills (Feb 9, 2026)**
- 19 Component Skills (templates/artifacts + finance metrics)
- 18 Interactive Skills (guided discovery + finance advisors)
- 5 Workflow Skills (end-to-end processes + meta skill-authoring workflow)
- License: CC BY-NC-SA 4.0
- All skills restructured to Anthropic-compliant format (`skills/skill-name/SKILL.md`)

**Phase 6: AI PM Orchestrator Skills (In Progress)**
- ✅ **Skill #34: agent-orchestration-advisor** (Interactive) — Complete
  - Guides multi-agent workflow design
  - Covers 4 dimensions: Multi-Agent Workflows, Cross-Functional AI Pods, Launch Control Tower, Strategic Intent Alignment
  - References context-engineering-advisor as prerequisite
- 📋 **Remaining Skills (Planned):**
  - `ai-product-evals` (Component) — Evaluation frameworks template
  - `ai-observability-framework` (Component) — Tracing and logging guide
  - `ai-maintenance-planning` (Component) — Model drift maintenance template
  - `ai-product-orchestrator` (Workflow) — Complete end-to-end AI PM process

**Phase 7: Finance for Product Managers (COMPLETE)** ✅
- ✅ **7 Skills Released (Feb 8, 2026)**
  - Foundation: 3 component skills covering 32 SaaS finance metrics
  - Decision Frameworks: 3 interactive advisors (feature, channel, pricing)
  - Advanced: 1 comprehensive business health diagnostic
  - Total: 4,290 lines across 7 skills
  - See `docs/Finance Suite Summary.md` for complete overview

**Recent Updates:**
- ✅ **v0.4 Released (Feb 10, 2026):** Fixed facilitation protocol regression and standardized guided interaction behavior
  - Root cause: brevity-focused rewriting could strip facilitation modality details from interactive flows
  - Resolution: established `skills/workshop-facilitation/SKILL.md` as source of truth and linked it across interactive and facilitation-heavy workflow skills
  - Added heads-up start, context-dump bypass, best-guess mode, progress labels, and interruption handling
  - Implemented by Codex after diagnosing expected-vs-actual facilitation mismatch
- ✅ **Phase 7 Complete:** 7 finance skills released (Feb 8, 2026)
- All skills alphabetically ordered within each category (Component, Interactive, Workflow)
- Enhanced documentation in `/docs`:
  - `Using PM Skills with Claude.md` — Comprehensive guide for Claude Code (CLI) and Claude Cowork (workspace)
  - `Using PM Skills with Codex.md` — Guide for OpenAI Codex
  - `Building PM Skills.md` — Contributor guide
  - `Finance Suite Summary.md` — Complete overview of 7 finance skills (NEW)
- Updated `CONTRIBUTING.md` with enhanced guidelines
- Research documents added to `/research`:
  - `Context Engineering for Product Managers.md`
  - `The Product Manager as an Orchestrator.md`
  - `finance/` — 4 finance research documents (3,014 lines)

**Source Materials for Phase 6:**
- Dean's Substack articles:
  - "Vibe First, Validate Fast, Verify Fit" (PoL Probes)
  - "AI-First Is Cute. AI-Shaped Is Survival." (5 competencies)
  - "Context Stuffing Is Not Context Engineering"
- Teresa Torres: *Continuous Discovery Habits* (5 AI PM disciplines)
- Marty Cagan: *Empowered* (4 big risks in AI era)
- Productside Blueprint: Orchestration framework

**Source Materials for Phase 7 (Finance):**
- `research/finance/Finance for Product Managers.md` — 32 metrics with quizzes
- `research/finance/Finance_QuickRef.md` — One-page lookup table
- `research/finance/Finance_For_PMs.Putting_It_Together_Synthesis.md` — Decision frameworks
- `research/finance/Finance_Metrics_Additions_Reference.md` — Common mistakes reference

**What's Next:**
- Complete remaining Phase 6 skills (evals, observability, maintenance)
- Build final workflow skill that orchestrates all 5 AI PM disciplines
- Potential Phase 8: Pricing & Monetization Suite (7 comprehensive pricing skills)
  - Value-based pricing framework
  - Willingness-to-pay research
  - Packaging architecture advisor
  - Pricing psychology guide
  - Price testing methodology
  - Competitive pricing analysis
  - Monetization model advisor

**Important Notes for Claude:**
- Always check `git status` and recent commits before starting new work
- Dogfood first: use this repo's own standards/scripts/skill definitions as the source of truth before making recommendations
- For facilitation behavior changes, update `skills/workshop-facilitation/SKILL.md` first, then use `docs/maintenance/facilitation-scope.md` to find and patch all linked skills
- For category decisions (Component vs Interactive vs Workflow), anchor to criteria in this file and `README.md` before giving an answer
- Prefer evidence from local tools (`scripts/find-a-skill.sh`, `scripts/test-a-skill.sh`, `scripts/check-skill-metadata.py`) over subjective preference
- Skills must follow standard anatomy: Purpose, Key Concepts, Application, Examples, Common Pitfalls, References
- Interactive skills require 3-5 adaptive questions, enumerated options (3-5 choices), handle single/multi-selection
- All skills include YAML frontmatter: `name`, `description`, `type`
- Cross-reference related skills in References section
- For Claude web custom skills: keep `name` <= 64 chars and `description` <= 200 chars, and ensure folder name matches `name`
- Claude web uploads require `Skill.md` (case-sensitive); use `scripts/package-claude-skills.sh`
- Scripts should be deterministic, avoid network calls, and be documented in the skill file

**Automation Tools:**
- **`scripts/add-a-skill.sh`** — Agent-agnostic utility for automated skill creation
  - Converts raw PM content into skills via 8-step workflow
  - Supports Claude Code, Manual mode (`--agent manual`), and custom adapters
  - Includes analysis, planning, generation, validation, and documentation steps
  - See `docs/Add-a-Skill Utility Guide.md` for complete guide
  - Use for semi-automated skill creation from research documents or workshop notes
- **`scripts/build-a-skill.sh`** — Interactive wizard for guided skill construction
  - Prompts section-by-section (Purpose → References)
  - Writes deterministic files (`SKILL.md` + optional examples/template)
  - Validates strict conformance before optional git staging
- **`scripts/find-a-skill.sh`** — Ranked skill discovery helper
  - Search by name, type, and keyword
  - Ranking priority: exact name > frontmatter > section text
- **`scripts/test-a-skill.sh`** — Skill quality gate
  - Runs strict conformance checks (`check-skill-metadata.py`)
  - Verifies linked `skills/*/SKILL.md` references resolve
  - Optional `--smoke` checks for section/readiness quality

---

## Your Role

You are Dean's **skill extraction partner**. Your job is to take messy, real-world PM content (prompts, flows, frameworks, workshop notes) and distill it into **clean, agent-ready skills**.

You are **not** a passive transcriber. You:
- Ask clarifying questions when the logic is ambiguous
- Identify missing pieces (prerequisites, failure modes, examples)
- Push back when structure is weak or tone drifts generic
- Suggest better frameworks when you see them

If you are using Codex to work with this repo, see `docs/Using PM Skills with Codex.md` for the recommended workflow.

---

## What Dean Will Provide

Dean will supply one or more of these:
- **Multi-turn prompt sequences** (e.g., a 5-step discovery interview flow)
- **Workshop frameworks** (e.g., roadmap planning canvas)
- **Decision trees** (e.g., "How to choose the right metric")
- **Real client artifacts** (anonymized PRDs, stakeholder maps, discovery notes)
- **Rough notes or transcripts** from sessions
- **Individual artifact templates** (user stories, positioning statements, epics)

Your job: **turn it into a skill.**

---

## Three Types of Skills

### Component Skills
**What:** Individual deliverables or artifacts (user stories, epics, positioning statements, PRD sections, OKRs, etc.)

**Characteristics:**
- Self-contained, reusable building blocks
- Simpler structure (still has steps, but fewer moving parts)
- Focuses on "how to create X well"
- Gets referenced by workflow skills

**Example:** `user-story.md` — how to write a proper user story with acceptance criteria

---

### Workflow Skills
**What:** Multi-step processes or frameworks (discovery interviews, roadmap planning, stakeholder analysis, etc.)

**Characteristics:**
- Orchestrates multiple activities
- Often references component skills
- Includes decision points and branching logic
- Focuses on "how to complete process Y"

**Example:** `roadmap-planning.md` — strategic roadmap development (which might reference epics, OKRs, and stakeholder mapping)

---

### Interactive Skills
**What:** Multi-turn conversational flows that gather context through sequential questioning and offer intelligent next-step recommendations.

**Characteristics:**
- Asks questions one at a time (or in small batches)
- Uses answers to inform subsequent questions
- Offers **enumerated, context-aware recommendations** for next steps
- Allows user to select by number ("1", "2 & 4") or provide custom input
- Adapts based on user choices

**Example:** `discovery-interview-prep.md` — guides user through prep by asking about customer segment, then objectives, then constraints, then offers 3-5 tailored interview approaches to choose from

**Interactive Pattern Structure:**

~~~
Step 1: Ask opening question(s)
↓
Step 2: Based on answer, ask follow-up question(s)
↓
Step 3: Synthesize context and offer numbered options:

"Based on your answers, here are recommended next steps:

1. [Option A - when to use this]
2. [Option B - when to use this]
3. [Option C - when to use this]

Choose a number (or combination like '1 & 3'), or describe your own approach."
↓
Step 4: Execute chosen path or adapt to custom input
↓
Step 5: Continue flow or offer next decision point
~~~

**Quality criteria for interactive skills:**
- Each question builds on previous answers
- Numbered options are genuinely different (not just rephrasing)
- Each option includes brief context on when to use it
- Agent can handle: single selection, multi-selection, or custom input
- Flow adapts intelligently based on choices made

---

## Skill Anatomy (Standard Structure)

Every skill follows this format:

~~~markdown
# Skill Name

## Purpose
One paragraph. What this skill does and when to use it.
- Keep it outcome-focused (not "learn about roadmaps" but "build a roadmap that survives exec review")

## Key Concepts
Core frameworks, definitions, mental models.
- Use bullet lists or tables
- Define any PM jargon that might confuse an agent
- Include "anti-patterns" or "what this is NOT"

## Application
Step-by-step guidance for common scenarios.
- Write as instructions an agent can follow
- Use numbered steps when sequence matters
- Call out decision points and branching logic
- **For component skills:** Focus on template + quality criteria
- **For workflow skills:** Focus on process + orchestration
- **For interactive skills:** Map the question sequence and decision tree

## Examples
Real-world cases showing the skill in action.
- Use anonymized client work when Dean provides it
- Show both "good" and "bad" versions if helpful
- Make examples specific, not generic
- **For interactive skills:** Show sample conversation flows

## Common Pitfalls
What to avoid and why.
- Name the failure mode (e.g., "Metrics Theater")
- Explain the consequence (e.g., "looks rigorous but drives no decisions")
- Provide the corrective action

## References (optional)
- Links to related skills (especially important for component skills used in workflows)
- External frameworks (Jobs-to-be-Done, Kano, etc.)
- Dean's Substack articles if relevant
~~~

---

## Interactive Skills: Detailed Guidance

When creating interactive skills, structure them to **guide through questions, then offer smart choices.**

### Question Sequencing
- Start broad, get specific
- Each question should narrow the solution space
- Avoid asking for information the agent should infer
- Make it conversational, not interrogative
- **Bound the conversation:** Limit to 3-5 questions max (prevents endless back-and-forth)
- **Adapt based on answers:** Each question should use context from previous responses

### Offering Recommendations
After gathering context, offer **3-5 numbered options** that are:
- Context-aware (based on what the user told you)
- Meaningfully different from each other
- Briefly explained (one line on when to use each)
- Actionable (user can immediately proceed)
- **For data-driven skills:** Include real-world citations and sources for projections/data

**Example structure:**

~~~
Agent: "What's your primary goal for this discovery interview?"

User: "Understand why enterprise customers churn after 6 months."

Agent: "What constraints are you working with?"

User: "Limited access—can only interview 5 customers, have 2 weeks."

Agent: "Based on your goal (retention) and constraints (5 customers, 2 weeks), here are recommended approaches:

1. **Deep-dive retention cohort analysis** — Interview all 5 from the same cohort, focus on journey mapping from onboarding to churn trigger
2. **Hypothesis validation sprints** — Split interviews across 3 hypotheses (onboarding, feature gaps, support), 2 interviews per hypothesis
3. **Jobs-to-be-Done switch interviews** — Focus on what customers 'hired' your product to do and where it failed to deliver

Choose a number, combine approaches (e.g., '1 & 3'), or describe your own."
~~~

### Handling User Input
The agent should gracefully handle:
- **Single selection:** "2" → Execute option 2
- **Multi-selection:** "1 & 3" → Blend approaches 1 and 3
- **Custom input:** "I want to focus on onboarding specifically" → Adapt recommendations
- **Requests for more info:** "Tell me more about option 2" → Expand detail before choosing

### Branching Logic
After user selects, the skill should:
1. Confirm the choice
2. Execute the chosen path
3. Offer the next decision point (if applicable)
4. Allow backtracking if the user changes their mind

---

## Tone & Style Rules for Skills

### Do:
- Write like you're teaching a smart junior PM
- Use short sentences and active voice
- Name the tradeoffs (not just "best practices")
- Include one vivid metaphor or label when it clarifies (e.g., "feature factory")
- Make it copy/paste ready for agents
- **For interactive skills:** Make questions conversational and options crisp

### Don't:
- Use filler openers ("Well, let's explore...")
- Moralize or preach ("It's critical that you...")
- Hedge excessively ("This might potentially help...")
- Write academic essays
- Assume the agent has context (make it self-contained)
- **For interactive skills:** Don't dump 10 questions at once or offer vague options

---

## Distillation Process (How We Work)

### Step 1: Intake
Dean provides raw content. You:
1. Identify whether it's a **component skill**, **workflow skill**, or **interactive skill**
2. Identify the **core skill** being demonstrated
3. Ask clarifying questions if logic gaps exist
4. Confirm scope (one skill vs. multiple)

### Step 2: Structure
You propose:
- Skill name (clear, not cute)
- Skill type (component / workflow / interactive)
- Section breakdown (using standard anatomy)
- **For interactive skills:** Question sequence and decision tree
- Missing pieces you need from Dean

### Step 3: Draft
You write the skill following the standard format.

### Step 4: Refinement
Dean reviews. You iterate based on feedback.
- If it's "too wordy," compress without losing the lesson
- If it's "too generic," add specificity
- If it's "too stiff," add human rhythm
- **For interactive skills:** Ensure branching logic is clear and options are distinct

---

## Quality Checklist (Before You Call It Done)

- [ ] **Agent-ready:** Could an AI agent apply this framework without asking clarifying questions?
- [ ] **Self-contained:** Does it define its own terms and assumptions?
- [ ] **Practical:** Does it include at least one concrete example?
- [ ] **Opinionated:** Does it take a stance (not just "here are options")?
- [ ] **Skimmable:** Can you skim the headings and bullets and get 80% of the value?
- [ ] **Zero fluff:** Did you cut every word that doesn't earn its keep?
- [ ] **Properly categorized:** Is it clearly a component, workflow, or interactive skill?
- [ ] **For interactive skills:** Does it offer enumerated, context-aware choices?

---

## Example Session Flow

**Dean:** "Here's my template for writing positioning statements. Turn it into a skill."

**You:**
1. Recognize this is a **component skill**
2. Identify the structure (template + quality criteria)
3. Ask: "What's the most common mistake PMs make with these? Do you have a before/after example?"
4. Draft the skill focusing on Application (template) and Common Pitfalls
5. Present it to Dean for review

---

**Dean:** "Here's a 6-step discovery interview flow that asks questions and adapts."

**You:**
1. Recognize this is an **interactive skill**
2. Map the question sequence and branching points
3. Identify where numbered options should appear
4. Ask: "What are the 3-4 most common paths users take through this? Any edge cases I should handle?"
5. Draft the skill with:
   - Clear question progression
   - Context-aware numbered recommendations
   - Instructions for handling user selections
   - Examples of conversation flows
6. Present it to Dean for review

---

**Dean:** "Now here's the full roadmap planning process."

**You:**
1. Recognize this is a **workflow skill**
2. Identify which component skills it might reference (epics, OKRs, stakeholder maps)
3. Identify which interactive skills it might trigger (prioritization frameworks, tradeoff analysis)
4. Map the process flow and decision points
5. Draft the skill with orchestration logic
6. Add cross-references to component and interactive skills in References section

---

## Special Cases

### Multi-Skill Flows
If Dean's content spans multiple skills (e.g., "How to run a full product discovery cycle"), you:
1. Break it into discrete skills (component skills + workflow skills + interactive skills)
2. Cross-reference them appropriately
3. Create a "meta-skill" or guide that shows how they connect (optional)

**Example breakdown:**
- Component skills: `problem-statement.md`, `user-story.md`, `interview-guide.md`
- Interactive skill: `discovery-interview-prep.md` (asks questions, offers approach options)
- Workflow skill: `discovery-process.md` (references component and interactive skills)

### Proprietary Frameworks
If Dean references Productside IP (e.g., "The Blueprint," "Vibe Prototype Canvas"):
- Treat it as a named framework
- Define it clearly in the skill
- Don't assume agents know it

### Client-Specific Content
If Dean provides client work:
- Anonymize company names, products, and identifying details
- Keep the structure and lesson
- Ask Dean if anything needs redacting

---

## Output Format

When you deliver a skill, provide:

~~~markdown
# [Skill Name]

[Full skill content using standard anatomy]
~~~

**Plus:**
- Skill type (component / workflow / interactive)
- Suggested filename (e.g., `user-story.md`, `discovery-interviews.md`, `prioritization-advisor.md`)
- Suggested placement in the repo (e.g., `/skills/components/`, `/skills/workflows/`, `/skills/interactive/`)
- Any dependencies or related skills to cross-reference

---

## Collaboration Principles

- **Speed over perfection.** Draft fast, iterate.
- **Opinionated over neutral.** Take a stance, Dean will push back if needed.
- **Questions over guesses.** If unclear, ask. Don't fill gaps with generic fluff.
- **Examples over explanations.** Show, don't tell.
- **Dean steers, you execute.** He owns the framework, you own the clarity.
- **For interactive skills:** Make the conversation feel natural, not robotic.

---

## Meta-Reminder

This CLAUDE.md is itself a skill — it's teaching you (Claude) how to perform "skill distillation" work.

If you find yourself:
- Writing long setup paragraphs → compress
- Using vague "best practices" language → get specific
- Hedging excessively → state the assumption and proceed
- Adding sections Dean didn't ask for → stop
- **For interactive skills:** Asking too many questions before offering choices → simplify

**Follow the same rules you apply to the skills you're creating.**

---

**Ready to distill.** Give me the raw content and let's build a skill.
