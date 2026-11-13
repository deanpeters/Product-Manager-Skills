---
name: pm-role-charter
argument-hint: "[the PM role, the product or area, and where the role feels unclear]"
description: "Write a one-page charter for a PM role: what it owns, decides, influences, and is measured on. Use when expectations clash, scope creeps, or a PM is held accountable for things they can't control."
intent: >-
  Make a PM role explicit enough to hold someone accountable and to defend: the outcome the role is
  responsible for, the decisions it makes versus shares, the interfaces with engineering, design,
  sales, and support, how success is judged, and what the role is not. Sized so a new PM gets a half
  page and a senior or multi-product role gets the full charter.
type: component
theme: stakeholder-comms
best_for:
  - "Defining a PM role when expectations differ between the PM, their manager, and peers"
  - "Onboarding a new PM with a shared understanding of the job"
  - "Pushing back on scope creep and on accountability without authority"
  - "Setting up product roles in a team that has never had them"
scenarios:
  - "I'm accountable for revenue but don't control pricing or sales. How do I frame the role?"
  - "Write a charter for a new PM joining our industrial controls team"
  - "My manager and engineering director describe my job differently"
  - "Our PMs act as project managers. How do we describe the role differently?"
estimated_time: "30-45 min"
---

# PM Role Charter

## Purpose

Write a **one-page charter** for a product role: the outcome it is responsible for, the decisions it
owns and the ones it shares, who it works with and how, how its success is judged, and what it is
*not*.

The sentence to keep in your head: **accountability without authority is a setup.** Most unhappy PM
roles are not a skill problem. They're a charter problem: the PM is held to an outcome they can't
influence, expected to decide what belongs to someone else, or drowning in work the role was never
meant to do. Writing it down turns an invisible argument into a visible agreement.

The charter is the role-level companion to the
[`decision-rights-matrix`](../decision-rights-matrix/SKILL.md): the matrix says who decides each
decision; the charter says what this role is for.

## Input

**Works best with:** The role, the product or area it covers, and where the role feels unclear.

**Also useful:** The job description, what the PM's manager expects, how peers (engineering, design,
sales, support) describe the PM's job, and recent moments of friction.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill asks what the role is for and where it hurts,
drafts the charter as a proposal, and marks every expectation as something the PM's manager and
peers must confirm.

**Example invocations:**
- `Charter for a PM on the field-service optimizer. I'm measured on revenue but sales owns pricing.`
- `New PM joining industrial controls. Draft a charter for the first 90 days and beyond.`

---

## Key Concepts

### The Seven Parts of a Charter

| Part | The question | A test |
|---|---|---|
| **Outcome** | What result is this role responsible for? | One outcome a stranger would understand, not an activity list |
| **Scope** | Which product, segment, or area? | Boundaries clear enough to say "that's not mine" |
| **Decisions owned** | What does the PM decide alone? | Specific decisions, not "strategy" |
| **Decisions shared** | What do they decide with others, and who has the last word? | One accountable person each (see [`decision-rights-matrix`](../decision-rights-matrix/SKILL.md)) |
| **Interfaces** | Who do they rely on, and for what? | What the PM gives and gets from engineering, design, sales, support, finance |
| **Success measures** | How will this role be judged? | A few measures the PM can influence (leading and lagging) |
| **What it is not** | What will the PM not do? | Named work that belongs elsewhere |

### Accountability Must Match Influence

If the role is judged on revenue but doesn't control pricing, the channel, or the sales motion,
the charter has to say **what the PM influences** (the product, the proof, the enablement) and
what they're measured on **given that**. Measure what the role can move: adoption, activation,
attach, and the leading indicators from [`launch-metrics`](../launch-metrics/SKILL.md), alongside
the business outcome it contributes to. Where accountability exceeds control, say so plainly and
name the gap for the manager to close.

### The PM Is Not the Project Manager (or Everyone's Assistant)

A frequent source of drift: the PM becomes the team's scheduler, note-taker, and ticket writer.
Those tasks are real and someone owns them, but the PM's value is **the problem, the customer, the
strategy, and the trade-offs**. Name the delegated work explicitly ("project management belongs to
the delivery lead") so scope creep can be named rather than absorbed.

### Right-Size the Charter

A new PM in a small team needs a half page: outcome, decisions, three measures, what it isn't. A
senior or multi-product role needs the full seven parts and an agreed review date. A charter longer
than a page is a policy document nobody reads. Recommend a size and let the user move it.

### A Charter Is a Conversation, Not a Document

Draft it, then **review it with the PM's manager and key peers**. Differences between how they
describe the role are the real findings. Agree the charter in the room; if it can't be agreed, the
disagreement itself is something to resolve with the manager. Revisit it when scope changes and at
least once a year.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not a job description.** A job description lists skills and duties; a charter says what the role is for and where it stops.
- **Not a performance review.** It sets expectations, not ratings.
- **Not a power grab.** It makes existing expectations visible; it does not claim authority.
- **Not permanent.** It changes when scope does.

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** Artifact first: the seven parts on one page. Commentary short, after. Every
expectation is a **proposal for the manager and peers to confirm**. Mark measures, targets, and
names you were not given as `[NEEDS SOURCE]`.

**If the PM brings a charter, critique first.** Does it name an outcome rather than activities? Is
accountability matched to influence? Are shared decisions single-owner? Does "what it is not" name
real work? Is it one page? Has anyone but the PM read it? Name gaps; offer rewrites last.

### Step 1: Name the Outcome and the Scope
One outcome sentence and the boundaries of the role.

### Step 2: List the Decisions
Owned alone, shared (with the accountable person), and not theirs.

### Step 3: Describe the Interfaces
For engineering, design, sales, support, and finance: what the PM provides, what they get.

### Step 4: Set the Measures
Two or three leading, one or two lagging, and where accountability exceeds control, the gap.

### Step 5: Write What It Isn't
Name the work that belongs elsewhere and who owns it.

### Step 6: Confirm With Others and Hand Back
Take it to the manager and key peers. Short summary (supplied, inferred, unknown), then a numbered
ladder, evidence-favored first, labeled `(Recommended)`: review it with the manager first; pair it
with a decision-rights matrix for the shared decisions; trim it to a half page; or schedule a
review in 90 days.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight PM, accountable for revenue without
control of pricing) and [`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield
new PM in a matrix organization).

---

## Common Pitfalls

### Pitfall 1: Accountability Without Influence
**Symptom:** Measured on revenue; no say in price, channel, or sales.
**Consequence:** Blame without levers.
**Fix:** Name what the PM influences, measure what they can move, and surface the gap.

### Pitfall 2: An Activity List
**Symptom:** "Writes PRDs, runs standups, manages the backlog."
**Consequence:** The role becomes tasks, and the outcome disappears.
**Fix:** Start from the outcome.

### Pitfall 3: Nothing in "What It Is Not"
**Symptom:** No named exclusions.
**Consequence:** Scope creep, and the PM becomes the team's assistant.
**Fix:** Name delegated work and who owns it.

### Pitfall 4: Written Alone
**Symptom:** The PM drafts and files it.
**Consequence:** Nobody else agreed, so it's ignored.
**Fix:** Review with the manager and peers; resolve differences.

### Pitfall 5: A Policy Document
**Symptom:** Five pages.
**Consequence:** Nobody reads it.
**Fix:** One page, seven parts.

### Pitfall 6: Never Revisited
**Symptom:** The charter predates two reorganizations.
**Consequence:** It describes a job that no longer exists.
**Fix:** Review when scope changes, and annually.

---

## References

### Skill Files
- [`template.md`](template.md): the seven parts on one page
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`decision-rights-matrix`](../decision-rights-matrix/SKILL.md): who decides each shared decision
- [`stakeholder-mapping`](../stakeholder-mapping/SKILL.md): the people the PM works with
- [`launch-metrics`](../launch-metrics/SKILL.md): measures the PM can influence
- [`director-readiness-advisor`](../director-readiness-advisor/SKILL.md) and [`altitude-horizon-framework`](../altitude-horizon-framework/SKILL.md): how the role changes with seniority
- [`executive-onboarding-playbook`](../executive-onboarding-playbook/SKILL.md): onboarding a senior role
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Responsibility without authority in product roles:** a recurring theme in product-management writing, for example Marty Cagan, *Empowered*, on empowered product teams.
- **Team charters:** common practice from team-working and project-management literature.

### Provenance
Distilled from practitioner experience defining PM roles in matrix and industrial organizations.
