---
name: eol-readiness-advisor
argument-hint: "[product or feature under EOL consideration, and what triggered it]"
description: "Run a go/no-go assessment for retiring a product or feature, then right-size the effort. Use when someone says \"we should probably kill this\" and nobody has made the call."
intent: >-
  Structured go/no-go assessment for sunsetting a product or feature. Determines whether EOL is the
  right call, how intense the sunset effort needs to be, and which organizational functions need to
  be involved. Prevents both premature kills and expensive delays on products that should have been
  retired sooner.
type: interactive
theme: eol-transition
best_for:
  - "Deciding whether a declining product should actually be retired — or held, harvested, or fixed"
  - "Right-sizing an EOL effort so a feature deprecation doesn't get a flagship playbook"
  - "Naming the obligations and landmines that make a sunset harder than it looks"
scenarios:
  - "Leadership keeps saying we should kill this module but nobody will make the call — help me assess it"
  - "We're retiring a hardware line with service contracts and channel partners; how big does this effort need to be?"
estimated_time: "15-25 min"
---

# EOL Readiness Advisor

## Purpose

Decide whether a product or feature should actually be retired — and if so, how much machinery the
retirement deserves. This skill produces a go/no-go verdict with named evidence, an **intensity
level** you choose, and a short list of the obligations that will bite you if ignored.

Most EOL guidance assumes the decision is already made and jumps to the plan. This skill sits
earlier: it is the conversation where "we should probably kill this" becomes a decision someone
will defend in a room.

It is equally willing to tell you **not** to retire. A "hold" or "harvest" verdict is a real
outcome here, not a consolation prize.

## Input

**Works best with:** The product or feature under consideration and what triggered the conversation
(a declining number, a strategy shift, a support-cost complaint, an exec offhand remark).

**Also useful:** Revenue and customer counts, whether a replacement exists, contract or regulatory
commitments, and any political sensitivities you already know about.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it
covers; don't re-ask.

**Arriving empty-handed? That works too.** The skill opens by asking what's under review and why,
then walks you through blast radius, intensity, and transition path one question at a time. You do
not need the numbers in front of you — "I don't know" is a valid answer that becomes a labeled
assumption in the verdict.

**Example invocations:**
- `Should we retire our legacy reporting module? Usage is down 60% and support costs are climbing.`
- `EOL readiness check on our NFA-200 controller line — 120 installs, channel partners, UL certified.`

---

## Key Concepts

### The Right-Sizing Dial

**Not all EOLs play out the same.** Some are a changelog entry and a support macro. Some consume
the whole company for three quarters. Most land in the middle. The single most common EOL failure
in either direction is a mismatch between the size of the sunset and the size of the response —
a flagship retirement run as a Jira ticket, or a feature deprecation that spawns a steering
committee.

So the intensity is a **dial you set**, not a verdict the framework hands you:

| Dimension | Level 1 — Light | Level 2 — Standard | Level 3 — Heavy |
|---|---|---|---|
| Typical scope | Feature, internal tool, unversioned API | Commercial product with active customers | Revenue-critical, hardware, regulated |
| Stakeholder stops | 3-4 | 7-8 | 10+ |
| Lifecycle gates used | 2-3 (NSC, EOS, EOL) | 4-5 (NSC, EOS, EOE, EOM, EOL) | All 8 (GA through EOSRV) |
| Functional areas | Product, Eng, Support, Docs | + Sales, Marketing, CS, Finance, Legal, IT, Data | + Supply Chain, Channel, Regulatory, Org |
| Enablement | Support FAQ only | + Sales talking points, objections, escalation | + Channel brief, account tiers, training |
| Customer message | Brief notice | Standard with phase table | Full with compliance section |
| Typical lead time | Weeks | 6-12 months | 12-24 months |

**Level 2 is where most sunsets belong.** Treat it as the default and argue your way up or down.

**The dial is yours to move.** Recommend a level, explain the reasoning, then let the user override
in either direction — and let them move it again later. A PM who says "give me the light version,
I know my org" is exercising judgment, not making an error. Honor it, and note in one line what the
lighter level leaves uncovered so the choice is informed rather than blind.

### Lifecycle Gates (shared vocabulary)

EOL is not one date. It is a series of gates, and most customer anger comes from collapsing them
into a single announcement:

- **GA (General Availability):** Actively sold and fully supported
- **NSC (Notice of Status Change):** The decision is communicated; planning begins
- **EOS (End of Sale):** No new customers can purchase
- **EOE (End of Expansion):** Existing customers cannot add capacity or seats
- **EOR (End of Renewal):** Existing contracts will not be renewed
- **EOM (End of Maintenance):** Bug fixes and patches stop
- **EOL (End of Life):** The product is retired
- **EOSRV (End of Service):** All support and service obligations end

Light sunsets use three of these. Heavy sunsets use all eight. Naming the gates you're *not* using
is as useful as naming the ones you are.

### The Four Retire Signals

Evidence that supports a go verdict. Two or more, strongly present, is a real case:

1. **Financial viability** — costs exceed revenue; support load drains disproportionate resources
2. **Strategic alignment** — conflicts with company direction; you are exiting this market
3. **Solution replacement** — an internal successor supersedes it; you're consolidating platforms
4. **Market irrelevance** — needs shifted, technology moved, the core problem stopped existing

### The Four Hold Signals

Evidence that argues against retiring *now*, even when the retire signals are loud:

1. **Obligation lock** — contracts, SLAs, regulatory commitments, or "lifetime" promises still run
2. **Strategic hostage** — low revenue, but it sits inside your most important accounts
3. **No landing place** — no replacement and no third-party alternative; customers would be stranded
4. **Exit costs exceed carry costs** — the sunset costs more than another year of quiet maintenance

### Anti-Patterns (what this is NOT)

- **Not a rubber stamp.** If the hold signals dominate, the verdict is hold, and the skill says so.
- **Not a portfolio screen.** This assesses one product. Screening a catalog is different work.
- **Not the plan.** The verdict and intensity level are inputs to planning, not the plan itself.
- **Not a financial model.** It reasons about revenue and cost qualitatively; it does not forecast.

---

## Application

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the default interaction
protocol for this skill.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

This skill asks **up to 4 adaptive questions**, then delivers a verdict, an intensity level, and
numbered next steps. Give the heads-up at the start: four questions, roughly fifteen minutes, and
they can dump context at any point to skip ahead.

---

### Question 1 of 4 — What's under review, and what triggered this?

**Agent asks:**

"What product or feature is under EOL consideration, and what brought it up? The trigger matters as
much as the product — a declining metric, a strategy shift, a support-cost complaint, and an exec
offhand remark lead to very different assessments."

**Is retirement even the right question yet?** This skill assesses one play: retiring. At the
mature-to-decline inflection there are three — **extend** the product, **replace** it with a
successor, or **retire** it. If the user hasn't established that retirement is the play, say so and
offer the upstream diagnosis:

> "Before we assess retiring it — is retiring the play you've settled on? There are two others
> (extend it, or replace it with a successor), and
> [`lifecycle-play-advisor`](../lifecycle-play-advisor/SKILL.md) works out which fits. Happy to
> continue here if the call is made."

Don't force the detour. A user who says "we've decided, assess the retirement" gets the assessment.

**Listen for the trigger type**, because it predicts the failure mode:

| Trigger | Watch for |
|---|---|
| Declining metric | Is it decline, or seasonality/measurement change? |
| Strategy shift | Is the product misaligned, or just unfashionable? |
| Support cost | Is retirement the fix, or is a bug fix the fix? |
| Exec remark | Is there evidence, or is this an opinion with a title? |
| Replacement shipped | Is the replacement actually at parity for these customers? |

If the trigger is an exec remark with no supporting evidence, say so plainly at verdict time. That
is the single most common source of premature kills.

---

### Question 2 of 4 — What's the blast radius?

**Agent asks:**

"Help me size the impact. Rough numbers are fine, and 'I don't know' is a real answer:

1. **Customers:** How many accounts or users are on it?
2. **Revenue:** Roughly what does it represent, and is it concentrated in a few accounts?
3. **Commitments:** Any contracts, SLAs, renewal dates, or regulatory obligations attached?
4. **Physical or channel:** Is there hardware, inventory, spare parts, or are partners reselling it?"

**Why this matters (say it):** These four answers set the intensity level. Item 3 is the one that
most often turns a "simple" sunset into a legal problem — it is asked early on purpose.

Mark any unknown as an assumption to be labeled in the verdict. Do not stall the flow to chase a
number; an assessment with three labeled assumptions beats an assessment that never happened.

---

### Question 3 of 4 — Set the intensity

**Agent presents the recommendation, then hands over the dial:**

"Based on what you've described, here's my read on how much machinery this deserves:

**Recommended: Level [N] — [Light / Standard / Heavy]**
Because: [two or three specifics drawn from their answers]

1. **Level 1 — Light.** Punch list, 3-4 stakeholders, brief notice. Right when the blast radius is
   internal or the users are few and reachable.
2. **Level 2 — Standard.** Cross-functional checklist, 7-8 stakeholders, phased customer comms.
   Right for a commercial product with real customers and no regulatory entanglement. *Most sunsets
   belong here.*
3. **Level 3 — Heavy.** Full playbook, 10+ stakeholders, all eight gates, channel and regulatory
   workstreams. Right when revenue is critical, hardware is in the field, or compliance applies.

Take the recommendation, or pick a different level — you know your organization. You can also
change it later; nothing downstream is locked to this choice."

**If the user dials down**, accept it and add one line: "Going lighter than recommended means
[the specific thing that goes uncovered — usually Legal review, channel notification, or migration
support]. Flagging it so it's a choice, not a surprise."

**If the user dials up**, accept it without argument. Over-preparing an EOL is a cheap mistake.

---

### Question 4 of 4 — Where do customers land?

**Agent asks:**

"What happens to the people using it? Three broad paths:

1. **Replacement** — another product of yours takes over
2. **Migration** — they move to a different configuration, tier, or platform
3. **Graceful exit** — nothing replaces it; they need data, notice, and alternatives

Which is it, and how ready is that path today?"

**Path readiness is a go/no-go input, not a detail.** A replacement that is not at feature parity
for *these specific customers* is not a landing place yet. If the path is unready, the verdict is
usually "go, but the announcement waits until [specific readiness condition]."

---

### Final Step: Deliver the assessment

Produce this structure:

```markdown
## EOL Readiness Assessment: [Product]

**Verdict:** [Go / Go-with-conditions / Hold / Harvest]
**Intensity:** Level [N] — [Light/Standard/Heavy] *(user-selected)*
**Confidence:** [High/Medium/Low] — based on [what's known vs. assumed]

### The Case to Retire
- [Retire signal + the evidence behind it]

### The Case Against (or: Conditions)
- [Hold signal + the evidence behind it]

### Assumptions I Made
- [Anything answered "I don't know," stated plainly]

### Obligations to Check Before Announcing
- [Contracts, SLAs, regulatory, "lifetime" promises, channel agreements]

### Landing Place
- **Path:** [Replacement / Migration / Graceful exit]
- **Readiness:** [Ready / Gap: specific gap / Not started]

### What This Level Covers — and Doesn't
- Covers: [gates, stakeholder count, artifacts implied by the level]
- Does not cover: [what the level deliberately skips]
```

Then offer numbered next steps:

"Where do you want to go next?

1. **Build the operational plan** — the phase-gated checklist for a Level [N] sunset
2. **Map the stakeholder conversations** — who to talk to, in what order, and what each must cover
3. **Prepare the internal teams** — support FAQ, sales talking points, objection handling
4. **Draft the customer announcement** — see [`eol-message`](../eol-message/SKILL.md)
5. **Re-run this assessment** with better numbers once you've chased the unknowns

Pick a number, combine them ('2 & 4'), or tell me what you'd rather do."

**On the verdict names:**
- **Go** — retire it; the case is clear
- **Go-with-conditions** — retire it, but a specific thing must be true before announcing
- **Hold** — do not retire now; the hold signals dominate; revisit on a named trigger
- **Harvest** — do not retire and do not invest; run it lean for its remaining revenue, and set a
  review date
- **Extend** — don't retire it; there's life in it. Reached when the hold signals dominate *and* the
  pressure turns out to be demand-side or distributional — a segment you could serve with a variant,
  or a channel and price problem wearing a product costume. Hand off to
  [`lifecycle-play-advisor`](../lifecycle-play-advisor/SKILL.md) to size the play

**Hold and Extend are different findings.** Hold says *not now*; Extend says *this product still has
a move available*. Don't collapse them — a PM told "hold" waits, and a PM told "extend" acts.

---

## Examples

### Example A — SaaS, dials down from the recommendation

**PM:** "Should we kill Fieldlight Classic? It's our legacy dispatch module. Leadership has been
hinting at it for two quarters."

**Agent (Q1):** "What triggered the hints — a metric, a strategy shift, or a cost complaint?"

**PM:** "Support tickets. Classic generates about 40% of our support volume on maybe 15% of
revenue. And we shipped Fieldlight Next last year."

**Agent (Q2):** "Blast radius — customers, revenue, commitments, and any channel or hardware?"

**PM:** "About 800 accounts, $2.4M ARR. Annual contracts, standard terms, nothing regulatory. Pure
SaaS, we sell direct."

**Agent (Q3):** "Recommended: **Level 2 — Standard.** 800 accounts with annual contracts and real
revenue means phased comms and a cross-functional checklist, but no regulatory or channel
workstream, so you don't need the heavy version. [presents the three levels]"

**PM:** "Honestly we're a 40-person company. Give me Level 1."

**Agent:** "Taking Level 1. Going lighter here means you skip the formal Legal review of the
renewal-date language and the phased sales enablement — with 800 annual contracts, the renewal
dates are the piece I'd least like to see uncovered. Flagging it so it's a choice, not a surprise.
Want to keep Level 1 with a single Legal check bolted on? That's a common middle."

**PM:** "Yeah, do that."

**Agent (Q4):** "Where do the 800 accounts land — Fieldlight Next, or something else?"

**PM:** "Next. It's at parity except for the custom dispatch rules maybe 30 accounts use."

**Verdict:** Go-with-conditions. Level 1 + Legal check. Condition: the 30 custom-rule accounts need
a named plan before announcement, or they become your escalation queue. Assumption labeled: support
volume figure is from memory, not pulled.

---

### Example B — Industrial, dials up, lands on Hold

**PM:** "We want to retire the NFA-200 retrofit controller. The NFA-500 launched and manufacturing
wants the line freed up."

**Agent (Q1):** "So the trigger is internal — manufacturing capacity plus a shipped successor. Any
customer-side signal, or is this entirely supply-side?"

**PM:** "Entirely supply-side. Customers are fine with the 200."

**Agent (Q2):** "Blast radius — installs, revenue, commitments, hardware and channel?"

**PM:** "About 120 installations. Eight channel partners resell it. Service contracts run through
2028 on some. UL and CE certified. And there's spare parts inventory."

**Agent (Q3):** "Recommended: **Level 3 — Heavy.** Service contracts running to 2028, eight
channel partners, regulatory certification, and physical spare parts — that's four separate
workstreams the lighter levels don't have room for."

**PM:** "Agreed, Level 3."

**Agent (Q4):** "Where do the 120 installs land? Is the NFA-500 a drop-in for the 200's
installed base?"

**PM:** "Not exactly. The 500 needs a different mounting bracket and the retrofit cases are... it'd
be a site visit each."

**Verdict:** **Hold.** The retire signals are real but supply-side only. Against them: service
contracts running to 2028 (obligation lock), and no drop-in landing place — 120 site visits is not
a migration path, it's a project needing its own funding. Customers are not asking for this.

Recommended instead: **EOS now, EOL later.** Stop selling the NFA-200, keep servicing it through
contract expiry, and fund the bracket/retrofit work as the actual prerequisite. Revisit when the
retrofit path exists or contracts wind down — whichever comes first. Manufacturing gets the line
back at EOS, which was the real ask.

*Note how the verdict separates the presenting problem (retire the product) from the underlying one
(free the manufacturing line) — and solves the second more cheaply.*

---

## Common Pitfalls

### Pitfall 1: The Opinion With a Title
**Symptom:** The entire case rests on an executive saying "we should kill that thing."

**Consequence:** You spend two quarters retiring a product that was quietly profitable, and nobody
remembers whose idea it was when the churn shows up.

**Fix:** Name the trigger explicitly in the assessment. If the evidence is one remark, the verdict
is "Hold — pending evidence," not "Go."

---

### Pitfall 2: One-Size Sunset
**Symptom:** Every EOL gets the same treatment — either everything runs as a ticket, or everything
gets the steering committee.

**Consequence:** Light sunsets burn political capital on ceremony. Heavy sunsets blow up in public.

**Fix:** Set the intensity deliberately, say it out loud, and name what the chosen level skips.

---

### Pitfall 3: Skipping the Obligation Check
**Symptom:** Blast radius is measured in customers and revenue; contracts and certifications go
unasked.

**Consequence:** The worst EOL failures on record are legal, not commercial — refund orders over
"lifetime" hardware promises, fines over retired services with no adequate alternative.

**Fix:** Ask about commitments in the *same breath* as revenue. It's question 2 for a reason.

---

### Pitfall 4: Treating "No Replacement" as a Detail
**Symptom:** The verdict is Go, and the landing place is "customers will find something."

**Consequence:** You are not retiring a product, you are evicting customers. They remember.

**Fix:** Graceful exit is a legitimate path — but it requires data export, extended notice, and
honest alternatives. If none exist yet, the verdict is Go-with-conditions.

---

### Pitfall 5: Solving the Presenting Problem
**Symptom:** Someone asks to retire a product; the assessment evaluates retiring the product.

**Consequence:** You run a full sunset when an End-of-Sale, a price increase, or a bug fix would
have satisfied the actual need.

**Fix:** Ask what the trigger is really about. "Free up the manufacturing line" is answered by EOS,
not EOL. Name the cheaper answer when you see it.

---

## References

### Related Skills

Each of these stands on its own — none require this skill to have run first, and this skill is not
a prerequisite for any of them. If you did run this assessment, carry your intensity level over by
simply saying "Level 2" when you start; there's no handoff format to preserve.

- [`eol-message`](../eol-message/SKILL.md) — the customer-facing announcement
- [`incoming-request-advisor`](../incoming-request-advisor/SKILL.md) — when the EOL request arrived
  as a message you need to decode first
- [`stakeholder-map`](../stakeholder-map/SKILL.md) — general stakeholder mapping
- [`business-health-diagnostic`](../business-health-diagnostic/SKILL.md) — when the trigger is
  financial and you want the numbers examined properly
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md) — the interaction protocol

### External Frameworks
- Product Life Cycle (PLC) — the decline stage is where EOL decisions live
- Mendelow's Matrix — power/interest stakeholder prioritization

### Provenance
- Adapted from `prompts/eol-readiness-assessment.md` in the
  `https://github.com/deanpeters/product-manager-prompts` repo.
