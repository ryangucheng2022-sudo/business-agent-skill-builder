# business-agent-skill-builder

English | [简体中文](README.zh-CN.md)

**Turn a real business workflow into a reusable agent skill — reliably.** A field-tested method (plus templates and checklists) for converting SOPs, spreadsheets and approval routines into skills an AI agent can execute with business-grade discipline: explicit inputs and outputs, traceable calculations, defined authority boundaries, human confirmation points, and validation against real cases.

Most "agent skills" fail in business settings not because the model is weak, but because nobody wrote down the boundary: what the agent may touch, which source wins when files conflict, which numbers need traceability, and where a human must confirm. This package is that missing design layer.

## What's inside

- `SKILL.md` — the method itself, as an agent skill: a 7-step flow from scoping one narrow workflow to iterating after real use.
- `references/business-skill-design.md` — fit test, the minimum business brief, and the input/output contract.
- `references/agent-boundary.md` — authority levels (read-only / draft-only / confirmed-write / autonomous-write), escalation points, source priority, and output risk labels.
- `references/business-skill-template.md` — a fill-in SKILL.md template for business workflows.
- `references/validation-checklist.md` — trigger, workflow, business-logic, resource and case-testing checks, plus done criteria.
- `examples/resale-cost-accounting/` — a complete miniature skill built with the method (field dictionary, calculation rules, exception cases), so you can see the target state instead of imagining it.

## Who is it for

| Role | Typical scenarios | What you get |
|---|---|---|
| **Business owners & operators** | "Our monthly costing / approval review / quotation analysis should just run itself" | A repeatable way to hand a workflow to an agent without handing over judgment: scope stays narrow, exceptions surface instead of hiding |
| **Functional experts (finance, supply chain, sales ops, HR)** | Encoding your formulas, checklists and review rules so others (and agents) execute them consistently | Your tacit rules become versioned references — field dictionaries, calculation rules, exception cases — instead of folklore in one person's head |
| **AI / digital transformation leads** | Rolling agents out across departments without incidents | The boundary framework (authority levels, confirmation points, source priority, risk labels) is the governance layer that makes deployment defensible |
| **Agent builders & consultants** | Delivering business skills for clients or internal platforms | Templates and a validation checklist that separate a demo from something a business can trust: case testing with known answers is built into the method |

## The method in one paragraph

Start with **one closed-loop task**, not a department assistant. Capture real invocation examples and artifacts. Define the **agent boundary** before writing anything: read vs. write, which systems, what needs human confirmation. Structure the skill minimally — rules in `references/`, deterministic work in `scripts/`, templates in `assets/`. Write instructions that tell the agent how to *perform* the work, with source checks, escalation and validation built in. **Validate against historical or representative cases** (normal, missing-field, conflicting-source, edge, and a real case with a known answer). Then iterate from real use, in small updates.

## Usage

Copy this folder into your agent platform's skills directory and ask the agent to build a skill with it, e.g.:

> "Using business-agent-skill-builder, turn our monthly quotation review into a skill. Here are last month's inputs and the approved output."

The worked example in `examples/` shows what a finished business skill looks like.

## License

MIT — see [LICENSE](LICENSE).
