---
name: battle-card-builder
argument-hint: "[your product vs which competitor, and the deal context]"
description: "Research and draft a competitive battle card from public evidence — every claim labeled and sourced. Use when a rep needs a field-action card, not a research report."
intent: >-
  Autonomous battle card construction: given your product and one competitor, the AI does the fieldwork
  — pricing pages, reviews, release notes, customer stories — and produces a field-action card with a
  source URL and Fact/Inference/Assumption label on every claim, sized to a rep's thirty seconds.
type: workflow
theme: market-intelligence
best_for:
  - "Arming sales against one competitor with claims they can actually defend"
  - "Turning a competitive snapshot or watch report into a field-action artifact"
  - "Building trap questions whose documented answers favor you"
scenarios:
  - "We keep hitting the same rival in enterprise deals — build the battle card from public evidence"
  - "Our battle card is six months old and sales stopped trusting it; rebuild it with sources"
estimated_time: "20-35 min per run"
---

# Battle Card Builder

## Purpose

Build a field-action competitive battle card from public evidence: **use or gather evidence → search
plan (if gathering) → draft card with per-claim labels → appendix → next-step options.** A battle
card is the artifact a rep opens mid-deal, not a research report — it must fit thirty seconds, every
claim must survive being said out loud to a hostile audience, and every claim therefore carries a
source URL, a date, and a Fact/Inference/Assumption label. Most battle cards in the wild are unlabeled
inference; this skill exists because of what it costs a rep when one of those turns out wrong.

## Input

**Works best with:** your product and its primary differentiation, and **the one competitor** this
card targets.
**Also useful:** the deal context (segment, buyer, common objections or the loss reason that triggered
this card), and any [`competitive-research-snapshot`](../competitive-research-snapshot/SKILL.md) or
[`competitive-intel-watch`](../competitive-intel-watch/SKILL.md) output in session — the skill uses
existing evidence and searches only for gaps and anything older than one quarter.

Input supplied inline with the invocation — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as answers already given. Use it against the question budget;
don't re-ask.

**Arriving empty-handed? That works too.** The skill opens with at most 3 questions (product +
competitor, segment + buyer, triggering objection) and proceeds on labeled assumptions if they go
unanswered.

**Example invocation:** `Build a battle card: our workflow platform vs [Competitor A], mid-market ops
buyers — triggered by three straight losses on "their integrations are deeper."`

## Key Concepts

- **Governing protocol:** honors the [`autonomous-investigation`](../autonomous-investigation/SKILL.md)
  contract — question budget of 3, search-plan gate, Fact/Inference/Assumption labels, Just Enough
  Mode, stable schema, 4-option Final Step.
- **Discipline mix:** SIGINT (pricing pages, site diffs — the freshest layer, what keeps cards from
  going stale) + OSINT (review mining for objection handling) + HUMINT (win/loss ground truth when
  you have it) — see [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md).
- **Field-action criterion.** Every element earns its place by being usable mid-conversation. Depth
  goes in the appendix; the card fits a rep's thirty seconds.
- **Trap questions are evidence work.** A trap question is only safe to ask when you *know the
  documented answer* — offense is built from citations, not bravado. "Never ask what you cannot
  evidence" is the section's law.
- **The "Do Not Say" section is protection.** Claims you can't evidence, or that invite a counter,
  are listed explicitly — the card protects the rep from the team's own folklore.
- **Two modes, one artifact.** This skill builds the card from *the world's* evidence
  (investigation); a facilitated workshop builds it from *your team's* evidence (win/loss knowledge,
  deal experience). The mode choice depends on where the evidence lives — bring rich internal
  win/loss knowledge to a facilitated session instead, and use this skill when the public record is
  the stronger source.
- **Do-not-invent list:** features, pricing, market share, customer wins, roadmap items, **quotes**.

## Application

1. **Check session for existing evidence** — a competitive snapshot or watch report. If present, use
   it as the evidence base; search only for gaps and freshness (older than one quarter).
2. **Credit inline context**, then ask only the unanswered questions (max 3):
   1. Your product, and the one competitor this card targets?
   2. What segment and buyer do these deals involve?
   3. What objection or loss reason triggered this card?
   If unanswered, proceed with labeled assumptions.
3. **If researching fresh, show the 3-bullet search plan** — what you'll check (pricing pages,
   release notes, reviews, customer stories, comparison content), source types, how facts will be
   separated from inference. Continue unless revised.
4. **Draft the card in the schema below exactly** — cards are diffable across runs, and the watch
   skill's update flags name these sections.

### Card schema (do not reorder)

~~~markdown
# Battle Card: [Your Product] vs [Competitor]
**As-of date:** | **Deal context:** [segment, buyer]

## 1. Thirty-Second Read
- **They win when:** [1-2 bullets, labeled]
- **We win when:** [1-2 bullets, labeled]
- **The one thing to say:** [a single defensible sentence]

## 2. Say This
- [Talking point] — [evidence: URL, date, label]
- [Max 4; every one sourced]

## 3. Ask This (trap questions)
- "[Question whose documented answer favors us]" — [the documented answer: URL, label]
- [Max 3; never ask what you cannot evidence]

## 4. Watch Out For
- [Their strength a rep should not walk into] — [URL, label]
- [Their likely counter to our pitch] — [Inference, basis]

## 5. Pricing & Packaging Snapshot
- [Their tiers/pricing as published] — [URL, as-of date]
- [Where "contact sales" hides the number] — [labeled]

## 6. Do Not Say
- [Claims we cannot evidence, or that invite a counter]

## Appendix: Evidence Table
| Claim | Label | Source | Date |
|---|---|---|---|

### Assumptions to Validate
- [Assumption 1] / [Assumption 2] / [Assumption 3]
~~~

A copy/paste fill-in version of this schema, with quality checks, lives in [`template.md`](template.md).

### Final Step (offer exactly 4 options)

1. Pressure-test the card: role-play the competitor's rep against it
2. Build the card for a second competitor
3. Set up [`competitive-intel-watch`](../competitive-intel-watch/SKILL.md) to keep this card current
4. Compress to a one-screen mobile version for the field

Accept `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`, or a custom path.

## Examples

**A trap question built correctly (fictional):**

> **Ask this:** "How does your migration handle custom fields over the 200-field limit?" — documented
> answer: their own docs state custom-field migration caps at 200 with manual re-entry beyond it —
> **Fact** ([docs page, checked Jul 2026](https://example.com/docs)). Safe to ask: the answer is in
> their documentation, so the rep isn't bluffing — they're citing.

**A "Do Not Say" entry earning its keep:**

> - Don't say "they can't do SSO on the starter tier" — they shipped it in June
>   ([release notes](https://example.com/changelog)); a rep repeating our old card walks into a
>   correction that costs the room's trust.
> - Don't lead with "we're cheaper" — true only below 50 seats ([their pricing](https://example.com/pricing),
>   [ours](https://example.com/our-pricing)); above that the math flips, and enterprise buyers check.

See [`examples/sample.md`](examples/sample.md) for a complete worked card (fictional FSM-software
market) rebuilt from the `competitive-intel-watch` example's update flags — the full chain landing
in a field artifact. [`examples/sample-industrial.md`](examples/sample-industrial.md) builds the
industrial version, where the channel partner is a card audience and pricing is opaque.

## Common Pitfalls

- **The unlabeled card.** Talking points without sources are folklore with formatting. The label is
  what tells a rep how hard they can lean on a claim when the buyer pushes back.
- **The research-report card.** Two pages of landscape context a rep will never read mid-deal. Thirty
  seconds is the budget; the appendix exists for everything else.
- **Trap questions on hope.** Asking a question whose answer you haven't documented hands the
  competitor a stage. If the evidence isn't in the appendix table, the question doesn't ship.
- **Quote invention.** A fabricated customer quote or paraphrased review presented as verbatim is the
  fastest way to destroy the card's credibility — and it's on the do-not-invent list for exactly that
  reason.
- **The immortal card.** Cards rot at SIGINT speed — pricing pages and release notes change monthly.
  A card without an as-of date, or without a watch feeding it update flags, is a liability wearing a
  logo.
- **Skipping "Do Not Say."** The section that protects reps from the team's own stale folklore is the
  one most often omitted — usually because nobody wants to write down which beloved claims are dead.

## References

- [`autonomous-investigation`](../autonomous-investigation/SKILL.md) (Workflow) — the governing protocol
- [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) (Component) — discipline sources; SIGINT keeps this card fresh
- [`competitive-research-snapshot`](../competitive-research-snapshot/SKILL.md) (Workflow) — upstream evidence base
- [`competitive-intel-watch`](../competitive-intel-watch/SKILL.md) (Workflow) — flags when this card's sections go stale
- [`positioning-statement`](../positioning-statement/SKILL.md) (Component) — the strategic layer the card's talking points should agree with
- Adapted from `market-intelligence/battle-card-builder-prompt.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
