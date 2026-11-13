# Message House Example: Industrial

**Offering:** NFA-500 retrofit controller (Northfield Automation)
**Target:** maintenance and plant engineers at mid-size discrete-manufacturing plants running aging
controllers; buyers are procurement and the plant manager
**Context:** successor to the NFA-200; sold through 8 partners; connected-service tier is new

**Why this example exists:** industrial buyers are technical and skeptical, so the *proof
hierarchy* and role variants do most of the work. It also shows the foundation as hard facts.

---

```markdown
## Draft critique (first)
Pillars as submitted: "Modular I/O," "Cloud connectivity," "Compact DIN-rail form factor."
All three are on the data sheet. None names an outcome.

## Message House: NFA-500

**ROOF**
> Upgrade the line without stopping it.

| Pillar | Outcome | Traces to | Cover test |
|---|---|---|---|
| 1 | Swap the old controller in a shift, not a shutdown | Pain: "we can't give up a weekend of production" (win/loss, 6 of 8 lost deals) [FROM YOU] | Passes |
| 2 | Hear about a fault before production does | Gain: maintenance planners want warning, not alarms [FROM YOU] | Passes |
| 3 | Keep the programs and wiring you already trust | Pain: fear of re-validating a proven process [FROM YOU] | Passes |

**Proof**
| Pillar | Proof | Type | Source |
|---|---|---|---|
| 1 | Install time at three pilot sites with bracket kit | Measured pilot | `[NEEDS SOURCE]`: site reports not collected |
| 2 | Warning lead time on bearing and thermal faults | Internal test | `[NEEDS SOURCE]`: method not written down |
| 3 | Program import verified against NFA-200 libraries | Internal test | Test report T-114 [FROM YOU] |

**Foundation:** UL 508A listed; CE conformity per declaration [no.] `[NEEDS SOURCE]`; ~120 NFA-200
sites in service; spare parts in 6 countries; service contracts through 2028 for the NFA-200 base.

**Superlatives found:** "the most reliable retrofit controller." No comparative data. Removed.

## Variants
| Role | Lead pillar | Wording |
|---|---|---|
| Maintenance engineer | 3 | "Your programs come with you." |
| Plant manager | 1 | "A shift, not a shutdown." |
| Procurement | 3 and foundation | "No re-validation. Parts and service in six countries." |
| Distributor | 1, plus margin | "A retrofit your customers have been asking for, with a bracket kit that keeps install time predictable." |

## Words
Use: "shift not shutdown," "your programs" (plant interviews). Avoid: "next-gen," "Industry 4.0," "seamless."

## Test plan
Six plant engineers from lost-deal interviews. Ask what they heard, believe, doubt. If fewer
than 4 repeat "without stopping," re-cut the roof.
```

## What to learn from this

- **Pillar 3 is a pain, not a feature.** "Keep what you trust" came from lost-deal interviews,
  not the data sheet.
- **Only one proof point is real so far.** The house says so, which tells the team what to gather
  before the trade fair.
- **Procurement gets the same pillars,** reordered, with the foundation doing the persuading.
