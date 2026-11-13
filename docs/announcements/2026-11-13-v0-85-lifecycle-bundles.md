# v0.85 — Lifecycle Bundles, a Navigator, and the Go-to-Market Gap Filled

**Released:** November 13, 2026
**Library:** 83 skills, up from 77 (31 Component, 30 Interactive, 22 Workflow) + 6 commands
**New:** six installable lifecycle bundles, `pm-skills-navigator`, 5 go-to-market skills, `LICENSING.md`, OpenCode install guide

---

## Why this release

The library had grown to 70-plus skills in one folder. That is fine for an agent, and hard for a
person. "Where do I start?" had no good answer, and issue #12 had asked for themed installs
for months.

## Bundles that follow the product lifecycle

Product work unfolds in an order: set the outcome before you investigate, investigate before you
define, define before you build. The bundles follow that arc, the same one as the Productside
Blueprint, the SDLC, and the ADLC.

| Bundle | The question it answers | Install |
|---|---|---|
| **Determine** | What are we trying to achieve, and what is the market doing? | `/plugin install pm-determine@pm-skills` |
| **Discover** | What is really going on with customers? | `pm-discover@pm-skills` |
| **Define** | What are we betting on, and how do we de-risk it? | `pm-define@pm-skills` |
| **Develop** | How do we specify, decide, and delegate the build? | `pm-develop@pm-skills` |
| **Deliver** | How do we take it to market, measure it, and retire it well? | `pm-deliver@pm-skills` |
| **Drive** | How do I handle stakeholders and my own career? (runs under all five) | `pm-drive@pm-skills` |

Inside each bundle, skills are grouped into **motions** (for example Define holds *De-risk* and
*Differentiate*). Every bundle carries a few shared helper skills, so it works installed alone.

Two design decisions worth naming:
- **`skills/` did not move.** About 25 files reference that path. A single mapping in
  `pm-skills.config.yaml` is the source of truth; the plugins, download packs, catalog, Streamlit
  browser, and navigator are all generated from it, and validators fail on drift.
- **Every skill still runs on its own.** The bundles are a way to find and install, not a pipeline.

Claude Desktop and Web users get the same grouping as `pm-<bundle>-pack.zip` downloads.

## Not sure where you are? `pm-skills-navigator`

[`pm-skills-navigator`](../../skills/pm-skills-navigator/SKILL.md) (Interactive) asks what's on
your desk, what is validated versus assumed, and what you need to walk away with, then names the
phase and routes you to one to three skills. It tells you plainly when a motion has no skill yet.

## The go-to-market gap, filled

Five new skills for the part of the lifecycle that decides whether the work lands:

- [`launch-plan`](../../skills/launch-plan/SKILL.md) (Workflow): tiered by size, four dates
  (announce, order, deliver, support), go/no-go criteria written *before* the gate, a readiness
  scorecard, and a premortem
- [`launch-metrics`](../../skills/launch-metrics/SKILL.md): leading and lagging indicators,
  guardrails, decision triggers agreed before the result, and 30/90/180-day reviews
- [`message-house`](../../skills/message-house/SKILL.md): roof, value pillars, sourced proof, and
  a "cover test" that catches feature lists posing as pillars
- [`sales-value-narrative`](../../skills/sales-value-narrative/SKILL.md): why change, why now, why us;
  "do nothing" named as the main competitor; objections and a do-not-say list
- [`buying-journey-enablement`](../../skills/buying-journey-enablement/SKILL.md) (Workflow): the
  assets each role needs at each buying stage, for direct sales and partners

Same conventions as the rest of the library: one dial the user sets (launch tier; never default to
the heaviest), every unsupplied number is `[NEEDS SOURCE]` and never invented, and every skill
ships a template and two worked examples (Fieldlight SaaS and Northfield industrial).

## Also in this release

- **Guided Context Capture** (Nov 12): facilitation upgrades and a configurable default entry mode
- **[`LICENSING.md`](../../LICENSING.md):** a plain-language answer to "can I use this at work?"
- **[OpenCode install guide](../../docs/INSTALL-OPENCODE.md):** adapted from a community pull request
- **Link repair:** 14 broken cross-skill links found while building the bundles, fixed
- **Drift guards:** prose counts (total, per type, per bundle) are now checked, so the README
  can't quietly disagree with the library

## Upgrading

- **Claude Code:** `/plugin marketplace update pm-skills`, then install a bundle or keep
  `product-manager-skills` for everything.
- **Claude Desktop / Web:** download a `pm-<bundle>-pack.zip` from the [download shelf](../../dist/).
  The older themed packs (`02`-`07`) are still there for this release and retire in the next.

## Thank you

To the people who filed the issues that shaped this: #12 (themed plugins), #27 (licensing), and PR
#20 (OpenCode), whose docs became the install guide.
