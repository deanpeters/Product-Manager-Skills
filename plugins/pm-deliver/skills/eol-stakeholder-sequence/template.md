# EOL Stakeholder Sequence Template

Pick a level, order the stops, then fill five fields per stop. Quality checks at the bottom.

## Provenance
Adapted from `prompts/eol-stakeholder-sequence.md` in the
`https://github.com/deanpeters/product-manager-prompts` repo.

---

## Pick your level first

| | Level 1 — Light | Level 2 — Standard | Level 3 — Heavy |
|---|---|---|---|
| Scope | Feature, internal tool, API | Commercial product, active customers | Revenue-critical, hardware, regulated |
| Stops | 3-4 | 7-8 | 10+ |
| Adds | Engineering, Support, affected users | + Legal, Finance, Sales, Marketing, CS, difficult customers | + Executives, Channel, Regulatory, key accounts |

**Most sequences are Level 2.** Never default to the heaviest.

**Sticky-note rule:** every bullet is 4-8 words.

---

## Template

```markdown
## EOL Stakeholder Sequence: [Product Name]

**Level**: [1-Light / 2-Standard / 3-Heavy]
**Stops in scope**: [count]
**Stops deliberately skipped**: [list + one-line why]

### Sequencing Principle

Talk to the people who can kill the plan before you talk to the people
who have to execute the plan. Each conversation informs the next. Do
not parallelize stops with upstream/downstream dependencies.

---

### Stop [N]: [Function or Stakeholder]

**When**: [Before/after which milestone or other stop]

**Why this stop matters for EOL**:
- [Reason in 4-8 words]

**What you need FROM them**:
- [Specific question or input needed]
- [Specific question or input needed]

**What you owe TO them**:
- [Context, lead time, or commitment you provide]
- [Context, lead time, or commitment you provide]

**Red flags to watch for**:
- [Signal that this stop surfaced a blocker]

**Output of this conversation**:
- [Decision, approval, or artifact produced]

(Repeat for each stop.)

---

### Parallel vs. Sequential Guidance

**Must be sequential**:
- [Stop A before Stop B: reason]

**Can run in parallel**:
- [Stop X and Stop Y: reason]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]
```

---

## The canonical order (filter by level)

**Level 2+ goes first, ahead of the Level 1 stops:**

1. **Legal** — contractual and regulatory exposure
2. **Finance** — revenue impact and forecast changes
3. **Sales** — pipeline, bundles, and field promises never written down
4. **Marketing** — campaigns already bought for the thing you're killing
5. **Customer Success** — they bear the brunt; work with them, not around them
6. **Your most difficult customers** — they find what you forgot

**Level 1+:**

7. **Engineering** — what depends on this technically
8. **Support** — what changes for support operations
9. **Affected users or internal teams** — who feels it first

**Level 3+:**

10. **Executive leadership** — strategic approval
11. **Channel partners** — inventory, commitments, their customer relationships
12. **Regulatory bodies** — filings and compliance
13. **Key accounts** — individual transition conversations

---

## Quality checks

Any "no" is a rewrite, not a nitpick.

**Order**
- [ ] Legal comes before anyone who'd have to replan if a contract term bites (L2+)
- [ ] Finance sizes the impact before revenue-facing teams are asked to act on it
- [ ] Sales is *asked what they promised* before being told the date
- [ ] The public announcement sits at the end of the internal sequence, not the start

**Completeness per stop**
- [ ] Every stop names when it happens, relative to another stop or milestone
- [ ] Every stop has both directions filled: what you need AND what you owe
- [ ] Every stop names an output — a decision, approval, or artifact
- [ ] Every stop lists at least one red flag to listen for

**Proportion**
- [ ] Level was chosen deliberately, not defaulted to the heaviest
- [ ] Skipped stops are named with a reason, not silently dropped
- [ ] If you dropped Legal or Finance, you know what that stop usually catches

**The stop teams skip**
- [ ] Two or three of your most difficult customers are in the sequence (L2+)
- [ ] Channel partners hear it from you before they hear it from their customers (L3)

**Sequencing hygiene**
- [ ] Parallel stops genuinely have no dependency between them
- [ ] Any stop moved out of canonical order has a stated reason
