# Changelog

All notable changes follow Semantic Versioning.

## [1.0.0-it4lia.1] - 2026-10-13

### Added

- IT4LIA governance, contribution, security, conduct, and compliance records.
- Issue and pull-request templates.
- Dependabot and CodeQL configuration.
- Uniform MIT and authorship headers for project-owned source.
- Dataset acquisition manifest and checksum-verified fetch utility.

### Changed

- Labeled the distribution as the IT4LIA policy-aligned release candidate.
- Separated project-owned source from third-party licensing exceptions.

### Removed

- Unlicensed redistributions of CED, Silverbox, and NanoDrone raw benchmark
  inputs. Canonical acquisition instructions and audited checksums replace the
  bundled raw files.

### Compatibility

No model equations, checkpoint bytes, experiment configurations, or learned
parameters were changed. End-to-end benchmark execution requires users to
acquire download-only raw datasets explicitly.
