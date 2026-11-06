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

## Data and Code Validation

For data-intensive skills, also check (see `references/data-pipeline-standards.md`):

- Source inputs are snapshotted and never modified in place; results do not depend on `.bak` copies.
- An input manifest declares expected files, source systems, periods, and key fields, and is validated at entry.
- A missing or malformed input stops the run instead of silently producing blank columns or partial results.
- Compute scripts read only a normalized staging layer, never source-system files directly.
- File lookup and data reading live in one shared module; renaming a source touches one place.
- Extract, transform, and presentation steps can be tested and re-run separately; scripts are import-safe (no logic, argument parsing, or global state at import time).
- Rates, mappings, thresholds, and paths are configuration, not code constants; dependencies are pinned.
- A baseline case exists as a re-runnable fixture with an expected result, not as numbers in a document.
- The workflow runs end to end from a single entry point, and run state is stored in a structured state file so an interrupted run can resume.
- Human confirmations are written back as data and matched to records by identity (key fields), never by row position alone.

## Done Criteria

The skill is ready when a fresh agent session can use it to:
- Understand the business workflow.
- Ask only necessary clarifying questions.
- Produce the expected artifact.
- Explain assumptions and source limitations.
- Surface risks before business action.
