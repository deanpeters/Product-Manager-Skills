---
name: stakeholder-engagement-advisor
description: Plan engagement for a specific stakeholder. Use when preparing an outreach, navigating resistance, or aligning a critical relationship before a key milestone.
compatibility: opencode
argument-hint: "[stakeholder and situation]"
metadata:
  best_for:
    - "Preparing to engage a powerful executive sponsor whose support is critical but whose motivations are unclear"
    - "Planning outreach to a resistant or skeptical stakeholder who could block your roadmap"
    - "Navigating first contact with a newly identified stakeholder mid-initiative"
    - "Designing inclusive engagement for a Q1 (high-impact, low-power) user community that needs more voice"
    - "Aligning cross-functional engagement strategy before a high-stakes roadmap review or launch"
  intent: >-
    Guide per-stakeholder engagement planning through the Adaptive Decision Ladder:
    three targeted questions diagnose the stakeholder's profile, power/impact quadrant,
    and your engagement context, then deliver a tailored approach — key message framing,
    recommended medium and cadence, what you need from them versus what they need from
    you, and a named next action with owner and deadline. Treats both sides of the
    relationship, not just yours.
  scenarios:
    - "Help me plan how to engage [stakeholder] before my roadmap review"
    - "I have a resistant stakeholder — how do I approach them?"
    - "I need to bring a new executive sponsor up to speed quickly"
    - "How do I engage frontline users who've been excluded from our feedback loops?"
    - "Help me prepare a 1:1 with someone who could block this initiative"
  sources:
    - "MITRE Innovation Toolkit — Quickstart Stakeholder Engagement Canvas: https://itk.mitre.org/toolkit-tools/quickstart-stakeholder-engagement-canvas/"
  type: interactive
---

# Stakeholder Engagement Advisor

## Purpose

Plan how to engage a specific stakeholder — before a critical conversation, milestone, or relationship repair. Generic stakeholder engagement fails because it treats all stakeholders with the same message, medium, and cadence. An executive sponsor who privately disagrees with your direction needs different handling than an impacted frontline user who's never been consulted. This skill diagnoses the specific stakeholder relationship you're managing and delivers a tailored engagement approach that accounts for both sides of the conversation — their motivations and yours.

Run this skill once per priority stakeholder. Priority stakeholders are those in the "manage closely" quadrant from stakeholder-mapping, every Q1 (high-impact, low-power) stakeholder regardless of Power × Interest placement, and anyone who has the potential to block, delay, or fundamentally reshape your initiative.

## Input

**Works best with:** The specific stakeholder and the situation — the conversation, milestone, or tension you're preparing for.
**Also useful:** Their power/interest read, history with you or the initiative, and what a good outcome looks like.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** The advisor opens by asking who the stakeholder is and what's coming up with them.

**Example invocation:** `Plan engagement: our VP Sales publicly supports the replatform but keeps escalating exceptions — QBR in 2 weeks.`

## Key Concepts

**Stakeholder Motivations vs. Your Motivations** — The most common engagement failure is planning only your side of the conversation. Effective stakeholder engagement requires mapping what the stakeholder needs, wants, and fears — separately from what you need from them. Where these overlap, you have an alignment path. Where they diverge, you have a negotiation to prepare for.

**Proxy** — A credible representative who speaks for or stands in for a stakeholder who is hard to reach, part of a large group, or represents a community rather than an individual. A good proxy is validated: they understand and can speak for the people they represent. A convenient proxy — the person who shows up to meetings — often cannot. Name the proxy explicitly and verify their representativeness before relying on their input.

**Analysis Before Action** — The engagement plan has two phases: diagnosis (who is this person, what drives them, what is the relationship history?) and planning (what will you say, through which medium, with what desired outcome?). Teams that skip directly to planning produce tactics without foundation — a message crafted for the wrong motivation, a medium that signals the wrong level of importance, an ask that misreads what the stakeholder actually controls.

**Equity Lens in Engagement** — High-impact, low-power stakeholders (Q1 from stakeholder-mapping) require proactive engagement design, not an open-door policy. An open door serves the people who already know they have a seat at the table. Q1 stakeholders typically need you to go to them: structured research recruitment, named roles in review processes, and deliberate inclusion in decisions that affect them.

**Next Action Commitment** — Every engagement plan must end with a named next action: who does what, by when, through which medium, with what key message and desired outcome. Engagement plans without this commitment are intentions, not plans. The next action is the only part that actually moves the relationship forward.

**Engagement Context** — The situational frame around the engagement matters as much as the stakeholder profile. Preparing for a first contact requires different framing than recovering from a conflict, securing buy-in before a launch, or maintaining an already-aligned relationship. The context shapes the message, the medium, and the desired outcome.

## Application

This skill runs as a guided conversation. Answer each question; the advisor synthesizes your inputs and delivers a tailored engagement plan structured around three decision points:

1. **Stakeholder profile** — who they are and what role they play
2. **Power and impact** — how much authority they hold vs. how much they're affected
3. **Engagement context** — the situation you're preparing for

After all three, you receive a set of numbered engagement approaches to choose from, then a specific action plan.

---

**Opening**

> "We're going to plan your engagement with a specific stakeholder. I'll ask three questions about them and the situation, then deliver a tailored approach — message framing, medium, cadence, and your next action.
>
> Who is this stakeholder? Give me their name, role, and one sentence on the history of your relationship with them so far."

---

**Question 1 of 3 — Stakeholder profile**

> "Which of the following best describes this stakeholder?
>
> 1. **Executive sponsor or senior decision-maker** — holds formal authority over scope, budget, or go/no-go; your initiative needs their active support or at minimum their absence of resistance
> 2. **Cross-functional peer or partner** — adjacent team lead whose capacity, systems, or process your initiative touches; peer relationship, not a reporting one
> 3. **End user or community representative** — the person or group who will live with the product's outcomes daily; may have limited org power but high stakes in the result
> 4. **Skeptic or potential blocker** — has publicly or privately expressed resistance, doubt, or competing priorities; could slow or derail the initiative if not addressed
> 5. **Newly identified stakeholder** — discovered mid-initiative; relationship history is thin or nonexistent"

*Based on the answer, tailor the next question and the eventual recommendation.*

---

**Question 2 of 3 — Power and impact profile**

> "Looking at this stakeholder's position from your stakeholder mapping — or your best read if you haven't mapped formally yet:
>
> 1. **High power, high impact** — they can shape the initiative AND they're significantly affected by its outcome (e.g., the VP whose team's workflow changes and who controls the budget)
> 2. **High power, low impact** — they control resources or approval but aren't significantly affected day-to-day (e.g., a CFO approving budget for a product they'll never use)
> 3. **Low power, high impact** — they're directly affected by the product's outcome but have limited org authority to shape it (e.g., frontline users, support agents, end communities)
> 4. **Low power, low impact** — limited stakes and limited authority; still worth mapping but engagement investment should be proportionate"

---

**Question 3 of 3 — Engagement context**

> "What's the situation you're preparing for?
>
> 1. **First contact** — establishing a relationship and earning credibility before the work gets political
> 2. **Pre-milestone alignment** — roadmap review, launch gate, OKR commitment, or exec briefing coming up; you need this stakeholder in a good place beforehand
> 3. **Resistance or conflict** — the stakeholder has expressed disagreement, is blocking progress, or has competing priorities that put them at cross-purposes
> 4. **Elevating an underrepresented voice** — this is a Q1 stakeholder who has been excluded from or underrepresented in decision-making; you're designing proactive inclusion
> 5. **Ongoing maintenance** — an existing, aligned relationship that needs sustained investment to stay that way"

---

**Synthesis and recommendations**

After all three answers, deliver a tailored engagement plan:

> "Based on [stakeholder type], [power/impact profile], and [engagement context], here are your recommended approaches:
>
> **1. [Approach name]** — [When this fits and what it accomplishes]
> **2. [Approach name]** — [Alternative for different risk tolerance or timeline]
> **3. [Approach name]** — [Option for higher or lower relationship investment]
>
> Choose a number, combine approaches (e.g., '1 then 3'), or describe your situation in more detail."

*After selection, deliver the specific plan:*

- **Key message:** What is the single most important thing you want them to understand or believe after this interaction?
- **Framing:** How does this initiative connect to what they care about? Lead with their goals, not yours.
- **Medium and format:** Email, 1:1, group briefing, written pre-read, working session, or research participation? Why this medium for this stakeholder?
- **Cadence:** One-time touchpoint or recurring? At what frequency?
- **What you need from them:** Be specific — a decision, an approval, information, validation, or simply awareness.
- **What they likely need from you:** Based on their profile — transparency, influence over design, credit for contribution, assurance about risk, or proof of impact.
- **Next action:** [Owner] will [action] via [medium] by [date/milestone], with the message "[key message]" and the desired outcome "[what success looks like for this interaction]."

---

**Handling edge cases**

- If the stakeholder is a large group (e.g., a user community): shift to proxy identification — name the most credible representative, validate their alignment to the group, design engagement through them while building broader touchpoints over time.
- If the relationship has history of conflict: lead with listening before proposing; the goal of the first engagement is to understand their concerns, not to persuade.
- If the engagement plan feels implausible given timeline or access constraints: scope down to what's achievable and name the residual risk explicitly.

## Examples

**Sample conversation flow — Executive sponsor, pre-milestone**

> *Advisor:* "Who is this stakeholder?"
> *User:* "SVP of Product — she's the exec sponsor. We've had two brief introductions at all-hands. She's publicly supportive but we've never had a real conversation about what she actually thinks about the approach."
>
> *Advisor:* "Which profile fits best: 1-5?" [see Question 1]
> *User:* "1 — Executive sponsor."
>
> *Advisor:* "Power and impact?" [see Question 2]
> *User:* "1 — High power, high impact. Her org uses the product and she controls the Q3 budget commitment."
>
> *Advisor:* "Engagement context?" [see Question 3]
> *User:* "2 — Pre-milestone. Roadmap review in three weeks."
>
> *Advisor:* "Recommended approaches:
> 1. **Pre-read + 1:1 alignment** — Send a two-page executive brief 5 days before the review, then request a 30-minute 1:1 to walk through it. Goal: surface her unstated concerns before the room hears them first.
> 2. **Working session** — Invite her into a 60-minute pre-review working session to shape the framing. Higher investment, but earns genuine co-ownership.
> 3. **Informal check-in** — A brief hallway or coffee conversation, no slides. Lower risk if her support is likely solid; insufficient if there's a 30% chance of a surprise objection.
>
> *Key message:* 'Here's where we are, why we made these calls, and the three decisions we need your guidance on.'
> *What she likely needs from you:* Evidence that you've managed the political risks she'd have to defend upward.
> *Next action:* [You] send executive brief to [her EA] by [date minus 5 days], request 30-minute slot before the review, with the message: 'I want to walk you through the direction and make sure you have what you need for the room.'"

---

**Sample flow — Frontline users, elevating underrepresented voice**

> *Advisor:* "Who is this stakeholder?"
> *User:* "Customer support agents — about 40 people. We've never talked to them during this initiative even though their tooling changes completely."
>
> *Profile:* 3 (End user / community representative)
> *Power/Impact:* 3 (Low power, high impact — Q1)
> *Context:* 4 (Elevating underrepresented voice)
>
> *Advisor:* "Recommended approach:
> 1. **Structured research recruitment** — Recruit 5-8 agents for a 30-minute discovery interview using the discovery-interview-prep skill. This gives you validated insight before requirements are locked and signals that their perspective shapes the product.
> 2. **UAT role with feedback loop** — Include agents in user acceptance testing with a clear feedback mechanism. Commit publicly to reporting back what changed because of their input.
> 3. **Proxy identification** — If direct access is limited, identify the team lead or most experienced agent who can credibly represent the group. Validate their representativeness with the team before relying on their input.
>
> *Key message:* 'We want to understand how this changes your day-to-day work before we finalize the design.'
> *Next action:* [You] coordinate with support manager by [date] to schedule 5 discovery interviews, with the message: 'We're redesigning intake and need the team's perspective to get it right.'"

## Common Pitfalls

**Planning only your side of the conversation.** An engagement plan that focuses entirely on your message and your ask treats the stakeholder as an audience to persuade rather than a person with their own goals, fears, and constraints. Map their motivations first. The message that lands is the one that connects to what they care about.

**Running it on every stakeholder regardless of priority.** Per-stakeholder engagement planning takes time. Reserve it for high-stakes relationships: "manage closely" stakeholders, Q1 stakeholders, and anyone who can block or derail. Monitor-tier stakeholders don't need a tailored plan.

**Treating the engagement plan as permanent.** Stakeholder relationships evolve. A successfully pre-aligned sponsor can become skeptical after a bad sprint review. An initially resistant peer can become an ally once they see their concern addressed. Revisit the plan after major milestones.

**Substituting a convenient proxy for a credible one.** The person who shows up to meetings and is easy to reach is often not the person who can accurately represent the group they nominally speak for. A credible proxy is validated — they've confirmed their own alignment with the group they represent.

**Ending without a named next action.** An engagement plan without owner, action, medium, and deadline is an intention. Intentions don't move relationships forward. The next action is the only output that matters.

**Using the same medium for all stakeholders.** An executive who's already in back-to-back meetings doesn't need another meeting — they need a well-written pre-read. A frontline user who's never been consulted doesn't need an email — they need a face-to-face research session that signals their perspective actually matters. Match the medium to the relationship and context.

## References

- [stakeholder-identification](../stakeholder-identification/SKILL.md) — prerequisite: build the stakeholder list before planning per-stakeholder engagement
- [stakeholder-mapping](../stakeholder-mapping/SKILL.md) — prerequisite: prioritize stakeholders and identify Q1 voices before engagement planning
- [discovery-interview-prep](../discovery-interview-prep/SKILL.md) — for engaging user stakeholders through structured research
- [workshop-facilitation](../workshop-facilitation/SKILL.md) — for facilitation-heavy engagement formats like working sessions and co-design
- MITRE Innovation Toolkit — [Quickstart Stakeholder Engagement Canvas](https://itk.mitre.org/toolkit-tools/quickstart-stakeholder-engagement-canvas/)
