# PESTEL Delta Report Template

Copy this for each quarterly re-scan. This monitor **requires a baseline** — a prior
`pestel-analysis` output to diff against; never diff across a scope change. Report material
movement only: regulation passed or credibly proposed, thresholds crossed, technology matured with
adoption evidence. **Broken assumptions are the real output** — one baseline entry now contradicted
by evidence outranks ten new observations, because strategy was built on it.

Real URLs and dates on everything — invented regulation is this domain's signature fabrication risk.

## Template

```markdown
# PESTEL Delta Report

## 1. Run Header
**Scope (from prior analysis):** [copy it — if scope changed, run a fresh pestel-analysis instead]
**Prior analysis date:** [YYYY-MM-DD]
**This run date:** [YYYY-MM-DD]

## 2. Factor-by-Factor Delta
_Keep "no material movement" factors to a single line each — the discipline is the product._

### Political: [moved / no material movement]
- **What moved:** [1-2 bullets, labeled, cited — only if moved]
- **Prior assumption affected:** [which entry from the baseline]
- **Reading:** [Inference — implication for the product scope]

### Economic: [moved / no material movement]
[same structure]

### Social: [moved / no material movement]
[same structure]

### Technological: [moved / no material movement]
[same structure]

### Environmental: [moved / no material movement]
[same structure]

### Legal: [moved / no material movement]
[same structure]

## 3. Broken Assumptions
- [Baseline entries now contradicted by evidence — the run's most important section; cited]

## 4. New to the Frame
- [Factors absent from the baseline that now warrant a slot]

## 5. So What?
- **Implications for strategy or roadmap:** [exactly 3 — label, confidence, URL where relevant]
- **Factors to watch closely next cycle:** [exactly 2]
- **Assumptions to validate:** [exactly 3]
```

## Quality checks before you call it done

- Every "moved" claim carries a real URL and date — regulations especially
- Each delta names the baseline entry it affects — a delta with no "prior assumption affected" line isn't actionable
- Quiet factors got one line, not a rewrite; a half-page report on a quiet quarter is the radar working
- Baseline entries that never move and touch no decision are flagged as furniture for retirement at the next baseline refresh
