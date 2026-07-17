---
name: ansoff-matrix
argument-hint: "[company or product line, its current core, and the growth outcome sought]"
description: "Map evidence-backed growth options across the Ansoff Matrix with risk-rated sequencing. Use when the question is where the next tranche of growth comes from, and at what risk."
intent: >-
  A researched Ansoff Matrix, not a brainstorm grid: market penetration, market development, product
  development, and diversification, each quadrant populated with candidate moves backed by documented
  signals, risk ratings that respect the matrix's risk gradient, and a recommended sequence with the
  assumption that breaks it.
type: workflow
theme: market-intelligence
best_for:
  - "Answering 'where does the next tranche of growth come from?' with evidence per option"
  - "Forcing diversification proposals to carry the evidence burden their risk demands"
  - "Sequencing growth moves so early wins fund the riskier bets"
scenarios:
  - "Growth planning for next year — map our options across the Ansoff quadrants with evidence"
  - "The board wants a diversification story; pressure-test it against what the signals actually support"
estimated_time: "25-40 min per run"
---

# Ansoff Matrix (Evidence-Backed)

## Purpose

Map a company's growth options across the Ansoff Matrix with evidence per quadrant: **use or gather
evidence → four quadrants with signals → risk-rated sequence → next-step options.** The four
quadrants — market penetration, market development, product development, diversification — organize
one question: *where does the next tranche of growth come from, and at what risk?* This is a research
instrument, not wishful whiteboarding: every candidate move must answer "what documented signal says
this demand exists?" And the close is a sequence, because growth options compound — penetration funds
development, and diversification bets the funding.

## Input

**Works best with:** the company or product line seeking growth, its **current core** (who is served,
with what, at what scale — the matrix's axes are defined relative to it), and the growth outcome and
horizon on the table.
**Also useful:** constraints (capital, capability, risk appetite), and any research in session — a
landscape scan, five-forces read, or [`company-intel`](../company-intel/SKILL.md) output lets the
matrix organize evidence instead of gathering it.

Input supplied inline with the invocation — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as answers already given. Use it against the question budget;
don't re-ask.

**Arriving empty-handed? That works too.** The skill opens with at most 3 questions (core, outcome
and horizon, constraints) and proceeds on labeled assumptions if they go unanswered.

**Example invocation:** `Ansoff growth options for our field-service product line — core: dispatch
software for mid-market HVAC firms, US. Outcome: +40% ARR in 24 months. Constraint: no acquisitions.`

## Key Concepts

- **Governing protocol:** honors the [`autonomous-investigation`](../autonomous-investigation/SKILL.md)
  contract — question budget of 3, search-plan gate, Fact/Inference/Assumption labels, Just Enough
  Mode (2-3 moves per quadrant), stable schema, 4-option Final Step.
- **The framework (Ansoff, 1957):** growth options plotted on two axes — existing vs. new *products*,
  existing vs. new *markets*. Penetration (existing/existing) is the lowest-risk quadrant;
  diversification (new/new) the highest, because it abandons both anchors of proven demand at once.
- **The risk gradient is law.** Penetration < market development ≈ product development <
  diversification. A diversification move rated "low risk" needs extraordinary evidence — and the
  gradient teaches why diversification proposals deserve the heaviest evidence burden and usually
  arrive with the lightest.
- **Signals, not wishes.** Candidate moves come from documented signals: underserved-segment data,
  expressed demand ([`voice-of-customer-miner`](../voice-of-customer-miner/SKILL.md) themes),
  competitor precedent, capability evidence. An empty diversification quadrant is an acceptable
  answer; an invented one is not.
- **Coaching vs. investigation — same map, different jobs:**
  [`organic-growth-advisor`](../organic-growth-advisor/SKILL.md) is the Interactive sibling that
  *diagnoses your growth constraint* through questions (its Growth Path Matrix shares Ansoff's
  axes); this skill *researches the evidence* for each quadrant's options. Diagnose there, evidence
  here — they pair deliberately.
- **When NOT to use:** feature-level prioritization (this is portfolio altitude — use
  [`feature-investment-advisor`](../feature-investment-advisor/SKILL.md) for a single build
  decision); no growth mandate or capacity — an options map without an owner is a poster.
- **Do-not-invent list:** market sizes, adoption data, competitor results, demand claims. Where
  sizing matters, flag it for [`tam-sam-som-calculator`](../tam-sam-som-calculator/SKILL.md) rather
  than guessing.

## Application

1. **Check session for existing evidence** (landscape scan, five forces, company intel, VoC). Present
   → the matrix organizes it; search only gaps.
2. **Credit inline context**, then ask only the unanswered questions (max 3):
   1. Which company or product line, and what is its current core?
   2. What growth outcome and horizon is on the table?
   3. Any constraints — capital, capability, risk appetite?
3. **If researching fresh, show the 3-bullet search plan** — what you'll search per quadrant
   (segment data, expressed demand, competitor precedents, capability signals), source types,
   fact/inference separation. Continue unless revised.
4. **Populate the quadrants and emit the schema below exactly.**

### Output schema (do not reorder)

~~~markdown
# Ansoff Growth Options: [Company / Product Line]
**As-of date:** | **Current core:** | **Growth outcome sought:**

## 1. Market Penetration (existing product, existing market — lowest risk)
- **[Candidate move]** — signal: [evidence, URL, label] — risk: [low/med/high, why]
- [2-3 moves]

## 2. Market Development (existing product, new market)
- **[Candidate move: segment, geography, or channel]** — signal: [evidence of underserved demand, URL, label] — risk: [rating, why]
- [2-3 moves]

## 3. Product Development (new product, existing market)
- **[Candidate move]** — signal: [expressed demand, VoC theme, competitor precedent, URL, label] — risk: [rating, why]
- [2-3 moves]

## 4. Diversification (new product, new market — highest risk)
- **[Candidate move]** — signal: [the extraordinary evidence this quadrant requires, URL, label] — risk: [rating, why]
- [1-2 moves; an empty quadrant is an acceptable answer]

## 5. Recommended Sequence (the "so what")
- **First:** [move] — because [evidence strength + funding logic]
- **Then:** [move] — funded/de-risked by the first
- **Not yet:** [the tempting move and why the evidence says wait]
- **The assumption that breaks this sequence:** [one line]

### Assumptions to Validate
- [Assumption 1] / [Assumption 2] / [Assumption 3]
~~~

A copy/paste fill-in version of this schema, with quality checks, lives in [`template.md`](template.md).

### Final Step (offer exactly 4 options)

1. Size the top move with TAM/SAM/SOM ([`tam-sam-som-calculator`](../tam-sam-som-calculator/SKILL.md)) (Recommended)
2. Pressure-test the sequence with a premortem
3. Deep-dive the diversification quadrant's evidence
4. Convert the first move into an opportunity solution tree ([`opportunity-solution-tree`](../opportunity-solution-tree/SKILL.md))

Accept `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`, or a custom path.

## Examples

**A quadrant entry earning its place (fictional):**

> ## 2. Market Development
> - **Adjacent trade: plumbing contractors, same size band** — signal: plumbing firms appear
>   unprompted in 14% of our category's review-site mentions asking "does this work for plumbing?" —
>   **Fact** ([review threads, URLs]); the two incumbents serving plumbing both gate scheduling
>   behind enterprise tiers — **Fact** ([pricing pages]) — risk: **medium** — demand signal is real
>   but second-hand; sales motion transfers, integrations don't fully.

**The sequence close doing its job:**

> - **First:** win-back campaign into the churned-but-reachable base (penetration) — strongest
>   evidence, funds everything else, 1-quarter payback
> - **Then:** plumbing-contractor entry (market development) — de-risked by the penetration win's
>   cash and case studies
> - **Not yet:** the IoT hardware bundle (diversification) — one analyst mention and founder
>   enthusiasm is not extraordinary evidence
> - **The assumption that breaks this sequence:** churned customers left for fixable reasons; if
>   win-loss shows they left the *category*, penetration is a dead first move and development leads.

See [`examples/sample.md`](examples/sample.md) for a complete worked matrix (fictional FSM-software
market) with an honestly empty diversification quadrant and a sequence whose breaking assumption is
named. [`examples/sample-industrial.md`](examples/sample-industrial.md) shows the opposite lesson: a
populated diversification quadrant whose entry fails the evidence bar in writing.

## Common Pitfalls

- **The brainstorm grid.** Four quadrants of unsourced ambition. Every move answers "what signal
  says this demand exists?" or it doesn't ship — that single rule converts Ansoff from wall art
  into an instrument.
- **Risk-gradient denial.** A diversification move rated low-risk on enthusiasm. The gradient is
  the framework's whole teaching: new product *and* new market means both anchors are gone.
- **Quadrant stuffing.** Filling diversification because empty feels lazy. An honestly empty
  quadrant is a finding; a padded one is a liability with a deadline.
- **Options without sequence.** A menu with no first move, no funding logic, no breaking
  assumption. Growth options compound — order is the strategy.
- **Sizing by vibe.** Attaching invented market sizes to moves. The do-not-invent list routes
  sizing to the TAM/SAM/SOM calculator, where the math shows its work.

## References

- [`organic-growth-advisor`](../organic-growth-advisor/SKILL.md) (Interactive) — the coaching
  sibling: diagnoses *which* growth path fits your constraint; this skill evidences the options
- [`autonomous-investigation`](../autonomous-investigation/SKILL.md) (Workflow) — the governing protocol
- [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) (Component) — signal sources per quadrant
- [`porters-five-forces`](../porters-five-forces/SKILL.md) (Workflow) — the profit-pool read that feeds this analysis
- [`tam-sam-som-calculator`](../tam-sam-som-calculator/SKILL.md) (Component) — sizes the moves
- [`voice-of-customer-miner`](../voice-of-customer-miner/SKILL.md) (Workflow) — expressed-demand signals for product development
- [`opportunity-solution-tree`](../opportunity-solution-tree/SKILL.md) (Interactive) — structures the first move's execution
- H. Igor Ansoff, "Strategies for Diversification" (Harvard Business Review, 1957)
- Adapted from `market-intelligence/ansoff-matrix-prompt.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
