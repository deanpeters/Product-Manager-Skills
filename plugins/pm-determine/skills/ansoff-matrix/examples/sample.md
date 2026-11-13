# Ansoff Matrix — Worked Example

All companies, products, URLs, and figures are **fictional**. Same scenario as the suite's other
examples: Fieldlight, a scheduling tool for trades businesses (10-100 techs, North America),
planning its expansion into field service management. The landscape scan, five-forces read, and
competitive snapshot were in session — so the matrix **organized existing evidence** and searched
only for demand signals it lacked (review-thread mining, adjacent-trade signals).

**Invocation:** `Ansoff growth options for Fieldlight — core: scheduling software for HVAC and
electrical shops of 10-100 techs, North America. Outcome: +60% ARR in 24 months. Constraint: no
acquisitions, one product team.`

---

# Ansoff Growth Options: Fieldlight
**As-of date:** 2026-07-31
**Current core:** scheduling + day board for HVAC/electrical shops, 10-100 techs, North America
**Growth outcome sought:** +60% ARR in 24 months; constraints: no acquisitions, one product team

## 1. Market Penetration (existing product, existing market — lowest risk)
- **Win the dispatcher upgrade: capacity-view add-on for existing accounts** — signal: "capacity planning" is our #2 feature request, 60+ votes on the public board — **Fact** ([feature board](https://example.com/fieldlight/board)) — risk: **low** — existing buyers, expressed demand, priced as add-on
- **Reactivation campaign into trial-expired accounts under 30 techs** — signal: 38% of expired trials cited "not ready yet," not "chose competitor," in exit surveys — **Fact** (internal survey data) — risk: **low** — known audience, cheap motion

## 2. Market Development (existing product, new market)
- **Adjacent trade: plumbing contractors, same size band** — signal: plumbing shops appear unprompted in review-site threads asking "does this work for plumbing?" — **Fact** ([review threads](https://example.com/reviews/fieldlight)); incumbent plumbing options gate scheduling behind suite tiers — **Fact** ([pricing pages](https://example.com/wrenchline/pricing)) — risk: **medium** — demand signal real but second-hand; trade-specific workflows (permits, parts) don't fully transfer
- **Canada expansion** — signal: inbound signups from Canadian IPs already convert at parity — **Fact** (internal analytics) — risk: **low-medium** — same product, minor tax/locale work

## 3. Product Development (new product, existing market)
- **Quoting, integrated with the schedule ("quote from the calendar")** — signal: DispatchCrow's quote → payments sequence proved the expansion path for a scheduling-led product — **Fact** ([their changelog](https://example.com/dispatchcrow/changelog)); no competitor quotes from the calendar — **Fact** (feature absence per docs); our own customers' #1 request category — **Fact** (feature board) — risk: **medium** — new build, proven category demand
- **Payments attach on top of quoting** — signal: category-wide attach economics documented in incumbent investor materials — **Fact** ([investor deck](https://example.com/wrenchline/investor)) — risk: **medium** — depends on quoting shipping first; processor take rates squeeze margin (five-forces supplier read)

## 4. Diversification (new product, new market — highest risk)
- Honestly empty. The tempting candidate — an IoT job-site hardware bundle for general contractors — has one analyst mention and founder enthusiasm behind it. That is not extraordinary evidence, and this quadrant demands it. Logged to the watchlist, not the matrix.

## 5. Recommended Sequence (the "so what")
- **First:** quoting integrated with the schedule (product development) — strongest demand signal we have (own customers + proven competitor path), and it's the gateway to payments — the actual economics of the expansion
- **Then:** payments attach, then plumbing entry — payments is funded and de-risked by quoting adoption; plumbing entry rides the same product with case studies in hand
- **Not yet:** the capacity-view add-on as a *headline* bet — it defends the core and should ship, but it grows ARPU single-digits; it funds nothing
- **The assumption that breaks this sequence:** customers want quoting *from us* rather than their accounting tool. If discovery says no, product development stalls and Canada + plumbing (market development) become the lead moves.

### Assumptions to Validate
- Customers want quoting from Fieldlight rather than their accounting tool (carried from the landscape scan — now the sequence's linchpin)
- Plumbing-shop demand survives contact with trade-specific workflow gaps
- Payments margin works at trades transaction sizes after processor take rates

---

## Why this example works

- **The matrix organized, rather than gathered.** Three prior investigations fed it; the only new
  research was demand-signal mining. That's the skill working as designed downstream of the suite.
- **The risk gradient held under temptation.** The IoT bundle wanted a diversification slot; the
  evidence bar said no. The empty quadrant with its reasoning *is* the deliverable there — compare
  the pitfall the skill names ("quadrant stuffing").
- **The sequence has funding logic, not just order.** Quoting → payments → plumbing compounds:
  each move pays for or de-risks the next. And the one assumption that breaks the sequence is
  named, with the fallback path stated — that's what makes this a plan an exec can stress-test.
- **Sizing was routed, not invented.** No market sizes appear anywhere; the Final Step's
  recommended option is running `tam-sam-som-calculator` on the quoting move.
