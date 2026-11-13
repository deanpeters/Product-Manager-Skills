---
name: pm-skills-navigator
argument-hint: "[the situation on your desk, in a sentence or two]"
description: "Find the right PM skill for the situation on your desk. Use when you don't know where you are in the product lifecycle or which skill in this library to start with."
intent: >-
  Guided triage from a situation to a route. Places the work on the product lifecycle by what is
  validated versus assumed, names the bundle and motion that fits, recommends one to three skills in
  order with a reason each, says plainly when the library has no skill for the need yet, and hands
  over a paste-ready first prompt.
type: interactive
theme: navigation
best_for:
  - "Not knowing which of the library's skills fits the problem on your desk this week"
  - "Checking whether you are about to do a later-phase job (a PRD, a roadmap) before an earlier one is done"
  - "Learning how the library's skills fit together by lifecycle phase"
scenarios:
  - "Leadership wants a feature and I can't tell if we should be framing, testing, or specifying it"
  - "I'm new to this library and want to know where to start for my product"
estimated_time: "5-10 min"
---

# PM Skills Navigator

## Purpose

Get from "here's what's on my desk" to "here's the skill to open first, and why", in about five
minutes. The library has dozens of skills. Most PMs don't need a catalog; they need a place to
start and a sense of what comes next.

The navigator works by finding **where the work is in the product lifecycle**, because the most
common mistake in product work is doing a later job before an earlier one is finished: writing the
PRD for a problem nobody has validated, or prioritizing solutions before the outcome is named. The
phase tells you which skills are premature.

It recommends a route, not a mandate. Every skill it points to runs on its own.

## Input

**Works best with:** The situation on your desk, in a sentence or two: what's happening, and what
you're supposed to produce or decide.

**Also useful:** What you already know for sure versus what you're assuming, who's asking, and how
much time you have.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The first question asks what's on your desk, and the rest
are answerable from what you already know. "I don't know" is a valid answer and becomes a labeled
assumption in the route.

**Example invocations:**
- `Our dispatchers don't use the route optimizer and my VP wants a redesign. Where do I start?`
- `I just joined a product team and don't know which of these skills matters for me.`

---

## Key Concepts

### The Arc

Product work tends to unfold in an order. The library groups its skills by that order:

| Phase (bundle) | The question | You're here when... | You can leave when... |
|---|---|---|---|
| **Determine** | What outcome are we after, and what is the market doing? | You can't state the outcome in a measurable sentence, or the market has moved | You have a measurable outcome and a view of the market and the customer |
| **Discover** | What is the real problem? | You have an outcome but the problem is a guess or a stakeholder's opinion | You have a problem statement backed by evidence from customers |
| **Define** | Is this solution worth building, and how do we position it? | You have a problem but the solution is untested | You have a tested bet worth building and can say who it's for and why you win |
| **Develop** | How do we turn it into buildable work? | The solution is chosen but isn't ready for a team (no PRD, stories, order) | A team can start, and knows what they're building and in what order |
| **Deliver** | How do we price it, take it to market, measure it, and retire it well? | It's built, or it's aging | It's priced and launched, and you can tell whether it worked, or it has been retired cleanly |
| **Drive** | How do I work with people and grow? | The question is about a stakeholder, an incoming request, or your own career | It's handled. This phase runs under all the others |

The same arc shows up in software delivery (plan, analyze, design, build, deploy) and in other
product frameworks. That's the point: it isn't a house opinion, it's how work earns the right to
move forward.

### The Phase Is Set by Evidence, Not by Where You Wish You Were

A team that says "we're in Develop" because a PRD is due, with an unvalidated problem underneath, is
actually in Discover. **Ask what's validated and what's assumed**, and place the work at the
earliest phase whose exit condition isn't met. Calling it later doesn't make it later.

### A Cycle, Not a Line

Work loops back (a failed test sends you to Discover again) and runs concurrently (launch prep
starts while you build). So the navigator:

- **Names two phases when the work straddles them,** and puts the one carrying the highest unresolved
  risk first.
- **Treats Drive as orthogonal.** A question about a stakeholder or your own career gets routed to
  Drive whatever phase the product is in.
- **Never blocks.** If you want a later-phase skill, it says what you're skipping and what that risk
  is, then helps you anyway. Your call.

### Motions: The Smaller Groups Inside a Bundle

Each bundle has motions, which are specific jobs. The map below is the full list. A motion marked
*Coming* has no skill yet. The navigator says so instead of forcing a poor fit.

### Anti-Patterns (what this is NOT)
- **Not a pipeline.** It suggests an order; it doesn't require one. Skip, reorder, or stop after one.
- **Not a gate.** It never refuses to help with a later-phase skill.
- **Not a replacement for the skills.** It points; the skills do the work.
- **Not a catalog.** For a flat list, see `catalog/skills-by-bundle.md`.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol. Give
the heads-up at the start (four questions, about five to ten minutes) and let the user dump context
to skip ahead.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

---

### The Map

This block is generated from `pm-skills.config.yaml`. Don't edit it here; run
`python3 scripts/check-bundles.py --write-navigator`.

<!-- BUNDLE-MAP:START -->
**Determine** (Context): Set outcomes and read the terrain: strategy, finance, market, customers.

- **Direct** (Business and product outcomes, strategy, and the finance behind them): [`product-strategy-session`](../product-strategy-session/SKILL.md), [`organic-growth-advisor`](../organic-growth-advisor/SKILL.md), [`business-health-diagnostic`](../business-health-diagnostic/SKILL.md), [`feature-investment-advisor`](../feature-investment-advisor/SKILL.md), [`finance-metrics-quickref`](../finance-metrics-quickref/SKILL.md), [`saas-economics-efficiency-metrics`](../saas-economics-efficiency-metrics/SKILL.md), [`saas-revenue-growth-metrics`](../saas-revenue-growth-metrics/SKILL.md)
- **Diagnose** (Strategic lenses: SWOT, Porter's, Ansoff, PESTEL, TAM/SAM/SOM): [`ansoff-matrix`](../ansoff-matrix/SKILL.md), [`pestel-analysis`](../pestel-analysis/SKILL.md), [`porters-five-forces`](../porters-five-forces/SKILL.md), [`swot-analysis`](../swot-analysis/SKILL.md), [`tam-sam-som-calculator`](../tam-sam-som-calculator/SKILL.md)
- **Detect** (The market and competitor investigation chain): [`company-intel`](../company-intel/SKILL.md), [`company-research`](../company-research/SKILL.md), [`competitive-analysis-process`](../competitive-analysis-process/SKILL.md), [`competitive-intel-watch`](../competitive-intel-watch/SKILL.md), [`competitive-research-snapshot`](../competitive-research-snapshot/SKILL.md), [`intel-discipline-advisor`](../intel-discipline-advisor/SKILL.md), [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md), [`market-landscape-scan`](../market-landscape-scan/SKILL.md), [`pestel-delta-monitor`](../pestel-delta-monitor/SKILL.md)
- **Describe** (Who the customer is: jobs, personas, voice of customer): [`jobs-to-be-done`](../jobs-to-be-done/SKILL.md), [`proto-persona`](../proto-persona/SKILL.md), [`voice-of-customer-miner`](../voice-of-customer-miner/SKILL.md)

**Discover** (Discover + Investigate): Find and frame the real problem.

- **Drill-down** (Interviews, problem framing, opportunity solution trees, journey maps): [`discovery-interview-prep`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/discovery-interview-prep/SKILL.md), [`discovery-process`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/discovery-process/SKILL.md), [`opportunity-solution-tree`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/opportunity-solution-tree/SKILL.md), [`problem-framing-canvas`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/problem-framing-canvas/SKILL.md), [`problem-statement`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/problem-statement/SKILL.md), [`customer-journey-map`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/customer-journey-map/SKILL.md), [`customer-journey-mapping-workshop`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/customer-journey-mapping-workshop/SKILL.md)
- **Dig** (Collect evidence: surveys, usage data, a steady customer-contact habit): [`survey-design-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/survey-design-advisor/SKILL.md), [`usage-data-investigation`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/usage-data-investigation/SKILL.md), [`discovery-habits-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/discovery-habits-advisor/SKILL.md)
- **Decode** (Make sense of it: synthesis and assumption mapping): [`research-synthesis`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/research-synthesis/SKILL.md), [`assumption-mapping`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/assumption-mapping/SKILL.md)

**Define** (Discover + Define): Shape a solution worth building and test the bet.

- **De-risk** (Hypotheses, probes, experiments, measurement): [`derisk-measurement-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/derisk-measurement-advisor/SKILL.md), [`lean-ux-canvas`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/lean-ux-canvas/SKILL.md), [`pol-probe-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/pol-probe-advisor/SKILL.md), [`pol-probe`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/pol-probe/SKILL.md), [`recommendation-canvas`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/recommendation-canvas/SKILL.md), [`epic-hypothesis`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/epic-hypothesis/SKILL.md)
- **Differentiate** (Positioning and competitive sales tools): [`positioning-statement`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/positioning-statement/SKILL.md), [`positioning-workshop`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/positioning-workshop/SKILL.md), [`battle-card-builder`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/battle-card-builder/SKILL.md)

**Develop** (Create): Turn the chosen solution into buildable work.

- **Document** (PRDs, press releases, storyboards): [`prd-development`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/prd-development/SKILL.md), [`press-release`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/press-release/SKILL.md), [`storyboard`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/storyboard/SKILL.md)
- **Draft** (User stories, splitting, story mapping, epic breakdown): [`user-story`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/user-story/SKILL.md), [`user-story-splitting`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/user-story-splitting/SKILL.md), [`user-story-mapping`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/user-story-mapping/SKILL.md), [`user-story-mapping-workshop`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/user-story-mapping-workshop/SKILL.md), [`epic-breakdown-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/epic-breakdown-advisor/SKILL.md)
- **Decide** (Prioritization and roadmaps): [`prioritization-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/prioritization-advisor/SKILL.md), [`roadmap-planning`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/roadmap-planning/SKILL.md)
- **Delegate** (Work with AI agents: orchestration, context engineering, readiness): [`agent-orchestration-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/agent-orchestration-advisor/SKILL.md), [`ai-shaped-readiness-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/ai-shaped-readiness-advisor/SKILL.md), [`context-engineering-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/context-engineering-advisor/SKILL.md)
- **Drumbeat** (Execution rhythm: backlog refinement, sprint planning, release readiness): [`backlog-refinement-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/backlog-refinement-advisor/SKILL.md), [`sprint-planning`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/sprint-planning/SKILL.md), [`release-readiness`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/release-readiness/SKILL.md)

**Deliver** (Deliver): Take it to market, measure it, and retire it well.

- **Debut** (Launch planning and messaging): [`launch-plan`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/launch-plan/SKILL.md), [`message-house`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/message-house/SKILL.md), [`sales-value-narrative`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/sales-value-narrative/SKILL.md), [`buying-journey-enablement`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/buying-journey-enablement/SKILL.md)
- **Dollars** (Pricing and packaging): [`finance-based-pricing-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/finance-based-pricing-advisor/SKILL.md), [`pricing-packaging-tracker`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/pricing-packaging-tracker/SKILL.md)
- **Demand** (Channels and acquisition): [`acquisition-channel-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/acquisition-channel-advisor/SKILL.md)
- **Dashboard** (Measure outcomes after launch): [`launch-metrics`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/launch-metrics/SKILL.md)
- **Deepen** (Keep customers and grow them: activation and retention): [`activation-design`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/activation-design/SKILL.md), [`retention-diagnostic-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/retention-diagnostic-advisor/SKILL.md)
- **Decommission** (Lifecycle plays through end of life): [`eol-checklist`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/eol-checklist/SKILL.md), [`eol-internal-enablement`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/eol-internal-enablement/SKILL.md), [`eol-message`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/eol-message/SKILL.md), [`eol-process`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/eol-process/SKILL.md), [`eol-readiness-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/eol-readiness-advisor/SKILL.md), [`eol-stakeholder-sequence`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/eol-stakeholder-sequence/SKILL.md), [`lifecycle-play-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/lifecycle-play-advisor/SKILL.md), [`product-lifecycle-plays`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/product-lifecycle-plays/SKILL.md)

**Drive** (Runs under all five phases): Drive your career and your stakeholders.

- **Diplomacy** (Stakeholders, incoming requests, alignment): [`incoming-request-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/incoming-request-advisor/SKILL.md), [`stakeholder-engagement-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/stakeholder-engagement-advisor/SKILL.md), [`stakeholder-identification`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/stakeholder-identification/SKILL.md), [`stakeholder-mapping`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/stakeholder-mapping/SKILL.md)
- **Demystify** (Career ladders, leadership transitions, interviews): [`altitude-horizon-framework`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/altitude-horizon-framework/SKILL.md), [`director-readiness-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/director-readiness-advisor/SKILL.md), [`executive-onboarding-playbook`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/executive-onboarding-playbook/SKILL.md), [`product-sense-interview-answer`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/product-sense-interview-answer/SKILL.md), [`vp-cpo-readiness-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/vp-cpo-readiness-advisor/SKILL.md)
- **Delineate** (Draw the lines: decision rights and the PM role): [`decision-rights-matrix`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/decision-rights-matrix/SKILL.md), [`pm-role-charter`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/pm-role-charter/SKILL.md)

**Core** (shared helpers that ship with every bundle): [`workshop-facilitation`](../workshop-facilitation/SKILL.md), [`pm-skills-navigator`](../pm-skills-navigator/SKILL.md), [`autonomous-investigation`](../autonomous-investigation/SKILL.md), [`pm-skill-creator`](../pm-skill-creator/SKILL.md), [`skill-authoring-workflow`](../skill-authoring-workflow/SKILL.md)
<!-- BUNDLE-MAP:END -->

---

## Application

This skill asks **up to 4 adaptive questions**, then recommends a route with reasons.

---

### Question 1 of 4: What's on your desk?

**Agent asks:**

"What's the situation? Tell me what's happening and what you're expected to produce or decide. One
or two sentences is plenty."

**Listen for the job-to-be-done behind the request.** "Write a PRD" is a deliverable; the situation
underneath (a stakeholder asked for a feature, or discovery found a pattern) decides which phase it
belongs to. If the answer is about people (a stakeholder, a request, your career), note it: that's
Drive, and it can skip Question 2.

---

### Question 2 of 4: What's validated, and what's assumed?

**Agent asks:**

"Let's find where this really stands. Which of these is true today?

1. **We have a measurable outcome we're aiming at** (not just a feature)
2. **We've talked to customers and can state the problem with evidence**
3. **We've tested a solution and it held up**
4. **None of those yet, or I'm not sure**

Pick any that apply."

**Place the work at the earliest phase whose exit condition is unmet:**

| They said | Earliest unmet | Phase |
|---|---|---|
| 4 (none) | The outcome | Determine |
| 1 only | The problem | Discover |
| 1 and 2, not 3 | The solution test | Define |
| 1, 2, and 3 | Buildable work, then market | Develop, then Deliver |

If their situation sounds later than their answers (a PRD is due but they picked 4), say so gently:
the PRD is premature, here's the evidence gap, and here's the smaller job that unblocks it.

---

### Question 3 of 4: What do you need to walk away with?

**Agent asks:**

"What would make this session worth it?

1. **A decision** (which option, build or not, which framework)
2. **An understanding** (what's going on, what customers need, what the market is doing)
3. **A document** (a PRD, stories, a positioning statement, a plan)
4. **Alignment** (getting people on board, handling a request, planning a conversation)"

**Use the answer to pick the motion and the skill type.** A decision usually means an interactive
advisor. An understanding usually means a workflow or an investigation. A document means a component
skill. Alignment means a Drive skill, whatever the phase.

---

### Question 4 of 4: How much time do you have?

**Agent asks:**

"Roughly how long can you give this: under an hour, a few hours, or days?"

**Use it to size the route, and honor an override either way.** Under an hour means one skill, the
quick one. A few hours means two or three in order. Days means the workflow version where one exists.
Name what a shorter route leaves uncovered.

---

### Final Step: Recommend the route

Deliver this structure:

```markdown
## Your Route: [Situation in a few words]

**Where the work is:** [Phase] (and [second phase] if it straddles) — because [what's validated vs assumed]
**Bundle / motion:** [Bundle] → [Motion]

### Start here
1. [`skill`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/skill/SKILL.md): [why this one first, one line]
2. [`skill`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/skill/SKILL.md): [what it adds]
3. [`skill`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/skill/SKILL.md): [optional; what it adds]

**What you're skipping, if anything:** [the earlier-phase job you aren't doing, and the risk]
**Gap, if any:** [a need with no skill yet, and the closest alternative]

### Paste this first
> [A real first prompt using their own details]

### Assumptions I made
- [Anything answered "I don't know"]
```

Then offer numbered next steps:

"Where next?

1. **Run the first skill now**, with the prompt above
2. **See the rest of this phase**, or the phase before or after it
3. **Check what you're skipping**, and go back for it first
4. **Navigate a different problem**

Pick a number, combine them, or tell me what you'd rather do."

---

## Examples

### Example A: SaaS, the PRD is premature

**Fieldlight (field service software).** The PM's VP wants a redesign of the route optimizer
because dispatchers "don't use it."

> **Q1.** "Dispatchers don't use the route optimizer. My VP wants it redesigned. I'm supposed to write the PRD."
>
> **Q2.** Which is true: outcome, problem, tested solution? → "Honestly, none. The VP has an outcome in mind, but nobody has asked a dispatcher why."
>
> **Q3.** What do you walk away with? → "A document, the PRD."
>
> **Q4.** Time? → "A couple of hours."

**Route:** Phase **Discover** (and Develop, where the request is pointing). The PRD is premature: the
problem is an opinion, not a finding.

1. [`problem-framing-canvas`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/problem-framing-canvas/SKILL.md): state the problem before the solution
2. [`discovery-interview-prep`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/discovery-interview-prep/SKILL.md): plan five dispatcher conversations
3. [`prd-development`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/prd-development/SKILL.md): once the problem is evidenced

**What you're skipping:** nothing yet; you're not skipping, you're sequencing. **Paste this first:**
*"Frame this problem: dispatchers 'don't use' the route optimizer, and my VP wants it redesigned."*

The coaching beat: the PRD was the right *deliverable* and the wrong *next step*. Naming it that way
keeps the PM from feeling blocked.

### Example B: Industrial, the work straddles two phases

**Northfield Automation (industrial retrofit controls).** NFA-200 sales have been flat for six
quarters. A distributor asks for a variant; engineering says it's a 14-month cycle.

> **Q1.** "NFA-200 is flat. A big distributor wants a variant. Sales is half-promising it."
>
> **Q2.** → "We have an outcome (hold margin). We don't know if it's the product or the channel."
>
> **Q3.** → "A decision: variant or not?"
>
> **Q4.** → "A week, but it's a big call."

**Route:** Phase **Deliver** (an aging product) and **Define** (the variant is an untested bet).
Highest unresolved risk first: **Deliver**, because nobody has established whether the product is
declining or badly distributed.

1. [`lifecycle-play-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/lifecycle-play-advisor/SKILL.md): is this extend, replace, retire, or nothing yet?
2. [`incoming-request-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/incoming-request-advisor/SKILL.md): decode what the distributor is asking before replying
3. [`pol-probe-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/pol-probe-advisor/SKILL.md): if "extend" wins, test the variant cheaply

**What you're skipping:** a 14-month build commitment on an untested variant. **Paste this first:**
*"Help me decide what to do with NFA-200: sales flat six quarters, a distributor wants a variant."*

The coaching beat: two phases named on purpose. Straddling is normal; what matters is which risk to
retire first.

---

## Common Pitfalls

### Pitfall 1: Placing the Work Where the Deliverable Is

**Symptom:** "A PRD is due, so we're in Develop."
**Consequence:** A polished spec for an unvalidated problem. Looks like progress, builds the wrong
thing well.
**Fix:** Place by evidence: the earliest phase whose exit condition is unmet.

### Pitfall 2: Treating the Route as a Pipeline

**Symptom:** Running all three recommended skills in order because they were listed.
**Consequence:** Process theater. The route is a suggestion; the first skill may be all you need.
**Fix:** Stop when the question is answered. Every skill runs alone.

### Pitfall 3: Forcing a Fit on a Gap

**Symptom:** Recommending a loosely related skill for a need the library doesn't cover yet.
**Consequence:** The PM trusts a template that doesn't fit, and the library loses credibility.
**Fix:** Say "no skill for this yet" and name the closest honest alternative with its limits.

### Pitfall 4: Blocking the Skip

**Symptom:** Refusing to help with a later-phase skill until an earlier one is done.
**Consequence:** Contradicts a cycle that really is concurrent, and the PM stops asking.
**Fix:** Name what's being skipped and the risk, then help anyway.

### Pitfall 5: Routing a People Problem Through the Product Arc

**Symptom:** Sending a stakeholder conflict to Discover.
**Consequence:** Customer research for a problem that's about a person.
**Fix:** Drive runs under every phase. Route people questions there directly.

---

## References

### Related Skills

These stand on their own; none is a prerequisite for this skill, and this skill isn't a prerequisite
for them.

- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): the interaction protocol
- [`lifecycle-play-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/lifecycle-play-advisor/SKILL.md): the product-lifecycle question (extend, replace, retire), not to be confused with the work lifecycle used here
- [`intel-discipline-advisor`](../intel-discipline-advisor/SKILL.md): a deeper navigator for the market-intelligence skills
- [`prioritization-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/prioritization-advisor/SKILL.md): when the question is "which option", not "which skill"

### External Frameworks
- Software development life cycle (plan, analyze, design, build, deploy): the same arc in engineering
- Productside Blueprint: the product lifecycle the phase names are aligned with

### Provenance
- Distilled from practitioner experience teaching the product lifecycle and routing PMs to the right
  tool for the phase they are actually in.
