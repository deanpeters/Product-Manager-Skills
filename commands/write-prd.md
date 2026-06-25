---
name: write-prd
description: Create a decision-ready PRD by chaining problem framing, requirements definition, and story scaffolding.
argument-hint: "<feature, initiative, or product change>"
uses:
  - prd-development
  - problem-statement
  - proto-persona
  - user-story
  - user-story-splitting
outputs:
  - Structured PRD
  - Core personas and requirements
  - Initial implementation-ready stories
---

# /write-prd

Generate a PRD that moves smoothly from strategy to delivery.

## Invocation

```text
/write-prd Team inbox redesign for faster triage in customer support
```

## Workflow

1. Define the problem context with `problem-statement`.
2. Align user assumptions with `proto-persona`.
3. Build the full document using `prd-development`.
4. Draft initial stories with `user-story`.
5. Split larger items with `user-story-splitting`.

## Checkpoints

- Validate scope boundaries before writing requirements.
- Keep success criteria measurable and tied to outcome metrics.
- Ensure at least one anti-pattern is called out in risks.
- Tag every gap inline: 🔶 **Assumption** (plausible but unvalidated) or 🔵 **Open Question** (needs discovery).
- After each section, review the "Before moving on" cross-section prompt in the template before continuing.
- After the final section, complete the **Self-Assessment**: strongest section, weakest section, top assumptions to validate, and recommended next step.

## Next Steps

- Run `/plan-roadmap` to sequence delivery.
- Run `/prioritize` if scope exceeds current capacity.
