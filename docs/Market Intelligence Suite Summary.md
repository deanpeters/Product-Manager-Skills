# Market Intelligence Suite Summary

**14 Skills + 2 Upgrades for Competitive & Market Research**

**Release Date:** July 17, 2026
**Suite Version:** 1.0 (repo v0.83)
**Total Skills:** 14 new (1 Component + 1 Interactive + 12 Workflow) + 2 upgraded
**Theme tag:** `market-intelligence`
**Release note:** [v0.83 announcement](announcements/2026-07-17-v0-83-market-intelligence-suite.md)

---

## Overview

The Market Intelligence Suite turns competitive and market research from a term paper into an
operating capability. Instead of a heroic annual deck of unlabeled inference, you get the
intelligence community's approach: **independent collection disciplines** that fail differently,
**explicit evidence labels** (Fact / Inference / Assumption) on every claim, **confidence that
escalates only as channels corroborate**, and **a cadence instead of a one-off**.

Every skill teaches the tradecraft while doing the work — the human PM should finish a run knowing
more about evidence discipline than when they started.

**What's included:**
- **Protocol layer:** the contract that makes AI research trustworthy and schedulable
- **Discipline layer:** eight collection channels with sources and signal → inference chains
- **Triage layer:** an advisor that routes your question to the right discipline mix
- **Investigation layer:** the four-skill chain plus evidence-cited strategy frameworks
- **Monitoring layer:** delta monitors that report change, not state
- **Orchestration layer:** the six-step umbrella process

**What's NOT included:**
- Pricing *strategy* (that's `finance-based-pricing-advisor`; the tracker here reads the market, it doesn't set your price)
- Discovery interviews (the suite's outputs *feed* discovery — see the VoC miner's mandatory validation handoff)
- Anything non-public: every source in the suite is published, filed, posted, or publicly observable (SCIP-grounded guardrails throughout)

---

## Suite Architecture

### Protocol Layer

[`autonomous-investigation`](../skills/autonomous-investigation/SKILL.md) (Workflow) — the
counterpart to `workshop-facilitation` for skills where the *world* holds the context instead of
you. Seven clauses every investigation skill honors: question budget, search-plan gate,
Fact/Inference/Assumption labels, do-not-invent lists, Just Enough Mode, stable diffable schemas,
and a 4-option Final Step. Because runs degrade gracefully when nobody answers, they can execute
as agent tasks, in loops, or on schedules — then diff this quarter against last.

### Discipline Layer

[`intelligence-collection-disciplines`](../skills/intelligence-collection-disciplines/SKILL.md)
(Component) — eight channels, each with free/paid source tables, signal → inference chains, and
the PM artifact it feeds:

| Discipline | Plain English | Primary PM Artifact |
|---|---|---|
| OSINT | Press, social, analysts, reviews | Battle cards, positioning |
| FININT | Filings, earnings calls, procurement | Battle cards, SOM capture rates |
| GEOINT/DEMOINT | Census, labor, trade statistics | TAM/SAM/SOM, ICPs, personas |
| TECHINT | Patents, technographics, changelogs | Roadmap bets |
| HUMINT | Talent moves, employee chatter, win/loss | Roadmap bets, battle cards |
| SIGINT | Web diffs, pricing changes, job posts | Battle cards, pricing strategy |
| MASINT | Supply chain, ops indicators | Threat assessment |
| All-Source Fusion | Cross-validation + confidence stacking | Everything above |

The Confidence Stacking Rule: 1 discipline flags = watch item; 2 = working hypothesis;
3+ = actionable intelligence; conflict = someone is bluffing — dig.

### Triage Layer

[`intel-discipline-advisor`](../skills/intel-discipline-advisor/SKILL.md) (Interactive) — the
pedagogic pairing for the compendium. Three adaptive questions about the decision on your desk,
then numbered recommendations naming discipline mix → cadence → executing skill → artifact fed.
Teaches the mapping as it routes; includes the honest off-ramp when your question belongs to
discovery or win/loss, not a public-web sweep.

### Investigation Layer

**The chain** — four Workflow skills, each consuming the prior's stable schema:

```
market-landscape-scan          who plays, how buyers segment, whitespace vs. dead zones
        ↓
competitive-research-snapshot  cited depth on the 2-4 players that matter
        ↓
competitive-intel-watch        scheduled delta monitor — material shifts only
        ↓
battle-card-builder            field-action card, every claim sourced and labeled
```

**Evidence-cited strategy frameworks** (same protocol, classic frames):
- [`swot-analysis`](../skills/swot-analysis/SKILL.md) — labeled quadrants + the S-O/W-T crossings most SWOTs skip
- [`porters-five-forces`](../skills/porters-five-forces/SKILL.md) — rated forces with signals; AI substitution named; closes at the profit pool
- [`ansoff-matrix`](../skills/ansoff-matrix/SKILL.md) — growth options with evidence per quadrant and a risk gradient that makes diversification carry its burden

### Monitoring Layer

- [`competitive-intel-watch`](../skills/competitive-intel-watch/SKILL.md) — competitor-level; "no material shifts" is a first-class result
- [`pricing-packaging-tracker`](../skills/pricing-packaging-tracker/SKILL.md) — pricing as a diffable time series; the gate moves before the price does
- [`pestel-delta-monitor`](../skills/pestel-delta-monitor/SKILL.md) — macro-level, pairs with `pestel-analysis`; broken assumptions are the real output
- [`voice-of-customer-miner`](../skills/voice-of-customer-miner/SKILL.md) — public-voice mining with verbatims, source-bias notes, and a mandatory handoff to real interviews

### Orchestration Layer

[`competitive-analysis-process`](../skills/competitive-analysis-process/SKILL.md) (Workflow) — the
six-step umbrella: landscape → product comparison → customer-need fulfillment → business baseline →
perception/positioning → strategic direction, each step naming its frameworks (Porter, Kano, ODI,
Ries & Trout, Hamel & Prahalad) and delegating to the right suite skill. Step 6 — where they're
*going* — is the one most teams skip, which is why they're perpetually surprised.

### Upgraded Skills

- [`tam-sam-som-calculator`](../skills/tam-sam-som-calculator/SKILL.md) — three entry modes: own
  numbers, guided interview, or autonomous bottom-up research (establishment counts × benchmarks,
  SOM capture rates from competitor filings). Bottom-up wins scrutiny because a skeptical CFO can
  attack one assumption at a time.
- [`company-intel`](../skills/company-intel/SKILL.md) — Executive Signal Refresh rerun pattern:
  Then/Now diffs with exact quotes, and **Dropped Language** — what leaders *stop* saying is often
  the strongest signal.

---

## Which Skill Do I Run?

| Your situation | Run |
|---|---|
| "I don't know where to start" | `intel-discipline-advisor` |
| New market, entry or re-positioning decision | `market-landscape-scan` |
| Need cited depth on specific competitors | `competitive-research-snapshot` |
| Keep research current without redoing it | `competitive-intel-watch` (or `pricing-packaging-tracker` for pricing) |
| Sales keeps losing to one rival | `battle-card-builder` |
| What are their customers angry about? | `voice-of-customer-miner` |
| One company's position, evidence-cited | `swot-analysis` (or `company-intel` for the full deep dive) |
| Why are margins eroding? / should we enter? | `porters-five-forces` |
| Where does the next tranche of growth come from? | `ansoff-matrix` |
| Which macro assumptions broke this quarter? | `pestel-delta-monitor` |
| How big is the market, defensibly? | `tam-sam-som-calculator` |
| The full picture, new strategy cycle | `competitive-analysis-process` |

## The Worked-Example Universe

All suite skills ship a `template.md` (the diffable schema as a copy/paste fill-in) and a worked
example in `examples/`. The examples share one fictional market — **Fieldlight**, a scheduling
tool for trades businesses, versus **Wrenchline**, **DispatchCrow**, and **Vantiga FSM** — and the
chain examples literally feed each other: the scan names the players, the snapshot analyzes them,
the watch diffs the snapshot, and the battle card rebuilds from the watch's update flags. Read
them in order to see the diffable-schema contract working end to end. (All names fictional, per
the repo's anonymization protocol.)

## Getting the Suite

- **One pack:** [`pm-determine-pack.zip`](https://github.com/deanpeters/Product-Manager-Skills/releases/latest/download/pm-determine-pack.zip) — the Determine bundle holds the whole suite (its Detect motion) plus the two upgraded skills
- **Browse individually:** the [`dist/`](https://github.com/deanpeters/Product-Manager-Skills/tree/main/dist) download shelf
- **Claude Code:** the plugin marketplace carries the `market-intelligence` category

## Sources & Credits

Adapted from practitioner experience in competitive and market intelligence, and the
`market-intelligence/` prompt collection in the companion
[product-manager-prompts](https://github.com/deanpeters/product-manager-prompts) repo. External
frameworks credited in each skill: Porter (1979), Ansoff (1957), Kano, Ulwick, Osterwalder &
Pigneur, Ries & Trout, Hamel & Prahalad. Guardrails follow the SCIP Code of Ethics.
