---
name: assumption-mapping
argument-hint: "[the idea or plan, and the decision it supports]"
description: "List the assumptions behind an idea and rank them by importance and evidence. Use when a plan feels solid and you need to find the beliefs it rests on before you commit."
intent: >-
  Surface the assumptions hiding inside an idea, a plan, or a business case, sort them into
  desirable, usable, viable, feasible, and ethical risk types, and place each on an importance by
  evidence map so the team tests the few that can sink the idea first. Output is a ranked list
  that feeds the de-risking skills.
type: component
theme: validation-experiments
best_for:
  - "Finding what an idea silently depends on before building or funding it"
  - "Deciding which belief to test first when you cannot test everything"
  - "Turning a confident plan into a short list of testable bets"
  - "Giving a team a shared picture of what is known versus believed"
scenarios:
  - "We're about to commit a quarter to this feature. What are we assuming?"
  - "Which of these 30 beliefs should we test first?"
  - "The business case says 20% attach. What has to be true for that?"
  - "Map the assumptions behind our retrofit migration plan"
estimated_time: "30-60 min"
---

# Assumption Mapping

## Purpose

Find the beliefs your idea silently depends on, rank them, and pick the few worth testing first.

Every plan is a stack of assumptions: *customers have this problem, they'll notice our solution,
they'll pay for it, we can build it, the channel will carry it.* Most are fine. A few can sink the
idea, and the dangerous ones are usually the ones nobody wrote down because they felt like facts.

The sentence to keep in your head: **you don't need to test everything, you need to test the
assumption that would hurt most if it were wrong and that you know least about.**

It sits between discovery and de-risking: [`research-synthesis`](../research-synthesis/SKILL.md)
tells you what you've learned, this skill tells you what you're still taking on faith, and the Define
skills ([`pol-probe-advisor`](../pol-probe-advisor/SKILL.md),
[`derisk-measurement-advisor`](../derisk-measurement-advisor/SKILL.md)) test it.

## Input

**Works best with:** The idea or plan, and the decision it supports (build it, fund it, launch it).

**Also useful:** The business case, the research you have, the customer and segment, and who must
believe the plan for it to go ahead.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill opens by asking what the idea is and what has
to be true for it to work, and builds the list from your answers. Assumptions it adds itself are
tagged as suggestions for you to confirm.

**Example invocations:**
- `Assumption map for the Route Optimizer add-on. Business case says 15% attach in year one.`
- `What are we assuming in the NFA-500 migration plan? Decision: fund the bracket kit.`

---

## Key Concepts

### What an Assumption Is

A statement you believe that the plan needs to be true, and that you have not verified. **Written as
a testable claim**, not a worry: "Dispatchers will try the optimizer without a training session,"
not "adoption might be hard."

### Five Kinds of Risk

Sort each assumption by the kind of way the idea could fail:

| Type | The question | Example |
|---|---|---|
| **Desirable** | Do customers want it, and does it solve a problem they feel? | Dispatchers feel the rescheduling pain weekly |
| **Usable** | Can they actually use it without help? | A dispatcher can optimize a day in under five minutes |
| **Viable** | Does it work for the business: revenue, cost, channel, legal? | Resellers will sell an add-on for a 15% margin |
| **Feasible** | Can we build and run it? | Routing runs under two seconds at peak load |
| **Ethical** | Could it cause harm or break trust? | Technician location data is acceptable to technicians |

Four of these come from the common product-risk framing (value, usability, viability, feasibility).
The fifth is added here because AI and location-data products fail on it, and nobody writes it
down. See [`recommendation-canvas`](../recommendation-canvas/SKILL.md) and
[`lean-ux-canvas`](../lean-ux-canvas/SKILL.md) for related framings.

### Generating Them: Ask "What Would Have to Be True?"

Walk the idea as a story, from first contact to payment to long-term use, and at each step ask what
has to be true. Do it by role (the user, the buyer, the person who builds it, the partner who
sells it) because each sees different risks. Include the **boring** ones (a team will actually
have time to do this; legal will approve). Boring assumptions sink more ideas than clever ones.

### Importance by Evidence

Place each assumption on two axes:

- **Importance:** if this is wrong, does the idea fail? (high = it does)
- **Evidence:** what do we actually have? (strong = observed or measured; weak = opinion)

| | **Strong evidence** | **Weak evidence** |
|---|---|---|
| **High importance** | Monitor. You know enough. | **Test first.** This is the leap of faith. |
| **Low importance** | Ignore | Park it. Revisit if the idea changes. |

The top-right cell is the work. Everything else is either known or doesn't matter yet.

### Evidence Is What Happened, Not What Was Said

Rank evidence by how close it is to real behavior: observed behavior and paid usage beat stated
intent, which beats expert opinion, which beats your own conviction. "Everyone I talked to loved it"
is weak evidence unless they paid, scheduled, or did something that cost them. Label what you hold as
Fact, Inference, or Assumption, as in [`autonomous-investigation`](../autonomous-investigation/SKILL.md).

### Pick the Few, and Name What Would Change Your Mind

For each top assumption, state the **kill condition**: what result would make you change or stop.
Without it, the test only reassures. Then hand the top two or three to a test:
[`pol-probe-advisor`](../pol-probe-advisor/SKILL.md) for a proof-of-life probe,
[`derisk-measurement-advisor`](../derisk-measurement-advisor/SKILL.md) for how to measure it.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally. Assumption mapping works well as a short team workshop: individuals
write assumptions alone first, then the group places them.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not a risk register.** Risks are worries; assumptions are testable claims the plan needs.
- **Not a test plan.** It chooses what to test. The Define skills design the test.
- **Not a verdict on the idea.** It shows what's unproven, not that the idea is wrong.
- **Not a list of everything.** Thirty assumptions ranked is useful; a hundred is noise.

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** Artifact first: the assumptions table, the map, the top three with kill
conditions. Commentary short, after. Tag each assumption `[FROM YOU]`, `[RESEARCH]`, or
`[AI-SUGGESTED, VALIDATE THIS]`, and record evidence only if you can name it. Evidence you can't
point to is "none."

**If the PM brings a list, critique first.** Are they testable claims or worries? Is every risk type
represented, or only desirability? Are the boring ones present? Is evidence behavior or opinion?
Name gaps; offer rewrites last.

### Step 1: Frame the Idea and the Decision
What the idea is, who it is for, and what decision it supports. The decision sets how much evidence
is enough.

### Step 2: Generate Assumptions
Walk the story by role, asking what must be true. Include boring ones. Write each as a testable
claim and tag its risk type.

### Step 3: Rate Importance and Evidence
For each, mark importance (does the idea fail if wrong?) and evidence (what do we actually hold,
named). Be harsh on evidence: opinion is weak.

### Step 4: Map and Choose
Place on the map. Pick the high-importance, weak-evidence assumptions. Choose the top two or three,
and write a kill condition for each.

### Step 5: Hand Off and Hand Back
Point each top assumption to a test skill. Close with a short summary (supplied, inferred,
unknown) and a numbered ladder, evidence-favored first, labeled `(Recommended)`: probe the top
assumption this week; gather evidence for two more before deciding; run the map as a team workshop;
or stop if a top assumption already looks fatal.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight Route Optimizer, SaaS) and
[`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield NFA-500 migration).
Both show the boring assumption being the one that matters.

---

## Common Pitfalls

### Pitfall 1: Only Desirability
**Symptom:** Every assumption is "customers will want it."
**Consequence:** The idea passes a demand test and dies on cost, channel, or legal.
**Fix:** Walk all five risk types by role.

### Pitfall 2: Worries Instead of Claims
**Symptom:** "Adoption might be hard."
**Consequence:** Nothing to test and no way to know when it's settled.
**Fix:** Restate as a testable claim with a threshold.

### Pitfall 3: Opinion Counted as Evidence
**Symptom:** "Strong evidence: the team is convinced."
**Consequence:** The riskiest belief looks safe.
**Fix:** Evidence is behavior or data you can name. Otherwise it's none.

### Pitfall 4: Testing What's Easy
**Symptom:** The team tests the cheap assumption, not the dangerous one.
**Consequence:** Progress that changes no decision.
**Fix:** Test the high-importance, weak-evidence one first.

### Pitfall 5: No Kill Condition
**Symptom:** The test has no result that would change the plan.
**Consequence:** It only ever reassures.
**Fix:** Write what result stops or changes the idea before running it.

### Pitfall 6: Skipping the Boring Ones
**Symptom:** No assumptions about capacity, legal, support, or sales readiness.
**Consequence:** The idea fails on the item nobody listed.
**Fix:** Ask each role what must be true for them.

---

## References

### Skill Files
- [`template.md`](template.md): assumptions table, map, top three with kill conditions
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`research-synthesis`](../research-synthesis/SKILL.md): upstream; what you've learned
- [`opportunity-solution-tree`](../opportunity-solution-tree/SKILL.md): where assumptions about solutions get tested
- [`pol-probe-advisor`](../pol-probe-advisor/SKILL.md) and [`pol-probe`](../pol-probe/SKILL.md): test an assumption cheaply
- [`derisk-measurement-advisor`](../derisk-measurement-advisor/SKILL.md): how to measure it
- [`lean-ux-canvas`](../lean-ux-canvas/SKILL.md) and [`recommendation-canvas`](../recommendation-canvas/SKILL.md): related framings
- [`epic-hypothesis`](../epic-hypothesis/SKILL.md): turn the chosen assumption into a hypothesis
- [`autonomous-investigation`](../autonomous-investigation/SKILL.md): Fact / Inference / Assumption vocabulary
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Assumption mapping, leap-of-faith assumptions:** Eric Ries, *The Lean Startup*; David J. Bland and Alex Osterwalder, *Testing Business Ideas*.
- **Four product risks:** Marty Cagan, *Inspired*.
- **Importance by evidence:** a widely used 2x2 in lean product practice.

### Provenance
Distilled from practitioner experience running assumption workshops and de-risking plans.
