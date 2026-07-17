---
name: competitive-intel-watch
argument-hint: "[prior snapshot (pasted/attached), and anything specific to watch]"
description: "Scheduled delta monitoring against a prior competitive snapshot. Use when tracking competitors on a cadence: material shifts only, cited evidence, battle-card update flags, runs unattended."
intent: >-
  A competitive intelligence delta monitor: given a previous Competitive Research Snapshot, sweep for
  material shifts since the last run and report only what changed — a cited changelog plus flags naming
  which battle card or positioning sections now need updating. Designed to run unattended on a loop or
  schedule; an empty changelog is a valid, useful result.
type: workflow
theme: market-intelligence
best_for:
  - "Keeping battle cards and positioning current without regenerating research weekly"
  - "Running unattended on a schedule and reporting only changes a rep or roadmap owner would act on"
  - "Turning competitive research from a one-off deliverable into a standing capability"
scenarios:
  - "Run this against last quarter's snapshot and tell me what actually changed"
  - "Set up a monthly competitor watch that flags when our battle card goes stale"
estimated_time: "10-25 min per run (after the baseline exists)"
---

# Competitive Intel Watch

## Purpose

Monitor a competitive landscape for **material shifts** since the last run. Diff the world against the
previous snapshot; report only what changed, with evidence; flag which downstream artifacts need
updating. This is the skill that turns competitive research from a document into a cadence — the
weekly SIGINT sweep and monthly OSINT digest from the fusion cadence live here. A watch reports
*change*, not *state*: regenerating the same report weekly is theater, and "no material shifts this
cycle" is a valid, useful result.

## Input

**Works best with:** the previous Competitive Research Snapshot (pasted or attached) — the baseline
this run diffs against — and the competitor list (defaults to those in the snapshot).
**Also useful:** anything specific you're watching for this cycle, and a materiality bar adjustment if
the default needs tightening or loosening.

Input supplied inline with the invocation — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as answers already given. Use it against the question budget;
don't re-ask.

**Arriving empty-handed? That works too.** With no prior snapshot, the skill falls back to **baseline
mode**: it produces a first snapshot using the `competitive-research-snapshot` structure and stops —
the delta value starts on run two.

**Example invocation:** `Competitive intel watch — prior snapshot pasted below; this cycle I'm
specifically watching for pricing moves. [snapshot]`

## Key Concepts

- **Governing protocol:** honors the [`autonomous-investigation`](../autonomous-investigation/SKILL.md)
  contract — question budget of 2 (this skill's tightest), search-plan gate, Fact/Inference/Assumption
  labels, Just Enough Mode, stable schema, 4-option Final Step.
- **Discipline mix:** SIGINT first (site diffs, pricing pages, job posts — the freshest layer), with
  OSINT and HUMINT signals monthly and FININT on the quarterly pass — the fusion cadence in
  [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) is this
  skill's operating rhythm.
- **The materiality bar.** Report a change only if a sales rep, pricing owner, or roadmap owner would
  plausibly act on it: pricing/packaging changes, launches and deprecations, positioning shifts,
  leadership moves, funding or M&A, major customer wins/losses, credible roadmap signals. Below the
  bar: cosmetic site changes, routine content marketing, minor releases. *Why it matters:* a watch
  that cries wolf gets ignored by cycle three — the bar is what keeps the audience.
- **Delta discipline.** Read the prior snapshot fully before searching; diff against it, never
  regenerate it. The empty changelog is a first-class outcome.
- **Update flags close the loop.** Research is only done when it names the artifact it changes — each
  material shift maps to the battle card, positioning, pricing, or roadmap sections now stale.
- **Do-not-invent list:** competitors, features, pricing, market share, customer wins, roadmap items,
  product claims. Every claimed change carries a URL *and a date*.
- **When NOT to use:** no baseline exists and you want the full treatment → run
  [`competitive-research-snapshot`](../competitive-research-snapshot/SKILL.md) first; the scope itself
  changed (new segment, pivot) → re-snapshot from scratch rather than diffing a stale scope.

## Application

1. **Determine mode.** Prior snapshot provided → delta mode. None → baseline mode: produce a
   snapshot per the `competitive-research-snapshot` schema and stop.
2. **Credit inline context**, then ask only the unanswered questions (max 2):
   1. Do you have the previous snapshot, or should I create a baseline?
   2. Anything specific you're watching for this cycle?
   If unanswered, proceed: baseline mode if no snapshot, default materiality bar otherwise.
3. **Read the prior snapshot fully before searching.** The diff target is the document, not your
   memory of the market.
4. **Show the 3-bullet search plan** — what you'll check per competitor, source types (company sites,
   pricing pages, release notes, press, investor materials, credible news, review sites, job
   postings), how facts will be separated from inference. Continue unless revised.
5. **Sweep and filter through the materiality bar.** When nothing clears it, say so plainly.
6. **Emit the schema below exactly** — runs must be diffable.

### Output schema (do not reorder)

~~~markdown
# Competitive Watch Report

## 1. Run Header
**Scope (from prior snapshot):** | **Prior snapshot date:** | **This run date:** | **Competitors checked:**

## 2. Changelog (Material Shifts Only)
For each material shift:
### [Competitor] — [4 to 8 word change summary]
- **What changed:** [1-2 bullets, labeled Fact/Inference]
- **Evidence:** [URL, date]
- **So what:** [why it clears the materiality bar]
- **Confidence:** [high / medium / low]

If nothing cleared the bar: "No material shifts this cycle." List
anything on the watchlist for next run.

## 3. Update Flags
| Downstream artifact | Sections needing update | Driven by |
|---|---|---|
| Battle card | | |
| Positioning statement | | |
| Pricing/packaging analysis | | |
| Roadmap assumptions | | |
Only rows with real updates; omit the rest.

## 4. Watchlist for Next Run
- [Signals below the bar but trending]
- [Open questions this run could not resolve]

### Assumptions to Validate
- [Assumption 1] / [Assumption 2] / [Assumption 3]
~~~

A copy/paste fill-in version of this schema, with quality checks, lives in [`template.md`](template.md).

### Final Step (offer exactly 4 options)

1. Update the battle card sections flagged above ([`battle-card-builder`](../battle-card-builder/SKILL.md))
2. Deep-dive the most significant change
3. Produce the refreshed full snapshot (new baseline)
4. Adjust the materiality bar or competitor list for next run

Accept `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`, or a custom path. On a scheduled, unattended
run, file the report and stop — the options wait for a human.

## Examples

**A changelog entry that clears the bar (fictional):**

> ### Ledgerline — mid-tier plan removed from pricing page
> - **What changed:** the $49 "Team" tier no longer appears; feature list redistributed upward —
>   **Fact** ([pricing page vs. archived version, Jul 2 vs. Jun 1](https://example.com/archive))
> - **Evidence:** URL + archive diff, dated
> - **So what:** entry price effectively doubled; our "cheaper to start" talking point is now
>   stronger, and their SMB churn may spike — clears the bar for both sales and pricing owners
> - **Confidence:** high

**The empty changelog done right:**

> No material shifts this cycle. Below-the-bar activity logged for trend: [Competitor B] published
> three thought-leadership posts on compliance automation (watchlist: possible positioning shift if
> their product pages follow), and two senior-engineer job posts mention a language we haven't seen
> in their stack before (watchlist: TECHINT corroboration needed before this means anything).

See [`examples/sample.md`](examples/sample.md) for a complete worked run (fictional FSM-software
market) that diffs against the `competitive-research-snapshot` example's baseline — including an
assumption from that baseline getting confirmed by the diff. [`examples/sample-industrial.md`](examples/sample-industrial.md)
shows the quarterly-cadence industrial version, where a top risk gets *demoted* and that's
reported as material.

## Common Pitfalls

- **Regeneration theater.** Producing a fresh full report each run and calling it a watch. The
  reader's question is "what changed?" — answer only that.
- **Materiality inflation.** Reporting blog posts and minor releases to seem productive. Every
  below-bar item reported costs credibility the real alerts will need later.
- **Fear of the empty changelog.** Padding a quiet cycle with noise. "No material change" backed by a
  real sweep is exactly what a healthy watch produces most cycles.
- **Undated evidence.** A change claim without both URL and date can't be verified *or diffed next
  run*. The date is half the evidence.
- **Diffing a stale scope.** The market pivoted, you entered a new segment — and the watch keeps
  diffing the old frame. Re-baseline when the scope changes; say so in the run header.
- **Orphaned intelligence.** A changelog with no update flags. If no artifact needs updating, the
  shift probably didn't clear the bar — flags are how research becomes action.

## References

- [`autonomous-investigation`](../autonomous-investigation/SKILL.md) (Workflow) — the governing protocol
- [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) (Component) — the fusion cadence this watch runs on
- [`competitive-research-snapshot`](../competitive-research-snapshot/SKILL.md) (Workflow) — produces the baseline this skill diffs against
- [`battle-card-builder`](../battle-card-builder/SKILL.md) (Workflow) — consumes the update flags
- [`pestel-analysis`](../pestel-analysis/SKILL.md) (Component) — the macro-environment sibling of this competitor-level watch
- Adapted from `market-intelligence/competitive-intel-watch-prompt.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
