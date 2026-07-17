# Market Landscape Scan — Worked Example

All companies, products, URLs, and figures below are **fictional**, invented to show the schema
doing its job. The same fictional market — field service management (FSM) software for mid-market
trades — runs through the examples of the whole chain: this scan feeds the
`competitive-research-snapshot` example, which feeds `competitive-intel-watch`, which feeds
`battle-card-builder`. Read them in order to see how a stable schema lets each skill consume the
prior one's output.

**Invocation:** `Run a market landscape scan on field service management software for mid-market
trades (HVAC, plumbing, electrical), North America — this supports a decision on whether Fieldlight
expands from scheduling into full FSM.`

---

# Market Landscape Snapshot

## 1. Scope
**Market / problem space:** software that runs a trades business's day — scheduling, dispatch, quotes, invoicing ("field service management" is the vendor term; owners say "the thing that runs my board")
**Boundary:** North America; companies with 10-200 technicians
**Decision supported:** whether Fieldlight expands from scheduling-only into full FSM
**As-of date:** 2026-06-15

## 2. How This Market Segments
- **Owner-operators graduating off paper (10-30 techs):** buy on price and setup time; churn when the software demands a back-office they don't have — **Inference** (review mining: setup complaints cluster under 30 techs; [reviews roundup](https://example.com/reviews/fsm-smb))
- **Dispatch-led shops (30-100 techs):** a full-time dispatcher is the real user; buy on board speed and tech-app adoption — **Fact** ([trade association survey, Apr 2026](https://example.com/tsa-survey-2026))
- **Multi-branch operators (100-200 techs):** buy on reporting and payroll integration; often run two systems during M&A — **Inference** (job postings at acquirers list dual-system admin roles)
- **Vendor/buyer disagreement:** vendors segment by trade vertical (HVAC vs. plumbing editions); buyers in owner forums segment by *whether they employ a dispatcher* — **Fact** ([forum thread, May 2026](https://example.com/forum/dispatcher-thread)). The vertical editions are packaging, not market structure.

## 3. Player Map

### Direct players
- **Wrenchline:** the incumbent; serves dispatch-led and multi-branch shops; wedge is depth (payroll, inventory, fleet); momentum signal: 14 years of trade-show sponsorships but hiring slowed to backfill-only — **Fact** ([careers page, Jun 2026](https://example.com/wrenchline/careers))
- **Vantiga FSM:** enterprise suite player moving downmarket; wedge is the parent suite's ERP tie-in; momentum: launched a "Vantiga Go" mid-market tier in March — **Fact** ([press release](https://example.com/vantiga/go-launch))

### Adjacent players (could enter)
- **General scheduling tools (incl. Fieldlight today):** already own the calendar; adjacency matters because the scheduling wedge is how DispatchCrow entered — **Fact** (their own origin story, [about page](https://example.com/dispatchcrow/about))

### Substitutes and non-consumption
- **Whiteboard + phone + group text:** persists because the dispatcher can see the whole day at once and nothing beats a phone call for a same-day change; strongest in the 10-30 tech segment — **Inference** (forum polls; no vendor admits to competing with a whiteboard, all of them do)
- **Spreadsheets + generic invoicing apps:** the graduation path off paper; persists because it's free and the owner already knows it

### Emerging entrants
- **DispatchCrow:** entered via scheduling two years ago, now shipping quoting and payments; bet: owner-operators will buy one cheap tool that grows with them; traction signal: Series A announced Jan 2026 — **Fact** ([funding coverage](https://example.com/news/dispatchcrow-series-a))

## 4. Dynamics
- **Where the money is:** dispatch-led shops carry the highest willingness-to-pay (per-tech pricing tolerated at 3-4x the owner-operator rate) — **Inference** (published pricing tiers across 6 vendors); payments attach is where vendors expand revenue without raising sticker price — **Fact** (two vendors' earnings language cites "payments attach rate"; [investor deck](https://example.com/wrenchline/investor))
- **Where the momentum is:** the low end — owner-operator tools adding features monthly while incumbent release notes slow — **Fact** (changelog cadence comparison, Jan-Jun 2026); tech-app quality is the new battleground — **Inference** (review complaints shifted from "missing features" to "my techs won't use it")
- **Consolidation or fragmentation:** consolidating at the top (two acquisitions in 18 months), fragmenting at the bottom — **Fact** ([acquisition coverage](https://example.com/news/fsm-mna))
- **Technology or regulatory shifts in play:** AI-drafted quotes appearing in two products' betas — **Fact** (both changelogs); contractor-classification rules could reshape how techs are scheduled — **Assumption** (proposed rule, not final)

## 5. Whitespace and Dead Zones
- **Nobody serves the 10-30 tech segment with real dispatch tooling:** opportunity or dead zone? Two prior entrants targeted it and moved upmarket within two years — **Fact** ([postmortem interview](https://example.com/news/fsm-pivots)); but both cited acquisition cost, not absent demand — **Inference** (founder cites CAC, not churn). Verdict: conditional whitespace — viable only with a self-serve motion. **Assumption to validate:** this segment will self-onboard without a sales call.
- **No incumbent has a credible offline mode for rural crews:** opportunity or dead zone? Review complaints exist but cluster in a small minority of shops — **Fact** (9 of ~400 mined reviews). Verdict: likely dead zone as a wedge; table stakes at most.

## 6. So What?
- **Implications for the decision in Scope:**
  1. Fieldlight's scheduling wedge is the *proven* entry path into FSM — DispatchCrow just walked it — **Fact** (their trajectory), confidence: high
  2. Expanding puts Fieldlight into direct contact with Wrenchline in the dispatch-led segment, where depth matters and Fieldlight has none yet — **Inference**, confidence: high
  3. Payments attach, not per-seat price, is where the expansion pays back — **Inference** (vendor economics above), confidence: medium
- **Players to deep-dive next:** Wrenchline (the incumbent Fieldlight would collide with), DispatchCrow (the entrant running Fieldlight's own playbook, two years ahead)
- **Assumptions to validate:**
  1. Fieldlight's current customers want quoting/invoicing from us rather than their accounting tool
  2. The 10-30 tech segment self-onboards without sales assist
  3. Wrenchline's slowed hiring signals retrenchment rather than efficiency

---

## Why this example works

- **The vendor/buyer disagreement is load-bearing.** The whole expansion decision reframes once you
  see buyers segment by "do we employ a dispatcher," not by trade vertical. That one bullet is worth
  more than the player map — and it came from a forum thread, not an analyst quadrant.
- **Non-consumption got a real entry.** The whiteboard is Wrenchline's biggest competitor and
  Fieldlight's too; omitting it would have made the market look more penetrated than it is.
- **Both whitespace claims faced the dead-zone test, and they resolved differently.** One survived
  conditionally (with the condition named as an assumption to validate); one was honestly called a
  dead zone. An example where every gap is an "opportunity" would be teaching the pitch, not the scan.
- **Section 6 hands off cleanly.** The two deep-dive players are exactly what the
  `competitive-research-snapshot` example picks up next.
