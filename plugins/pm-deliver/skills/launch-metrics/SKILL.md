---
name: launch-metrics
argument-hint: "[what launched or is launching, and how long your sales cycle is]"
description: "Define launch success metrics, decision triggers, and 30/90/180-day reviews before launch. Use when you need to know early whether a launch is working and what you will do if it isn't."
intent: >-
  Turn "was the launch a success?" into a question the team can answer with data, early enough to
  act, using thresholds and responses agreed before anyone sees the results. Pairs leading with
  lagging indicators across adoption, commercial, operational, and customer categories, and
  schedules structured reviews that end in owned actions.
type: component
theme: strategy-positioning
best_for:
  - "Defining what launch success means before a launch, not after"
  - "Choosing leading indicators when sales cycles are long or revenue arrives late"
  - "Setting up 30, 90, and 180-day reviews with agreed stay / adjust / escalate triggers"
  - "Auditing a launch dashboard that tracks activity instead of results"
scenarios:
  - "How will we know the route optimizer launch is working before the quarterly numbers land?"
  - "Our launch dashboard shows trade-fair leads and press mentions. What should we track instead?"
  - "Plan the 90-day review for a new controller with an 8-month sales cycle"
  - "Distributor orders are strong but I don't trust them. What am I missing?"
estimated_time: "30-45 min"
---

# Launch Metrics

## Purpose

Define **how you will know the launch is working**: a short set of leading and lagging indicators
across four categories, each with a baseline, a target, a data source, and an owner; a funnel view
and a cohort view; and a 30, 90, and 180-day review plan in which the response to each result
(stay the course, adjust, escalate) is agreed *before* the launch.

The governing sentence: **launching is an event; commercial success is an ongoing responsibility.**
The dashboard starts at launch and runs until its metrics hand over to the ongoing product
metrics.

It picks up where [`launch-plan`](../launch-plan/SKILL.md) ends. The plan asks "are we ready?" This
skill asks "is it working?" Its findings feed what happens next to the product.

## Input

**Works best with:** What is launching, and how long a typical sale takes from first contact to
revenue.

**Also useful:** The business case or target outcome, the launch plan, the previous product's
launch results, what systems hold your data (CRM, billing, support tool, warranty or product
analytics), and who reviews results.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill asks what launched, how long a sale takes, and
what outcome the launch must produce, then proposes a metric set with every number left as a
labeled blank for you to fill. It will not make up your baselines.

**Example invocations:**
- `Launch metrics for the Route Optimizer. Self-serve add-on, 30-day trial, GA June 12.`
- `Audit this dashboard: trade fair leads, web visits, press mentions, units shipped to distributors.`

---

## Key Concepts

### Leading and Lagging Indicators

A **lagging indicator** reports a result after it happened: revenue, margin, retention, warranty
cost. It tells you whether the launch worked, usually too late to change the outcome. A **leading
indicator** moves first and predicts the lagging one: qualified quotes, trials started, accounts
that completed setup, first installations commissioned, repeat orders from pilot customers.

When a sale takes six to eighteen months, revenue at day 90 says almost nothing. A dashboard of
lagging indicators discovers the problem at the annual review, after the budget is set. **Pair each
lagging indicator with at least one leading indicator that should move first.**

### Four Categories, All Four

A launch can win in one category and fail in another.

| Category | Answers | Leading examples | Lagging examples |
|---|---|---|---|
| **Adoption** | Are customers buying and using it? | Qualified quotes, trials started, setup completed, units commissioned | Active accounts or installed base after trial, repeat orders |
| **Commercial** | Is it making money as planned? | Pipeline value, share of deals at list price, tender or specification wins | Revenue vs plan, win rate, price realization, gross margin |
| **Operational** | Can we deliver and support it? | On-time delivery or provisioning, first-time-right setup, support first-response time | Early-life failures, warranty or refund cost, tickets per customer or unit |
| **Customer** | Are they satisfied, and willing to say so? | Satisfaction at onboarding or commissioning, issues in the first weeks | Satisfaction at 6-12 months, reference willingness, renewal or contract churn |

Some metrics are **guardrails**, not goals. They don't show success, but if they break, the launch
is in trouble regardless of sales: warranty or refund rate, early-life failures, on-time delivery,
price realization. Hitting volume by discounting heavily, or by shipping what fails in the field,
has not succeeded.

### Baselines and Targets Need Sources

Without a baseline, a metric is an opinion. The baseline is the previous product's figure, the
current product in the same segment, an industry benchmark, or a pilot result, and each needs a
source. Every target needs a number, a date, a basis (baseline, benchmark, business case, pilot),
a source for that basis or `[NEEDS SOURCE]`, and an owner who agreed it.

**The team sets the targets.** This skill can point out that a target is far above the last
product's result, or that the business case assumes a win rate nobody has seen. It does not pick
the number.

### Intake Is Not Demand (Sell-In vs. Sell-Through)

In channel businesses the first orders are often partners stocking up: **sell-in**. That is not
customer demand. **Sell-through** (partner sales to end customers) and installations or active
usage show whether customers are buying. The SaaS equivalent is **seats purchased vs. seats
activated**, or **trials started vs. trials that reached the first valuable outcome**. A strong
first quarter of intake that hides a stalled sell-through is the commonest launch mirage. Track
both. Judge adoption on the second.

### Early Failures Show Up Fast

New products fail early before they settle: hardware shows early-life failures (the front of the
reliability "bathtub curve"), software shows onboarding drop-off and first-month incidents. These
are among the fastest signals a launch gives. Track them from the first customer, by cause, and
agree in advance what rate triggers escalation to engineering and quality.

### The 30, 90, and 180-Day Reviews

Each review has a different job:

- **30 days: is the launch running?** Mostly leading and operational signals: delivered, set up,
  support load, early failures, first feedback. Fix execution.
- **90 days: is it on track?** Leading commercial signals (pipeline, quotes, sell-through, trial
  conversion), adoption, quality trends, price realization. Adjust go-to-market.
- **180 days: is it working?** First lagging results against plan: revenue, win rate, margin,
  warranty or refund cost, satisfaction. Decide: on course, larger correction, or leadership
  attention. Hand findings forward.

For long-cycle capital equipment, add a 12-month review for lagging commercial results.

### Decision Triggers: Agree the Response Before the Result

A dashboard that prompts no action is a filing exercise. For each metric agree three ranges in
advance:

- **Stay the course:** within the expected range.
- **Adjust:** off track but within the team's authority to fix. Named owner, named action.
- **Escalate:** far off track or a guardrail broken. Goes to the forum with decision rights, with
  options.

This prevents rationalizing ("it's still early") and overreacting to noise. With small volumes,
one large deal can swing a metric: say how many data points a trigger needs before it fires.

### Fewer Metrics, Named Sources, Named Owners

Eight to twelve metrics across the four categories is usually enough. Each names the system it
comes from and the person who reports it. A metric with no source is a metric nobody collects.

### Funnel and Cohort Views

**Funnel (AARRR, adapted).** Dave McClure's Acquisition, Activation, Retention, Revenue, Referral
funnel travels well once you translate it:

| Stage | Consumer-app meaning | Your meaning (examples) |
|---|---|---|
| **Acquisition** | Visitors | SaaS: qualified trials started. Industrial: target accounts engaged, quotes issued |
| **Activation** | First good experience | SaaS: first route optimized. Industrial: first unit commissioned |
| **Retention** | Return users | SaaS: active after day 30, renewals. Industrial: units in use, service contracts renewed |
| **Revenue** | Paying users | Orders vs plan, price realization, attach rate |
| **Referral** | Invites | Reference customers, site visits hosted, specifications that name the product |

The point is the **conversion between stages**: many quotes and few orders is a price, proof, or
buying-group problem; many orders and few activations is an onboarding or delivery problem; strong
activation and weak renewal is a value problem.

**Cohort view.** A cohort is a group with a shared starting point (customers who started in the
launch month, who came through partners, who got release 1.0). Follow each over time in a table:
a row per cohort, a column per period (month 1, 3, 6), the metric in each cell. It answers what an
average cannot: do customers who started after we fixed onboarding retain better than the first
group? With small numbers, show the count beside every rate and don't conclude from a cohort of
three.

### The Post-Launch Review: Expected, Actual, Why, Change

The dashboard says what moved. The review says what you learn and do. Run each checkpoint as a
short structured conversation with function owners, not a slide read-out.

**Retro rundown.** For each metric in focus and each decision the launch plan made:

| Expected | Actual | Why the gap | What to change |
|---|---|---|---|
| What the plan said, with target and source | What happened, with data source | The team's explanation, labeled a hypothesis until checked | One owned action, or "no change" |

"Expected" comes from targets agreed before launch, **never rewritten after the result.** "Why" is
a hypothesis: if the team can't check it, it goes on the list to test, not into the findings.

**Rose, bud, thorn.** Numbers miss what the field sees. Before the rundown, each owner writes
observations alone: **rose** (working, protect it), **bud** (early opportunity, unproven),
**thorn** (friction hurting the launch now). Group into themes. Thorns become "why" candidates and
actions, buds become tests or roadmap input, roses become what the next launch keeps. Each
observation records who saw it. It is field evidence, not customer research. One report is one
data point.

If the launch plan ran a premortem, check its failure drivers at each review: did any start to
happen? A review that ends with sorted notes and no owners was a discussion, not a review. Both
techniques are adapted from the MITRE Innovation Toolkit.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not the ongoing product KPI system.** Launch metrics hand over to it.
- **Not the launch checklist.** See [`launch-plan`](../launch-plan/SKILL.md).
- **Not target-setting.** The team sets targets. This skill pressure-tests them.
- **Not a verdict.** AI does not make the stay, adjust, or escalate call on real results.

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** The artifact first: the metric set by category with baselines, targets,
sources, owners, and triggers, then the funnel, cohorts, and review plan. Commentary short, after.
Draft in two stages: **working draft** (every line tagged `[FROM YOU]`, `[RESEARCH]`, or
`[AI-SUGGESTED, VALIDATE THIS]`; every baseline, target, and threshold without a source
`[NEEDS SOURCE]`; AI-suggested metrics carry no numbers); then a **committed copy** with tags
removed, followed by a ranked **Riskiest Assumptions** list and a **Baselines to Collect** list.

**If the PM brings a dashboard, critique first.** Coverage across all four categories; each lagging
indicator paired with a leading one; activity metrics posing as results (leads, visits, mentions,
sessions held); intake reported as adoption; every baseline and target sourced and owned;
guardrails present; stay / adjust / escalate ranges on every metric. Name gaps. Offer rewrites last.

### Step 1: Confirm Scope
What launched, to which markets and channels, when; the outcome the launch must produce (from the
business case or roadmap); the sales cycle; who reviews results and decides on escalations.
**Guard against one-world metrics.** Defaults to daily active users and web funnels miss machines
and services; defaults to quotes and commissioning miss self-serve software. Ask what is physical,
what is service, and what is digital before suggesting metrics.

### Step 2: Gather Evidence
Offer **research** (published benchmarks, always with source and limits) and **your artifacts**
(business case, launch plan, previous launch results, CRM, billing, support and warranty data,
partner sell-through, pilot results). Either, both, or neither.

### Step 3: Choose the Metrics
Two to three per category, mixing leading and lagging, guardrails marked, eight to twelve in all.
Keep the user's; add missing ones tagged AI-suggested. Then define each funnel stage in this
product's terms, name the conversion that matters most and its source, and define the cohorts (by
start month, channel, or release) with the metric and periods to compare.

### Step 4: Set Baselines, Targets, Sources, Owners
For each metric: the exact definition, baseline and its source, target and its basis, system,
owner, frequency. List baselines to collect before launch.

### Step 5: Set the Triggers
Stay, adjust, escalate ranges per metric, with owner and likely response for the last two, and the
minimum data points before a trigger fires.

### Step 6: Plan the Reviews
For each of 30, 90, and 180 days (plus 12 months if long-cycle): date, attendees, metrics in focus,
the question it answers, the decision it can make, and the rose-bud-thorn and rundown format. When
the PM brings real results, lay out the rundown, check that "expected" matches what was agreed,
flag untested explanations, and check every thorn has an owner.

### Step 7: Hand Over
State which findings go forward, when launch metrics hand over to ongoing product metrics, and who
keeps the dashboard running after the last review.

### Step 8: Hand Back the Decision
Short summary (supplied, inferred, unknown), then a numbered decision ladder, evidence-favored
first, labeled `(Recommended)`: circulate the set to owners to confirm baselines and targets;
collect the missing baselines before launch; cut to the eight that matter most; align targets with
the business-case owner first.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight route optimizer, SaaS add-on) and
[`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield NFA-500 controller,
including the sell-in mirage).

---

## Common Pitfalls

### Pitfall 1: Only Lagging Indicators
**Symptom:** The launch is judged on revenue and share.
**Consequence:** With long cycles, problems surface at the annual review, too late to fix.
**Fix:** Pair every lagging indicator with a leading one.

### Pitfall 2: Activity Metrics Posing as Results
**Symptom:** The dashboard counts leads, visits, press mentions, and sessions held.
**Consequence:** The launch looks busy and successful while orders do not come.
**Fix:** Track what the activity should produce: qualified quotes, activations, installations, repeat orders.

### Pitfall 3: Intake Counted as Adoption
**Symptom:** Partner stocking orders, or seats purchased but never activated, reported as demand.
**Consequence:** A strong quarter hides weak real demand, then orders stop.
**Fix:** Track sell-through and activation separately from intake.

### Pitfall 4: No Guardrails
**Symptom:** No metrics for delivery, early failures, refunds or warranty, or price realization.
**Consequence:** Sales look good while the base generates cost and bad references.
**Fix:** Add guardrails from the first customer, with thresholds agreed with quality and support.

### Pitfall 5: Targets Without a Basis
**Symptom:** "Win rate 40%" with no baseline, benchmark, or business case.
**Consequence:** A miss can't be read: failed launch or wishful target?
**Fix:** Every target has a basis and a source, or stays `[NEEDS SOURCE]`.

### Pitfall 6: Triggers Written After the Results
**Symptom:** The response to each result is decided in the review meeting.
**Consequence:** Bad results are rationalized and noise is overreacted to.
**Fix:** Agree ranges before launch, including data points needed before a trigger fires.

### Pitfall 7: Too Many Metrics
**Symptom:** Thirty metrics, no story.
**Consequence:** Nobody reads the dashboard and real signals drown.
**Fix:** Eight to twelve across four categories, each with a reason to exist.

### Pitfall 8: Metrics Nobody Collects
**Symptom:** No system or owner named, or the data cannot be queried.
**Consequence:** The first review has no data.
**Fix:** Name the system and owner, and test the report before launch.

### Pitfall 9: The Model Sets the Numbers
**Symptom:** An AI-drafted dashboard arrives with confident baselines and targets nobody supplied.
**Consequence:** The team commits to targets with no basis and judges the launch against them.
**Fix:** Every number is sourced or `[NEEDS SOURCE]`. The team sets the targets.

### Pitfall 10: Reviews That Explain Instead of Learn
**Symptom:** A slide read-out. "Expected" is quietly restated to match the result, every gap gets a
confident explanation nobody checks, and the meeting ends with no owners.
**Consequence:** The same thorns reappear at 180 days.
**Fix:** Run the rundown against targets agreed before launch, label every "why" a hypothesis until
checked, and close with owned actions tied to the triggers.

---

## References

### Skill Files
- [`template.md`](template.md): metric set, triggers, funnel, cohorts, review plan, review record
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`launch-plan`](../launch-plan/SKILL.md): upstream; dates, functions, and premortem drivers to watch
- [`saas-revenue-growth-metrics`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/saas-revenue-growth-metrics/SKILL.md) and [`saas-economics-efficiency-metrics`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/saas-economics-efficiency-metrics/SKILL.md): definitions for revenue and efficiency metrics
- [`finance-metrics-quickref`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/finance-metrics-quickref/SKILL.md): one-page lookup when a metric's formula is in doubt
- [`finance-based-pricing-advisor`](../finance-based-pricing-advisor/SKILL.md): upstream; list price that price realization measures against
- [`lifecycle-play-advisor`](../lifecycle-play-advisor/SKILL.md): downstream; launch results can change the product's lifecycle stance
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Leading and lagging indicators:** Robert S. Kaplan and David P. Norton, *The Balanced Scorecard*.
- **Outcomes over activity:** Joshua Seiden, *Outcomes Over Output*.
- **Price realization:** Michael V. Marn and Robert L. Rosiello, "Managing Price, Gaining Profit," *Harvard Business Review* (1992).
- **AARRR:** Dave McClure, "Startup Metrics for Pirates" (2007), adapted here.
- **Early-life failures:** the reliability "bathtub curve."
- **Retro rundown and rose, bud, thorn:** adapted from the MITRE Innovation Toolkit (itk.mitre.org).

### Provenance
Distilled from practitioner experience measuring launches and running post-launch reviews.
