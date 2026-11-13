# Product Lifecycle Plays Example — SaaS

**Product line:** Fieldlight FSM platform, four modules
**When:** September 2025 — the portfolio review that produced the Classic Dispatch decision
**Why this example:** it's the prequel to the EOL suite. The Classic Dispatch retirement documented
in `eol-process` and `eol-message` starts here, as one row in a four-row worksheet — and the
interaction check moves a second product's timeline.

---

## Worksheet 2: Portfolio View

```markdown
## Lifecycle Plays: Fieldlight FSM Platform

| Product | Stage | Yes-count | Pressure | Reasons to Extend | Reasons to Replace | Reasons to Retire | Play |
|---|---|---|---|---|---|---|---|
| Classic Dispatch | In decline | 6/7 | Capability | None found -- architecture is the ceiling | Cannot do real-time; 40% of support volume | Customers still need dispatch daily | **Replace** |
| Invoicing | Mature, healthy | 1/7 | None | Multi-currency requested by 40 accounts | -- | -- | **Invest** |
| Parts | Mature, softening | 3/7 | Demand-side | Distributors asking for a read-only tier | -- | -- | **Extend** |
| SMS Alerts | In decline | 6/7 | Capability | None -- carrier rules keep tightening | Portal already covers the need | Usage down 71%; need has moved | **Retire** |

### Interaction Checks
- [x] No two products are the replacement for the same customers
- [x] No extension undercuts the case for another product's replacement
- [ ] No two retirements land in the same window for the same customer
      **FAILED** -- Classic Dispatch replacement and SMS Alerts retirement
      both hit the same dispatcher persona in H1 2026
- [x] Sequencing across the line is deliberate, not incidental

**Action from the failed check**: move SMS Alerts retirement to Q4 2026,
after Classic migration completes. Dispatchers absorb one change, not two.
```

---

## Worksheet 1: Stage Diagnosis (Classic Dispatch)

```markdown
## Lifecycle Diagnosis: Fieldlight Classic Dispatch

**Trigger**: Support cost. Classic drives ~40% of support volume on ~15% of revenue
**Revenue trend**: Flat for five quarters, slight decline in the last two

### Transition Questions

| # | Lever | Ask | Yes/No | Evidence |
|---|---|---|---|---|
| 1 | Marketing objective | Is defending market share still profitable? | No | We don't win deals on Classic anymore |
| 2 | Competition | Are loyalty efforts no longer retaining users? | Yes | Renewals hold, but on the platform, not Classic |
| 3 | Product | Are legacy support costs becoming unsustainable? | Yes | 40% of volume on 15% of revenue |
| 4 | Promotion | Should we run migration campaigns instead of loyalty? | Yes | Every Classic conversation is already a Next pitch |
| 5 | Place | Are we losing money on certain channels? | No | Direct only; channel economics fine |
| 6 | Price | Are our value-add bundles losing effectiveness? | Yes | Classic no longer justifies its tier |
| 7 | Data strategy | Is our data shifting from predictive to transitional? | Yes | We track migration readiness, not usage growth |

**Yes count**: 5/7
**Stage**: Crossing into decline

### Pressure Source

- [ ] Demand-side
- [x] Supply/cost-side -- support load is the loudest signal
- [x] Capability-side -- overnight batch architecture cannot do real-time

**Primary pressure**: Capability. The support cost is a symptom of the
architecture: Classic recalculates once nightly, so every mid-day change
becomes a support call.

### Extension Test

1. Segment a variant could serve? **No** -- the limitation is universal,
   not segment-specific
2. Capability addable without re-architecture? **No** -- real-time
   reoptimization is the whole ask and the batch design forecloses it
3. Repackage or rebrand reach a different buyer? **No** -- tested with a
   "Dispatch Lite" concept in 2024; no interest
4. Decline in the product, or the channel/price around it? **The product** --
   direct channel is healthy, pricing is competitive

### Recommended Play

**Play**: Replace
**Because**: capability ceiling is architectural, extension tested and failed,
support economics worsening, and Next Scheduling already exists at near parity
**What this play costs**: a GTM for Next plus a funded EOL for Classic --
two workstreams, roughly three quarters
**What we're accepting**: ~30 accounts on custom dispatch rules will need
hand-holding, and some will churn. We are choosing that over carrying the
support load indefinitely.
```

---

## Worksheet 3: Risk Register (Classic Dispatch → Next Scheduling)

```markdown
## Replacement Risk Register: Classic Dispatch -> Next Scheduling

| # | Hazard | Applies? | Probability | Impact | Mitigation | Contingency (Plan B) |
|---|---|---|---|---|---|---|
| 1 | GTM process failure | [x] | Low | Med | Next already sells well to new accounts | Extend Classic 6 months; re-approach migration |
| 2 | Delayed market entry | [ ] | -- | -- | Next shipped 2024 | -- |
| 3 | Internal misalignment | [x] | Med | Med | Single roadmap owner; Sales briefed pre-announce | Pause EOS; realign before customer comms |
| 4 | External forces | [ ] | -- | -- | No regulatory or macro exposure | -- |
| 5 | Regulatory risk | [ ] | -- | -- | Dispatch data carries no compliance surface | -- |
| 6 | Unexpected cannibalization | [x] | High | Low | Deliberate -- Next is meant to absorb Classic | Accept; both are on the same platform SKU |
| 7 | Poor EOL management | [x] | Med | **High** | Fund the EOL as its own workstream; run the full process | Slip the EOL date, not the enablement; extend Classic if migration stalls below 80% |

### Cannibalization Plan
- Which product wins which customer: Next wins all of them; that's the intent
- Margin during the overlap: unchanged -- both included in the platform tier,
  no separate SKU revenue to lose
- How long the overlap runs: ten months, March to December 2026

### Retirement Funding
- Who owns the EOL of the old product: Product (with CS for the account tier)
- Is it funded: Yes -- 2 temp support headcount and CS migration time approved
```

---

## What to notice

- **The interaction check changed a decision.** Nothing in the Classic diagnosis was wrong; the
  portfolio view caught that two separate plays would land on the same dispatcher in the same
  half-year. SMS Alerts moved to Q4. That finding only exists at the line level.
- **The extension test was run and failed, in writing.** Including the 2024 "Dispatch Lite"
  experiment. When someone asks in March why we didn't just add features, the answer is on file.
- **Cannibalization is rated High probability, Low impact — and that's correct.** It's deliberate
  and there's no separate SKU revenue to protect. Not every hazard is a threat; rating it honestly
  is what keeps the register credible.
- **Hazard 7 carries the only High impact rating.** Poor EOL management is the risk that mattered on
  this play, and the contingency is specific: *slip the EOL date, not the enablement.* That single
  line is the difference between a managed transition and the Vista pattern.
- **The tradeoff is stated, not buried.** "~30 accounts will need hand-holding, and some will churn.
  We are choosing that." In the eventual retrospective, 11 of 19 churned accounts came from that
  segment — the cost was named a year before it was paid.
