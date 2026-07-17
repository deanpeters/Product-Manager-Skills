# Intelligence Collection Disciplines — Worked Example (Industrial)

All companies, products, URLs, and figures are **fictional**. Industrial sibling of
[`sample.md`](sample.md) — and the one where the physical-world disciplines finally star. The SaaS
plan consciously skipped MASINT and GEOINT/DEMOINT; this plan runs them, because the target
leaves fingerprints in customs records, certification registries, and facility permits that no
SaaS competitor ever files.

---

# Collection Plan: Meridian Freight Systems / plant-floor automation entry

## Instantiation
[TARGET]      = Meridian Freight Systems
[MARKET]      = plant-floor automation & monitoring; NAICS 333 (machinery mfg) / 334 (instruments), buyers in NAICS 31-33
[GEOGRAPHY]   = United States, Canada
[BUYER]       = plant managers and corporate engineering, discrete manufacturers 100-500 employees
[CAPABILITY]  = extending their warehouse-robotics platform onto the manufacturing floor
[DECISION]    = how much 2027 roadmap Northfield fences off for a defensive play — and of what kind

## Discipline Selection

| Discipline | Running? | Why (which signal chains) | Key sources (free first) |
|---|---|---|---|
| OSINT | ✅ light | conference footprint + solutions-page language shifts | trade-show exhibitor lists, their site |
| FININT | ◻ not yet | private; re-opens on any raise or when partner firms (public) name them in filings | Crunchbase, partner 10-Ks |
| GEOINT/DEMOINT | ✅ | terrain check: does the target segment exist at the size their move implies? establishment counts by NAICS + employee band | census County Business Patterns |
| TECHINT | ✅ | API docs diffs (asset-class modeling) + patent classifications drifting from warehouse to general industrial | their docs, patents.google.com |
| HUMINT | ✅ | domain-hiring chain: controls engineers/channel roles = staffing the bet; absence is also a signal | LinkedIn jobs, careers page |
| SIGINT | ✅ | new subdomains, early-access forms, solutions-page diffs | crt.sh, Wayback |
| MASINT | ✅ | the star here: customs component volumes, certification registry progress, facility permits | ImportYeti-class trade data, cert registry, local permit records |

Six running — more than the SaaS plan's four, justified: a physical-product entry emits on more
channels, and [DECISION] hinges on *timing*, which the physical channels date best.

## Cadence
- **Monthly (SIGINT + OSINT, ~30 min):** solutions-page diff; crt.sh; exhibitor-list scan for manufacturing trade shows
- **Quarterly (MASINT + TECHINT deep pass):** customs volumes; certification registry status; patent classification sweep; API docs diff
- **Annual (GEOINT/DEMOINT):** refresh the establishment-count terrain when census data updates
- **Event-driven (48h):** certification status change; any funding event (re-opens FININT); domain hiring appearing

## Fusion Table (as of 2026-11-28)

| Discipline | Signal found | Label | Source URL + date |
|---|---|---|---|
| MASINT | cert filing "in process," plant-floor equipment class, via subsidiary | Fact | [registry](https://example.com/certregistry/meridian), Oct 2026 |
| MASINT | component imports up two consecutive quarters | Fact | [trade data](https://example.com/tradedata/meridian), Nov 2026 |
| SIGINT | "Manufacturing early access" form on solutions page | Fact | [page diff](https://example.com/archive/meridian-solutions), Nov 2026 |
| TECHINT | API models generic asset classes; patent filings still warehouse-classified | Fact | [docs](https://example.com/meridian/docs); patents, Nov 2026 |
| HUMINT | **no** manufacturing-domain hires — zero controls/channel postings | Fact (absence) | job boards, Nov 2026 |
| GEOINT/DEMOINT | target segment: ~38k establishments in band across [GEOGRAPHY] — the move's math works | Fact | [census CBP](https://example.com/census/cbp), 2026 |

**Fusion verdict:** 4 channels say building, 1 says not-staffing → **conflict → dig** → registry
detail names a partner engineering firm as responsible party — **Fact**. Resolved reading:
partner-led entry, 12-36 months out (certification clock) — **actionable**, with the response
aimed at the partner layer, not the product layer.

## Provenance & Guardrails
- Registry and customs pages archived at collection date (registries restructure; permit portals purge)
- All sources public: filings, registries, published records, their own site. Stage test: clean —
  every method here could be described at Meridian's user conference without a wince.

---

## Why this example works

- **MASINT earned its seat.** Customs volumes and a certification registry did what no SaaS
  source can: they *dated* the threat (12-36 month certification clock) and graded it as
  commitment rather than ambition. This is the discipline the SaaS sibling rightly skipped and
  this market rightly runs.
- **An absence is in the fusion table as a Fact.** Zero domain hires is checkable, dated,
  sourced — and it's the signal that triggered the conflict rule and found the partner-led
  vector. Fusion tables that only admit positive signals miss the most interesting rows.
- **GEOINT/DEMOINT played its quiet role:** the terrain check. Before treating the move as
  rational, the plan verified the target segment exists at entry-justifying scale — the
  discipline that keeps you from imputing a strategy the market couldn't support.
- **Six disciplines here, four in SaaS — both defended.** Discipline count follows what the
  target *emits* and what the decision *needs*, not a completeness instinct. The two siblings
  demonstrate the selection logic from opposite directions.
