---
name: stakeholder-identification
description: Map every stakeholder before engaging anyone. Use when launching an initiative, scoping discovery, or building an engagement plan from scratch.
compatibility: opencode
argument-hint: "[initiative]"
metadata:
  best_for:
    - "Launching a new initiative where the stakeholder landscape is unmapped and influence networks are unknown"
    - "Scoping a discovery sprint to define who to research, interview, and recruit"
    - "Preparing a PRD stakeholder section with a validated, comprehensive list before writing requirements"
    - "Onboarding to a new product domain and needing to map allies, gatekeepers, and decision-makers quickly"
    - "Pressure-testing an existing stakeholder list for blind spots, bias, and missing edge-case populations"
  intent: >-
    Produce a comprehensive, equity-aware stakeholder set before any engagement begins.
    Combines broad brainstorm with structured categorization (Allies / Audiences / Influencers,
    R/P/D marking), an explicit equity and bias check, and a disciplined narrowing to
    the 2-3 stakeholders to understand deeply first. Designed to run as a solo exercise
    or a kickoff workshop. Feed outputs directly into stakeholder-mapping for prioritization.
  scenarios:
    - "Who are all the stakeholders for this initiative?"
    - "Are we missing anyone important in our stakeholder map?"
    - "Help me prepare the stakeholder section of my PRD"
    - "Who should we recruit for discovery research?"
  sources:
    - "MITRE Innovation Toolkit — Stakeholder Identification Canvas: https://itk.mitre.org/toolkit-tools/stakeholder-identification-canvas/"
    - "MITRE Innovation Toolkit — Community Map: https://itk.mitre.org/toolkit-tools/community-map/"
  type: component
---

# Stakeholder Identification

## Purpose

Map every stakeholder before engaging anyone. This skill produces a comprehensive, equity-aware stakeholder set — not just the obvious sponsors and users, but the gatekeepers, the impacted communities, and the voices your team defaults to overlooking.

Most PM stakeholder lists are written from memory in five minutes. They reliably capture executives, product peers, and the most vocal users. They reliably miss the marginalized user groups who bear the product's consequences without having the organizational power to shape its decisions. This skill forces a slower, more structured brainstorm that builds the foundation for every engagement decision that follows.

Use this before stakeholder-mapping (which prioritizes) and before stakeholder-engagement-advisor (which plans per-stakeholder outreach). Identification comes first — you cannot prioritize people you haven't named.

## Input

**Works best with:** The initiative, product, or decision you're mapping stakeholders for.
**Also useful:** Stakeholders already on your list (the skill's job is to find who's missing), org context, and affected communities.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** The skill asks what the initiative is and who it touches, then runs the equity-aware sweep.

**Example invocation:** `Identify stakeholders for migrating all customers to the new billing system by Q4.`

## Key Concepts

**Allies, Audiences, Influencers** — The three categories that clarify stakeholder relationship to your work. Allies actively support the initiative; audiences are impacted by it; influencers shape opinion or decisions without being directly affected. Sorting stakeholders this way reveals who to recruit, who to inform, and who to persuade — three different engagement jobs.

**R/P/D Marking** — Tagging each stakeholder as a provider of Resources (budget, headcount, access), Permission (approval to proceed, regulatory clearance), or Decision-making authority (final say). This quickly surfaces who can fund, block, or green-light your initiative versus who is merely interested. One stakeholder can hold multiple tags.

**Equity Lens** — Deliberately stretching the list to include stakeholders who are often excluded: marginalized user populations, frontline employees, downstream communities, people who bear the product's consequences but lack organizational power to influence its design. Without this step, teams optimize for loud, well-resourced voices and build products that fail the quieter majority.

**Primary, Secondary, Tertiary Effects** — Tracing ripple effects of your product outward from direct users to indirectly affected groups. A feature that changes how support agents work (primary) affects how customers experience service (secondary), which affects the company's reputation and churn (tertiary). Following the chain surfaces stakeholders that single-level thinking misses.

**Notice Bias & Assumptions** — An explicit team check: who did we default to naming? Who is absent from the list? Whose perspective are we treating as universal? This step names the blind spots before they become requirements gaps.

**Identification vs. Prioritization** — The discipline of separating who exists from who matters most. The goal of this skill is a complete list, not a prioritized one. Collapsing these two steps causes teams to prematurely cut stakeholders they haven't yet understood. Prioritization happens in stakeholder-mapping.

## Application

**Step 1 — Brainstorm without filtering**

Generate a fast, unconstrained list of potential stakeholders: individuals, teams, organizations, and communities connected to this initiative. Do not self-edit. Write down anyone who could plausibly have a stake — even if their involvement seems unlikely.

If working in a group, run this silently for 4-6 minutes before sharing.

**Step 2 — Categorize**

Sort each stakeholder into one or more of these categories:

- **Allies** — who actively supports this work or would benefit from its success?
- **Audiences** — who is impacted by the outcome, directly or indirectly?
- **Influencers** — who shapes decisions, opinion, or adoption without being a direct participant?

Note: a stakeholder can appear in more than one category. Those overlaps — an ally who is also a key influencer — often mark your highest-leverage relationships.

**Step 3 — Apply R/P/D marking**

For each stakeholder, mark whether they provide:

- **R** — Resources (budget, people, data, access)
- **P** — Permission (approval, legal clearance, sign-off)
- **D** — Decision authority (final say on scope, prioritization, or launch)

Any stakeholder holding P or D who is missing from your list is a gap that will surface later as a blocker.

**Step 4 — Apply the equity lens**

Ask the following questions about your list:

- Who experiences a significant difference or consequence from this product — financially, professionally, or in their daily experience?
- Who bears the product's costs or risks without having the power to shape its design?
- Whose perspective is missing because we assumed someone else represents them?
- Who are the primary users? Who are the secondary users? Who is affected in the third degree?

Add anyone the equity lens surfaces. These stakeholders are likely to end up in Q1 of your stakeholder-mapping (high impact, low power) — the voices most important to elevate.

**Step 5 — Notice bias and assumptions**

As a group, answer explicitly:

- Who did we default to naming in Step 1?
- Who is absent? Why?
- What assumptions did we make about who counts as a stakeholder?

Record the answers. These shape your research plan and recruitment strategy.

**Step 6 — Narrow to priority targets**

With the full list visible, identify the 2-3 stakeholders you need to understand most deeply before proceeding. These are typically:

- The highest-power decision-makers whose buy-in is required
- The highest-impact users whose needs are least understood
- The most likely blockers or skeptics

For each priority stakeholder, capture: name, category, R/P/D tag, and a one-line "what we need to learn from them." These outputs feed directly into stakeholder-mapping and stakeholder-engagement-advisor.

## Examples

**Situation:** A product team is scoping a new intake workflow that replaces manual email-based requests with a self-service portal. Initial stakeholder list: VP of Operations, Engineering Lead, PMO Director, enterprise customers.

**Underdeveloped (common default):**
The list captures obvious sponsors and the customer segment that asked loudest for the feature. Missing: the customer support agents who currently process every manual request (primary daily users of the current workflow), IT security team (P — must approve data handling), compliance officer (P — regulatory implications), small business customers who lack technical staff to use a self-service portal (high-impact, low-power audience).

**Stronger list after applying equity lens and R/P/D marking:**
- VP of Operations (D, Ally) — final scope authority
- Engineering Lead (R, Ally) — capacity and technical feasibility
- PMO Director (P, Influencer) — must approve process change
- Enterprise customers (Audience) — primary users of new portal
- **Customer support agents** (Audience, R) — process every intake today; adoption risk if not consulted
- **IT Security** (P) — data handling approval required
- **Compliance Officer** (P) — regulatory review
- **Small business customers** (Audience) — impacted differently; may need a non-self-service path

The second list produces a PRD with different requirements, a different rollout plan, and a different definition of success.

## Common Pitfalls

**Treating the first brainstorm as the final list.** The initial pass reliably captures 60% of stakeholders and systematically misses the 40% who are less visible. The categorization and equity steps exist to close that gap — skipping them defeats the exercise.

**Listing roles or org units instead of people.** "Engineering" is not a stakeholder. The engineering lead who controls sprint capacity is. Vague category names prevent you from booking the conversation you actually need.

**Conflating identification with prioritization.** Cutting stakeholders during the brainstorm phase, before you've understood their actual influence or impact, is how high-impact, low-power voices get silently dropped. Complete the list first. Prioritize in stakeholder-mapping.

**Skipping the bias and assumptions check.** Teams that skip this step feel confident in their completeness. Teams that run it discover they've assumed a well-resourced user proxy speaks for everyone. Name the blind spot explicitly.

**Running it solo without external validation.** A single person's stakeholder map reflects a single person's network and assumptions. If working solo, use the bias check to identify who is absent from your mental model, then validate with a cross-functional colleague before proceeding.

**Generating a complete list but capturing no next steps.** The canvas ends with priority targets and actions for a reason. A comprehensive stakeholder list with no "who talks to whom, by when" attached is a document, not a plan.

## References

- [stakeholder-mapping](../stakeholder-mapping/SKILL.md) — next step: prioritize the identified stakeholders using Power × Interest and Impact × Power grids
- [stakeholder-engagement-advisor](../stakeholder-engagement-advisor/SKILL.md) — per-stakeholder engagement planning once priority targets are set
- [discovery-interview-prep](../discovery-interview-prep/SKILL.md) — use identified stakeholders as the basis for research recruitment
- [proto-persona](../proto-persona/SKILL.md) — once high-priority user stakeholders are identified, develop hypothesis-driven personas
- MITRE Innovation Toolkit — [Stakeholder Identification Canvas](https://itk.mitre.org/toolkit-tools/stakeholder-identification-canvas/)
- MITRE Innovation Toolkit — [Community Map](https://itk.mitre.org/toolkit-tools/community-map/)
