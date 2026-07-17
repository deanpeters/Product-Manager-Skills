---
name: autonomous-investigation
description: "The protocol behind every investigation skill. Use when AI research must proceed without you: search-plan gate, Fact/Inference/Assumption labels, confidence stacking, diffable outputs."
intent: >-
  Provide the canonical contract for autonomous research skills: a bounded question budget, a search-plan
  gate, three-level evidence labeling, do-not-invent lists, just-enough output, stable diffable schemas,
  and confidence stacking — so investigations are trustworthy, schedulable, and comparable run over run.
type: workflow
theme: market-intelligence
best_for:
  - "Defining consistent behavior for research skills that run as agent tasks or on schedules"
  - "Keeping AI research honest: labeled evidence, real citations, no invented facts"
  - "Making run N and run N+1 diffable so delta monitoring is possible"
scenarios:
  - "Set up a competitive scan that can re-run quarterly without me babysitting it"
  - "I want research output where I can tell facts from the AI's guesses"
estimated_time: "protocol reference; investigations vary (15-45 min per run)"
---

# Autonomous Investigation Protocol

## Purpose

Provide the canonical contract for **investigation skills** — research the AI performs in the world (web
search, published data, public filings) while you review the evidence instead of feeding it context.
Where `workshop-facilitation` governs skills that ask you questions one at a time, this protocol governs
skills that *proceed without you*: they budget their questions, show their plan, label every claim, and
produce output stable enough to diff against last quarter's run. That last property is the payoff — an
investigation honoring this contract can run as an agent task, in a loop, or on a schedule.

## Input

**Nothing required** — this skill defines the protocol other investigation skills follow.
**Also useful when invoked standalone:** the target of the investigation and, above all, **the decision
the research should support**. Research without a decision is a hobby; every investigation skill asks
for the decision because it determines what "just enough" means.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as answers already given. Use it, credit it against the question
budget, and don't re-ask.

**Arriving empty-handed? That works too.** The protocol's whole design is to proceed on best-available
evidence with labeled assumptions when nobody answers questions. When another skill references this
protocol, that skill's Input section governs what to provide.

**Example invocation:** `Run an autonomous investigation on [TARGET]'s move into workflow automation —
this supports our Q3 roadmap bet on the same space.`

## Key Concepts

### Two protocols, two jobs

| | `workshop-facilitation` | `autonomous-investigation` |
|---|---|---|
| Who holds the context | The user | The world (public sources) |
| Interaction shape | One question per turn | Question budget, then proceed |
| Blocked by silence? | Yes — waits for answers | No — labels assumptions and continues |
| Schedulable? | No | Yes — that's the point |

### The contract

Every investigation skill honors all seven clauses. They are not a menu.

1. **Question budget** — a hard cap (usually 3) on clarifying questions. When the budget is spent or
   nobody answers, proceed with labeled assumptions. This is what makes investigations schedulable:
   an unattended run degrades gracefully instead of stalling.

2. **Search-plan gate** — before researching, show a 3-bullet plan: what you'll search, which source
   types, how you'll separate fact from inference. Continue unless the user revises it. *Why it
   teaches:* reviewing a plan takes 10 seconds; reviewing a wrong report takes 10 minutes. The gate is
   the cheapest correction point in the whole workflow.

3. **Evidence labels** — every key claim carries exactly one label:
   - **Fact** — source-supported; a checkable URL sits next to it
   - **Inference** — evidence-based interpretation; the evidence is cited, the leap is yours to judge
   - **Assumption** — working guess made to keep moving; listed for validation
   Keep labels short. Things you *couldn't find* are not a fourth label — they go in an explicit gaps
   list. *Why it teaches:* most competitive "facts" in strategy decks are unlabeled inference. Three-level
   honesty is the habit that separates intelligence from confident storytelling.

4. **Do-not-invent list** — each investigation skill names its domain's specific fabrication risks
   (competitors, pricing, market share, patent contents, customer wins...) and forbids inventing them.
   Real, checkable URLs only; a claim without a source and date is an opinion wearing a badge.
   *Why it teaches:* the list tells the human exactly what to verify first.

5. **Just Enough Mode** — default output is the strongest findings in short bullets, sized to the
   decision. Verbose Mode exists only on request. Research value is decision support, not page count.

6. **Stable output schema** — section order and structure never drift between runs, so run N and
   run N+1 are diffable. Delta monitoring, scheduled refreshes, and "what changed since last quarter"
   all depend on this clause.

7. **Final Step block** — end with exactly 4 numbered next options (artifacts to build, deeper passes
   to run, assumptions to validate). Accept `1`, `1 and 3`, `Verbose Mode`, or a custom path.

### The Confidence Stacking Rule

Labels grade individual claims; stacking grades the *story*. When signals arrive from independent
collection channels (see `intelligence-collection-disciplines`):

~~~
1 channel flags it   → Watch item. Log it, do nothing.
2 channels agree     → Working hypothesis. Assign someone to probe.
3+ channels agree    → Actionable intelligence. Brief leadership, adjust plans.
Channels conflict    → The most interesting case. Someone is bluffing. Dig.
~~~

One corollary that generalizes everywhere: **treat announcements as intent until funding, procurement,
hiring, or contracts corroborate them.** Ambition shows up in press releases; commitment shows up in
filings, job posts, and purchase orders.

### Guardrails

All collection under this protocol is legal, ethical, open-source work:

- **Yes:** anything published, filed, posted, or observable in public.
- **No:** pretexting (lying about who you are), soliciting NDA-protected information, hiring someone
  specifically to extract a former employer's secrets, scraping in violation of terms you accepted.

The rule of thumb, borrowed from the competitive-intelligence profession (SCIP Code of Ethics): **if
you'd be uncomfortable explaining your method on stage at the target's user conference, don't use the
method.**

## Application

### For skills implementing this protocol

1. Declare this skill in References as the governing protocol.
2. State the skill's question budget (default 3) and the questions themselves.
3. Define the domain's do-not-invent list — name the specific things AI fabricates in this territory.
4. Define the stable output schema with numbered sections; mark it "do not reorder."
5. End the schema with a Final Step block of exactly 4 options.

### For agents running an investigation

1. Read inline invocation context first; credit it against the question budget.
2. Ask only unanswered budget questions. If silence, proceed — label every gap-filling guess
   **Assumption**.
3. Show the 3-bullet search plan. Continue unless revised.
4. Research in Just Enough Mode: mixed source types, real URLs captured with dates.
5. Label every key claim **Fact / Inference / Assumption**. Put what you couldn't find in a gaps list.
6. Apply confidence stacking when multiple channels speak to the same move; report the stack level,
   not just the signals.
7. Emit the skill's schema exactly — same sections, same order — so this run diffs against the last.
8. Close with the Final Step block. If the user picks a number, execute; if they answer nothing (a
   scheduled run), file the output and stop.

## Examples

**Opening of a protocol-honoring run (user gave target + decision inline, so no questions spent):**

> **Search plan** (say "revise" to change it):
> - Search [TARGET]'s pricing pages, release notes, and last two earnings transcripts
> - Source mix: company site, filings, credible press, review sites
> - Facts get URLs; interpretations get labeled Inference; gaps become Assumptions to validate
>
> *(research happens)*
>
> **Key finding:** [TARGET] removed its mid-tier plan in May — **Fact**
> ([pricing page diff, May 12](https://example.com/archive)). Packaging is consolidating toward
> enterprise — **Inference** (tier removal + two enterprise-only features shipped since April).
> They will raise the entry price within two quarters — **Assumption** (pattern-based; validate
> against their next pricing-page change).
>
> **Final Step — reply 1, 2, 3, 4, a combination, or "Verbose Mode":**
> 1. Build the battle card from these findings
> 2. Executive comparison matrix
> 3. Risks/opportunities for the next 2 quarters
> 4. Discovery questions to validate the assumptions

**A scheduled run with no human present:** the same skill runs quarterly from a saved invocation. The
question budget is already spent (zero questions — context was inline), the plan gate auto-continues,
and the output diffs cleanly against last quarter because the schema didn't move. The delta — not the
report — is what the team reads.

## Common Pitfalls

- **Report theater.** Twenty pages signal effort, not intelligence. If the decision fits on one page of
  labeled findings, twenty pages is a defect. Just Enough Mode is the contract, not a suggestion.
- **Unlabeled inference.** "Competitor X is pivoting to AI" stated as fact when it's an interpretation
  of two job posts. The label isn't decoration — it tells the reader what to check before betting on it.
- **Invented citations.** A URL that doesn't resolve, a quote that doesn't exist. The do-not-invent list
  names the domain's temptations; honor it or the whole output is suspect.
- **Skipping the plan gate.** Ten minutes of research in the wrong direction costs more than ten seconds
  of plan review. The gate exists because redirecting a plan is cheap and redirecting a report is not.
- **Announcement inflation.** Treating a press release as a commitment. Announcements are intent;
  corroborate with money, hiring, or contracts before you re-plan around them.
- **Schema drift.** "Improving" the output structure between runs quietly destroys diffability — the
  delta monitor downstream now compares apples to a reorganized orchard.
- **Single-source certainty.** One signal is an anecdote. Escalate confidence only as independent
  channels agree — that's the stacking rule doing its job.

## References

- [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) (Component) —
  the eight collection channels whose signals this protocol labels and stacks
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md) (Interactive) — the sibling protocol for
  skills where the *user* holds the context
- Investigation skills honoring this contract: `market-landscape-scan`, `competitive-research-snapshot`,
  `competitive-intel-watch`, `battle-card-builder` (References section of each names this protocol)
- SCIP Code of Ethics — the competitive-intelligence profession's reference standard
- Adapted from the market-intelligence investigation contract in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
