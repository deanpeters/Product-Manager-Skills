# Competitive Analysis Process Tracker

Copy this to run and track a six-step competitive analysis engagement. The steps are a **menu, not
a mandate** — scope to the decision, record which steps you're running and why, and note what each
step's artifact fed. A step that doesn't feed an output is a detour; an analysis that skips Step 7
never happened, organizationally speaking.

## Template

```markdown
# Competitive Analysis: [Market / Competitor Set]

## Step 0 — Scope
**Decision this analysis supports:** [roadmap bet / positioning refresh / market entry / deal defense]
**Competitor set:** [named, or "TBD — Step 1 will surface it"]
**Steps in scope:** [which of 1-6, and why the others are skipped]
**Existing intelligence to consume:** [prior scans, snapshots, cards — consumed, not repeated]
**Target date:** [when the decision gets made — the analysis is late after this]

## Step 1 — Landscape Overview
**Run:** `market-landscape-scan` | **Status:** [pending / done / skipped because ___]
**Artifact:** [link to the landscape snapshot]
**Decision point resolved:** which 2-4 players get depth: [names + one-line why each]

## Step 2 — Product-Level Comparison
**Run:** `competitive-research-snapshot` | **Status:**
**Artifact:** [link to the snapshot; its comparison matrix is this step's deliverable]
**Kano/Whole-Product/JTBD notes:** [what the capability map exposed that the feature list hid]

## Step 3 — Customer-Need Fulfillment
**Run:** `voice-of-customer-miner` | **Status:**
**Artifact:** [link to the VoC snapshot]
**Promise-delivery gaps spotted:** [marketing checks their reviews say they don't cash — feeds Step 5]

## Step 4 — Business Baseline
**Run:** `company-intel` per deep-dive competitor | **Status:**
**Artifact:** [links, one per competitor]
**Baseline notes:** [revenue streams, channels, org signals worth carrying forward]

## Step 5 — Perception & Relative Positioning
**Run:** contrast Step 2 stated positioning vs. Step 3 customer language; draft with `positioning-statement` | **Status:**
**Artifact:** [positioning statement / perceptual map]
**The uncontested space:** [where nobody's promise lands — the counter-move candidate]

## Step 6 — Strategic Direction
**Run:** forward-looking disciplines (TECHINT/HUMINT/FININT/MASINT), fused; then `competitive-intel-watch` on a cadence | **Status:**
**Artifact:** [direction read per competitor, with confidence stack]
**Committed bets vs. exploration:** [what stacked signals support; single signals stay on the watchlist]

## Step 7 — Outputs
| Output | Built? | Owner / consumer | Fed by steps |
|---|---|---|---|
| Battle card(s) | | sales | 2, 3, 5 |
| Executive comparison matrix | | exec staff | 2 |
| Positioning counter-moves | | PMM | 3, 5 |
| Threat assessment brief | | leadership | 6 |

**Maintenance cadence installed:** [competitive-intel-watch schedule — weekly SIGINT for cards,
quarterly deep pass for direction. If this line is blank, the analysis didn't end; it just stopped.]
```

## Quality checks before you call it done

- Step 0 names the decision and the skipped steps have stated reasons — "we ran everything" is not scoping
- Each completed step links a real artifact produced by the delegated skill
- Step 6 ran or has an explicit skip reason — it's the step whose absence causes launch-day surprise
- Step 7's table has owners, and the watch cadence is installed with a schedule
