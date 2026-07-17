# Market Landscape Scan — Worked Example (Industrial)

All companies, products, URLs, and figures are **fictional**. This is the industrial sibling of
[`sample.md`](sample.md) (SaaS): same schema, different physics. The scenario runs through the
whole chain's industrial examples — **Northfield Automation**, a software-led automation vendor,
scanning the retrofit-automation market before deciding whether to productize. Note what changes
when the market is industrial: analyst coverage thins, but MASINT-adjacent signals (facilities,
certifications, distributor networks) get loud.

**Invocation:** `Run a market landscape scan on retrofit automation and modernization for mid-size
discrete manufacturers, North America — this supports Northfield's decision on launching a
productized retrofit line versus staying in custom enterprise projects.`

---

# Market Landscape Snapshot

## 1. Scope
**Market / problem space:** getting 15-30-year-old production lines monitored and semi-automated without replacing them ("retrofit" is the vendor word; plant managers say "keep the line running and tell me why it stopped")
**Boundary:** North America; discrete manufacturers, 100-500 plant employees
**Decision supported:** whether Northfield launches a productized retrofit kit + software line, or stays in custom enterprise projects
**As-of date:** 2026-08-14

## 2. How This Market Segments
- **Corporate-engineering buyers (multi-plant):** modernization is a capital program; buy on standards compliance and vendor longevity — **Fact** ([trade association capital-spend survey, 2026](https://example.com/nam-survey))
- **Plant-manager buyers (single plant):** downtime is the only KPI; buy whatever the trusted systems integrator recommends — **Inference** (integrator-channel dominance per distributor data below)
- **Run-to-failure holdouts:** no monitoring, fix what breaks; the largest "segment" by plant count — **Inference** (census establishment counts vs. vendor-claimed install bases leave a huge remainder)
- **Vendor/buyer disagreement:** vendors segment by industry vertical (automotive, food & bev, aerospace); buyers segment by *who controls the retrofit budget* — corporate vs. plant. A "food & bev edition" doesn't answer the plant manager's actual question, which is whether it needs corporate sign-off — **Inference** (buyer-forum threads; [example](https://example.com/plantforum/budget-thread))

## 3. Player Map

### Direct players
- **Helix Motion Systems:** component incumbent moving up into monitoring via its "Foresight" aftermarket program; wedge is the installed base — their components are already in most plants; momentum signal: Foresight named a P&L owner in October — **Fact** ([Q3 earnings transcript](https://example.com/helix/q3-transcript))
- **Corvid Industrial (industrial arm):** post-split, refocusing; strong in aerospace-adjacent plants; momentum unclear — split-related integration noise dominates their signals — **Fact** ([split coverage](https://example.com/news/corvid-split))

### Adjacent players (could enter)
- **Meridian Freight Systems:** warehouse-robotics platform; adjacency matters because a warehouse-floor platform is one SKU away from a plant-floor platform, and their component order volumes keep climbing — **Fact** ([customs records via trade data](https://example.com/tradedata/meridian))

### Substitutes and non-consumption
- **The systems integrator as substitute:** plants don't buy products, they buy their integrator's judgment; a "product" that bypasses the integrator competes with the buyer's most trusted advisor — **Inference** (channel structure)
- **Run-to-failure:** persists because the CFO sees monitoring as cost, not insurance, until the first six-figure downtime event — the true incumbent in this market

### Emerging entrants
- **Sensor-first startups (2-3 funded in 18 months):** bet: clip-on vibration/current sensors + dashboards, no controls integration; traction: pilot announcements but no distributor listings yet — **Fact** (funding coverage) / **Inference** (distributor-catalog absence = no channel, which in this market means no scale)

## 4. Dynamics
- **Where the money is:** service contracts, not hardware — incumbents' investor materials break out "aftermarket & services" as the margin engine — **Fact** ([Helix investor deck](https://example.com/helix/investor)); corporate capital programs carry 10x the deal size of plant-level purchases — **Inference** (published case-study deal shapes)
- **Where the momentum is:** aftermarket data plays (Foresight-style) — three incumbents launched monitoring subscriptions in 12 months — **Fact** (product pages); the integrator channel is consolidating — two regional integrator roll-ups this year — **Fact** ([M&A coverage](https://example.com/news/integrator-rollups))
- **Consolidation or fragmentation:** consolidating at every layer — vendors, integrators, even distributors — **Fact** (same coverage)
- **Technology or regulatory shifts in play:** updated machinery-safety rules add documentation burden to any retrofit touching controls — **Fact** ([regulatory register](https://example.com/regs/machinery)); AI-based anomaly detection is in every vendor's marketing and almost nobody's spec sheets — **Inference** (marketing/docs gap)

## 5. Whitespace and Dead Zones
- **Productized retrofit for the 100-500-employee plant, sold *through* integrators:** opportunity or dead zone? Nobody productizes for this segment — but the sensor startups that tried bypassing integrators stalled at pilots — **Fact** (no distributor listings after 18 months). Verdict: conditional whitespace — the product must make the integrator the hero, not the casualty. **Assumption to validate:** integrators will carry a Northfield product line at margins that keep them loyal.
- **Direct-to-plant-manager e-commerce for sensors:** opportunity or dead zone? Two attempts, both pivoted to channel sales — **Fact** (their own announcements). Verdict: dead zone; this market buys trust, not SKUs.

## 6. So What?
- **Implications for the decision in Scope:**
  1. A productized line is viable only as an integrator-channel play — direct product sales fight the market's trust structure and lose — **Inference**, confidence: high
  2. Helix's Foresight makes the installed base the battleground: they monetize *their* components' data; Northfield's opening is plants with mixed-vendor equipment Foresight won't cover — **Inference**, confidence: medium
  3. The machinery-safety documentation burden is a feature opportunity wearing a compliance costume — whoever automates the paperwork wins the integrator's love — **Inference**, confidence: medium
- **Players to deep-dive next:** Helix Motion Systems (the installed-base incumbent), Meridian Freight Systems (the adjacent platform whose customs data says something is coming)
- **Assumptions to validate:**
  1. Integrators will carry a productized Northfield line at loyalty-keeping margins
  2. Mixed-vendor plants are numerous enough to be a wedge (needs GEOINT/DEMOINT establishment data)
  3. Corvid's post-split quiet is distraction, not stealth

---

## Why this example works

- **Same schema, different physics.** Compare with the SaaS example: the segmentation axis moved
  from "who gets paged" to "who controls capital," the killer substitute moved from a whiteboard
  to the systems integrator, and the freshest signals moved from pricing pages to customs records
  and distributor catalogs. The schema held; the tradecraft adapted.
- **Non-consumption is still the biggest competitor** — run-to-failure here, the whiteboard in
  SaaS. Every market has one; it never appears in a quadrant.
- **The dead-zone test killed a tempting idea** (direct e-commerce) using the market's own failed
  attempts as evidence — and conditioned the surviving whitespace on the channel insight.
- **Section 6 hands off to the industrial chain:** Helix and Meridian are exactly who the
  `competitive-research-snapshot` industrial example picks up.
