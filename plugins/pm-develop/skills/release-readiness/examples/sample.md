# Release Readiness Example: SaaS

**Release:** change to how overage is billed (Fieldlight). Reaches all paying accounts.
**Why this example exists:** a billing change is invisible to users until it's wrong, so it earns
Level 3 even though it's a small code change.

---

```markdown
## The release
**What changes:** overage computed per technician-day instead of per month.
**What does not change:** base plan prices, invoice layout.
**Reaches:** all ~1,400 paying accounts. **Reversibility:** a feature flag undoes the calculation,
but invoices already issued would need credit notes.
**Level:** 3 Heavy. Reach is total and a wrong invoice is hard to undo.

## The seven checks
| Check | State | Evidence |
|---|---|---|
| Tested | Unit tests, replay of last 3 months' usage on a copy | Replay diff report. **Not tested:** accounts with mid-month plan changes |
| Rollout | 1% (internal + 20 friendly accounts) → 10% → 100%, 48 hours each | Move-on: zero invoice variance above 0.5% |
| Monitoring | Invoice variance, support tickets tagged billing | Watcher: finance ops, daily for 7 days |
| Rollback | Flag off; credit-note script ready | **Not rehearsed.** Hold until rehearsed |
| Support | Billing FAQ + escalation to finance ops | Support lead briefed |
| Dependencies | Finance month-end close Day 28-3 | Ship on Day 8, off the close window |

## Go / hold criteria
| # | Criterion | Threshold | Type |
|---|---|---|---|
| 1 | Replay variance | < 0.5% on every tested account | Must-pass |
| 2 | Rollback rehearsed | Credit-note script run on a copy | Must-pass |
| 3 | Mid-month plan-change accounts | Manually checked for 10 | Watch |

## Decision
**Hold** until criterion 2 is met (one day). Then go to the 1% stage. Decided by: VP Product.
```

## What to learn from this

- **A small change got the heavy check** because the cost of a wrong invoice is trust.
- **The unrehearsed rollback caused the hold,** a one-day delay instead of a billing incident.
- **The release avoided the finance close window,** which no test would have shown.
