# Agent Boundary

Use this reference to define what a business agent may do.

## Authority Levels

Choose one authority level per workflow.

Read-only:
- Inspect files, emails, pages, or system records.
- Summarize and analyze.
- Do not modify source systems.

Draft-only:
- Prepare approval opinions, emails, reports, tables, or updates.
- Ask the user before sending, submitting, approving, or changing records.

Confirmed-write:
- Make changes only after the user confirms the exact action.
- Restate the target system, record, change, and consequence before action.

Autonomous-write:
- Use only for low-risk internal maintenance with clear rollback.
- Avoid for finance, legal, customer commitments, approvals, and production data.

## Escalation Points

Require human confirmation when:
- A financial amount, margin, cost, tax, or exchange rate is uncertain.
- A policy or approval rule conflicts with another source.
- The agent would approve, reject, submit, send, or delete something.
- A missing field materially changes the result.
- The action affects customers, suppliers, employees, contracts, or accounting records.

## Source Priority

Define source priority when data conflicts.

Example:
1. Signed contract or approved system record.
2. Finance-controlled master data.
3. Latest official export.
4. Email or chat attachment.
5. User-provided note.

The agent should state when it uses a lower-priority source.

## Output Risk Labels

Use simple labels:
- Confirmed: directly supported by source data.
- Calculated: derived from stated rules.
- Assumed: based on an explicit assumption.
- Needs confirmation: cannot be completed safely without user input.

## Guardrails for Business Agents

Always preserve traceability for important numbers and decisions.

Do not hide missing data behind polished prose.

Do not treat a similar historical case as a policy unless the user says it is authoritative.

Prefer a draft recommendation when the workflow has legal, financial, HR, approval, or customer impact.

Keep computation deterministic. All calculation belongs in scripts; the agent only triggers the workflow, supplies parameters, obtains human confirmations, and reports exceptions. If swapping the agent or model would change the numbers, the boundary is wrong — move that logic into a script.

Write human confirmations back as data, and match them to records by identity (key fields such as item or document codes), never by row number or position alone. Rows can be re-sorted, added, or removed between collection and write-back; an identity check is what prevents a confirmed value from landing on the wrong record.
