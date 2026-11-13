# Finance Metrics Snapshot Template

A decision-first worksheet: name the call you're making, pull only the metrics that bear on it,
then read them together. Quality checks at the bottom.

## Provenance
Adapted from `prompts/` in the
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts) repo.

**Note:** this skill is deliberately single-domain — the metrics are SaaS metrics — so it ships a
template without the usual second-domain worked example.

---

## Worksheet 1: Decision snapshot

Start with the decision. Metrics pulled without one become a dashboard nobody acts on.

```markdown
## Metrics Snapshot: [Decision being made] — [Date]

**The call:** [build / don't build, scale / kill a channel, raise / hold price,
hire / wait, raise capital / extend runway]
**Who decides:** [name or role]
**By when:** [date]

### Metrics that bear on this call

| Metric | Current | Trend | Benchmark | Read |
|---|---|---|---|---|
| [metric] | [value] | [up/flat/down over N periods] | [healthy range] | [green/watch/red] |

### Metrics I could not get
| Metric | Why it matters here | What I'm assuming instead |
|---|---|---|

### The read
[Two or three sentences. What the numbers say together — not one at a time.]

### The call
[Decision + the single metric that would change your mind if it moved.]
```

---

## Worksheet 2: Four-lens health check

For a periodic review rather than a single decision. Pull one or two per lens, not all of them.

```markdown
## Business Health Snapshot — [Period]

### Growth
| Metric | Value | Trend | Read |
|---|---|---|---|
| Revenue growth rate | | | |
| New vs. expansion mix | | | |

### Retention
| Metric | Value | Trend | Read |
|---|---|---|---|
| NRR | | | |
| Gross churn | | | |
| Cohort direction (recent vs. older) | | | |

### Unit economics
| Metric | Value | Trend | Read |
|---|---|---|---|
| CAC payback (months) | | | |
| LTV:CAC | | | |
| Gross margin | | | |

### Capital efficiency
| Metric | Value | Trend | Read |
|---|---|---|---|
| Burn multiple | | | |
| Runway (months) | | | |

### What these say together
[The cross-lens read. Strong growth + weak payback is a different
company than flat growth + strong payback. The interaction is the
insight; single metrics rarely are.]

### The one thing to fix first
[Named, with why it outranks the others.]
```

---

## Worksheet 3: Red-flag scan

```markdown
## Red Flags — [Date]

| Category | Flag | Present? | Evidence | Urgency |
|---|---|---|---|---|
| Growth | Growth decelerating while spend rises | | | |
| Retention | NRR below 100% | | | |
| Retention | Recent cohorts retaining worse than older | | | |
| Economics | CAC payback lengthening quarter over quarter | | | |
| Economics | Gross margin declining as you scale | | | |
| Capital | Burn multiple rising | | | |
| Capital | Runway under 12 months without a plan | | | |

**Leading vs. lagging:** [which flags are early warnings vs. damage already done]
**Acting on:** [the one or two you'll actually address this quarter]
```

---

## Quality checks

**Decision-first**
- [ ] The decision is written down **before** the metrics
- [ ] Every metric pulled bears on that decision — no metric is present just because it was easy
- [ ] The call names what would change your mind

**Honesty**
- [ ] Metrics you couldn't get are listed, with the assumption standing in for each
- [ ] Trends cover enough periods to be a trend, not a blip
- [ ] Benchmarks are stage-appropriate — early-stage optimizes for growth, scale-stage for
      efficiency, and applying the wrong benchmark produces confidently wrong reads

**Reading them together**
- [ ] The synthesis says what the metrics mean **in combination**, not one at a time
- [ ] Interactions are named — strong growth with weak payback is a different diagnosis than either
      signal alone
- [ ] Leading indicators are distinguished from lagging ones

**Action**
- [ ] Exactly one "fix first," with a reason it outranks the rest
- [ ] Nothing here is metrics theater: if the snapshot changes no decision, it wasn't worth pulling
