---
name: launch-plan
argument-hint: "[what is launching, and the date that drives it]"
description: "Build a launch plan sized by tier: owners, dates, go/no-go criteria, and a readiness scorecard. Use when a launch needs every function ready at once and nobody has defined 'ready'."
intent: >-
  Make a launch a coordinated business event instead of a ship date, so every function that touches
  the customer is ready, the effort fits the size of the launch, and the go/no-go call is made on
  criteria the team agreed before anyone saw the status. Right-sized so a minor variant gets a short
  punch list and a platform launch gets the full cross-functional plan.
type: workflow
theme: strategy-positioning
best_for:
  - "Planning a launch across Sales, Support or Service, Marketing, Legal, and Operations"
  - "Deciding how much launch effort an offering deserves before the work starts"
  - "Writing go/no-go criteria before the gate, not after the status is known"
  - "Reviewing a launch plan for the function everyone forgot"
scenarios:
  - "We launch the route optimizer in six weeks and Support has not seen it yet. Build the plan"
  - "Is this a Tier 1 or Tier 2 launch, and what does each function owe us?"
  - "Review our launch plan. I think we forgot the distributors and the spare parts"
  - "Help me write go/no-go criteria for a hardware launch with a trade-fair date"
estimated_time: "30-60 min to plan; weeks to execute"
---

# Launch Plan

## Purpose

Build the plan that makes a launch land: a checklist of what each function must have ready, sized
by launch tier, with a named owner, a date, and a status on every row; go/no-go criteria agreed
before the gate; and a one-page **Launch Readiness Scorecard** the launch forum uses to decide.

The sentence to keep in your head: **a launch is a business event, not a ship date.** Engineering
finishing the product is one row. A customer experiences a launch as finding out about it, getting
a price, buying it, receiving it, using it, and getting help when it breaks. Each of those belongs
to a different function, and the customer sees whichever one is not ready.

The PM orchestrates. The PM does not own every row. This is influence work: make the gaps visible
early enough that the people who own them can close them.

## Input

**Works best with:** What is launching and the date that drives it (a conference, a contract, a
season, a budget year).

**Also useful:** The positioning statement, the price decision, the channels you sell through
(direct, partners, distributors, marketplaces), the last launch's lessons learned, and who will
make the go/no-go call.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill opens by asking what is launching and what
fixes the date, proposes a tier from your answers, and builds from there. Anything you can't supply
becomes a labeled `[NEEDS SOURCE]` blank instead of an invented one.

**Example invocations:**
- `Launch plan for our route optimizer. GA is June 12, Sales and Support are not briefed.`
- `Review our launch checklist for the NFA-500 controller. Trade fair is April 21. I think we forgot distributor price files.`

---

## Key Concepts

### Right-Size the Launch (the Tier Dial)

**Not every launch deserves the same effort.** A tier is an agreed size class that decides how many
rows apply and how deep each goes.

| | **Tier 1: Full** | **Tier 2: Standard** | **Tier 3: Light** |
|---|---|---|---|
| Typical launch | New platform or generation, new market, new business model, large revenue at stake, new regulatory exposure | Significant new variant, major feature or option, adjacent segment on existing channels | Minor variant, small feature, cost-down invisible to customers |
| Functions engaged | All | Most, lighter depth | Price list, release note, internal notice |
| Gates | Formal go/no-go (often two: order intake, first shipment or GA) | One gate | None unless compliance is touched |
| Output feel | Cross-functional playbook | Working checklist with owners | Punch list |

Score the tier on six criteria, each low / medium / high with a one-line reason: **revenue and
margin at stake**, **newness to the customer**, **newness to the company** (new channel, model, or
production process), **regulatory and safety exposure**, **installed-base impact** (replaces,
cannibalizes, or must coexist with what customers own), and **channel impact** (do partners need new
skills, stock, or contracts).

**Tier 2 is the default. Never default to Tier 1.** Recommend a tier, say why in one line, and let
the user move it in either direction. If they go lighter, name what drops out so the choice is
informed. If the scores split (low revenue, high regulatory exposure) say so: a Tier 2 launch can
carry a Tier 1 compliance workload. Watch for **tier inflation** (everything is Tier 1, so the
checklist becomes noise) and **tier deflation** (a Tier 1 change labeled Tier 3 to dodge the work).

### Readiness by Function

Organize the checklist by function, because that is how ownership works in a matrix organization.
These are the functions that most often fail:

- **Sales and channel.** Briefed and trained before customers hear; partners told early enough to
  plan stock, training, and their own messaging; quoting and configuration tools updated; demo
  environments or demo units ready.
- **Support, Service, and spare parts.** Trained before the first customer; runbooks, diagnostic
  tools, and escalation paths released; capacity planned for the launch wave; for hardware, spare
  parts defined, priced, and stocked where the field needs them.
- **Operations, supply chain, and production.** Capacity and lead times confirmed; ramp sized to
  the realistic forecast, not the hopeful one; first-article or first-release quality passed.
- **Pricing and commercial.** Price, discounts, and packaging approved; price lists, billing, and
  quoting entries created; partner price files sent in time for *their* cycles.
- **Legal, compliance, and certification.** Terms, privacy, and security reviews done; for
  hardware, conformity assessment and country approvals planned. A missing certificate stops
  shipments no matter how ready everything else is.
- **Documentation and training.** Guides, safety instructions, and customer training in every
  language and market you sell into.
- **Marketing.** Messaging from the positioning statement, web page, data sheets, demos, press,
  event material.
- **Internal enablement.** Order handling, customer success, finance, and legal know what changes
  for them. FAQs and escalation contacts exist.

### Four Dates, Not One

Software launches often collapse these into one day. Industrial launches cannot. Name all four, and
make the gap between each a deliberate choice:

1. **Announce.** Customers and the market hear.
2. **Order opens.** Quotes and orders accepted, delivery promised.
3. **First delivery.** The product reaches a customer (first shipment, or first tenant live).
4. **Full support.** Service, training, and spare parts available everywhere you sell.

Announcing long before you can deliver stalls sales of the current product while customers wait.
Opening orders before capacity is confirmed breaks delivery promises. Delivering before support is
ready turns the first customers into the worst reference stories.

### Go/No-Go Criteria Are Agreed Before the Gate

A gate is a scheduled decision. Its criteria must be written down, with owners and thresholds,
before anyone sees the status. Otherwise the team looks at a mixed picture and talks itself ready.

- **Must-pass:** if one fails, the launch does not proceed (support trained in launch regions;
  signed declaration of conformity; security review closed).
- **Watch:** a failure needs a mitigation and an owner but does not stop the launch (translated
  guide for a secondary market).

The PM prepares the gate. The forum with decision rights makes the call. This skill never makes the
go/no-go decision.

### The Launch Readiness Scorecard

The checklist has dozens of rows. The forum needs one page: a row per function, a column per
readiness criterion, with status, owner, and evidence.

| Function | Readiness criteria | Status | Owner | Evidence |
|---|---|---|---|---|
| Support | Agents trained, runbook live, escalation path tested | Ready / At risk / Not ready | Named person | Training roster, runbook link |

Three rules keep it honest:
- **Status needs evidence.** Ready means the evidence in the criterion exists. An owner's optimism
  is "At risk" until it does.
- **Define the statuses before the first review.** What makes a row Ready, At risk, Not ready.
- **Must-pass rows are marked.** One must-pass "Not ready" means the scorecard says no-go, however
  green the rest looks.

**RACI for the work, DACI for the decision.** Give each function row a RACI (Responsible,
Accountable, Consulted, Informed). Give each gate a DACI: the **Driver** (usually the PM) prepares
it, one **Approver** decides, **Contributors** supply status and evidence, the **Informed** hear the
outcome. A go/no-go with two approvers is not a decision.

### Owners Are People, Not Departments

"Marketing" is not an owner. Every row needs a named person (or role, if names are confidential)
who has agreed to the date. A row the owner has not agreed to is a wish. Mark it At risk.

### The Premortem: Imagine the Launch Already Failed

A checklist finds the rows a team forgot. It does not find the failure nobody wants to say out
loud. Gary Klein's **premortem** does: imagine the launch has already failed and explain why.
Treating failure as a fact that already happened makes people name more and sharper causes than
"what could go wrong?", and it gives quiet doubters permission to speak.

Run it once, after the checklist and criteria are drafted, before the gate:

1. **Set the scene.** "It is six months after launch, and it failed. What happened?"
2. **Write failure stories alone first.** Each function owner writes what failure looks like from
   where they sit. Writing alone keeps the most senior voice from setting the story.
3. **List the causes.** Actions, inactions, assumptions, dependencies, partners.
4. **Rank by likelihood and impact.** Keep the few drivers that matter.
5. **Convert every driver into the plan.** Each becomes a readiness criterion (must-pass or watch)
   or a risk with an owner, a trigger, and a response. A story that changes nothing was not
   finished.

The premortem is a team exercise. AI can prompt it and propose typical failure stories as labeled
suggestions. It cannot know why *your* launch would fail.

### Pre-Approval Check: Will This Plan Hold?

Before the forum approves, test it as an approver would:

- **Owners:** separate owners for delivery, adoption, operation, and measurement. No risk owned by
  "the team."
- **Dependencies:** the critical path is named, including outside parties and capacity assumptions.
- **Risks:** each has a cause, trigger, consequence, response, owner, and remaining exposure.
- **Adoption:** someone owns whether sales, partners, and customers actually change behavior, not
  just whether they were trained.
- **Evidence:** milestones produce evidence (a signed record, a training roster), not just dates.
- **Rollback:** what pauses orders, what happens to units already delivered, and who decides.

Match the depth to the tier and to how reversible the step is.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally: heads-up, context dump, numbered choices, one question per turn.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not the build plan.** Engineering's schedule is one input, not the launch plan.
- **Not a campaign plan.** Marketing owns that. This plan checks that it exists and is on time.
- **Not the go/no-go decision.** The forum decides. You prepare the gate.
- **Not a pricing decision.** See [`finance-based-pricing-advisor`](../finance-based-pricing-advisor/SKILL.md).
- **Not the success measures.** What "worked" means belongs to [`launch-metrics`](../launch-metrics/SKILL.md).

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** The artifact comes first: tier assessment, four dates, checklist by
function, go/no-go criteria, scorecard, risks. Commentary is short and trails it. Draft in two
stages: a **working draft** where every row carries a provenance tag (`[FROM YOU]`, `[RESEARCH]`,
`[AI-SUGGESTED, VALIDATE THIS]`) and every unsupplied date, owner, quantity, or threshold is
`[NEEDS SOURCE]`, never a plausible guess; then a **committed copy** with tags removed, followed by
a ranked **Riskiest Assumptions** list.

**If the PM brings a draft, critique first.** Check the tier and its evidence; the four dates;
each function for missing rows, missing owners, missing dates, and "green" with no evidence; whether
go/no-go criteria were written before the gate and are measurable; the pre-approval check; and
where the premortem's drivers landed. Name gaps; don't fill them. Offer rewrites last.

### Step 1: Confirm Scope
Establish what is launching and what is new about it, which markets and regions, which channels,
what fixes the date, and who makes the go/no-go call. **Guard against defaulting to one kind of
launch.** A SaaS checklist (release notes, feature flags, in-app announcement) misses certification,
spare parts, and distributors. A hardware checklist misses security review, billing, and
tenant-level rollback. Ask whether the offering includes hardware, installation, or physical
service, and whether it is software, and include the rows that apply.

### Step 2: Gather Evidence
Offer two things: **research** (applicable regulations for the category and market, event dates,
partner price-list cycles, competitor launch timing if public) and **your own artifacts**
(positioning, roadmap, price calendar, lead times, partner agreements, last launch's lessons). Either, both, or
neither is fine.

### Step 3: Propose the Tier
Score the six criteria with one-line reasons. Recommend a tier, name what a lighter tier would
leave uncovered, and say the forum confirms it. Let the user move it.

### Step 4: Set the Four Dates
Ask for, or mark `[NEEDS SOURCE]`: announce, order opens, first delivery, full support. Work
backward from the fixed date and name the lead times on the critical path (certification, supplier
tooling, translation, partner price-list deadlines, spare parts stocking, security review).

### Step 5: Build the Checklist by Function
For each function, the rows that apply at this tier, each with a one-line deliverable ("done" in a
sentence), a named owner, a due date relative to the four dates, and a status. Keep rows the user
supplied; add missing ones as `[AI-SUGGESTED, VALIDATE THIS]`. Never invent owners or dates.

### Step 6: Draft the Go/No-Go Criteria and the Scorecard
Four to eight criteria: what is checked, threshold, evidence, owner, must-pass or watch. Name the
gates and who decides at each. Then roll the checklist into the scorecard with written status
definitions, RACI per row, and a DACI per gate.

### Step 7: Name the Risks, Run the Premortem, Run the Pre-Approval Check
List the top risks (critical-path rows, rows without agreed owners, dates held by outside parties),
each with one mitigation and one owner. Run the premortem with function owners and convert every
driver. Close with the pre-approval check. Name each gap; don't fill it.

### Step 8: Hand Off and Hand Back
The plan ends at "ready." Whether the launch *worked* is a different question: offer
[`launch-metrics`](../launch-metrics/SKILL.md). Close with a short summary (supplied, inferred,
unknown) and a numbered decision ladder, the evidence-favored option first, labeled `(Recommended)`:
confirm the tier and send rows to owners for agreement; hold a kickoff with all function owners to
fill the `[NEEDS SOURCE]` rows; move the announce date to close a gap; or reduce scope (fewer
regions first) to protect the support date.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight route optimizer, SaaS, Tier 2) and
[`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield NFA-500 controller,
hardware, Tier 1). The second shows the four dates pulling apart, which SaaS launches rarely see.

---

## Common Pitfalls

### Pitfall 1: Treating the Ship Date as the Launch
**Symptom:** The plan is the engineering schedule with a marketing row added at the end.
**Consequence:** Customers can buy what nobody can onboard, service, or supply. The first customers
become negative references.
**Fix:** Plan the four dates and check every function against them.

### Pitfall 2: One Checklist Size for Every Launch
**Symptom:** A small variant gets the 120-row platform checklist, or a platform gets ten rows.
**Consequence:** Teams stop taking the checklist seriously, or big launches go under-prepared.
**Fix:** Score the tier, recommend one, let the user move it. Never default to the heaviest.

### Pitfall 3: The PM Owns Every Row
**Symptom:** The owner column says "PM" all the way down, or names departments.
**Consequence:** Nothing happens on time because the people who do the work never agreed to it.
**Fix:** Every row gets a named owner from the function that does the work, who agrees the date.

### Pitfall 4: Compliance Discovered Late
**Symptom:** A certificate, security review, or country approval appears four weeks before launch.
**Consequence:** Delivery stops. No marketing fixes a product that cannot legally ship or pass a
customer's security review.
**Fix:** Put it on the critical path from the start. Ask the compliance owner what each market
needs and plan backward from their lead times.

### Pitfall 5: The Channel Hears Last
**Symptom:** Partners learn about the launch with customers, at the announcement.
**Consequence:** They can't quote, stock, or train. They keep selling the old thing, or a
competitor's.
**Fix:** Brief partners months ahead, under confidentiality if needed. Check their deadlines.

### Pitfall 6: Support Forgotten
**Symptom:** No rows for Support or Service training, runbooks, tools, or spare parts.
**Consequence:** The first problem takes weeks to fix. Promises fail and the cost of fixing rises.
**Fix:** Make "full support" a dated milestone with its own must-pass criteria.

### Pitfall 7: Criteria Written After the Fact
**Symptom:** Criteria appear in the gate deck, shaped around the current status.
**Consequence:** The gate becomes theater and real risks are rationalized away.
**Fix:** Agree must-pass and watch criteria, thresholds, and owners before the status is reviewed.

### Pitfall 8: Announcing Too Early
**Symptom:** The launch is announced long before orders open or delivery starts, with no plan for
the current product.
**Consequence:** Customers delay buying the current product. Revenue dips before the new one arrives.
**Fix:** Make the announce-to-delivery gap a deliberate decision and plan how Sales handles current deals in it.

### Pitfall 9: Invented Dates and Quantities
**Symptom:** The AI-drafted plan has confident lead times, stock levels, and owner names nobody supplied.
**Consequence:** It looks complete and is wrong. The team commits to dates nobody checked.
**Fix:** Every unagreed date, quantity, threshold, and owner is `[NEEDS SOURCE]` until a function supplies it.

### Pitfall 10: A Premortem That Changes Nothing
**Symptom:** Vivid failure stories, a better mood, and a plan that is word-for-word the same. Or AI
wrote the stories and no function owner read them.
**Consequence:** The doubts are on record and still unmanaged. The launch fails the way someone
predicted.
**Fix:** Every ranked driver ends in the plan as a criterion or an owned risk with a trigger and a
response. Stories come from the people who will run the launch.

---

## References

### Skill Files
- [`template.md`](template.md): tier assessment, four dates, checklist, criteria, scorecard, premortem, pre-approval check
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`positioning-statement`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/positioning-statement/SKILL.md): upstream; feeds marketing and sales messaging
- [`press-release`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/press-release/SKILL.md): upstream; forces the customer promise into words before launch
- [`finance-based-pricing-advisor`](../finance-based-pricing-advisor/SKILL.md): upstream; price and packaging feed the price rows
- [`roadmap-planning`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/roadmap-planning/SKILL.md): upstream; sets which launches are coming and roughly when
- [`launch-metrics`](../launch-metrics/SKILL.md): downstream; how the launch is judged after it happens, including whether the premortem's drivers showed up
- [`stakeholder-mapping`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/stakeholder-mapping/SKILL.md): for owners who have not agreed their rows
- [`decision-rights-matrix`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/decision-rights-matrix/SKILL.md): names the forum and the one approver for each gate
- [`eol-process`](../eol-process/SKILL.md): the other end of the lifecycle; a launch that replaces a product usually needs a sunset plan beside it
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Stage-gate:** Robert G. Cooper, *Winning at New Products*, the origin of gates with pre-agreed criteria.
- **DACI and RACI:** standard decision and responsibility frameworks in product and project practice, used here for the gate and for the rows.
- **Premortem:** Gary Klein, "Performing a Project Premortem," *Harvard Business Review* (2007). Facilitation steps adapted from the premortem tool in the MITRE Innovation Toolkit (itk.mitre.org).
- **Launch tiering:** common product marketing practice with no single originator; this version scores six explicit criteria.

### Provenance
Distilled from practitioner experience running cross-functional launch readiness for B2B and
industrial products.
