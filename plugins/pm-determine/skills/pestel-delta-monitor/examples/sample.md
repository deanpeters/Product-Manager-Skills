# PESTEL Delta Monitor — Worked Example

All companies, regulations, URLs, and figures are **fictional**. Same scenario as the suite's
other examples: Fieldlight, a scheduling tool for trades businesses expanding into field service
management. The baseline is a (fictional) full PESTEL run in April 2026 covering "US trades-software
market, shops of 10-200 techs." This is the July quarterly re-scan.

**Invocation:** `PESTEL delta against the attached April analysis — scope is our US trades-software
market; I suspect the contractor-classification rule matters. [baseline attached]`

Both budget questions were answered inline (baseline attached, suspected event named), so the skill
asked nothing, read the baseline fully, and checked the suspected event first.

---

# PESTEL Delta Report

## 1. Run Header
**Scope (from prior analysis):** US trades-software market; shops of 10-200 technicians
**Prior analysis date:** 2026-04-10
**This run date:** 2026-07-31

## 2. Factor-by-Factor Delta

### Political: no material movement
One line: infrastructure-spending debate continues; nothing passed, no threshold crossed.

### Economic: moved
- **What moved:** small-business lending rates crossed 9.5% — the exact threshold baseline entry E2 named as the point where shops defer software spend — **Fact** ([central bank small-business lending data, Jul 2026](https://example.com/fed/sb-lending))
- **Prior assumption affected:** E2 assumed rates would stay below the deferral threshold through 2026, which justified the aggressive Q4 upsell targets
- **Reading:** expansion-revenue assumptions for Q4 need a haircut; retention motions outperform upsell motions in rate-squeezed quarters — **Inference**

### Social: no material movement
One line: skilled-trades labor shortage persists at baseline levels; no new data crossing thresholds.

### Technological: moved
- **What moved:** the largest consumer review platform opened its API to AI booking agents — **Fact** ([platform announcement, Jun 2026](https://example.com/platform/agent-api))
- **Prior assumption affected:** T1 treated "AI agents booking home services directly" as a 2028+ scenario
- **Reading:** the booking layer could commoditize sooner than the baseline assumed — whoever owns the schedule still wins, but inbound-lead features lose defensibility first — **Inference**

### Environmental: no material movement
One line: heat-pump incentive programs unchanged since the baseline logged them.

### Legal: moved
- **What moved:** the contractor-classification rule cleared its comment period with the subcontractor-scheduling provision intact; effective March 2027 — **Fact** ([federal register entry, Jul 2026](https://example.com/regs/contractor-rule))
- **Prior assumption affected:** L1 assumed the provision would be stripped, so scheduling subcontractors like employees carried no compliance exposure
- **Reading:** how our board schedules subs becomes a compliance feature by March — and a sales asset in the enterprise segment before that — **Inference**

## 3. Broken Assumptions
- **E2 (rates below deferral threshold):** broken — cited above. Q4 expansion targets were built on it.
- **L1 (provision would be stripped):** broken — cited above. The "subs are just rows on the board" product stance now has a compliance clock on it.

## 4. New to the Frame
- **AI booking-agent access to review platforms** — absent from the April baseline entirely; warrants a Technological slot with a quarterly watch.

## 5. So What?
- **Implications for strategy or roadmap:**
  1. Shift Q4 motion from upsell to retention — **Inference** from E2, confidence: medium, pending one more month of lending data
  2. Sub-scheduling compliance work enters the roadmap with a hard date (March 2027) — **Fact**-driven, confidence: high
  3. Re-weight inbound-lead features downward in the expansion plan; the booking layer's defensibility is eroding — **Inference** from T-delta, confidence: low-medium
- **Factors to watch closely next cycle:** AI booking-agent adoption (does any FSM competitor integrate?); lending-rate trajectory
- **Assumptions to validate:**
  1. The deferral threshold in E2 actually predicts our customers' behavior (it was industry lore — instrument it)
  2. Enterprise buyers will pay for classification-compliance features before the deadline
  3. Baseline entries P1 and Env2 have touched no decision in three runs — furniture? Flag for retirement at the next baseline refresh.

---

## Why this example works

- **Broken assumptions are the headline, and they're traceable.** Both broken entries (E2, L1) are
  named by their baseline IDs, cited, and tied to the decisions built on them. That's the diff
  doing what a fresh re-write never could — you can't break an assumption you didn't write down.
- **The quiet factors got one line each.** Three of six factors didn't move, and the report says so
  in three lines total. The whole document is about a page — that brevity is the radar working.
- **The suspected event was checked first and confirmed** — but the run also caught something the
  user didn't suspect (the platform API change), which is why the sweep still runs even when you
  arrive with a hypothesis.
- **Furniture got flagged.** Two baseline entries that never move and touch no decision are marked
  for retirement, keeping future runs honest about what belongs on the radar.
