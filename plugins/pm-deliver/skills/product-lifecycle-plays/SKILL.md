---
name: product-lifecycle-plays
argument-hint: "[product or product line, and the signal that something needs to change]"
description: "Map a product's lifecycle stage and choose between extension, replacement, and retirement plays. Use when a product is maturing or declining and the next move isn't obvious."
intent: >-
  Diagnose where a product sits in the Product Life Cycle and choose deliberately among the three
  plays available at the decline inflection — extend the product, replace it with a successor, or
  retire it. Includes the mature-to-declining transition questions, the seven replacement hazards
  with a risk register, and a portfolio worksheet for deciding across a product line.
type: component
theme: product-lifecycle
best_for:
  - "Deciding whether a fading product should be extended, replaced, or retired"
  - "Diagnosing whether a product has actually crossed from mature into decline"
  - "Running the play decision across a whole product line, not one product at a time"
scenarios:
  - "Revenue is flattening on our flagship and people are arguing about a rewrite versus a refresh"
  - "We have four aging SKUs and no consistent way to decide what happens to each"
estimated_time: "25-45 min"
---

# Product Lifecycle Plays

## Purpose

Decide what to do with a product that has stopped growing. There are three plays — **extend**,
**replace**, **retire** — and picking the wrong one is expensive in a different way each time. This
skill gives you the stage diagnosis, the criteria that discriminate the plays, and the hazard
register for the one that goes wrong most often.

Most teams skip straight to a play. Someone says "let's rebuild it" or "let's kill it," and the
argument that follows is about the answer rather than the diagnosis. The diagnosis is the work.

## Input

**Works best with:** The product or product line, and the signal that prompted the question —
flattening revenue, rising support costs, a competitor move, a strategy shift.

**Also useful:** Revenue and margin trend, customer counts and concentration, support load, what
else in the portfolio is adjacent, and how much investment appetite exists.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it
covers; don't re-ask.

**Arriving empty-handed? That works too.** Bring the product name and a hunch. The stage diagnosis
runs off the transition questions below, which are answerable from what a PM already knows without
pulling a report.

**Example invocations:**
- `Revenue on our reporting module has been flat for six quarters — extend, replace, or retire?`
- `Run the play worksheet across our four aging SKUs.`

---

## Key Concepts

### The Product Life Cycle

Five stages, each with a different economic job:

| Stage | What's happening | The job |
|---|---|---|
| **Design** | Concept, prototype, launch planning | Prove the problem is real |
| **Introduce** | Launch, awareness, first sales | Find the early adopters |
| **Grow** | Rapid sales, market expansion | Build the customer base |
| **Mature** | Peak sales, peak profitability | Defend position, maximize margin |
| **Decline** | Falling sales, phase-out planning | Maximize remaining value |

**Go-to-market happens at the front. End-of-life happens at the back. The plays live at the
mature-to-decline inflection** — which is exactly where most teams have no framework and default to
whoever argues hardest.

### The Strategy Grid

What "good" looks like changes by stage. Each lever tells you something different about where you
actually are:

| Lever | Mature | Declining |
|---|---|---|
| Marketing objective | Defend market position | Maximize remaining value |
| Competition | Emphasize brand loyalty | Consolidate customer base |
| Product | Optimize | Extended CX, streamline support |
| Promotion | Loyalty incentives | Migration campaigns |
| Place (distribution) | Optimize channels | Focus on profitable channels |
| Price | Value-add bundles | Selective discounting |
| Data strategy | Predictive modeling | Transition planning data |

### The Transition Questions

**This is the diagnostic.** For each lever, ask the question that tells you whether you've crossed
from mature into decline. Answering "yes" to four or more means you are in decline regardless of
what the revenue chart says this quarter:

| Lever | Ask |
|---|---|
| Marketing objective | Is defending market share still profitable? |
| Competition | Are loyalty efforts no longer retaining users? |
| Product | Are legacy support costs becoming unsustainable? |
| Promotion | Should we be running migration campaigns instead of loyalty ones? |
| Place | Are we losing money on certain distribution channels? |
| Price | Are our value-add bundles losing effectiveness? |
| Data strategy | Is our data shifting from predictive to transitional? |

**Why ask rather than measure:** revenue lags. A product can post a flat quarter while every one of
these has already turned. The questions catch the inflection before the chart does.

### The Three Plays

**Extension Play** — introduce a new variant or additional features to an existing product line.

*Reasons why:* expand into new customer segments · meet diverse customer needs · differentiate from
competitors · boost sales with new variants · strengthen brand loyalty.

*Shape:* the existing product keeps running; you add alongside. Cheapest play, lowest risk, and the
one most often dismissed because it isn't exciting.

**Replacement Play** — introduce a new product to take the place of an existing one, offering
similar or improved capability while phasing the old one out.

*Reasons why:* address supply issues · reduce production costs · eliminate obsolete or unused
features · align with strategic goals · comply with regulatory change.

*Shape:* **GTM and EOL happen simultaneously.** This is the expensive play, and the reason is
structural — see below.

**Retirement Play** — phase the product out without a successor of your own.

*Reasons why:* costs exceed revenue · strategic exit from the market · the core problem stopped
existing · technology made it obsolete.

*Shape:* pure EOL. Customers land somewhere else, possibly a competitor, and the goal becomes
losing the product without losing the customer.

### Why Replacement Is the Expensive Play

On a replacement you are running a **launch and a retirement at the same time, for two products
that compete with each other.** Every GTM risk and every EOL risk applies at once, plus one that
only exists here: cannibalization between your own two products.

Both directions of that failure are instructive:
- **Kodak** feared cannibalizing film and starved its digital business. The fear cost the market.
- **Amgen** cannibalized Epogen with Aranesp deliberately. It worked, and still produced complex
  pricing dynamics they had to manage for years.

Fear it and you lose the future; ignore it and you lose margin. Plan for it and you get a
transition.

### The Seven Replacement Hazards

What goes wrong on a replacement play, with the pattern each one leaves:

| # | Hazard | Pattern |
|---|---|---|
| 1 | **GTM process failure** | The successor exists but nobody adopts it (Zune) |
| 2 | **Delayed market entry** | Late launch lets competitors define the category (BlackBerry) |
| 3 | **Internal misalignment** | Siloed R&D, marketing, and sales blunt the launch (New Coke) |
| 4 | **External forces** | Backlash, safety, or macro shocks force withdrawal (Google Glass) |
| 5 | **Regulatory risk** | Compliance missed, or the successor triggers new obligations |
| 6 | **Unexpected cannibalization** | The two products fight each other (Kodak, Amgen) |
| 7 | **Poor EOL management** | The successor lands but the old product's exit is botched (Vista, AT&T POTS, Nest Revolv) |

**Hazard 7 is the one this repo's EOL suite exists to prevent** — and it's the one teams discount
most, because by the time they're planning the launch, the retirement feels like paperwork.

### The Risk Register

For each hazard that applies, fill five columns. The fifth is the one people skip:

| Risk | Probability | Impact | Mitigation | Contingency |
|---|---|---|---|---|
| What could adversely affect the business case? | How likely? | How bad? | How do we reduce the probability? | **What is Plan B?** |

A register with no contingency column is a worry list. Plan B is what makes it a plan.

### Anti-Patterns (what this is NOT)
- **Not a growth framework.** Where the next tranche of growth comes from is a different question —
  see `ansoff-matrix` and `organic-growth-advisor`.
- **Not a forecast.** It reasons about stage and direction, not numbers.
- **Not automatic.** Decline is not a death sentence; a mature product throwing off margin with low
  support cost is a harvest, not a project.
- **Not one product at a time, necessarily.** The worksheet runs across a line, and the plays
  interact — two products can't both be the replacement.

---

## Application

Use `template.md` for the worksheet and risk register.

### Step 1: Diagnose the stage

Run the seven transition questions. Count the yeses:

- **0-1 yes** — mature and healthy. The question isn't a play, it's whether to invest more
- **2-3 yes** — mature and softening. Extension play territory; watch quarterly
- **4-5 yes** — crossing into decline. Pick a play deliberately, now
- **6-7 yes** — in decline. Replace or retire; extension likely postpones a decision rather than
  changing an outcome

Write down which questions came back yes. The *pattern* discriminates the plays more than the count
does.

### Step 2: Identify what's driving the pressure

Three sources, and they point at different plays:

| Pressure | Signal | Points toward |
|---|---|---|
| **Demand-side** | Needs shifted, segments moved, competitors differentiated | **Extend** — if the core still solves a real problem for someone |
| **Supply/cost-side** | Components EOL, production cost, support load, strategy shift | **Replace** — the problem is your economics, not the customer's need |
| **Capability-side** | Technology obsolete, architecture at its limit, regulation changed | **Replace** or **Retire** — depends on whether the need survives the technology |

**The trap:** supply-side pressure feels like a customer problem when it reaches the roadmap. "We
need to rebuild this" often means "our costs are bad," which is a legitimate reason for a
replacement — but say it out loud, because it changes what success looks like.

### Step 3: Test the extension play first

Extension is the cheapest play and the most frequently skipped. Before accepting replace or retire,
ask:

1. Is there a **segment** the current product could serve with a variant?
2. Is there a **need** an added capability would meet without re-architecture?
3. Would a **repackage or rebrand** reach a different buyer?
4. Is the decline in the *product*, or in the *channel* or *price* around it?

Question 4 catches a specific and common error: a product judged to be declining when the actual
failure is a distribution channel that stopped working or a bundle that lost its edge. Fixing the
lever is cheaper than replacing the product.

If the honest answer to all four is no, extension is off the table — and now you know why, which
you'll need when someone asks in three months.

### Step 4: If replacing, build the risk register before committing

Walk the seven hazards. For each one that applies, fill all five columns including the contingency.
Rate probability and impact honestly — a register where everything is "low/low" was filled in to be
finished.

Two questions worth forcing:
- **Cannibalization:** which product wins which customer, and what happens to margin during overlap?
- **Hazard 7:** who owns the retirement, and is it funded? A replacement with an unfunded EOL is a
  launch with a liability attached.

### Step 5: If retiring, hand off

The retirement play is a full process of its own. Confirm the two things that most often turn out
to be false — that there's a landing place for customers, and that no contractual or regulatory
obligation blocks the timeline — then move to the EOL suite.

### Step 6: Run it across the line

For a product family, build the portfolio worksheet: every product, its stage, its yes-count, its
pressure source, and its recommended play. Then check the interactions:

- Two products can't both be the replacement for the same customers
- An extension on one product can undercut the case for another's replacement
- Retiring two adjacent products in the same window doubles the customer's disruption, not yours

### Final Step: Offer what comes next

"Where next?

1. **Talk through the diagnosis** — see [`lifecycle-play-advisor`](../lifecycle-play-advisor/SKILL.md)
   if you'd rather be walked through the questions (Recommended)
2. **Run the retirement** — see [`eol-process`](../eol-process/SKILL.md) or
   [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md)
3. **Plan the extension** — see [`organic-growth-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/organic-growth-advisor/SKILL.md) for
   which growth path the variant serves
4. **Build the risk register** for a replacement play in depth

Reply with a number, a combination, or your own path."

---

## Examples

- `examples/sample.md` — Fieldlight product line (SaaS, four modules, three different plays)
- `examples/sample-industrial.md` — Northfield Automation controller line (industrial, a
  replacement play with the risk register that predicted what actually went wrong)

---

## Common Pitfalls

### Pitfall 1: Arguing the Play Before the Diagnosis
**Symptom:** The meeting opens with "should we rebuild it or kill it?"

**Consequence:** The loudest advocate wins, and the product's actual stage never gets established.
Six months later nobody can reconstruct why.

**Fix:** Run the seven transition questions first, in writing. The pattern of yeses usually settles
the argument without anyone having to win it.

---

### Pitfall 2: Skipping Extension Because It's Boring
**Symptom:** The options considered are replace and retire. Extension never comes up.

**Consequence:** You spend a replacement's budget on a product a variant would have carried for
three more profitable years.

**Fix:** Test the four extension questions explicitly and record the answers. "No, because…" is a
useful artifact; silence isn't.

---

### Pitfall 3: Mistaking a Channel Problem for a Product Problem
**Symptom:** Revenue is falling, so the product is judged to be in decline.

**Consequence:** You replace a healthy product while the broken distribution channel or stale
bundle carries straight over to the successor.

**Fix:** Transition question 5 and 6 exist for this. Check the lever before condemning the product.

---

### Pitfall 4: The Register Without a Plan B
**Symptom:** Risks are listed with mitigations. The contingency column is empty or reads "monitor."

**Consequence:** The mitigation fails — they do — and there's no prepared response, so the response
is improvised under time pressure in public.

**Fix:** Every risk rated medium or above gets a real contingency. "What is Plan B?" is the whole
point of the column.

---

### Pitfall 5: Funding the Launch, Not the Retirement
**Symptom:** The replacement play has a GTM budget and no EOL budget.

**Consequence:** Hazard 7. The successor ships, the old product limps on unsupported, and customers
experience the transition as abandonment while you celebrate a launch.

**Fix:** A replacement play is two funded workstreams. If the retirement isn't funded, you have
chosen an extension play with extra steps.

---

## References

### Related Skills

These stand on their own — none is a prerequisite for this skill, and this skill isn't a
prerequisite for them.

- [`lifecycle-play-advisor`](../lifecycle-play-advisor/SKILL.md) — the guided version of this
  diagnosis
- [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md) — the retirement play's go/no-go
- [`eol-process`](../eol-process/SKILL.md) — running a retirement end to end
- [`organic-growth-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/organic-growth-advisor/SKILL.md) — which growth path an extension
  serves
- [`ansoff-matrix`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/ansoff-matrix/SKILL.md) — where the next tranche of growth comes from
- [`roadmap-planning`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/roadmap-planning/SKILL.md) — sequencing the play once it's chosen

### External Frameworks
- Product Life Cycle (PLC) — the five-stage economic model
- Diffusion of innovations / the chasm — why some replacements never cross to the mainstream
- Product Life Cycle strategy grid — marketing-mix levers by stage

### Provenance
- Distilled from practitioner experience running product lifecycle transitions and product
  retirements across software, hardware, and regulated industries.
