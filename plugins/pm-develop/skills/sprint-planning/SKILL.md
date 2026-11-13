---
name: sprint-planning
argument-hint: "[the team, the sprint length, and the backlog you're planning from]"
description: "Plan a sprint around a goal, real capacity, and named risks. Use when a team's sprints end with carryover, a pile of unrelated tickets, or a goal nobody can state."
intent: >-
  Run sprint planning as a decision about what the team can commit to and why, not a ticket-filling
  exercise. Starts from a sprint goal, sizes capacity from real availability, selects work that
  serves the goal, holds slack for the unplanned, names the risks and dependencies, and leaves a
  commitment the team believes. Works for software sprints and for hardware or service teams on a
  fixed cadence.
type: workflow
theme: pm-artifacts
best_for:
  - "Planning a sprint around one goal instead of a list of tickets"
  - "Fixing chronic carryover by sizing to real capacity"
  - "Making risks and dependencies visible before the sprint starts"
  - "Teams on a fixed cadence outside pure software (hardware, service, ops)"
scenarios:
  - "Every sprint we carry a third of the work over. Help me plan this one differently"
  - "We have 6 people, two on leave, and 40 tickets. What goes in?"
  - "Write a sprint goal for a sprint that is mostly bug fixes"
  - "Plan a two-week cadence for a hardware firmware team with a supplier dependency"
estimated_time: "30-60 min"
---

# Sprint Planning

## Purpose

Plan one sprint so the team commits to something it can finish and can explain. The output is a
**sprint goal**, a **capacity number built from real availability**, a **selected set of work that
serves the goal**, **slack for the unplanned**, and a short list of **risks and dependencies** with
owners.

The sentence to keep in your head: **a sprint is a commitment to a goal, not a promise to close
tickets.** When the goal is clear, the team can drop a ticket and still succeed. When there is only
a list, every dropped ticket is a failure and every sprint ends in carryover.

The PM's job here is to bring the *why* and the priority. The team owns the *how much*.

## Input

**Works best with:** The team, the sprint length, and the prioritized backlog you're planning from.

**Also useful:** Who is away, last sprint's result and carryover, known dependencies (other teams,
suppliers), and any date the sprint has to land.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill asks about the team, the length, and what
matters most this sprint, builds a goal from your answers, and marks capacity and estimates it
doesn't have as `[NEEDS SOURCE]` for the team to fill. It never sets the team's capacity for them.

**Example invocations:**
- `Plan a 2-week sprint. 6 engineers, 2 on leave for 3 days. Top priority: onboarding drop-off.`
- `Sprint plan for the firmware team. Waiting on a supplier sample. Last sprint carried over 5 of 12.`

---

## Key Concepts

### Goal First

Write the sprint goal **before** picking tickets, as one sentence about an outcome someone outside
the team would recognize: "A dispatcher can optimize a day without help." Then choose work that
serves it. A good goal passes three tests: **specific** (you can tell if it's met), **valuable**
(someone cares), and **flexible** (several ways to get there, so the team can adapt mid-sprint).
A goal like "finish 14 tickets" is a quota, and "improve the product" cannot be failed.

### Capacity From Reality

Capacity is **available focused hours**, not headcount times days. Start with the people, subtract
leave, holidays, recurring meetings, support rotation, and review time, and apply a focus factor
that reflects how much of the rest goes to the sprint work. Use the team's own **recent
completed** work as the check: if the last three sprints finished around 30 units and the plan says
45, the plan is a wish. Let the team set the number. A PM who pushes capacity up is borrowing from
quality.

### Slack Is Not Waste

Every sprint absorbs the unplanned: a production bug, a customer escalation, a blocked ticket,
someone out sick. Plan for it by holding **a share of capacity unallocated** (a common starting
point is 15-20%, adjusted from your history). Teams with no slack hit every surprise as a failure
and teach themselves to stop trusting the plan.

### Work That Serves the Goal, Sized to Fit

Pull from the prioritized backlog only what serves the goal, in priority order, and stop when
capacity (less slack) is reached. Each item should be **ready**: understood, small enough to finish,
and with a clear "done." If it isn't, send it to
[`backlog-refinement-advisor`](../backlog-refinement-advisor/SKILL.md) rather than guessing.
Large items split by thin vertical slices ([`user-story-splitting`](../user-story-splitting/SKILL.md)).

### Risks and Dependencies Are Planned Work

For each dependency (another team, a supplier, an approval) name the **owner**, the **date it's
needed**, and the **fallback** if it slips. A sprint that depends on something nobody owns is a
sprint at risk. Flag these on day one, not on day eight.

### Not Only Software

The rhythm works for hardware, service, and operations teams on a fixed cadence. The items are
different (a firmware build, a supplier test, a commissioning checklist) and the dependencies are
physical (parts, rigs, certification slots), so lead times matter more and slack should be larger.
Carryover is expected where the lead time is real; the goal still sets the direction.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not a status meeting.** It decides what the team commits to.
- **Not estimation by the PM.** The team sizes the work.
- **Not a forecast of the roadmap.** See [`roadmap-planning`](../roadmap-planning/SKILL.md).
- **Not the backlog's priority order.** See [`prioritization-advisor`](../prioritization-advisor/SKILL.md).

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** Artifact first: the goal, capacity, the selected work, slack, risks and
dependencies, and the commitment. Commentary short, after. Mark any capacity figure, estimate, or
availability the team has not supplied as `[NEEDS SOURCE]`. Never set it.

**If the PM brings a plan, critique first.** Is there a goal that is specific, valuable, and
flexible? Is capacity from real availability and recent history? Is there slack? Does every item
serve the goal and carry a definition of done? Does each dependency have an owner and a fallback?
Name gaps; offer rewrites last.

### Step 1: Set the Sprint Goal
Ask what outcome matters most this sprint and write one sentence. Run the three tests.

### Step 2: Build Capacity
People, minus leave and recurring commitments, with a focus factor, checked against the last three
sprints. The team confirms the number.

### Step 3: Hold Slack
Set the unallocated share from history. Say what it will absorb.

### Step 4: Select the Work
From the prioritized backlog, only what serves the goal, until capacity less slack is reached.
Flag items that are not ready. Mark which items are stretch.

### Step 5: Name Risks and Dependencies
Owner, needed-by date, and fallback for each. Name the one thing most likely to break the goal.

### Step 6: Confirm the Commitment and Hand Back
The team states aloud whether it believes the plan. Short summary (supplied, inferred, unknown),
then a numbered ladder, evidence-favored first, labeled `(Recommended)`: drop to the capacity the
last three sprints support; refine two not-ready items before starting; escalate the unowned
dependency; or keep the plan and review carryover on day five.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight onboarding sprint, SaaS) and
[`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield firmware team with a
supplier dependency).

---

## Common Pitfalls

### Pitfall 1: A List Instead of a Goal
**Symptom:** "Complete tickets 101-118."
**Consequence:** Every drop is a failure, and the team can't trade scope for outcome.
**Fix:** One-sentence goal first; tickets serve it.

### Pitfall 2: Capacity From Headcount
**Symptom:** 6 people x 10 days.
**Consequence:** Meetings, leave, and support vanish from the math and the sprint overruns.
**Fix:** Available focused hours, checked against recent completed work.

### Pitfall 3: The PM Sets the Number
**Symptom:** "We need 40 points this sprint."
**Consequence:** Quality is borrowed, and the team stops estimating honestly.
**Fix:** The team sets capacity. The PM sets the goal and the order.

### Pitfall 4: No Slack
**Symptom:** 100% of capacity allocated.
**Consequence:** Any surprise breaks the sprint and trust in planning.
**Fix:** Hold a share unallocated, tuned from history.

### Pitfall 5: Unowned Dependencies
**Symptom:** "We're waiting on the platform team."
**Consequence:** The sprint stalls on day six.
**Fix:** Owner, needed-by date, and fallback on day one.

### Pitfall 6: Carryover Treated as Normal
**Symptom:** A third of the work carries over every sprint.
**Consequence:** The plan is fiction and nobody believes it.
**Fix:** Plan to the last three sprints' throughput, and read the carryover in retrospect.

---

## References

### Skill Files
- [`template.md`](template.md): goal, capacity, selected work, slack, risks, commitment
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`backlog-refinement-advisor`](../backlog-refinement-advisor/SKILL.md): upstream; makes items ready
- [`prioritization-advisor`](../prioritization-advisor/SKILL.md): the order of the backlog
- [`user-story-splitting`](../user-story-splitting/SKILL.md): slice large items
- [`release-readiness`](../release-readiness/SKILL.md): downstream; the check before shipping
- [`roadmap-planning`](../roadmap-planning/SKILL.md): the longer horizon the sprint serves
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Sprint goal and sprint planning:** *The Scrum Guide* (Ken Schwaber and Jeff Sutherland).
- **Flow and throughput as a check on capacity:** common practice from Kanban and Lean.

### Provenance
Distilled from practitioner experience coaching product and engineering teams on planning cadence.
