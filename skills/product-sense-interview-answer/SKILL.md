---
name: product-sense-interview-answer
description: Structure a spoken PM product-sense answer with assumptions, segmentation, pain-point prioritization, and MVP tradeoffs. Use when practicing design, improve, or build-next interview questions.
compatibility: opencode
argument-hint: "[interview prompt]"
metadata:
  best_for:
    - "Practicing product design and product improvement interview questions"
    - "Coaching candidates who jump to solutions too quickly"
    - "Turning messy ideation into a crisp spoken interview answer"
  estimated_time: "20-30 min"
  intent: >-
    Coach PM candidates through open-ended product-sense interviews using a repeatable
    six-part answer spine: clarify, rationale, goal, segmentation, pain points,
    and solution choice. Use this to practice product design and product improvement
    questions, avoid solution-first answers, and produce responses that sound
    thoughtful out loud rather than over-scripted on the page.
  scenarios:
    - "How would you improve YouTube?"
    - "Design a product for travelers with flight anxiety"
    - "What would you build next for DoorDash?"
  theme: career-leadership
  type: component
---

## Purpose

Help PM candidates and interview coaches structure product-sense answers that sound strong out loud, not just on paper. Use this when practicing prompts like "How would you improve X?", "Design a product for Y", or "What would you build next for Z?"

This is not a memorize-and-recite script. It is a reasoning scaffold that prevents solution-jumping, forces real prioritization, and leaves the interviewer with a clean story they can follow.

## Input

**Works best with:** The interview prompt you're practicing (e.g., 'How would you improve X?', 'Design a product for Y').
**Also useful:** The company/role you're interviewing for and how much time the answer gets.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** The skill asks for the prompt, then walks the reasoning scaffold with you out loud.

**Example invocation:** `Practice this: 'How would you improve Google Maps for commuters?' — 25-minute answer, L5 PM loop.`

## Key Concepts

### What Product Sense Interviews Actually Test

Strong product-sense answers do more than generate ideas. Interviewers are usually testing whether you can:

- Clarify ambiguous prompts without getting stuck
- Tie user value to market or business logic
- Segment thoughtfully instead of talking about "everyone"
- Prioritize one pain point instead of describing ten equally
- Make tradeoffs explicit when choosing an MVP
- Communicate clearly under time pressure

### The Six-Part Answer Spine

1. **Clarify** - Reduce ambiguity, define scope, and state assumptions.
2. **Rationale** - Explain why the problem matters now for the market and, if relevant, the company.
3. **Product Goal** - Define the user outcome you want to create before talking about features.
4. **Segmentation** - Choose who to serve first and show why that target wins.
5. **Pain Points** - Map the journey, name the main frictions, and pick the one worth solving first.
6. **Solution** - Generate distinct options, compare them, and commit to one MVP with clear exclusions.

The order matters. If you skip from prompt to feature ideas, your answer sounds clever but ungrounded. If you establish the user, goal, and pain first, your solution feels earned.

### Why This Works

- **Prevents feature dumping:** You do not start with ideas before you know whose problem you are solving.
- **Balances user and business thinking:** The answer includes demand, company fit, and strategic tradeoffs rather than pure UX talk.
- **Creates a speakable narrative:** Each section becomes a short checkpoint the interviewer can follow.
- **Forces prioritization:** Reach, impact, fit, frequency, severity, and effort all surface tradeoffs instead of hand-wavy optimism.

### Anti-Patterns (What This Is NOT)

- **Not a feature brainstorm:** Listing ideas without choosing a target user or problem is not product sense.
- **Not a TAM presentation:** You do not need made-up market numbers to sound strategic.
- **Not a memorized monologue:** Rigid scripts break as soon as the interviewer redirects or narrows scope.
- **Not a business-case-only answer:** Product sense still requires empathy, behavior, and user context.

### When to Use This

- Product design questions
- Product improvement questions
- "What would you build next?" prompts
- Mock interviews where you want a repeatable spoken structure

### When NOT to Use This

- Behavioral interviews that need STAR stories
- Execution and analytics cases that revolve around metrics diagnosis
- Go-to-market or pricing interviews where distribution or monetization is the main problem

## Application

Use [`template.md`](template.md) as the working structure.

### Delivery Rules

- State your structure early so the interviewer knows where you are going.
- Ask only 1-2 clarifying questions. More than that feels like stalling.
- Keep lists MECE where possible: segments should be distinct, pain points should not overlap, and solutions should not be three versions of the same thing.
- Speak in short sentences. Interview answers should sound conversational, not like a memo read aloud.
- If the prompt does not name a company, use a startup assumption and skip fake company-mission talk.

### Step 1: Clarify the Prompt

Start by surfacing the two ambiguities that change the answer most. Good clarifiers usually narrow:

- Product or surface area
- User group
- Time horizon
- Business model or operating constraints

If the interviewer does not answer, state your assumptions and move on. The goal is to unblock the rest of the answer, not to turn the interview into requirements gathering.

**Quality bar:** Ask questions that materially change the solution. "Are we talking mobile or desktop?" matters less than "Are we optimizing for viewers, creators, or advertisers?"

### Step 2: Build the Rationale Before the Feature

Explain why the space matters now.

For the market view, cover:

- Why the market is big or strategically important
- Why the problem matters to real people
- Why now is a good moment to act

If a company is named, then add:

- Mission fit
- Business objective
- Competitive landscape
- Market gap
- Unique strength

End this section with a one-line thesis. That thesis should make the rest of the answer feel inevitable.

**Quality bar:** Use qualitative signals unless you know the numbers cold. Fake precision is worse than grounded judgment.

### Step 3: Define the Product Goal

Write one sentence in this format:

`Help [user] [achieve outcome], so that [broader impact].`

Then describe what success looks like for the user in observable terms.

**Good:** "Help beginner YouTube learners find content they are glad they watched, so that the platform becomes an intentional learning destination."

**Bad:** "Build a personalized AI learning path feature." That is a solution disguised as a goal.

### Step 4: Segment the Market and Pick a Target

Do not jump straight to persona. First identify the ecosystem players, then choose the player you want to serve. After that, choose two segmentation dimensions that actually change needs.

Good segmentation dimensions usually change:

- Goal or job to be done
- Stakes or consequence level
- Expertise level
- Workflow constraints
- Frequency of the problem

Weak dimensions are often demographic cuts that do not change the product meaningfully.

After choosing your target segment:

- Give a brief reach / impact / strategic-fit rationale
- Write a two-sentence persona
- Keep the persona free of pain points; pain comes next

### Step 5: Map Pain Points and Prioritize One

Break the user journey into 4-6 stages. Then list the frictions across that journey.

Prioritize the top pain point using:

- **Frequency** - how often the user hits it
- **Severity** - how badly it blocks the job, how underserved it is, and the emotional cost

This is the fulcrum of the entire answer. If the pain point is vague or weak, the solution section becomes generic.

**Quality bar:** Pain points should describe user friction, not missing features. "No structured progression after each video" is a pain. "No AI learning path" is already a solution.

### Step 6: Generate Options, Choose an MVP, and Close

List three distinct solutions. They should solve the same pain in different ways, not represent three feature line-items inside one idea.

Evaluate each option on:

- User impact
- Effort

Then choose one MVP and specify:

- Core features
- 1-2 explicit v1 exclusions
- Top risks and mitigations

Close with a one-sentence recap that names:

- Target segment
- Top pain point
- First bet

That final sentence is what the interviewer should remember.

## Examples

### Good Example: Improve YouTube for Beginner Learners

See [`examples/improve-youtube.md`](examples/improve-youtube.md) for a full worked example.

What makes it strong:

- It chooses one player first: viewers, not "everyone in the ecosystem"
- It segments by learning intent and expertise level, which both change needs materially
- It picks one pain point: no structured progression across videos
- It compares multiple solutions before choosing Learning Paths as the MVP

### Good Example: Design a Fire Alarm for the Deaf

A strong answer to this prompt would explicitly state a startup assumption if no company is named, prioritize people who live alone, and choose the wake-up problem before discussing dispatch or smart-home integrations.

What makes this example useful:

- The target segment is clear and high-stakes
- Severity matters more than broad reach
- Hardware, software, and ecosystem constraints are part of the reasoning

### Anti-Pattern Example

"I would improve YouTube by adding AI summaries, better recommendations, creator analytics, and a study mode."

Why this fails:

- No target user
- No prioritized pain point
- No business or market logic
- Four ideas that were never compared against each other

This kind of answer can sound energetic in the moment, but it signals weak PM judgment.

## Common Pitfalls

- **Solution-first thinking:** You start pitching features before naming the user or problem. Fix it by forcing yourself to write the product goal and top pain point before brainstorming solutions.
- **Segmentation theater:** You list many segments, then pick one with no tradeoff logic. Fix it by explicitly comparing reach, impact, and strategic fit.
- **Goal-as-feature:** Your "goal" describes the thing you want to build. Fix it by rewriting it as a user outcome.
- **Pain points that are really solutions:** "Users need a dashboard" is not a pain point. Rewrite in user-language first.
- **Three fake options:** Your three solutions are really one solution with minor variations. Fix it by varying the product mechanism, not just the packaging.
- **Weak close:** You end after listing features. Fix it by restating the target segment, the pain, and the first bet in one sentence.
- **Over-answering every branch:** You try to prove breadth instead of making choices. Product-sense interviews reward focus more than exhaustiveness.

## References

- [`template.md`](template.md)
- [`examples/improve-youtube.md`](examples/improve-youtube.md)
- [`skills/problem-statement/SKILL.md`](../problem-statement/SKILL.md)
- [`skills/proto-persona/SKILL.md`](../proto-persona/SKILL.md)
- [`skills/customer-journey-map/SKILL.md`](../customer-journey-map/SKILL.md)
- [`skills/opportunity-solution-tree/SKILL.md`](../opportunity-solution-tree/SKILL.md)
- Lewis C. Lin, *Decode and Conquer*
- Gayle Laakmann McDowell and Jackie Bavaro, *Cracking the PM Interview*
