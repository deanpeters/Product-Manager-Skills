---
name: stakeholder-mapping
description: Prioritize stakeholders using two complementary grids. Use when setting engagement strategy and surfacing whose voice needs elevating after stakeholder identification.
compatibility: opencode
argument-hint: "[stakeholder list or initiative]"
metadata:
  best_for:
    - "After stakeholder identification, when you need to decide who gets which level of engagement"
    - "Preparing an engagement plan before a roadmap review where executives and impacted user groups have conflicting authority"
    - "Surfacing high-impact, low-power user segments who deserve more voice in product decisions but lack org pull"
    - "Re-baselining stakeholder strategy after a reorg has shifted who holds decision authority"
    - "Planning a compliance or regulatory initiative where power to block sits separately from who bears the consequences"
  intent: >-
    Run two complementary 2x2 grids — Power × Interest (sets engagement strategy per
    stakeholder) and Impact × Power (surfaces who bears consequences but lacks voice) —
    then compare outputs to reveal blind spots and plan quadrant migration. The grids
    answer different questions and neither one alone is sufficient: Power × Interest
    tells you how to engage; Impact × Power tells you whose voice to elevate. Feed
    outputs into stakeholder-engagement-advisor for per-stakeholder action planning.
  scenarios:
    - "Who should I prioritize engaging on this initiative?"
    - "How do I handle stakeholders with conflicting priorities?"
    - "Help me figure out whose voice is missing from our roadmap decisions"
    - "I need a stakeholder engagement strategy before our quarterly review"
  sources:
    - "MITRE Innovation Toolkit — Stakeholder Map & Matrix: https://itk.mitre.org/toolkit-tools/stakeholder-map-and-matrix/"
    - "MITRE Innovation Toolkit — Stakeholder Power Categories: https://itk.mitre.org/toolkit-tools/stakeholder-power-categories/"
  type: component
---

# Stakeholder Mapping

## Purpose

Prioritize stakeholders and set engagement strategy. This skill runs two complementary grids on your identified stakeholder set and deliberately compares what they reveal, because each grid shows you something the other cannot.

**Power × Interest** answers: how much does each stakeholder care about this initiative, and how much can they influence it? It produces engagement strategies — who to involve deeply, who to keep informed, who to monitor. This is the grid most PMs know.

**Impact × Power** answers: who bears the consequences of this product's outcomes, and how much organizational power do they actually hold? It surfaces the stakeholders who matter most to get right but are most likely to be underrepresented — high impact, low power.

Running only the first grid optimizes for managing relationships with the powerful. Running only the second produces an equity analysis without an engagement plan. The insight lives in comparing them: a stakeholder who appears in "keep informed" on the first grid and "high impact, low power" on the second is someone you've been under-engaging with consequences that fall entirely on them. That's a product risk.

Use this after stakeholder-identification (which builds the full list) and before stakeholder-engagement-advisor (which plans per-stakeholder outreach).

## Input

**Works best with:** Your identified stakeholder list (ideally from `stakeholder-identification`).
**Also useful:** What you know about each person's power, interest, and current stance, plus the engagement decisions the map must drive.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** The skill asks for the stakeholder set first — mapping unidentified stakeholders just formalizes your blind spots.

**Example invocation:** `Map these 14 stakeholders for the billing migration on both grids — list attached with role notes.`

## Key Concepts

**Power × Interest Grid** — A 2×2 that plots stakeholders by their power to affect the initiative (vertical axis) and their interest in its outcome (horizontal axis). Produces four quadrants with prescribed engagement strategies:
- High power, high interest → **Manage closely** (co-design, frequent touchpoints)
- High power, low interest → **Keep satisfied** (executive briefings, strategic framing)
- Low power, high interest → **Keep informed** (newsletters, demos, transparency)
- Low power, low interest → **Monitor** (light touch, check-ins only)

**Impact × Power Grid** — A 2×2 that plots stakeholders by whether they are significantly affected by the initiative (vertical axis) and the power they hold to shape it (horizontal axis). Produces four quadrants:
- High impact, high power → **Q2** — impacted and empowered; manage closely
- High impact, low power → **Q1** — impacted but marginalized; elevate their voice deliberately
- Low impact, high power → **Q4** — gatekeepers; manage relationship, lower engagement depth
- Low impact, low power → **Q3** — monitor, minimal investment

**Elevating Q1 Voices** — High-impact, low-power stakeholders (Q1) are the people most likely to experience your product's failure modes and least likely to appear in your normal feedback loops. Deliberately increasing their role in roadmap decisions — through research recruitment, usability testing, and requirements review — is not just equitable; it reduces the product risk of building for the wrong problems.

**Quadrant Migration** — The deliberate strategy of moving a stakeholder from their current quadrant to a desired one through targeted actions. A skeptical executive currently in "monitor" who needs to become a sponsor requires a different set of actions than one already in "manage closely." Making migration explicit turns the map from a snapshot into a plan.

**Impact vs. Power** — These are not the same dimension. A frontline support agent has high impact (their daily workflow changes completely) but low power (no seat at the roadmap table). A VP of Finance has high power (budget approval) but low impact (the product doesn't change how they work). Conflating the two is the most common mapping error.

**Paired Variables** — The reason to run both grids rather than one. Different paired axes reveal different relationships. A single grid produces a single, incomplete picture. Running multiple analyses and comparing outputs is where the real insight lives.

**Engagement Strategy** — The differentiated communication and involvement approach assigned per quadrant. It allocates limited PM bandwidth where it yields the most leverage — and protects against the trap of treating all stakeholders equally, which means investing in low-stakes relationships while neglecting critical ones.

## Application

**Step 1 — Run the Power × Interest grid**

For each stakeholder from your identification exercise, assess:
- **Power:** Can this person or group significantly shape, regulate, approve, or block this initiative? (Consider formal authority, budget, veto power, and informal influence.)
- **Interest:** Is this person or group actively engaged in or affected by the outcome? Do they have stated or likely opinions about the direction?

Place each stakeholder in the appropriate quadrant. Don't rank or quantify within quadrants at this step — the placement itself is the output.

Assign engagement strategy per quadrant:
- Manage closely → deep involvement, co-design sessions, weekly or bi-weekly touchpoints
- Keep satisfied → executive briefings, high-level framing, milestone updates
- Keep informed → structured communications, demos, read-only access to artifacts
- Monitor → light check-ins, available but not pursued

**Step 2 — Run the Impact × Power grid**

For each stakeholder, assess separately:
- **Impact:** Will this initiative significantly affect this person or group — financially, professionally, in their daily work, or in their access to services? If yes, they're high impact.
- **Power:** Can they significantly shape the initiative, regardless of whether they want to? (Same definition as Step 1, but assessed independently of interest.)

Place each stakeholder in the Q1–Q4 quadrants. Do this without referencing your Power × Interest placements — the independence of the two assessments is what makes the comparison valuable.

**Step 3 — Compare and find the gaps**

Place both grids side by side and ask:

- Who appears in "keep informed" on Grid 1 and Q1 (high impact, low power) on Grid 2? These are stakeholders you're under-engaging relative to how much the product affects them.
- Who appears in "manage closely" on Grid 1 and Q3/Q4 on Grid 2? These are powerful stakeholders with little stake in the outcome — watch for over-investment.
- Who moved dramatically between grids? Those shifts reveal where power and consequences are misaligned.

**Step 4 — Plan quadrant migration**

For stakeholders you want to move:
- Q1 → Q2: Actively recruit them into advisory processes, discovery research, and requirements review. Give them a named role, not just passive access.
- Monitor → Keep informed: Increase transparency to build awareness and early alignment before the initiative becomes relevant to them.
- Skeptic in any quadrant → Ally: Identify what they need to believe to become supportive, then design 1:1 engagement to address those concerns directly.

Document: who is moving, what action triggers the move, and who owns it.

**Step 5 — Feed into engagement planning**

For each stakeholder in "manage closely" and each Q1 stakeholder, create an engagement plan using stakeholder-engagement-advisor. These are the relationships where tactical planning — specific messages, mediums, cadences, and success criteria — yields the most return.

## Examples

**Situation:** A platform team is migrating internal API infrastructure. Stakeholder list: VP of Engineering (sponsor), three engineering leads (direct users), Legal (compliance review), the customer support team (their tooling depends on the APIs), and enterprise customers who won't see the change directly but whose uptime depends on it.

**Power × Interest grid placements:**
- VP of Engineering → Manage closely (high power, high interest)
- Engineering Leads → Manage closely (high power, high interest — direct builders)
- Legal → Keep satisfied (high power, low day-to-day interest)
- Customer Support → Keep informed (low power, high interest — their tools change)
- Enterprise Customers → Monitor (low power, low stated interest)

**Impact × Power grid placements:**
- VP of Engineering → Q2 (high impact, high power)
- Engineering Leads → Q2 (high impact, high power)
- Legal → Q4 (low impact, high power)
- Customer Support → **Q1** (high impact, low power — their tooling breaks if migration fails)
- Enterprise Customers → **Q1** (high impact, low power — uptime dependency)

**The gap the comparison reveals:** Customer Support and Enterprise Customers are "monitor" or "keep informed" on Grid 1, but Q1 on Grid 2. The migration team has been treating them as passive observers when they're actually the highest-risk stakeholders. Resolution: recruit support agents into UAT, create an enterprise customer communication plan with rollback triggers, and add both groups to the launch readiness criteria.

## Common Pitfalls

**Running only one grid.** Power × Interest without Impact × Power optimizes for managing relationships with the powerful while systematically under-serving high-impact, low-power groups. Impact × Power without Power × Interest produces an equity analysis with no engagement strategy attached. Both grids earn their place.

**Conflating organizational seniority with power.** A mid-level program manager who controls the approval queue for your initiative holds more practical power than a VP who's uninvolved. Informal influence — process knowledge, gatekeeping, coalition-building — is real power. Assess it, don't assume the org chart reflects it.

**Treating placement as permanent.** Org changes, budget cycles, and stakeholder rotations shift people between quadrants. Build in a re-run cadence at quarterly review cycles or after significant org events.

**Stopping at placement without engagement actions.** Two grids with dots on them and no "who does what next" is a pretty slide, not a plan. The map is a means to the migration strategy and the per-stakeholder engagement plan.

**Quantifying or ranking within quadrants at placement time.** The method explicitly discourages this. False precision at the categorization step derails the discussion into arguing about relative rankings instead of identifying who's missing from the right quadrants.

**Letting Q1 stakeholders remain decorative.** Naming high-impact, low-power stakeholders on the canvas and then continuing to engage them the same way is the most common failure. Elevation requires a concrete action: a named research slot, a co-design session, a role in requirements review, a presence at the launch readiness gate.

## References

- [stakeholder-identification](../stakeholder-identification/SKILL.md) — prerequisite: build the full stakeholder list before prioritizing
- [stakeholder-engagement-advisor](../stakeholder-engagement-advisor/SKILL.md) — next step: per-stakeholder engagement planning for "manage closely" and Q1 stakeholders
- [discovery-interview-prep](../discovery-interview-prep/SKILL.md) — recruit Q1 stakeholders into research
- [workshop-facilitation](../workshop-facilitation/SKILL.md) — run the mapping exercise as a facilitated team session
- MITRE Innovation Toolkit — [Stakeholder Map & Matrix](https://itk.mitre.org/toolkit-tools/stakeholder-map-and-matrix/)
- MITRE Innovation Toolkit — [Stakeholder Power Categories](https://itk.mitre.org/toolkit-tools/stakeholder-power-categories/)
