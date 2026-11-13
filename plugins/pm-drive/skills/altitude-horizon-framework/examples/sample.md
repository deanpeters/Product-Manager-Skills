# Altitude-Horizon Framework Examples

This file shows how to apply the framework in a realistic PM-to-Director transition scenario.

---

## Example 1: Good Use of the Cascading Context Map

### Scenario

Company priority from CEO: "Win larger enterprise deals this year."

A newly promoted Director has three PMs asking: "What does that mean for our roadmaps this quarter?"

### Completed Context Cascade

```markdown
## Context Cascade

**Company Priority:** Win larger enterprise deals this year.

**Business Unit Translation:** Increase average contract value and reduce time-to-security-approval for enterprise prospects.

**Product Portfolio Translation:**
- Product A: strengthen admin controls and role permissions
- Product B: improve API documentation and integration reliability
- Product C: close SOC 2 and SSO adoption gaps

**Team Accountabilities:**
- Team A owns admin controls and audit logs
- Team B owns API docs, SDK quality, and integration examples
- Team C owns security certifications and SSO implementation quality

**Why this matters:**
Enterprise growth does not mean "build random enterprise features."
It means removing blockers that stall enterprise deals and procurement.
```

### Why This Is Strong

- Translates vague strategy into concrete team ownership.
- Preserves altitude: portfolio and outcomes first, backlog details second.
- Makes trade-offs visible: what changes now vs. later.

---

## Example 2: Anti-Pattern (Hero Syndrome)

### Scenario

A PM escalates a conflict with Sales about roadmap commitments.

### Director Response (Weak)

"I will jump into the account call and handle this for you."

### Director Response (Strong)

"Walk me through your current framing. I will coach your next move, then you lead the conversation."

### Why the First Response Fails

- Solves immediate pain but reinforces dependency.
- Keeps the Director in PM-level conflict resolution.
- Prevents PM growth on stakeholder leadership.

### Better Follow-Through

1. Debrief the PM's framing.
2. Align on one clear message and one fallback position.
3. Let PM lead with Director in support.
4. Post-call: identify one behavior to improve next time.

---

## Example 3: Altitude Calibration Check

Use this quick self-audit before major decisions:

- Am I deciding at team/backlog altitude or portfolio altitude?
- Who should own this decision at my current role level?
- If I step in, am I building system clarity or rescuing execution?
- What context translation is missing for the team right now?

If most answers point to execution rescue, you are likely slipping into Hero Syndrome.
