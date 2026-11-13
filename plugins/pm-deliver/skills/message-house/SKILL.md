---
name: message-house
argument-hint: "[offering, target customer, and your positioning if you have it]"
description: "Build a message house: one roof message, three value pillars, sourced proof, a foundation, and role and channel variants. Use when Marketing, Sales, and partners each tell a different story."
intent: >-
  Give everyone who speaks about the offering one consistent, customer-tested value story built on
  real customer pains and gains and backed by proof, so the market hears value instead of a feature
  list. Turns a positioning statement into words customers will read, without inventing proof.
type: component
theme: strategy-positioning
best_for:
  - "Turning a positioning statement into customer-facing messages before a launch"
  - "Aligning Marketing, Sales, and partners on one value story"
  - "Adapting one core message for different buying-group roles and channels"
  - "Reviewing messaging for feature lists, superlatives, and claims nobody can prove"
scenarios:
  - "Our website, deck, and sales email all say different things. Build one messaging framework"
  - "We have a positioning statement. How do we say it to a dispatcher versus a CFO?"
  - "Review our messaging. I think our three pillars are just three features"
  - "Build the message house for a new variable-speed controller line"
estimated_time: "30-45 min"
---

# Message House

## Purpose

Build a **message house**: the one thing you want customers to remember (the roof), the value
themes that hold it up (the pillars), the proof under each theme, the credibility facts the whole
house stands on (the foundation), plus variants by buying-group role and channel, words to use and
avoid, and a plan to test it with real customers.

It sits between strategy (positioning, jobs, pains and gains) and the material people actually use
(web page, deck, brochure, partner kit). It is the source copywriters write *from*, not the final
copy. The failure it prevents: a message house whose pillars are three features, so customers hear
a spec sheet and nobody sees why it matters.

## Input

**Works best with:** The offering, the target customer, and your positioning statement if you have
one.

**Also useful:** The customer's top pains and gains (from interviews or [`jobs-to-be-done`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/jobs-to-be-done/SKILL.md)),
proof you already hold (tests, references, measured results), your current messaging, and the
channels you speak through.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill asks who the customer is and what they are
trying to get done, drafts pillars as labeled hypotheses, and leaves every proof point as a
`[NEEDS SOURCE]` blank. It will not invent a customer, a quote, or a number.

**Example invocations:**
- `Message house for the Route Optimizer. Positioning: for dispatchers at 50-300 tech field service companies...`
- `Review these three pillars: variable speed drive, IoT connectivity, compact design.`

---

## Key Concepts

### What a Message House Is

| Part | Holds | Test |
|---|---|---|
| **Roof** | One umbrella value message | Can a customer repeat it after one reading? Is it value, not a feature? |
| **Pillars** (about three) | Value themes, each tied to a top customer pain or gain | Does each name an outcome the customer cares about? Are the three distinct? |
| **Proof points** (under each pillar) | Evidence: tests, references, measured results, a calculation the customer can repeat | Is each sourced, or flagged `[NEEDS SOURCE]`? |
| **Foundation** | Facts that make any claim believable: time in market, installed base or customer count, service network, certifications, security attestations | True today and verifiable? Facts, not adjectives? |

Three pillars is a habit, not a law. Two strong pillars beat four weak ones. More than four and
nobody remembers any.

### Start From the Customer, Not the Spec Sheet

Pillars come from the customer's side: the jobs, the top pains, and the top gains, where the
offering is also genuinely strong. The pillar names the outcome; the features are the reason it's
true.

| Feature pillar (drift) | Value pillar |
|---|---|
| Variable speed drive | Pay for the air you use, not the air you waste |
| Real-time GPS and routing engine | Fit the emergency job in without wrecking the day |
| Compact design | Fits the cabinet you already have |

**The cover test:** cover the product name. If a competitor's data sheet could produce the same
pillar, it's a feature posing as a pillar.

### Link to Positioning and to Jobs, Pains, and Gains

The roof must agree with the [`positioning-statement`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/positioning-statement/SKILL.md): same
target, same category, same main benefit. Each pillar should trace to a specific pain or gain, and
each proof point to evidence. Keep the trace visible in the artifact so anyone who later changes a
message can see what it rests on.

### Proof: Sourced or Flagged

Proof turns a claim into a reason to believe. Strongest first: independent test or certification;
a named customer reference with written permission; a measured result from a pilot or installed
base; an internal test with the method available; a calculation the customer can repeat with their
own numbers. An unsupported claim is not proof. A pillar with no proof is a hypothesis and stays
out of external material until the proof exists.

### Superlatives Need Proof Too

"Leading," "best-in-class," "most efficient," "unique," "first": each is a claim of fact. Technical
buyers discount them, and unverifiable comparative claims carry legal risk. Use one only when you
can name the basis (tested by whom, against what, under which standard) and Legal has cleared it.
Otherwise say the specific thing: "cuts dispatcher rescheduling time by [X]%, measured across 14
pilot accounts" beats "the smartest scheduler" if the pilot exists, and if it doesn't, neither
belongs in the house.

### Variants by Role and by Channel

The roof and pillars stay the same. Emphasis and words change.

- **By role.** The day-to-day user hears the pillar as daily work; the technical evaluator as
  integration, reliability, and security; procurement as total cost and supplier risk; finance as
  payback; the sponsor as the outcome they own. A variant reorders and rewords pillars and picks the
  proof that role trusts. **It never adds a new pillar for one role.**
- **By channel.** Partners and resellers need short messages they can carry beside many brands, plus
  why this is good for *their* business. Integrators need technical proof. The web and events need a
  headline and one proof each. Support and service need words they can use on a call or on site.

### Words to Use, Words to Avoid

A short shared vocabulary keeps the house consistent. **Use:** the customer's own words for their
pains and gains, taken from interviews, sales calls, and support tickets. **Avoid:** internal
jargon, unproven superlatives, and terms the customer doesn't use. Mark words from real customers
as such.

### Test With Real Customers

A message house is a hypothesis until customers react to it. Plan the test: which messages, which
customers (five to eight from the target segment), how (read the roof and pillars aloud and ask
what they heard, what they believe, and what they doubt), and what result changes the house. Record
what customers *repeat back*, not whether they said they liked it.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not positioning.** Positioning is the internal strategic anchor. The house turns it into customer language.
- **Not the sales story.** The narrative, objections, and battle cards live in [`sales-value-narrative`](../sales-value-narrative/SKILL.md).
- **Not copywriting.** It's the source copywriters write from, not the ad or web page.
- **Not a source of proof.** It organizes proof you have and flags proof you need.

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** Artifact first: scope, roof, pillars with their trace to pains and gains,
proof under each, foundation, role variants, channel variants, words to use and avoid, test plan.
Commentary short, after. Two stages: a **working draft** where every line carries a provenance tag
(`[FROM YOU]`, `[RESEARCH]`, `[AI-SUGGESTED, VALIDATE THIS]`) and every unsupported proof point is
`[NEEDS SOURCE]` with the type of proof needed; then a **committed copy** with tags removed,
followed by a ranked **Proof to Gather** list and a **Messages to Test** list.

**If the PM brings a draft, critique first.** Is the roof one idea, in customer language, and
consistent with positioning? Apply the cover test to each pillar. Does each pillar trace to a
specific pain or gain? Quote every unsupported claim and every superlative. Is the foundation
facts or adjectives? Do variants keep the same pillars? Has any of it been tested? Name gaps;
offer rewrites last.

### Step 1: Confirm Scope
The offering, the target customer, the positioning (or note its absence), the roles in the buying
group, the channels. Ask what is software, what is physical, what is service, so the foundation and
proof fit the real offering.

### Step 2: Gather the Customer's Pains and Gains
From interviews, jobs work, support tickets, win/loss notes. Pick the few that matter most to the
customer *and* where you are genuinely strong. Anything you draft yourself is a hypothesis.

### Step 3: Draft the Roof, Pillars, and Trace
Roof first (one idea). Then pillars as outcomes, each with the pain or gain it traces to. Run the
cover test on each.

### Step 4: Attach Proof and Build the Foundation
Proof under each pillar, ranked by strength, sourced or flagged. Foundation as verifiable facts.
Flag every superlative for proof and Legal review.

### Step 5: Write Variants and Vocabulary
One variant per role that matters and per channel in use, same pillars. Words to use (with their
source) and words to avoid.

### Step 6: Plan the Test and Hand Back
Who to test with, what to ask, and what result changes the house. Close with a short summary
(supplied, inferred, unknown) and a numbered ladder, evidence-favored first, labeled
`(Recommended)`: gather the missing proof; test the roof with five customers; reconcile existing
assets to the house; or build the sales narrative on top.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight Route Optimizer, SaaS) and
[`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield NFA-500, hardware).
Both show a feature-pillar draft rebuilt as value pillars.

---

## Common Pitfalls

### Pitfall 1: Feature Pillars
**Symptom:** Pillars read like a data sheet: speed, connectivity, size.
**Consequence:** Customers hear specs, not reasons to care.
**Fix:** Name the outcome the customer gets. Apply the cover test.

### Pitfall 2: Pillars With No Trace
**Symptom:** Nobody can say which customer pain a pillar answers.
**Consequence:** The house reflects what the company likes about itself.
**Fix:** Record the pain or gain behind each pillar and where it was heard.

### Pitfall 3: Unproven Superlatives
**Symptom:** "Best-in-class," "most reliable," "the only."
**Consequence:** Technical buyers discount you; legal risk follows.
**Fix:** Name the basis and clear it with Legal, or say the specific measured thing.

### Pitfall 4: A New Message for Every Role
**Symptom:** Each role gets its own pillars.
**Consequence:** The market hears five stories and the roof means nothing.
**Fix:** Same pillars, different emphasis and proof.

### Pitfall 5: The Foundation Is Adjectives
**Symptom:** "Trusted," "innovative," "world-class."
**Consequence:** Nothing for the customer to verify.
**Fix:** Years, counts, certifications, attestations, coverage, each true today.

### Pitfall 6: Untested Messaging
**Symptom:** The house was approved internally and shipped.
**Consequence:** It may persuade the room that wrote it and no one else.
**Fix:** Test with five to eight target customers and record what they repeat back.

### Pitfall 7: Invented Proof
**Symptom:** An AI-drafted house arrives with confident percentages, quotes, and customer names.
**Consequence:** One false claim repeated to a technical buyer loses the deal and the credibility.
**Fix:** Every proof point is sourced or `[NEEDS SOURCE]`. Never invent a customer or a number.

---

## References

### Skill Files
- [`template.md`](template.md): the house, trace, proof, variants, vocabulary, test plan
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`positioning-statement`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/positioning-statement/SKILL.md): upstream; the roof must agree with it
- [`positioning-workshop`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/positioning-workshop/SKILL.md): upstream; the facilitated version
- [`jobs-to-be-done`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/jobs-to-be-done/SKILL.md) and [`proto-persona`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/proto-persona/SKILL.md): upstream; the pains and gains pillars rest on
- [`sales-value-narrative`](../sales-value-narrative/SKILL.md): downstream; the sales story built on the pillars
- [`launch-plan`](../launch-plan/SKILL.md): the plan's marketing rows draw on the house
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Message house:** a widely used communications structure (roof, pillars, foundation) with no single originator.
- **Jobs, pains, gains:** Alexander Osterwalder et al., *Value Proposition Design*.

### Provenance
Distilled from practitioner experience building value messaging for B2B and industrial offerings.
