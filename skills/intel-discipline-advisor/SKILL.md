---
name: intel-discipline-advisor
argument-hint: "[the decision or competitive question on your desk]"
description: "Triage a competitive or market question into the right intelligence disciplines, cadence, and executing skill. Use when you know something needs researching but not which channel to run."
intent: >-
  Interactive triage for market intelligence: three adaptive questions about the decision on your desk,
  then numbered recommendations naming the discipline mix (OSINT, FININT, TECHINT...), the cadence, and
  the investigation skill that executes — teaching the decision-to-discipline mapping through use, so
  you eventually stop needing the advisor.
type: interactive
theme: market-intelligence
best_for:
  - "Picking the two or three collection disciplines a specific decision actually needs"
  - "Setting up a watch cadence that matches how fast the evidence really changes"
  - "Learning the decision-to-discipline mapping instead of running everything on everything"
scenarios:
  - "I think a competitor is up to something but I don't know where to look first"
  - "I have four hours this quarter for competitive intel — where do they go?"
estimated_time: "5-10 min"
---

# Intel Discipline Advisor

## Purpose

Triage a competitive or market question into the right intelligence response: which of the eight
collection disciplines to run, on what cadence, feeding which artifact, executed by which skill. The
[`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) compendium
holds everything about every channel; this advisor answers the question a busy PM actually has —
*"given what's on my desk, which two or three channels matter, and where do my limited hours go?"*
Running every discipline on every question is the failure mode; scoping to the decision is the craft.
The advisor teaches the mapping as it routes, so by your third session you won't need it. That's the
goal.

## Input

**Works best with:** the decision or question on your desk, in your words — "I think [Competitor A]
is building something," "my TAM slide got shredded," "sales keeps getting surprised."
**Also useful:** any signal you've already noticed (a job posting, a pricing change, an earnings
remark), your time budget, and whether you're limited to free sources.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The advisor opens by asking what's on your desk, with
enumerated situations to pick from.

**Example invocation:** `Intel discipline advisor: two of their senior engineers just followed our
CTO on a preprint server, and their careers page doubled — what do I run?`

## Key Concepts

- **Facilitation protocol:** use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the
  default interaction protocol (entry modes, one question per turn, progress labels, numbered
  recommendations). This file defines the domain logic.
- **The routing brain** is the artifact-mapping table in `intelligence-collection-disciplines`:
  every PM artifact has a known discipline mix and refresh cadence. The advisor's job is matching
  the user's situation to a row — and *showing the match*, because the mapping is the lesson.
- **Signals already seen are a head start.** If the user noticed a job posting surge, HUMINT has
  already flagged once — the recommendation starts from "1 discipline flagged" on the confidence
  stacking ladder and names which *independent* channels would corroborate (see
  [`autonomous-investigation`](../autonomous-investigation/SKILL.md)).
- **Cadence must match evidence speed and human capacity.** Pricing pages change monthly; statistics
  releases change annually. A watch the user can't sustain is worse than none — it produces false
  confidence that someone is watching.
- **The honest off-ramp.** Some questions don't need an investigation: if the question is "why do
  customers churn," the answer is win/loss interviews and discovery, not a patent sweep. The advisor
  says so.

## Application

This interactive skill asks **3 adaptive questions**, then offers **numbered, context-aware
recommendations**.

### Question 1: What's on your desk?

"What's the situation? Pick the closest, or describe your own:

1. **Suspected competitor move** — you think someone is building, entering, or repositioning
2. **An artifact to build or refresh** — TAM/SAM/SOM, battle card, positioning, ICP/personas, pricing analysis
3. **A margin or market-structure puzzle** — margins eroding, category shifting, entry decision
4. **Standing watch setup** — you want ongoing coverage, not a one-off answer"

### Question 2: Adaptive follow-up

- **If 1 (suspected move):** "What tipped you off — a job posting, a pricing change, an exec's
  post, a patent, a customer remark? (Whatever you saw is one discipline already flagging; we'll
  pick the independent channels that could corroborate it.)"
- **If 2 (artifact):** "Which artifact, and does a prior version exist to diff against?"
- **If 3 (structure puzzle):** "Is the question about the whole industry's structure, or one
  company's position in it?"
- **If 4 (watch):** "Honestly, how much recurring time can you or your team commit — 30 minutes a
  week, a half-day a month, a day a quarter?"

### Question 3: Constraints

"Two quick constraints: free sources only or is paid tooling available, and any geographic focus?
(Region changes which registries and statistics bureaus apply.)"

### Then: Recommend

Synthesize and offer **3-5 numbered recommendations**, each naming: **discipline mix → cadence →
executing skill → artifact fed**, with one line on when it's the right choice. Always show *why* the
disciplines were chosen (the mapping-table logic), and include the off-ramp when it's honest.
Handle single selection, combinations ("1 and 3"), and custom directions per the facilitation
protocol.

**Routing quick-reference** (from the artifact-mapping table):

| Situation | Discipline mix | Executing skill |
|---|---|---|
| Suspected move | Corroborate the seen signal: TECHINT + HUMINT + SIGINT + FININT, fused | [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) fusion template, then [`competitive-intel-watch`](../competitive-intel-watch/SKILL.md) |
| Battle card | SIGINT + OSINT + HUMINT | [`battle-card-builder`](../battle-card-builder/SKILL.md), kept fresh by the watch |
| TAM/SAM/SOM | GEOINT/DEMOINT + FININT capture rates | [`tam-sam-som-calculator`](../tam-sam-som-calculator/SKILL.md) Mode 3 |
| Positioning / ICP | OSINT + GEOINT/DEMOINT (+ VoC) | [`voice-of-customer-miner`](../voice-of-customer-miner/SKILL.md) → [`positioning-statement`](../positioning-statement/SKILL.md) |
| Industry structure | FININT + OSINT | [`porters-five-forces`](../porters-five-forces/SKILL.md) |
| One company's position | OSINT + FININT + HUMINT | [`swot-analysis`](../swot-analysis/SKILL.md) or [`company-intel`](../company-intel/SKILL.md) |
| Pricing question | SIGINT + FININT | [`pricing-packaging-tracker`](../pricing-packaging-tracker/SKILL.md) |
| Macro exposure | GEOINT/DEMOINT + regulatory FININT | [`pestel-delta-monitor`](../pestel-delta-monitor/SKILL.md) |
| Standing watch | SIGINT weekly, OSINT+HUMINT monthly, FININT+TECHINT quarterly — scaled to stated capacity | [`competitive-intel-watch`](../competitive-intel-watch/SKILL.md) |
| The full picture | All of the above, sequenced | [`competitive-analysis-process`](../competitive-analysis-process/SKILL.md) |

Close by offering the one-page **triage card** ([`template.md`](template.md)) filled in from the
session — the route, its "because," and a review date, as a handoff artifact.

## Examples

**Sample flow (fictional):**

> **Q1** → User: "1 — I think [Competitor A] is building a data-platform play."
> **Q2** → User: "Their careers page doubled, mostly data engineers."
> **Q3** → User: "Free sources, US only."
>
> "Your hiring observation means **HUMINT has already flagged once** — one discipline is an anecdote,
> so the job is corroboration from *independent* channels. Recommendations:
>
> 1. **TECHINT sweep this week** (patents.google.com + their GitHub org + arXiv affiliations, free) —
>    a paper-or-patent cluster in the same specialty as the hiring surge is the strongest fusion pair
>    available. *Pick this first: highest corroboration value per hour.*
> 2. **SIGINT check, 30 minutes** (crt.sh for new subdomains, Wayback diff on their product pages) —
>    catches launch staging if this is further along than hiring suggests.
> 3. **FININT pass at their next earnings call** — listen for capex dodges and segment-language
>    shifts; free via their IR page. *Slower, but turns hypothesis into briefable intelligence.*
> 4. **Set the watch instead** — if this can't get hours this quarter, wire [Competitor A] into
>    `competitive-intel-watch` monthly and let the cadence catch it.
>
> Reply 1, 2, 3, 4, a combination like '1 and 2', or tell me more. (Two agreeing disciplines = working
> hypothesis; three = brief your leadership.)"

**The off-ramp in action:** user picks "artifact: ICP refresh," but Q2 reveals the real question is
"why did our last three enterprise deals stall?" The honest recommendation leads with win/loss
interviews (HUMINT's ground-truth layer) and [`discovery-interview-prep`](../discovery-interview-prep/SKILL.md)
— "no public-web sweep answers a question your own churned prospects can answer better."

See [`examples/conversation-flow.md`](examples/conversation-flow.md) for a full end-to-end session:
inline input crediting two of the three questions, a capacity answer that gets believed, a
combination selection, and a "tell me more" that earns a teaching answer.
[`examples/conversation-flow-industrial.md`](examples/conversation-flow-industrial.md) shows the
routing shift for a physical-world signal — permits and customs data instead of site diffs.

## Common Pitfalls

- **Prescribing the full eight.** Recommending every discipline is refusing to triage. Two or three
  channels matched to the decision beats coverage theater — the mapping table exists so you can skip.
- **Ignoring the seen signal.** The user's tip-off is a free head start on the stacking ladder.
  Recommending channels that *re-detect* the same signal type adds no corroboration; independence is
  what stacks.
- **Cadence fantasy.** Designing a weekly watch for a team with a quarterly attention span. Ask the
  capacity question and believe the answer.
- **Routing without teaching.** Handing over a recommendation without the "because" strips the
  lesson. Every recommendation shows its mapping-table logic — the user should leave better at
  triage, not just triaged.
- **No off-ramp.** Forcing every question into an investigation. Discovery, win/loss, and support
  tickets answer some questions better than any public-web sweep; say so when it's true.

## References

- [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) (Component) — the compendium this advisor routes into; the pedagogic pair
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md) (Interactive) — facilitation protocol
- [`autonomous-investigation`](../autonomous-investigation/SKILL.md) (Workflow) — confidence stacking and evidence labels the recommendations lean on
- Executing skills: [`competitive-intel-watch`](../competitive-intel-watch/SKILL.md), [`battle-card-builder`](../battle-card-builder/SKILL.md), [`tam-sam-som-calculator`](../tam-sam-som-calculator/SKILL.md), [`porters-five-forces`](../porters-five-forces/SKILL.md), [`swot-analysis`](../swot-analysis/SKILL.md), [`voice-of-customer-miner`](../voice-of-customer-miner/SKILL.md), [`pricing-packaging-tracker`](../pricing-packaging-tracker/SKILL.md), [`pestel-delta-monitor`](../pestel-delta-monitor/SKILL.md), [`competitive-analysis-process`](../competitive-analysis-process/SKILL.md)
- [`discovery-interview-prep`](../discovery-interview-prep/SKILL.md) (Interactive) — the off-ramp when the question belongs to discovery
- Companion to Dean Peters' "Competitive Research on Steroids" compendium (Productside).
