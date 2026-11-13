# Company Intel Template

The 11-section research brief as a copy/paste fill-in, plus the cross-company comparison block and
the rerun diff. Quality checks at the bottom.

## Provenance
Adapted from Dean Peters' company-profile-executive-insights research prompt in the
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts) repo.

---

## Before you fill anything in

**Label every claim.** This is an investigation artifact, so the reader must be able to tell what
you know from what you inferred:

- **Fact** — stated in a named source, with a link
- **Inference** — your reasoning from one or more facts; show the chain
- **Assumption** — you needed it to proceed and could not verify it

An unlabeled brief is an opinion wearing a citation.

---

## The brief

```markdown
# Company Intel: [Entity] — [Date]

**Entry point:** [Single company / Competitor set / Industry / Discover competitors]
**Research window:** [dates covered]
**Confidence:** [High / Medium / Low] — [what drives it]

## 1. What This Entity Is
[Business definition, founding, market position, scale. What makes it distinct.]

## 2. How It Makes Money
[Revenue streams, cost structure, margin dynamics, financial logic.
Seasonal or cyclical patterns. Growth levers and risks.]

## 3. Who It Serves
[Buyers, users, influencers, administrators, blockers.
Segment differences. Multi-stakeholder complexity.]

## 4. What It Sells or Delivers
[Core value propositions. Key offers in plain language.
How the offer creates value for the customer.]

## 5. Key Product Lines or Offers
[Mapped by product family, platform, service, channel.
Digital vs. human-assisted. Legacy vs. emerging.
Distinguish: business line, offer, product, feature set, service layer,
enabling platform.]

## 6. Business and Market Pressures
[Competitive forces, regulatory pressure, technology shifts,
operational constraints. Name the tensions.]

## 7. Competitors and Alternatives
[Direct, adjacent, substitutes, emerging disruptors.
Where differentiation is won or lost.]

## 8. Important Trends and Risks
[Macro forces, buyer expectation shifts, AI and automation impact,
consolidation or commoditization threats.]

## 9. Strategic Signals
[Patents: recent filings, technology domains, R&D bets.
Hiring: volume roles, skills language, seniority patterns.
Leadership: arrivals, departures, origins, new roles created.
Source every signal.]

## 10. What This Means for Product Management
[Org dynamics, discovery maturity, delivery model, cross-functional
friction, AI readiness. Product-led vs. sales-led. Likely PM
challenges. Domain skills a PM would need here. Label inferences.]

## 11. Sources and Confidence
[All sources, organized by section. Assumptions and inferences flagged
explicitly. Sections where data was thin, named as thin.]
```

---

## Cross-company comparison (competitor sets only)

Produce sections 1-11 per company first, then:

```markdown
## 12. Cross-Company Comparison

| Dimension | [Co A] | [Co B] | [Co C] |
|---|---|---|---|
| Business model | | | |
| Primary buyer | | | |
| Pricing posture | | | |
| Where they win | | | |
| Where they're exposed | | | |
| Strategic direction | | | |

**Where the market agrees:** [convergent bets]
**Where it splits:** [divergent bets — usually the interesting part]
**Whitespace:** [what nobody is serving, and a note on why]
```

---

## Rerun diff (Executive Signal Refresh)

When re-running against a prior brief, the **changes** are the output — not a fresh full brief.

```markdown
## Signal Refresh: [Entity] — [prior date] -> [now]

### Then / Now
| Signal | Then | Now | So what |
|---|---|---|---|
| [theme] | [prior language] | [current language] | [implication] |

### Dropped Language
[What leaders have STOPPED saying since the last read. Often the
strongest signal in the document — a quietly retired priority says
more than a new one.]

### New Language
[Themes that appeared since the last read.]

### Unchanged
[What held steady. Stability is a finding too.]
```

---

## Quality checks

Any "no" is a rewrite, not a nitpick.

**Evidence discipline**
- [ ] Every claim carries Fact / Inference / Assumption
- [ ] Every Fact has a source link; every Inference shows its chain
- [ ] Thin sections are named as thin rather than padded
- [ ] Nothing was invented to complete a section — an honest gap beats a plausible fill

**Depth**
- [ ] Every section pushes past description to **implication** — "so what for us?"
- [ ] Section 6 names specific tensions, not a list of industry facts
- [ ] Section 9 signals are sourced individually, not summarized
- [ ] Section 10 says something a PM could act on this week

**Source hygiene**
- [ ] Primary sources preferred over coverage-of-coverage
- [ ] **Do not sanitize** — quote leadership language as spoken, including the awkward parts
- [ ] Dates on every signal; a two-year-old hiring pattern is not a current signal

**Reruns**
- [ ] The diff is the deliverable, not a regenerated brief
- [ ] **Dropped Language** is populated — if you skipped it, you skipped the best signal
- [ ] Unchanged items are listed rather than silently omitted
