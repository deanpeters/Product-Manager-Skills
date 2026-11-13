# Product Requirements Document (PRD)

##### **Document Instructions:**

> This Product Requirements Document (PRD) is a **communications and alignment device.** It serves as a **bridge between strategy and execution** to help teams and stakeholders organise on **shared goals** by focusing on solving **real customer problems**. It serves as a **decision-making guide** to clarify:
>
> - **What** the product must achieve.
> - **Why** it matters to the business and customers.
> - **How** success will be measured.
>
> By structuring decisions around **customer needs** and **market priorities**, the PRD ensures teams work toward **clear, validated outcomes**, avoiding misalignment and wasted effort. It turns abstract ideas into **actionable execution plans**, balancing **innovation with constraints** through structured collaboration.

##### **Document Steps:**

> Each step ensures the PRD remains a **customer-centric, strategic asset**, guiding the team from problem discovery to execution.
>
> 1. **Define the problem space**: Start with customer needs and pain points before exploring solutions.
> 2. **Establish differentiation**: Identify what makes the product unique and why it's worth building.
> 3. **Align with business strategy**: Ensure every requirement ties to measurable outcomes.
> 4. **Quantify success**: Use data-driven success and health metrics to track progress and risks.
> 5. **Plan execution**: Detail user stories and acceptance criteria that prioritise business goals while managing dependencies and constraints.

##### **Tagging Gaps: Assumptions vs. Open Questions**

> As you complete each section, tag every gap explicitly. Do not invent facts, data, approvals, or commitments.
>
> - **🔶 Assumption** — You filled this in based on inference, analogy, or incomplete data. It is plausible but unvalidated. Every assumption is a risk until confirmed. *(e.g., "🔶 Assumption: 60% of churned users leave due to onboarding friction — based on exit survey sample of 43 respondents, not full-cohort analysis.")*
> - **🔵 Open Question** — You don't know this yet and need to find out. The answer requires discovery, a stakeholder conversation, or data you don't have. *(e.g., "🔵 Open Question: What is the current baseline for time-to-first-action? Analytics team has not confirmed.")*
>
> Tag inline, right where the gap appears — not just in Section 10. Section 10 collects them, but each section should surface its own unknowns so reviewers see them in context.

##### **Document Activities and Contributing Skills:**

> To make the PRD a **living, decision-making tool**, teams engage in structured exercises that drive clarity, alignment, and measurable outcomes. The skills below are primary inputs — each one feeds a specific section of this document.
>
> | Skill | Primary Input To |
> |---|---|
> | **Problem Framing Canvas** (`problem-framing-canvas`) | Section 2 — Problem Statement |
> | **Problem Statement** (`problem-statement`) | Section 2 — Problem Statement |
> | **Proto-Persona** (`proto-persona`) | Section 3 — Target Users & Personas |
> | **Jobs-to-Be-Done** (`jobs-to-be-done`) | Section 3 — Target Users & Personas |
> | **Customer Journey Map** (`customer-journey-map`) | Section 3 — Target Users & Personas |
> | **TAM/SAM/SOM Calculator** (`tam-sam-som-calculator`) | Section 4 — Strategic Context |
> | **Positioning Statement** (`positioning-statement`) | Section 4 — Strategic Context |
> | **Opportunity Solution Tree** (`opportunity-solution-tree`) | Section 1 — Executive Summary; Section 5 — Solution Overview |
> | **User Story Mapping Workshop** (`user-story-mapping-workshop`) | Section 5 — Solution Overview; Section 7 — User Stories |
> | **PESTEL Analysis** (`pestel-analysis`) | Section 9 — Dependencies & Risks |
> | **Epic Hypothesis** (`epic-hypothesis`) | Section 7 — User Stories & Requirements |
> | **Epic Breakdown Advisor** (`epic-breakdown-advisor`) | Section 7 — User Stories & Requirements |
> | **User Story** (`user-story`) | Section 7 — User Stories & Requirements |
> | **Recommendation Canvas** (`recommendation-canvas`) | Stakeholder alignment (pre-PRD or appendix) |
> | **Stakeholder Mapping** (`stakeholder-mapping`) | Stakeholder alignment (pre-PRD or appendix) |

***

## Document Information

### Authors

[Author 1]

[Author 2]

### Reviewers

- [Reviewer 1]
- [Reviewer 2]

**Date:** [Insert Date]

### Change Log

| Version | Date       | Author          | Change Description     |
|---------|------------|-----------------|------------------------|
| 0.1     | YYYY-MM-DD | [Your Name]     | Initial draft          |
| 0.2     | YYYY-MM-DD | [Reviewer Name] | Feedback incorporated  |
| 1.0     | YYYY-MM-DD | [Approver Name] | Final version approved |

***

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Problem Statement](#2-problem-statement)
3. [Target Users & Personas](#3-target-users--personas)
4. [Strategic Context](#4-strategic-context)
5. [Solution Overview](#5-solution-overview)
6. [Success Metrics](#6-success-metrics)
7. [User Stories & Requirements](#7-user-stories--requirements)
8. [Out of Scope](#8-out-of-scope)
9. [Dependencies & Risks](#9-dependencies--risks)
10. [Open Questions](#10-open-questions)

***

## 1. Executive Summary

*The Elevator Pitch for Skimmers*

##### **Section Instructions:**

> This section provides a **one-paragraph overview** that any stakeholder can read in 30 seconds and understand what you're building, for whom, and why it matters. Write it first to force clarity, but refine it last after all other sections are complete.

##### **Section Steps:**

> 1. **Name the solution**: What are you building?
> 2. **Name the user**: Who is it for?
> 3. **Name the problem**: What does it solve?
> 4. **Name the impact**: What measurable outcome will it produce?

##### **Contributing Skills:**

> - **Opportunity Solution Tree** (`opportunity-solution-tree`): Confirms that the proposed solution ladders up to a validated product outcome and business goal. If the executive summary cannot trace back to the tree, the initiative may not be grounded in a real customer problem.

##### **Section Activities:**

> - **One-Sentence Test**: Can you state the summary in a single sentence using the format below? If not, the scope may be unclear.
> - **Stakeholder Gut-Check**: Read the summary to someone outside the project. If they can't explain it back, simplify.

***

**Format:** "We're building [solution] for [persona] to solve [problem], which will result in [impact]."

- [Write a one-paragraph executive summary *(e.g., "We're building a guided onboarding checklist for non-technical small business owners to solve the problem of 60% drop-off in the first 24 hours due to lack of guidance, which will increase activation rate from 40% to 60% and reduce churn by 10%.")*]

##### **Before moving on — Section 1 → Section 2:**

> Review what you just wrote. The executive summary names a persona, a problem, and an impact. Check:
> - Does the **problem** you named have evidence behind it, or is it an 🔶 Assumption? If assumption, tag it now — Section 2 is where you'll either ground it in data or escalate it to an 🔵 Open Question.
> - Does the **persona** you named match a real customer segment you can describe in detail? If not, Section 3 will expose the gap — be ready for it.
> - Is the **impact** a measurable outcome or a vague aspiration? If vague, Section 6 will force you to name a metric and a target.

***

## 2. Problem Statement

*What Problem Are We Solving?*

##### **Section Instructions:**

> This section frames the **customer problem with evidence**. It ensures alignment by articulating the problem space clearly — who has this problem, what it is, why it's painful, and what data supports it — before jumping to solutions.

##### **Section Steps:**

> 1. **Identify who has the problem**: Describe the specific user or customer segment affected.
> 2. **Articulate the problem**: State what is happening (or not happening) in concrete terms.
> 3. **Explain why it's painful**: Describe the impact on the user's workflow, goals, or experience.
> 4. **Provide evidence**: Include customer quotes, analytics, support tickets, or research findings.

##### **Contributing Skills:**

> - **Problem Statement** (`problem-statement`): Structures the problem using a validated format. Complete this before writing requirements to prevent premature solution bias.
> - **Problem Framing Canvas** (`problem-framing-canvas`): Uses MITRE's Look Inward / Look Outward / Reframe sequence to ensure the team is solving the right problem — not just the first problem that came to mind.
> - **Discovery Process** (`discovery-process`): If you haven't done discovery yet, run this first. A PRD without discovery evidence is a guess dressed up as a plan.

##### **Section Activities:**

> - **Problem Framing Workshop**: Facilitate a session to clearly articulate the problem space before exploring solutions.
> - **Evidence Gathering**: Search for supporting data across customer interviews, analytics dashboards, support tickets, and competitive research.
> - **Problem Validation**: Review the problem statement with customers or customer-facing teams — if they wouldn't nod at it, it needs more work.

***

### Who Has This Problem?

- [Describe the specific user or customer segment affected *(e.g., non-technical small business owners — solopreneurs and teams of 1–10 — who sign up for a SaaS product for the first time)*]

### What Is the Problem?

- [State the problem in concrete, observable terms *(e.g., 60% of users abandon onboarding within the first 24 hours because they don't know what to do first — they see an empty dashboard with no guidance, get overwhelmed by options, and leave)*]

### Why Is It Painful?

- **User impact**: [Describe the consequence for the user *(e.g., wastes 30–60 minutes trying to figure out the product, never reaches the "aha moment," churns before experiencing value)*]
- **Business impact**: [Describe the consequence for the business *(e.g., 60% activation failure drives high churn, low LTV, and poor word-of-mouth)*]

### Evidence

- **Interviews**: [Cite discovery research *(e.g., 8 of 10 churned users said "I didn't know what to do first" — discovery interviews, Feb 2026)*]
- **Analytics**: [Cite product data *(e.g., 60% of signups complete zero actions within 24 hours — Mixpanel, Jan 2026)*]
- **Support signals**: [Cite support data *(e.g., "How do I get started?" is the #1 support question — 350 tickets/month)*]
- **Customer quote**: [Include a verbatim quote *(e.g., "I logged in, saw an empty dashboard, and thought 'now what?' I gave up and went back to my spreadsheet.")*]

##### **Before moving on — Section 2 → Section 3:**

> The problem statement names who has the problem. Check:
> - Is the **"who"** specific enough to build a persona around, or is it a broad category like "small business owners"? Section 3 needs a concrete individual — role, goals, pain points, current behaviour.
> - Does your **evidence** include at least one direct customer quote or data point? If all four evidence slots are empty or tagged 🔶 Assumption, consider running `discovery-interview-prep` before continuing.
> - Does the **business impact** connect to a metric your leadership actually tracks? If not, Section 4 (Strategic Context) will struggle to make the case.

***

## 3. Target Users & Personas

*Who Are We Building For?*

##### **Section Instructions:**

> This section identifies **who the product is for** — their goals, responsibilities, pain points, and current behaviour. It ensures the team builds for a specific person, not an abstraction.

##### **Section Steps:**

> 1. **Define the primary persona**: The person whose problem you are solving. Include their role, goals, pain points, and current behaviour.
> 2. **Define secondary personas** (if applicable): Other users who interact with the product but are not the primary target.
> 3. **Capture jobs-to-be-done**: What functional, emotional, and social jobs is the user trying to accomplish?
> 4. **Validate personas**: Review with customer-facing teams to confirm personas reflect real customer behaviour, not internal assumptions.

##### **Contributing Skills:**

> - **Proto-Persona** (`proto-persona`): Creates a structured persona profile grounded in discovery research. Avoid creating personas from scratch in isolation — anchor them to real customer data.
> - **Jobs-to-Be-Done** (`jobs-to-be-done`): Identifies the functional, emotional, and social jobs customers need to get done, the pains they experience today, and the gains they are seeking. Use this to validate persona definitions.
> - **Customer Journey Map** (`customer-journey-map`): Maps the end-to-end experience to identify where the persona's pain points cluster — useful when the problem spans multiple touchpoints.
> - **Discovery Interview Prep** (`discovery-interview-prep`): Plans Mom Test-style interviews to validate persona assumptions before committing to them.

##### **Section Activities:**

> - **Persona Workshop**: Collaboratively define primary and secondary personas with cross-functional input from sales, UX, and customer success.
> - **JTBD Canvas Session**: Identify pains, gains, and jobs-to-be-done for each primary persona.
> - **Persona Validation**: Refine personas with cross-functional feedback — if sales, support, and UX don't recognise the persona, it's fiction.

***

### Primary Persona

- **Name**: [A realistic individual name — not a job-title placeholder like "Startup Steve"]
- **Role**: [Job title and responsibilities *(e.g., freelance consultant, solopreneur)*]
- **Context**: [Company size, tech savviness, relevant constraints *(e.g., 1-person business, no IT support, uses email and spreadsheets)*]
- **Goals**: [What they are trying to achieve *(e.g., get value from software fast without technical expertise)*]
- **Pain points**: [What makes their current situation difficult *(e.g., overwhelmed by complex UIs, no time to watch tutorials, needs immediate value)*]
- **Current behaviour**: [How they handle the problem today *(e.g., signs up for products, tries for 1 day, churns if not immediately useful)*]

### Secondary Personas (if applicable)

- **Name**: [Realistic individual name]
- **Role**: [Job title and responsibilities *(e.g., owner-operator managing a small team of 5–10)*]
- **Differs from primary**: [Key differences in needs, tolerance, or behaviour *(e.g., more tolerant of complexity, willing to invest setup time, also needs to onboard team members)*]

### Jobs-to-Be-Done

- **Functional job**: [What the user is trying to accomplish *(e.g., set up the product and complete a first meaningful task within 30 minutes)*]
- **Emotional job**: [How the user wants to feel *(e.g., confident that the product is worth the investment, not stupid for not figuring it out)*]
- **Social job**: [How the user wants to be perceived *(e.g., seen by their team as someone who picks good tools)*]

##### **Before moving on — Section 3 → Section 4:**

> The persona and JTBD define who you're building for. Check:
> - Does the **persona's pain point** match the problem you stated in Section 2? If the persona's biggest frustration is something different from Section 2's problem, one of them is wrong.
> - Is the persona **a real customer of your product**, or did you accidentally describe your own team, your PM audience, or a generic archetype? The persona is the person who uses or buys the product — not the person writing this PRD.
> - Are the **jobs-to-be-done** grounded in observed behaviour or inferred? Tag any inferred JTBD as 🔶 Assumption.

***

## 4. Strategic Context

*Why This, Why Now?*

##### **Section Instructions:**

> This section explains the **business case** for the initiative. It connects the product to business goals, market opportunity, competitive landscape, and urgency — ensuring stakeholders understand why this matters and why it can't wait.

##### **Section Steps:**

> 1. **Link to business goals**: Show how this initiative supports company OKRs or strategic priorities.
> 2. **Size the opportunity** (optional): Quantify the addressable market or revenue potential.
> 3. **Assess the competitive landscape**: Identify how competitors address this problem and where the gap is.
> 4. **Explain "why now?"**: Articulate the urgency — what has changed that makes this the right time?

##### **Contributing Skills:**

> - **TAM/SAM/SOM Calculator** (`tam-sam-som-calculator`): Sizes the market opportunity with structured inputs. Use for major initiatives or exec presentations — skip for incremental features.
> - **Positioning Statement** (`positioning-statement`): Geoffrey Moore's template for defining who you serve, what you solve, and how you're different. Use alongside competitive analysis to sharpen differentiation.
> - **Organic Growth Advisor** (`organic-growth-advisor`): McKinsey Growth Pyramid triage — diagnoses whether the growth constraint is in new segments, geographies, channels, or products.

##### **Section Activities:**

> - **Vision Alignment Workshop**: Facilitate a session to clarify how the product aligns with the company's long-term strategy.
> - **Competitive Landscape Review**: Identify how competitors address the same problem and where gaps exist.
> - **Data Scavenger Hunt**: Surface supporting evidence from internal dashboards, annual reports, competitive research, or tools like JIRA.

***

### Business Goals

- **Strategic alignment**: [How this supports company OKRs or strategic priorities *(e.g., "This initiative supports our Q1 OKR: Reduce churn from 15% to 8%. Improving onboarding activation directly impacts retention.")*]
- **Revenue impact**: [Expected impact on revenue, retention, or cost *(e.g., reducing first-week churn by 10% represents $2.4M in recovered annual revenue)*]

### Market Opportunity (optional)

- **TAM**: [Total addressable market *(e.g., 50M small businesses globally)*]
- **SAM**: [Serviceable addressable market *(e.g., 5M using SaaS tools in our category)*]
- **SOM**: [Serviceable obtainable market *(e.g., 500K solopreneurs in target segments)*]

### Competitive Landscape

- **Current alternatives**: [How competitors or substitutes address this problem *(e.g., Competitor A and Competitor B both have guided onboarding. Our lack of guidance is cited as a churn reason in exit surveys.)*]
- **Our gap**: [Where we are weaker or undifferentiated *(e.g., we are the only product in the category that drops users into an empty dashboard with no first-run experience)*]

### Why Now?

- [Articulate the urgency *(e.g., "Churn spiked 15% in Q4. Onboarding is the #1 driver — 60% churn in first 30 days. Fixing this is critical to hitting our retention OKR.")*]

##### **Before moving on — Section 4 → Section 5:**

> Strategic context justifies the investment. Check:
> - Does the **"why now?"** hold up under scrutiny, or is it just "we should have done this a while ago"? If the urgency is manufactured, stakeholders will sense it.
> - Can you draw a straight line from **business goal → problem (Section 2) → persona (Section 3) → this initiative**? If any link is weak, the solution you're about to describe in Section 5 may not be the right one.
> - If you included **TAM/SAM/SOM**, are the numbers sourced or estimated? Tag estimated figures as 🔶 Assumption.

***

## 5. Solution Overview

*What Are We Building?*

##### **Section Instructions:**

> This section describes the **proposed solution at a high level** — enough for stakeholders to understand what the product will do and how it works, without prescribing UI details or implementation specifics. Keep it high-level. Let design own the UI.

##### **Section Steps:**

> 1. **Write a solution description**: 2–3 paragraphs explaining what the product does and how.
> 2. **List key features**: The capabilities the solution provides.
> 3. **Add user flows or wireframes** (optional): Visual explanation for complex features.
> 4. **Reference the story map** (optional): If the solution has been decomposed into release slices.

##### **Contributing Skills:**

> - **Opportunity Solution Tree** (`opportunity-solution-tree`): Generates opportunities and solutions, then recommends the best proof-of-concept to test first. Use as a cross-check — the solution described here should trace back to a validated opportunity on the tree.
> - **User Story Mapping Workshop** (`user-story-mapping-workshop`): Decomposes the solution into activities, steps, and details to identify release slices. Use for complex features with multiple delivery phases.

##### **Section Activities:**

> - **Solution Sketch Session**: Collaboratively sketch the solution with design and engineering — whiteboard-level, not pixel-level.
> - **Story Mapping Workshop**: Decompose the solution into a user activity map to identify the thinnest viable slice for the first release.
> - **Feasibility Check**: Review the proposed solution with engineering to surface constraints, dependencies, or technical risks early.

***

### Solution Description

- [Write a high-level description of what you're building and how it works *(e.g., "We're building a guided onboarding checklist that walks new users through core workflows step-by-step when they first log in. A modal appears on first login showing 3 steps: Create your first project, Invite a teammate (optional), Complete a sample task. As each step is completed, the checklist updates with checkmarks and a progress bar.")*]

### Key Features

- [Feature 1 *(e.g., "Minimal: Only 3 core steps — not overwhelming")*]
- [Feature 2 *(e.g., "Dismissible: Users can skip if they prefer to explore")*]
- [Feature 3 *(e.g., "Progress tracking: Visual progress bar showing 1/3, 2/3, 3/3")*]
- [Feature 4 *(e.g., "Celebration: Positive reinforcement modal on completion")*]

### User Flows / Wireframes (optional)

- [Link to or embed user flow diagrams, wireframes, or sketches]

### Story Map (optional)

- [Link to story map output from `user-story-mapping-workshop`]

##### **Before moving on — Section 5 → Section 6:**

> The solution overview describes what you're building. Check:
> - Does every **key feature** trace back to a pain point in Section 2 or a job-to-be-done in Section 3? A feature that doesn't solve a stated problem is scope creep — move it to Section 8 (Out of Scope) or justify why it's here.
> - Is the solution **high-level enough** for this stage? If you've specified button labels, pixel dimensions, or implementation details, you've gone too far — pull back and let design own the UI.
> - Can you name a **metric that will move** if this solution works? If not, Section 6 will be difficult — and that's a signal the solution may not be focused enough.

***

## 6. Success Metrics

*How Will We Know It Worked?*

##### **Section Instructions:**

> This section defines **how success will be measured** — the primary metric you're optimising for, secondary metrics you're monitoring, and guardrail metrics that must not regress. Without this section, you cannot validate whether the feature succeeded.

##### **Section Steps:**

> 1. **Define the primary metric**: The ONE metric this feature must move. If you can't name one, the initiative isn't focused enough.
> 2. **Define secondary metrics**: Additional indicators of success that you'll monitor but not optimise for.
> 3. **Define guardrail metrics**: Metrics that should NOT get worse as a result of this initiative.
> 4. **Set targets**: For each metric, state the current baseline and the target.

##### **Contributing Skills:**

> - **Business Health Diagnostic** (`business-health-diagnostic`): Diagnoses SaaS health across growth, retention, efficiency, and capital. Use to identify which metrics are already underperforming and should be tracked.
> - **Feature Investment Advisor** (`feature-investment-advisor`): Build/don't-build recommendation using revenue impact, cost, ROI, and strategic value. Use to validate that the expected metric impact justifies the investment.
> - **SaaS Revenue Growth Metrics** (`saas-revenue-growth-metrics`): Reference for selecting the right growth and retention metrics.

##### **Section Activities:**

> - **Metric Selection Workshop**: Align with analytics and leadership on which metrics matter most and what targets are realistic.
> - **Instrumentation Planning**: Define how each metric will be tracked, what events need to be instrumented, and which tools will be used.
> - **Baseline Measurement**: Confirm current values for all metrics before development begins — you cannot measure improvement without a baseline.

***

### Primary Metric

- **Metric**: [The ONE metric you're optimising for *(e.g., activation rate — % of users completing first action within 24 hours)*]
- **Current**: [Baseline value *(e.g., 40%)*]
- **Target**: [Goal value *(e.g., 60%)*]
- **Timeline**: [When you'll measure *(e.g., 30 days after launch)*]

### Secondary Metrics

- [Metric 2 *(e.g., time-to-first-action: reduce from 3 days to 1 day)*]
- [Metric 3 *(e.g., onboarding checklist completion rate: target 80%)*]
- [Metric 4 *(e.g., support ticket volume for "How do I get started?": reduce from 350/month to 175/month)*]

### Guardrail Metrics

- [Metric that must NOT regress *(e.g., sign-up conversion rate: maintain at 10% — don't add friction to the signup flow)*]

##### **Before moving on — Section 6 → Section 7:**

> Success metrics define how you'll know the solution worked. Check:
> - Does the **primary metric** directly measure the problem from Section 2? If the problem is "users don't know what to do first" and the primary metric is "page views," there's a disconnect.
> - Do you have a **current baseline** for every metric, or are baselines tagged 🔶 Assumption? Without a baseline, you cannot measure improvement — flag this for the analytics team now, not after launch.
> - Is there at least one **guardrail metric**? Every initiative has side effects. If you can't name one thing that shouldn't get worse, you haven't thought about trade-offs.

***

## 7. User Stories & Requirements

*What Exactly Are We Delivering?*

##### **Section Instructions:**

> This section breaks the solution into **user stories with acceptance criteria** that engineering can act on. It starts with an epic hypothesis — a testable statement linking the feature to the expected outcome — and then decomposes the work into deliverable stories.

##### **Section Steps:**

> 1. **Write the epic hypothesis**: A testable statement linking what you're building to the expected outcome.
> 2. **Break down the epic**: Use splitting patterns to decompose the epic into stories sized for delivery.
> 3. **Write user stories**: Each story in "As a / I want / So that" format with acceptance criteria.
> 4. **Document constraints and edge cases**: Technical limitations, browser support, error states, and boundary conditions.

##### **Contributing Skills:**

> - **Epic Hypothesis** (`epic-hypothesis`): Structures the testable hypothesis that connects the feature to expected outcomes. Write this before breaking down stories.
> - **Epic Breakdown Advisor** (`epic-breakdown-advisor`): Splits large epics using Richard Lawrence's 9 patterns — workflow steps, business rule variations, CRUD operations, etc.
> - **User Story** (`user-story`): Mike Cohn format with Gherkin acceptance criteria and anti-pattern checks.
> - **User Story Splitting** (`user-story-splitting`): Further decomposes stories that are still too large for a single sprint.

##### **Section Activities:**

> - **Epic Hypothesis Workshop**: Collaboratively draft the testable hypothesis with PM, design, and engineering.
> - **Story Breakdown Session**: Use the Epic Breakdown Advisor patterns to split the epic into delivery-sized stories with the full team.
> - **Acceptance Criteria Review**: Review each story's acceptance criteria with engineering and QA to confirm they are testable and unambiguous.
> - **Edge Case Identification**: Walk through failure modes, boundary conditions, and unexpected user behaviour.

***

### Epic Hypothesis

- [Write the testable hypothesis *(e.g., "We believe that adding a guided onboarding checklist for non-technical users will increase activation rate from 40% to 60% because users currently drop off due to lack of guidance. We'll measure success by activation rate 30 days post-launch.")*]

### User Stories

**Story 1: [Short title]**

As a [persona], I want [capability], so that [outcome].

**Acceptance Criteria:**

- [ ] [Testable criterion *(e.g., when user logs in for the first time, modal appears with checklist)*]
- [ ] [Testable criterion *(e.g., checklist shows 3 steps: "Create project," "Invite teammate," "Complete task")*]
- [ ] [Testable criterion *(e.g., modal is dismissible via close button)*]
- [ ] [Testable criterion *(e.g., if dismissed, checklist does not reappear — user preference saved)*]

**Story 2: [Short title]**

As a [persona], I want [capability], so that [outcome].

**Acceptance Criteria:**

- [ ] [Testable criterion]
- [ ] [Testable criterion]
- [ ] [Testable criterion]

**Story 3: [Short title]**

As a [persona], I want [capability], so that [outcome].

**Acceptance Criteria:**

- [ ] [Testable criterion]
- [ ] [Testable criterion]
- [ ] [Testable criterion]

### Constraints & Edge Cases

- **Technical constraints**: [Platform limitations, browser support, performance requirements *(e.g., must work on mobile web; checklist state must persist across sessions)*]
- **Edge cases**: [Boundary conditions and unexpected behaviour *(e.g., what if user completes steps out of order? What if user skips optional steps?)*]

##### **Before moving on — Section 7 → Section 8:**

> User stories break the solution into deliverable work. Check:
> - Does the **epic hypothesis** reference the primary metric from Section 6? If the hypothesis can't be validated against a metric you've already defined, either the metric or the hypothesis needs to change.
> - Do the **acceptance criteria** cover the edge cases, or are edge cases only listed at the bottom? Each story's AC should be testable on its own — QA shouldn't need to read the edge cases section to know what "done" means.
> - Are any stories **too large** for a single sprint? If a story has more than 5–6 acceptance criteria, consider splitting it with `user-story-splitting`.

***

## 8. Out of Scope

*What We Are NOT Building*

##### **Section Instructions:**

> This section explicitly documents **what is excluded** from this initiative and why. Without it, scope creep is inevitable — stakeholders will assume features are included unless you say otherwise.

##### **Section Steps:**

> 1. **List excluded features**: Name specific capabilities that are NOT part of this release.
> 2. **Explain the rationale**: For each exclusion, state why it's not included now.
> 3. **Flag future considerations**: Note which excluded items may be revisited in a later release.

##### **Section Activities:**

> - **Scope Boundary Workshop**: Review the solution overview with stakeholders and explicitly ask "What do you expect this to include?" — the gap between their answer and your plan is your out-of-scope list.
> - **Prioritisation Review**: Use the Prioritization Advisor (`prioritization-advisor`) to validate that excluded items are genuinely lower priority, not just forgotten.

***

### Not Included in This Release

- [Excluded feature + rationale *(e.g., "Advanced onboarding personalisation — different checklists per persona. Adds complexity; test the simple version first.")*]
- [Excluded feature + rationale *(e.g., "Video tutorials embedded in checklist. Resource-intensive; validate the checklist concept first.")*]
- [Excluded feature + rationale *(e.g., "Gamification — badges, points. Nice-to-have; focus on core workflow guidance.")*]

### Future Considerations

- [Items that may be revisited *(e.g., "Mobile-optimised onboarding — desktop-first for now, mobile in a future release.")*]

##### **Before moving on — Section 8 → Section 9:**

> Out of scope defines what you're NOT building. Check:
> - Did stakeholders **actually ask for** any of the excluded items, or is this a preemptive list? The most valuable out-of-scope entries are the ones someone will be disappointed about — those need the strongest rationale.
> - Are any excluded items actually **dependencies in disguise**? If "mobile support" is out of scope but 40% of your persona's usage is mobile, that's a risk for Section 9, not just a scope boundary.
> - Does the out-of-scope list **match the solution overview** in Section 5? Features mentioned in Section 5 should not also appear here. Features NOT mentioned in Section 5 but expected by stakeholders should appear here.

***

## 9. Dependencies & Risks

*What Could Go Wrong, and What Do We Need?*

##### **Section Instructions:**

> This section identifies **dependencies** that must be in place before or during execution, and **risks** that could derail the initiative. For each risk, define a mitigation strategy.

##### **Section Steps:**

> 1. **Map technical dependencies**: Platform upgrades, API changes, infrastructure requirements.
> 2. **Map external dependencies**: Third-party integrations, partnerships, vendor timelines.
> 3. **Map team dependencies**: Design handoffs, data pipeline work, cross-team coordination.
> 4. **Identify risks**: What could go wrong? Consider value, usability, feasibility, and viability risks.
> 5. **Define mitigations**: For each risk, state a specific, actionable mitigation strategy.

##### **Contributing Skills:**

> - **PESTEL Analysis** (`pestel-analysis`): Surfaces political, economic, social, technological, environmental, and legal risks from the external environment. Use to identify which external factors are most likely to shift during the product lifecycle.
> - **Feature Investment Advisor** (`feature-investment-advisor`): Assesses feasibility and viability risks as part of the build/don't-build recommendation.
> - **POL Probe Advisor** (`pol-probe-advisor`): Recommends which prototype type to run based on your hypothesis and risk level — useful for mitigating value and usability risks cheaply before committing to full build.

##### **Section Activities:**

> - **Dependency Mapping Session**: Walk through the solution with engineering and identify every external system, team, or vendor that must deliver for this initiative to succeed.
> - **Risk Assessment Workshop**: Use Cagan's Four Risks (value, usability, feasibility, viability) as a framework to surface the riskiest assumptions. For each risk, ask: "Can we collapse this with a one-week experiment?"
> - **Mitigation Planning**: For high-priority risks, assign an owner and a concrete next action.

***

### Dependencies

- **Technical**: [Platform or infrastructure requirements *(e.g., no technical dependencies — uses existing modals framework)*]
- **External**: [Third-party integrations or partnerships *(e.g., analytics provider must support custom event tracking for checklist interactions)*]
- **Team**: [Cross-team handoffs *(e.g., design: wireframes for checklist UI, ETA Week 1)*]

### Risks & Mitigations

- **Risk**: [What could go wrong *(e.g., users dismiss the checklist immediately and never see it)*]
  - **Mitigation**: [How you'll address it *(e.g., track dismissal rate; if >50%, iterate on messaging or timing)*]
- **Risk**: [What could go wrong *(e.g., checklist steps are too generic and don't resonate with all personas)*]
  - **Mitigation**: [How you'll address it *(e.g., start with primary persona, personalise later based on usage data)*]

##### **Before moving on — Section 9 → Section 10:**

> Dependencies and risks surface what could block or derail you. Check:
> - Have you accounted for **all four of Cagan's risks** — value (will customers want this?), usability (can they use it?), feasibility (can we build it?), and viability (does the business case hold)? Most PRDs overweight feasibility and underweight value risk.
> - For each risk, is the **mitigation actionable** — with an owner and a trigger? "Monitor closely" is not a mitigation strategy.
> - Do any of your 🔶 Assumptions from earlier sections appear here as risks? They should — an unvalidated assumption IS a risk. If they don't appear, either the assumption is low-stakes (fine) or you've lost track of it (not fine).

***

## 10. Open Questions

*What We Haven't Decided Yet*

##### **Section Instructions:**

> This section captures **unresolved decisions** and **areas requiring further discovery**. Every PRD has open questions — documenting them is a sign of intellectual honesty, not incompleteness. The goal is to make the unknowns visible so they can be resolved deliberately, not accidentally.

##### **Section Steps:**

> 1. **List unresolved decisions**: Questions that need answers before or during development.
> 2. **Assign owners**: Who is responsible for resolving each question?
> 3. **Set deadlines**: When must each question be answered to avoid blocking development?

##### **Section Activities:**

> - **Open Questions Review**: Walk through the list with the team weekly to close items and surface new ones.
> - **Decision Log**: As questions are resolved, move them from this section to a decision log (or inline in the relevant PRD section) with the rationale.

***

| Question | Owner | Deadline | Status |
|----------|-------|----------|--------|
| [Unresolved question *(e.g., should the checklist be mandatory or optional?)*] | [Name] | [Date] | [Open / Resolved] |
| [Unresolved question *(e.g., should we A/B test checklist vs. no checklist?)*] | [Name] | [Date] | [Open / Resolved] |
| [Unresolved question *(e.g., what happens if the user completes steps out of order?)*] | [Name] | [Date] | [Open / Resolved] |

***

## PRD Self-Assessment

*Honest Diagnostics Before You Share This Document*

##### **Section Instructions:**

> Complete this section after finishing all 10 sections above. It turns the PRD from a deliverable into a diagnostic — surfacing where the document is strong, where it's weak, and what must be validated before committing to build. Share this assessment with reviewers alongside the PRD itself.

***

### Strongest Section

- [Name the section you're most confident in and why *(e.g., "Section 2 — Problem Statement. Grounded in 10 discovery interviews and corroborated by support ticket data. The problem is real and well-evidenced.")*]

### Weakest Section

- [Name the section that needs the most work and why *(e.g., "Section 4 — Strategic Context. The TAM/SAM/SOM numbers are rough estimates from a two-year-old analyst report. The 'why now' rationale is compelling internally but hasn't been validated with customers.")*]

### Top Assumptions to Validate

> Collect all 🔶 Assumption tags from throughout the document. List the ones that carry the highest risk if they turn out to be wrong.

| # | Assumption | Section | Risk if Wrong | Proposed Validation |
|---|------------|---------|---------------|---------------------|
| 1 | [Statement tagged 🔶 above] | [Section #] | [What breaks if this is false] | [How to test — interview, data pull, experiment] |
| 2 | [Statement tagged 🔶 above] | [Section #] | [What breaks if this is false] | [How to test] |
| 3 | [Statement tagged 🔶 above] | [Section #] | [What breaks if this is false] | [How to test] |

### Recommended Next Step

- [What is the single most important thing to do before this PRD is ready for stakeholder review? *(e.g., "Run 3 discovery interviews with churned users to validate the onboarding friction assumption before presenting to the leadership team." or "Get baseline metrics from the analytics team for Section 6 — without baselines, we can't set credible targets.")*]

***

*End of PRD Template*
