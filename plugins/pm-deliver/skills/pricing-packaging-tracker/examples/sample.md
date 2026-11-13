# Pricing & Packaging Tracker — Worked Example

All companies, prices, URLs, and figures are **fictional**. Same scenario as the suite's other
examples: Fieldlight tracking its FSM competitors. This is a **delta-mode** run diffing against a
June 28 baseline capture; it lands in the same fictional month as the `competitive-intel-watch`
example and catches the same Wrenchline move from the pricing-specialist angle — plus a structural
change the broader watch's materiality bar didn't feature.

**Invocation:** `Pricing tracker on Wrenchline, DispatchCrow, Vantiga FSM — prior capture from
June 28 pasted below. [capture]`

---

# Pricing Capture / Delta Report

## 1. Run Header
**Competitor set:** Wrenchline, DispatchCrow, Vantiga FSM
**Prior capture date:** 2026-06-28
**This run date:** 2026-07-31

## 2. Pricing Capture (per competitor)
_Delta mode — captures below only for the two competitors with changes._

### Wrenchline — [pricing page](https://example.com/wrenchline/pricing), as of 2026-07-31
- **Tiers:** Essentials: $79/mo flat (< 25 techs) — **new** · Pro: $59/tech/mo, annual · Suite: $89/tech/mo, annual, 25-tech minimum
- **Key gates:** dispatch board gates at Pro; payroll/inventory/fleet gate at Suite; quoting now included from Essentials up — **new placement**
- **Usage limits:** Essentials hard-caps at 25 technicians
- **Free tier / trial:** 14-day trial, card required (unchanged)
- **Enterprise signals:** "contact sales" above 100 techs (unchanged)

### DispatchCrow — [pricing page](https://example.com/dispatchcrow/pricing), as of 2026-07-31
- **Tiers:** Free (≤5 techs) · Grow: $39/tech/mo · Pro: $69/tech/mo (all unchanged)
- **Key gates:** payments now included at Grow (was Pro) — **moved down**; capacity view listed as "coming to Pro" — **new**
- **Usage limits:** unchanged
- **Free tier / trial:** free tier unchanged
- **Enterprise signals:** none published (unchanged)

## 3. Changes Since Last Capture (Delta Mode)

### Wrenchline — new $79 Essentials tier below the suite
- **Then / Now:** entry point was Pro at $59/tech/mo annual (a 10-tech shop: ~$590/mo) → Essentials $79/mo flat, monthly billing, no dispatch board — **Fact**
- **Evidence:** [pricing page vs. archived capture, Jun 28 vs. Jul 31](https://example.com/archive/wrenchline-pricing)
- **Reading:** a flat-price fighter brand aimed at the self-serve low end — defends against DispatchCrow and us without discounting the suite — **Inference**. The withheld dispatch board is the tell: they're protecting the Pro upgrade path, not serving the segment.

### DispatchCrow — payments gate moved down a tier
- **Then / Now:** payments gated at Pro ($69) → included at Grow ($39) — **Fact**
- **Evidence:** [pricing page vs. archived capture, Jun 28 vs. Jul 31](https://example.com/archive/dispatchcrow-pricing)
- **Reading:** the subscription price didn't move; the *gate* did. They're trading gate revenue for transaction volume — payments take-rate is becoming the business model, with the software as distribution — **Inference**. Their "coming to Pro" capacity-view note also corroborates the watch report's hiring-based inference from the product side.

_Vantiga FSM: no pricing or packaging changes this cycle._

## 4. Signals
- Both movers cut the *effective* entry cost without touching headline per-tech prices — the market is competing on entry friction, not list price — **Inference**
- For our pricing: a $79 flat competitor tier and a $39 payments-included tier now bracket our planned entry point; our quoting module's pricing needs to assume payments revenue arrives later, not at launch — **Inference**
- For the battle card: the Pricing & Packaging Snapshot section is stale as of Jul 24 (Essentials) — already flagged by the watch; this capture supplies the exact then/now rows

### Assumptions to Validate
- Essentials' 25-tech cap is enforced at signup, not negotiable (mystery-shop it)
- DispatchCrow's take-rate economics work at trades transaction sizes (same open question as ours)
- Vantiga's unchanged page reflects strategy, not neglect — their Go tier launched in March and hasn't moved since

---

## Why this example works

- **Structure told the story before numbers did.** Neither mover changed a headline price.
  A new tier and a relocated gate carried the entire strategic signal — exactly the
  "the gate moves first" teaching the skill is built on.
- **The then/now discipline makes claims checkable.** Every change is old → new with an archive
  diff URL and both dates. Next quarter's run diffs against this document with zero archaeology.
- **The quiet competitor got one line.** Vantiga didn't move; the report says so and moves on —
  but the Assumptions section still asks whether that quiet is strategy or neglect.
- **It cooperates with the chain without duplicating it.** The watch report caught Essentials at
  materiality altitude; this capture supplies the row-level detail the battle card's pricing
  section actually pastes in. Two skills, one event, different jobs.
