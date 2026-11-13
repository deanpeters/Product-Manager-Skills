# Example: Diagnose a Metric Drop

**Prompt:** "Weekly active users dropped 8% last week. What do you do?"

## Why this example exists

The `improve-youtube.md` example covers an **improvement** question, where the work is
segmentation and opportunity selection. This is a **diagnostic** question, and it rewards a
different shape entirely.

Candidates who pattern-match a diagnostic prompt onto the improvement framework — segment users,
list pain points, propose features — fail it, because the interviewer isn't asking what to build.
They're asking whether you can tell a real problem from an artifact before you spend a team's
quarter on it.

**The structural difference:** an improvement question opens outward toward opportunity. A
diagnostic question narrows inward toward cause. Solutions are the last thing you reach for, and
often you shouldn't reach for them at all.

---

## Condensed Walkthrough

### 1. Clarify — establish the metric is real before explaining it

"Before I theorize, four quick questions:

1. **Is the measurement trustworthy?** Any logging changes, SDK releases, or analytics
   migrations that week?
2. **What's the comparison?** Down 8% versus the prior week, the same week last year, or trend?
3. **How is WAU defined here**, and did the definition change?
4. **Is the drop uniform** or concentrated in a platform, geography, or cohort?"

**Why this comes first:** a meaningful share of real-world metric drops are instrumentation
changes, holiday effects, or definitional shifts. Explaining an artifact with a product theory is
the single most common way to fail this question — and in the real job, the most expensive.

*Assume for this answer: instrumentation is clean, it's an 8% week-over-week drop against a flat
trend, and it's concentrated in Android users in one region.*

### 2. Narrow before hypothesizing

That concentration eliminates most global explanations immediately.

Still live:
- An Android release regression
- A regional outage, carrier, or network issue
- A regional competitor or pricing move
- A local event — holiday, disruption, seasonality
- An app store or distribution change in that market

Ruled out by the concentration itself: pricing changes elsewhere, global algorithm changes,
company-wide seasonality.

**The discipline:** the shape of the drop does more elimination work than any hypothesis list. Get
the shape first.

### 3. Order hypotheses by cheapness to test, not by likelihood

| Hypothesis | How to test | Time |
|---|---|---|
| Android release regression | Compare app versions; check crash rate by version | Minutes |
| Regional outage | Check error rates and CDN status for the region | Minutes |
| App store / distribution change | Check install and update rates | Hours |
| Competitor or pricing move | Market check, app store rankings | A day |
| Local event | Calendar, news for the region | A day |

"I'd start with the top two because they're minutes of work, not because they're most likely.
Cheap tests first is how you avoid spending a week on the interesting hypothesis."

### 4. Reason to a conclusion

*Assume: crash rate on Android 4.2.1, released that week, is 6x baseline in that region only, and
the region's dominant device family maps to a specific OS version.*

"That's the cause: a release regression, device-specific, which is why it looked regional. The
fix is a rollback or patch, and the follow-up is why device coverage in that market wasn't in the
release test matrix."

### 5. Say what you'd do about the process, not just the bug

- **Immediate:** roll back 4.2.1 for affected devices; confirm recovery
- **Short-term:** add that device family to pre-release testing
- **Systemic:** alert on crash rate *by version and region*, not aggregate — the aggregate never
  moved enough to page anyone

**This is the part that separates answers.** The bug is a day's work. The missing alert is why an
8% drop took a week to notice, and it will cause the next one too.

---

## What to notice

- **No feature was proposed.** The prompt sounded like a product question and was an engineering
  regression. Reaching for the improvement framework would have produced a confident, irrelevant
  answer.
- **Clarifying questions did real work.** "Is it uniform or concentrated?" eliminated more
  hypotheses than any subsequent reasoning step.
- **Hypotheses were ordered by test cost, not plausibility.** This is the habit interviewers are
  actually probing — it's what makes someone fast in the job rather than merely insightful.
- **The answer ended on the detection gap.** Aggregate alerting missed a concentrated failure.
  Naming the systemic fix shows you think past the incident.
- **It stayed a diagnosis throughout.** Compare with `improve-youtube.md`, which is right to spend
  most of its length on segmentation and opportunity. Same interviewer, same hour, opposite shape —
  and using the wrong one is the failure mode this pair exists to teach.
