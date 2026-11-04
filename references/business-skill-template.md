# Business Skill Template

Use this template when drafting a new business skill. Replace bracketed text and delete sections that do not apply.

```markdown
---
name: [short-hyphen-case-name]
description: [What this business skill does and exactly when to use it. Include business scenarios, source artifact types, and common user requests that should trigger it.]
---

# [Business Skill Name]

## Overview

Use this skill to [perform the workflow] for [target audience or business owner]. Prioritize traceability, validation, and clear handling of missing or conflicting source data.

## Required Inputs

- [Required file, table, system, or user-provided data]
- [Required field or business parameter]
- [Optional but useful supporting source]

If required inputs are missing, ask for them or produce a partial result labeled `Needs confirmation`.

## Workflow

1. Inspect the source artifacts and identify their dates, versions, and owners.
2. Validate required fields and source completeness.
3. Apply the rules in `references/[rules-file].md`.
4. Run any deterministic scripts in `scripts/` when available.
5. Identify exceptions and unresolved assumptions.
6. Produce the required output in the expected format.
7. Summarize source files, assumptions, and items needing confirmation.

## Source Priority

1. [Highest authority source]
2. [Second source]
3. [Fallback source]

When sources conflict, use the highest-priority source and report the conflict.

## Output Requirements

The output must include:
- [Main result]
- [Key table or artifact]
- [Exception list]
- [Source and assumption notes]
- [Recommended next action]

## Escalation

Ask for user confirmation before:
- [Financial, legal, approval, or operational action]
- [Using a fallback assumption]
- [Submitting or sending anything externally]
```

Recommended references:
- `references/process.md`
- `references/field-dictionary.md`
- `references/calculation-rules.md`
- `references/exception-cases.md`
- `references/output-format.md`

Recommended scripts:
- `scripts/validate-inputs.py`
- `scripts/calculate.py`
- `scripts/reconcile-sources.py`

Recommended assets:
- `assets/output-template.xlsx`
- `assets/report-template.docx`
