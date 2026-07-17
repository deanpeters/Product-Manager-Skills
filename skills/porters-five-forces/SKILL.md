---
name: porters-five-forces
argument-hint: "[industry or segment, and the decision it supports]"
description: "Read an industry's structure through Porter's Five Forces with documented signals per rating, ending at the profit pool. Use when weighing market entry or when margins erode and nobody can say why."
intent: >-
  An evidence-cited five-forces read: rivalry, new entrants, substitutes (with AI-driven substitution
  named explicitly), buyer power, and supplier power — each force rated weak/moderate/strong with the
  documented signals that justify the rating, closing with where the profit pool sits and who is
  squeezing it.
type: workflow
theme: market-intelligence
best_for:
  - "Pressure-testing a market-entry decision against the industry's actual structure"
  - "Explaining margin erosion structurally instead of blaming execution"
  - "Grounding strategy debates in rated forces with evidence, not vibes"
scenarios:
  - "We're considering entering the clinical-data-management space — what does its structure do to everyone who plays?"
  - "Our margins keep compressing and every explanation is tactical; give me the structural read"
estimated_time: "25-40 min per run"
---

# Porter's Five Forces (Evidence-Cited)

## Purpose

Read an industry's structure through Porter's Five Forces, with evidence: **search plan →
force-by-force ratings with signals → profit-pool implication → next-step options.** Each force —
competitive rivalry, threat of new entrants, threat of substitutes, buyer power, supplier power — is
rated weak/moderate/strong and justified with documented signals, because a rating without signals is
vibes. The analysis closes where it should have been aiming all along: **where the profit pool sits
and who is squeezing it.** Five forces is an argument about where margin goes, not a diagram for
slide four.

## Input

**Works best with:** the industry or segment, named as precisely as you can ("clinical data
management SaaS," not "healthcare"), and **the decision this analysis should support**.
**Also useful:** a geographic boundary if the structure differs by region, and a
[`market-landscape-scan`](../market-landscape-scan/SKILL.md) in session — the forces read builds on
it and searches only gaps.

Input supplied inline with the invocation — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as answers already given. Use it against the question budget;
don't re-ask.

**Arriving empty-handed? That works too.** The skill opens with at most 3 questions (segment,
decision, boundary) and proceeds on labeled assumptions if they go unanswered.

**Example invocation:** `Five forces on mid-market field-service management software, North America —
decision: whether we enter or partner.`

## Key Concepts

- **Governing protocol:** honors the [`autonomous-investigation`](../autonomous-investigation/SKILL.md)
  contract — question budget of 3, search-plan gate, Fact/Inference/Assumption labels, Just Enough
  Mode (2-4 signals per force), stable schema, 4-option Final Step. Disciplines: FININT
  (concentration, margins, filings) + OSINT (analyst coverage, trade press) per
  [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md).
- **The framework (Porter, 1979):** industry profitability is determined by five structural forces,
  not by how hard incumbents work. Rivalry sets the intensity of margin competition; entry threat
  caps pricing; substitutes cap value; buyer power extracts margin downstream; supplier power
  extracts it upstream. Structure explains what negotiation skill cannot: **pricing power is
  structural.**
- **Ratings must survive "how do you know?"** Each weak/moderate/strong rating stands on documented
  signals — concentration data, switching costs, entry examples and how they fared, substitute
  adoption curves, margin trends. Forces-with-signals is the difference between naming a framework
  and using one.
- **AI-driven substitution is a named candidate, always.** In most knowledge industries it is now
  *the* substitute threat; assess it explicitly in the substitutes force rather than letting the
  analysis pretend it's 2015. Supplier power gets the same modern read: cloud, model, and platform
  dependencies are supplier concentration.
- **Industry, not player:** this reads what the structure does to *everyone* who plays.
  [`swot-analysis`](../swot-analysis/SKILL.md) reads one company's position within it.
- **When NOT to use:** nascent categories with no stable structure — the forces are still forming;
  run the landscape scan and revisit.
- **Do-not-invent list:** market share, margin data, entrant names, funding rounds, adoption figures.

## Application

1. **Credit inline context**, then ask only the unanswered questions (max 3):
   1. Which industry or segment, precisely?
   2. What decision should this support?
   3. Any geographic boundary?
2. **Show the 3-bullet search plan** — what you'll search per force, source types (filings, analyst
   coverage, trade press, pricing pages, funding databases), fact/inference separation. Continue
   unless revised. If a landscape scan is in session, build on it; search only gaps.
3. **Rate each force with signals, then emit the schema below exactly.**

### Output schema (do not reorder)

~~~markdown
# Five Forces: [Industry / Segment]
**As-of date:** | **Boundary:** | **Decision supported:**

## 1. Competitive Rivalry — [weak / moderate / strong]
- Signals: [concentration, growth rate, differentiation, exit barriers — each with URL + label]
- What it means here: [one sentence]

## 2. Threat of New Entrants — [weak / moderate / strong]
- Signals: [entry barriers, capital needs, recent entrants and how they fared, regulation — each with URL + label]
- What it means here: [one sentence]

## 3. Threat of Substitutes — [weak / moderate / strong]
- Signals: [substitute adoption, price-performance trajectory, switching evidence — each with URL + label]
- AI-driven substitution, named and assessed: [labeled]
- What it means here: [one sentence]

## 4. Buyer Power — [weak / moderate / strong]
- Signals: [buyer concentration, switching costs, price transparency, backward-integration examples — URL + label]
- What it means here: [one sentence]

## 5. Supplier Power — [weak / moderate / strong]
- Signals: [supplier concentration (including cloud/model/platform dependencies), input differentiation — URL + label]
- What it means here: [one sentence]

## 6. The Profit Pool (the "so what")
- Where margin sits today, and the force squeezing it: [labeled]
- Structure trend: [tightening / loosening, on what evidence]
- For your decision: [2 sentences tying structure to the decision named above]

### Assumptions to Validate
- [Assumption 1] / [Assumption 2] / [Assumption 3]
~~~

### Final Step (offer exactly 4 options)

1. Trace the strongest force into your strategy's exposed assumptions
2. Run [`market-landscape-scan`](../market-landscape-scan/SKILL.md) to name the players behind each force
3. Feed the profit-pool read into an Ansoff growth-options analysis ([`ansoff-matrix`](../ansoff-matrix/SKILL.md))
4. Schedule-ready version: which force signals should a re-run watch?

Accept `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.

## Examples

**A rating that survives "how do you know?" (fictional):**

> ## 4. Buyer Power — strong
> - Signals: top 10 buyers account for ~60% of segment spend — **Fact** ([trade association data,
>   URL]); three publicized incumbent-to-rival switches in 18 months with no reported penalty —
>   **Fact** ([press coverage, URLs]); public rate cards make pricing fully transparent — **Fact**
>   ([vendor pricing pages]); one major buyer built the capability in-house — **Fact** ([their
>   engineering blog, URL])
> - What it means here: buyers can credibly threaten to leave or build, so list-price integrity is
>   an illusion in this segment — discounting pressure is structural, not a sales-discipline problem.

**The profit-pool close doing its job:** rivalry moderate, entrants weak, substitutes strong (AI
agents absorbing the low-complexity tier), buyers strong, suppliers moderate. The pool sits in the
regulated high-complexity tier — the only place two strong forces don't reach — **Inference**. For
the entry decision: enter *only* via the regulated tier; the volume tier's margin is already spoken
for by buyers below and AI substitution above.

## Common Pitfalls

- **Ratings as vibes.** "Rivalry: strong" because it feels crowded. Every rating stands on signals
  with URLs, or the whole exercise is a diagram.
- **Skipping the AI substitute.** Assessing substitutes as adjacent products while an AI workflow
  eats the category's low end. Name it and rate it, even when the rating is "weak — for now."
- **Confusing competitors with structure.** Listing who plays (that's the landscape scan) instead of
  what the structure does to everyone who plays. The forces are about margin physics, not rosters.
- **No profit-pool close.** Five rated forces and no answer to "where does margin go?" The close is
  the analysis; everything above it is evidence assembly.
- **Forcing structure onto a nascent category.** Rating forces that haven't formed yet produces
  confident noise. Say "still forming," scan the landscape, revisit in two quarters.

## References

- [`autonomous-investigation`](../autonomous-investigation/SKILL.md) (Workflow) — the governing protocol
- [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) (Component) — FININT/OSINT sources behind the signals
- [`market-landscape-scan`](../market-landscape-scan/SKILL.md) (Workflow) — who plays; this skill asks what the structure does to them
- [`swot-analysis`](../swot-analysis/SKILL.md) (Workflow) — one company's position within the structure
- [`ansoff-matrix`](../ansoff-matrix/SKILL.md) (Workflow) — growth options informed by the profit-pool read
- Michael E. Porter, "How Competitive Forces Shape Strategy" (Harvard Business Review, 1979)
- Adapted from `market-intelligence/porters-five-forces-prompt.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
