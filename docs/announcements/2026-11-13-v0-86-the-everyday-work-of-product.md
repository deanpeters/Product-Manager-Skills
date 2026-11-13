# v0.86: The Everyday Work of Product, Now on the Map

**Released:** November 13, 2026
**Library:** 95 skills, up from 83 (36 Component, 34 Interactive, 25 Workflow) + 6 commands
**New:** 12 skills across Discover, Develop, Drive, and Deliver; a Practitioner-first README and install path; a docs style guard
**Retired:** the older themed packs `02` through `07`

---

## Why this release

The industry is moving the same direction. Claude Code installs skills as plugins from
marketplaces. Codex reads skills from `.agents/skills`, OpenCode reads the same `SKILL.md`
format, and the other coding agents are heading toward installable, bundled capabilities
instead of loose prompts. The era of "paste a giant prompt and hope" is ending. The era of
**named, installable bundles** is here.

This library does not go stale, because it moves when the terrain moves. v0.85 reorganized 83
skills into six lifecycle bundles so they install the way agents now expect.

The payoff is for you. Nobody's job needs all 95 skills at once, and a flat list of 95 is a
wall, not a tool. Bundles let you install what matches your work: Discover if you live in
research, Develop if you live in the backlog, Drive if your week is stakeholders and your
career. Install one bundle, or two, and your agent's skill list stays short enough to be
useful. Keeping up with the times is how we make it easier to pick the right slice, instead
of making you carry the whole library.

v0.86 is what that structure was for: filling the map. A bundle with gaps is a promise you haven't kept.

## What fills the map

The gaps were not exotic. They were the work PMs do every week and the work they skip.

**Discover: Dig** (go find the evidence)
- [`survey-design-advisor`](../../skills/survey-design-advisor/SKILL.md): what to ask, what not to
  ask, and when a survey is the wrong tool
- [`usage-data-investigation`](../../skills/usage-data-investigation/SKILL.md): turn "the numbers
  look off" into a question you can answer
- [`discovery-habits-advisor`](../../skills/discovery-habits-advisor/SKILL.md): make discovery a
  weekly habit instead of a project

**Discover: Decode** (make sense of what you found)
- [`research-synthesis`](../../skills/research-synthesis/SKILL.md): from a pile of notes to
  defensible findings
- [`assumption-mapping`](../../skills/assumption-mapping/SKILL.md): which assumptions can sink you,
  ranked

**Develop: Drumbeat** (the rhythm of building)
- [`backlog-refinement-advisor`](../../skills/backlog-refinement-advisor/SKILL.md)
- [`sprint-planning`](../../skills/sprint-planning/SKILL.md)
- [`release-readiness`](../../skills/release-readiness/SKILL.md)

**Drive: Delineate** (who decides what)
- [`decision-rights-matrix`](../../skills/decision-rights-matrix/SKILL.md)
- [`pm-role-charter`](../../skills/pm-role-charter/SKILL.md)

**Deliver: Deepen** (after launch is where retention is won)
- [`activation-design`](../../skills/activation-design/SKILL.md)
- [`retention-diagnostic-advisor`](../../skills/retention-diagnostic-advisor/SKILL.md)

Every one ships a `template.md` (Component and Workflow skills) and worked examples in two
domains, SaaS and industrial, so none of them quietly teaches "this is a software technique."
The intensity dial is yours: Light, Standard, or Heavy, never defaulted to the heaviest.

## Easier to start

A new reader now reaches their first skill in about five minutes. The README opens with a plain
definition of a skill and a short numbered path with the exact menu (**Settings → Capabilities →
Skills**), a prompt to paste, and a cue for what working looks like. `START_HERE.md` is layered
so the terminal steps live where the terminal users look. The Claude Desktop install guide now
says what to upload (the skill ZIPs inside the pack, never the outer one).

## Kept honest: a docs style guard

`scripts/check-docs-style.py` runs in validation. It fails the build on "click here" links,
stale version lines, stale pack names, and menu paths set in code font. A library that teaches
clarity should not let its own docs rot.

## Older packs retire

The themed packs `02-discovery` through `07-lifecycle-eol` are replaced by the six lifecycle
bundles. They stayed on the shelf for one release; this is the release they go. If you installed
one, nothing breaks: every skill in them lives in a bundle, and the bundle packs are
`pm-<bundle>-pack.zip` on the [download shelf](../../dist/).

## Upgrade

- **Claude Code:** `/plugin marketplace update pm-skills`, then install or refresh a bundle, for
  example `/plugin install pm-develop@pm-skills`
- **Claude Desktop / Web:** download the bundle pack you want, unzip it, upload the skill ZIPs
  inside
- **Codex, OpenCode, others:** pull the new `pm-skills-codex.zip`, or copy `skills/*`

## What's next

Reconciling overlapping frameworks (Porter's, Ansoff, Lean UX) across the library, and more
depth in Discover and Develop. The map will keep moving because the terrain does.
