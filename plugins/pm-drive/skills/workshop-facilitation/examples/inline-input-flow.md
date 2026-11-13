# Example Flow: Inline Input Skips Answered Questions

This transcript demonstrates the **inline-input rule** from the Input section of every skill: anything the user supplies with the invocation counts as answers already given. The facilitator credits that context, skips the questions it covers, and resumes mid-flow — it does not march the user back through questions they already answered.

The session below uses `discovery-interview-prep` running on this facilitation protocol, but the pattern applies to any interactive skill.

---

## The Transcript

**User (invocation with inline context):**

> Use discovery-interview-prep: I need to understand why enterprise customers churn after 6 months. I can only get 5 interviews, and I have 2 weeks before the roadmap review.

**Facilitator:**

> Quick heads-up: this normally takes about 7-10 minutes and around 6 questions — but you've already answered most of the context questions in your request, so we'll be faster.
>
> Here's what I have from what you gave me:
> - **Research goal:** understand why enterprise customers churn after ~6 months ✓
> - **Constraints:** 5 interviews max, 2-week window ✓
> - **Deadline driver:** roadmap review ✓
>
> That covers Context Q1, Q3, and Q4. Two things I still need:
>
> **Context Q2/6 — Who are you interviewing?**
> 1. Churned customers only
> 2. At-risk customers still on the platform
> 3. A mix of churned and retained (contrast pairs)
> 4. Other (specify)

**User:**

> 3

**Facilitator:**

> Contrast pairs — good instinct for a churn question; retained customers show you what churned ones are missing.
>
> **Context Q5/6 — Do you have hypotheses going in, or is this exploratory?**
> 1. Strong hypotheses (we suspect onboarding)
> 2. A few loose hunches
> 3. Fully exploratory — no assumptions yet

**User:**

> 2 — we think it's either onboarding or a missing integration

**Facilitator:**

> That's everything. Based on your goal (6-month enterprise churn), constraints (5 interviews, 2 weeks), and your two hunches, here are recommended approaches:
>
> 1. **Hypothesis-split interviews** (Recommended) — 2 interviews probing onboarding, 2 probing the integration gap, 1 held back as a wildcard exploratory slot
> 2. **Journey-mapping deep dive** — walk all 5 through their first 6 months chronologically; slower per interview but surfaces triggers you haven't hypothesized
> 3. **JTBD switch interviews** — focus on what customers "hired" you for and where the product failed to deliver; strongest if churned customers moved to a competitor
>
> Choose a number, combine (e.g., "1 & 3"), or describe your own approach.

---

## Why This Works

- **The invocation context was treated as answers, not preamble.** The facilitator restated what it extracted (goal, constraints, deadline) and *showed* which questions were credited — the user sees their input landed and trusts the flow.
- **Progress labels stayed honest.** The session opened at `Context Q2/6`, not `Q1/6`, because Q1 was already answered. Restarting the count would signal the inline input was ignored.
- **Only the gaps were asked.** Two questions instead of six. The guided mechanism didn't disappear — it did exactly its job, on exactly the missing pieces.
- **The empty-handed path still exists.** A user who invokes the same skill with no context gets the full heads-up, entry-mode choice, and all six questions. Inline input is a shortcut, never a requirement — that's the "invitation, not gate" principle from the Input convention.

## The Anti-Pattern (What Not to Do)

**User:** *(same rich invocation as above)*

**Facilitator (wrong):**

> Welcome! This session takes 7-10 minutes. Let's begin.
>
> **Context Q1/6 — What's your primary goal for this discovery work?**

The user already answered that — in the message the facilitator is replying to. Re-asking teaches the user that context given up front is wasted, which trains them to withhold it. Interaction drag compounds from there: every re-asked question is a turn the session didn't need.

**Corrective action:** before asking Q1 of any flow, scan the invocation (and any pasted context) against the question list. Credit what's covered, say so explicitly, and open at the first genuinely unanswered question.
