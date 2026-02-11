# Facilitation Scope Maintenance

## Why This Exists

Facilitation behavior is shared. If it breaks in one guided skill, it is usually broken everywhere that inherits the same protocol.

Use this file to quickly identify impacted skills and apply repo-wide fixes consistently.

## Canonical Source Of Truth

- `skills/workshop-facilitation/SKILL.md`

Core rule to preserve:
- Regular context/scoring questions should offer quick-select numbered options (include `Other (specify)` when useful).
- Numbered recommendations are for decision points only.

## How To Find Impacted Skills

Run:

```bash
rg -l "workshop-facilitation/SKILL.md" skills/*/SKILL.md | sort
```

This is the authoritative scope query. Do not rely only on static lists.

## Current Scope Snapshot (2026-02-11)

These files currently reference the facilitation source:

- `skills/acquisition-channel-advisor/SKILL.md`
- `skills/ai-shaped-readiness-advisor/SKILL.md`
- `skills/business-health-diagnostic/SKILL.md`
- `skills/context-engineering-advisor/SKILL.md`
- `skills/customer-journey-mapping-workshop/SKILL.md`
- `skills/discovery-interview-prep/SKILL.md`
- `skills/discovery-process/SKILL.md`
- `skills/epic-breakdown-advisor/SKILL.md`
- `skills/feature-investment-advisor/SKILL.md`
- `skills/finance-based-pricing-advisor/SKILL.md`
- `skills/lean-ux-canvas/SKILL.md`
- `skills/opportunity-solution-tree/SKILL.md`
- `skills/pol-probe-advisor/SKILL.md`
- `skills/positioning-workshop/SKILL.md`
- `skills/prd-development/SKILL.md`
- `skills/prioritization-advisor/SKILL.md`
- `skills/problem-framing-canvas/SKILL.md`
- `skills/product-strategy-session/SKILL.md`
- `skills/roadmap-planning/SKILL.md`
- `skills/skill-authoring-workflow/SKILL.md`
- `skills/tam-sam-som-calculator/SKILL.md`
- `skills/user-story-mapping-workshop/SKILL.md`

## Update Checklist

1. Edit `skills/workshop-facilitation/SKILL.md` first.
2. Run the scope query and patch affected skills when local wording may drift.
3. Sanity-check for contradictory language:

```bash
rg -n "numbered recommendations each turn|numbered recommendations at decision points" skills/*/SKILL.md
```

4. Run conformance checks on changed skills:

```bash
python3 scripts/check-skill-metadata.py <changed-skill-paths...>
```

