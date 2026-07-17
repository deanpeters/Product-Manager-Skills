# Competitive Watch Report Template

Copy this for each watch run. A watch reports **change, not state** — the reader's question is
"what changed since last time?", and "no material shifts this cycle" is a valid, useful answer.
Diff against the prior snapshot; never regenerate it. Section order is stable so runs can be
diffed against each other.

Every claimed change carries a URL **and a date** — the date is half the evidence.

## Template

```markdown
# Competitive Watch Report

## 1. Run Header
**Scope (from prior snapshot):** [copy it — if the scope itself changed, re-baseline instead and say so]
**Prior snapshot date:** [YYYY-MM-DD]
**This run date:** [YYYY-MM-DD]
**Competitors checked:** [list]

## 2. Changelog (Material Shifts Only)
_The materiality bar: report a change only if a sales rep, pricing owner, or roadmap owner would
plausibly act on it. Below the bar: cosmetic site changes, routine content marketing, minor releases._

### [Competitor] — [4 to 8 word change summary]
- **What changed:** [1-2 bullets, labeled Fact/Inference]
- **Evidence:** [URL, date — archive/diff link where possible]
- **So what:** [why it clears the materiality bar — who acts on it]
- **Confidence:** [high / medium / low]

_If nothing cleared the bar:_ "No material shifts this cycle." _Then list anything on the
watchlist for next run — a quiet cycle is reported, not padded._

## 3. Update Flags
_Only rows with real updates; omit the rest. A changelog with no flags usually means the shift
didn't actually clear the bar._

| Downstream artifact | Sections needing update | Driven by |
|---|---|---|
| Battle card | | |
| Positioning statement | | |
| Pricing/packaging analysis | | |
| Roadmap assumptions | | |

## 4. Watchlist for Next Run
- [Signals below the bar but trending]
- [Open questions this run could not resolve]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]
```

## Quality checks before you call it done

- Every changelog entry has URL **and date** — undated evidence can't be verified or diffed next run
- Every entry's "So what" names who would act (rep, pricing owner, roadmap owner) — if nobody would, it's watchlist material
- The prior snapshot was read fully before searching — the diff target is the document, not your memory of the market
- If the cycle was quiet, the report says so plainly instead of promoting below-bar noise
