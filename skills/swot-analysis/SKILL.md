---
name: swot-analysis
argument-hint: "[company and scope, and the decision it supports]"
description: "Build an evidence-cited SWOT of one company — yours or a competitor's — from public sources, ending with the S-O/W-T crossings. Use for strategy reviews, board prep, or competitor depth."
intent: >-
  An evidence-cited SWOT from the public record: strengths and weaknesses from documented capability
  and customer voice, opportunities and threats from market and macro signals — every entry labeled
  and sourced, closing with the S-O attack and W-T exposure crossings that most SWOTs skip.
type: workflow
theme: market-intelligence
best_for:
  - "Strategy reviews and board prep that need a defensible read on one company's position"
  - "Competitor depth after a snapshot has identified who matters"
  - "Partnership or acquisition evaluation grounded in evidence, not impressions"
scenarios:
  - "SWOT our biggest competitor before the strategy offsite — from public evidence"
  - "We're evaluating a partnership with [company]; what does the public record say about their position?"
estimated_time: "20-35 min per run"
---

# SWOT Analysis (Evidence-Cited)

## Purpose

Build an evidence-cited SWOT of one company — yours or a competitor's — from the public record:
**use or gather evidence → four labeled quadrants → crossings → next-step options.** Strengths and
weaknesses come from documented capability and customer voice; opportunities and threats from market,
competitor, and macro signals. Every entry carries a source and a label, and the analysis ends with
the S-O and W-T crossings — because a SWOT without "so what" is a parking lot with four sections.

## Input

**Works best with:** the company to analyze, the scope (whole company or one product line/market),
and **the decision this SWOT should support**.
**Also useful:** the perspective — theirs, or yours competing with them — and any research already in
session (a [`competitive-research-snapshot`](../competitive-research-snapshot/SKILL.md), VoC themes, a
landscape scan, [`company-intel`](../company-intel/SKILL.md) output): the SWOT then *synthesizes*
instead of re-searching.

Input supplied inline with the invocation — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as answers already given. Use it against the question budget;
don't re-ask.

**Arriving empty-handed? That works too.** The skill opens with at most 3 questions (company + scope,
decision, perspective) and proceeds on labeled assumptions if they go unanswered.

**Example invocation:** `Evidence-cited SWOT on [Competitor A]'s mid-market product line, from our
perspective — supports the Q3 positioning refresh. Last month's snapshot is attached.`

## Key Concepts

- **Governing protocol:** honors the [`autonomous-investigation`](../autonomous-investigation/SKILL.md)
  contract — question budget of 3, search-plan gate, Fact/Inference/Assumption labels, Just Enough
  Mode (max 5 ranked entries per quadrant), stable schema, 4-option Final Step. Disciplines: OSINT +
  FININT + HUMINT per [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md).
- **Quadrant discipline.** S and W are *internal and current*; O and T are *external*. The most
  common SWOT error is an "opportunity" that requires the company to act — that's a strategy, not an
  opportunity. Flag it when you catch it; catching it is half the teaching.
- **Claimed vs. evidenced advantage.** Strengths sourced from the company's own marketing are
  claims; strengths corroborated by customer voice, filings, or independent coverage are evidence.
  Customer voice weighs heaviest on weaknesses — buyers document weaknesses vendors won't.
- **The crossings are the deliverable.** S-O names the attack (which strength unlocks which
  opportunity); W-T names the exposure (which weakness a threat finds first). SWOT is an input to
  moves, not a wall poster.
- **Companion, not substitute:** [`porters-five-forces`](../porters-five-forces/SKILL.md) reads the
  *industry's* structure; this reads *one company's* position within it. Run both when the decision
  is market entry.
- **When NOT to use:** internal-only SWOT from private knowledge → run it as a team workshop with
  your evidence; the whole competitor set → snapshot first, SWOT the one or two that matter.
- **Do-not-invent list:** financials, customer wins, market share, product claims, roadmap items.

## Application

1. **Check session for existing evidence** (snapshot, VoC themes, landscape scan, company-intel).
   Present → synthesize from it; search only gaps and staleness.
2. **Credit inline context**, then ask only the unanswered questions (max 3):
   1. Which company, and whole-company or one product line?
   2. What decision should this support?
   3. From whose perspective — theirs, or yours competing with them?
3. **If researching fresh, show the 3-bullet search plan** — source sweep (filings, reviews, press,
   pricing pages, hiring signals), how internal vs. external evidence will be separated, how facts
   split from inference. Continue unless revised.
4. **Emit the schema below exactly.**

### Output schema (do not reorder)

~~~markdown
# SWOT: [Company / Scope]
**As-of date:** | **Decision supported:** | **Perspective:**

## 1. Strengths (internal, evidenced)
- [Entry] — [evidence: URL, date] — [Fact/Inference]
- [Max 5, ranked by defensibility]

## 2. Weaknesses (internal, evidenced)
- [Entry — customer voice weighs heaviest here] — [URL] — [label]
- [Max 5, ranked by exploitability]

## 3. Opportunities (external)
- [Entry — market/macro signal] — [URL] — [label]
- [Max 5, ranked by fit to their strengths]

## 4. Threats (external)
- [Entry — competitor/regulatory/technology signal] — [URL] — [label]
- [Max 5, ranked by likelihood x damage]

## 5. The Crossings (the "so what")
- **S-O (attack):** [strength that unlocks which opportunity — 1-2 moves, labeled Inference]
- **W-T (exposure):** [weakness a threat will find first — 1-2 risks, labeled Inference]
- **For your decision:** [what this SWOT says about the decision named above, in 2 sentences]

### Assumptions to Validate
- [Assumption 1] / [Assumption 2] / [Assumption 3]
~~~

A copy/paste fill-in version of this schema, with quality checks, lives in [`template.md`](template.md).

### Final Step (offer exactly 4 options)

1. Run the W-T exposure into a battle card or risk plan ([`battle-card-builder`](../battle-card-builder/SKILL.md))
2. SWOT a second company for side-by-side comparison
3. Feed the crossings into a positioning statement ([`positioning-statement`](../positioning-statement/SKILL.md))
4. Schedule-ready version: which entries should a quarterly re-run watch?

Accept `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`, or a custom path.

## Examples

**The quadrant discipline catching a disguised strategy (fictional):**

> Draft opportunity: "expand into the compliance-automation segment." Caught and reclassified — that
> requires *them* to act, so it's a candidate strategy, not an opportunity. The underlying
> opportunity, restated externally: "compliance-automation demand in their install base is growing —
> **Fact** ([industry survey, URL]) — and no incumbent serves it." Now the S-O crossing can test
> whether any *documented strength* (their services arm, their audit-trail architecture) actually
> unlocks it — or whether it's a mirage that flatters the roadmap.

**Claimed vs. evidenced, side by side:**

> - Their site claims "enterprise-grade reliability" — that's a claim, not a strength.
> - Strength as evidenced: "publishes a status page with 26 months of >99.95% uptime — **Fact**
>   ([status page, URL]) — and reliability praise recurs across independent reviews — **Fact**
>   ([review site, URL])." Ranked #2 by defensibility: verifiable, sustained, hard to copy quickly.

See [`examples/sample.md`](examples/sample.md) for a complete worked SWOT (fictional FSM-software
market, same scenario as the suite's chain examples) that synthesizes from a snapshot and watch
report already in session. [`examples/sample-industrial.md`](examples/sample-industrial.md) runs the
same quadrant discipline on an industrial evidence diet, including a fortress-move warning in the
S-O crossing.

## Common Pitfalls

- **The four-box brainstorm.** Unsourced entries from a conference room are opinions arranged in
  quadrants. Evidence per entry is what separates this SWOT from the one nobody trusts.
- **Opportunities that are strategies.** "Launch in Europe" is a move; "European demand outpacing
  local supply" is an opportunity. If the entry needs the company to act, reclassify it.
- **Marketing-sourced strengths.** A strengths quadrant built from the company's own website is
  their positioning statement wearing your logo. Corroborate or label as claim.
- **Skipping the crossings.** Four tidy quadrants and no moves. The S-O attack and W-T exposure are
  why the analysis exists — the decision-support sentence at the end is the test it must pass.
- **Wish-list contamination.** Internal hopes ("we'd love better onboarding") placed in W, or
  fears in T, without evidence. Every quadrant works the public record; wishes go to the roadmap.

## References

- [`autonomous-investigation`](../autonomous-investigation/SKILL.md) (Workflow) — the governing protocol
- [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) (Component) — the evidence channels behind each quadrant
- [`porters-five-forces`](../porters-five-forces/SKILL.md) (Workflow) — industry structure; run both for market-entry decisions
- [`competitive-research-snapshot`](../competitive-research-snapshot/SKILL.md) (Workflow) — upstream evidence base
- [`voice-of-customer-miner`](../voice-of-customer-miner/SKILL.md) (Workflow) — the weaknesses quadrant's best source
- [`positioning-statement`](../positioning-statement/SKILL.md) (Component) — consumes the crossings
- SWOT framework as standard strategy practice; adapted from
  `market-intelligence/swot-analysis-prompt.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
