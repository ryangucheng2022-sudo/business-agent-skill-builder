# Business Agent Skill Builder

## Overview

Use this skill to convert a real business workflow into a reusable agent skill and, when needed, an agent operating pattern. Focus on business reliability: clear inputs, explicit outputs, traceable calculations, escalation points, and validation against real cases.

This skill is a business-design layer. When actually creating or modifying a skill folder, also follow your platform's skill-creator workflow if available.

## Working Flow

1. Identify the narrow business workflow.
2. Collect concrete user requests and real artifacts.
3. Define the agent boundary and authority.
4. Design the skill structure and reusable resources.
5. Write the skill instructions and references.
6. Validate with historical or representative cases.
7. Iterate after real use.

## Step 1: Scope the Workflow

Start with one closed-loop task, not a broad department assistant.

Good first skills:
- Calculate resale cost from exported Excel files.
- Review an OA approval and draft an approval opinion.
- Convert quotation inputs into a pricing analysis.
- Generate a monthly KPI review from a standard report.
- Check a contract against a company review checklist.

Avoid a broad scope such as "finance assistant" until several narrow skills work reliably.

Read `references/business-skill-design.md` when the workflow scope, required artifacts, or target output is still unclear.

## Step 2: Capture Examples

Ask for or infer examples of how users will invoke the skill.

Capture:
- Trigger phrases the user might say.
- Input files or systems involved.
- Expected output format.
- Known formulas, policies, or judgment rules.
- Frequent exceptions and ambiguous cases.
- The person or role who consumes the result.

For each example, identify whether the work needs procedural instructions, reference material, reusable scripts, or templates.

## Step 3: Define Agent Boundary

Before writing the skill, define what the agent may do.

Specify:
- Read-only versus write-capable actions.
- Systems or files the agent may access.
- Whether the agent may submit, send, approve, update, or only draft.
- Which conditions require human confirmation.
- How to handle missing data, conflicting source files, or policy uncertainty.

Read `references/agent-boundary.md` when the workflow touches approvals, finance numbers, customer commitments, legal language, or operational systems.

## Step 4: Design Skill Contents

Use the minimum structure that makes the workflow repeatable.

Recommended layout:

```text
business-workflow-name/
├── SKILL.md
├── references/
│   ├── process.md
│   ├── field-dictionary.md
│   ├── calculation-rules.md
│   └── exception-cases.md
├── scripts/
│   └── validate-or-calculate.py
├── assets/
│   └── output-template.xlsx
└── agents/
    └── openai.yaml
```

Use `references/` for business rules, field dictionaries, SOPs, policy notes, and examples. Use `scripts/` only when deterministic calculation, parsing, reconciliation, or validation is repeated. Use `assets/` for output templates, blank forms, branded documents, and reusable workbook structures.

Read `references/business-skill-template.md` before drafting a new business skill.

## Step 5: Write Business-Grade Instructions

The resulting skill should tell the agent how to perform the work, not explain the business in a textbook style.

Include:
- A clear frontmatter description with specific trigger scenarios.
- A short overview.
- A decision flow.
- Required source checks.
- Calculation or judgment rules.
- Output requirements.
- Escalation and uncertainty handling.
- Validation steps.

Keep detailed business rules in reference files. Keep `SKILL.md` focused on navigation and the core workflow.

## Step 6: Validate the Skill

Validate against real or representative cases before trusting the skill.

Check:
- The skill triggers for the right user requests.
- Required inputs are requested when missing.
- Calculations match known outputs.
- Exceptions are surfaced instead of hidden.
- The result cites source files, fields, or assumptions.
- The output is usable by the target business audience.

Read `references/validation-checklist.md` before calling the skill done.

## Step 7: Iterate From Use

After every real use, update the skill when one of these appears:
- A new recurring input format.
- A new formula or policy rule.
- A repeated exception.
- A confusing user phrase that should trigger the skill.
- A validation gap.
- A better output template.

Prefer small updates that improve the next run. Do not expand the skill into unrelated workflows.
