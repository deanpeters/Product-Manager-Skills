---
name: eol-internal-enablement
argument-hint: "[product being sunset, replacement, and key dates]"
description: "Build the support FAQ, sales talking points, and objection handling teams need before an EOL announcement. Use when customer-facing teams must be ready before customers hear."
intent: >-
  Generate the internal enablement materials customer-facing teams need before an EOL announcement
  goes out: a support FAQ, sales comparison talking points, objection-handling scripts using
  Acknowledge-Reframe-Offer, and an escalation playbook. Right-sized so a feature deprecation gets a
  one-page support note while a major sunset gets a full role-specific enablement pack.
type: component
theme: eol-transition
best_for:
  - "Arming Support and Sales before the announcement, not five minutes after it"
  - "Turning predictable EOL objections into honest, non-defensive responses"
  - "Giving escalations a named path before the churn-risk calls start"
scenarios:
  - "We announce the sunset in three weeks and Support has nothing — what do they need?"
  - "Sales keeps getting ambushed on our EOL; build them talking points and objection handling"
estimated_time: "25-45 min"
---

# EOL Internal Enablement

## Purpose

Build what customer-facing teams need **before** the EOL announcement goes out: a support FAQ, sales
talking points with honest comparison data, objection handling, an escalation ladder, and — when the
sunset warrants it — a channel partner brief and a training outline.

The cardinal sin of EOL communication is handing Support and Sales the announcement five minutes
before customers get it and wishing them luck. This skill exists to prevent that. Internal readiness
is a prerequisite for announcing, not a follow-up task.

## Input

**Works best with:** The product being sunset, what replaces it (if anything), and the key dates.

**Also useful:** The objections you expect, which accounts are at risk, what continues versus what
stops, and whether channel partners are in the picture.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it
covers; don't re-ask.

**Arriving empty-handed? That works too.** The skill asks up to three questions — what's being sunset
and what replaces it, the dates for stopping sale/support/service, and the top objections you expect
— then builds the pack. If you don't know the objections, it drafts the predictable ones and you
edit.

**Example invocations:**
- `Build the enablement pack for our legacy module sunset — replaced by the new dashboard, EOL Dec 31.`
- `Support FAQ only, feature deprecation, no replacement, three weeks notice.`

---

## Key Concepts

### Right-Size the Pack

**Not all EOLs play out the same.** Most land in the middle:

| | **Level 1 — Light** | **Level 2 — Standard** | **Level 3 — Heavy** |
|---|---|---|---|
| Typical scope | Feature, internal tool, API | Commercial product, active customers | Revenue-critical, hardware, regulated |
| Produces | Support FAQ only (10-15 Q&A) | + Sales talking points, objection handling, escalation playbook | + Channel brief, account escalation tiers, training outline |
| Audience | Support | Support, Sales, CS | + Partners, execs, field service |
| Prep time | An afternoon | A week | Several weeks with live training |

**Level 2 is the default.** Recommend a level, say why in one line, and let the user move it.
**Never default to Level 3** — a full training program for a feature deprecation teaches teams that
EOL enablement is bureaucracy, and they'll tune out the one that matters.

If someone dials down to a Support FAQ only, name what's dropping: usually the objection handling,
which is what Sales needs when a customer says "we renewed last quarter."

### Enablement Precedes Announcement — Always

Set an explicit "enablement complete by" date that falls **before** the announcement date. If those
two dates aren't separated on the plan, they will collapse in practice, and Support will learn about
the sunset from an angry customer.

### Organize the FAQ by What Customers Ask

Not by internal category. Lead with the questions that will generate the most call volume. The six
that always come, in roughly this order:

1. **What is happening?**
2. **What does this mean for me?**
3. **What are my options?**
4. **What about my data?**
5. **What about my contract?**
6. **When does support end?**

Answers are one to two sentences, honest and specific. "We're evaluating options" is not an answer;
it's a deferral that the customer will hear as evasion.

### Acknowledge — Reframe — Offer

Every objection response follows the same three-beat pattern:

1. **Acknowledge** — validate the frustration as legitimate, without hedging or apologizing twice
2. **Reframe** — give the honest reason or the genuine upside, without pretending the loss isn't real
3. **Offer** — a concrete accommodation, option, or next step the rep can actually deliver

**Why the order matters:** teams under pressure skip straight to Offer, which reads as a bribe, or
straight to Reframe, which reads as a lecture. Acknowledging first is what makes the other two
land — and it costs nothing.

**The offer must be real.** An objection handler that ends in "I'll see what I can do" trains reps
to make promises the company hasn't agreed to. Get the accommodation approved *before* it goes in
the pack.

### The Predictable Objections

Five show up in nearly every sunset. Draft these before asking what else might come:

1. **"We just bought this / renewed last quarter."**
2. **"The replacement doesn't have feature X."**
3. **"We're going to leave entirely."**
4. **"Why should we trust your next product?"**
5. **"Can you make an exception for us?"**

The fourth is the one teams answer worst, because the honest answer is about *how you're handling
this transition* — the current sunset is the evidence for the next promise.

### Escalation Is a Ladder With Names

Four rungs, each with a named owner and a trigger:

- **Level 1** — standard questions (Support)
- **Level 2** — unhappy customers (Support lead or CS)
- **Level 3** — churn-risk accounts (CS lead or account exec)
- **Executive** — named accounts, press, legal threats

An escalation path without names is a diagram. Reps need to know who to call at 4pm on a Friday.

### The Sticky-Note Rule

Bullets are **4 to 8 words**. FAQ answers are one to two sentences. A rep reads this between calls,
not in a training room.

### Anti-Patterns (what this is NOT)
- **Not the customer announcement.** This is what teams know before customers hear.
- **Not a script to read aloud.** It's preparation, not a teleprompter.
- **Not spin.** Defensive talking points survive one call and then get abandoned.
- **Not optional at Level 1.** Even a feature deprecation needs Support to know what to say.

---

## Application

### Step 1: Set the level and the dates

Recommend a level from blast radius, present all three, let the user choose. Then pin two dates:
the **announcement date** and the **enablement-complete date** that precedes it.

### Step 2: Build the support FAQ (all levels)

Ten to fifteen Q&A pairs, organized by the six customer questions above. Write the answer a customer
would accept, then check it against what's actually true. If those differ, the problem is the plan,
not the wording — flag it.

Include the escalation ladder at the end of the FAQ, with names.

### Step 3: Build sales talking points (Level 2+)

- **Positioning:** how to frame it, what language to avoid, what to lead with
- **Comparison table:** sunset product vs. replacement, capability by capability — **including the
  gaps**. A comparison table with no gaps is a marketing sheet, and reps stop trusting it the first
  time a customer finds one.
- **Pipeline guidance:** deals in progress, pending renewals, bundled pricing, new prospects asking
- **Competitive response:** what to say when a competitor raises your EOL, and when a customer asks
  whether anything else is getting killed

### Step 4: Build objection handling (Level 2+)

Start with the five predictable objections. Add two or three specific to this product and customer
base. Each gets Acknowledge-Reframe-Offer, with the offer pre-approved.

### Step 5: Channel brief and training (Level 3)

**Channel brief** covers three things: what partners need to know, what they may tell their
customers, and what they must *not* do. The third is the one that prevents a partner from
freelancing a migration promise you can't honor.

**Training outline** is 60-90 minutes: context and rationale, timeline walkthrough, FAQ review,
objection role-play, escalation paths, open questions. The role-play is the part that works — reading
objection handlers silently doesn't build the reflex.

### Step 6: Assumptions

Close with what you assumed: which objections you predicted rather than heard, which accommodations
you believe are approved, which dates you treated as firm.

### Final Step: Offer what comes next

"Where next?

1. **Draft the customer announcement** — see [`eol-message`](../eol-message/SKILL.md) (Recommended)
2. **Build account-specific talking points** for your top at-risk customers
3. **Write role-play scenarios** for the training session
4. **Create a 30-day post-announcement monitoring checklist**

Reply with a number, a combination ('1 & 2'), or your own path."

---

## Examples

- `examples/sample.md` — Fieldlight Classic Dispatch (SaaS, Level 2 pack)
- `examples/sample-industrial.md` — NFA-200 controller line (industrial, Level 3 with channel brief)

---

## Common Pitfalls

### Pitfall 1: Enablement After Announcement
**Symptom:** The FAQ is drafted the week the email goes out.

**Consequence:** Support improvises for three days. Their improvisations become your de facto
policy, and some of them contradict each other.

**Fix:** Put "enablement complete" on the plan as a date that gates the announcement.

---

### Pitfall 2: The Gapless Comparison Table
**Symptom:** Every row shows the replacement matching or beating the sunset product.

**Consequence:** The first customer to name a real gap discredits the whole table, and the rep has
nothing to fall back on.

**Fix:** Name the gaps, with the workaround or parity date next to them. Reps who can concede a
point keep credibility for the rest.

---

### Pitfall 3: Defensive Objection Handling
**Symptom:** Responses that explain why the customer shouldn't feel that way.

**Consequence:** The customer escalates, because being told your reaction is wrong is worse than
the original news.

**Fix:** Acknowledge first, always. The frustration is legitimate even when the decision is correct.

---

### Pitfall 4: The Unfunded Offer
**Symptom:** Objection handlers end with accommodations nobody approved — discounts, extensions,
custom migrations.

**Consequence:** Reps promise them, Finance refuses them, and the customer now has two grievances.

**Fix:** Every offer in the pack is pre-approved with a limit. If it isn't approved, it isn't in
the pack.

---

### Pitfall 5: Nameless Escalation
**Symptom:** "Escalate to the appropriate team."

**Consequence:** The churn-risk call sits in a queue for two days.

**Fix:** Four rungs, each with a name and a trigger. Test it by asking a rep who they'd call.

---

## References

### Related Skills

These stand on their own — none is a prerequisite for this skill, and this skill isn't a
prerequisite for them. If you already picked a level elsewhere, say "Level 2" and this skill builds
to it.

- [`eol-message`](../eol-message/SKILL.md) — the customer-facing announcement this prepares teams for
- [`eol-stakeholder-sequence`](../eol-stakeholder-sequence/SKILL.md) — the conversations that surface
  what belongs in this pack
- [`eol-checklist`](../eol-checklist/SKILL.md) — where the enablement-complete date lives
- [`eol-readiness-advisor`](../eol-readiness-advisor/SKILL.md) — if the decision still needs a case
- [`incoming-request-advisor`](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/incoming-request-advisor/SKILL.md) — for decoding the escalations
  this pack will generate

### External Frameworks
- Acknowledge-Reframe-Offer — objection handling pattern
- Customer success playbooks — retention plays during transitions

### Provenance
- Adapted from `prompts/eol-internal-enablement.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
