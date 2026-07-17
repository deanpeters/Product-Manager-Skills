---
name: voice-of-customer-miner
argument-hint: "[whose customer voice, and the decision it informs]"
description: "Mine public reviews, app stores, and forums for unmet needs, competitor weaknesses, and switching triggers — with quoted evidence. Use when you want customer voice without waiting on interviews."
intent: >-
  Mine public customer voice for unmet needs, competitor weaknesses, and switching triggers, with real
  quoted verbatims and labeled inference. Bridges competitive intelligence and discovery: outputs feed
  JTBD canvases, opportunity solution trees, and battle cards — as hypotheses to validate, not verdicts.
type: workflow
theme: market-intelligence
best_for:
  - "Finding what users actually complain about and wish for — yours and competitors' — from the public record"
  - "Arming battle cards with competitor weaknesses in customers' own words"
  - "Seeding discovery interviews and opportunity trees with evidence-backed hypotheses"
scenarios:
  - "Mine the reviews of our top two competitors — what are their customers angriest about?"
  - "Before the interview cycle starts, what does the public web say our segment's unmet needs are?"
estimated_time: "20-35 min per run"
---

# Voice-of-Customer Miner

## Purpose

Mine public customer voice — review sites, app stores, Reddit and practitioner forums, community
boards — for unmet needs, competitor weaknesses, and switching triggers: **search plan → source sweep
→ verbatim capture → need themes → so what → next-step options.** This bridges competitive
intelligence and discovery: it delivers customers' exact words without waiting on an interview cycle.
But public voice skews toward the angry and the vocal, so every theme it surfaces is a *hypothesis to
validate*, never a verdict — the output's last stop is always a real conversation.

## Input

**Works best with:** the product(s) or competitor(s) to mine — yours, a rival's, or a set — and **the
decision this should inform**.
**Also useful:** a theme to focus on (onboarding, pricing, reliability) if you have one; otherwise the
sweep runs open.

Input supplied inline with the invocation — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as answers already given. Use it against the question budget;
don't re-ask.

**Arriving empty-handed? That works too.** The skill opens with at most 3 questions (whose voice,
what decision, theme or open sweep) and proceeds on labeled assumptions if they go unanswered.

**Example invocation:** `Mine voice-of-customer for [Competitor A] and [Competitor B], focus on
onboarding — informs whether our Q1 bet is a migration tool.`

## Key Concepts

- **Governing protocol:** honors the [`autonomous-investigation`](../autonomous-investigation/SKILL.md)
  contract — question budget of 3, search-plan gate, Fact/Inference/Assumption labels, Just Enough
  Mode, stable schema, 4-option Final Step. Discipline: OSINT's review-and-community layer (see
  [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md)).
- **Theme by need, not by feature.** "Exports are broken" is a feature complaint; "I can't get my
  data where my team works" is the underlying need. Theming by need is the same solution-free
  discipline as JTBD and painstorming — and it's what makes themes portable into discovery.
- **Verbatims are the product.** Short, real, quoted customer language with URLs. Verbatims teach
  persona language: the exact words customers use become interview probes and positioning copy.
  Never fabricate quotes, ratings, review counts, or reviewer roles.
- **Every source has a known skew.** Reviewers skew negative; vendor communities skew loyal; app
  stores over-represent update anger. Note the bias per source — public voice is evidence with a
  known skew, not ground truth.
- **Honest frequency.** *Recurring across sources* ≠ *concentrated in one thread* ≠ *isolated but
  vivid*. Say which; one articulate ranter is not a theme.
- **When NOT to use:** no meaningful public footprint (early-stage, niche enterprise) → run
  [`discovery-interview-prep`](../discovery-interview-prep/SKILL.md) instead; you need *your* users'
  voice on a private area → mine your own tickets and research; statistical confidence required →
  this is qualitative theming.

## Application

1. **Credit inline context**, then ask only the unanswered questions (max 3):
   1. Whose customer voice — yours, a competitor's, or a set?
   2. What decision should this inform?
   3. Any specific theme to focus on, or open sweep?
2. **Show the 3-bullet search plan** — which voice sources you'll sweep, how you'll select
   representative verbatims, how observation will be separated from interpretation. Continue unless
   revised.
3. **Sweep mixed voice sources** — review sites (G2, Capterra, TrustRadius), app stores, Reddit and
   practitioner forums, community boards, social threads — capturing short real quotes with URLs and
   noting each source's bias.
4. **Emit the schema below exactly.**

### Output schema (do not reorder)

~~~markdown
# Voice-of-Customer Snapshot

## 1. Scope
**Products mined:** | **Decision supported:** | **Sources swept:** | **As-of date:**

## 2. Need Themes
For each of the top 3-5 themes:
### Theme: [Underlying need, solution-free, 4 to 8 words]
- **Frequency:** [recurring across sources / concentrated / isolated]
- **Verbatim:** "[short real quote]" — [source, URL]
- **Verbatim:** "[short real quote]" — [source, URL]
- **Who says it:** [role/segment, if evident — labeled]
- **Reading:** [Inference — what this suggests]

## 3. Competitor Weak Points
- **[Competitor]:** [weakness in customers' words; frequency; URL]
- [Max 5, strongest evidence only]

## 4. Switching Triggers
- [What pushes customers off a product; what pulls them; labeled, cited]

## 5. So What?
- **3** opportunity hypotheses (phrased as problems, not features)
- **2** battle-card-ready weaknesses (with evidence quality noted)
- **3** assumptions to validate in real interviews
Each bullet: label, confidence, URL where relevant.
~~~

A copy/paste fill-in version of this schema, with quality checks, lives in [`template.md`](template.md).

### Final Step (offer exactly 4 options)

1. Generate discovery interview questions from the top theme ([`discovery-interview-prep`](../discovery-interview-prep/SKILL.md))
2. Feed the weaknesses into a competitive battle card ([`battle-card-builder`](../battle-card-builder/SKILL.md))
3. Build an opportunity solution tree from the top hypothesis ([`opportunity-solution-tree`](../opportunity-solution-tree/SKILL.md))
4. Re-run scoped to one theme in Verbose Mode

Accept `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`, or a custom path.

## Examples

**A theme done right (fictional product, illustrative verbatims):**

> ### Theme: getting historical data out at contract end
> - **Frequency:** recurring — 9 reviews across two sites plus a forum thread, past 6 months
> - **Verbatim:** "export took three support tickets and still dropped custom fields" — [G2-style review, URL]
> - **Verbatim:** "we stayed a year longer than we wanted because leaving meant losing our audit trail" — [forum thread, URL]
> - **Who says it:** ops managers at 50-200-person firms — **Inference** (reviewer titles where shown)
> - **Reading:** exit friction is functioning as involuntary retention — **Inference**; a rival with
>   effortless migration turns this from their moat into their churn event.

Notice the theme name contains no feature ("export tool") — it names the need, so discovery can
explore solutions the reviews never imagined.

See [`examples/sample.md`](examples/sample.md) for a complete worked mining run (fictional
FSM-software market) where frequency honesty caps a vivid theme at low confidence and each
source's bias becomes a reading instruction. [`examples/sample-industrial.md`](examples/sample-industrial.md)
shows the thin-voice case — what honest mining looks like when the market barely posts reviews.

## Common Pitfalls

- **Feature-name theming.** Clustering by the feature customers blame instead of the need underneath
  hands your roadmap to the loudest UI complaint.
- **Verbatim laundering.** Paraphrasing a review and quoting it. If it has quote marks, it must be a
  real excerpt at a real URL — this domain's do-not-invent list exists because fabricated customer
  quotes are both tempting and toxic.
- **Rant amplification.** One vivid one-star review presented as a theme. Frequency honesty is the
  discipline: recurring, concentrated, or isolated — say which.
- **Skew blindness.** Reading review sites as a census. The angry and the vocal are over-sampled;
  the satisfied-and-silent majority never posts. Bias notes per source are mandatory.
- **Skipping the validation handoff.** Shipping themes straight into the roadmap. The output's
  "assumptions to validate in real interviews" section is the bridge to discovery — use it.

## References

- [`autonomous-investigation`](../autonomous-investigation/SKILL.md) (Workflow) — the governing protocol
- [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) (Component) — OSINT review-mining sources and bias tradecraft
- [`jobs-to-be-done`](../jobs-to-be-done/SKILL.md) (Component) — the solution-free framing themes should land in
- [`discovery-interview-prep`](../discovery-interview-prep/SKILL.md) (Interactive) — where the validation happens
- [`opportunity-solution-tree`](../opportunity-solution-tree/SKILL.md) (Interactive) — structures the opportunity hypotheses
- [`battle-card-builder`](../battle-card-builder/SKILL.md) (Workflow) — consumes the weak points
- Adapted from `market-intelligence/voice-of-customer-miner-prompt.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
