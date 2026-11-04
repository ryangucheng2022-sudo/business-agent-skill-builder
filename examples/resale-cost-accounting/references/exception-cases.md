# Exception Cases (example)

| Case | Handling |
|---|---|
| Missing purchase cost | Row goes to the exception list as `Needs confirmation`; exclude from margin summary, keep in the table with cost blank |
| Negative margin | Flag with reason candidates (price below cost, stale cost, wrong part mapping); do not report as final without confirmation |
| Duplicate order lines | List both rows; ask which is authoritative before calculating totals |
| Conflicting exchange rates | Use the higher-priority source (rate table over note), report the conflict and the rate used |
| Expired purchase cost | Use it only with an `Assumed` label and a confirmation request |
| Part not in master data | Exception list; never invent a cost from a similar part |
