---
name: buying-journey-enablement
argument-hint: "[offering, who buys it, and how you sell: direct, partners, self-serve]"
description: "Map how a buying group buys, then assign the enablement asset for each stage and role, for direct sales and partners. Use when Sales has a pile of assets and customers still stall."
intent: >-
  Enable the buying, not only the selling: map the buying jobs a group must complete, what each role
  needs at each stage, and the one asset that meets it, then set what partners need, how they are
  trained and certified, and how field feedback keeps the toolkit current. Fewer, better assets.
type: workflow
theme: strategy-positioning
best_for:
  - "Building a sales enablement toolkit around how customers actually buy"
  - "Finding where target accounts stall and which asset is missing"
  - "Separating what direct sales, resellers, and integrators each need"
  - "Cutting a library of assets nobody uses"
scenarios:
  - "Deals stall after the demo. Where in the buying process are we losing them?"
  - "We have 60 sales assets. Which stage and role does each serve?"
  - "What do our distributors need that our direct reps don't?"
  - "Set up partner training and certification for the NFA-500 launch"
estimated_time: "45-90 min"
---

# Buying Journey Enablement

## Purpose

Map how your customers actually buy, and give each stage and role the asset that helps them move
forward. Then separate what direct sales, partners, and integrators need, set how partners are
trained and certified, and build the loop that brings field feedback back.

Sales enablement often starts from the seller's process: prospect, qualify, demo, propose, close.
Customers don't experience it that way. They work through buying tasks in their own order, mostly
when you're not in the room. **Enablement that helps the customer finish each buying task, including
the ones nobody from your team sees, wins more deals than enablement that only helps the rep
present.**

This is the "when and for whom" skill. [`message-house`](../message-house/SKILL.md) supplies the
words, [`sales-value-narrative`](../sales-value-narrative/SKILL.md) the story, and
[`battle-card-builder`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/battle-card-builder/SKILL.md) the card. This skill places each at the
stage where it earns its keep.

## Input

**Works best with:** The offering, who is in the buying group, and how you sell (direct, partners,
self-serve with sales assist).

**Also useful:** Win/loss notes, where deals stall, the current list of sales assets, partner
agreements, and any customer-journey work you've done.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill asks how deals really progress and where they
stall, drafts the journey as a hypothesis for you to check against win/loss evidence, and leaves
asset owners and dates as `[NEEDS SOURCE]` blanks.

**Example invocations:**
- `Buying journey for Route Optimizer. Deals stall between the demo and the CFO's sign-off.`
- `Here are our 40 sales assets. Map them to the buying journey and tell me what's missing.`

---

## Key Concepts

### The Buying Journey: Six Buying Jobs

B2B buying research commonly describes six jobs a buying group must complete. They aren't a
straight line: groups loop back, run several at once, and revisit earlier jobs when someone new
joins.

| Buying job | What the group is doing | Typical stall |
|---|---|---|
| **Problem identification** | Recognizing something must change and is worth fixing | The cost of the status quo is invisible |
| **Solution exploration** | Learning what kinds of solutions exist | They only look at what they bought last time |
| **Requirements building** | Writing what the solution must do (a spec or an RFP) | The spec is written around a competitor, or by someone you never met |
| **Supplier selection** | Shortlisting and comparing | Comparison on unlike offers; your differentiators aren't in it |
| **Validation** | Checking claims are true: references, trials, test reports | No reference in their industry; no trial possible |
| **Consensus creation** | Getting the whole group to agree and the budget approved | Each role heard a different story; finance was never addressed |

These are a planning lens, not a law. Check them against how your customers really bought, from
win/loss interviews and from Sales.

### The Buying Group at Each Stage

Roles aren't equally active at every stage. The technical evaluator may drive problem
identification and requirements; procurement may enter only at supplier selection; finance may
appear only at consensus, and then decide. The journey map shows, for each stage, **which roles are
active and what each needs to move forward**: a question answered, a risk reduced, a number they
can defend internally. See the role table in
[`sales-value-narrative`](../sales-value-narrative/SKILL.md).

### One Asset per Need

| Stage | Typical assets |
|---|---|
| Problem identification | Discovery questions for reps; cost-of-status-quo calculator; an article or webinar on the problem |
| Solution exploration | Overview by application; comparison of *types* of solution (not suppliers); a short explainer partners can share |
| Requirements building | Specification support and RFP text the customer may reuse; spec sheet; standards and security summary; integration guide |
| Supplier selection | Battle card; proposal template; total-cost comparison; demo script |
| Validation | Reference cases with written permission; trial or site-visit guide; third-party reports; ROI calculator using *their* numbers |
| Consensus creation | A business case the champion can present internally; one-page summaries per role; answers to finance and procurement questions |

Plus cross-stage assets: a **sales guide** (how to run each stage with this offering), the
narrative, and an objection sheet. **Fewer, better assets beat a large library.** For each, record
the stage, the role it serves, the channel that uses it, an owner, and an as-of date. An asset with
no stage and no role is a candidate for deletion.

### Direct Sales vs. Partners

| Need | Direct sales | Resellers and distributors | Integrators and consultants |
|---|---|---|---|
| Depth | Full narrative, account business cases, battle cards | Short, ready-to-use material they can carry beside many brands | Deep technical and integration material, spec text, interfaces |
| Why sell it | Targets and compensation | Margin, service revenue, a gap in their range, ease of selling | Project margin, fewer integration problems, a reference |
| Format | CRM-linked content, internal training | Co-branded or white-label, local language, demo access | Technical docs, configuration tools, test access |
| Support | Sales engineers, product | Partner manager, technical hotline, lead sharing | Application engineering, early access |

Write the partner version on purpose. A partner who gets the direct team's 40-slide deck will sell
what they already know.

### Training and Certification

A one-day launch event is not enablement. A workable structure has levels: a short **sales** level
(the narrative, target customer, top objections), a **technical** level (configuration,
installation or setup, commissioning), and a **support** level where partners install or maintain.
Certification tests that the partner can *do* the task, not that they attended. Tie it to something
the partner values: listing as certified, lead sharing, better margin, demo access. Plan
recertification when the offering changes.

### The Feedback Loop From the Field

The toolkit is out of date the day a competitor changes price or a new objection appears.
**Collect** (win/loss, objections heard, assets requested that don't exist, assets nobody uses,
questions partners ask the hotline); **review** on a cadence (monthly for the first six months);
**act** (update or retire assets, refresh cards, add proof, adjust training); **close the loop**
(tell the field what changed because of what they reported, or they stop reporting).

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally. For a facilitated version of the journey itself with customers, see
[`customer-journey-mapping-workshop`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/customer-journey-mapping-workshop/SKILL.md).

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not the customer journey map.** That maps the customer's experience of using the product; this maps the *buying* process. See [`customer-journey-map`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/customer-journey-map/SKILL.md).
- **Not a CRM stage definition.** It describes the customer's tasks, not your pipeline stages.
- **Not content creation.** It decides which asset is needed where; other skills build them.
- **Not a pipeline.** The stages loop; the skill is a map, not a sequence to force.

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** Artifact first: the journey map (stage, roles active, what each needs, the
stall, the asset), the asset inventory, the direct-versus-partner table, the training and
certification levels, the feedback loop. Commentary short, after. Two stages: a **working draft**
with provenance tags (`[FROM YOU]`, `[RESEARCH]`, `[AI-SUGGESTED, VALIDATE THIS]`) and
`[NEEDS SOURCE]` for owners, dates, and stall evidence; then a **committed copy** with tags removed,
followed by a ranked **Missing Assets** list and **Stall Hypotheses to Check** list.

**If the PM brings assets, critique first.** Map each existing asset to a stage and role. Name
assets with neither, stages with no asset, roles with no asset anywhere, and the partner version if
one doesn't exist. Offer additions last.

### Step 1: Confirm Scope
The offering, the buying group, direct and partner motions, and the evidence you have about how
deals really progress (win/loss, rep interviews).

### Step 2: Draft the Journey as a Hypothesis
Walk the six jobs. For each: who is active, what they need to move forward, and the typical stall
for *this* offering, tagged as a hypothesis until checked against win/loss.

### Step 3: Assign the Asset
One asset per need, using what exists first. Mark each with the stage, role, channel, owner, and
as-of date. Mark gaps and candidates for deletion.

### Step 4: Split Direct From Partner
Complete the table. Write what partners need on purpose.

### Step 5: Set Training and Certification
Levels, what's tested, what partners get in return, and when recertification happens.

### Step 6: Build the Feedback Loop
What's collected, who reviews, how often, and how the field is told what changed.

### Step 7: Hand Back
Short summary (supplied, inferred, unknown) and a numbered ladder, evidence-favored first, labeled
`(Recommended)`: check the stall hypotheses against ten recent win/loss deals; build the one
missing asset at the stage where most deals stall; write the partner version; or retire the assets
that serve no stage.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight Route Optimizer, SaaS) and
[`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield NFA-500, hardware with
partners). Both found that the largest gap was an asset for a role the team never sells to.

---

## Common Pitfalls

### Pitfall 1: Enabling the Seller's Process
**Symptom:** Assets are organized by prospect, qualify, demo, propose, close.
**Consequence:** Nothing helps the customer when no rep is in the room.
**Fix:** Organize by the buying jobs the group must complete.

### Pitfall 2: The Journey as a Straight Line
**Symptom:** The map forces one stage after another.
**Consequence:** It breaks the first time a new stakeholder joins late and reopens requirements.
**Fix:** Treat stages as loops and note which can run in parallel.

### Pitfall 3: A Library, Not a Toolkit
**Symptom:** Sixty assets, none tagged to a stage or role.
**Consequence:** Reps can't find them and customers see mixed messages.
**Fix:** Tag every asset with stage, role, channel, owner, and date. Delete the rest.

### Pitfall 4: Skipping Finance and Procurement
**Symptom:** Every asset speaks to the user and the technical evaluator.
**Consequence:** Deals stall at consensus, where finance finally appears.
**Fix:** Give consensus creation and supplier selection their own assets and role summaries.

### Pitfall 5: One Version for Partners
**Symptom:** Partners get the direct team's deck.
**Consequence:** They sell what they already know.
**Fix:** A short, partner-shaped version that says why it's good for their business.

### Pitfall 6: Training Without Certification
**Symptom:** One launch event, attendance counted.
**Consequence:** Partners attend and still can't configure or install.
**Fix:** Levels that test the task, tied to something the partner values.

### Pitfall 7: No Feedback Loop
**Symptom:** The toolkit was built at launch and never touched.
**Consequence:** A year later it contradicts the price list and ignores the new objection.
**Fix:** Collect, review monthly, act, and tell the field what changed.

### Pitfall 8: Stall Hypotheses Treated as Facts
**Symptom:** The journey map was drafted from assumption and shipped.
**Consequence:** The team builds assets for stalls that don't happen.
**Fix:** Check each stall against win/loss before building.

---

## References

### Skill Files
- [`template.md`](template.md): journey map, asset inventory, partner table, certification, feedback loop
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`message-house`](../message-house/SKILL.md): upstream; the words
- [`sales-value-narrative`](../sales-value-narrative/SKILL.md): upstream; the story and objections
- [`battle-card-builder`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/battle-card-builder/SKILL.md): builds the supplier-selection card
- [`customer-journey-mapping-workshop`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/customer-journey-mapping-workshop/SKILL.md): the facilitated customer-experience journey
- [`acquisition-channel-advisor`](../acquisition-channel-advisor/SKILL.md): which channels to sell through in the first place
- [`launch-plan`](../launch-plan/SKILL.md): the plan's sales and channel rows depend on this
- [`launch-metrics`](../launch-metrics/SKILL.md): funnel metrics reveal where buyers stall
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Buying jobs:** the six-job model of B2B buying, from Gartner buyer research (problem identification, solution exploration, requirements building, supplier selection, validation, consensus creation). Check it against your own win/loss.

### Provenance
Distilled from practitioner experience building sales and channel enablement for B2B and industrial offerings.
