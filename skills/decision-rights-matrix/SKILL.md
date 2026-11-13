---
name: decision-rights-matrix
argument-hint: "[the decisions that stall, and who is involved]"
description: "Define who decides, who is consulted, and who is told for key product decisions, with one accountable person each. Use when decisions stall, get reopened, or go to whoever pushes hardest."
intent: >-
  Make it explicit who decides what, using RACI for the work and DACI (or a similar single-approver
  model) for decisions, for the handful of product decisions that cause the most friction: pricing,
  roadmap, requirements, launch go/no-go, and end of life. Adds the forums where decisions are made,
  the escalation path, and a decision log. Right-sized so a small team gets a half-page and a
  matrix organization gets the full set.
type: component
theme: stakeholder-comms
best_for:
  - "Ending decision thrash on pricing, roadmap, or launch go/no-go"
  - "Clarifying decision rights after a reorganization or when a new team joins"
  - "Setting up decision forums and escalation paths that resolve conflicts in days"
  - "Leading through a matrix organization without relying on goodwill"
scenarios:
  - "Sales keeps overriding our list prices with special deals. Who actually decides?"
  - "Who should make the go/no-go call on our launch?"
  - "Every roadmap decision gets reopened in the next meeting. How do we make them stick?"
  - "Draft a RACI for our product decisions across product, engineering, sales, and support"
estimated_time: "30-60 min"
---

# Decision Rights Matrix

## Purpose

Write down **who decides what**, for the product decisions that cause the most friction, so decisions
stick. The output is a matrix of decisions against roles, **exactly one accountable person per
decision**, the **forums** where decisions are made and how often, an **escalation path**, and a
**decision log**.

The sentence to keep in your head: **a decision with two deciders has none.** When nobody knows who
decides, decisions go to the loudest voice, get reopened by whoever lost, and leave the PM
persuading instead of leading.

This is influence infrastructure for a matrix organization. It does not give the PM authority they
don't have; it makes the authority that exists **visible and agreed**, which is what lets a PM lead
without goodwill as the only tool.

## Input

**Works best with:** The decisions that stall or get reopened, and who is involved in them.

**Also useful:** The org chart or teams involved, any existing forums (product review, steering
committee), recent examples of a decision that went wrong, and who has senior sponsorship.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill asks which decisions hurt most and who is
involved, drafts a matrix as a proposal, and marks every role assignment as something the people
named must agree, not assume.

**Example invocations:**
- `Sales overrides our list prices with special deals. Draft a matrix for pricing, roadmap, and launch go/no-go.`
- `New platform team just joined. Who decides on architecture versus product scope?`

---

## Key Concepts

### RACI and DACI: One for the Work, One for the Decision

- **RACI** assigns the *work*: **R**esponsible (does it), **A**ccountable (owns the outcome, one
  person), **C**onsulted (two-way input before), **I**nformed (told after).
- **DACI** frames a *decision*: **D**river (runs the process, usually the PM), **A**pprover (one
  person who decides), **C**ontributors (supply input and evidence), **I**nformed.

Use RACI to map recurring responsibilities across functions, and DACI for a specific decision you
are about to make. Alternatives exist (RAPID, a "consent" model); the rule that survives all of
them is **one decider**.

### One Accountable Person

If two people are both accountable, the matrix hasn't decided anything. When the honest answer is
"both," split the decision into two decisions (for example: *what we build* is the PM, *how it's
built* is engineering). Keep splitting until each has one name.

### Pick the Decisions That Hurt

Don't map everything. Start with the decisions where friction already exists, usually 5-8:

| Decision | Common conflict |
|---|---|
| **What goes on the roadmap** | Sales requests vs strategy vs engineering capacity |
| **Pricing and discount rules** | Sales vs product vs finance |
| **Requirements and scope** | Product vs engineering |
| **Launch go / no-go** | Product vs sales vs support vs legal |
| **Portfolio entry or exit (including end of life)** | Product vs finance vs leadership |
| **Customer-specific commitments** | Sales vs engineering |

Add decisions that have caused a real fight in the last year. Leave out ones nobody argues about.

### Decide Vs. Input Vs. Veto

Clarify three things people confuse: **who decides**, **who must be consulted** before (and what
"consulted" means: their input is heard, not that they agree), and **who can veto** (rare, and only
for a stated reason such as legal or safety). Most conflicts come from consulted people acting like
approvers, or approvers deciding without consulting.

### Forums: Where Decisions Get Made

A decision needs a place and a rhythm: a **product review** for roadmap and scope, a **pricing
council** for discounts, a **launch forum** for go/no-go. For each: who attends, how often, what it
decides (and what it doesn't), and what it needs ahead (a one-page brief). Too many forums become
theater. Prefer fewer forums with clear mandates.

### Escalation

When people disagree and the decider is unmoved, there must be a **named next step**: who the
dispute goes to, within how many days, with what material. Without escalation, disputes simmer.
Escalation is not failure; an unescalated conflict is.

### The Decision Log

A short record of each significant decision: what, who decided, when, on what evidence, and what it
supersedes. It ends relitigation ("we decided this in March, here's why") and teaches the next PM
the reasoning.

### Right-Size the Matrix

A small team needs a half-page: five decisions, one name each. A matrix organization with several
business units needs forums, escalation, and a log. Over-building a matrix for a ten-person team is
the same failure as under-building it for a global one. Offer a level and let the user move it.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally. Draft the matrix as a proposal and have the named people confirm it.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not an org chart.** It's about decisions, not reporting lines.
- **Not authority granted by the PM.** Leadership has to agree it, or it's a wish.
- **Not a process for every decision.** Only the ones that hurt.
- **Not stakeholder management.** See [`stakeholder-mapping`](../stakeholder-mapping/SKILL.md) for the people dynamics.

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** Artifact first: the decisions, the matrix (one accountable each), the
forums, the escalation path, and the decision log format. Commentary short, after. Every role
assignment is a **proposal for the named person to confirm**. Never present an assignment as
agreed. Mark any name, cadence, or threshold you were not given as `[NEEDS SOURCE]`.

**If the PM brings a matrix, critique first.** Does each decision have exactly one accountable
person? Is "consulted" defined? Are forums and escalation named? Is there anything mapped that
nobody argues about? Did the named people agree? Name gaps; offer rewrites last.

### Step 1: Choose the Decisions
Ask which decisions stalled or got reopened. Pick 5-8. For each, name the recent example.

### Step 2: Propose Roles
For each decision, propose the Driver or Responsible, the single Accountable or Approver, the
Consulted, and the Informed. Where two people want to be accountable, split the decision.

### Step 3: Define Forums and Escalation
For each forum: who, how often, what it decides, what it needs. Name the escalation path and its
time limit.

### Step 4: Set the Log
One line per significant decision, kept where the team can find it.

### Step 5: Confirm With the People Named, and Hand Back
The matrix is a proposal until each accountable person agrees. Short summary (supplied, inferred,
unknown), then a numbered ladder, evidence-favored first, labeled `(Recommended)`: take it to the
accountable people individually before a group review; get leadership to endorse it; start with the
one decision that hurts most; or run a short trial and review in a quarter.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight discount overrides, SaaS) and
[`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield launch go/no-go and
pricing in a matrix organization).

---

## Common Pitfalls

### Pitfall 1: Two Accountable People
**Symptom:** "Product and Sales own pricing."
**Consequence:** Nobody does, and the loudest wins.
**Fix:** Split the decision until each has one name.

### Pitfall 2: Consulted Acting as Approver
**Symptom:** A consulted team blocks a decision it can't make.
**Consequence:** Decisions stall and resentment grows.
**Fix:** Define consulted as input heard, not agreement.

### Pitfall 3: Assignments Nobody Agreed
**Symptom:** The PM publishes a matrix.
**Consequence:** It's ignored the first time it's inconvenient.
**Fix:** The named people confirm it; leadership endorses it.

### Pitfall 4: Mapping Everything
**Symptom:** A 40-row matrix.
**Consequence:** Nobody reads it, and it hides the five that matter.
**Fix:** Start with the decisions that already cause friction.

### Pitfall 5: Forums Without Mandates
**Symptom:** A weekly meeting that reviews everything and decides nothing.
**Consequence:** Theater, and a slower org.
**Fix:** Each forum states what it decides and what it doesn't.

### Pitfall 6: No Escalation Path
**Symptom:** A disagreement with no named next step.
**Consequence:** It simmers until someone goes around the process.
**Fix:** Name who it goes to, in how many days, with what material.

### Pitfall 7: No Decision Log
**Symptom:** The same decision is reopened every quarter.
**Consequence:** Time lost and trust eroded.
**Fix:** A short log: what, who, when, why.

---

## References

### Skill Files
- [`template.md`](template.md): decisions, matrix, forums, escalation, log
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`pm-role-charter`](../pm-role-charter/SKILL.md): the PM's own role boundaries
- [`stakeholder-mapping`](../stakeholder-mapping/SKILL.md): the people behind each role
- [`launch-plan`](../launch-plan/SKILL.md): the go/no-go decision this matrix assigns
- [`eol-stakeholder-sequence`](../eol-stakeholder-sequence/SKILL.md) and [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md): end-of-life decisions
- [`prioritization-advisor`](../prioritization-advisor/SKILL.md): how the roadmap decision gets made
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **RACI:** standard responsibility assignment practice with no single originator.
- **DACI:** the Driver, Approver, Contributors, Informed decision model, popularized at Intuit and widely used in product teams.
- **RAPID:** Paul Rogers and Marcia Blenko, "Who Has the D?" *Harvard Business Review* (2006).

### Provenance
Distilled from practitioner experience clarifying decision rights in matrix product organizations.
