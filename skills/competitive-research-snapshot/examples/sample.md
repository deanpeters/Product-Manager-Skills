# Competitive Research Snapshot — Worked Example

All companies, products, URLs, and figures are **fictional**. This example continues the scenario
from `market-landscape-scan/examples/sample.md`: Fieldlight, a scheduling tool for trades
businesses, is deciding whether to expand into full field service management (FSM). The landscape
scan named two deep-dive players — Wrenchline and DispatchCrow — and this snapshot picks them up,
adding Vantiga FSM because its downmarket move touches the same buyers. The output below becomes the
baseline that the `competitive-intel-watch` example diffs against.

**Invocation:** `Competitive research snapshot for Fieldlight — decision: does the FSM expansion
lead with quoting or with dispatch? Competitors: Wrenchline, DispatchCrow; landscape scan from
June 15 is in session.`

Note what the skill did with that invocation: all three budget questions were answered inline, so it
asked nothing and went straight to the search plan. It also credited the landscape scan instead of
re-researching the market structure.

---

# Competitive Research Snapshot

## 1. Scope
**Company/product:** Fieldlight (scheduling for trades businesses, expanding toward FSM)
**Category:** field service management for mid-market trades
**Decision supported:** whether the FSM expansion leads with quoting or with dispatch
**Competitors analyzed:** Wrenchline (incumbent we'd collide with), DispatchCrow (running our playbook, two years ahead), Vantiga FSM (enterprise suite moving downmarket into the same buyers)
**As-of date:** 2026-06-28

## 2. Competitor Snapshots

### Competitor: Wrenchline
- **Positioning:** "the operating system for the trades" — **Fact** ([homepage, Jun 2026](https://example.com/wrenchline))
- **Relevant capability:** dispatch board with capacity planning; the deepest in category per reviewer consensus — **Fact** ([review site category report](https://example.com/reviews/dispatch-2026))
- **Likely strength:** switching costs — payroll, inventory, and fleet modules make it the system of record; multi-year contracts standard — **Fact** ([pricing page](https://example.com/wrenchline/pricing), contract terms listed)
- **Likely weakness:** tech-app adoption; "my techs won't use it" is the largest complaint cluster, 40+ reviews since January — **Inference** (review mining; no adoption data published)
- **Key source URL:** [pricing page](https://example.com/wrenchline/pricing)

### Competitor: DispatchCrow
- **Positioning:** "the first tool a growing shop buys, the last one it outgrows" — **Fact** ([homepage, Jun 2026](https://example.com/dispatchcrow))
- **Relevant capability:** shipped quoting in November, payments in April — expansion sequence was quote → invoice → payments, not dispatch — **Fact** ([changelog](https://example.com/dispatchcrow/changelog))
- **Likely strength:** self-serve onboarding; free tier to 5 techs, no sales call below 30 — **Fact** ([pricing page](https://example.com/dispatchcrow/pricing))
- **Likely weakness:** dispatch depth; their board lacks capacity planning and reviewers switching upmarket cite it — **Inference** (feature absence is Fact per docs; that it drives churn is inferred from 6 switching reviews)
- **Key source URL:** [changelog](https://example.com/dispatchcrow/changelog)

### Competitor: Vantiga FSM
- **Positioning:** "field service, connected to the business" (ERP tie-in) — **Fact** ([product page, Jun 2026](https://example.com/vantiga/fsm))
- **Relevant capability:** "Vantiga Go" mid-market tier launched March — **Fact** ([press release](https://example.com/vantiga/go-launch))
- **Likely strength:** wins where the buyer already runs the Vantiga suite — **Assumption** (their claim; no independent mid-market win evidence found)
- **Likely weakness:** implementation weight; only two Go-tier reviews exist and both mention implementation partners — **Inference** (thin evidence, noted)
- **Key source URL:** [product page](https://example.com/vantiga/fsm)

## 3. Quick Comparison
| Dimension | Fieldlight | Wrenchline | DispatchCrow | Vantiga FSM |
|---|---|---|---|---|
| Target customer | shops of 10-100 techs (scheduling-led) | dispatch-led and multi-branch, 30-200 | owner-operators, 5-50 | Vantiga-suite accounts trying mid-market |
| Core use case | scheduling and the day board | full back office for the trades | grow-with-you toolkit | field service inside the ERP |
| Main strength | tech-app adoption (our reviews) | depth and switching costs | self-serve motion | suite tie-in |
| Main weakness | no quoting/invoicing yet | tech-app adoption | dispatch depth | implementation weight |
| Evidence quality | high (own data) | high | high | **low — mostly their own marketing** |

## 4. So What?
- **Product strategy implications:**
  1. Lead with quoting, not dispatch: DispatchCrow's quote → payments sequence is a proven expansion path for a scheduling-led product, and dispatch is where Wrenchline is strongest — **Inference** (their changelog trajectory + Wrenchline's review moat), confidence: high
  2. Our tech-app adoption strength attacks Wrenchline's largest complaint cluster — the wedge writes itself, but only in dispatch-led shops, which we reach *after* quoting funds the roadmap — **Inference**, confidence: medium
  3. Vantiga Go is not a near-term threat to our segment — **Assumption to validate** (evidence quality low; revisit when independent reviews exist), confidence: low
- **Competitive risks:**
  1. DispatchCrow adds capacity planning before we ship quoting, closing their gap while we open ours — **Assumption**, watch their changelog
  2. Wrenchline bundles a "lite" tier to defend the low end — **Assumption**, no signal yet
- **Product opportunities:**
  1. Quoting integrated with the schedule ("quote from the calendar") — neither rival does this — **Fact** (feature absence per both docs)
  2. Win the dispatcher later with adoption-led dispatch: board built for techs who already like our app — **Inference**
- **Assumptions to validate:**
  1. Our customers want quoting from us rather than their accounting tool (carried forward from the landscape scan — still open)
  2. DispatchCrow's churn upmarket is real and reachable by us
  3. Vantiga Go's mid-market traction is as thin as its review count suggests

---

## Why this example works

- **The decision shaped everything.** "Quoting or dispatch?" is why the snapshots dwell on expansion
  sequences and dispatch depth rather than, say, marketing spend. A section that didn't serve that
  question didn't ship — that's Just Enough Mode.
- **The Evidence quality row did its job.** Vantiga's column is rated low, and the So What section
  respects that: Vantiga gets an *assumption to validate*, not a strategy implication. Weak evidence
  was contained, not laundered.
- **Labels carry the argument's weight.** The headline recommendation (lead with quoting) is an
  Inference with its basis shown, so a skeptical exec can attack the basis instead of the vibe.
- **It builds on the chain.** The landscape scan chose the competitors; this snapshot inherited an
  open assumption from it; the As-of date (2026-06-28) is what the `competitive-intel-watch` example
  diffs against next.
