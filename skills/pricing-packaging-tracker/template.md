# Pricing Capture / Delta Report Template

Copy this for each tracking run. A single capture is trivia; **the sequence is intelligence** —
the schema never drifts between runs, because diffability is the entire value. Watch structure as
closely as numbers: tiers, gates, limits, and free-tier boundaries move before prices do, and a
tier that disappears telegraphs a move upmarket months before the price list admits it.

Never invent prices, tiers, limits, discounts, or negotiated figures. "Contact sales" is data —
record the honest boundary and label any inference.

## Template

```markdown
# Pricing Capture / Delta Report

## 1. Run Header
**Competitor set:** [list]
**Prior capture date:** [YYYY-MM-DD, or "baseline run"]
**This run date:** [YYYY-MM-DD]

## 2. Pricing Capture (per competitor)
_Baseline mode: full capture per competitor. Delta mode: this section only for competitors
with changes._

### [Competitor] — [pricing page URL, as-of date]
- **Tiers:** [name: price / unit / billing terms, one bullet each]
- **Key gates:** [which capabilities gate which tier, 2-4 bullets]
- **Usage limits:** [the limits that matter, 1-2 bullets]
- **Free tier / trial:** [boundary, 1 bullet]
- **Enterprise signals:** [published floors, "contact sales" scope]

## 3. Changes Since Last Capture (Delta Mode)
### [Competitor] — [4 to 8 word change summary]
- **Then / Now:** [old -> new, labeled Fact]
- **Evidence:** [URL, date — archive/diff link where possible]
- **Reading:** [Inference — repositioning, monetization push, response to whom?]

_If nothing changed:_ "No pricing or packaging changes this cycle."

## 4. Signals
- [Cross-competitor patterns: direction of the market's pricing, labeled]
- [Implications for your pricing or battle cards: 2-3 bullets]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]
```

## Quality checks before you call it done

- Every capture has a URL and as-of date — undated pricing can't be diffed next run
- Gates and limits are recorded, not just prices — the gate moves first
- No "contact sales" cell contains an invented figure; inferences are labeled as such
- The schema matches the prior run exactly — "improving" the format between runs breaks every future diff
- A named artifact consumes this output (battle card, pricing review, watch report) — a cadence without a consumer dies quietly
