# Stakeholder Mapping Example — Industrial

**Initiative:** Northfield Automation's remote firmware update for the NFA-500.

Continues from the `stakeholder-identification` industrial example, which surfaced plant OT security
as a Permission-holder at every site.

---

## Grid 1: Power × Interest

| | **High Interest** | **Low Interest** |
|---|---|---|
| **High Power** | **Manage closely**<br>· Northfield VP Engineering<br>· Plant operations managers | **Keep satisfied**<br>· Regulatory (UL/CE)<br>· Northfield CFO |
| **Low Power** | **Keep informed**<br>· Northfield field service<br>· Channel partners | **Monitor**<br>· Plant OT security<br>· Plant maintenance staff<br>· Plant safety officers |

Read alone: co-design with ops managers and engineering, brief Regulatory, inform field service and
partners, ignore the rest.

---

## Grid 2: Impact × Power

| | **High Power** | **Low Power** |
|---|---|---|
| **High Impact** | **Q2**<br>· Plant operations managers<br>· **Plant OT security**<br>· Channel partners | **Q1 — elevate deliberately**<br>· **Plant maintenance staff**<br>· Plant safety officers |
| **Low Impact** | **Q4**<br>· Northfield CFO<br>· Regulatory (UL/CE) | **Q3**<br>· Notification/telemetry vendor |

---

## The comparison

| Stakeholder | Power×Interest | Impact×Power | Tension |
|---|---|---|---|
| **Plant OT security** | Monitor | **Q2** | Holds Permission at every site and is deeply affected. Low expressed interest only because they haven't been told a network ingress is coming |
| **Plant maintenance staff** | Monitor | **Q1** | A controller on their line changes state remotely; they stand at the panel when it goes wrong, with no say in enrollment |
| Plant safety officers | Monitor | **Q1** | Own the incident review if an update contributes to an unplanned stop |
| Regulatory | Keep satisfied | Q4 | High power, low impact — a gate, and correctly treated as one |
| Channel partners | Keep informed | **Q2** | Higher stakes than grid 1 suggests: the feature removes billable site visits |

**Q1 and misplaced-Q2 voices to elevate:**
- **Plant OT security** — the most consequential correction. Four conversations across pilot sites
  *before* the design is fixed, on what network path, authentication, and audit evidence they would
  require. They can refuse silently, site by site, and you'd never see a single "no."
- **Plant maintenance staff** — what they need to trust a remote change: notification, veto,
  rollback visibility.
- **Plant safety officers** — what evidence they'd need in an incident review.

**The mismatch that matters most:** plant OT security. Grid 1 puts them in *Monitor* — low power,
low interest. Grid 2 puts them in **Q2**, high impact and high power, because they hold Permission
at every site. Acting on grid 1 alone would have shipped a feature that quietly fails to be
adoptable, one refused network request at a time, with no visible rejection anywhere.

---

## Engagement plan

| Stakeholder | Quadrant | Engagement | Cadence | Owner |
|---|---|---|---|---|
| Plant OT security | Q2 | Design consultation on network path and audit evidence | 4 sessions pre-spec | PM + Eng lead |
| Plant maintenance staff | Q1 | Interviews, then review of the notification/veto design | Twice pre-launch | PM |
| Plant safety officers | Q1 | Review of the incident-evidence trail | Once pre-launch | PM |
| Plant operations managers | Q2 | Co-design, pilot cohort | Biweekly | PM |
| Channel partners | Q2 | Commercial conversation on service-revenue impact | Monthly | Channel lead |
| Regulatory | Q4 | Listing impact assessment | At spec, at launch | Regulatory |

---

## Quadrant migration

| Stakeholder | From | To | Why | How |
|---|---|---|---|---|
| Plant OT security | Monitor (P×I) | Manage closely | They are a silent veto at every site; involving them early converts a blocker into a specification | Bring them into design before the network path is fixed, and give them the audit evidence they ask for |
| Channel partners | Keep informed | Manage closely | The feature removes billable visits; unaddressed, they slow adoption at accounts they service | Commercial conversation about what replaces that revenue, before launch, not after |

---

## What to notice

- **The most dangerous stakeholder was in *Monitor*.** OT security has no interest in your product
  and absolute authority over whether it can reach a plant. A single grid puts them last; the
  comparison puts them first.
- **A silent veto is worse than a loud one.** OT security doesn't escalate — they decline a firewall
  change. Adoption just never materializes, and nobody can point at a rejection. That's what makes
  the mismatch expensive rather than merely wrong.
- **Channel partners moved quadrants for commercial reasons, not process ones.** The feature removes
  revenue they currently earn. The engagement is a commercial conversation, not a briefing.
- **Q1 here is about consequence, not convenience.** Maintenance staff and safety officers absorb
  the risk of a remote change to equipment they're responsible for. Neither has a vote in enrollment.
- **The same pattern as the SaaS example, different stakes.** Both initiatives put the most affected,
  least powerful group in *Monitor* on the first grid. Running the second grid is what corrected it
  in both cases — which suggests the mismatch is structural, not a one-off oversight.
