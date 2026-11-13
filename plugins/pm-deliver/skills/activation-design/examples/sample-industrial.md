# Activation Design Example: Industrial

**Product:** NFA-500 controller with a connected-service tier (Northfield Automation)
**Customer:** plant maintenance teams; installs by partner crews
**Why this example exists:** in hardware, activation spans delivery, install, commissioning, and
connection, owned by four parties. The weeks of delay were handoffs, not the product.

---

```markdown
## The moment
**Customer's goal:** keep the line running and hear about faults before production does.
**Activation (hypothesis):** unit commissioned, connected to the service, and reporting for 14 days
with no service call.
**Evidence:** `[NEEDS SOURCE]`. NFA-200 data has no connected tier. Treat as hypothesis until the first cohort.

## The path today (first 14 units)
| Step | Owner | Median | Stopped here |
|---|---|---|---|
| Delivery to site | Logistics | 6 days | 0 |
| Install and wiring | Partner crew | 9 days | 2 waiting on a shutdown window |
| Commissioning | Partner crew / Service | 11 days | 3 waiting on a service visit |
| Connection to service | Customer IT | 17 days | 5 waiting on firewall approval |
**Time to value:** median 43 days; the slowest units 70+.

## Blockers
| Blocker | Evidence | Fix |
|---|---|---|
| Firewall approval | 5 of 14 units | Send IT a one-page network note with the order (pre-fill) |
| Waiting for a service visit | 3 of 14 | Partner crews certified to commission (remove) |
| Shutdown window | 2 of 14 | Book the window at quote time |

## Designed path
| Checkpoint | Action | Owner | Stall handling |
|---|---|---|---|
| 1 | Network note to customer IT at order | Sales | Day 7: partner calls IT |
| 2 | Install in a booked window | Partner | Day 14 after delivery: partner manager calls |
| 3 | Commission and connect | Certified partner | Day 21: service engineer visit |
| 4 | 14-day reporting check | Service | Day 35: call the plant |
**Handoff:** quote captures the plant IT contact, shutdown calendar, and who will operate the unit.

## Metric
**Connected and reporting within 45 days of delivery:** 4 of 14 baseline · target `[NEEDS SOURCE]`.
**Median time to activate:** 43 days · **Guardrail:** service visits per new unit.
```

## What to learn from this

- **The longest wait was firewall approval,** an IT dependency no product feature touches.
- **The fix was captured at the quote,** which is a sales handoff, not an onboarding step.
- **Stall handling has days attached,** so a quiet customer triggers an action.
