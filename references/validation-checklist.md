# Validation Checklist

Use this checklist before considering a business skill ready.

## Trigger Validation

- The skill name is short and action-oriented.
- The frontmatter description includes concrete trigger scenarios.
- Common Chinese and English user phrases are covered when relevant.
- The skill does not trigger for unrelated broad requests.

## Workflow Validation

- The workflow has a clear start and finish.
- Required inputs are listed.
- Missing input behavior is defined.
- Source priority is defined.
- Manual confirmation points are explicit.

## Business Logic Validation

- Formulas and policies live in references or scripts.
- Important numbers can be traced to source fields.
- Units, currencies, dates, and rounding are defined.
- Exception cases are not silently ignored.
- The output distinguishes confirmed facts from assumptions.

## Resource Validation

- `SKILL.md` stays concise and navigational.
- Detailed rules are in `references/`.
- Repeated deterministic work is moved to `scripts/` when useful.
- Templates and reusable output files are in `assets/`.
- Placeholder files are removed.

## Case Testing

Test at least:
- One normal case.
- One missing-field case.
- One conflicting-source case.
- One edge case with abnormal result.
- One real historical case with a known answer, if available.

For each case, compare:
- Final numbers.
- Exception detection.
- Explanation quality.
- Output format.
- Whether the agent asked for confirmation at the right time.

## Done Criteria

The skill is ready when a fresh agent session can use it to:
- Understand the business workflow.
- Ask only necessary clarifying questions.
- Produce the expected artifact.
- Explain assumptions and source limitations.
- Surface risks before business action.
