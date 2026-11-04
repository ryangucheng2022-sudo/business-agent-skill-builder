# Business Skill Design

Use this reference when turning a business process into a reusable skill.

## Fit Test

A workflow is a good skill candidate when:
- It happens repeatedly.
- It has recognizable inputs and outputs.
- It follows a stable SOP, policy, formula, checklist, or template.
- Mistakes are expensive enough that validation matters.
- The user would benefit from the agent remembering the process next time.

A workflow is not ready when:
- The goal changes every time.
- The rules are mostly undocumented and cannot be inferred from examples.
- The required data is unavailable.
- The agent would need unrestricted authority in a live system.

## Minimum Business Brief

Collect these details:
- Workflow name.
- Business owner or target audience.
- User request examples.
- Source artifacts and systems.
- Required output.
- Core rules and formulas.
- Known exception cases.
- Validation source or historical examples.
- Human confirmation points.

## Input and Output Contract

Define the contract before implementing.

Inputs:
- File types, systems, tables, or forms.
- Required fields.
- Optional fields.
- Source priority when multiple files conflict.
- Date, currency, unit, and version assumptions.

Outputs:
- Final artifact type.
- Required sections, sheets, columns, or comments.
- Summary style.
- Traceability requirement.
- Handling of incomplete data.

## Skill Versus Agent

Use a skill for repeatable knowledge and workflow:
- SOPs.
- Formulas.
- Field dictionaries.
- Templates.
- Validation routines.
- Examples.

Use an agent pattern for execution authority and orchestration:
- Which skills to call.
- Which systems to inspect.
- Whether actions are read-only, draft-only, or write-capable.
- What must be confirmed by the user.

## Example: Resale Cost Accounting

Possible skill contents:
- `references/field-dictionary.md`: customer, part number, quantity, selling price, purchase cost, tax, freight, rebate, exchange rate.
- `references/calculation-rules.md`: cost formula, currency conversion, rounding, tax treatment, abnormal margin rules.
- `references/exception-cases.md`: missing cost, negative margin, duplicate order, conflicting exchange rate.
- `scripts/validate-and-calculate.py`: deterministic workbook validation and cost calculation.
- `assets/resale-cost-template.xlsx`: standard output workbook.

Expected output:
- Cleaned calculation table.
- Exception list.
- Margin summary.
- Source and assumption notes.
