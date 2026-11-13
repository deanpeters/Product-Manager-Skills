# EOL Stakeholder Sequence Example — SaaS

**Product:** Fieldlight Classic Dispatch
**Level:** 2 — Standard · **Stops:** 8
**Context:** ~800 accounts, $2.4M ARR, annual contracts, sold direct, no regulatory constraint.
Replaced by Fieldlight Next. ~30 accounts use custom dispatch rules that don't carry over. Only the
product leadership team knows so far.

---

```markdown
## EOL Stakeholder Sequence: Fieldlight Classic Dispatch

**Level**: 2 -- Standard
**Stops in scope**: 8
**Stops deliberately skipped**: Channel (sold direct, no resellers);
Regulatory (no compliance surface on dispatch data)

### Sequencing Principle

Talk to the people who can kill the plan before you talk to the people
who have to execute the plan. Each conversation informs the next.

---

### Stop 1: Legal

**When**: Before anyone outside product leadership

**Why this stop matters for EOL**:
- Contract terms can end the discussion

**What you need FROM them**:
- Any multi-year Classic commitments?
- Do renewals auto-extend past December?
- Is uptime SLA product-specific or platform-wide?

**What you owe TO them**:
- Draft timeline and rationale
- Two weeks to review contracts

**Red flags to watch for**:
- Enterprise contracts naming Classic specifically
- Auto-renewal past the EOL date

**Output of this conversation**:
- Written go or no-go on the December date

### Stop 2: Finance

**When**: After Legal clears the date

**Why this stop matters for EOL**:
- Sizes every downstream decision

**What you need FROM them**:
- Actual Classic-attributed ARR
- Churn assumption we should plan against
- Budget available for migration support

**What you owe TO them**:
- Migration cost estimate
- Retention scenarios, best and worst

**Red flags to watch for**:
- Classic revenue booked in a bundle
- Board forecast already assumes this ARR

**Output of this conversation**:
- Agreed retention target and support budget

### Stop 3: Sales

**When**: After Finance, before any wider comms

**Why this stop matters for EOL**:
- Field promises never reach contracts

**What you need FROM them**:
- What has anyone promised about Classic's future?
- Which open deals include Classic?
- Any verbal roadmap commitments outstanding?

**What you owe TO them**:
- Firm EOS date to quote against
- Next positioning and pricing
- Named support for at-risk renewals

**Red flags to watch for**:
- "I told them we'd support it indefinitely"
- Classic bundled into a signed multi-year deal

**Output of this conversation**:
- List of field commitments to honor or unwind

### Stop 4: Marketing

**When**: Same week as Sales

**Why this stop matters for EOL**:
- Campaigns run ahead of decisions

**What you need FROM them**:
- Any Classic demand gen committed this quarter?
- What content references Classic?

**What you owe TO them**:
- Approved announcement language
- Lead time for site and docs updates

**Red flags to watch for**:
- Paid campaign already booked
- Classic featured in an upcoming webinar

**Output of this conversation**:
- Campaign stop list and comms calendar

### Stop 5: Customer Success

**When**: After Sales, before customer outreach

**Why this stop matters for EOL**:
- They absorb the customer reaction

**What you need FROM them**:
- Which accounts will take this worst?
- Who is already unhappy for other reasons?
- Realistic migration effort per account?

**What you owe TO them**:
- Full timeline before customers hear it
- Save-play budget and authority
- Migration support staffing

**Red flags to watch for**:
- Accounts already at renewal risk
- CS learning about this from a customer

**Output of this conversation**:
- Tiered account list with owners

### Stop 6: Three most difficult customers

**When**: Under NDA, before public announcement

**Why this stop matters for EOL**:
- They find what everyone missed

**What you need FROM them**:
- What would break in your workflow?
- What have you built on the v1 API?
- What would make this survivable?

**What you owe TO them**:
- Early notice and a real hearing
- First access to migration support
- Honest answer on the custom-rule gap

**Red flags to watch for**:
- Integrations nobody knew existed
- "We renewed last month because of Classic"

**Output of this conversation**:
- Revised impact list and accommodation offers

### Stop 7: Engineering

**When**: In parallel with Stops 3-5

**Why this stop matters for EOL**:
- They know the hidden dependencies

**What you need FROM them**:
- What internally reads the v1 dispatch API?
- Can rule migration be automated?
- What breaks if Classic goes read-only?

**What you owe TO them**:
- Firm phase dates to build against
- Decision on migration tooling scope

**Red flags to watch for**:
- Internal systems querying Classic directly
- Migration tooling larger than expected

**Output of this conversation**:
- Dependency inventory and tooling plan

### Stop 8: Support

**When**: Last internal stop, before announcement

**Why this stop matters for EOL**:
- They take the first wave

**What you need FROM them**:
- Expected ticket volume and staffing needs
- Which questions will dominate?

**What you owe TO them**:
- Complete FAQ before customers hear
- Escalation path with named owners
- Advance notice, not same-day

**Red flags to watch for**:
- No capacity for a volume spike
- FAQ still unwritten at announcement week

**Output of this conversation**:
- Staffed support plan and escalation ladder

---

### Parallel vs. Sequential Guidance

**Must be sequential**:
- Legal before Finance: contract terms change the revenue math
- Finance before Sales: Sales needs the retention target
- Sales before CS: field commitments shape account tiering
- CS before difficult customers: tiering picks who to call

**Can run in parallel**:
- Engineering and Stops 3-5: no dependency, different questions
- Marketing and Sales: same week, different asks

### Assumptions to Validate
- Assumes only product leadership currently knows
- Assumes no enterprise contract names Classic specifically
- Assumes CS relationships with the top accounts are intact
```

---

## What to notice

- **Legal is Stop 1 and gates everything.** Its output is a written go/no-go on the date. If that
  comes back no, seven conversations never need to happen.
- **Sales is asked, not told.** "What has anyone promised about Classic's future?" comes before the
  date is handed over. Field commitments that never reached a contract are the single most common
  post-announcement ambush.
- **The difficult-customer stop has real currency to offer.** Early notice, first access to
  migration support, and an honest answer on the custom-rule gap — that's what buys candor instead
  of a complaint.
- **Support is last internally and still before customers.** The cardinal sin is handing Support an
  announcement five minutes before customers get it. Last in sequence, not last to know.
- **Two stops are skipped with reasons.** Channel and Regulatory are named as excluded and why, so
  a reviewer can challenge the reasoning rather than guess at an omission.
