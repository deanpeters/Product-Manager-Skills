# Product Lifecycle Plays Template

Three worksheets: the stage diagnosis (per product), the portfolio view (per line), and the risk
register (replacement plays only). Quality checks at the bottom.

## Provenance
Distilled from practitioner experience running product lifecycle transitions and product
retirements across software, hardware, and regulated industries.

---

## Worksheet 1: Stage Diagnosis

```markdown
## Lifecycle Diagnosis: [Product Name]

**Trigger**: [what prompted this question]
**Revenue trend**: [direction over how many quarters]

### Transition Questions

| # | Lever | Ask | Yes/No | Evidence |
|---|---|---|---|---|
| 1 | Marketing objective | Is defending market share still profitable? | [ ] | [note] |
| 2 | Competition | Are loyalty efforts no longer retaining users? | [ ] | [note] |
| 3 | Product | Are legacy support costs becoming unsustainable? | [ ] | [note] |
| 4 | Promotion | Should we run migration campaigns instead of loyalty? | [ ] | [note] |
| 5 | Place | Are we losing money on certain channels? | [ ] | [note] |
| 6 | Price | Are our value-add bundles losing effectiveness? | [ ] | [note] |
| 7 | Data strategy | Is our data shifting from predictive to transitional? | [ ] | [note] |

**Yes count**: [0-7]
**Stage**: [Mature and healthy / Mature and softening / Crossing into decline / In decline]

### Pressure Source

- [ ] **Demand-side** -- needs shifted, segments moved, competitors differentiated
- [ ] **Supply/cost-side** -- components, production cost, support load, strategy
- [ ] **Capability-side** -- technology obsolete, architecture at its limit, regulation

**Primary pressure**: [which one, and the evidence]

### Extension Test (answer all four before ruling it out)

1. Is there a segment a variant could serve? [Yes/No -- why]
2. Is there a need an added capability would meet without re-architecture? [Yes/No -- why]
3. Would a repackage or rebrand reach a different buyer? [Yes/No -- why]
4. Is the decline in the product, or in the channel or price around it? [which]

### Recommended Play

**Play**: [Extend / Replace / Retire / Harvest]
**Because**: [two or three specifics from above]
**What this play costs**: [rough shape of the investment]
**What we're accepting by choosing it**: [the tradeoff, stated plainly]
```

---

## Worksheet 2: Portfolio View

For a product line. Fill one row per product, then check the interactions.

```markdown
## Lifecycle Plays: [Product Line]

| Product | Stage | Yes-count | Pressure | Reasons to Extend | Reasons to Replace | Reasons to Retire | Play |
|---|---|---|---|---|---|---|---|
| [A] | [stage] | [n]/7 | [source] | [reason] | [reason] | [reason] | [play] |
| [B] | | | | | | | |
| [C] | | | | | | | |
| [D] | | | | | | | |

### Interaction Checks
- [ ] No two products are the replacement for the same customers
- [ ] No extension undercuts the case for another product's replacement
- [ ] No two retirements land in the same window for the same customer
- [ ] Sequencing across the line is deliberate, not incidental
```

---

## Worksheet 3: Risk Register (replacement plays)

```markdown
## Replacement Risk Register: [Old Product] -> [New Product]

| # | Hazard | Applies? | Probability | Impact | Mitigation | Contingency (Plan B) |
|---|---|---|---|---|---|---|
| 1 | GTM process failure | [ ] | [H/M/L] | [H/M/L] | [action] | [Plan B] |
| 2 | Delayed market entry | [ ] | | | | |
| 3 | Internal misalignment | [ ] | | | | |
| 4 | External forces | [ ] | | | | |
| 5 | Regulatory risk | [ ] | | | | |
| 6 | Unexpected cannibalization | [ ] | | | | |
| 7 | Poor EOL management | [ ] | | | | |

### Cannibalization Plan
- Which product wins which customer: [answer]
- Margin during the overlap period: [answer]
- How long the overlap runs: [answer]

### Retirement Funding
- Who owns the EOL of the old product: [named owner]
- Is it funded: [Yes / No -- and if no, what that means]
```

---

## Quality checks

Any "no" is a rewrite, not a nitpick.

**Diagnosis before play**
- [ ] All seven transition questions answered with evidence, not vibes
- [ ] The play was chosen after the diagnosis, not defended by it
- [ ] The pattern of yeses — not just the count — informed the choice

**Extension got a fair hearing**
- [ ] All four extension questions answered explicitly
- [ ] If extension was ruled out, the "no, because…" is written down
- [ ] Channel and price were checked before the product was condemned

**Honesty about pressure**
- [ ] The pressure source is named, including when it's "our costs, not their needs"
- [ ] What the chosen play costs, and what it trades away, are both stated

**Replacement rigor (if replacing)**
- [ ] Every applicable hazard has a contingency, not just a mitigation
- [ ] Nothing is rated low/low without a reason
- [ ] Cannibalization is planned in both directions — who wins, and what margin does
- [ ] **The retirement is funded and owned** — otherwise this is an extension with extra steps

**Portfolio coherence (if a line)**
- [ ] Interaction checks completed
- [ ] Retirement windows don't stack on the same customers
