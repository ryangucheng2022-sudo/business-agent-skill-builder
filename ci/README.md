# CI kit

Ready-to-enable GitHub Actions setup, kept outside `.github/workflows/`
so it can be reviewed and versioned like any other file.

**Enable it:** copy `ci.yml` to `.github/workflows/ci.yml` and push.

The job runs the skill validator against this repo itself (it must pass:
frontmatter present, links resolve, boundary and validation material in
place) and asserts that the deliberately broken fixture in
`ci/broken-skill/` is rejected.
