# PRD Examples

## Example 1: Good PRD Excerpt (Guided Onboarding)

A well-structured PRD using the template conventions — inline assumption/open-question tagging, evidence-backed claims, and a self-assessment at the end.

### Section 2 — Problem Statement

**Who Has This Problem?**

Non-technical small business owners — solopreneurs and teams of 1–10 — who sign up for our SaaS product for the first time.

**What Is the Problem?**

60% of users abandon onboarding within the first 24 hours because they don't know what to do first. They see an empty dashboard with no guidance, get overwhelmed by options, and leave.

**Why Is It Painful?**

- **User impact**: Wastes 30–60 minutes trying to figure out the product, never reaches the "aha moment," churns before experiencing value.
- **Business impact**: 60% activation failure drives high churn, low LTV, and poor word-of-mouth.

**Evidence**

- **Interviews**: 8 of 10 churned users said "I didn't know what to do first" — discovery interviews, Feb 2026.
- **Analytics**: 60% of signups complete zero actions within 24 hours — Mixpanel, Jan 2026.
- **Support signals**: "How do I get started?" is the #1 support question — 350 tickets/month.
- **Customer quote**: "I logged in, saw an empty dashboard, and thought 'now what?' I gave up and went back to my spreadsheet."

**Why this works:**
- Evidence from three independent sources (interviews, analytics, support tickets)
- Quantified business impact (60% activation failure, LTV consequences)
- Verbatim customer quote grounds the problem in real experience

---

### Section 6 — Success Metrics (with inline tagging)

**Primary Metric**

- **Metric**: Activation rate — % of users completing first action within 24 hours
- **Current**: 40%
- **Target**: 60% 🔶 **Assumption**: Target based on industry benchmark for comparable B2B SaaS onboarding improvements — not validated against our specific user base.
- **Timeline**: 30 days after launch

**Secondary Metrics**

- Time-to-first-action: reduce from 3 days to 1 day
- Onboarding checklist completion rate: target 80%
- Support ticket volume for "How do I get started?": reduce from 350/month to 175/month

**Guardrail Metrics**

- Sign-up conversion rate: maintain at 10% — don't add friction to the signup flow
- 🔵 **Open Question**: Should we also track session duration as a guardrail? If checklist completion inflates session time without delivering value, we could be measuring activity, not progress. Analytics team to confirm.

**Why this works:**
- Primary metric is directly tied to the problem in Section 2 (activation failure)
- Assumptions are tagged inline with 🔶 so reviewers see them in context
- Open questions are tagged with 🔵 and include who needs to resolve them
- Guardrail metric prevents the initiative from creating new problems

---

### Self-Assessment (end of PRD)

**Strongest Section**

Section 2 — Problem Statement. Grounded in 10 discovery interviews and corroborated by support ticket data and Mixpanel analytics. The problem is real and well-evidenced.

**Weakest Section**

Section 4 — Strategic Context. The TAM/SAM/SOM numbers are rough estimates from a two-year-old analyst report. The "why now" rationale is compelling internally but hasn't been validated with customers.

**Top Assumptions to Validate**

| # | Assumption | Section | Risk if Wrong | Proposed Validation |
|---|------------|---------|---------------|---------------------|
| 1 | 60% target activation rate is achievable | Section 6 | Engineering builds to wrong success bar; initiative declared a failure at 55% | Survey 3 comparable SaaS companies for post-onboarding-redesign benchmarks |
| 2 | Solopreneurs are the primary churning segment | Section 3 | Onboarding designed for wrong persona | Segment churn data by company size in Mixpanel; confirm with 5 exit interviews |
| 3 | Checklist format is the right intervention | Section 5 | Build wrong solution; interactive tour or video might work better | Run `pol-probe` experiment: 50-user prototype test comparing checklist vs. tooltip tour |

**Recommended Next Step**

Run 3 discovery interviews with recently churned solopreneurs to validate the onboarding friction assumption before presenting to the leadership team. Without this, Section 2's evidence rests heavily on a small interview sample (n=10).

---

## Example 2: Bad PRD (Feature List)

A PRD that skips evidence, personas, metrics, and acceptance criteria — the kind that produces misalignment and wasted effort.

**Problem Statement:**
> "Users want better onboarding."

**Solution:**
> "Add onboarding."

**Requirements:**
> "1. Onboarding flow
> 2. Tooltips
> 3. Help docs"

**Why this fails:**
- No evidence (who wants this? how do we know?)
- No personas (who is "users"?)
- No success metrics (how do we measure "better"?)
- No acceptance criteria (what does "onboarding flow" mean?)
- No strategic context (why now? why this over other priorities?)
- No assumptions tagged — every claim is presented as fact with no evidence
- No self-assessment — no honest accounting of what's known vs. guessed

**Fix with the PRD template:**
- **Section 2**: Write a problem statement with evidence from discovery interviews — tag any unvalidated claims as 🔶 Assumption
- **Section 3**: Define a persona (not "users" — a specific person with goals, pain points, and current behaviour)
- **Section 6**: Define success metrics with baselines and targets (activation rate 40% → 60%)
- **Section 7**: Break down "onboarding flow" into user stories with testable acceptance criteria
- **Self-Assessment**: Surface the weakest section and top assumptions before sharing with stakeholders
