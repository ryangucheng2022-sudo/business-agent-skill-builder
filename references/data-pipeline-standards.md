# Data Pipeline Standards

Use this reference when a business skill reads source files, exports, or
system data and computes results — accounting, reconciliation, KPI
reporting, inventory, pricing, or any recurring Excel/data workflow.

Business rules can be perfect while the data engineering underneath is
unsafe. These standards come from auditing a real monthly
inventory-accounting skill: its rule base and checks were strong (93
documented rules, two validation suites), yet an architecture review
found that most high-risk failures were symptoms of missing data and
code structure, not wrong business logic. Validate all three layers:
business rules, reliability, and data/code architecture.

## D-01: Raw Data Is Immutable

Source data is read-only. Computation never modifies a source file in
place, and a pile of `.bak_*` copies is not version management.

- Snapshot every input into a raw area before processing (a monthly
  raw snapshot workbook or folder is enough).
- Write all derived data to new files or a working layer.
- If a step must append to a working file, it appends to a copy, never
  to the only copy of the input.

Check: if every backup file were deleted, could the current result be
reproduced from the original inputs alone?

## D-02: Inputs Sign a Contract First

Before processing, declare an input manifest: which files or exports
are expected, from which system, for which period, with which key
fields or structure, and how severe a missing input is.

- Validate the manifest at entry. A missing or malformed input stops
  the run with a clear error.
- Never degrade silently — for example, leaving a whole column blank
  and continuing because a snapshot file was absent.

Check: when any input is missing, does the workflow stop at the door,
or does it produce a polished result with hidden holes?

## D-03: Layer the Data, Never Skip Layers

Keep four layers, in order:

```text
raw/        untouched snapshots of every input
staging/    normalized, schema-checked tables
compute/    scripts that read staging only
output/     final artifacts for the business audience
```

Downstream reads only the layer above it. Compute scripts never open
source-system files directly.

Check: search the compute scripts for source file paths. There should
be none — only staging paths.

## D-04: Reproducible and Traceable

Every output number must trace back to a specific input file and
version. A baseline case must exist in executable form — a fixture
plus an expected result that can be re-run — not as numbers quoted in
a document.

Check: on a clean machine, following only the skill's documentation,
can a fresh session re-run the baseline case and reproduce every
number?

## D-05: One Data-Access Layer

Locating files, building paths, and reading sources live in exactly
one shared module. Business scripts call it; they do not each resolve
directories, guess file names, and open their own data sources.

Check: if a source file is renamed or moved, how many files must
change? The correct answer is one.

## D-06: Separate Extract, Transform, Present

Ingestion, transformation, and presentation are separate steps that
can each be tested and re-run independently. A script that reads a
CSV, applies mapping rules, appends rows into a business workbook,
and formats cells in one pass cannot be safely re-run or unit-tested.

Scripts must also be import-safe: importing a module runs no business
logic, parses no command-line arguments, and computes no global state
from the current date or working directory.

Check: can the transform step run in memory against a fixture and
have its output asserted, without touching a real workbook?

## D-07: Configuration Lives Outside Code

Rates, mappings, thresholds, and paths are configuration, not code
constants. Business parameters change more often than logic; changing
a tax rate must not require editing a script.

- Keep parameters in one config file or one clearly marked section.
- Pin dependency versions.
- Ship a minimal test suite with the skill; it is a release gate,
  not an optional extra.

Check: when a business parameter changes, does anyone have to edit
code? Is there a test command that runs green before release?

## How This Connects

- The input manifest in D-02 is part of the input contract in
  `references/business-skill-design.md`.
- The deterministic boundary behind D-06 — scripts compute, the
  agent only triggers, supplies parameters, confirms, and reports —
  is stated as a guardrail in `references/agent-boundary.md`.
- `references/validation-checklist.md` turns D-01 to D-07 into
  pass/fail checks, together with the orchestration and confirmation
  standards (single entry point, explicit run state, identity-checked
  human confirmations).
