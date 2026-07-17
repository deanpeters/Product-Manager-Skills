# Autonomous Investigation Protocol — In Action

All companies, products, URLs, and figures are **fictional**. This example shows the protocol's
clauses firing in sequence during one investigation — including the moment most examples skip: the
user **revising the search plan at the gate**, and what an honest gaps list looks like when the
world doesn't cooperate. The scenario matches the suite's other examples (Fieldlight, a trades
scheduling tool investigating the FSM market).

---

## 1. The invocation credits the budget

> **User:** Run an investigation on DispatchCrow's expansion trajectory — this supports our
> decision on how fast to ship quoting. I already know they raised a Series A in January.

Two of the three budget questions (target, decision) arrived inline; the known fact is credited as
context. One question remains in budget, and the skill spends it well:

> **Agent:** One question before I plan the search: is the decision about *whether* to ship
> quoting, or *when*? The evidence bar differs — "whether" needs demand proof, "when" needs their
> velocity read.

> **User:** When. Whether is decided.

## 2. The search-plan gate — and a revision

> **Agent:** **Search plan** (say "revise" to change it):
> - Sweep DispatchCrow's changelog, careers page, and blog for shipping velocity and roadmap signals
> - Source mix: their site, funding coverage, review sites, practitioner forums
> - Facts get URLs; interpretations get labeled Inference; gaps become Assumptions to validate

> **User:** Revise — add their app store release notes. Their web changelog lags the mobile app.

> **Agent:** Good catch — app store release histories added as a SIGINT source. Proceeding.

Ten seconds of plan review just improved the run. That's the gate doing its job — redirecting a
plan is cheap; redirecting a finished report is not.

## 3. Labeled findings, a stack, and an honest gaps list

> **Key findings:**
> - Shipped quoting Nov 2025, payments Apr 2026 — five months between module launches — **Fact**
>   ([changelog](https://example.com/dispatchcrow/changelog))
> - App store release cadence doubled since the Series A: 2-week cycles now — **Fact**
>   ([release history](https://example.com/appstore/dispatchcrow))
> - Two senior dispatch hires from the category incumbent in July — **Fact**
>   ([their blog](https://example.com/dispatchcrow/blog/dispatch-team))
> - Payments moved down a pricing tier in July — **Fact** ([pricing archive diff](https://example.com/archive))
>
> **The stack (3 channels agree):** faster release cadence (SIGINT) + dispatch-specialist hires
> (HUMINT) + payments repositioned as volume play (SIGINT-pricing) → they are building toward the
> dispatch-led mid-market *now*, funded by payments volume — **actionable intelligence**, not a
> watch item.
>
> **Reading for your decision:** their module gap was five months. If capacity planning started at
> the July hires, expect it Q1 2027 — **Inference** (their own historical cadence). Your quoting
> window is roughly two quarters — **Inference**.
>
> **Gaps (couldn't find, not guessed):**
> - No revenue or payments-volume figures anywhere public — their take-rate economics are unknowable from outside
> - No beta signups or docs for capacity planning yet — the Q1 2027 date rests entirely on cadence inference
>
> **Final Step — reply 1, 2, 3, 4, a combination, or "Verbose Mode":**
> 1. Set up a `competitive-intel-watch` tripwire on their capacity-planning beta
> 2. Deep-dive their payments economics from processor partnerships
> 3. Trace this timeline into our roadmap assumptions
> 4. Discovery questions to validate the two-quarter window

## 4. The same skill, unattended

Three months later the same invocation runs on a schedule. No human answers; the budget is spent
silently (context was saved inline), the gate auto-continues with the revised plan (app store
sources included — the revision persisted because it was part of the saved invocation), and the
output lands in the same schema. The team reads the *diff*: release cadence held, a
"capacity view (beta)" line appeared in the app store notes — the tripwire from option 1 fires,
one quarter earlier than the inference predicted.

---

## Why this example works

- **Every clause of the contract appears under load.** Budget credited by inline context, one
  question spent surgically, the gate catching a source gap, labels on every claim, a 3-channel
  stack graded "actionable," a gaps list instead of invented figures, exactly 4 closing options.
- **The gaps list is the do-not-invent list working.** Payments economics were unknowable, so the
  report says *unknowable* — the tempting move (a plausible-sounding take-rate estimate) would have
  poisoned the roadmap math downstream.
- **The unattended run shows why the clauses exist.** Question budget, auto-continuing gate, and
  stable schema are exactly the three properties that let the scheduled run happen at all — and the
  diff, not the report, is what the team reads.
