# Investigation Brief Template

Copy this when launching an investigation under the autonomous-investigation protocol — either to
brief an agent (paste it with the invocation) or to design a new investigation skill. It captures
the contract's seven clauses as fill-in decisions, so an unattended run degrades gracefully instead
of stalling or improvising.

## Template

```markdown
# Investigation Brief: [Target]

## The Decision
**This research supports:** [the decision — research without a decision is a hobby]
**Decision deadline:** [when — "just enough" is sized to this]

## Question Budget
**Budget:** [hard cap, usually 3]
**The questions:** [list them — anything answered inline below is already credited]
1. [Question 1]
2. [Question 2]
3. [Question 3]
**Already answered inline:** [what the invocation context already covers — don't re-ask]

## Search Plan (the gate — 3 bullets, shown before researching)
- What will be searched: [targets, topics]
- Source types: [company pages, filings, reviews, press, communities...]
- Fact/inference separation: [facts get URLs; interpretations get labeled Inference; gaps become Assumptions]

## Do-Not-Invent List (this domain's fabrication risks)
- [e.g., competitors, pricing, market share, funding rounds, customer wins, quotes]
- Rule: real, checkable URLs only — a claim without a source and date is an opinion wearing a badge

## Output Contract
**Schema:** [name the stable schema, or paste it — sections numbered, marked "do not reorder"]
**Mode:** Just Enough (Verbose only on request)
**Every key claim labeled:** Fact / Inference / Assumption — what couldn't be found goes in a gaps list, not a fourth label

## Confidence Stacking (for multi-channel findings)
- 1 channel → watch item · 2 channels → working hypothesis · 3+ → actionable · conflict → dig
- Announcements are intent until funding, hiring, procurement, or contracts corroborate

## Final Step Block
[Exactly 4 numbered next options the run will close with. On an unattended run: file the output and stop.]
1. [Option]
2. [Option]
3. [Option]
4. [Option]

## Guardrails check
- All collection is public-record OSINT: published, filed, posted, or observable
- The stage test: comfortable explaining every method at the target's user conference? If not, cut it.
```

## Quality checks before you call it done

- The decision is named — if it isn't, stop and get it; it defines "just enough"
- The do-not-invent list is domain-specific, not generic
- The schema is stable and numbered — a drifted schema silently breaks every future diff
- The Final Step block has exactly 4 options, and the unattended behavior (file and stop) is stated
