---
name: survey-design-advisor
argument-hint: "[what you want to learn, and from whom]"
description: "Decide whether a survey is the right tool, then shape it. Use when you're about to send a survey and want to learn something real instead of collecting biased, unusable answers."
intent: >-
  Guided triage from a research question to a survey decision. Checks whether a survey is the right
  method at all, then fits the question types, sample, length, and bias controls to what you need
  to learn, and flags the leading questions and sampling traps that make survey data look more
  certain than it is. Recommends a design, or recommends interviews or usage data instead.
type: interactive
theme: discovery-research
best_for:
  - "Deciding whether a survey, interviews, or usage data fits the question"
  - "Writing questions that measure instead of lead"
  - "Choosing who to ask and how many, and what the results can claim"
  - "Reviewing a survey draft before it goes out"
scenarios:
  - "We want to know if customers would pay for a routing add-on. Should we survey them?"
  - "Review my survey. I think half the questions are leading"
  - "We need to size how many plants run aging controllers. Survey or something else?"
  - "How many responses do we need, and who should get it?"
estimated_time: "10-20 min"
---

# Survey Design Advisor

## Purpose

Decide **whether a survey is the right way to learn what you want to know**, and if it is, design
one that produces answers you can use.

Surveys are cheap to send and easy to misuse. They are good at one thing: **measuring how common
something is, across a group you can reach, when you already know what to ask.** They are poor at
discovering *why*, finding problems you haven't thought of, or predicting what people will do. A
survey answers the questions you wrote, in the words you chose, from the people who replied. All
three are biased, and the data still looks like a number.

The sentence to keep in your head: **use interviews to find out what to ask, and a survey to find
out how many.**

## Input

**Works best with:** What you want to learn, from whom, and what decision the answer informs.

**Also useful:** The people you can reach and how (email list, in-app, partners), a draft survey,
and prior research or usage data on the same question.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill starts with the question you're trying to
answer and what you'll do with the result, then walks the decision from there. If a survey is the
wrong tool, it says so and points you to the right one.

**Example invocations:**
- `Should we survey customers about a routing add-on? We want to know if they'd pay.`
- `Review this survey draft before I send it to 400 plant engineers.`

---

## Key Concepts

### When a Survey Fits, and When It Doesn't

| You want to... | Best tool | Why |
|---|---|---|
| Find out **why** people behave a way, or what problems exist | Interviews ([`discovery-interview-prep`](../discovery-interview-prep/SKILL.md)) | A survey can't follow up or notice what you didn't ask |
| See what people **actually do** | Usage data ([`usage-data-investigation`](../usage-data-investigation/SKILL.md)) | Behavior beats stated behavior |
| Measure **how common** a known thing is across a group | **Survey** | This is its job |
| Test **willingness to pay** | A priced test or a real commitment | Stated intent overstates behavior |
| Compare **known options** on a defined scale | **Survey** | With care for order effects |

If the answer to "what will we do differently depending on the result?" is "nothing," don't send it.

### Stated Is Not Done

What people say they'll do and what they do diverge, and surveys capture the first. "Would you use
this?" gets yes from people who never will. Ask about **past behavior** ("When did you last
rebuild your schedule by hand?") rather than **future intent** ("Would you use a tool that...?").

### Bias Lives in Four Places

- **Question bias.** Leading ("How much do you love..."), loaded, double-barreled (two questions in
  one), or full of jargon. Neutral wording, one idea per question.
- **Scale and order bias.** Early options and positive anchors get picked more. Randomize options
  where order is meaningless, and use balanced scales.
- **Sample bias.** The people who answer are the ones who like you, have time, or were reachable.
  A survey sent to your newsletter describes your newsletter.
- **Non-response bias.** Silence is data: the busiest and the unhappiest often don't answer.

### Sample: Who, and How Many

Define **who you need to hear from** before the question list. Then ask where they are and whether
you can reach them. A small, well-chosen sample of the right people beats a large one of whoever
replied. Say what the result **can claim**: "of the 140 plant engineers who responded from our
partner lists" is honest; "the market" is not. Don't promise statistics a response count can't
carry.

### Length and Question Types

Short wins: every extra question loses people, and the last ones get rushed answers. Put the
**most important questions first**, keep it under a few minutes, and use **closed questions** for
measurement and **one or two open questions** for the things you didn't think to ask. A required
open text box at the end is where the real finding often hides.

### Test It Before You Send It

Have five people from the target group take it aloud and tell you what each question meant to
them. Misread questions show up in five minutes and ruin a thousand responses.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol:
heads-up, one question per turn, numbered options, and best-guess mode on request.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not a survey generator.** It decides the method and shapes the design; the questions are yours to own.
- **Not a statistics tool.** It won't compute significance on a thin response set.
- **Not a substitute for interviews.** If you don't know what to ask, talk to people first.

---

## Application

This skill asks **up to 4 adaptive questions**, then recommends a design (or a different method).

### Question 1 of 4: What do you want to learn, and what will you do with it?

**Agent asks:**

"What do you want to find out, and what decision will the answer change?"

**Listen for the method hidden in the question.** "Why do customers churn?" is an interview question.
"What share of accounts use feature X?" is usage data. "How many plants run aging controllers?" is a
survey (or a purchased list). If no decision depends on it, say so and stop.

### Question 2 of 4: Is this about how common, why, or what they'll do?

**Agent asks:**

"Which is closer to what you need?

1. **How common is something** (how many, how often, which of these)
2. **Why something happens, or what problems exist** (reasons, causes, unknowns)
3. **What people will do or pay** (future behavior, willingness to pay)
4. **Not sure**"

**Route:** 1 → survey fits. 2 → recommend interviews, and offer a short survey *after* to size what
they found. 3 → warn that stated intent overstates behavior; recommend a priced or committed test
([`pol-probe-advisor`](../pol-probe-advisor/SKILL.md)) with a survey only as a supplement. 4 → help
them name it.

### Question 3 of 4: Who do you need to hear from, and can you reach them?

**Agent asks:**

"Who exactly should answer, and how will you reach them?

1. **Our own customers** (email, in-app)
2. **Prospects or a market segment** (a list, panel, or partner channel)
3. **People through partners or resellers**
4. **I'm not sure who I need**"

**Use it to name the sampling bias** (own customers = engaged customers; partners = partner-served)
and what the results can and cannot claim. Ask how many they can realistically reach.

### Question 4 of 4: How long and what shape?

**Agent asks:**

"How much of their time can you ask for, and do you already have a draft?"

**Fit the design:** under 3 minutes, 8-12 closed questions plus one open; most important first;
neutral wording; past behavior, not future intent. If a draft exists, critique it first: quote each
leading, loaded, or double-barreled question and say why.

### Final Step: Recommend the design

```markdown
## Survey Recommendation: [what you're learning]

**Verdict:** [Survey fits / Interviews first / Usage data first / Priced test instead]
**Why:** [one or two lines tied to their answers]

### If a survey: the design
- **Who:** [target and reach, and what the results can claim]
- **Questions:** [about N, closed vs open, order, past-behavior framing]
- **Bias controls:** [neutral wording, randomized options, balanced scales]
- **Sample and what it can't say:** [size realistic, non-response caveat]
- **Test first:** five people from the target group, read aloud

### Questions to fix (if a draft was supplied)
| Question | Problem | Rewrite (option to accept, adapt, or reject) |

### Next
1. [skill or action]
2. [skill or action]
```

---

## Examples

### Example A: SaaS, "would they pay?"

**User:** "We want to know if customers would pay for the Route Optimizer. Let's survey the base."

**Agent (Q2):** "Which is closer: how common something is, why it happens, or what people will do
or pay?" → **3 (will pay).**

**Agent:** "Stated willingness to pay overstates real behavior, and a survey to your own customers
reaches your most engaged ones. A survey can tell you how many feel the rescheduling pain. It can't
tell you they'll pay. Here's what I'd do:"

**Verdict:** *Interviews first, then a priced test.* Ask 6-8 dispatchers about the last time they
rebuilt the day (past behavior). Then offer the add-on at a real price to a small group and count who
signs up ([`pol-probe-advisor`](../pol-probe-advisor/SKILL.md)). If you still want a survey, use it to
size the pain ("In the last two weeks, how many times did you rebuild the day by hand?"), not
willingness to pay.

### Example B: Industrial, "how many plants?"

**User:** "How many mid-size plants run controllers older than ten years? We need to size the retrofit market."

**Agent (Q2):** → **1 (how common).** "A survey fits, with a caution about who you can reach."

**Agent (Q3):** "Partners reach plants they already serve, so the results describe partner-served
plants, not the market." → **3 (through partners).**

**Verdict:** *Survey fits, scoped honestly.* About 10 closed questions, controller age and count
first, one open question on what stops replacement. Send through partners and say the result speaks
to partner-served plants. Test with five maintenance engineers. Pair it with the market-sizing
skill ([`tam-sam-som-calculator`](../tam-sam-som-calculator/SKILL.md)) rather than extrapolating.

---

## Common Pitfalls

### Pitfall 1: Surveying to Discover
**Symptom:** A survey sent to find out what problems exist.
**Consequence:** You get answers to the questions you wrote and miss the ones you didn't.
**Fix:** Interview first, then survey to measure what you found.

### Pitfall 2: Asking About the Future
**Symptom:** "Would you use...?" "Would you pay...?"
**Consequence:** Optimistic yeses that don't turn into behavior.
**Fix:** Ask about past behavior, or test with a real commitment.

### Pitfall 3: Leading and Double-Barreled Questions
**Symptom:** "How satisfied are you with our fast, reliable support?"
**Consequence:** Two questions, one answer, and a nudge.
**Fix:** One neutral idea per question.

### Pitfall 4: Surveying Your Friends
**Symptom:** Sent to the newsletter or the most engaged customers.
**Consequence:** The data describes your fans.
**Fix:** Name the sample, and say what the result can't claim.

### Pitfall 5: Claiming More Than the Sample Supports
**Symptom:** "The market wants X," from 60 replies.
**Consequence:** A decision rests on a number that looks bigger than it is.
**Fix:** Report counts, the reach, and the non-response.

### Pitfall 6: No Test Run
**Symptom:** Sent without anyone reading it aloud first.
**Consequence:** A thousand responses to a question nobody understood.
**Fix:** Five people from the target group, read aloud.

---

## References

### Related Skills
- [`discovery-interview-prep`](../discovery-interview-prep/SKILL.md): find out what to ask
- [`research-synthesis`](../research-synthesis/SKILL.md): make sense of open-ended answers
- [`usage-data-investigation`](../usage-data-investigation/SKILL.md): what people actually do
- [`pol-probe-advisor`](../pol-probe-advisor/SKILL.md): test real commitment cheaply
- [`tam-sam-som-calculator`](../tam-sam-som-calculator/SKILL.md): market sizing
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Past behavior over stated intent:** Rob Fitzpatrick, *The Mom Test*.
- **Survey bias (question, order, sampling, non-response):** standard survey methodology, for example Don Dillman, *Internet, Phone, Mail, and Mixed-Mode Surveys*.

### Provenance
Distilled from practitioner experience designing and reviewing customer surveys for B2B and industrial products.
