# product-strategy-session.md

## Purpose
Guide product managers through a comprehensive product strategy session by orchestrating positioning, problem framing, customer discovery, and roadmap planning skills into a cohesive end-to-end process. Use this to move from vague strategic direction to concrete, validated product strategy with clear positioning, target customers, problem statements, and prioritized roadmap—ensuring alignment across stakeholders before committing to execution.

This is not a one-time workshop—it's a repeatable process for establishing or refreshing product strategy, typically spanning 2-4 weeks with multiple touchpoints.

## Key Concepts

### What is a Product Strategy Session?

A product strategy session is a structured, multi-phase process that takes a product from strategic ambiguity to validated direction. It orchestrates:

1. **Positioning & Market Context** — Define who you serve, what problem you solve, and how you're differentiated
2. **Problem Discovery & Validation** — Frame and validate customer problems through research
3. **Solution Exploration** — Generate opportunity solutions and prioritize based on impact
4. **Roadmap Planning** — Sequence epics and releases based on strategy

### Why This Works
- **Structured discovery:** Prevents jumping to solutions before understanding problems
- **Stakeholder alignment:** Creates shared mental model across exec, product, design, engineering
- **Validated strategy:** Tests assumptions before committing resources
- **Executable roadmap:** Connects high-level strategy to concrete work

### Anti-Patterns (What This Is NOT)
- **Not a feature brainstorm:** Strategy sessions frame problems, not just list features
- **Not waterfall planning:** Builds in feedback loops and iteration
- **Not a solo PM exercise:** Requires cross-functional participation

### When to Use This
- Launching a new product or major initiative
- Annual/quarterly strategic planning cycles
- Repositioning an existing product
- Onboarding new product leaders (align on strategy)

### When NOT to Use This
- When strategy is already clear and validated
- For tactical feature additions (no strategic shift needed)
- When you lack executive sponsorship (strategy won't stick)

---

## Application

This workflow orchestrates **6 phases** over **2-4 weeks**, using multiple component and interactive skills.

---

## Phase 1: Positioning & Market Context (Week 1, Days 1-2)

**Goal:** Define target customer, problem space, and differentiation.

### Activities

**1. Run Positioning Workshop**
- **Use:** `positioning-workshop.md` (interactive)
- **Participants:** PM, product leadership, marketing, sales
- **Duration:** 90 minutes
- **Output:** Draft positioning statement

**2. Define Proto-Personas**
- **Use:** `proto-persona.md` (component)
- **Participants:** PM, design, customer-facing teams
- **Duration:** 60 minutes
- **Output:** 1-3 proto-personas (hypothesis-driven)

**3. Map Jobs-to-be-Done**
- **Use:** `jobs-to-be-done.md` (component)
- **Participants:** PM, design
- **Duration:** 60 minutes
- **Output:** JTBD statements for each persona

### Decision Point 1: Do we have enough customer context?

**If YES:** Proceed to Phase 2 (Problem Framing)

**If NO:** Run additional discovery:
- **Use:** `discovery-interview-prep.md` (interactive)
- Schedule 5-10 customer interviews
- Validate positioning assumptions before proceeding
- **Time impact:** +1 week

---

## Phase 2: Problem Framing & Validation (Week 1, Days 3-5)

**Goal:** Frame the core customer problem and validate it's worth solving.

### Activities

**1. Run Problem Framing Canvas**
- **Use:** `problem-framing-canvas.md` (interactive - MITRE)
- **Participants:** PM, design, engineering lead, customer success
- **Duration:** 120 minutes
- **Output:** Refined problem statement + "How Might We" question

**2. Create Formal Problem Statement**
- **Use:** `problem-statement.md` (component)
- **Participants:** PM
- **Duration:** 30 minutes
- **Output:** Structured problem statement for PRD/roadmap

**3. Map Customer Journey (Optional)**
- **Use:** `customer-journey-mapping-workshop.md` (interactive)
- **When to use:** If problem spans multiple touchpoints or phases
- **Participants:** PM, design, customer success
- **Duration:** 90 minutes
- **Output:** Journey map with pain points and opportunities

### Decision Point 2: Is the problem validated?

**If YES:** Proceed to Phase 3 (Solution Exploration)

**If NO:** Run customer discovery interviews:
- **Use:** `discovery-interview-prep.md` (interactive)
- Validate problem hypothesis with 5-10 customers
- Iterate problem statement based on findings
- **Time impact:** +1 week

---

## Phase 3: Solution Exploration (Week 2, Days 1-3)

**Goal:** Generate solution options, prioritize based on feasibility/impact, and select POC.

### Activities

**1. Generate Opportunity Solution Tree**
- **Use:** `opportunity-solution-tree.md` (interactive)
- **Participants:** PM, design, engineering lead
- **Duration:** 90 minutes
- **Output:** 3 opportunities, 3 solutions per opportunity, POC recommendation

**Alternative: Use Lean UX Canvas**
- **Use:** `lean-ux-canvas.md` (interactive)
- **When to use:** If you prefer hypothesis-driven approach over OST
- **Output:** Business problem, hypotheses, experiments

**2. Define Epic Hypotheses**
- **Use:** `epic-hypothesis.md` (component)
- **Participants:** PM
- **Duration:** 60 minutes per epic
- **Output:** Epic hypothesis statements for top 3-5 initiatives

**3. Create User Story Map (Optional)**
- **Use:** `user-story-mapping-workshop.md` (interactive)
- **When to use:** For complex features requiring release planning
- **Participants:** PM, design, engineering
- **Duration:** 120 minutes
- **Output:** Story map with backbone, release slices

### Decision Point 3: Do we need to test solutions before committing?

**If YES (high uncertainty):** Run experiments:
- Design POC experiments per `opportunity-solution-tree.md` output
- Test with 10-20 customers (prototype, concierge, landing page test)
- **Time impact:** +1-2 weeks

**If NO (low uncertainty):** Proceed to Phase 4 (Prioritization)

---

## Phase 4: Prioritization & Roadmap Planning (Week 2, Days 4-5)

**Goal:** Prioritize initiatives and sequence into executable roadmap.

### Activities

**1. Choose Prioritization Framework**
- **Use:** `prioritization-advisor.md` (interactive)
- **Participants:** PM
- **Duration:** 30 minutes
- **Output:** Recommended prioritization framework (RICE, ICE, Value/Effort, etc.)

**2. Score & Prioritize Epics**
- **Use:** Prioritization framework from step 1
- **Participants:** PM, engineering lead, product leadership
- **Duration:** 90 minutes
- **Output:** Ranked backlog of epics

**3. Sequence Roadmap by Release**
- **Participants:** PM, engineering lead
- **Duration:** 60 minutes
- **Output:** Quarterly or release-based roadmap (Q1: Epics A, B; Q2: Epics C, D, E)

**4. Map TAM/SAM/SOM (Optional)**
- **Use:** `tam-sam-som-calculator.md` (interactive)
- **When to use:** For exec presentations, fundraising, or market sizing
- **Participants:** PM, business ops
- **Duration:** 60 minutes
- **Output:** Market size projections with citations

---

## Phase 5: Stakeholder Alignment & Communication (Week 3)

**Goal:** Present strategy to stakeholders, gather feedback, refine.

### Activities

**1. Create Visionary Press Release (Optional)**
- **Use:** `press-release.md` (component)
- **When to use:** For major product launches or exec buy-in
- **Participants:** PM, marketing
- **Duration:** 60 minutes
- **Output:** Amazon Working Backwards-style press release

**2. Present Strategy to Stakeholders**
- **Format:** 60-min presentation covering:
  - Positioning statement (Phase 1)
  - Problem statement (Phase 2)
  - Solution options & prioritization (Phase 3-4)
  - Roadmap (Phase 4)
- **Participants:** Execs, product leadership, key stakeholders
- **Output:** Feedback, open questions, approval to proceed

**3. Refine Based on Feedback**
- **Duration:** 1-2 days
- **Output:** Updated strategy artifacts

---

## Phase 6: Execution Planning (Week 4)

**Goal:** Break epics into user stories, plan first sprint/release.

### Activities

**1. Break Down Top Epic**
- **Use:** `epic-breakdown-advisor.md` (interactive - with Richard Lawrence's 9 patterns)
- **Participants:** PM, design, engineering
- **Duration:** 90 minutes
- **Output:** User stories split by patterns (workflow, CRUD, business rules, etc.)

**2. Write User Stories**
- **Use:** `user-story.md` (component)
- **Participants:** PM
- **Duration:** 30 minutes per story
- **Output:** User stories with acceptance criteria

**3. Plan First Sprint/Release**
- **Participants:** PM, engineering
- **Duration:** 60 minutes
- **Output:** Sprint backlog or release plan

---

## Complete Workflow: End-to-End Summary

```
Week 1:
├─ Day 1-2: Positioning & Market Context
│  ├─ positioning-workshop.md (90 min)
│  ├─ proto-persona.md (60 min)
│  └─ jobs-to-be-done.md (60 min)
│
├─ Day 3-5: Problem Framing & Validation
│  ├─ problem-framing-canvas.md (120 min)
│  ├─ problem-statement.md (30 min)
│  └─ [Optional] customer-journey-mapping-workshop.md (90 min)
│
└─ Decision: Validate problem? (if NO, +1 week discovery)

Week 2:
├─ Day 1-3: Solution Exploration
│  ├─ opportunity-solution-tree.md (90 min)
│  ├─ epic-hypothesis.md (60 min per epic)
│  └─ [Optional] user-story-mapping-workshop.md (120 min)
│
├─ Decision: Test solutions? (if YES, +1-2 weeks experiments)
│
└─ Day 4-5: Prioritization & Roadmap
   ├─ prioritization-advisor.md (30 min)
   ├─ Score & prioritize epics (90 min)
   ├─ Sequence roadmap (60 min)
   └─ [Optional] tam-sam-som-calculator.md (60 min)

Week 3:
└─ Stakeholder Alignment
   ├─ [Optional] press-release.md (60 min)
   ├─ Present strategy (60 min)
   └─ Refine based on feedback (1-2 days)

Week 4:
└─ Execution Planning
   ├─ epic-breakdown-advisor.md (90 min)
   ├─ user-story.md (30 min per story)
   └─ Plan first sprint (60 min)
```

**Total Time Investment:**
- **Minimum:** 2 weeks (no discovery/experiments)
- **Typical:** 3 weeks (includes 1 round of validation)
- **Maximum:** 4-6 weeks (includes discovery interviews + experiments)

---

## Examples

### Example 1: Good Product Strategy Session (SaaS Onboarding Improvement)

**Context:** Existing SaaS product with 60% onboarding drop-off, need strategic approach to retention.

**Phase 1 - Positioning:**
- Ran `positioning-workshop.md`: Defined target = "non-technical small business owners"
- Created proto-personas: "Solo Entrepreneur Sam" (no IT support)
- JTBD: "Help me get value from software fast without technical expertise"

**Phase 2 - Problem Framing:**
- Ran `problem-framing-canvas.md`: Problem = "Users abandon onboarding because jargon-heavy UI and lack guidance"
- Problem statement: "60% of non-technical users drop off in first 24 hours due to overwhelming, unclear onboarding flow"

**Phase 3 - Solution Exploration:**
- Ran `opportunity-solution-tree.md`: Generated 3 opportunities (guidance, simplification, support)
- Selected opportunity: "Lack of onboarding guidance"
- Solutions: Guided checklist, tooltips, email drip, human-assisted onboarding
- POC: Guided checklist (test with prototype)

**Phase 4 - Prioritization:**
- Ran `prioritization-advisor.md`: Recommended RICE (early PMF stage, some data)
- Scored epics: Guided onboarding (RICE: 12,000), In-app help (8,000), Human onboarding (3,000)
- Roadmap: Q1 = Guided onboarding, Q2 = In-app help

**Phase 5 - Alignment:**
- Presented to execs: Problem statement + OST + roadmap
- Feedback: "Can we run experiment before full build?" → Added 2-week prototype test

**Phase 6 - Execution:**
- Ran `epic-breakdown-advisor.md`: Split "Guided onboarding" using workflow pattern
- Stories: R1 = Simple checklist (3 steps), R2 = Progress tracking, R3 = Celebration/gamification
- Planned Sprint 1: Build R1 (simple checklist)

**Outcome:** Clear, validated strategy with executive buy-in and executable roadmap.

---

### Example 2: Bad Product Strategy Session (Skipped Discovery)

**Context:** Startup wants to build mobile app.

**Phase 1 - Positioning:** Skipped (assumed positioning was clear)

**Phase 2 - Problem Framing:** Skipped (jumped to solution: "We need a mobile app")

**Phase 3 - Solution Exploration:** Skipped (already decided on solution)

**Phase 4 - Prioritization:** Built feature list, prioritized by "what's easiest"

**Phase 6 - Execution:** Started building mobile app immediately

**Why this failed:**
- No positioning validation (who is the app for?)
- No problem validation (do customers actually need mobile access?)
- No alternative solutions explored (responsive web? PWA?)
- 3 months later: Mobile app built, low usage, wrong problem solved

**Fix with strategy session:**
- Run positioning workshop: Discovered target = "field workers who can't access desktop"
- Run problem framing: Validated that mobile-first users can't complete workflows on the go
- Run OST: Explored alternatives (mobile app, responsive web, PWA, SMS notifications)
- Run experiments: Tested responsive web first (2 weeks), validated it solved 80% of problem
- Outcome: Built responsive web instead of native app, saved 2 months dev time

---

## Common Pitfalls

### Pitfall 1: Skipping Problem Validation
**Symptom:** Jump from positioning to solution exploration without validating problem

**Consequence:** Build solutions to unvalidated problems

**Fix:** Force decision point after Phase 2: "Is problem validated?" If NO, run discovery interviews.

---

### Pitfall 2: Solo PM Exercise
**Symptom:** PM runs strategy session alone, presents finished strategy to team

**Consequence:** No buy-in, team doesn't understand rationale

**Fix:** Include cross-functional participants in workshops (design, eng, sales, CS)

---

### Pitfall 3: Strategy Session Without Executive Sponsorship
**Symptom:** Run full strategy session, execs don't show up for Phase 5 alignment

**Consequence:** Strategy doesn't get resourced or prioritized

**Fix:** Secure exec commitment upfront; schedule Phase 5 presentation before starting.

---

### Pitfall 4: No Decision Points (Run All Phases Regardless)
**Symptom:** Blindly follow all 6 phases without checking if discovery/experiments are needed

**Consequence:** Waste time on low-uncertainty activities

**Fix:** Use decision points after Phase 2 and Phase 3 to adapt workflow.

---

### Pitfall 5: Strategy Session Becomes Permanent Process
**Symptom:** Team spends 6 weeks in strategy mode, never executes

**Consequence:** Analysis paralysis, no delivery

**Fix:** Time-box strategy session to 2-4 weeks; after Phase 6, move to execution.

---

## References

### Related Skills (Orchestrated by This Workflow)

**Phase 1:**
- `positioning-workshop.md` (interactive)
- `proto-persona.md` (component)
- `jobs-to-be-done.md` (component)

**Phase 2:**
- `problem-framing-canvas.md` (interactive)
- `problem-statement.md` (component)
- `customer-journey-mapping-workshop.md` (interactive, optional)
- `discovery-interview-prep.md` (interactive, if validation needed)

**Phase 3:**
- `opportunity-solution-tree.md` (interactive)
- `lean-ux-canvas.md` (interactive, alternative)
- `epic-hypothesis.md` (component)
- `user-story-mapping-workshop.md` (interactive, optional)

**Phase 4:**
- `prioritization-advisor.md` (interactive)
- `tam-sam-som-calculator.md` (interactive, optional)

**Phase 5:**
- `press-release.md` (component, optional)

**Phase 6:**
- `epic-breakdown-advisor.md` (interactive)
- `user-story.md` (component)

### External Frameworks
- Teresa Torres, *Continuous Discovery Habits* (2021) — Opportunity solution tree framework
- Jeff Gothelf, *Lean UX* (2016) — Hypothesis-driven product development
- Marty Cagan, *Inspired* (2017) — Product discovery process

### Dean's Work
- Productside Blueprint — Strategic product discovery
- [If Dean has strategy session resources, link here]

---

**Skill type:** Workflow
**Suggested filename:** `product-strategy-session.md`
**Suggested placement:** `/skills/workflows/`
**Dependencies:** Orchestrates 15+ component and interactive skills across 6 phases
