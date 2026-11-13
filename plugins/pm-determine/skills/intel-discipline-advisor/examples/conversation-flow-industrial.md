# Intel Discipline Advisor — Conversation Flow Example (Industrial)

All companies, signals, and figures are **fictional**. Industrial sibling of
[`conversation-flow.md`](conversation-flow.md). The SaaS transcript showed inline-input crediting
and a combination selection; this one shows the advisor handling a **physical-world signal**, a
**paid-tools question answered honestly**, and the routing logic shifting disciplines because the
market emits differently.

---

**User:** `Intel discipline advisor — a distributor rep mentioned our component competitor just
leased a second building near their plant. Means anything?`

**Agent:** Heads-up on how this works: three quick questions, then numbered recommendations. Your
invocation already answered the first — this is a **suspected competitor move**, and the signal
you've seen is a facility lease (that's MASINT flagging once — resource allocation rarely lies,
but one signal is still an anecdote). It also arrived via a distributor rep, which makes it
HUMINT-carried — worth noting because secondhand facility news needs the primary record.

**Question 2 of 3:** what would this competitor plausibly *do* with a second building — more
capacity for what they already make, or something new? If you're not sure, say so; the search can
carry both hypotheses.

**User:** Not sure. Could be capacity, could be the electrification line they keep hinting at in
trade interviews.

**Question 3 of 3 — constraints:** free sources only, or is paid tooling (trade-data
subscriptions, patent analytics) available? And how much time does this get?

**User:** We have an ImportYeti-type trade data subscription. Maybe a day, total.

**Agent:** Good — that subscription matters here; this is one of the few questions where paid
trade data beats an afternoon of free searching. Here's the triage.

Your signal is MASINT-flagged (facility) but secondhand. Job one is *confirming the primary
record*; job two is *disambiguating capacity vs. new capability* — and those are different
signal chains:

> 1. **Confirm + read the building (2 hrs, free)** — local permit records and the business
>    journal for the lease; permits tell you more than square footage: power/water capacity
>    upgrades and zoning class separate "warehouse" from "production line." *Mapping logic:
>    MASINT facility chains — land, power, permits precede equipment by 6-36 months.*
> 2. **Customs pull on their component imports (2 hrs, your subscription)** — capacity looks
>    like *more of the same* inputs; a new electrification line looks like *new* input
>    categories and new supplier geographies. *Mapping logic: MASINT supply-chain chain — input
>    mix shifts disambiguate exactly your two hypotheses.*
> 3. **TECHINT cross-check (2 hrs, free)** — patent classifications and any standards-committee
>    appearances around electrification; their trade-interview hints are OSINT ambition — a
>    filing cluster would be commitment. *Mapping logic: announcements are intent until TECHINT/
>    FININT corroborate.*
> 4. **The off-ramp, honestly:** if the real worry is "will they out-capacity us on existing
>    products," your sales ops win/loss data on lead times answers it faster than any registry —
>    ask whether you've been losing on delivery dates first.
>
> Reply 1, 2, 3, 4, or a combination like "1 and 2". With a day: 1 and 2 fit; add 3 only if 2
> shows new input categories. (Progress: triage complete.)

**User:** 1 and 2. If the imports show new categories, I'll come back for 3.

**Agent:** Exactly the right sequencing — you've just run the confidence-stacking ladder
yourself: MASINT-primary confirmation, then a second independent MASINT chain, holding TECHINT in
reserve as the escalation trigger. Two agreeing channels = working hypothesis, enough to assign
someone; three = brief leadership. One page to carry it: want the triage card
([`template.md`](../template.md)) filled in with the route, the escalation trigger, and a review
date?

---

## Why this example works

- **The routing shifted with the physics.** The SaaS transcript routed to SIGINT sweeps and
  review mining; the same advisor, given a facility signal, routed to permits, customs data, and
  patents — the mapping table's logic visibly responding to what the market emits, which is the
  lesson the advisor exists to teach.
- **The signal's *carrier* got read, not just its content.** A distributor-relayed facility lease
  is HUMINT carrying MASINT — so recommendation 1 is *confirm the primary record*, the step
  secondhand signals always need and usually skip.
- **The paid-tool answer was honest in both directions:** the trade-data subscription genuinely
  changes recommendation 2, and everything else stayed free — no tool-maximalism.
- **The user left running the stacking ladder unprompted** ("if imports show new categories,
  I'll come back for 3") — the by-your-third-session-you-won't-need-me goal, caught on
  transcript.
