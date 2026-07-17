# Competitive Intel Watch — Worked Example

All companies, products, URLs, and figures are **fictional**. This example continues the chain:
the `competitive-research-snapshot` example (Fieldlight vs. Wrenchline, DispatchCrow, Vantiga FSM,
dated 2026-06-28) is the baseline this run diffs against. The update flags below are what the
`battle-card-builder` example consumes.

**Invocation:** `Competitive intel watch — prior snapshot pasted below (dated Jun 28); this cycle
I'm specifically watching for DispatchCrow shipping capacity planning. [snapshot]`

Both budget questions were answered inline (snapshot provided, watch focus stated), so the skill
asked nothing, read the snapshot fully, showed its search plan, and swept.

---

# Competitive Watch Report

## 1. Run Header
**Scope (from prior snapshot):** Fieldlight vs. FSM competitors; decision context: FSM expansion leading with quoting
**Prior snapshot date:** 2026-06-28
**This run date:** 2026-07-28
**Competitors checked:** Wrenchline, DispatchCrow, Vantiga FSM

## 2. Changelog (Material Shifts Only)

### Wrenchline — launched "Wrenchline Essentials" entry tier
- **What changed:** new $79/month tier for shops under 25 techs appeared on the pricing page; no dispatch board, no payroll — scheduling, quoting, invoicing only — **Fact** ([pricing page vs. archived version, Jul 24 vs. Jun 28](https://example.com/archive/wrenchline-pricing))
- **Evidence:** URL + archive diff, dated Jul 24, 2026
- **So what:** this is the "lite tier to defend the low end" we filed as an Assumption in the June snapshot — now confirmed. It lands directly on Fieldlight's segment and includes the quoting we haven't shipped yet. Pricing owner and roadmap owner both act on this.
- **Confidence:** high

### DispatchCrow — two senior hires from Wrenchline's dispatch team
- **What changed:** DispatchCrow announced a "head of dispatch experience" and a senior PM, both ex-Wrenchline per their own announcement post — **Fact** ([company blog, Jul 15](https://example.com/dispatchcrow/blog/dispatch-team)); capacity planning is coming — **Inference** (that's the expertise those hires carry; no roadmap statement yet)
- **Evidence:** URL, dated Jul 15, 2026
- **So what:** the competitive risk from the June snapshot ("DispatchCrow closes their dispatch gap while we open ours") just moved from Assumption toward likely. Roadmap owner acts: the window for quoting-first expansion is real but narrower than planned.
- **Confidence:** medium (hires are Fact; the product conclusion is Inference)

_Vantiga FSM: nothing cleared the bar. Two blog posts and a webinar — routine content marketing._

## 3. Update Flags
| Downstream artifact | Sections needing update | Driven by |
|---|---|---|
| Battle card | Pricing & Packaging Snapshot; Do Not Say ("we're the affordable option" now contested) | Wrenchline Essentials tier |
| Pricing/packaging analysis | Entry-tier comparison table | Wrenchline Essentials tier |
| Roadmap assumptions | Quoting-first timeline; dispatch-gap window | DispatchCrow hires |

## 4. Watchlist for Next Run
- DispatchCrow changelog for any dispatch-board or capacity-planning beta (the hires suggest 1-2 quarters out)
- Wrenchline Essentials review volume — whether the tier is real motion or a defensive press release
- Vantiga Go independent reviews (still only two; evidence quality on that column remains low)

### Assumptions to Validate
- Wrenchline Essentials excludes the dispatch board permanently, not just at launch
- DispatchCrow's new hires are building capacity planning rather than polishing the existing board
- Our "quote from the calendar" differentiator still has no direct equivalent shipping elsewhere

---

## Why this example works

- **It reports change, not state.** Three competitors were swept; the report contains two entries
  and one explicit "nothing cleared the bar." A regenerated full snapshot would have buried both
  signals in ten sections of unchanged prose.
- **The diff paid off against the baseline's own assumptions.** The June snapshot filed "Wrenchline
  bundles a lite tier" as an Assumption with no signal; this run *confirmed* it with an archive
  diff. That's the compounding value of a stable schema — assumptions become tripwires.
- **Labels stayed honest under excitement.** The DispatchCrow hires are a Fact; "capacity planning
  is coming" stays an Inference with its basis shown, and confidence is marked medium, not high.
- **The update flags close the loop.** Each material shift names the artifact and section it
  stales — the battle card flags here are exactly what the `battle-card-builder` example picks up.
