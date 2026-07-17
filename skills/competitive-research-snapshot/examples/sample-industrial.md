# Competitive Research Snapshot — Worked Example (Industrial)

All companies, products, URLs, and figures are **fictional**. Industrial sibling of
[`sample.md`](sample.md): Northfield Automation, deciding how to enter retrofit automation, takes
the two deep-dive players named by the industrial landscape scan — Helix Motion Systems and
Meridian Freight Systems — plus Corvid Industrial as the wounded incumbent. Note the FININT weight
here: two of three competitors are public filers, so the evidence base tilts from pricing pages
(SaaS) toward earnings language and segment reporting.

**Invocation:** `Competitive research snapshot for Northfield Automation — decision: does the
retrofit line lead with monitoring software or hardware kits? Competitors: Helix, Meridian,
Corvid. August landscape scan in session.`

---

# Competitive Research Snapshot

## 1. Scope
**Company/product:** Northfield Automation (software-defined automation; entering productized retrofit)
**Category:** retrofit automation for mid-size discrete manufacturers
**Decision supported:** whether the retrofit line leads with monitoring software or hardware kits
**Competitors analyzed:** Helix Motion Systems (installed-base incumbent), Meridian Freight Systems (adjacent platform, entry signals), Corvid Industrial (post-split incumbent)
**As-of date:** 2026-08-28

## 2. Competitor Snapshots

### Competitor: Helix Motion Systems
- **Positioning:** "intelligence for every asset you already own" (Foresight aftermarket program) — **Fact** ([Foresight page, Aug 2026](https://example.com/helix/foresight))
- **Relevant capability:** monitoring subscriptions on Helix components; digital-twin hiring wave through 2026 — **Fact** ([careers archive](https://example.com/helix/careers))
- **Likely strength:** installed base + distributor network; their components already sit in most target plants — **Fact** (market-share disclosures in [annual filing](https://example.com/helix/10k))
- **Likely weakness:** Foresight covers *Helix* equipment; mixed-vendor plants get partial pictures — **Fact** (their own compatibility docs) — and the program was just re-scoped into the aftermarket P&L, suggesting contained ambition — **Inference** (Q3 transcript + VP of Digital Transformation's September departure)
- **Key source URL:** [Q3 earnings transcript](https://example.com/helix/q3-transcript)

### Competitor: Meridian Freight Systems
- **Positioning:** "the autonomous warehouse, delivered" — nothing about plants, yet — **Fact** ([homepage, Aug 2026](https://example.com/meridian))
- **Relevant capability:** a fleet-management software layer that is equipment-agnostic by design — the architecture transfers to plant floors — **Inference** (their API docs describe generic asset classes)
- **Likely strength:** platform software maturity; won two marquee logistics deployments — **Fact** ([press coverage](https://example.com/news/meridian-deployments))
- **Likely weakness:** zero manufacturing channel — no distributor listings, no integrator partnerships, no plant-floor certifications on record — **Fact** (registry and catalog absence, checked Aug 2026)
- **Key source URL:** [API documentation](https://example.com/meridian/docs)

### Competitor: Corvid Industrial
- **Positioning:** "focused industrial automation" (post-split messaging) — **Fact** ([investor page](https://example.com/corvid/investors))
- **Relevant capability:** strong controls-engineering services arm in aerospace-adjacent plants — **Fact** (segment reporting)
- **Likely strength:** deep integrator relationships in its verticals — **Inference** (partner-award history)
- **Likely weakness:** split-driven distraction; two senior product leaders departed within four months of separation — **Fact** ([announcements](https://example.com/news/corvid-departures)); employee reviews mention "reorg" at 3x the category rate — **Inference** (review mining)
- **Key source URL:** [separation filing](https://example.com/corvid/form10)

## 3. Quick Comparison
| Dimension | Northfield | Helix | Meridian | Corvid |
|---|---|---|---|---|
| Target customer | mixed-vendor mid-size plants (via integrators) | plants running Helix components | logistics/warehouse (today) | aerospace-adjacent plants |
| Core use case | software-defined retrofit | aftermarket monitoring on own base | autonomous material movement | controls engineering projects |
| Main strength | vendor-agnostic software | installed base + channel | platform software maturity | integrator trust in-vertical |
| Main weakness | no retrofit product yet | single-vendor coverage | no manufacturing channel | post-split distraction |
| Evidence quality | high (own data) | high (filings + docs) | medium (inference on transfer intent) | high |

## 4. So What?
- **Product strategy implications:**
  1. Lead with monitoring *software* for mixed-vendor plants — it attacks Helix's structural gap (single-vendor coverage) with Northfield's actual strength, and hardware kits would fight Helix's distributor moat head-on — **Inference**, confidence: high
  2. Meridian is the future competitor, not the current one: architecture transfers, channel doesn't — their entry timeline is gated by certifications and distributor onboarding, both publicly observable — **Inference**, confidence: medium
  3. Corvid's vertical integrator relationships are momentarily contestable — distraction windows close — **Inference**, confidence: medium
- **Competitive risks:**
  1. Helix opens Foresight to third-party equipment, erasing the mixed-vendor gap — **Assumption**, watch their compatibility docs
  2. Meridian buys its manufacturing channel (acquires an integrator roll-up) instead of building it — **Assumption**, watch M&A
- **Product opportunities:**
  1. Machinery-safety documentation automation bundled with monitoring — nobody ships it — **Fact** (feature absence across all three)
  2. Integrator-white-label program — turns the channel threat into distribution — **Inference**
- **Assumptions to validate:**
  1. Integrators will carry a Northfield product at loyalty-keeping margins (carried from the scan — still open)
  2. Mixed-vendor plants are the majority of the 100-500-employee segment (needs establishment data)
  3. Meridian's asset-agnostic API reflects strategy, not accident

---

## Why this example works

- **The discipline mix shifted with the market.** The SaaS sibling leaned on pricing pages and
  changelogs; this one leans on filings, segment reporting, certifications registries, and
  distributor catalogs — because that's where industrial competitors leave fingerprints. Same
  schema, same labels, different sources.
- **Absence of evidence became evidence, honestly labeled.** Meridian's missing distributor
  listings and certifications are *Facts* (checkable absences) that ground the "future, not
  current, competitor" call — and its evidence-quality cell is marked medium because the transfer
  *intent* is still inference.
- **The decision got a real answer with a falsifiable basis:** lead with software because of
  Helix's single-vendor gap. If Risk 1 materializes (Foresight opens up), the strategy's
  foundation is named and the watch knows exactly what to look for.
- **It chains:** the As-of date and these assumptions are what the industrial
  `competitive-intel-watch` example diffs against.
