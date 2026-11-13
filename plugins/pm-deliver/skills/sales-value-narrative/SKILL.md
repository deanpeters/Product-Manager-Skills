---
name: sales-value-narrative
argument-hint: "[offering, who you sell to, and the alternative you most often lose to]"
description: "Build a sales value narrative: why change, why now, why us, value by buying-group role, objections, and a do-not-say list. Use when Sales or partners must explain value with claims they can defend."
intent: >-
  Give Sales and partners a short story the customer can retell inside their own company, from the
  cost of staying put to a better outcome, with proof for every claim and a prepared answer for the
  objections reps actually hear. Hands the one-page competitive card to battle-card-builder.
type: component
theme: strategy-positioning
best_for:
  - "Enabling Sales or partners to explain value to a group of buyers, not one champion"
  - "Starting with why change and why now instead of a feature tour"
  - "Preparing objection answers from what reps really hear"
  - "Giving reps a do-not-say list that protects deals and credibility"
scenarios:
  - "Reps open with features and lose to 'we'll just keep what we have'. Build the narrative"
  - "Our resellers need a story they can tell in ten minutes. What goes in it?"
  - "Write the objection handling for 'too expensive' and 'we'll wait until next budget'"
  - "Review our sales deck. I think it's a product tour"
estimated_time: "30-45 min"
---

# Sales Value Narrative

## Purpose

Build the story Sales and partners tell: **why change, why now, why us**, then the value for each
person in the buying group, the proof behind each claim, prepared answers to the objections reps
actually hear, and a short **do-not-say** list. The test of a good narrative is whether your
champion can retell it to people you will never meet.

It builds on the [`message-house`](../message-house/SKILL.md) (the pillars become the spine of
"why us") and feeds [`buying-journey-enablement`](../buying-journey-enablement/SKILL.md) (which says
*when* each piece gets used). The one-page competitive card is built by
[`battle-card-builder`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/battle-card-builder/SKILL.md); this skill tells you what the card needs
from the narrative.

## Input

**Works best with:** The offering, who you sell to (the roles in the buying group), and the
alternative you most often lose to, which is often "do nothing."

**Also useful:** The message house, win/loss notes, the objections reps hear (from reps, not from
the product team), proof you hold, and pricing and packaging.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill asks who buys and what usually beats you, then
drafts the narrative as labeled hypotheses with every proof point and number left as a
`[NEEDS SOURCE]` blank.

**Example invocations:**
- `Sales narrative for Route Optimizer. We lose to "our dispatchers manage fine in spreadsheets."`
- `Objection handling for the NFA-500: price, switching risk, and "our current supplier is fine."`

---

## Key Concepts

### Narrative, Not Feature Tour

A feature tour starts at your product and leaves the customer to work out why it matters. A
narrative starts at the customer's situation and moves to a better outcome, with your offering as
the way there. In a group purchase the person you're talking to has to sell the decision internally.
Give them a story they can retell.

### Why Change, Why Now, Why Us (in that order)

1. **Why change?** What does the status quo cost? The strongest competitor is usually *doing
   nothing*: the spreadsheet, the old machine, the current supplier. Show the cost of staying put
   in the customer's terms (hours, downtime, errors, risk, compliance).
2. **Why now?** What makes delay expensive? A trigger: a regulation, a renewal date, an aging
   system losing support, rising cost, a new site, an audit. Without a why-now, deals slip to next
   year's budget.
3. **Why us?** What can you do that the alternatives can't, that matters to *this* customer, and
   that they can verify? Differentiation they can't check is a claim, not a reason.

Most sales material starts with "why us," which skips the two questions the customer has to answer
first.

### The Buying Group

Most purchases are decided by a group. Each role weighs different value and fears different risk:

| Role | Typical people | Cares about | Fears |
|---|---|---|---|
| **User** | Dispatchers, operators, technicians | Easier daily work, reliability | More work, being blamed when it fails |
| **Buyer** | Procurement | Price, terms, supplier risk, comparable offers | Overpaying, an unreliable supplier |
| **Technical evaluator** | IT, security, engineering, maintenance | Integration, standards, security, supportability | Integration failure, non-compliance |
| **Finance** | Controller, CFO | Payback, total cost, budget fit | An investment that doesn't pay back, hidden costs |
| **Sponsor** | VP, plant or operations head | The outcome they own | A failed project with their name on it |

Add **gatekeepers** and **influencers** (consultants, integrators) when they matter. In channel
sales the partner is a role too: they need a reason to sell you instead of another brand. Write
value **per role**. If every role gets the same message, it's generic.

### Proof: Sourced or Flagged

A claim without proof is an opinion. Strongest first: independent test or certification; named
reference with written permission; measured result from a pilot or installed base; internal test
with the method available; a calculation the customer can repeat with their own numbers; an
unsupported claim (not proof). Every proof point is sourced or `[NEEDS SOURCE]`. **Never invent
proof**: no made-up customers, quotes, percentages, or awards. A rep who repeats one invented claim
to a technical evaluator loses the deal and the credibility. Comparative claims about a named
competitor carry legal risk; have Legal review them before they leave the building.

### Objection Handling

Objections are information. The structure: **Acknowledge** without arguing; **Clarify** what's
behind it ("too expensive" can mean over budget this year, more than a competitor's quote, or "I
don't believe the savings"); **Respond** with proof matched to the real concern; **Confirm** it
answered. Prepare answers for the objections Sales actually hears, collected from reps, partners,
and win/loss reviews, not the ones the product team would like to answer. Common ones: price,
switching risk, compatibility with what they have, "our current approach is fine," support coverage,
security, and "we'll wait for next budget."

### Trap Questions and the Do-Not-Say List

A **trap question** leads the customer to discover a weakness in the alternative. It's safe only
when you hold the documented answer. Never ask what you can't evidence: a trap built on a guess
hands the competitor the stage. A **do-not-say list** protects reps from claims that are outdated,
unprovable, or invite a counter. Teams skip it most, and it saves the most deals.

### The Narrative and the Battle Card

The narrative stays the same across competitors. What changes per alternative that keeps winning
(each named competitor, plus the status quo) is the traps, the proof, and the do-not-say list, and
that is the **battle card**: one page, thirty seconds, with an as-of date, because competitive facts
go stale. Use [`battle-card-builder`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/battle-card-builder/SKILL.md) to research and draft each
card from public evidence. This skill supplies the story and the objections it rests on.

### Enablement Is Collaboration

The PM brings the value logic, proof, and competitive facts. Sales brings what customers really say
and what works in the room. Partners bring what their people can carry beside a dozen other brands.
Build it with them, test it with two or three reps on real accounts, and revise. A narrative the PM
writes alone and hands over at a launch event is rarely used.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not a pitch deck.** It is the story and logic a deck should follow.
- **Not messaging architecture.** That is the [`message-house`](../message-house/SKILL.md).
- **Not a battle card.** See [`battle-card-builder`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/battle-card-builder/SKILL.md).
- **Not invented proof.** Every claim is sourced or flagged.

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** Artifact first: scope, why change / why now / why us, value by role, proof,
objections, traps, do-not-say, what each competitor card needs. Commentary short, after. Two
stages: a **working draft** where every line carries a provenance tag (`[FROM YOU]`, `[RESEARCH]`,
`[AI-SUGGESTED, VALIDATE THIS]`) and unsupported proof is `[NEEDS SOURCE]`; then a **committed
copy** with tags removed, followed by a ranked **Proof to Gather** list and the **Questions to Ask
Reps** list.

**If the PM brings a deck or narrative, critique first.** Does it open with why us? Is the status
quo named as a competitor? Is there a why-now? Is value written per role? Is every claim sourced,
and every comparison cleared by Legal? Are the objections ones reps actually hear? Is there a
do-not-say list? Name gaps; offer rewrites last.

### Step 1: Confirm Scope
The offering, the roles in the buying group, the sales motion (direct, partner, self-serve with
sales assist), and the alternatives that win, including the status quo.

### Step 2: Cost of the Status Quo
In the customer's terms, with a source or `[NEEDS SOURCE]`. Offer a calculation they can repeat
with their own numbers.

### Step 3: Why Now
Name the trigger events that make delay expensive for this segment, and how a rep spots them.

### Step 4: Why Us, From the Message House
Take the pillars and proof. If no house exists, draft the differentiators and note that other
material may drift from them.

### Step 5: Value by Role
One short block per role: what they care about, the value in their terms, the proof they trust, the
risk to defuse.

### Step 6: Objections, Traps, and Do-Not-Say
Collect real objections from reps. Write acknowledge-clarify-respond-confirm answers. Add trap
questions only where you hold the evidence. Write the do-not-say list.

### Step 7: Hand Off and Hand Back
Note which competitors and status-quo patterns each need a card (point to
[`battle-card-builder`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/battle-card-builder/SKILL.md)), and where each piece is used (point to
[`buying-journey-enablement`](../buying-journey-enablement/SKILL.md)). Close with a short summary
and a numbered ladder, evidence-favored first, labeled `(Recommended)`: test it with two reps on
live deals; gather the missing proof; build a card for the status quo first; or write the partner
version.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight Route Optimizer, SaaS) and
[`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield NFA-500, hardware).

---

## Common Pitfalls

### Pitfall 1: Starting With Why Us
**Symptom:** The deck opens with company history and features.
**Consequence:** The customer never agrees there is a problem worth solving.
**Fix:** Open with the cost of the status quo, then why now, then why us.

### Pitfall 2: Ignoring "Do Nothing"
**Symptom:** The narrative compares only against named competitors.
**Consequence:** You lose to the spreadsheet or the old machine.
**Fix:** Name the status quo as a competitor and price it.

### Pitfall 3: One Message for Every Role
**Symptom:** The same value statement goes to the user, the buyer, and finance.
**Consequence:** It speaks to none of them.
**Fix:** Write value per role with the proof that role trusts.

### Pitfall 4: Objections From the Product Team
**Symptom:** The objection list is what the product team wishes customers asked.
**Consequence:** Reps meet the real objection with no answer.
**Fix:** Collect from reps, partners, and win/loss.

### Pitfall 5: Traps Built on Guesses
**Symptom:** A rep asks a trap question about a competitor weakness nobody verified.
**Consequence:** The customer or the competitor corrects them, in public.
**Fix:** Ask only what you can evidence.

### Pitfall 6: No Do-Not-Say List
**Symptom:** Reps repeat last year's claims.
**Consequence:** Outdated or unprovable claims reach technical buyers.
**Fix:** Keep a short, dated do-not-say list.

### Pitfall 7: Invented Proof
**Symptom:** AI-drafted narrative with confident percentages and customer names.
**Consequence:** One false claim loses the deal and the credibility.
**Fix:** Sourced or `[NEEDS SOURCE]`. Never invent.

### Pitfall 8: Written Alone, Handed Over at Launch
**Symptom:** The PM writes it and presents it once.
**Consequence:** Nobody uses it.
**Fix:** Build it with reps and partners and test it on live accounts.

---

## References

### Skill Files
- [`template.md`](template.md): narrative, roles, objections, traps, do-not-say
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`message-house`](../message-house/SKILL.md): upstream; pillars and proof become "why us"
- [`battle-card-builder`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/battle-card-builder/SKILL.md): builds the one-page card per alternative
- [`competitive-research-snapshot`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/competitive-research-snapshot/SKILL.md): upstream evidence for competitive claims
- [`buying-journey-enablement`](../buying-journey-enablement/SKILL.md): where each piece is used, by whom
- [`positioning-statement`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/positioning-statement/SKILL.md): upstream anchor
- [`launch-plan`](../launch-plan/SKILL.md): the plan's sales readiness rows depend on this
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Buying group and buying jobs:** common B2B sales research on committee purchasing.
- **Objection handling (acknowledge, clarify, respond, confirm):** standard sales practice with no single originator.

### Provenance
Distilled from practitioner experience enabling sales and partner teams on B2B and industrial offerings.
