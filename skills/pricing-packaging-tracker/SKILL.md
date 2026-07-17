---
name: pricing-packaging-tracker
argument-hint: "[competitor set, and prior capture if one exists]"
description: "Track competitor pricing and packaging as a diffable time series. Use when monitoring tiers, gates, limits, and price moves on a monthly or quarterly cadence."
intent: >-
  Capture competitor public pricing pages into a stable schema, diff against the prior capture, and
  report tier changes, price moves, feature-gate shifts, and packaging restructures with URLs and
  dates — because packaging changes signal strategy earlier than price changes do.
type: workflow
theme: market-intelligence
best_for:
  - "Keeping battle-card pricing sections current without manual screenshot archaeology"
  - "Catching packaging restructures — the earliest public signal of a strategy shift"
  - "Building the pricing time series that grounds your own pricing decisions"
scenarios:
  - "Baseline the pricing pages of our four main competitors, then track monthly"
  - "Did anyone in our space change pricing or packaging this quarter?"
estimated_time: "15-30 min per run"
---

# Pricing & Packaging Tracker

## Purpose

Track competitor pricing and packaging as a **diffable time series**, not a screenshot: **capture (or
diff) → structure changes → price changes → signals → next-step options.** The stable capture schema
is the point — run N diffs against run N-1, so the report is what *moved*, with evidence. And the
skill watches structure as closely as numbers, because packaging changes (gates, limits, tier
restructures) usually signal strategy earlier than price changes do: a tier that disappears telegraphs
a move upmarket months before the price list admits it.

## Input

**Works best with:** the competitor set to track (or the snapshot they came from), and the prior
pricing capture if one exists — that's what turns this run into a delta report.
**Also useful:** your own pricing context, if the comparison should include you.

Input supplied inline with the invocation — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as answers already given. Use it against the question budget;
don't re-ask.

**Arriving empty-handed? That works too.** With no prior capture the skill runs **baseline mode**:
full capture per competitor, and the delta value starts next run. With no competitor list, it asks —
that's one of its two budget questions.

**Example invocation:** `Pricing tracker on [Competitor A], [Competitor B], [Competitor C] — prior
capture from April pasted below.`

## Key Concepts

- **Governing protocol:** honors the [`autonomous-investigation`](../autonomous-investigation/SKILL.md)
  contract — question budget of 2, Fact/Inference/Assumption labels, Just Enough Mode, stable schema,
  4-option Final Step. Discipline: SIGINT (pricing pages, site diffs) with FININT corroboration — see
  [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md).
- **Time series, not screenshot.** A single capture is trivia; the sequence is intelligence. The
  schema never drifts between runs, because diffability is the entire value.
- **Structure over numbers.** Record tiers, billing units, feature gates, usage limits, free-tier
  boundaries, and enterprise-floor signals — not just prices. The gate moves first; the price
  follows.
- **"Contact sales" is data, honestly labeled.** Where pricing is opaque, track what *is* public
  (editions, gates, published floors) and mark the rest. Infer only with labels; never invent
  prices, tiers, limits, discounts, or negotiated figures.
- **When NOT to use:** you need pricing *strategy* advice →
  [`finance-based-pricing-advisor`](../finance-based-pricing-advisor/SKILL.md) (this tracks the
  market; it doesn't set your price); pricing is fully opaque across the whole set → expect thin
  results, and consider [`voice-of-customer-miner`](../voice-of-customer-miner/SKILL.md) or win/loss
  evidence instead.

## Application

1. **Determine mode.** Prior capture provided → delta mode (report changes only). None → baseline
   mode (full capture, then stop).
2. **Credit inline context**, then ask only the unanswered questions (max 2):
   1. Which competitors' pricing should I track?
   2. Prior capture to diff against, or is this the baseline?
3. **Capture from live pricing pages** — plan-comparison pages, published rate cards, credible
   pricing-change coverage — with URL and as-of date per competitor.
4. **Emit the schema below exactly** — diffability is the point.

### Output schema (do not reorder)

~~~markdown
# Pricing Capture / Delta Report

## 1. Run Header
**Competitor set:** | **Prior capture date:** [or "baseline run"] | **This run date:**

## 2. Pricing Capture (per competitor)
### [Competitor] — [pricing page URL, as-of date]
- **Tiers:** [name: price / unit / billing terms, one bullet each]
- **Key gates:** [which capabilities gate which tier, 2-4 bullets]
- **Usage limits:** [the limits that matter, 1-2 bullets]
- **Free tier / trial:** [boundary, 1 bullet]
- **Enterprise signals:** [published floors, "contact sales" scope]

(Baseline mode: full capture per competitor. Delta mode: this section
only for competitors with changes.)

## 3. Changes Since Last Capture (Delta Mode)
### [Competitor] — [4 to 8 word change summary]
- **Then / Now:** [old -> new, labeled Fact]
- **Evidence:** [URL, date]
- **Reading:** [Inference — repositioning, monetization push, response to whom?]

If nothing changed: "No pricing or packaging changes this cycle."

## 4. Signals
- [Cross-competitor patterns: direction of the market's pricing, labeled]
- [Implications for your pricing or battle cards: 2-3 bullets]

### Assumptions to Validate
- [Assumption 1] / [Assumption 2] / [Assumption 3]
~~~

A copy/paste fill-in version of this schema, with quality checks, lives in [`template.md`](template.md).

### Final Step (offer exactly 4 options)

1. Update battle card pricing sections from these changes ([`battle-card-builder`](../battle-card-builder/SKILL.md))
2. Deep-dive one competitor's packaging logic
3. Compare your pricing against this capture
4. Set the cadence and watchlist for the next run

Accept `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`, or a custom path.

## Examples

**A delta entry reading structure, not just price (fictional):**

> ### [Competitor B] — API access moved from Pro to new Scale tier
> - **Then / Now:** API access included in Pro ($79/seat) → gated behind new "Scale" tier
>   ($149/seat, 10-seat minimum) — **Fact**
> - **Evidence:** [pricing page vs. archived capture, URL, dates]
> - **Reading:** the price didn't change; the *gate* did. Developer-led accounts are being pushed
>   into a sales conversation — **Inference**: monetization push on their fastest-growing usage
>   pattern, and a window for us with API-first buyers while their community absorbs it.

**The cross-competitor signal:** three of four tracked competitors added usage-based add-ons this
quarter while holding seat prices flat — **Inference:** the market is testing consumption pricing
without headline price increases. Your pricing debate is no longer hypothetical; the Signals section
names the evidence.

See [`examples/sample.md`](examples/sample.md) for a complete worked delta run (fictional
FSM-software market) where both material moves are structural — a new tier and a relocated gate —
and no headline price changed at all. [`examples/sample-industrial.md`](examples/sample-industrial.md)
shows the fully opaque case: zero published prices, and structure as the only public signal.

## Common Pitfalls

- **Screenshot thinking.** Capturing once and calling it competitive pricing intel. The value
  compounds only on a cadence — baseline, then diff, forever.
- **Number fixation.** Reporting only price changes while a tier quietly gained a 5-seat minimum.
  Structure is the leading indicator; watch the gates.
- **Inventing the opaque.** Filling "contact sales" cells with plausible figures. Publish the
  honest boundary and label any inference — a battle card built on invented enterprise pricing
  detonates in a live deal.
- **Schema improvisation.** Reordering or "improving" the capture format between runs breaks every
  future diff. The schema is a contract with your own future runs.
- **Tracking without a consumer.** If no battle card, pricing review, or watch report consumes the
  output, the cadence dies quietly. Wire the Final Step's first option into a real artifact.

## References

- [`autonomous-investigation`](../autonomous-investigation/SKILL.md) (Workflow) — the governing protocol
- [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) (Component) — SIGINT sources: Wayback diffs, pricing-page monitoring
- [`competitive-intel-watch`](../competitive-intel-watch/SKILL.md) (Workflow) — the broader watch this tracker feeds
- [`battle-card-builder`](../battle-card-builder/SKILL.md) (Workflow) — consumes the pricing snapshot sections
- [`finance-based-pricing-advisor`](../finance-based-pricing-advisor/SKILL.md) (Interactive) — sets *your* price; this skill informs it with market evidence
- Adapted from `market-intelligence/pricing-packaging-tracker-prompt.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
