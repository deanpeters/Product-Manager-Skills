---
name: competitive-research-snapshot
argument-hint: "[company/product/segment, and the decision it supports]"
description: "Research a competitive landscape with cited snapshots, a comparison matrix, and so-what implications. Use when a product decision needs competitive grounding, not a market report."
intent: >-
  Autonomous competitive research as a workflow: search plan, competitor selection, just-enough
  research, Fact/Inference/Assumption labels, real URL citations, and next-step options — producing a
  stable snapshot schema that battle cards and delta monitors consume and diff.
type: workflow
theme: market-intelligence
best_for:
  - "Grounding a positioning, roadmap, or deal-support decision in cited competitive evidence"
  - "Creating the baseline snapshot that the competitive intel watch diffs against"
  - "Board or exec prep that needs labeled facts instead of confident storytelling"
scenarios:
  - "We're rewriting our positioning next sprint — get me a cited read on our top three competitors"
  - "Sales keeps losing to one rival; I need evidence on where they're actually strong and weak"
estimated_time: "20-40 min per run"
---

# Competitive Research Snapshot

## Purpose

Research a company's competitive landscape using a workflow, not a one-shot answer: **search plan →
competitor selection → just-enough research → fact/inference labels → real URL citations → next-step
options.** The output is a decision-support snapshot, not a market report — and because its schema is
stable, downstream skills (battle cards, delta monitors) can consume it and diff it. Because it
proceeds on labeled assumptions when questions go unanswered, it can run as an agent task or on a
schedule; re-run it and diff against the prior snapshot.

## Input

**Works best with:** the company, product, or segment to research, and **the decision this research
should support** (positioning, roadmap bet, deal support, board prep) — the decision determines what
"just enough" means.
**Also useful:** known competitors (or explicit permission to identify them), and any prior snapshot
or `market-landscape-scan` output in session — the skill builds on evidence already gathered rather
than re-researching it.

Input supplied inline with the invocation — text after the skill name, a pasted context dump, or an
appended `ARGUMENTS:` line — counts as answers already given. Use it against the question budget;
don't re-ask.

**Arriving empty-handed? That works too.** The skill opens with at most 3 questions (subject,
decision, competitors) and proceeds on labeled assumptions if they go unanswered.

**Example invocation:** `Competitive research snapshot on our expense-automation product — decision:
which roadmap bet wins Q1. Competitors: [Competitor A], [Competitor B]; find a third if one matters.`

## Key Concepts

- **Governing protocol:** honors the [`autonomous-investigation`](../autonomous-investigation/SKILL.md)
  contract in full — question budget of 3, search-plan gate, Fact/Inference/Assumption labels, Just
  Enough Mode, stable schema, 4-option Final Step.
- **Discipline mix:** OSINT (press, reviews, analyst coverage) + FININT (filings, earnings language)
  + SIGINT (pricing pages, site changes) — see
  [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md).
- **Decision-support snapshot, not market report.** Every section earns its place by serving the
  decision named in Scope. Research value is decision support, not page count.
- **Snapshot as baseline.** The schema is a contract with future runs: `competitive-intel-watch`
  diffs the world against this document. Section order never changes.
- **Three or four competitors, not eight.** Depth on the players who matter beats coverage of players
  who don't. Use provided competitors; if none, identify the top 3 (4 only if clearly needed), each
  with name, why relevant, source URL, and confidence.
- **Do-not-invent list (this domain's fabrication risks):** competitors, features, pricing, market
  share, customer wins, roadmap items, product claims.
- **When NOT to use:** you need market *sizing* → [`tam-sam-som-calculator`](../tam-sam-som-calculator/SKILL.md);
  you need deep intel on *one* company's strategy and executives →
  [`company-research`](../company-research/SKILL.md) / [`company-intel`](../company-intel/SKILL.md);
  the facts are already gathered → go straight to the battle card.

## Application

1. **Credit inline context**, then ask only the unanswered questions (max 3):
   1. What company/product/segment?
   2. What decision should this support?
   3. Known competitors, or should I identify them?
   If unanswered, proceed with labeled assumptions.
2. **Show the 3-bullet search plan** — what you'll search, source types, how facts will be separated
   from inference. Continue unless revised.
3. **Select competitors** — provided ones, or top 3 identified (4 only if clearly needed). For each:
   name; why relevant; source URL; confidence.
4. **Research in Just Enough Mode** with mixed sources: company sites, product/pricing pages,
   customer stories, press releases, investor materials, credible news, analyst/review sites.
5. **Emit the schema below exactly** — it is a stable schema for diffing runs over time.

### Output schema (do not reorder)

~~~markdown
# Competitive Research Snapshot

## 1. Scope
**Company/product:** | **Category:** | **Decision supported:** | **Competitors analyzed:**

## 2. Competitor Snapshots
For each competitor, max 5 bullets:
### Competitor: [Name]
- **Positioning:**
- **Relevant capability:**
- **Likely strength:**
- **Likely weakness:**
- **Key source URL:**

## 3. Quick Comparison
| Dimension | Company | Comp 1 | Comp 2 | Comp 3 |
|---|---|---|---|---|
| Target customer | | | | |
| Core use case | | | | |
| Main strength | | | | |
| Main weakness | | | | |
| Evidence quality | | | | |

## 4. So What?
- **3** product strategy implications
- **2** competitive risks
- **2** product opportunities
- **3** assumptions to validate
Each bullet: label, confidence, source URL where relevant.
~~~

A copy/paste fill-in version of this schema, with quality checks, lives in [`template.md`](template.md).

### Final Step (offer exactly 4 options)

1. Competitive battle card ([`battle-card-builder`](../battle-card-builder/SKILL.md))
2. Executive comparison matrix
3. Product risks/opportunities for the next 2 quarters
4. Discovery questions to validate the assumptions

Accept `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`, or a custom path.

## Examples

**A competitor snapshot with honest labels (fictional):**

> ### Competitor: Ledgerline
> - **Positioning:** "finance automation for mid-market CFOs" — **Fact** ([homepage, Jul 2026](https://example.com))
> - **Relevant capability:** approval-chain builder shipped in May — **Fact** ([release notes](https://example.com/changelog))
> - **Likely strength:** ERP integrations; 40+ listed, reviewers confirm the top 5 work well — **Fact** ([G2 reviews](https://example.com/reviews))
> - **Likely weakness:** implementation time; complaint cluster across 11 reviews since March — **Inference** (review mining; no benchmark data)
> - **Key source URL:** [pricing page](https://example.com/pricing)

**The "Evidence quality" row doing its job:** the comparison matrix rates Comp 3's column *low* —
every claim traces to their own marketing. The So What section then refuses to list Comp 3 as a
primary risk: "insufficient independent evidence — **Assumption to validate** via customer
references." That row exists so weak columns can't masquerade as strong ones.

See [`examples/sample.md`](examples/sample.md) for a complete worked snapshot (fictional
FSM-software market) that consumes the `market-landscape-scan` example and becomes the baseline the
`competitive-intel-watch` example diffs against. [`examples/sample-industrial.md`](examples/sample-industrial.md)
shows the same schema on an industrial evidence diet — filings, registries, and honest
absence-of-evidence.

## Common Pitfalls

- **The market-report trap.** Twenty pages on industry trends nobody asked for. If a section doesn't
  serve the decision in Scope, it's padding — Just Enough Mode is the contract.
- **Marketing-page credulity.** A competitor's claimed capabilities recorded as facts. Their site is
  a Fact about *what they claim*; whether it works is review-site territory or an Inference, labeled.
- **Coverage over depth.** Eight competitors with two facts each. Select three that matter and go
  deep — the comparison matrix should be full, not wide.
- **Unlabeled So What.** Implications stated with borrowed confidence. The label and confidence on
  each So What bullet is what makes it usable in a roadmap argument.
- **Regenerating instead of diffing.** Re-running this skill weekly and re-reading the whole output
  is theater — that's what [`competitive-intel-watch`](../competitive-intel-watch/SKILL.md) is for.

## References

- [`autonomous-investigation`](../autonomous-investigation/SKILL.md) (Workflow) — the governing protocol
- [`intelligence-collection-disciplines`](../intelligence-collection-disciplines/SKILL.md) (Component) — discipline sources and signal chains
- [`market-landscape-scan`](../market-landscape-scan/SKILL.md) (Workflow) — upstream: surfaces which players deserve this snapshot
- [`competitive-intel-watch`](../competitive-intel-watch/SKILL.md) (Workflow) — downstream: diffs future runs against this baseline
- [`battle-card-builder`](../battle-card-builder/SKILL.md) (Workflow) — downstream: turns the snapshot into a field-action card
- [`company-research`](../company-research/SKILL.md), [`company-intel`](../company-intel/SKILL.md) — single-company deep dives
- Adapted from `market-intelligence/competitive-research-snapshot-prompt.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
