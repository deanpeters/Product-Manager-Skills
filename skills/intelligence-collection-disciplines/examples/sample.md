# Intelligence Collection Disciplines — Worked Example

All companies, products, URLs, and figures are **fictional**. This example shows a complete
collection plan and its fusion outcome — the operation the compendium teaches. It's the same
fictional scenario as the suite's other examples (Fieldlight, a trades-scheduling tool expanding
into FSM), and it shows the *collection side* of the fused conclusion that appears in the
`competitive-analysis-process` example's Step 6.

---

# Collection Plan: DispatchCrow / suspected dispatch-depth build

## Instantiation
[TARGET]      = DispatchCrow
[MARKET]      = field service management software; NAICS 513210 (software publishers)
[GEOGRAPHY]   = United States, Canada
[BUYER]       = owner or office manager, trades shops of 10-100 technicians
[CAPABILITY]  = building real dispatch/capacity-planning depth (moving upmarket into our target segment)
[DECISION]    = how much of our two-quarter quoting window is real — sets the FSM expansion pace

## Discipline Selection

| Discipline | Running? | Why (which signal chains) | Key sources (free first) |
|---|---|---|---|
| OSINT | ✅ | review complaints clustering on their dispatch board = their roadmap pressure point | review sites, trades forums |
| FININT | ◻ not yet | private company; Crunchbase free tier only — thin until they raise again | Crunchbase |
| GEOINT/DEMOINT | ◻ no | terrain already mapped in the June TAM pass; refresh annually | — |
| TECHINT | ✅ | changelog + API docs diffs → beta capabilities before announcement | their changelog, API docs, app store notes |
| HUMINT | ✅ | hiring surge/specialty chain → building a capability, not a feature | LinkedIn jobs, their careers page, blog |
| SIGINT | ✅ | pricing-gate moves + new subdomains → monetization strategy and launch staging | pricing page snapshots, Wayback, crt.sh |
| MASINT | ◻ no | software target; ops-capacity signals folded into HUMINT job-post reading | — |

Four disciplines, chosen because they feed [DECISION]; the table's empty rows are decisions too.

## Cadence
- **Weekly (SIGINT, ~30 min):** pricing page diff; crt.sh check for new `*.dispatchcrow.com` certs
- **Monthly (OSINT + HUMINT):** review mining for dispatch-board complaints; careers-page sweep
- **Quarterly (TECHINT deep pass):** API docs diff; app store release-note review
- **Event-driven (48h):** funding announcement (re-opens FININT); any "capacity" language shipping anywhere

## Fusion Table (as of 2026-07-31)

| Discipline | Signal found | Label | Source URL + date |
|---|---|---|---|
| HUMINT | head of dispatch experience + senior PM hired, both ex-incumbent | Fact | [blog post](https://example.com/dispatchcrow/blog/dispatch-team), Jul 15 |
| SIGINT | payments gate moved down a tier — take-rate becoming the model | Fact | [pricing archive diff](https://example.com/archive/dispatchcrow-pricing), Jul 31 |
| TECHINT | "capacity view — coming to Pro" appears on pricing page feature list | Fact | [pricing page](https://example.com/dispatchcrow/pricing), Jul 31 |
| OSINT | upmarket-switcher reviews: "fine until we hit 40 techs, then the board falls over" | Fact (that they say it) | [review threads](https://example.com/reviews/dispatchcrow), Jun-Jul |

**Fusion verdict:** 4 disciplines, one story → **actionable intelligence** → they are building
dispatch depth to move upmarket, funded by payments volume. Recommended response: compress the
quoting timeline — plan against a Q1 2027 capacity-planning launch, not "someday"; brief the
roadmap owner this week.

One deliberate down-grade: the OSINT complaint cluster alone was a *watch item* back in June — it
says customers want depth, not that DispatchCrow is building it. It joined the story only when
HUMINT and TECHINT arrived. That's the stacking rule preventing a June overreaction.

---

## Why this example works

- **The empty rows are the discipline.** Three disciplines were consciously *not* run, with
  reasons — the artifact-mapping table's whole point. Eight checkmarks would mean nobody chose.
- **[DECISION] shaped everything.** "How real is our two-quarter window?" selected the four
  disciplines that read *their* velocity, and set cadences to how fast each channel actually
  changes (pricing weekly, patents never — they're a five-person startup).
- **The stacking rule ran in both directions.** Four agreeing channels escalated to actionable;
  but the example also shows the June signal correctly *held* at watch-item until independent
  channels corroborated. Escalation discipline is the rule's other half.
- **Announcements-as-intent never triggered** — none of the four signals is a press release. The
  hires, the gate move, and the pricing-page feature list are all commitment-side evidence, which
  is why the verdict earns "actionable" with no announcement at all.
