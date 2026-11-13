# Recommendation Canvas Example — Life Sciences

An AI investment decision at **Brightwater Biologics** for **Trialpath**, the platform its
coordinators and monitors use to run clinical studies.

**Why this domain changes the AI decision:** the question isn't only "does the model work well
enough." It's "who is accountable when it's wrong, and can that answer survive an audit." A model
at 94% accuracy is excellent in most products and potentially unusable here, depending entirely on
what happens with the other 6%.

---

```markdown
## AI Query Triage Canvas — Trialpath

### The Opportunity
Monitors raise data queries against site-entered trial data. Sites currently receive them as an
undifferentiated queue and work them in arrival order. Median resolution is 11 days; the queries
that actually block database lock are indistinguishable from routine ones until someone reads
each one.

### Target Outcome
Reduce median resolution time for lock-blocking queries from 11 days to under 4, without
increasing the rate of queries closed incorrectly.

### Hypotheses
1. **If** queries are ranked by likely impact on database lock, **then** sites will resolve
   blocking queries first, **because** the current queue gives them no basis to choose
2. **If** ranking is presented as a suggestion with the reason shown, **then** coordinators will
   use it, **because** an unexplained ordering in a regulated workflow gets ignored
3. **If** a human remains the decision-maker on every query, **then** the capability stays within
   existing validation scope

### AI Suitability
- **Good fit:** ranking and suggestion over a corpus of historical queries with known outcomes
- **Poor fit:** auto-closing queries, auto-editing data, or anything that writes to the
  trial record without a person
- **The line:** the model orders work. A human does the work and is accountable for it.

### Risks
| Risk | Severity | Mitigation |
|---|---|---|
| Model deprioritizes a blocking query | **High** | Ranking never hides queries; full queue always visible and sortable |
| Coordinators over-trust the ranking | Medium | Show the reason for each rank; no confidence scores presented as certainty |
| Regulatory acceptability of AI in workflow | **High** | Suggestion-only, human-in-loop, decisions and rationale in the audit trail |
| Training data reflects historical bias | Medium | Validate ranking against a held-out set from sites not in training data |
| Model drift as protocols change | Medium | Quarterly re-evaluation; documented retraining trigger |

### Positioning
Not "AI-powered trial management." Internally and externally: *"Trialpath suggests which queries
to work first, and shows you why."* The claim is deliberately small and defensible.

### Kill Criteria
- If held-out ranking accuracy on blocking queries falls below 80%, stop
- If validation scope must expand to a full computerized-system revalidation, stop and reassess
  cost against the 7-day benefit
- If coordinators in pilot ignore the ranking more than half the time, the problem isn't ranking

### Decision
**Proceed to a two-site pilot**, suggestion-only, with the validation impact assessment completed
before any model touches production data.
```

---

## What this canvas teaches that the SaaS one can't

- **"AI suitability" has a hard line, and it's drawn on accountability.** The model *orders* work;
  a human *does* it. That single distinction keeps the capability inside existing validation scope
  — and if it were crossed, the entire cost structure of the feature changes.
- **Two risks are rated High, and neither is model accuracy.** Deprioritizing a blocking query and
  regulatory acceptability both outrank raw performance. In most products accuracy is the headline
  risk; here it's a mid-tier input to a bigger question.
- **The mitigation for the top risk is a design constraint, not a model improvement.** "Ranking
  never hides queries" means the worst case degrades to today's behavior. Designing the failure
  mode to be the status quo is often stronger than making the model better.
- **Positioning is deliberately unimpressive.** "Suggests which queries to work first, and shows
  you why" is a smaller claim than the marketing instinct wants — and it's the version that
  survives an auditor asking what the system does.
- **A kill criterion targets the mechanism, not just the metric.** If coordinators ignore the
  ranking, the problem isn't ranking quality — it's that ordering wasn't the constraint. That
  criterion prevents a year of model tuning against the wrong bottleneck.
