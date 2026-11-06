# Changelog

## 1.1.0 (2026-11-06)

Adds the data and code architecture layer distilled from auditing a
real data-intensive business skill whose business rules were strong
but whose engineering structure was not.

- New reference: `references/data-pipeline-standards.md` — immutable
  raw inputs, input manifest contracts, data layering (raw, staging,
  compute, output), a single data-access layer, extract/transform/
  present separation with import-safe scripts, configuration outside
  code, and reproducible baselines.
- `references/validation-checklist.md`: new Data and Code Validation
  section turning those standards into pass/fail checks, including
  single-entry orchestration with explicit run state and
  identity-checked human confirmations.
- `references/agent-boundary.md`: deterministic-computation guardrail
  (scripts compute; the agent triggers, supplies parameters, confirms,
  and reports) and identity-matched confirmation write-back.
- `references/business-skill-design.md`: the input contract now calls
  for a manifest for data-intensive workflows.
- `references/business-skill-template.md`: Required Inputs gains an
  input-manifest entry.
- `SKILL.md`: Step 4 points data-intensive work to the new reference;
  Step 6 makes its checks a release gate.

## v1.0.0 (2026-11-04)

Initial open-source release.

- The 7-step skill-building method as an agent skill (`SKILL.md`).
- References: business skill design (fit test, brief, I/O contract),
  agent boundary (authority levels, escalation, source priority, risk
  labels), a fill-in business skill template, and a validation checklist.
- Worked example: `examples/resale-cost-accounting/`, a complete miniature
  business skill (skill file + field dictionary + calculation rules +
  exception cases) built with the method.
- Wording generalized to be agent-platform neutral.
