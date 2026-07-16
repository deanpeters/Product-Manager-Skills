# Product Manager Skills v0.80 Execution Brief

## Mission

Create version 0.80 of `deanpeters/Product-Manager-Skills` as a coherent **AI Product Builder + Product Sense** release.

The release thesis is:

> AI compresses execution, but it does not improve judgment. v0.80 helps product managers build faster without outsourcing product sense.

The release should not become a vibe-coding prompt pack. It should teach product managers how to decide whether a problem deserves AI, prototype only what needs to be learned, define agent boundaries, evaluate AI quality, and hand off evidence without pretending a demo is a product.

## Hard exclusions

Do not use, mention, summarize, paraphrase, or derive examples from:

- Productside customer work
- Productside customer names
- Customer decks
- Customer workshops
- Customer playbooks
- Customer-specific examples
- Consulting delivery artifacts
- Private business development material
- Any enterprise/customer case example that is not explicitly public and non-customer-derived

Allowed source material:

1. The public `Product-Manager-Skills` repository itself.
2. The uploaded Substack export at `deanpeters.substack.com/` (also available in the path 'research/deanpeters-substack-posts.zip' of this project; see the 15 Days of AIPM series capstone at https://deanpeters.substack.com/p/day-15-the-wave-is-already-here)
3. Public market evidence only when needed for release notes or context.
4. Original synthesis from public/product-management concepts.

When in doubt, exclude the material.

## Repo principles to preserve

Before editing, read these repository files:

- `README.md`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `catalog/skills-by-type.md`
- `catalog/skills-index.yaml`
- `catalog/commands-index.yaml`
- several existing `skills/*/SKILL.md` files from each type: component, interactive, workflow
- several existing `commands/*.md` files

Preserve these repo principles:

1. `skills/` is the source of truth.
2. `dist/` is generated and should not be hand-edited.
3. Skills must be pedagogic-first, not merely output-generating.
4. ABC — Always Be Coaching.
5. Skills should explain reasoning, not just steps.
6. Examples should show the thinking, not just the output.
7. Anti-patterns are required learning scaffolding, not filler.
8. Interactive skills should guide, not interrogate.
9. Workflow skills should compose existing skills where possible.
10. Commands should provide momentum while skills provide expertise.

## Release name and positioning

Recommended release name:

> v0.80 — AI Product Builder Track

Recommended tagline:

> Build faster without outsourcing judgment.

Optional more Dean-flavored tagline:

> Build faster. Think harder. Ship less nonsense.

Recommended release description:

> v0.80 helps product managers survive the AI builder era without becoming feature-factory accelerants. The new skills teach PMs how to decide whether AI belongs, prototype only what needs to be learned, define agent boundaries, evaluate AI quality, and hand off evidence without pretending a demo is a product.

## Release arc

Use this conceptual sequence across docs, catalogs, commands, and release notes:

```text
Sense -> Decide -> Learn -> Guardrail -> Specify -> Evaluate -> Build -> Red-team -> Handoff
```

## Skills to add in v0.80

Create these nine skills:

1. `ai-product-sense`
2. `ai-feature-or-not`
3. `prototype-learning-plan`
4. `vibe-coding-guardrails`
5. `ai-agent-requirements`
6. `ai-evals-for-product-managers`
7. `ai-product-builder-playbook`
8. `product-sense-red-team`
9. `prototype-to-production-handoff`

Suggested implementation order:

1. `ai-product-sense`
2. `ai-feature-or-not`
3. `prototype-learning-plan`
4. `vibe-coding-guardrails`
5. `ai-agent-requirements`
6. `ai-evals-for-product-managers`
7. `product-sense-red-team`
8. `prototype-to-production-handoff`
9. `ai-product-builder-playbook`

Reason: build the reusable primitives first, then create the orchestration skill last.

## Commands to add in v0.80

Create these three commands if they fit the current repo command conventions:

1. `sharpen-product-sense`
2. `build-with-judgment`
3. `define-agentic-product`

Command details appear later in this brief.

## Shared reference to add

Create a shared reference if repo conventions allow shared references. Preferred path:

```text
references/ai-product-builder-principles.md
```

If the repo uses a different shared-reference convention, follow the repo convention. If there is no shared-reference convention, place equivalent principle sections inside each skill without creating brittle cross-links.

### Proposed shared reference content

```markdown
# AI Product Builder Principles

## Purpose

These principles unify the v0.80 AI Product Builder Track. Use them to keep product-builder work grounded in product judgment, evidence, safety, and learning.

## Principles

1. **AI efficiency is rent. AI-augmented judgment is the moat.**
   AI can make product work faster, but speed without judgment just ships bad assumptions with better formatting.

2. **Product sense comes before tool use.**
   Start with the user, the job, the behavior change, the business reason, and the evidence standard before selecting AI tools.

3. **A prototype is a learning instrument, not a baby product.**
   A prototype exists to answer a decision-critical question. It does not earn production status because it demos well.

4. **AI is not always the right answer.**
   Sometimes the right solution is deterministic automation, workflow redesign, better information architecture, clearer positioning, or no build at all.

5. **Agents are delegated authority, not smarter features.**
   If an agent can read, write, decide, trigger, or escalate, requirements must define its authority boundary.

6. **Benchmarks are not product readiness.**
   Model performance only matters when mapped to user-visible quality, failure cost, business value, and operating constraints.

7. **Context quality beats context volume.**
   Stuffing more context into an AI system is not the same as designing the right context, memory, retrieval, constraints, and review loops.

8. **If everything still compiles, the risk may be harder to see.**
   AI-generated systems can look functional while hiding fragility, duplication, security gaps, and maintenance debt.

9. **A PM-built prototype earns the next conversation, not production status.**
   Handoff requires humility: what was learned, what was not validated, what shortcuts were taken, and what engineering must inspect.

10. **Build faster without outsourcing judgment.**
    The goal is not to make PMs reckless builders. The goal is to help PMs turn judgment into evidence faster.
```

## Source archive inventory

The uploaded Substack export contains these high-value posts for v0.80. Use them as style, themes, and public source grounding. Do not over-quote. Prefer short signature phrases and synthesized principles.

### Core release / AI PM framing

- `ai-first-is-cute-ai-shaped-is-survival-5-ai-pm-skills-2026.md`
- `day-01---wth-is-ai-product-management.md`
- `day-02---the-ai-pm-skills-nobody-teaches.md`
- `stop-calling-it-ai-product-management.md`
- `which-ai-journey-are-you-on.md`
- `organizing-on-ai.md`
- `no-ai-wont-replace-your-job.md`
- `the-unspoken-state-of-pm-as-of-mid-2025.md`

### Product-builder / vibe-coding / prototyping

- `wth-is-a-product-builder.md`
- `the-vibe-code-deluge.md`
- `the-coming-vibe-app-collapse.md`
- `vibe-first-validate-fast-verify-fit.md`
- `vibe-to-learn-not-to-earn.md`
- `weekend-at-lennys---part-1.md`
- `if-you-give-a-manager-an-mvp.md`
- `timeboxes-are-not-evil.md`

### AI feature judgment / accidental AI / strategy

- `day-08---accidental-ai-vs-ai-first.md`
- `agentic-tool-tourism-is-not-a-strategy.md`
- `why-starting-with-why-matters-for-ai.md`
- `how-might-we-ai.md`
- `top-10-ai-pm-mistakes-of-2025.md`
- `ms-copilot-proves-you-can-ship-ai-perfectly--still-lose.md`
- `sauerkraut-is-not-a-strategy.md`
- `day-07---youre-playing-the-wrong-ai-game.md`

### Agents / delegated authority / accountability

- `day-10---your-agents-are-running-feral.md`
- `day-11---build-agents-that-dont-go-rogue.md`
- `agentic-orange-is-it-worth-the-squeeze.md`
- `2026--an-ai-accountability-odyssey.md`
- `i-replaced-my-pm-with-a-bash-script.md`

### Evals / context / AI quality

- `eddie-the-eval-and-the-fools-gold-framework.md`
- `sam-altmans-missing-gpt-5-benchmark.md`
- `context-stuffing--context-engineering.md`
- `day-05---context-engineering-is-a-team-sport.md`
- `day-09---more-data-wont-save-you.md`
- `even-the-worlds-best-ai-cant-fix-bad-product-management.md`
- `day-12---de-risk-your-ai-before-the-board-does.md`

### Product sense / red-team / feature-factory failure modes

- `feature-hostage-negotiations-just-a-small-fix.md`
- `why-your-ai-generated-user-stories-suck-and-what-to-do-about-it.md`
- `day-03---stop-solving-the-wrong-problem.md`
- `day-06---the-customer-signals-ai-gets-wrong.md`
- `the-ancient-art-of-product.md`
- `stakeholder-shuttle-diplomacy.md`
- `you-burn-50k-a-sprint--act-like-it.md`

## Voice and style constraints

The skills should sound like Product Manager Skills, not like generic AI consultancy content.

Use:

- Sharp, practical product language
- Named failure modes
- Short memorable principles
- Anti-theater framing
- Concrete artifacts
- Coaching prompts
- Consequences of bad behavior
- Examples that make judgment visible

Avoid:

- Hype language
- “Transform your organization” language
- Generic “unlock innovation” language
- AI vendor boosterism
- Overclaiming
- Treating PMs as junior engineers
- Treating vibe coding as inherently good or inherently bad
- Enterprise case examples derived from customers

Acceptable recurring phrases from the Substack archive:

- “Build faster without outsourcing judgment.”
- “AI efficiency is rent. AI-augmented judgment is the moat.”
- “A prototype is a learning instrument, not a baby product.”
- “The prototype lied beautifully.”
- “Your agents are running feral.”
- “A lack of screaming is not confirmation of competence.”
- “Context stuffing is not context engineering.”
- “Stop solving the wrong problem.”
- “You’re playing the wrong AI game.”
- “AI doesn’t speed you up. It speeds you off a cliff — faster, louder, and with better formatting.”
- “The market isn’t paying for code.”
- “Nothing triggers alarm when everything still compiles.”

Use these sparingly. They should season the skills, not dominate them.

## Frontmatter guidance

Inspect current skills to confirm exact frontmatter schema. Do not assume the schema. The repo may include fields beyond `name`, `description`, and `type`.

At minimum, each skill should have:

- `name`: exact folder name
- `description`: trigger-oriented description explaining what the skill does and when to use it
- `type`: one of the repo’s accepted types, if current schema uses `type`

Descriptions should be specific enough for agent selection. Include likely trigger phrases.

Example description pattern:

```yaml
name: ai-product-sense
description: Use this when a product manager, founder, or product leader needs to evaluate an AI product idea, AI feature proposal, product-builder concept, or prototype opportunity before committing to discovery, build, roadmap, or stakeholder review. Helps separate AI novelty from user value, clarify the behavior change, identify the riskiest assumption, define evidence standards, and recommend whether to build, prototype, research, reframe, or reject.
type: interactive
```

Adjust to current repo standards.

## Standard skill structure

Each new `SKILL.md` should include sections that align with existing repo patterns. Use the repo’s actual pattern after inspecting examples. If no stronger pattern exists, use:

1. Purpose
2. Key Concepts
3. When to Use
4. Inputs
5. Workflow
6. Output
7. Examples
8. Common Pitfalls
9. Coaching Prompts
10. References

Do not make skills pure templates. Every skill should teach the PM how to think.

## Interactive skill behavior

For interactive skills:

- Start with a brief session heads-up.
- Ask only the next few useful questions.
- Support “Best guess” mode.
- Support “Context dump” mode.
- Provide progressive recommendations instead of waiting for perfect information.
- If the user gives enough context, proceed without over-questioning.
- Always explain the reasoning behind the recommendation.
- End with an artifact or decision-ready output.

## Component skill behavior

For component skills:

- Produce a usable artifact quickly.
- Include enough guidance for the PM to adapt it.
- Surface assumptions.
- Include quality checks.
- Include anti-patterns.

## Workflow skill behavior

For workflow skills:

- Orchestrate lower-level skills.
- Make decision checkpoints explicit.
- Show which phase the user is in.
- Do not duplicate entire child-skill content; summarize and hand off.
- Preserve the v0.80 release arc.

---

# Skill 1: `ai-product-sense`

## Type

Interactive

## Priority

P0 — foundational skill for the release.

## Purpose

Help product managers evaluate an AI-shaped product idea, feature proposal, product-builder concept, or prototype opportunity before committing to build, discovery, roadmap, or stakeholder review.

The skill should diagnose whether the idea reflects product sense or merely AI/tool enthusiasm.

## Core thesis

Product sense is the ability to decide what deserves to exist before AI makes it cheap to build.

## Source posts to use

Primary:

- `ai-first-is-cute-ai-shaped-is-survival-5-ai-pm-skills-2026.md`
- `why-starting-with-why-matters-for-ai.md`
- `how-might-we-ai.md`
- `day-03---stop-solving-the-wrong-problem.md`
- `sam-altmans-missing-gpt-5-benchmark.md`
- `the-vibe-code-deluge.md`

Secondary:

- `day-02---the-ai-pm-skills-nobody-teaches.md`
- `organizing-on-ai.md`
- `even-the-worlds-best-ai-cant-fix-bad-product-management.md`

## Key concepts

- Product sense before tool use
- AI-shaped, not AI-first
- Behavior change over feature excitement
- User value over AI novelty
- Evidence standards
- Assumption clarity
- Strategic fit
- Trust and failure tolerance
- The “remove AI from the sentence” test

## Suggested workflow

1. Capture the idea in one sentence.
2. Identify the user and situation.
3. Clarify the user job, pain, or desired progress.
4. Identify the behavior change the product must create.
5. Identify why AI appears necessary.
6. Remove the word “AI” and restate the value proposition.
7. Identify the current workaround or alternative.
8. Identify the riskiest assumption.
9. Define what evidence would change the decision.
10. Recommend: build, prototype, research, reframe, or reject.

## Inputs

Ask for:

- User/customer segment
- Problem/opportunity
- Proposed AI idea
- Current workaround
- Desired behavior change
- Known evidence
- Business reason
- Constraints

If context is missing, proceed with stated assumptions.

## Output artifact

```markdown
# AI Product Sense Assessment

## 1. Idea Summary

## 2. User and Situation

## 3. Real Problem / Job

## 4. Behavior Change Required

## 5. AI Necessity Check

## 6. Current Alternative / Workaround

## 7. Strongest Case For the Idea

## 8. Weakest Assumption

## 9. Evidence Needed

## 10. Product Sense Diagnosis

## 11. Recommended Next Move
- Build
- Prototype
- Research
- Reframe
- Reject
```

## Common pitfalls

- Starting with “we need an AI feature.”
- Confusing stakeholder excitement with user demand.
- Treating demo plausibility as market pull.
- Solving a workflow problem with a chatbot.
- Using AI to hide a weak value proposition.
- Measuring novelty instead of behavior change.

## Example scenario

User says:

> We want to add an AI assistant to our onboarding flow so users can ask questions.

Skill should coach:

- What onboarding behavior is failing?
- What questions are users asking?
- Would better IA, checklists, examples, or progressive disclosure solve it?
- Is the assistant needed because inputs vary widely?
- What evidence shows users would ask instead of abandon?
- What is the lowest-cost test?

Possible diagnosis:

> The idea may be valid, but “AI assistant” is currently a solution-shaped placeholder. The product-sense move is to isolate the onboarding decision or confusion that causes drop-off, then decide whether AI is needed to handle variability or whether deterministic guidance is enough.

---

# Skill 2: `ai-feature-or-not`

## Type

Interactive

## Priority

P0

## Purpose

Help PMs decide whether a proposed product solution should use AI, use AI only assistively, use deterministic automation, fix product/design first, or not be built yet.

## Core thesis

Most teams do not need “AI-first.” They need to decide whether AI belongs in the product at all.

## Source posts to use

Primary:

- `day-08---accidental-ai-vs-ai-first.md`
- `agentic-tool-tourism-is-not-a-strategy.md`
- `why-starting-with-why-matters-for-ai.md`
- `top-10-ai-pm-mistakes-of-2025.md`
- `ms-copilot-proves-you-can-ship-ai-perfectly--still-lose.md`
- `sauerkraut-is-not-a-strategy.md`

Secondary:

- `how-might-we-ai.md`
- `day-07---youre-playing-the-wrong-ai-game.md`
- `organizing-on-ai.md`

## Key concepts

- AI-shaped vs AI-bolted-on
- Accidental AI
- Tool tourism
- Deterministic vs probabilistic solution fit
- Workflow fit
- Trust cost
- Review burden
- Cost/latency tradeoffs
- Data/context readiness
- Explainability needs

## Decision model

Use this decision set:

| Decision | Meaning |
|---|---|
| Use AI | AI is central to value creation because the problem requires synthesis, generation, natural-language interaction, prediction, pattern detection, or adaptive assistance. |
| Use AI assistively | AI helps the team or workflow, but should not become the core product experience yet. |
| Use deterministic automation | Rules, workflow, integrations, or templates solve the problem more safely and cheaply. |
| Fix product/design first | The issue is clarity, UX, positioning, trust, workflow, incentives, or information architecture. |
| Do not build yet | Problem, evidence, ownership, data, or risk profile is too weak. |

## Suggested workflow

1. Restate the proposed feature.
2. Identify the problem it claims to solve.
3. Identify why AI is being proposed.
4. Evaluate input ambiguity.
5. Evaluate output variability.
6. Evaluate user trust and failure cost.
7. Evaluate ground truth availability.
8. Evaluate data/context readiness.
9. Compare AI vs deterministic alternatives.
10. Make the decision.
11. Define next step and evidence needed.

## Output artifact

```markdown
# AI Feature Decision

## Proposed Feature

## Problem It Claims to Solve

## AI Necessity Signals

## AI Risk Signals

## Simpler Alternatives

## Decision

## Rationale

## Evidence Needed Before Build

## Recommended Next Step
```

## Common pitfalls

- Using AI to solve a positioning problem.
- Automating a broken workflow.
- Exposing AI to users before proving internal value.
- Choosing nondeterminism where users need reliability.
- Treating “competitors have AI” as a user need.
- Creating review burden and calling it productivity.

---

# Skill 3: `prototype-learning-plan`

## Type

Component

## Priority

P0

## Purpose

Turn a product or AI feature idea into a disciplined learning plan before any prototype is built.

## Core thesis

A prototype is not a baby product. It is a learning instrument.

## Source posts to use

Primary:

- `vibe-first-validate-fast-verify-fit.md`
- `day-13---tiny-bets-beat-titanic-assumptions.md`
- `vibe-to-learn-not-to-earn.md`
- `if-you-give-a-manager-an-mvp.md`
- `timeboxes-are-not-evil.md`
- `sam-altmans-missing-gpt-5-benchmark.md`

Secondary:

- `stage-fright-is-real-so-is-product-demo-regret.md`
- `the-unspoken-state-of-pm-as-of-mid-2025.md`

## Key concepts

- Proof-of-Life Probe
- Tiny bets over Titanic assumptions
- Learning before earning
- Prototype fidelity selection
- Decision-driven validation
- Kill/change/continue criteria
- What the prototype proves vs cannot prove

## Suggested workflow

1. Identify the decision the prototype should inform.
2. Identify the riskiest assumption.
3. Choose the lightest prototype that can test that assumption.
4. Define the target reviewer/user.
5. Define the test scenario.
6. Define what evidence counts.
7. Define what evidence does not count.
8. Define kill/change/continue thresholds.
9. Define timebox.
10. Define capture/debrief plan.

## Prototype fidelity options

- Storyboard
- Landing page
- Concierge test
- Wizard-of-Oz test
- Clickable mockup
- Synthetic-data simulation
- Workflow automation mock
- Throwaway coded prototype
- Internal demo
- Proof-of-Life Probe

## Output artifact

```markdown
# Prototype Learning Plan

## 1. Decision to Inform

## 2. Riskiest Assumption

## 3. Learning Question

## 4. Prototype Type

## 5. Why This Fidelity Is Enough

## 6. Target Participant / Reviewer

## 7. Test Scenario

## 8. Evidence to Capture

## 9. What This Will Not Prove

## 10. Kill / Change / Continue Criteria

## 11. Timebox

## 12. Debrief Questions
```

## Common pitfalls

- Building the fanciest prototype instead of the smallest useful one.
- Treating “users liked it” as validation.
- Calling a prototype an MVP.
- Letting stakeholder demo value override customer learning.
- Testing usability when the real risk is desirability.
- Testing feasibility when the real risk is willingness to change behavior.

---

# Skill 4: `vibe-coding-guardrails`

## Type

Interactive

## Priority

P0

## Purpose

Help PMs use AI coding/product-building tools safely and responsibly without creating shadow systems, brittle prototypes, hidden technical debt, or engineering-trust damage.

## Core thesis

AI-assisted building without judgment produces plausible systems that compile, demo well, and quietly become expensive.

## Source posts to use

Primary:

- `the-vibe-code-deluge.md`
- `the-coming-vibe-app-collapse.md`
- `wth-is-a-product-builder.md`
- `vibe-first-validate-fast-verify-fit.md`
- `the-maqāmāt-of-builderai.md`
- `weekend-at-lennys---part-1.md`

Secondary:

- `vibe-to-learn-not-to-earn.md`
- `dig-like-an-arms-merchant--deal-like-a-peacemaker.md`

## Key concepts

- Build classification
- Data boundaries
- Authority boundaries
- Review boundaries
- Lifespan boundaries
- Ownership boundaries
- Engineering trust
- Disposable vs durable artifacts
- Shadow-system prevention

## Build classifications

| Classification | Meaning | Default guardrail |
|---|---|---|
| Learning artifact | Built to understand possibility or behavior | Disposable unless explicitly promoted |
| Demo artifact | Built to communicate a concept | Must not be treated as validated product |
| Internal workflow tool | Used by team members | Needs ownership, support, data review, and cleanup path |
| Production candidate | May become real product/system | Requires engineering, security, design, and product review |
| Unsafe / blocked | Touches sensitive systems without ownership/review | Do not proceed |

## Suggested workflow

1. Ask what is being built.
2. Classify the artifact.
3. Identify data touched.
4. Identify systems touched.
5. Identify user/customer exposure.
6. Identify whether it can read/write/trigger actions.
7. Define owner and lifespan.
8. Define required review.
9. Define what must not happen.
10. Produce guardrail checklist and next action.

## Output artifact

```markdown
# Vibe-Coding Guardrail Assessment

## Artifact Classification

## Intended Use

## Not Intended For

## Data Boundaries

## System Boundaries

## Authority Boundaries

## Review Required

## Lifespan / Disposal Plan

## Owner

## Engineering Trust Risks

## Allowed Next Step

## Blockers
```

## Common pitfalls

- “It works on my laptop, so it is ready.”
- Shipping prototype code because stakeholders liked the demo.
- Creating a shadow system and calling it empowerment.
- Forgetting cleanup and ownership.
- Hiding AI-generated shortcuts from engineering.
- Touching real customer data in a learning artifact.
- Confusing technical plausibility with product validation.

---

# Skill 5: `ai-agent-requirements`

## Type

Component

## Priority

P0/P1

## Purpose

Help PMs define agentic product behavior before implementation by specifying delegation boundaries, tool/data access, human checkpoints, observability, evaluation needs, and failure handling.

## Core thesis

An agent is not a smarter feature. It is delegated authority.

## Source posts to use

Primary:

- `day-10---your-agents-are-running-feral.md`
- `day-11---build-agents-that-dont-go-rogue.md`
- `agentic-orange-is-it-worth-the-squeeze.md`
- `agentic-tool-tourism-is-not-a-strategy.md`
- `2026--an-ai-accountability-odyssey.md`
- `i-replaced-my-pm-with-a-bash-script.md`

Secondary:

- `youve-entered-the-automation-zone.md`
- `day-12---de-risk-your-ai-before-the-board-does.md`

## Key concepts

- Delegated authority
- Agent job statement
- Trigger conditions
- Actor/user
- Read/write/decide/trigger/escalate permissions
- Human-in-the-loop checkpoints
- Tool access
- Data access
- Memory/context requirements
- Logs/traces/observability
- Failure taxonomy
- Escalation and rollback
- Cost boundaries

## Suggested artifact name

Use “Agent Delegation Contract” as the primary artifact.

## Output artifact

```markdown
# Agent Delegation Contract

## 1. Agent Name / Working Label

## 2. User / Actor Served

## 3. Job to Be Delegated

## 4. Trigger Conditions

## 5. Allowed Actions

## 6. Forbidden Actions

## 7. Tool Access

## 8. Data Access

## 9. Context / Memory Requirements

## 10. Human Checkpoints

## 11. Escalation Paths

## 12. Observability Requirements

## 13. Evaluation Requirements

## 14. Failure Modes

## 15. Cost / Latency Boundaries

## 16. Rollback / Shutdown Conditions

## 17. Open Questions
```

## Suggested workflow

1. Define what job the agent performs.
2. Define who it serves.
3. Define when it acts.
4. Define what it may read.
5. Define what it may write.
6. Define what it may decide.
7. Define what it may trigger.
8. Define what it must never do.
9. Define when a human must review.
10. Define what must be logged.
11. Define failure and rollback paths.

## Common pitfalls

- Calling a chatbot an agent.
- Giving tools to an agent before defining authority.
- Forgetting escalation.
- Assuming silence means competence.
- Treating observability as an engineering-only concern.
- Letting agents accumulate scope without ownership.
- Measuring task completion while ignoring failure cost.

---

# Skill 6: `ai-evals-for-product-managers`

## Type

Workflow or Interactive

Recommendation: Workflow if the repo’s workflow skills support multi-step artifact creation; otherwise Interactive.

## Priority

P0/P1

## Purpose

Help PMs define product-quality evals for AI features, agents, copilots, or AI-assisted workflows without pretending PMs need to become ML engineers.

## Core thesis

Evals without product context become expensive dashboards for impending disasters.

## Source posts to use

Primary:

- `eddie-the-eval-and-the-fools-gold-framework.md`
- `sam-altmans-missing-gpt-5-benchmark.md`
- `context-stuffing--context-engineering.md`
- `day-09---more-data-wont-save-you.md`
- `even-the-worlds-best-ai-cant-fix-bad-product-management.md`
- `day-12---de-risk-your-ai-before-the-board-does.md`

Secondary:

- `day-05---context-engineering-is-a-team-sport.md`
- `day-06---the-customer-signals-ai-gets-wrong.md`

## Key concepts

- User-visible quality
- Product readiness vs model benchmark
- Failure taxonomy
- Golden examples
- Human review rubric
- Ground truth
- Context quality
- Drift
- Monitoring
- Launch thresholds
- “Not ready” criteria

## Suggested workflow

1. Define the AI behavior being evaluated.
2. Define user-visible quality dimensions.
3. Define unacceptable failures.
4. Define expected inputs and contexts.
5. Define output standards.
6. Create failure taxonomy.
7. Create golden example plan.
8. Define human review rubric.
9. Define telemetry/monitoring.
10. Define launch thresholds.
11. Define review cadence.
12. Define owner and decision rights.

## Output artifact

```markdown
# AI Product Eval Plan

## 1. AI Behavior Under Evaluation

## 2. User-Visible Quality Dimensions

## 3. Product Readiness Criteria

## 4. Unacceptable Failures

## 5. Input / Context Requirements

## 6. Output Standards

## 7. Failure Taxonomy

## 8. Golden Examples Plan

## 9. Human Review Rubric

## 10. Telemetry / Monitoring

## 11. Launch Thresholds

## 12. Drift / Regression Checks

## 13. Review Cadence

## 14. Owner / Decision Rights
```

## Common pitfalls

- Treating benchmark performance as product readiness.
- Measuring only hallucination.
- Ignoring the cost of false confidence.
- Failing to define “not ready.”
- Collecting more data without improving signal quality.
- Using evals as theater after launch instead of decision support before launch.

---

# Skill 7: `product-sense-red-team`

## Type

Interactive

## Priority

P1, but strongly recommended for v0.80 because it gives the release its sharp edge.

## Purpose

Stress-test a product idea, AI feature, prototype, or roadmap bet before it becomes politically expensive.

## Core thesis

The cheapest time to find bad product logic is before the prototype becomes politically expensive.

## Source posts to use

Primary:

- `feature-hostage-negotiations-just-a-small-fix.md`
- `why-your-ai-generated-user-stories-suck-and-what-to-do-about-it.md`
- `day-12---de-risk-your-ai-before-the-board-does.md`
- `day-07---youre-playing-the-wrong-ai-game.md`
- `day-03---stop-solving-the-wrong-problem.md`
- `the-unspoken-state-of-pm-as-of-mid-2025.md`

Secondary:

- `stakeholder-shuttle-diplomacy.md`
- `you-burn-50k-a-sprint--act-like-it.md`
- `ship-it--ship-it-good.md`

## Red-team lenses

| Lens | Question |
|---|---|
| Problem truth | Is the problem real, repeated, and costly? |
| User behavior | What behavior must change? |
| Evidence | What have we actually observed? |
| Alternative gravity | What will users keep doing instead? |
| AI necessity | Does AI create value or just theater? |
| Trust | What must users believe before relying on it? |
| Failure cost | What happens when the system is wrong? |
| Incentives | Who benefits if this gets built? Who pays the tax? |
| Strategy | Why should this company do this now? |
| Hidden cost | What cost is being disguised as “just a small fix”? |

## Suggested workflow

1. Capture the idea.
2. State the strongest case for it.
3. State the strongest case against it.
4. Apply the red-team lenses.
5. Identify fatal assumption candidates.
6. Identify what evidence is missing.
7. Recommend build/prototype/research/reframe/kill.
8. Provide a cleaner version of the idea if it survives.

## Output artifact

```markdown
# Product Sense Red-Team Review

## 1. Idea Under Review

## 2. Strongest Case For

## 3. Strongest Case Against

## 4. Red-Team Findings

## 5. Hidden Costs / Externalities

## 6. Fatal Assumption Candidates

## 7. Evidence Needed

## 8. Reframe Options

## 9. Recommendation
- Build
- Prototype
- Research
- Reframe
- Kill

## 10. Cleaner Next-Step Brief
```

## Common pitfalls

- Softening critique until it becomes useless.
- Confusing cynicism with red-teaming.
- Treating stakeholder pressure as strategy.
- Ignoring opportunity cost.
- Focusing only on feasibility.
- Failing to produce a better path after critique.

---

# Skill 8: `prototype-to-production-handoff`

## Type

Workflow

## Priority

P1

## Purpose

Convert a PM-built or AI-assisted prototype into an engineering-ready handoff that clearly separates learning, assumptions, shortcuts, validation, risks, and recommended next action.

## Core thesis

A prototype earns the next conversation. It does not earn production status.

## Source posts to use

Primary:

- `vibe-first-validate-fast-verify-fit.md`
- `context-stuffing--context-engineering.md`
- `the-coming-vibe-app-collapse.md`
- `the-vibe-code-deluge.md`
- `day-11---build-agents-that-dont-go-rogue.md`
- `eddie-the-eval-and-the-fools-gold-framework.md`

Secondary:

- `vibe-to-learn-not-to-earn.md`
- `weekend-at-lennys---part-1.md`

## Key concepts

- Prototype humility
- Product validation vs technical validation
- What was proven
- What was not proven
- Shortcuts taken
- AI-generated code risk
- Data/security limitations
- Engineering review
- Rebuild/refactor/discard decision

## Suggested workflow

1. Identify prototype purpose.
2. Summarize what was built.
3. State what was learned.
4. State what was not validated.
5. List assumptions.
6. List shortcuts.
7. Identify data/security/privacy/compliance concerns, if any.
8. Identify technical unknowns.
9. Identify user evidence.
10. Recommend rebuild/refactor/discard/continue learning.
11. Produce engineering handoff.

## Output artifact

```markdown
# Prototype-to-Production Handoff

## 1. Prototype Summary

## 2. Original Learning Goal

## 3. What the Prototype Proved

## 4. What the Prototype Did Not Prove

## 5. User / Stakeholder Evidence

## 6. Assumptions Still Untested

## 7. Shortcuts Taken

## 8. AI-Generated or Unknown Code Risks

## 9. Data / Security / Privacy / Compliance Notes

## 10. Technical Unknowns

## 11. Product Questions Remaining

## 12. Engineering Review Needed

## 13. Recommended Path
- Rebuild
- Refactor
- Discard
- Continue learning
- Productize after review

## 14. Handoff Brief
```

## Common pitfalls

- “Just clean this up.”
- Shipping prototype code because it demos well.
- Forgetting to document what the prototype did not prove.
- Hiding generated-code uncertainty.
- Handing engineering a pile of vibe-coded artifacts without context.
- Confusing validation evidence with implementation readiness.

---

# Skill 9: `ai-product-builder-playbook`

## Type

Workflow

## Priority

P0 as release flagship, but implement last.

## Purpose

Guide PMs from AI-shaped product idea to disciplined prototype path, guardrails, eval thinking, and handoff plan.

## Core thesis

The AI-era PM builder is not defined by coding ability. They are defined by the ability to turn judgment into evidence quickly.

## Source posts to use

Primary:

- `wth-is-a-product-builder.md`
- `ai-first-is-cute-ai-shaped-is-survival-5-ai-pm-skills-2026.md`
- `vibe-first-validate-fast-verify-fit.md`
- `the-vibe-code-deluge.md`
- `no-ai-wont-replace-your-job.md`
- `organizing-on-ai.md`

Secondary:

- `vibe-to-learn-not-to-earn.md`
- `weekend-at-lennys---part-1.md`
- `the-coming-vibe-app-collapse.md`

## Composition

This workflow should compose or reference:

1. `ai-product-sense`
2. `ai-feature-or-not`
3. `prototype-learning-plan`
4. `vibe-coding-guardrails`
5. `ai-evals-for-product-managers`
6. `prototype-to-production-handoff`

It should optionally invoke `product-sense-red-team` before or after prototype planning.

## Suggested workflow

1. Sense: clarify user, problem, behavior change, and evidence standard.
2. Decide: determine whether AI belongs.
3. Learn: define prototype learning plan.
4. Guardrail: classify build and define boundaries.
5. Build brief: generate instructions for a builder tool or engineering partner.
6. Evaluate: define what “good enough” means.
7. Red-team: stress-test the plan.
8. Handoff: decide what happens after the prototype.

## Output artifact

```markdown
# AI Product Builder Playbook

## 1. Product Sense Summary

## 2. AI Feature Decision

## 3. Prototype Learning Plan

## 4. Guardrails

## 5. Builder Brief

## 6. Eval / Quality Plan

## 7. Red-Team Findings

## 8. Handoff Path

## 9. Recommended Next Move
```

## Builder brief format

```markdown
# Builder Brief

## Goal

## User / Situation

## Problem to Demonstrate

## What to Build

## What Not to Build

## Required Inputs

## Required Outputs

## Constraints

## Data Rules

## UX Notes

## Evaluation Criteria

## Timebox

## Disposal / Handoff Plan
```

## Common pitfalls

- Building before product sense.
- Treating code output as learning.
- Skipping AI necessity decision.
- Generating a fancy demo with no evidence plan.
- Letting the prototype become the roadmap.
- Failing to define what happens after the build.

---

# Commands

## Command 1: `sharpen-product-sense`

## Purpose

Stress-test whether an AI or product idea deserves more investment before build momentum takes over.

## Orchestration

```text
ai-product-sense
-> ai-feature-or-not
-> product-sense-red-team
-> prototype-learning-plan
```

## Output

```markdown
# Sharpen Product Sense Output

## Product Judgment Assessment

## AI Necessity Decision

## Strongest Opportunity Framing

## Riskiest Assumption

## Red-Team Findings

## Evidence Plan

## Recommended Next Action
```

## Command 2: `build-with-judgment`

## Purpose

Move from product idea to AI-assisted prototype without confusing velocity with evidence.

## Orchestration

```text
ai-product-sense
-> ai-feature-or-not
-> prototype-learning-plan
-> vibe-coding-guardrails
-> ai-product-builder-playbook
-> prototype-to-production-handoff
```

## Output

```markdown
# Build With Judgment Output

## Product Sense Summary

## AI Decision

## Prototype Learning Plan

## Guardrails

## Builder Brief

## Validation / Eval Plan

## Handoff Path
```

## Command 3: `define-agentic-product`

## Purpose

Define agent behavior, boundaries, quality standards, and handoff requirements before implementation.

## Orchestration

```text
ai-feature-or-not
-> ai-agent-requirements
-> ai-evals-for-product-managers
-> prototype-to-production-handoff
```

## Output

```markdown
# Define Agentic Product Output

## AI / Agent Necessity Decision

## Agent Delegation Contract

## Eval Plan

## Failure Modes

## Human Checkpoints

## Observability Requirements

## Handoff Requirements
```

---

# Catalog and docs updates

Update generated or source docs according to repo conventions. Do not hand-edit generated files if repo scripts regenerate them.

Likely required updates:

- `skills/<new-skill>/SKILL.md` for each skill
- `commands/<new-command>.md` for each command
- release note under `docs/announcements/`
- README update for v0.80
- catalog regeneration through repo scripts
- version badge or version metadata if repo uses it
- AI PM pack or themed release pack configuration if repo has pack definitions

Do not guess pack behavior. Inspect scripts and release docs.

## Suggested release note file

```text
docs/announcements/2026-XX-XX-v0-80-ai-product-builder-track.md
```

Use the actual release date when known.

## Suggested release note outline

```markdown
# v0.80 — AI Product Builder Track

## Build faster without outsourcing judgment

AI has made it easier for product managers to create prototypes, workflows, demos, and agentic product concepts. That does not mean every PM should build more things faster. It means product judgment matters more because bad assumptions now become plausible artifacts almost instantly.

v0.80 adds a coherent AI Product Builder Track for PMs who need to evaluate AI ideas, decide whether AI belongs, prototype to learn, define agent boundaries, evaluate AI quality, and hand off evidence without pretending a demo is a product.

## What shipped

- ai-product-sense
- ai-feature-or-not
- prototype-learning-plan
- vibe-coding-guardrails
- ai-agent-requirements
- ai-evals-for-product-managers
- product-sense-red-team
- prototype-to-production-handoff
- ai-product-builder-playbook

## New commands

- sharpen-product-sense
- build-with-judgment
- define-agentic-product

## Why it matters

When everyone can build, product sense becomes the differentiator. These skills help PMs build faster, think harder, and ship less nonsense.
```

---

# Implementation checklist

## Phase 0 — Inspect repository

- [ ] Create branch: `v0.80-ai-product-builder-track` or similar.
- [ ] Read `README.md`.
- [ ] Read `AGENTS.md`.
- [ ] Read `CONTRIBUTING.md`.
- [ ] Read skill examples by type.
- [ ] Read existing commands.
- [ ] Inspect validation scripts.
- [ ] Inspect catalog generation scripts.
- [ ] Inspect release packaging scripts.

## Phase 1 — Create shared principles

- [ ] Add shared principles file if repo structure supports it.
- [ ] If not supported, embed principles inside relevant skill bodies.
- [ ] Ensure all references are relative and valid.

## Phase 2 — Create primitive skills

- [ ] Add `ai-product-sense`.
- [ ] Add `ai-feature-or-not`.
- [ ] Add `prototype-learning-plan`.
- [ ] Add `vibe-coding-guardrails`.
- [ ] Add `ai-agent-requirements`.
- [ ] Add `ai-evals-for-product-managers`.
- [ ] Add `product-sense-red-team`.
- [ ] Add `prototype-to-production-handoff`.

## Phase 3 — Create orchestration skill

- [ ] Add `ai-product-builder-playbook`.
- [ ] Ensure it references child skills without duplicating them excessively.
- [ ] Ensure it can still stand alone if invoked directly.

## Phase 4 — Create commands

- [ ] Add `sharpen-product-sense`.
- [ ] Add `build-with-judgment`.
- [ ] Add `define-agentic-product`.
- [ ] Follow existing command metadata/schema.
- [ ] Ensure command names and used skills are cataloged.

## Phase 5 — Validate

Run repo validation commands according to current scripts. Likely commands include some combination of:

```bash
./scripts/test-library.sh
./scripts/generate-catalog.py
./scripts/check-skill-triggers.py --show-cases
./scripts/build-release.sh
```

Do not assume exact commands; inspect scripts first.

## Phase 6 — Review quality

For each skill:

- [ ] Frontmatter is valid.
- [ ] Folder name matches skill name.
- [ ] Description is trigger-oriented.
- [ ] Type matches repo taxonomy.
- [ ] Purpose is clear.
- [ ] Key concepts are teachable.
- [ ] Workflow is executable.
- [ ] Output artifact is concrete.
- [ ] Examples show reasoning.
- [ ] Common pitfalls are specific.
- [ ] No Productside customer material appears.
- [ ] No customer-derived examples appear.
- [ ] No generated `dist/` files are hand-edited.
- [ ] All relative links resolve.
- [ ] Validation passes.

## Phase 7 — Smoke-test prompts

Run one smoke-test prompt per skill. Suggested prompts:

### `ai-product-sense`

```text
We want to add an AI assistant to our onboarding flow so users can ask questions. Help me decide if this is a good product idea.
```

### `ai-feature-or-not`

```text
Our CEO wants every dashboard to include an AI summary. Should this be an AI feature or something else?
```

### `prototype-learning-plan`

```text
We think users would trust an AI-generated weekly planning recommendation. Create a prototype learning plan.
```

### `vibe-coding-guardrails`

```text
I built a small internal tool with Cursor that summarizes customer notes and writes next-step recommendations. What guardrails do I need before sharing it with the team?
```

### `ai-agent-requirements`

```text
Define requirements for an agent that monitors incoming support tickets and drafts suggested responses.
```

### `ai-evals-for-product-managers`

```text
Create an eval plan for an AI feature that summarizes user interviews into product insights.
```

### `product-sense-red-team`

```text
Red-team this idea: an AI copilot that tells PMs what features to build next based on Jira, Slack, and customer calls.
```

### `prototype-to-production-handoff`

```text
I built a prototype that classifies feedback themes from interview notes. Create an engineering handoff.
```

### `ai-product-builder-playbook`

```text
I want to test whether PMs would use an AI tool that turns messy stakeholder input into an opportunity map. Guide me through the builder playbook.
```

### `sharpen-product-sense`

```text
Sharpen this idea: AI feature prioritization based on customer call transcripts, support tickets, and revenue impact.
```

### `build-with-judgment`

```text
Help me move from idea to prototype for an AI customer-discovery synthesis tool.
```

### `define-agentic-product`

```text
Define an agentic product that watches onboarding analytics, identifies stuck users, and suggests interventions.
```

---

# Quality bar

A v0.80 skill is acceptable only if it:

1. Helps the PM think better, not just produce faster.
2. Makes the judgment behind the artifact visible.
3. Names anti-patterns sharply.
4. Produces a concrete artifact or decision.
5. Avoids AI hype.
6. Avoids customer-derived examples.
7. Can be used by a PM in a real ambiguous situation.
8. Fits the release arc.
9. Works as part of the command layer.
10. Passes repo validation.

## Non-goals

Do not build:

- A generic AI prompt pack.
- A generic vibe-coding guide.
- An engineering tutorial.
- A model-selection guide.
- A customer-specific AI transformation framework.
- A set of skills that only generate documents without coaching.

## Final desired outcome

After implementation, the repo should have a visible v0.80 AI Product Builder Track with:

- 9 new skills
- 3 new commands
- updated catalogs
- updated README/release note
- validation passing
- no customer-derived source material
- a coherent release story

The release should make this point unmistakable:

> When everyone can build, product sense becomes the differentiator.
