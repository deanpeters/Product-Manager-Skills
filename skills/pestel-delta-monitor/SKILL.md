---
name: pestel-delta-monitor
argument-hint: "[prior PESTEL analysis, and any suspected events since]"
description: "Quarterly re-scan of a prior PESTEL analysis. Use when checking which macro factors moved, which assumptions broke, and what's new — turning PESTEL from a workshop artifact into a radar."
intent: >-
  Refresh a PESTEL analysis by diffing each factor against the prior run and reporting material
  movement only — regulation passed, thresholds crossed, technology matured, assumptions broken.
  Macro factors move slowly; the value is catching the two that moved, not re-debating the twenty
  that did not.
type: workflow
theme: market-intelligence
best_for:
  - "Keeping a PESTEL analysis alive on a quarterly cadence instead of letting it rot in a deck"
  - "Catching which macro assumptions your strategy quietly depends on — and which just broke"
  - "Feeding regulatory and macro shifts into roadmap and OKR conversations with citations"
scenarios:
  - "Here's the PESTEL we did in Q1 — what's moved since?"
  - "A new regulation just passed in our space; re-run the macro scan against our baseline"
estimated_time: "15-30 min per run"
---

# PESTEL Delta Monitor

## Purpose

Refresh a PESTEL analysis by diffing each factor — Political, Economic, Social, Technological,
Environmental, Legal — against the prior run and reporting **material movement only**: **search plan
→ factor-by-factor diff → broken assumptions → new entrants to the frame → next-step options.** Macro
factors move slowly, which is exactly why teams stop looking; the value of a cadence is catching the
two factors that moved, not re-debating the twenty that didn't. Diffing also reveals which baseline
entries were live assumptions versus furniture — **broken assumptions are the real output.**

## Input

**Works best with:** the prior PESTEL analysis (pasted or attached) and the product/market scope it
covered — this skill *requires* a baseline to diff against.
**Also useful:** any events since the last run you already suspect matter — they get checked first.

Input supplied inline with the invocation — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as answers already given. Use it against the question budget;
don't re-ask.

**Arriving empty-handed?** This is the one investigation skill with a hard prerequisite: with no
baseline, it recommends running [`pestel-analysis`](../pestel-analysis/SKILL.md) first and stops —
there is nothing to diff. (That referral *is* the empty-handed path: you leave knowing exactly what
to do first.)

**Example invocation:** `PESTEL delta against the attached Q1 analysis — scope is our EU payments
product; I suspect the new AI liability directive matters.`

## Key Concepts

- **Governing protocol:** honors the [`autonomous-investigation`](../autonomous-investigation/SKILL.md)
  contract — question budget of 2, search-plan gate, Fact/Inference/Assumption labels, Just Enough
  Mode, stable schema, 4-option Final Step. Disciplines: GEOINT/DEMOINT statistics plus FININT
  regulatory sources (see [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md));
  this is the annual/quarterly layer of the fusion cadence.
- **Materiality for macro factors:** regulation passed *or credibly proposed*, macro indicators
  crossing thresholds your baseline named, technology maturation with adoption evidence, social
  signals with data behind them. "No material movement" per factor is a valid and *common* result —
  a quiet quarter reported honestly keeps the radar trusted.
- **Broken assumptions are the headline.** A baseline entry now contradicted by evidence outranks
  ten new observations, because strategy was built on it. The diff exists to find these.
- **Assumptions vs. furniture.** Entries that never move and touch no decision were furniture —
  flag them for retirement at the next baseline refresh rather than re-scanning them forever.
- **Scope changes break diffs.** New market, pivot, fundamentally different business context → redo
  the full PESTEL; never diff across a scope change.
- **Do-not-invent list:** regulations, statistics, dates, events. Real URLs and dates on everything —
  invented regulation is this domain's signature fabrication risk.

## Application

1. **Check the prerequisite.** No prior PESTEL → recommend [`pestel-analysis`](../pestel-analysis/SKILL.md)
   and stop. Scope changed since the baseline → recommend a fresh full analysis and stop.
2. **Credit inline context**, then ask only the unanswered questions (max 2):
   1. Prior PESTEL to paste?
   2. Any events since then you already suspect matter?
3. **Read the prior analysis fully; diff factor by factor** — the baseline document is the diff
   target, not your general knowledge of the macro environment.
4. **Show the 3-bullet search plan** — which factor categories get active searching this cycle
   (suspected events first), source types (government and regulatory sources, central-bank and
   statistical data, credible news, industry bodies, standards organizations), fact/inference
   separation. Continue unless revised.
5. **Emit the schema below exactly.**

### Output schema (do not reorder)

~~~markdown
# PESTEL Delta Report

## 1. Run Header
**Scope (from prior analysis):** | **Prior analysis date:** | **This run date:**

## 2. Factor-by-Factor Delta
For each of P / E / S / T / E / L:
### [Factor]: [moved / no material movement]
- **What moved:** [1-2 bullets, labeled, cited — only if moved]
- **Prior assumption affected:** [which entry from the baseline]
- **Reading:** [Inference — implication for the product scope]

Keep "no material movement" factors to a single line each.

## 3. Broken Assumptions
- [Baseline entries now contradicted by evidence — the run's most important section; cited]

## 4. New to the Frame
- [Factors absent from the baseline that now warrant a slot]

## 5. So What?
- **3** implications for strategy or roadmap
- **2** factors to watch closely next cycle
- **3** assumptions to validate
Each bullet: label, confidence, URL where relevant.
~~~

### Final Step (offer exactly 4 options)

1. Update the baseline PESTEL with these deltas (new baseline)
2. Deep-dive the most consequential moved factor
3. Trace the broken assumptions into roadmap or OKR impact
4. Set next cycle's watch priorities

Accept `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`, or a custom path.

## Examples

**A factor that moved, traced to its assumption (fictional):**

> ### Legal: moved
> - **What moved:** the data-residency provision cleared committee with an 18-month compliance
>   window — **Fact** ([legislature record, URL, date])
> - **Prior assumption affected:** baseline entry L2 assumed "no residency mandate before 2028,"
>   which justified deferring the regional storage architecture
> - **Reading:** the deferral logic is dead — **Inference**: the architecture decision moves from
>   someday to next two roadmap quarters, and compliance becomes a sales asset in regulated verticals
>   before it's a legal obligation.

**A quiet quarter reported honestly:** five factors show "no material movement" at one line each;
one Economic entry moved (a rate-path shift crossing the baseline's stated budget-gate threshold).
The report is half a page. That brevity *is* the radar working — the reader spends two minutes and
knows the strategy's macro floor held except where it didn't.

## Common Pitfalls

- **Re-debating the unmoved.** Rewriting all six factors every quarter turns the radar back into
  the workshop it was meant to replace. One line per quiet factor — the discipline is the product.
- **Materiality inflation.** Promoting think-pieces and proposals-going-nowhere into "movement."
  The bar is passed/credibly-proposed regulation, crossed thresholds, adoption evidence — not
  discourse.
- **Burying broken assumptions.** Listing deltas without connecting them to the baseline entries
  they contradict. The "prior assumption affected" line is what makes a delta actionable.
- **Diffing across a pivot.** The business entered a new market and the monitor keeps diffing the
  old scope's factors. Scope change = new baseline, always.
- **Invented specificity.** A regulation name, effective date, or statistic that doesn't check out.
  In this domain a fabricated citation isn't just wrong, it's a compliance risk for the reader —
  the do-not-invent list is load-bearing.

## References

- [`pestel-analysis`](../pestel-analysis/SKILL.md) (Component) — builds the baseline this monitor
  diffs against; the pair turns PESTEL into an operating radar
- [`autonomous-investigation`](../autonomous-investigation/SKILL.md) (Workflow) — the governing protocol
- [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) (Component) — GEOINT/DEMOINT statistical sources; regulatory registries
- [`derisk-measurement-advisor`](../derisk-measurement-advisor/SKILL.md) (Interactive) — consumes broken assumptions as risk inputs
- [`competitive-intel-watch`](../competitive-intel-watch/SKILL.md) (Workflow) — the competitor-level sibling of this macro-level watch
- Adapted from `market-intelligence/pestel-delta-monitor-prompt.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
