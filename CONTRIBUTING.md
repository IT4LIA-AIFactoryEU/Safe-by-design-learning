# Contributing

Thank you for helping improve the framework.

## Before opening an issue

- Use the bug template for reproducible defects.
- Use the feature template for new capabilities.
- Use the question template for usage or interpretation questions.
- Follow `SECURITY.md` for vulnerabilities; never report them publicly.

Search existing issues before opening a new one. Include the repository
version, Python version, operating system, exact command, minimal inputs, and a
short traceback where applicable. Never attach credentials or private data.

## Contribution workflow

1. Create an issue or reference the relevant context.
2. Create a focused branch from `main`.
3. Make one coherent change and add or update tests.
4. Run the validation commands below.
5. Open a pull request using the repository template.
6. Address review feedback; do not force-push after review unless coordinated.

External contributors should use a fork. IT4LIA organization members should
prefer branches when their permissions allow it.

## Validation

```bash
python -m compileall -q .
python validate_release.py --structural
python scripts/validate_it4lia_compliance.py
```

Run the relevant end-to-end validators when dependencies and benchmark data are
available. Do not overwrite frozen checkpoints, configurations, figures, or
certificate reports.

## Code style

- Target Python 3.11.
- Prefer clear, typed, testable functions and explicit failures.
- Avoid machine-specific paths and hidden network access.
- Preserve public APIs, checkpoint compatibility, and numerical semantics.
- Keep dataset-specific logic out of the common model core.
- Add concise human-readable docstrings and comments for non-obvious behavior.
- Keep source attribution and the MIT license disclaimer current.

Project-owned source files must identify their substantive authors and refer to
the root `LICENSE`. Do not apply project attribution or licensing headers to
third-party code; preserve its upstream notices and record it in
`THIRD_PARTY_NOTICES.md`.
