---
name: market-landscape-scan
argument-hint: "[market or problem space, and the decision it supports]"
description: "Map a market's segments, players, substitutes, and whitespace with cited evidence. Use when entering or re-evaluating a market before sizing, positioning, or picking competitors to study."
intent: >-
  Autonomous market discovery: map how buyers segment the market, who plays where (direct, adjacent,
  substitutes, emerging), where the money and momentum are, and whether apparent whitespace is
  opportunity or dead zone — with labeled evidence, so sizing and positioning start from structure
  instead of vibes.
type: workflow
theme: market-intelligence
best_for:
  - "Mapping who plays in a market before committing to enter or re-position"
  - "Scoping a new product line with a defensible view of segments and substitutes"
  - "Producing the landscape view that feeds TAM/SAM/SOM sizing and competitor deep-dives"
scenarios:
  - "We're considering a move into contract-analytics tooling — map that market for me"
  - "My exec team keeps citing an analyst quadrant; show me how buyers actually segment this space"
estimated_time: "20-40 min per run"
---

# Market Landscape Scan

## Purpose

Map a market's structure using a workflow, not a one-shot answer: **search plan → segmentation →
player mapping → dynamics → whitespace → next-step options.** The output is the landscape view that
everything downstream stands on — sizing needs to know the segments, positioning needs to know the
players, and competitor deep-dives need to know who's worth the effort. This skill maps structure,
not magnitude: it tells you who plays where and why, not how big the prize is.

## Input

**Works best with:** the market, segment, or problem space to map — in your words, not an analyst
category — and **the decision this landscape should support** (market entry, new product line,
re-positioning, build-vs-buy).
**Also useful:** any boundary narrower than global — geography, buyer size, price band — and players
you already know about, so the scan spends its effort on what you don't.

Input supplied inline with the invocation — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as answers already given. Use it against the question budget;
don't re-ask.

**Arriving empty-handed? That works too.** The skill opens with at most 3 questions (market, decision,
boundary) and proceeds on labeled assumptions if they go unanswered — that's the
`autonomous-investigation` contract.

**Example invocation:** `Run a market landscape scan on developer-facing API observability tools,
EU-only — this supports a Q4 market-entry decision.`

## Key Concepts

- **Governing protocol:** this skill honors the [`autonomous-investigation`](../autonomous-investigation/SKILL.md)
  contract — question budget of 3, search-plan gate, Fact/Inference/Assumption labels, Just Enough
  Mode, stable schema, 4-option Final Step.
- **Discipline mix:** primarily OSINT (analyst and review coverage, press, communities) with
  GEOINT/DEMOINT for segment reality-checks and FININT for funding signals — see
  [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md).
- **Buyer-view segmentation.** Map the market as *buyers* experience it, not as vendors or analysts
  carve it — and note where the two disagree. Analyst quadrants are a map someone else drew for their
  own purposes; the disagreement between vendor categories and buyer reality is often where the
  opportunity hides.
- **Non-consumption is a competitor.** "They use spreadsheets" belongs on the player map. Treating
  substitutes and non-consumption as competitors is the most commercially useful habit in market
  analysis — the biggest rival is usually the status quo, and it never shows up in a quadrant.
- **The dead-zone test.** Every whitespace claim must survive the question *"or is it a dead zone?"*
  Empty space is either opportunity or evidence of no demand; the honest counter-reading is mandatory,
  not optional.
- **Do-not-invent list (this domain's fabrication risks):** companies, products, funding rounds,
  market share, growth rates, customer claims.

## Application

1. **Credit inline context**, then ask only the unanswered questions (max 3):
   1. What market or problem space, in your words?
   2. What decision should this landscape support?
   3. Any boundary — geography, buyer size, price band?
   If unanswered, proceed with labeled assumptions.
2. **Show the 3-bullet search plan** — what you'll search, source types (analyst and review sites,
   company and pricing pages, funding databases, industry press, trade bodies, practitioner
   communities), and how facts will be separated from inference. Continue unless revised.
3. **Research in Just Enough Mode** and emit the schema below *exactly* — it is the stable base
   that quarterly re-scans diff against.

### Output schema (do not reorder)

~~~markdown
# Market Landscape Snapshot

## 1. Scope
**Market / problem space:** | **Boundary:** | **Decision supported:** | **As-of date:**

## 2. How This Market Segments
- [3-5 segments as buyers experience them, each 1 bullet]
- [Where vendor categories disagree with buyer reality: 1 bullet]

## 3. Player Map
### Direct players
- **[Name]:** [who they serve; wedge; 1 momentum signal; URL]
### Adjacent players (could enter)
- **[Name]:** [why adjacency matters; URL]
### Substitutes and non-consumption
- **[What buyers do instead]:** [why it persists]
### Emerging entrants
- **[Name]:** [what bet they're making; funding/traction signal; URL]

Cap the full map at 12 players; strongest signal only.

## 4. Dynamics
- **Where the money is:** [2 bullets, labeled]
- **Where the momentum is:** [2 bullets, labeled]
- **Consolidation or fragmentation:** [1 bullet]
- **Technology or regulatory shifts in play:** [1-2 bullets]

## 5. Whitespace and Dead Zones
- **[Apparent gap]:** opportunity or dead zone? [evidence either way]
- [2-3 of these, each with the honest counter-reading]

## 6. So What?
- **3** implications for the decision named in Scope
- **2** players to deep-dive next
- **3** assumptions to validate
Each bullet: label, confidence, URL where relevant.
~~~

### Final Step (offer exactly 4 options)

1. Run [`competitive-research-snapshot`](../competitive-research-snapshot/SKILL.md) on the deep-dive players
2. Run [`tam-sam-som-calculator`](../tam-sam-som-calculator/SKILL.md) sizing on the most promising segment
3. Draft a positioning hypothesis against this landscape ([`positioning-statement`](../positioning-statement/SKILL.md))
4. Schedule-ready version: what should a quarterly re-scan watch?

Accept `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`, or a custom path.

## Examples

**Segmentation catching a vendor/buyer disagreement (all names fictional):**

> Vendors in this space market three categories: "observability platforms," "APM," and "log
> management." Buyers in practitioner forums segment differently — **Fact**
> ([community thread, Jun 2026](https://example.com/thread)): by *who gets paged* (dev-owned vs.
> ops-owned) and by *cost model tolerance* (per-seat vs. per-GB). Two "different" vendor categories
> compete head-to-head for dev-owned/per-seat buyers — **Inference** (same buyers evaluating both in
> review-site comparisons). The category language is marketing architecture, not market structure.

**A whitespace claim surviving the dead-zone test:**

> **Apparent gap:** nobody serves sub-50-employee agencies at self-serve pricing. Opportunity or dead
> zone? Two prior entrants targeted exactly this and pivoted upmarket within 18 months — **Fact**
> ([funding announcements, URLs](https://example.com)). Their stated reason was willingness-to-pay,
> not demand — **Inference** (founder postmortem cites CAC/LTV, not lack of interest). Verdict:
> conditional whitespace — viable only with a radically cheaper acquisition motion. **Assumption to
> validate:** the segment's tooling budget clears $50/month.

## Common Pitfalls

- **Adopting the analyst map.** Reciting a quadrant is not a landscape scan — quadrants exclude
  substitutes, lag emerging entrants, and segment by what's convenient to rank. Use them as one
  OSINT source, labeled, never as the frame.
- **Omitting non-consumption.** A player map without "what buyers do instead" flatters every vendor
  on it and hides the real competitor: inertia.
- **Whitespace romanticism.** Declaring every empty cell an opportunity. If the counter-reading is
  missing, the analysis is a pitch, not intelligence.
- **Player-map sprawl.** Twenty players with two facts each beats nothing, but twelve with the
  strongest signal each beats it badly. The cap is the discipline.
- **Scope drift between re-scans.** Changing the boundary or schema between runs silently breaks
  comparability — a re-scan of a different scope is a new baseline, and should say so.

## References

- [`autonomous-investigation`](../autonomous-investigation/SKILL.md) (Workflow) — the governing protocol
- [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) (Component) — discipline sources and signal chains
- [`competitive-research-snapshot`](../competitive-research-snapshot/SKILL.md) (Workflow) — deep-dive on the players this scan surfaces
- [`tam-sam-som-calculator`](../tam-sam-som-calculator/SKILL.md) (Component) — sizes the segments this scan maps
- [`positioning-statement`](../positioning-statement/SKILL.md) (Component) — positions against this landscape
- Adapted from `market-intelligence/market-landscape-scan-prompt.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
