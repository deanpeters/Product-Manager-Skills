# Skill Authoring Example

A real build from this repository: `lifecycle-play-advisor`, the Interactive skill that diagnoses
whether a fading product should be extended, replaced, or retired.

**Why this one:** it shows the Preflight phase doing the work it exists to do — nearly stopping the
build — and it shows the Component + Interactive pairing decision that this repo prefers over one
large skill.

---

## Phase 1 — Preflight

```bash
./scripts/find-a-skill.sh --mode trigger "product lifecycle decline extend replace"
# -> No matching skills found
```

Then a wider check, because "no matches" often means the query was wrong rather than the gap real:

```bash
grep -rl "Product Life Cycle\|product lifecycle\|PLC" skills/*/SKILL.md
# -> company-intel, eol-readiness-advisor, eol-process  (references only, no PLC skill)
```

**Overlap found:** `organic-growth-advisor` and `ansoff-matrix` both cover growth options.

**Why not extend one of those?** They ask *where does growth come from.* This asks *what do we do
with this specific product at the decline inflection.* Different question, different entry point,
different user state. The honest boundary: when the answer here is "extend," it hands off to
`organic-growth-advisor` for which growth path the variant serves.

**Type decision:** the source material contained both a framework (PLC grid, three plays, seven
replacement hazards, a risk register) and a diagnostic flow. That's the classic signal for the
repo's preferred pairing:

- `product-lifecycle-plays` — **Component**, the reusable framework
- `lifecycle-play-advisor` — **Interactive**, the guided triage

**Rejected alternative:** one large skill holding both. It would have buried the framework inside a
conversation flow, making it unusable as reference for someone who just wants the hazard list.

---

## Phase 2 — Generate draft

Written by hand. The source was workshop material with a strong internal structure already, so
`add-a-skill.sh` would have flattened it. **Rule of thumb:** use the generator when source material
is unstructured, write by hand when the structure is the value.

---

## Phase 3 — Tighten

What the review pass changed:

- **Added a "when NOT to use."** The first draft only said when to use it, which meant it read as
  applicable to every product question.
- **Added "nothing yet" as a real outcome.** The draft always produced a play. A mature product
  throwing off margin doesn't need a project, and a skill that always recommends action is a skill
  that generates busywork.
- **Made the extension test mandatory rather than optional.** Extension is the cheapest play and the
  most frequently skipped; leaving the test optional guaranteed it would be skipped.
- **Added two conversation-flow examples** (Interactive skills substitute these for the usual
  worked artifacts) — one where the recommendation contradicts the user's stated plan, because a
  triage skill that only confirms is worthless.
- **Cut a "Benefits of Lifecycle Thinking" section.** Pure filler. Nothing under it changed a
  decision.

---

## Phase 4 — Validate

```bash
bash scripts/test-a-skill.sh --smoke skills/lifecycle-play-advisor/SKILL.md
#   PASS conformance
#   PASS linked skill paths
#   PASS smoke checks

python3 scripts/check-skill-triggers.py
#   All skills pass trigger-readiness checks.
```

**A real failure caught here on the sibling workflow skill:** `eol-process` failed smoke with
*"section 'Application' is empty."* Cause: an H2 phase header (`## Phase 1: Decide`) directly
following `## Application`, so the parser saw no content between them. Fix: a lead-in paragraph,
the same way `discovery-process` does it.

---

## Phase 5 — Integrate

- README: new "Aging products" nav block, plus the pack table row
- `marketplace.json`: entries added by hand, alphabetically — **nothing automates this**, and
  `check-library-drift.py` is what catches you forgetting
- Cross-references added in both directions with `eol-readiness-advisor`,
  `organic-growth-advisor`, and `ansoff-matrix`
- `generate-catalog.py`, then `build-dist.sh`, then `check-dist-freshness.py`
- `validate-skills.sh` — 77 skills, no drift

---

## What to notice

- **Preflight nearly killed the build, and that's the point.** Two existing growth skills looked
  like overlap. Articulating the boundary — *where does growth come from* versus *what do we do with
  this product* — is what justified a new skill and produced the cross-references.
- **The pairing decision came from the source material's shape**, not from preference. Framework
  plus flow means Component plus Interactive.
- **Tightening removed a section and added a non-answer.** "Nothing yet" as a valid outcome is worth
  more than most features, because it stops the skill from manufacturing work.
- **The validator caught a structural bug no human review would have.** An empty-looking Application
  section is invisible when you're reading the file top to bottom.
- **Integration is the phase people skip.** Marketplace, catalog, and dist are all hand-triggered.
  A skill that exists in `skills/` but nowhere else is a skill nobody will find.
