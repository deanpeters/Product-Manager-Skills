# Product Lifecycle Plays Example — Industrial

**Product line:** Northfield Automation retrofit control products
**When:** June 2025 — the play decision that preceded the NFA-200 end-of-life work
**Why this example:** it shows a risk register that **named the right hazard and mis-rated it.**
The NFA-200 replacement play was correct; the failure was assuming the landing place was ready.
Sixteen months later that assumption collapsed and the whole EOL had to be re-scoped. The annotated
register at the bottom shows where the miss was visible at the time.

---

## Worksheet 2: Portfolio View

```markdown
## Lifecycle Plays: Northfield Retrofit Control Products

| Product | Stage | Yes-count | Pressure | Reasons to Extend | Reasons to Replace | Reasons to Retire | Play |
|---|---|---|---|---|---|---|---|
| NFA-200 controller | Mature, softening | 4/7 | Supply/cost | Fixed I/O caps the addressable jobs | Line capacity needed; NFA-500 ready | Installed base still under contract | **Replace** |
| NFA-200-EX I/O modules | Mature, softening | 4/7 | Supply/cost | -- | Tied to NFA-200 lifecycle | -- | **Replace** (with parent) |
| NFA-100 controller | In decline | 7/7 | Capability | None -- superseded twice | Already replaced by NFA-200 | 6 units left, all out of contract | **Retire** |
| SmartLink gateway | Mature, healthy | 1/7 | Demand-side | OEMs asking for a DIN-rail variant | -- | -- | **Extend** |

### Interaction Checks
- [x] No two products are the replacement for the same customers
- [x] No extension undercuts the case for another product's replacement
- [x] No two retirements land in the same window for the same customer
      (NFA-100's 6 units share no sites with NFA-200 installations)
- [x] Sequencing across the line is deliberate, not incidental
```

---

## Worksheet 1: Stage Diagnosis (NFA-200)

```markdown
## Lifecycle Diagnosis: NFA-200 Series Retrofit Controller

**Trigger**: Manufacturing requested the line for NFA-500 capacity
**Revenue trend**: Flat for four quarters; service revenue growing

### Transition Questions

| # | Lever | Ask | Yes/No | Evidence |
|---|---|---|---|---|
| 1 | Marketing objective | Is defending market share still profitable? | Yes* | Still wins retrofit bids on price |
| 2 | Competition | Are loyalty efforts no longer retaining users? | No | Installed base is loyal and under contract |
| 3 | Product | Are legacy support costs becoming unsustainable? | No | Service margin is healthy |
| 4 | Promotion | Should we run migration campaigns instead of loyalty? | Yes | New bids should be quoting NFA-500 |
| 5 | Place | Are we losing money on certain channels? | No | All 8 partners profitable |
| 6 | Price | Are our value-add bundles losing effectiveness? | Yes | Fixed I/O limits what we can bundle |
| 7 | Data strategy | Is our data shifting from predictive to transitional? | Yes | Planning around NFA-500 attach, not NFA-200 growth |

*Question 1 answered "yes" meaning defending IS still profitable -- a mature
signal, not a decline signal. Counted as a no for decline purposes.

**Yes count**: 4/7 (decline-direction answers: 4, 6, 7, and a soft 1)
**Stage**: Mature and softening -- not yet in decline

### Pressure Source

- [ ] Demand-side -- customers are not asking for this
- [x] Supply/cost-side -- manufacturing capacity is the actual driver
- [ ] Capability-side -- the NFA-200 still does its job well

**Primary pressure**: Supply-side, and internal. Said plainly: our
manufacturing constraint, not our customers' problem. That framing matters --
it means the customer-facing case for change is weak and the transition has
to be carried entirely by us.

### Extension Test

1. Segment a variant could serve? **Partially** -- a modular I/O variant
   would open larger jobs, but that variant is essentially the NFA-500
2. Capability addable without re-architecture? **No** -- modular I/O requires
   a new backplane
3. Repackage or rebrand reach a different buyer? **No** -- industrial buyers
   specify on capability
4. Decline in the product, or the channel/price around it? **Neither** --
   the product is fine; we want the factory line back

### Recommended Play

**Play**: Replace
**Because**: the extension a customer would want IS the NFA-500; manufacturing
needs the capacity; NFA-500 exists and is selling to new accounts
**What this play costs**: NFA-500 GTM (underway) plus an EOL for the NFA-200
**What we're accepting**: 120 installations must eventually move, and we are
choosing to start that clock for internal reasons rather than customer ones.
```

---

## Worksheet 3: Risk Register — as filled in, June 2025

```markdown
## Replacement Risk Register: NFA-200 -> NFA-500

| # | Hazard | Applies? | Probability | Impact | Mitigation | Contingency (Plan B) |
|---|---|---|---|---|---|---|
| 1 | GTM process failure | [x] | Low | Med | NFA-500 already winning new bids | Hold NFA-200 in the price book longer |
| 2 | Delayed market entry | [ ] | -- | -- | NFA-500 shipped 2024 | -- |
| 3 | Internal misalignment | [x] | Med | Med | Ops, Sales, Service on one plan | Pause EOS until aligned |
| 4 | External forces | [ ] | -- | -- | No macro exposure identified | -- |
| 5 | Regulatory risk | [x] | Low | High | UL/CE confirmed unaffected for installed units | Regulatory issues change-control package |
| 6 | Unexpected cannibalization | [x] | Med | Low | Deliberate; NFA-500 carries higher margin | Accept |
| 7 | Poor EOL management | [x] | **Low** | High | "Installed base stays under contract; migration is straightforward" | Extend service window |

### Cannibalization Plan
- Which product wins which customer: NFA-500 takes all new bids immediately
- Margin during the overlap: improves -- NFA-500 margin is higher
- How long the overlap runs: assumed 18 months

### Retirement Funding
- Who owns the EOL of the old product: Product
- Is it funded: Partially -- service continuity budgeted, retrofit engineering not
```

---

## What actually happened — and where it was visible

Sixteen months later, the stakeholder sequence broke the plan. Two findings:

1. **Service agreements ran to 2028 and were not terminable** — an obligation lock
2. **The NFA-500 was not a drop-in.** Different mounting bracket and panel depth; 120 site visits;
   two of three sampled sites needed a production shutdown; the bracket engineering was unfunded

The verdict changed from "retire the NFA-200" to **End of Sale now, EOL not scheduled**, with the
retrofit path funded as the precondition. Four months of rework.

**Both findings were visible in this worksheet in June 2025:**

- **Hazard 7 was rated Low probability on an assumption, not evidence.** The mitigation column reads
  "migration is straightforward" — that is a belief, and beliefs don't belong in a mitigation cell.
  Rating it Medium would have triggered the question that mattered: *is the NFA-500 a drop-in for
  the installed base?*
- **The funding line already said no.** "Retrofit engineering not funded" is written down, right
  there, and nobody treated an unfunded retrofit as a blocker on the play. A replacement play whose
  retirement is unfunded is an extension play with extra steps — that's Pitfall 5 in the skill, and
  this is what it looks like in the wild.
- **The extension test was answered honestly and the answer was ignored.** "The extension a customer
  would want IS the NFA-500" was correct, and it should have prompted a follow-up: if the NFA-500 is
  the extension customers want, why can't it go where the NFA-200 already is?

**The lesson isn't that the play was wrong.** Replace was the right call, and it survived the
re-scoping. The lesson is that a register is only as good as its worst-rated cell, and the cheapest
moment to check a landing-place assumption is when you're writing "Low" next to Hazard 7 — not
sixteen months later in a room with Legal.
