# Example Conversation Flow — incoming-request-advisor

A full end-to-end interaction: message extraction, one gap-filling question, the rendered breakdown, and the closing options. Names and details are anonymized.

---

**User:**

> incoming-request-advisor
>
> Screenshot attached. It's a Slack thread. My eng lead posted it in our team channel this morning.

*(attached image contains:)*

> **Priya Nadel** (Director of Engineering)
> "Team — leadership wants the AI summarization feature demoable by the all-hands on the 30th. I know discovery isn't done but we need SOMETHING on screen. Can product commit to a scope by EOD so we can start? Not looking for the full thing, just don't want to show up empty-handed."

---

**Agent:**

I've extracted the message. It's readable in full. One thing changes the read before I analyze:

**Do you want analysis only, or a drafted reply too?**

---

**User:**

> Analysis first. I'll decide on a reply after.

---

**Agent:**

## Incoming Request Breakdown

### 1. Classify
- Mandate with deadline, Slack thread

### 2. Sender Read
- Priya Nadel, Director of Engineering
- Relationship: peer, high influence
- Relaying leadership pressure downward

### 3. Literal Ask
- Commit demo scope by EOD

### 4. Underlying Problem Space
- Leadership wants visible AI progress
- Job: avoid empty-handed all-hands
- Outcome is credibility, not shipped feature

### 5. Sentiment and Subtext
- Urgent, slightly defensive tone
- Tell: "just don't want to show up empty-handed"
- Cover-me energy, not malice

### 6. Must-Haves vs Nice-to-Haves
- Must: something on screen by the 30th
- Nice: real summarization accuracy

### 7. Hard Negatives
- Not the full feature
- No expectation of production quality

### 8. Success Criteria
- Leadership sees credible progress (inference)
- All-hands demo does not embarrass team (inference)

### 9. Hard Constraints
- All-hands date: the 30th
- Scope decision wanted by EOD

### 10. Gaps and Ambiguities
- Who in leadership is actually asking
- What "demoable" means to them
- Is discovery still allowed to continue

### 11. Risks
- EOD scope lock precedes discovery
- Demo becomes the de facto spec
- Scope creep after the demo lands

### 12. Recommended Next Steps
- Confirm what leadership needs to see
- Offer a thin demoable slice
- Protect discovery timeline in writing

### Assumptions to Validate
- Success is credibility, not shipped feature
- "Leadership" is unnamed and unconfirmed
- Discovery can continue past the demo

---

Two questions sharpen this:

1. Is the all-hands date on the 30th actually fixed, or aspirational?
2. Does leadership need working software, or a credible plan-plus-mockup?

Now, pick your next move:

1. **Draft a reply to Priya** (Recommended)
2. **Build a meeting agenda for this ask**
3. **Reframe the ask as a discovery framing**
4. **Draft a counter-proposal that protects the outcome**

Reply with `1`, `2`, `3`, `4`, a combination like `1 and 4`, or describe your own path.

---

**User:**

> 1 and 4

---

**Agent:**

Blending them: a reply to Priya that *is* the counter-proposal — commits to a thin, honest slice by the 30th while protecting the discovery track.

> "Priya — yes, we'll have something demoable by the 30th. Proposing we show a working summarization slice on one real document type (support tickets), with a clear 'here's what's next' framing rather than implying it's done. That gets leadership a credible on-screen story without locking full scope before discovery closes. I'll send the one-pager by EOD. Sound right?"

Want me to tighten the tone, add the one-pager outline, or draft the discovery-protection note for leadership?
