# Usage Data Investigation Example: Industrial

**Question:** what is the early-life fault pattern on NFA-500 units, and does it differ by configuration?
**Unit:** commissioned unit · **Window:** first 90 days in the field · **Decision:** whether to issue a field bulletin

**Why this example exists:** the "usage" data is service and warranty records, small counts, and
the pattern depended on a field the system recorded inconsistently.

---

```markdown
## Data check
- Source: service system (fault tickets) joined to ERP (units commissioned).
- Tracking: fault cause is free text in 40% of tickets; unusable for those.
- Definition: "fault" includes two ticket types that changed on Aug 1 (flagged).
- Missing: units at partner sites reported by partners monthly (lag up to 5 weeks).
- Sample: 64 commissioned units, 11 fault tickets. Small: read counts, not rates.

## Findings
1. **Fact:** 11 fault tickets on 64 units in first 90 days (17%; 11 of 64).
2. **Fact:** 7 of the 11 involve the bracket-mounted configuration; 4 involve the standard mount. The bracket-mounted configuration is 28 of 64 units.
3. **Inference:** bracket-mounted units fault at a higher rate (7 of 28 vs 4 of 36). With these counts, the gap could be noise.
4. **Fact:** 5 of the 7 bracket-mounted faults sit with one partner crew.
5. **Assumption:** the torque spec is the cause. (Free-text causes can't confirm it.)

## What people must answer
| Question | Who | Ask |
|---|---|---|
| Is it the bracket, or the crew? | Service lead; that partner's installers | "Show me how you torque the fasteners. What does the guide say?" |
| What is the real cause on the 40% unlabeled tickets? | Service technicians | Review the 4 open tickets by hand |

**Do not issue a bulletin yet.** Do re-check at 120 days with the cause field made mandatory.
```

## What to learn from this

- **Finding 3 is an Inference with a warning.** Seven of 28 versus four of 36 is not a result.
- **Finding 4 changed the question** from "the bracket" to "the crew," which no chart would have said.
- **The recommendation is to wait and fix the data,** which is a legitimate outcome.
