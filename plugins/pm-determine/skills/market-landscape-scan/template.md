# Market Landscape Snapshot Template

Copy this to record a landscape scan. The section order is a contract: quarterly re-scans diff
against this document, and downstream skills (`tam-sam-som-calculator`, `competitive-research-snapshot`)
consume it. Do not reorder or rename sections — a changed schema silently breaks comparability.

Label every claim **Fact** (cited, verifiable), **Inference** (reasoned from facts, basis shown), or
**Assumption** (unverified, needs validation).

## Template

```markdown
# Market Landscape Snapshot

## 1. Scope
**Market / problem space:** [in the buyer's words, not an analyst category]
**Boundary:** [geography, buyer size, price band — or "none stated (Assumption)"]
**Decision supported:** [market entry / new product line / re-positioning / build-vs-buy]
**As-of date:** [YYYY-MM-DD — re-scans diff against this]

## 2. How This Market Segments
- [Segment 1 as buyers experience it — 1 bullet, labeled]
- [Segment 2 — 1 bullet, labeled]
- [Segment 3 (3-5 total) — 1 bullet, labeled]
- **Vendor/buyer disagreement:** [where vendor categories don't match buyer reality — often where the opportunity hides]

## 3. Player Map
_Cap the full map at 12 players; strongest signal only._

### Direct players
- **[Name]:** [who they serve; wedge; 1 momentum signal; URL]

### Adjacent players (could enter)
- **[Name]:** [why adjacency matters; URL]

### Substitutes and non-consumption
- **[What buyers do instead]:** [why it persists — the status quo is a competitor]

### Emerging entrants
- **[Name]:** [what bet they're making; funding/traction signal; URL]

## 4. Dynamics
- **Where the money is:** [2 bullets, labeled]
- **Where the momentum is:** [2 bullets, labeled]
- **Consolidation or fragmentation:** [1 bullet]
- **Technology or regulatory shifts in play:** [1-2 bullets]

## 5. Whitespace and Dead Zones
- **[Apparent gap]:** opportunity or dead zone? [evidence either way — the counter-reading is mandatory]
- [2-3 of these total, each with the honest counter-reading]

## 6. So What?
- **Implications for the decision in Scope:** [exactly 3, each with label + confidence]
- **Players to deep-dive next:** [exactly 2 — these feed `competitive-research-snapshot`]
- **Assumptions to validate:** [exactly 3]
```

## Quality checks before you call it done

- Every whitespace claim survived the *"or is it a dead zone?"* question with evidence, not hope
- "What buyers do instead" appears on the player map — a map without non-consumption flatters every vendor on it
- No section cites an analyst quadrant as the frame (one labeled OSINT source among many is fine)
- The As-of date is present — without it, the next re-scan has nothing to diff against
