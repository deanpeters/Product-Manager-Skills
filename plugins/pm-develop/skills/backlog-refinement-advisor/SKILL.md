---
name: backlog-refinement-advisor
argument-hint: "[the backlog items or epic you want ready for the team]"
description: "Get backlog items ready for planning: understood, small, testable. Use when planning stalls on unclear tickets, or items keep growing and bouncing back mid-sprint."
intent: >-
  Guided triage from a messy backlog item to a ready one. Diagnoses what is missing (the why, the
  scope, the acceptance, the size, or a dependency), recommends the refinement move that fits
  (clarify, split, spike, or park), and defines "ready" for this team so planning stops guessing.
  Right-sized so a small fix gets a sentence and a risky epic gets a conversation.
type: interactive
theme: pm-artifacts
best_for:
  - "Making items ready before planning instead of discovering gaps in it"
  - "Deciding whether an item needs clarifying, splitting, a spike, or parking"
  - "Setting a team's own definition of ready"
  - "Keeping refinement short and regular instead of a long meeting"
scenarios:
  - "Planning keeps stalling because tickets are vague. Where do I start?"
  - "This epic keeps growing. Should we split it, spike it, or park it?"
  - "What does 'ready' mean for our team?"
  - "We refine for two hours every week and still find surprises mid-sprint"
estimated_time: "10-20 min"
---

# Backlog Refinement Advisor

## Purpose

Take a backlog item (or a pile of them) from vague to **ready**: understood well enough that the
team can size it, small enough to finish in a sprint, and testable enough that "done" is not an
argument.

Refinement is where planning is won or lost. Items that arrive in planning half-understood turn
into a long meeting, an estimate nobody trusts, and a ticket that bounces back on day six.

The sentence to keep in your head: **refinement is a short, regular conversation about the next few
weeks of work, not a meeting that grooms the whole backlog.** Ready is a conversation outcome, not
a field in the tool.

## Input

**Works best with:** The item, epic, or list you want ready, and when the team plans next.

**Also useful:** The team's current definition of ready (if any), the acceptance criteria written
so far, known dependencies, and how often items bounce mid-sprint.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill asks what the item is and what's unclear, and
recommends the smallest refinement move. It sizes the effort to the item: a small fix gets one line
of acceptance, a risky epic gets a conversation and possibly a spike.

**Example invocations:**
- `Epic: dispatcher can reschedule jobs from a map. Planning is Thursday and nobody can size it.`
- `Item: replace the discontinued relay on the NFA-500 power board. Unclear what testing is needed.`

---

## Key Concepts

### What "Ready" Means

An item is ready when the team can answer yes to all of these (the team sets its own list; this is
a starting point):

1. **Understood.** We know why it matters and who it's for.
2. **Small.** It can finish within one sprint, ideally in a few days.
3. **Testable.** We can say what "done" looks like: acceptance a tester could check.
4. **Unblocked.** Its dependencies are known and available (or an owner and a date).
5. **Sized.** The team has put a size on it and trusts it.

An item that fails one of these goes to the move that fixes it. An item that is ready should not be
refined again.

### The Four Moves

| Move | When | What it does |
|---|---|---|
| **Clarify** | The *why* or the *what* is fuzzy | A short conversation with the person who knows, ending with acceptance in plain words |
| **Split** | It's too big for one sprint | Cut into thin vertical slices that each deliver value ([`user-story-splitting`](../user-story-splitting/SKILL.md), [`epic-breakdown-advisor`](../epic-breakdown-advisor/SKILL.md)) |
| **Spike** | The unknown is technical or physical and blocks sizing | A time-boxed investigation (a day or two) that ends with a decision, not a deliverable |
| **Park** | It isn't coming soon, or nobody can say why it matters | Leave it out of the near backlog; revisit when a decision depends on it |

Parking is a legitimate answer. A backlog that holds everything holds nothing.

### Keep Refinement Short and Regular

A common rhythm: **a short refinement session every week or so, looking only at the next one or
two sprints' worth of work**. Beyond that horizon, detail goes stale before it's used. Aim for
2-3 items in depth rather than 20 in passing, and stop when the next sprint is covered.

### Right-Size the Detail

Detail should match risk and distance. A small, obvious fix needs a line of acceptance. A risky,
cross-team epic needs a real conversation, a split, and maybe a spike. Over-specifying a small item
wastes time; under-specifying a risky one costs a sprint. Ask how reversible and how costly a wrong
guess would be.

### Acceptance in Plain Words

Acceptance criteria say what must be true, in terms anyone can check, without prescribing the
implementation: "A dispatcher can drag a job to another technician and see a conflict warning," not
"use component X." For hardware and service work, acceptance may be a test result, a
certification step, or a checklist.

### The Whole Team Refines

Engineers, a designer, and a tester in the room catch gaps a PM alone won't. The PM brings the why
and the priority. The team brings feasibility, size, and the questions. If only the PM refines,
planning becomes the first time anyone else sees the item.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol:
heads-up, one question per turn, numbered options, and best-guess mode on request.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not a grooming marathon.** Short and regular beats long and rare.
- **Not estimation by the PM.** The team sizes.
- **Not prioritization.** See [`prioritization-advisor`](../prioritization-advisor/SKILL.md).
- **Not a specification exercise.** Ready means enough to start, not everything.

---

## Application

This skill asks **up to 4 adaptive questions**, then recommends the move.

### Question 1 of 4: What's the item, and when does the team need it?

**Agent asks:**

"Which item (or epic) do you want ready, and when does the team plan next?"

**Listen for scale and risk.** A small fix, a risky epic, and a vague idea need different moves.

### Question 2 of 4: What's missing?

**Agent asks:**

"What's the main gap?

1. **We don't agree what it's for, or what 'done' is** (unclear)
2. **It's too big for one sprint** (large)
3. **There's an unknown that blocks sizing** (technical or physical unknown)
4. **It's blocked by something outside the team** (dependency)
5. **I'm not sure anyone needs it soon** (maybe park)"

**Map to the move:** 1 → clarify. 2 → split. 3 → spike. 4 → name the owner and date, then decide
whether to start anyway. 5 → park.

### Question 3 of 4: How risky is a wrong guess?

**Agent asks:**

"If the team guesses wrong on this, how costly is it?

1. **Cheap and reversible** (a small change we can undo)
2. **Moderate** (a sprint of rework)
3. **Expensive or hard to undo** (a customer commitment, hardware tooling, a certification)"

**Size the detail:** 1 → one line of acceptance and go. 2 → clarify and size together. 3 → clarify,
split, and spike before committing, and name what a lighter pass would leave uncovered.

### Question 4 of 4: Who's in the conversation?

**Agent asks:**

"Who can be in the room: engineering, design, test, the person who knows the customer?"

**Fit the session:** missing voices become named questions to take away. If only the PM is
available, say what will probably surface in planning.

### Final Step: Recommend the move

```markdown
## Refinement Move: [item]

**Move:** [Clarify / Split / Spike / Park], because [one line tied to their answers]
**Detail level:** [light / standard / thorough], because a wrong guess is [cheap / moderate / costly].
A lighter pass would leave [uncovered].

### Make it ready
- **Understood:** [the why and who, in one line]
- **Acceptance (plain words):** [what a tester could check]
- **Slices (if split):** [thin vertical slices, first one deliverable]
- **Spike (if any):** [question, time box, what decision it ends with]
- **Dependencies:** [owner and date]

### Ready check
Understood ☐ Small ☐ Testable ☐ Unblocked ☐ Sized ☐

### Next
1. [action]
2. [action]
```

---

## Examples

### Example A: SaaS, a large epic

**User:** "Epic: dispatchers can reschedule jobs from a map. Planning is Thursday and nobody can
size it."

**Agent (Q2):** → **2 (large).** **(Q3):** → **2 (moderate).** **(Q4):** "PM, two engineers, a designer."

**Move:** *Split, with one clarifying question first.* Detail level: standard (a sprint of rework
if wrong). First clarify the *why* (is it reschedule speed or visibility?). Then slice: (1) show jobs
on a map, read-only; (2) drag a job to another technician; (3) conflict warning on drop. Slice 1 is
deliverable alone. Acceptance for slice 2: "A dispatcher can drag a job to another technician and
sees a conflict warning if skills don't match." Ready check: slices 1 and 2 ready for Thursday;
slice 3 parked until slice 2 ships.

### Example B: Industrial, an unknown that blocks sizing

**User:** "Item: replace the discontinued relay on the NFA-500 power board. We don't know what
testing is needed."

**Agent (Q2):** → **3 (unknown).** **(Q3):** → **3 (expensive: certification)**.

**Move:** *Spike, then clarify.* Detail level: thorough (a re-evaluation could void listing). Spike
(two days, owner: compliance engineer): ask the assessment body whether a like-for-like relay needs
re-evaluation, and get one quote for a drop-in replacement. It ends with a decision: replace now,
or last-time-buy. Don't size the item until the spike closes. A lighter pass would leave the
certification risk uncovered until it becomes a schedule problem.

---

## Common Pitfalls

### Pitfall 1: Refining Everything
**Symptom:** A two-hour weekly grooming of the whole backlog.
**Consequence:** Detail goes stale and meetings feel pointless.
**Fix:** Refine only the next one or two sprints' work, a few items deep.

### Pitfall 2: Ready Is a Field in the Tool
**Symptom:** The "ready" flag is set by the PM alone.
**Consequence:** Planning discovers the gaps, and items bounce.
**Fix:** Ready is the outcome of a conversation with the team.

### Pitfall 3: Over-Specifying Small Items
**Symptom:** A page of acceptance for a one-line fix.
**Consequence:** Time wasted and the team stops reading.
**Fix:** Match detail to risk.

### Pitfall 4: Skipping the Spike
**Symptom:** An unknown gets a guess for an estimate.
**Consequence:** A surprise on day six.
**Fix:** A time-boxed spike that ends with a decision.

### Pitfall 5: Never Parking
**Symptom:** The backlog holds every idea ever raised.
**Consequence:** Nobody trusts it, and refinement drowns in it.
**Fix:** Park what isn't coming soon, and revisit it when a decision needs it.

### Pitfall 6: Refining Without the Team
**Symptom:** The PM prepares tickets alone.
**Consequence:** Feasibility surfaces in planning.
**Fix:** Engineers, design, and test are in the conversation.

---

## References

### Related Skills
- [`sprint-planning`](../sprint-planning/SKILL.md): downstream; plans with ready items
- [`user-story`](../user-story/SKILL.md) and [`user-story-splitting`](../user-story-splitting/SKILL.md): write and slice items
- [`epic-breakdown-advisor`](../epic-breakdown-advisor/SKILL.md): break a large epic down
- [`prioritization-advisor`](../prioritization-advisor/SKILL.md): the order of the backlog
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Backlog refinement and Definition of Ready:** common agile practice; *The Scrum Guide* describes refinement as ongoing.
- **INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable):** Bill Wake.
- **Vertical slicing:** Richard Lawrence's splitting patterns (Humanizing Work).

### Provenance
Distilled from practitioner experience coaching product and engineering teams on backlog practice.
