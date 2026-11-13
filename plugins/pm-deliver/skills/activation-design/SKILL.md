---
name: activation-design
argument-hint: "[the product, the customer, and what 'first real value' looks like]"
description: "Define the moment a new customer first gets real value, then design the shortest path to it. Use when trials stall, installs sit idle, or onboarding is a checklist nobody finishes."
intent: >-
  Name the activation moment (the first time a customer gets the value they bought for), measure the
  time to reach it, find what stands between sign-up or delivery and that moment, and design the
  onboarding path, owner handoffs, and checkpoints around it. Works for self-serve software, assisted
  onboarding, and hardware commissioning, and ends with an activation metric the team can track.
type: component
theme: pm-artifacts
best_for:
  - "Defining what 'activated' means so the team stops counting sign-ups"
  - "Shortening the time from purchase or delivery to first real value"
  - "Designing onboarding around the customer's outcome instead of a feature tour"
  - "Handing a new customer between sales, onboarding, and support without a gap"
scenarios:
  - "Trials start but few reach a first optimized route. What should 'activated' mean?"
  - "Commissioned units sit idle for weeks. How do we design the first 30 days?"
  - "Our onboarding is a 20-step checklist nobody finishes. What do we cut?"
  - "Define the activation metric for a connected-service launch"
estimated_time: "30-45 min"
---

# Activation Design

## Purpose

Define **the moment a new customer first gets the value they bought for**, and design the shortest
reliable path to it. The output is an **activation definition**, a **time-to-value measure**, the
**blockers** on the path, an **onboarding path** with owners and checkpoints, and the **metric** the
team will track.

The sentence to keep in your head: **a customer who hasn't reached first value hasn't really
bought yet.** Sign-ups, deliveries, and logins are activity. Activation is the first time the
customer's own problem is solved. Customers who don't reach it quietly leave, and the churn shows up
months later in a number that can't be traced to its cause.

It connects the launch ([`launch-plan`](../launch-plan/SKILL.md)), the funnel
([`usage-data-investigation`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/usage-data-investigation/SKILL.md)), and retention
([`retention-diagnostic-advisor`](../retention-diagnostic-advisor/SKILL.md)).

## Input

**Works best with:** The product, the customer, and what first real value looks like to them.

**Also useful:** Where customers stall today (funnel or interview evidence), the current onboarding
steps and owners, time-to-value if you know it, and who touches the customer (sales, onboarding,
support, partners).

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill asks what the customer is trying to get done
and what "it worked" looks like to them, proposes an activation moment as a hypothesis, and marks
every number it lacks `[NEEDS SOURCE]`. It will not invent a benchmark.

**Example invocations:**
- `Activation for Route Optimizer. A dispatcher optimizing a real day is the aha moment, I think.`
- `Commissioning plan for NFA-500. Units are installed but not running the connected service.`

---

## Key Concepts

### The Activation Moment

The **first time the customer gets the outcome they bought for**, in their own terms. It is a
behavior or a result, not a page view or a delivery. Good tests:

- **Customer-visible:** the customer could say "that worked."
- **Predictive:** customers who reach it stay and expand at a clearly higher rate (check with data
  when you have it; otherwise it's a hypothesis).
- **Specific and countable:** you can say how many reached it and how long it took.

| Product | Weak activation | Real activation |
|---|---|---|
| Route optimizer (SaaS) | Account created; tour finished | A dispatcher optimizes a real day and keeps the result |
| Connected controller (hardware) | Unit delivered; unit installed | Unit commissioned, connected, and reporting for 14 days without a service call |

### Time to Value

Measure the **time from purchase or sign-up to activation**, and watch the median and the slow tail.
The tail is where customers disappear. Shorten the path by removing steps, pre-filling data,
providing defaults, and doing work for the customer, in that order. In hardware, time to value
includes shipping, installation, and commissioning, and the delays are often scheduling, not the
product.

### Find What Stands Between

List the steps from purchase to activation, then for each ask: **is it necessary, who owns it, and
what stops customers here?** Typical blockers: missing data the customer must supply, a decision
that needs someone else's approval, a configuration nobody explained, an install that waits on a
site visit, a handoff between sales and onboarding where context is lost. Use funnel data and a few
conversations to find the real one, not the one you assume.

### Design the Path Around the Outcome

Build the onboarding as the shortest path to the activation moment, not a tour of features. Put
**one action per checkpoint**, name the **owner** of each (the product, an onboarding specialist, a
partner, the customer), and decide what happens when a customer **stalls** (a nudge, a call, an
offer to do it for them) and after how many days. A path without stall handling is a hope.

### Handoffs Are Where Context Dies

The customer told sales what they want. If onboarding asks again, the customer notices. Write what
sales must capture (the outcome, the people, the constraints) and pass it on. Partner-led
onboarding needs the same handoff, plus training so the partner can reach activation, not just
installation. See [`buying-journey-enablement`](../buying-journey-enablement/SKILL.md).

### Right-Size the Design

A self-serve add-on needs a short path and a nudge. A complex installation with several roles needs
a plan with owners and dates. Don't build a 30-day program for something customers finish in 10
minutes, or a 10-minute tour for something that needs a site visit. Recommend a size and let the user
move it.

### One Metric, and What Else to Watch

Track **the share of new customers who reach activation within N days** (N set by your reality, not a
benchmark), with the count beside it. Also watch the median time to activate and where customers
stall. Pair it with a guardrail (support contacts per new customer) so you don't speed activation
by dumping work on support. See [`launch-metrics`](../launch-metrics/SKILL.md).

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not a product tour.** It's a path to an outcome.
- **Not a marketing funnel.** It begins after the customer has bought or signed up.
- **Not a retention program.** It's the front door; retention is the long game.
- **Not a benchmark.** The target time-to-value comes from your data, not an average.

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** Artifact first: the activation definition, time-to-value, the path with
blockers, the onboarding design (owners, checkpoints, stall handling), the metric. Commentary short,
after. Every figure is from supplied data or `[NEEDS SOURCE]`. Label whether the activation moment
is **evidenced** (customers who reach it retain better) or a **hypothesis**.

**If the PM brings an onboarding plan, critique first.** Is "activated" a customer outcome or
activity? Is time to value measured, with the tail? Are blockers evidenced? Does each step have an
owner? Is stall handling defined? Is the handoff from sales explicit? Name gaps; offer rewrites last.

### Step 1: Define the Moment
What the customer is trying to get done and what "it worked" looks like to them. Propose the
activation moment and label it evidenced or hypothesis.

### Step 2: Measure the Path
Steps from purchase to activation, who owns each, how long each takes (from data or marked
`[NEEDS SOURCE]`), and where customers stop.

### Step 3: Find the Blockers
For each slow or leaky step: necessary? owned? what stops customers? Rank by how many customers it
costs.

### Step 4: Design the Path
Shortest path, one action per checkpoint, an owner each, stall handling, and the sales-to-onboarding
handoff.

### Step 5: Set the Metric and Hand Back
Activation rate within N days with counts, median time, and a guardrail. Short summary (supplied,
inferred, unknown), then a numbered ladder, evidence-favored first, labeled `(Recommended)`: check
whether activated customers retain better; remove the worst blocker first; add stall handling at
day 3; or interview five customers who stalled.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight self-serve onboarding, SaaS) and
[`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield commissioning and
connected-service activation, industrial).

---

## Common Pitfalls

### Pitfall 1: Activation = Sign-Up
**Symptom:** "Activated" means an account exists.
**Consequence:** The metric rises while customers get nothing.
**Fix:** Define it as the first real outcome, in the customer's terms.

### Pitfall 2: An Untested Aha Moment
**Symptom:** The moment is declared, never checked against retention.
**Consequence:** The team optimizes a step that doesn't predict anything.
**Fix:** Label it a hypothesis until activated customers are shown to retain better.

### Pitfall 3: A Feature Tour
**Symptom:** Onboarding walks through screens.
**Consequence:** Customers finish the tour and never reach value.
**Fix:** Build the path to the outcome, one action per checkpoint.

### Pitfall 4: No Owner per Step
**Symptom:** "Onboarding" owns everything.
**Consequence:** Steps nobody owns are the steps that stall.
**Fix:** Name the owner of each checkpoint.

### Pitfall 5: No Stall Handling
**Symptom:** A customer goes quiet on day 4 and nobody notices.
**Consequence:** The slow tail becomes churn.
**Fix:** Define the nudge, the call, and the day each happens.

### Pitfall 6: Asking Twice
**Symptom:** Onboarding asks what sales already learned.
**Consequence:** The customer feels unheard.
**Fix:** Define what sales captures and passes on.

---

## References

### Skill Files
- [`template.md`](template.md): activation definition, path, blockers, onboarding design, metric
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`usage-data-investigation`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/usage-data-investigation/SKILL.md): find where customers stall
- [`retention-diagnostic-advisor`](../retention-diagnostic-advisor/SKILL.md): downstream; why customers leave
- [`launch-plan`](../launch-plan/SKILL.md) and [`launch-metrics`](../launch-metrics/SKILL.md): the launch around it, and its measures
- [`customer-journey-map`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/customer-journey-map/SKILL.md): the customer's experience
- [`buying-journey-enablement`](../buying-journey-enablement/SKILL.md): the handoff from selling
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Activation and the aha moment:** from growth practice, including the AARRR funnel (Dave McClure, "Startup Metrics for Pirates," 2007).
- **Time to value:** common customer-success practice.

### Provenance
Distilled from practitioner experience designing onboarding for software and connected-hardware products.
