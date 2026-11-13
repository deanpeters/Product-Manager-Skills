# PESTEL Delta Monitor — Worked Example (Industrial)

All companies, regulations, URLs, and figures are **fictional**. Industrial sibling of
[`sample.md`](sample.md): Northfield Automation's quarterly macro re-scan. Industrial PESTEL runs
hotter than SaaS in exactly the factors the SaaS sibling reported quiet — tariffs, energy,
physical-safety regulation — which is the pedagogic reason this sibling exists.

**Invocation:** `PESTEL delta against the attached August analysis — scope is North American
retrofit automation for mid-size manufacturers; I suspect the tariff schedule change matters.
[baseline attached]`

---

# PESTEL Delta Report

## 1. Run Header
**Scope (from prior analysis):** North American retrofit automation; mid-size discrete manufacturers
**Prior analysis date:** 2026-08-20
**This run date:** 2026-11-20

## 2. Factor-by-Factor Delta

### Political: moved
- **What moved:** the tariff schedule for imported industrial sensors and PLC-interface components was revised upward, effective January 2027 — **Fact** ([tariff schedule notice, Nov 2026](https://example.com/tariffs/notice))
- **Prior assumption affected:** P1 assumed component tariffs stable through 2027, which underpinned the hardware-partner cost model
- **Reading:** hardware-inclusive retrofit offers get more expensive relative to software-led ones — the software-led strategy gains a tailwind nobody planned for — **Inference**

### Economic: moved
- **What moved:** industrial electricity prices crossed the baseline's E3 threshold in two target regions — **Fact** ([energy price data](https://example.com/eia/industrial-rates))
- **Prior assumption affected:** E3 marked the price point where energy-monitoring features shift from nice-to-have to CFO-priority
- **Reading:** energy-consumption dashboards move up the feature priority list; sales narrative gains a payback story — **Inference**

### Social: no material movement
One line: skilled-maintenance-technician shortage persists at baseline severity; no threshold crossed.

### Technological: no material movement
One line: AI-over-historian pilots still trade-press chatter, nothing productized (the five-forces watch item — unchanged).

### Environmental: moved
- **What moved:** two states finalized reporting rules requiring energy-intensity disclosures from manufacturers above a size threshold that includes the top of our segment — **Fact** ([state register entries, Oct 2026](https://example.com/regs/energy-disclosure))
- **Prior assumption affected:** Env1 had this as "proposed, watch" — it graduated
- **Reading:** monitoring data becomes compliance data for the affected plants — a second regulatory tailwind for the documentation-automation product line — **Inference**

### Legal: no material movement
One line: machinery-safety documentation rules unchanged since the baseline logged them (already in the roadmap).

## 3. Broken Assumptions
- **P1 (stable component tariffs):** broken — the hardware-partner cost model needs a January 2027 rebuild, and partner pricing conversations should start now.
- *(E3 and Env1 are threshold crossings the baseline anticipated — the radar working as designed, not assumptions breaking.)*

## 4. New to the Frame
- **Trade-policy volatility as a standing factor** — the baseline treated tariffs as a single static entry; one revision in a quarter suggests a volatility watch, not a point estimate.

## 5. So What?
- **Implications for strategy or roadmap:**
  1. Software-led entry just got a cost tailwind vs. hardware-heavy rivals — quantify it into the battle card's pricing section — **Inference**, confidence: high
  2. Energy dashboards + disclosure reporting = one feature answering two new pressures (E3, Env1) — candidate for the next roadmap slot — **Inference**, confidence: medium
  3. Hardware-partner agreements need tariff-adjustment clauses before January — **Fact**-driven, confidence: high
- **Factors to watch closely next cycle:** further tariff-schedule revisions; the AI-over-historian substitute (still quiet, still the strategic wildcard)
- **Assumptions to validate:**
  1. Partners will absorb or share tariff costs rather than pass them through whole
  2. Disclosure-rule plant threshold actually captures our segment's top tier (legal read of the size definitions)
  3. Energy-price threshold E3 predicts buying behavior, not just CFO attention

---

## Why this example works

- **The hot factors swapped.** The SaaS sibling moved on lending rates, platform APIs, and
  contractor law; this one moves on tariffs, energy prices, and disclosure rules — with Social
  and Technological quiet. Running both siblings against each other teaches what "PESTEL depends
  on your physics" means in practice.
- **Threshold crossings vs. broken assumptions are distinguished.** E3 and Env1 crossed lines the
  baseline *predicted* — that's the radar working. P1 was contradicted — that's an assumption
  breaking. The report refuses to blur the two, because only one of them means the baseline was
  wrong.
- **Two deltas converge on one roadmap item** (energy dashboards serving both an economic and an
  environmental pressure) — macro monitoring earning a product decision, which is the only reason
  to run it.
- **New-to-the-frame upgraded a point estimate to a volatility watch** — the meta-lesson that a
  factor's *stability* is itself an assumption the diff can break.
