# Stakeholder Identification Template

Six steps, one worksheet each. Quality checks at the bottom.

## Provenance
Adapted from `prompts/` in the
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts) repo.

---

## Step 1: Brainstorm without filtering

Four to six minutes, silent if in a group. Do not evaluate yet — evaluating during generation is
what produces a list of the same eight people every time.

```markdown
## Stakeholder Brainstorm: [Initiative]

Individuals, teams, organizations, and groups:
- [name or role]
- [name or role]
```

---

## Step 2: Categorize

A stakeholder can appear in more than one column. **The overlaps are the interesting part** — an
ally who is also a gatekeeper is a different relationship than either alone.

```markdown
| Stakeholder | Ally | Audience | Influencer |
|---|---|---|---|
| [who] | ✓ | | ✓ |
```

- **Allies** — actively support this, or benefit from its success
- **Audiences** — impacted by the outcome, directly or indirectly
- **Influencers** — shape decisions, opinion, or adoption without participating directly

---

## Step 3: R/P/D marking

```markdown
| Stakeholder | R (Resources) | P (Permission) | D (Decision) | Notes |
|---|---|---|---|---|
| [who] | budget/data/access | approval/sign-off | final say | |
```

**The gap test:** anyone holding **P** or **D** who wasn't in your Step 1 list is a gap that will
surface later as a blocked launch. Add them now and note that you missed them — the pattern of who
you forget is itself information.

---

## Step 4: Equity lens

```markdown
### Equity Lens

- Who experiences a significant consequence — financially, professionally, or personally?
- Who bears the product's costs or risks **without power to shape its design**?
- Whose perspective is missing because we assumed someone else represents them?
- Primary users? Secondary users? Affected in the third degree?

**Added by this lens:**
- [who, and what consequence they bear]
```

Stakeholders surfaced here usually land in Q1 of a stakeholder map — high impact, low power — and
are the ones most likely to be discovered late.

---

## Step 5: Bias and assumptions

```markdown
### Bias Check

- Who did we default to naming first? [answer]
- Who is absent, and why? [answer]
- What did we assume about who counts as a stakeholder? [answer]
```

Record the answers. They shape the research plan and recruitment strategy, not just this list.

---

## Step 6: Narrow to priority targets

Two or three. More than that isn't prioritization.

```markdown
### Priority Stakeholders

| Name | Category | R/P/D | What we need to learn |
|---|---|---|---|
| | | | |
```

Choose from:
- Highest-power decision-makers whose buy-in is required
- Highest-impact users whose needs are least understood
- Most likely blockers or skeptics

---

## Quality checks

**Generation**
- [ ] Step 1 ran without filtering — no one was excluded during brainstorm
- [ ] The list includes people outside your organization where relevant

**Coverage**
- [ ] Every P and D holder appears; any late additions are noted as gaps
- [ ] Overlaps between categories are marked rather than forced into one column
- [ ] The equity lens actually added someone. If it added nobody, it wasn't run honestly

**Honesty**
- [ ] The bias check names a real default, not "we were thorough"
- [ ] Someone who bears cost without power is on the list

**Prioritization**
- [ ] Two or three priority targets, not eight
- [ ] Each has a specific "what we need to learn," not "understand their needs"
- [ ] At least one is a likely skeptic or blocker
