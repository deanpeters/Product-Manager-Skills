# Voice-of-Customer Miner — Worked Example

All companies, quotes, URLs, and figures are **fictional** — including the verbatims, which are
invented here purely to show the format. (In a real run, an invented verbatim is the cardinal sin;
in a fictional worked example, the fiction is declared.) Same scenario as the suite's other
examples: Fieldlight, expanding into FSM, needs to know whether quoting is really the right lead
move — and what Wrenchline's customers are angriest about.

**Invocation:** `Mine voice-of-customer for Wrenchline and DispatchCrow — informs whether quoting
is the right first module for our FSM expansion. Open sweep, but flag anything about quoting.`

---

# Voice-of-Customer Snapshot

## 1. Scope
**Products mined:** Wrenchline, DispatchCrow
**Decision supported:** whether quoting is the right first module for Fieldlight's FSM expansion
**Sources swept:** two B2B review sites (skew: negative, ops-manager heavy), both iOS/Android app stores (skew: technician anger after updates), one trades-owner forum (skew: owner-operators, small shops)
**As-of date:** 2026-07-31

## 2. Need Themes

### Theme: quote the job before leaving the driveway
- **Frequency:** recurring — across both review sites and the forum, 20+ mentions in 6 months
- **Verbatim:** "my guy finishes the walkthrough and then sits in the truck for 25 minutes building the quote on his laptop" — [review site, URL]
- **Verbatim:** "if I don't get the quote out same-day I lose the job to whoever does" — [forum thread, URL]
- **Who says it:** owners and office managers at 10-50 tech shops — **Inference** (reviewer titles where shown)
- **Reading:** speed-to-quote is a revenue event, not an admin task — **Inference**; a quoting tool that starts from the scheduled job's data (already in the calendar) attacks the delay directly.

### Theme: techs need the app to survive a parking lot
- **Frequency:** recurring — dominant complaint cluster in both app stores
- **Verbatim:** "three taps to close a job became seven after the update. my techs just stopped closing jobs" — [app store review, URL]
- **Verbatim:** "works great in the office wifi. useless in a parking garage" — [app store review, URL]
- **Who says it:** field technicians directly (app stores are the one source where techs, not buyers, speak) — **Fact** (reviewer context)
- **Reading:** the buyer evaluates the dashboard, but the tech decides adoption — **Inference**; app-store voice is the adoption early-warning channel the review sites miss.

### Theme: getting money in without chasing it
- **Frequency:** concentrated — one long forum mega-thread, some review-site echo
- **Verbatim:** "the work is done in June, the check clears in September" — [forum thread, URL]
- **Who says it:** owner-operators — **Fact** (forum section)
- **Reading:** invoicing/payment friction reads as a cash-flow problem, not a software feature — **Inference**; supports payments as the follow-on to quoting, but the concentration (one thread) caps confidence.

## 3. Competitor Weak Points
- **Wrenchline:** "my techs won't use it" — recurring, 40+ reviews since January across both review sites — [URL] (consistent with the snapshot's weakness read; now in customers' own words)
- **Wrenchline:** implementation pain — "we paid for eight weeks of setup and still did the data import ourselves" — recurring — [URL]
- **DispatchCrow:** dispatch depth at scale — "fine until we hit 40 techs, then the board falls over" — concentrated in upmarket-switcher reviews — [URL]

## 4. Switching Triggers
- **Push (off Wrenchline):** a failed update or forced tier migration is the named event in most switch stories — **Inference** (review mining, 8 switch narratives)
- **Pull (to DispatchCrow):** "we were live the same afternoon" — same-day self-serve start recurs as the pull — **Fact** (their reviews, URLs)

## 5. So What?
- **Opportunity hypotheses:**
  1. Shops lose winnable jobs in the gap between walkthrough and quote — **Inference**, confidence: high (recurring across source types)
  2. Tech-app usability decides adoption before any feature comparison does — **Inference**, confidence: high
  3. Cash-flow pain makes payments the natural second module — **Inference**, confidence: low (single-thread concentration)
- **Battle-card-ready weaknesses:**
  1. Wrenchline tech-app resistance — evidence quality: high (recurring, two source types)
  2. Wrenchline implementation pain — evidence quality: medium (recurring but review-site only, and reviewers skew negative)
- **Assumptions to validate in real interviews:**
  1. The quote delay is caused by data re-entry (not by pricing judgment, which software can't fix)
  2. Techs actually influence purchase/renewal decisions the way app-store anger implies
  3. The cash-flow thread generalizes beyond owner-operators

---

## Why this example works

- **Theme names contain no features.** "Quote the job before leaving the driveway" — not "quote
  builder." The need framing leaves discovery room for solutions the reviews never imagined
  (voice quoting? photo-to-line-items?).
- **Each source's skew is named and *used*.** App stores skew toward technician update-anger — and
  that's exactly why they're the one channel where the tech, not the buyer, speaks. Bias notes
  aren't disclaimers; they're reading instructions.
- **Frequency honesty changed a conclusion.** The cash-flow theme is vivid but concentrated in one
  mega-thread, so the payments hypothesis ships at *low* confidence — one articulate thread is not
  a theme. That's the discipline the Common Pitfalls warn about, applied.
- **The output lands as hypotheses, not verdicts.** The decision ("is quoting the right lead?")
  gets strong support, but the last section routes everything to real interviews — the bridge from
  competitive intelligence to discovery that this skill exists to build.
