---
name: usage-data-investigation
argument-hint: "[the question about customer behavior, and what data you can reach]"
description: "Investigate what customers actually do from product analytics, with every claim labeled Fact, Inference, or Assumption. Use when you need behavior evidence, not opinions, before deciding."
intent: >-
  Turn a question about customer behavior into a disciplined read of product usage data: define the
  question and the unit of analysis, check the data's trustworthiness, look at funnels, cohorts, and
  segments, separate what the data shows from what you conclude, and name the follow-up that
  qualitative research must answer. Quantitative discovery that points to the "why" without claiming it.
type: workflow
theme: discovery-research
best_for:
  - "Finding where customers drop off, and who, before deciding what to build"
  - "Checking a belief about behavior against what the product data shows"
  - "Reading a launch or trial funnel, cohorts, and segments honestly"
  - "Knowing which question the numbers can't answer and a conversation must"
scenarios:
  - "Trials start but few reach a first optimized route. Where do they stall?"
  - "Leadership says feature X is popular. What does the usage data actually show?"
  - "Do customers who onboarded after the fix retain better than those before?"
  - "Commissioned units report faults early. Which unit configurations, and when?"
estimated_time: "45-90 min"
---

# Usage Data Investigation

## Purpose

Read what your customers **do**, from the data your product already produces, and say exactly what
that does and does not tell you. The skill moves a question through five steps: **frame** it,
**check the data**, **look** (funnel, cohort, segment), **separate** fact from inference, and
**hand the "why" to people** who can answer it.

The sentence to keep in your head: **data tells you what happened and where, almost never why.**
Behavior data is the strongest evidence of what customers do and the weakest explanation of why they
do it. Use it to aim your interviews, not to replace them.

It is the quantitative partner to [`research-synthesis`](../research-synthesis/SKILL.md) and feeds
[`launch-metrics`](../launch-metrics/SKILL.md) once a launch is live.

## Input

**Works best with:** A question about customer behavior, and what data you can reach (product
analytics, an export, a dashboard screenshot, pasted numbers).

**Also useful:** What the product does, how "active" or "activated" is defined today, the time
range, known data problems (tracking gaps, a migration), and what decision this will inform.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill asks what you're trying to learn and what data
exists, then helps you define the question, the metrics, and the cuts you'd want, and marks every
number it lacks `[NEEDS SOURCE]`. It will not make up numbers or trends. It needs your data to
analyze; without it, it helps you plan the investigation.

**Example invocations:**
- `Trials start but few optimize a route. Here's the funnel export. Where do they stall?`
- `Warranty tickets for the NFA-500 by month and configuration. What's the early-life pattern?`

---

## Key Concepts

### Fact, Inference, Assumption

Label every claim. This is the vocabulary used across the library
([`autonomous-investigation`](../autonomous-investigation/SKILL.md)):

| Label | Meaning | Example |
|---|---|---|
| **Fact** | Directly in the data, with the metric defined | "41% of trials that started in March reached a first optimized route within 7 days" |
| **Inference** | Your reading of what the fact suggests | "Trials without a dispatcher invited rarely activate" |
| **Assumption** | Believed but not shown by this data | "Dispatchers don't see the value" |

Most bad data stories are an inference presented as a fact. The "why" is nearly always an
inference.

### Start With a Question, Not a Dashboard

"Let's look at the data" finds what is easy to count. Write the question first, in a form the
data can answer: *which step loses the most trials, for which kind of account, and did it change
after the onboarding fix?* Name the **unit** (account, user, unit installed), the **window**, and
the **decision** the answer informs. If no decision depends on it, stop.

### Check the Data Before Believing It

Before any chart, ask four things: **Is the event tracked correctly** (does "activated" fire when
you think it does)? **Is the definition stable** (did it change mid-period)? **Who is missing**
(ad blockers, offline units, accounts that never connected, test accounts mixed in)? **Is the
sample enough** to read (small counts swing wildly)? A confident chart of bad data is worse than
no chart.

### Funnel: Where Do They Stop?

A funnel counts how many reach each step toward a valuable outcome. Define each step as a
behavior, not a page view. The useful number is the **conversion between steps**: the biggest drop
is where to look first. In hardware or service, the steps are physical or contractual (quoted,
ordered, delivered, commissioned, in use), and the data comes from CRM, ERP, and service systems as
much as from product analytics.

### Cohorts: Did Something Change?

A cohort groups customers by a shared starting point (the month they began, the release they got,
the channel they came through) and follows each over time. It tells you whether **later customers
do better than earlier ones**, which an overall average hides. Show the count with every rate.
Small cohorts mislead: three accounts is a story, not a trend.

### Segments: Who Behaves Differently?

Cut by who the customer is (size, industry, plan, role, source) and by how they started. Averages
blend groups with opposite behavior. A feature "used by 30%" may be used by 80% of one segment and
0% of another, and that difference is the finding.

### Correlation, Not Cause

Customers who use feature X retain better. That does not mean X causes retention: engaged
customers use more of everything. State the pattern as a Fact, the causal story as an Inference,
and say how you could test it (an experiment, or interviews). Never present usage-retention
correlation as proof of value.

### Hand the "Why" to People

Every investigation ends by naming the question the data can't answer and who can: a short list of
interview questions, a segment to talk to, a cohort to compare. This is where
[`discovery-interview-prep`](../discovery-interview-prep/SKILL.md) takes over.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not a dashboard build.** It reads data you have; it doesn't design your analytics stack.
- **Not statistical proof.** It reads patterns honestly; it doesn't run significance tests on thin data.
- **Not an explanation.** It says what and where, and points to who can say why.
- **Not invented numbers.** Every figure comes from data you supplied, or is `[NEEDS SOURCE]`.

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** Artifact first: the question, the data check, the funnel, cohort, and
segment reads, the labeled findings, and the follow-up questions for people. Commentary short,
after. Every number traces to supplied data or is `[NEEDS SOURCE]`. Every statement carries a label:
Fact, Inference, or Assumption.

**If the PM brings an analysis, critique first.** Is there a question and a decision? Was the data
checked? Are definitions stable? Are counts shown beside rates? Is a correlation read as cause?
Are Facts and Inferences separated? Name gaps; offer rewrites last.

### Step 1: Frame the Question
Write the question, the unit, the window, and the decision. Name the definition of each key
event (what exactly counts as "activated").

### Step 2: Check the Data
Run the four checks: tracking, definition stability, who's missing, sample size. Record what you
cannot trust and how it limits what follows.

### Step 3: Look: Funnel, Cohort, Segment
Funnel to find the biggest drop. Cohorts to see change over time. Segments to find who differs.
Show counts with rates. Stay within what the data supports.

### Step 4: Label the Findings
Write each finding as a Fact (with the metric and its definition), then any Inference (marked, with
its reasoning), then the Assumptions the data cannot settle. Flag any correlation presented as
cause.

### Step 5: Name What People Must Answer
List the "why" questions the data raised, the segment or cohort to talk to, and the interview
questions to ask. Point to [`discovery-interview-prep`](../discovery-interview-prep/SKILL.md).

### Step 6: Hand Back
Short summary (supplied, inferred, unknown) and a numbered ladder, evidence-favored first, labeled
`(Recommended)`: interview the stalled segment; fix the tracking gap before concluding; compare the
two cohorts again in a month; or run an experiment on the suspected cause.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight trial funnel, SaaS) and
[`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield early-life faults,
industrial). Both end with a question only a conversation can answer.

---

## Common Pitfalls

### Pitfall 1: Starting With the Dashboard
**Symptom:** "Let's see what the data says."
**Consequence:** You find what's easy to count, and nothing tied to a decision.
**Fix:** Write the question and the decision first.

### Pitfall 2: Trusting Untested Tracking
**Symptom:** A chart of an event nobody verified fires correctly.
**Consequence:** The team acts on a bug.
**Fix:** Check tracking, definition stability, who's missing, and sample size first.

### Pitfall 3: Averages That Hide Segments
**Symptom:** "30% use the feature."
**Consequence:** Opposite behavior in two groups cancels into a bland number.
**Fix:** Cut by segment and cohort.

### Pitfall 4: Correlation Sold as Cause
**Symptom:** "Users of X retain better, so X drives retention."
**Consequence:** The team builds more X and retention doesn't move.
**Fix:** Label the cause an Inference and say how you'd test it.

### Pitfall 5: Rates Without Counts
**Symptom:** "Conversion doubled" with a cohort of five.
**Consequence:** Noise reads as a trend.
**Fix:** Show the count beside every rate.

### Pitfall 6: Stopping at the Number
**Symptom:** The investigation ends with a chart.
**Consequence:** Nobody learns why, so the same drop returns.
**Fix:** End with the questions people must answer.

### Pitfall 7: Invented Numbers
**Symptom:** AI-drafted trends nobody supplied.
**Consequence:** The team decides on data that doesn't exist.
**Fix:** Numbers come from your data or are `[NEEDS SOURCE]`.

---

## References

### Skill Files
- [`template.md`](template.md): question, data check, funnel, cohort, segment, labeled findings
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`research-synthesis`](../research-synthesis/SKILL.md): the qualitative partner
- [`discovery-interview-prep`](../discovery-interview-prep/SKILL.md): where the "why" gets answered
- [`launch-metrics`](../launch-metrics/SKILL.md): the post-launch dashboard this feeds
- [`derisk-measurement-advisor`](../derisk-measurement-advisor/SKILL.md): how to measure a belief
- [`saas-revenue-growth-metrics`](../saas-revenue-growth-metrics/SKILL.md): metric definitions
- [`autonomous-investigation`](../autonomous-investigation/SKILL.md): the Fact / Inference / Assumption vocabulary
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Funnels and cohorts:** standard product-analytics practice; the AARRR funnel is from Dave McClure, "Startup Metrics for Pirates" (2007).
- **Outcomes over activity:** Joshua Seiden, *Outcomes Over Output*.
- **Correlation versus causation in product data:** standard statistical caution, widely taught in analytics practice.

### Provenance
Distilled from practitioner experience reading product and service data for B2B and industrial products.
