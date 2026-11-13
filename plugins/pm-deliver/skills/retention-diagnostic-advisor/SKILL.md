---
name: retention-diagnostic-advisor
argument-hint: "[what's churning or going quiet, and what you already know]"
description: "Find why customers leave or go quiet, then pick the fix that fits. Use when churn or renewal numbers slipped and you need the cause before you launch a retention program."
intent: >-
  Guided triage from a retention symptom to a diagnosis. Separates four causes (never activated,
  never a fit, value faded, or something changed around the customer), checks which the evidence
  supports, and recommends the move that fits (activation fix, segment correction, value
  reinforcement, or a save and win-back play). Says plainly when the data can't tell yet.
type: interactive
theme: finance-metrics
best_for:
  - "Diagnosing why churn rose before building a retention program"
  - "Telling 'never activated' from 'lost value' from 'bad fit'"
  - "Picking the retention move that matches the cause"
  - "Reading a renewal or contract-churn problem in long-cycle business"
scenarios:
  - "Churn rose last quarter and leadership wants a loyalty program. Where do I start?"
  - "Service-contract renewals dropped on one product line. What is going on?"
  - "Customers who signed in March are leaving at six months. Why?"
  - "Which customers should we try to save, and which should we let go?"
estimated_time: "10-20 min"
---

# Retention Diagnostic Advisor

## Purpose

Find **why customers leave or go quiet**, and match the fix to the cause. Retention programs fail
when they treat all churn as one problem: a discount saves the customer who found it too expensive
and does nothing for the one who never got started.

The sentence to keep in your head: **churn is the last event, not the cause.** The cause happened
earlier: the customer never got value, was never the right customer, got value and then lost it, or
something around them changed. Each needs a different fix.

## Input

**Works best with:** What's churning or going quiet (which customers, since when) and what you
already know about why.

**Also useful:** Retention or renewal numbers by cohort and segment, exit or cancellation reasons,
time from sign-up to churn, support history of customers who left, and how long a typical contract
runs.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill asks what's happening and what you've seen, and
works out which cause is most likely from your answers. If the data can't tell the causes apart, it
says so and names the cheapest way to find out.

**Example invocations:**
- `Churn rose from 6% to 9% last quarter. Most leavers had under 90 days with us.`
- `Service-contract renewals on the NFA-200 base fell from 62% to 48%. Contracts run 3 years.`

---

## Key Concepts

### Four Causes of Leaving

| Cause | What it looks like | Typical timing |
|---|---|---|
| **Never activated** | Customer signed up or bought but never got first value ([`activation-design`](../activation-design/SKILL.md)) | Early: first weeks or months; usage never started |
| **Never a fit** | Wrong customer: wrong size, use case, or expectation set in the sale | Early to mid; leaves after a trial or first renewal |
| **Value faded** | Got value, then stopped: needs changed, usage dropped, a champion left | Mid to late; usage falls before the exit |
| **Something changed** | Budget cut, merger, a competitor, a regulation, a product being retired | Any time; often not about your product |

Most real churn is a mix, but **one usually dominates**. Find it before you act.

### Read the Timeline, Not the Rate

The average churn rate hides the pattern. Look at **when** in the customer's life they leave (by
months since start) and **what they did before** (usage curve, support contacts, champion changes).
Early-life churn points to activation and fit. Churn after a long healthy period points to faded
value or outside change. A usage drop that precedes cancellation by weeks is your earliest warning.

### Segment Before You Conclude

Cut by **customer size, industry, source (direct, partner, self-serve), plan, and the version they
bought**. Retention that is 95% in one segment and 60% in another is two problems, and the weak
segment might be customers you never should have sold to ([`sales-value-narrative`](../sales-value-narrative/SKILL.md)
decides who you tell the story to).

### Stated Reasons Are Weak Evidence

"Too expensive" is the most common exit reason and the least informative: it often means "didn't see
the value." Treat exit reasons as a starting question ("What did you expect it to do for you?"), not
a finding, and compare them with behavior (did they ever activate? did usage fall first?).

### Leading Signals

Watch the signals that move before the exit: **usage trend, breadth of use (how many people or
features), support sentiment, champion turnover, and missed milestones.** For contract businesses
add: engagement with the service, unused entitlements, and who the renewal decision-maker is. A
simple health view built from these is better than waiting for a cancellation. See
[`launch-metrics`](../launch-metrics/SKILL.md) for leading and lagging pairs.

### Who to Save and Who to Let Go

Not every customer is worth saving. Ask: would they have been a good customer if the cause were
fixed? Saving a bad-fit customer at a discount trains the market and fills support with the wrong
requests. Be explicit about the customers you'll try to keep, the ones you'll let go, and why.

### Right-Size the Response

A small contract base needs a conversation with each at-risk account. A large self-serve base needs
an automated health signal and a few targeted plays. Don't build a heavy program to solve a cause the
data hasn't confirmed. Recommend a level and let the user move it.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol:
heads-up, one question per turn, numbered options, and best-guess mode on request.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not a retention program.** It diagnoses; the fix depends on the cause.
- **Not a churn forecast.** It explains past behavior and points to early signals.
- **Not a discount strategy.** Price is rarely the cause and is a costly cure.

---

## Application

This skill asks **up to 4 adaptive questions**, then recommends a diagnosis and a move.

### Question 1 of 4: What's happening?

**Agent asks:**

"Describe what you're seeing: who is leaving or going quiet, since when, and what you've noticed
about them."

**Listen for the timeline and the segment.** "Mostly under 90 days" and "mostly large accounts at
renewal" point to different causes.

### Question 2 of 4: When in their life do they leave?

**Agent asks:**

"When do customers typically leave?

1. **Early: before or just after they really start** (first weeks or months)
2. **At the first renewal or trial end**
3. **After a long, healthy period**
4. **No clear pattern / I don't know**"

**Map to the likely cause:** 1 → never activated. 2 → never a fit or never activated. 3 → value
faded or something changed. 4 → say the data can't tell yet and name how to find out.

### Question 3 of 4: Did they ever get started?

**Agent asks:**

"For the customers who left, what do you know about what they did before they left?

1. **Most never really used it** (little or no usage)
2. **They used it, then usage dropped over weeks or months**
3. **They used it until something changed** (a person left, a merger, a budget cut)
4. **I haven't looked at this yet**"

**Confirm or revise.** 1 → activation. 2 → value faded. 3 → something changed. 4 → recommend this
check first; it's the cheapest way to separate the causes.

### Question 4 of 4: Who are they?

**Agent asks:**

"Do the leavers share anything: size, industry, how they came to you, what they bought?"

**Find the segment.** A shared trait suggests a fit problem. No shared trait points to a product or
service cause. Ask how big the base is, so the response can be sized.

### Final Step: Recommend the diagnosis and move

```markdown
## Retention Diagnosis: [context]

**Most likely cause:** [Never activated / Never a fit / Value faded / Something changed],
because [the evidence from their answers]
**Confidence:** [strong / suggestive / thin] · **What would change my mind:** [one check]

### The move
- **If never activated:** [fix the path to first value; see activation-design]
- **If never a fit:** [change who you sell to; adjust the story and qualification]
- **If value faded:** [reinforce value: usage reviews, new use cases, a champion plan]
- **If something changed:** [save plays only where it's winnable; plan for the rest]

### Leading signals to watch
[usage trend, breadth, support sentiment, champion turnover, unused entitlements]

### Who to save and who to let go
[with reasons]

### Next
1. [skill or action]
2. [skill or action]
```

---

## Examples

### Example A: SaaS, early churn

**User:** "Churn rose from 6% to 9% last quarter. Most leavers had under 90 days with us. Leadership
wants a loyalty program."

**Agent (Q2):** → **1 (early).** **(Q3):** → **1 (most never really used it).** **(Q4):** "Mostly
accounts under 100 technicians that came in through the March promo."

**Diagnosis:** *Never activated, with a fit component.* Confidence: suggestive (we have the
timing and the usage, not why). A loyalty program would target customers who never got started. The
move: fix the path to first value ([`activation-design`](../activation-design/SKILL.md)) and look
at who the March promotion brought in. What would change my mind: if the leavers had real usage
before leaving.

### Example B: Industrial, renewals

**User:** "Service-contract renewals on the NFA-200 base fell from 62% to 48%. Contracts run three
years."

**Agent (Q2):** → **2 (at renewal).** **(Q3):** → **3 (something changed):** "Several plants were
told the NFA-200 is being retired." **(Q4):** "Mostly plants with 1-2 units."

**Diagnosis:** *Something changed: the product's end-of-sale announcement.* Confidence: strong
(timing matches the announcement; the leavers share a trait). The move is not a loyalty program but
a clear transition path: contract terms through 2028, a migration offer for the NFA-500, and the
messaging from [`eol-message`](../eol-message/SKILL.md). Save plays for plants with 3+ units; let
the rest migrate on their schedule. What would change my mind: if non-announced plants also drop.

---

## Common Pitfalls

### Pitfall 1: Treating All Churn as One Problem
**Symptom:** One loyalty program for every leaver.
**Consequence:** It misses the cause for most of them.
**Fix:** Separate the four causes first.

### Pitfall 2: Believing the Exit Survey
**Symptom:** "Too expensive" accepted as the cause.
**Consequence:** Discounts that don't save the customer who never got value.
**Fix:** Compare the stated reason with behavior.

### Pitfall 3: Reading the Rate, Not the Timeline
**Symptom:** Tracking the average monthly churn.
**Consequence:** Early-life and late-life problems blur together.
**Fix:** Chart churn by months since start and by segment.

### Pitfall 4: Saving Everyone
**Symptom:** Discounts to every at-risk account.
**Consequence:** Bad-fit customers stay and drain support.
**Fix:** Decide who is worth saving and why.

### Pitfall 5: Waiting for the Cancellation
**Symptom:** Action begins at the cancel request.
**Consequence:** The decision is already made.
**Fix:** Watch leading signals: usage trend, breadth, champion changes.

### Pitfall 6: Ignoring Outside Change
**Symptom:** Churn blamed on the product when a merger or announcement caused it.
**Consequence:** A fix for something that wasn't broken.
**Fix:** Check what changed around the customers.

---

## References

### Related Skills
- [`activation-design`](../activation-design/SKILL.md): fix the path to first value
- [`usage-data-investigation`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/usage-data-investigation/SKILL.md): read usage and cohorts
- [`launch-metrics`](../launch-metrics/SKILL.md): leading and lagging indicators and triggers
- [`saas-revenue-growth-metrics`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/saas-revenue-growth-metrics/SKILL.md): churn and retention definitions
- [`eol-message`](../eol-message/SKILL.md) and [`eol-process`](../eol-process/SKILL.md): when retirement is the cause
- [`organic-growth-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/organic-growth-advisor/SKILL.md): growth paths beyond retention
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Cohort retention curves:** standard product and customer analytics practice.
- **Customer health scoring and leading signals:** common customer-success practice.
- **Value realization and time to value:** customer-success literature.

### Provenance
Distilled from practitioner experience diagnosing churn and renewal problems in software and industrial service businesses.
