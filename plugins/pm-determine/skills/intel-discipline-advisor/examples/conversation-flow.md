# Intel Discipline Advisor — Conversation Flow Example

All companies, signals, and figures are **fictional**. This transcript shows the full interaction:
inline input crediting an answer (Q1 is skipped because the invocation already answered it),
adaptive questioning, honest capacity handling, numbered recommendations that show their
mapping-table logic, a combination selection, and the closing handoff to the triage card.

---

**User:** `Intel discipline advisor: our sales team lost three straight deals to Wrenchline on
"their platform is more complete" — I want to know if that objection is about to get worse.`

**Agent:** Heads-up on how this works: normally I'd ask three quick questions, but your invocation
already answered the first — this is a **suspected competitor move** (Wrenchline deepening the
platform story), with a signal already seen: three consistent win/loss objections. That's HUMINT
flagging once, from the highest-ground-truth layer there is.

**Question 2 of 3 — the follow-up:** those three losses — same segment and deal size, or spread?
(Concentrated losses suggest a targeted play; spread losses suggest a general narrative shift.)

**User:** All mid-market, all against their full-suite pitch. Also — free tools only, and honestly
I've got maybe 2 hours now and 30 min/week after that.

**Agent:** That answered **Question 3** (constraints) too — free sources, ~2 hours now,
30 min/week sustained. No more questions; here's the triage.

Your win/loss signal means HUMINT has flagged once. One discipline is an anecdote — the job is
corroboration from channels that fail *differently*. Recommendations:

> 1. **SIGINT sweep now (~1 hour, free)** — Wayback diff their pricing and product pages over the
>    last two quarters; check crt.sh for new subdomains. *Mapping logic: battle cards run on
>    SIGINT + OSINT + HUMINT, and SIGINT is the freshest layer — if the "complete platform" pitch
>    is about to get a product behind it, staging shows up here first.* Executing skill:
>    feed findings into `battle-card-builder` to rebuild the objection handling.
> 2. **OSINT review-mining pass (~1 hour, free)** — mine their reviews for whether *customers*
>    echo the completeness story or contradict it ("bought the suite, use two modules"). *Mapping
>    logic: the promise-delivery gap is battle-card ammunition — if the platform pitch outruns the
>    product, your counter writes itself.* Executing skill: `voice-of-customer-miner`.
> 3. **Set the 30-min/week watch** — wire Wrenchline into `competitive-intel-watch`, monthly
>    materiality bar, so the corroboration keeps arriving without you hunting. *Mapping logic:
>    your sustained capacity is exactly the weekly SIGINT layer's cost; anything heavier would be
>    cadence fantasy.*
> 4. **The off-ramp, honestly:** if the real question is "why are we losing" rather than "what
>    are they building," two more win/loss interviews beat any public sweep — your churned
>    prospects already know the answer. Route: `discovery-interview-prep`.
>
> Reply 1, 2, 3, 4, a combination like "1 and 3", or tell me more. (Progress: triage complete —
> recommendations on the table.)

**User:** 1 and 3. And say more about why not 2 first?

**Agent:** Good combination — 1 gives you the now-answer inside your 2 hours, 3 makes the
corroboration self-sustaining.

Why 2 isn't first *for you*: review mining is the strongest play when the decision is positioning
copy or a counter-narrative. Your stated worry is "about to get worse" — a **forward-looking**
question, and reviews look backward; they'd tell you about the platform they shipped, not the one
they're building. It's the right second sweep if option 1 finds staging evidence. That's the
mapping lesson: OSINT-voice reads the present, SIGINT reads the near future, and the question's
tense picks the discipline.

Want the one-page triage card (`template.md`) filled in from this session, so the route and its
review date land somewhere your future self will find them?

---

## Why this example works

- **Inline input was credited, twice.** The invocation answered Q1, and the user's Q2 reply
  volunteered the constraints — so Q3 was never asked. Three budgeted questions, one actually
  spent. Re-asking answered questions is the anti-pattern (`workshop-facilitation`,
  `inline-input-flow.md`).
- **Every recommendation carries its "because."** The mapping-table logic rides along in italics —
  the user leaves knowing *why* SIGINT reads the near future, which is the advisor's stated goal:
  by the third session they shouldn't need it.
- **The capacity answer was believed.** 30 min/week produced a monthly-bar watch, not the
  aspirational weekly deep sweep that dies by cycle three.
- **The off-ramp was offered even though the intel route was live** — and the "tell me more"
  request got a real teaching answer (question tense → discipline choice), not a re-pitch.
