# Skill Authoring Worksheet

A per-skill tracker for the five phases, with the commands and the definition of done. Quality
checks at the bottom.

## Provenance
Dogfooded from this repo's own authoring standards — `CLAUDE.md`, `CONTRIBUTING.md`, and the
validation scripts under `scripts/`.

**Note:** this is a meta-skill about building skills in this repository, so it ships one worked
example rather than the usual two business domains. A second "domain" here would be artificial.

---

## The tracker

```markdown
## Skill Build: [skill-name]

**Type:** [component / interactive / workflow]
**Theme:** [existing theme, or "new — justify below"]
**Source material:** [file, transcript, prompt, or "original"]

---

### Phase 1 — Preflight

- [ ] Searched for overlap: `./scripts/find-a-skill.sh --keyword "<topic>"`
- Overlapping skills found: [list, or none]
- **Decision:** [new skill / extend an existing one / merge]
- **Why not extend an existing skill?** [answer — this is the question most often skipped]

**Type rationale:**
- Component = one artifact or template
- Interactive = 3-5 adaptive questions + numbered options
- Workflow = multi-phase orchestration
- **Chosen because:** [reason]

---

### Phase 2 — Generate draft

- [ ] `./scripts/add-a-skill.sh research/<file>.md`  (from source material)
- [ ] `./scripts/build-a-skill.sh`  (guided prompts)
- [ ] Written by hand

---

### Phase 3 — Tighten

- [ ] Clear "when to use" — and a "when NOT to use"
- [ ] At least one concrete example; two from different business domains where the skill isn't
      definitionally single-domain
- [ ] `template.md` if the skill produces an artifact — output schema as a copy/paste fill-in,
      with quality checks
- [ ] At least one explicit anti-pattern, with its consequence named
- [ ] No filler, no vague consultant-speak
- [ ] Pedagogy intact — explanation is load-bearing, not decoration

---

### Phase 4 — Validate

```bash
./scripts/test-a-skill.sh --skill <skill-name> --smoke
python3 scripts/check-skill-metadata.py skills/<skill-name>/SKILL.md
python3 scripts/check-skill-triggers.py
```

- [ ] Conformance passes
- [ ] Linked skill paths resolve
- [ ] Smoke checks pass with no new warnings
- [ ] Trigger audit clean (`description` contains a literal "Use when")

---

### Phase 5 — Integrate

- [ ] Added to the correct README category table and nav block
- [ ] Added to `.claude-plugin/marketplace.json` — **hand-maintained**, alphabetical
- [ ] Cross-referenced from related skills' References sections
- [ ] `python3 scripts/generate-catalog.py`
- [ ] `bash scripts/build-dist.sh`
- [ ] `python3 scripts/check-dist-freshness.py`
- [ ] `bash scripts/validate-skills.sh` — the CI path

---

### Frontmatter check

- [ ] `name` matches the folder name exactly
- [ ] `description` ≤200 chars, contains a literal "Use when"
- [ ] `intent`, `type` present
- [ ] `theme`, `best_for`, `scenarios`, `estimated_time` present
- [ ] YAML values containing colons are quoted
```

---

## Quality checks

**Preflight**
- [ ] You genuinely searched before building. Duplicate skills are the most common waste in this repo
- [ ] "Why not extend an existing skill?" has a real answer

**Anatomy**
- [ ] Sections in order: Purpose, Input, Key Concepts, Application, Examples, Common Pitfalls,
      References
- [ ] The Input section reads as invitation, never as a gate — "Works best with," plus reassurance
      that arriving empty-handed is fine
- [ ] No bare `$ARGUMENTS` anywhere in the body (validation fails on it, and the stance is
      deliberate)

**Pedagogy — the one that matters most here**
- [ ] Anti-patterns are present and explain the *consequence*, not just the mistake
- [ ] Examples show reasoning, not only output
- [ ] Nothing was cut purely to tighten copy. **Stripping learning scaffolding is a defect in this
      repo, not an improvement**

**Workflow skills specifically**
- [ ] `## Application` has a lead-in paragraph before the first phase header — an H2 phase header
      immediately after it makes smoke report the section as empty

**Integration**
- [ ] Marketplace entry added — nothing else adds it for you
- [ ] Catalog and dist regenerated, freshness check passing
