# Third-party notices and exceptions

The root MIT License applies to project-owned source code. It does not override
the licenses or terms of third-party software, data, or pretrained artifacts.

## DeepDissipativeModel

- Upstream: https://github.com/kojima-r/DeepDissipativeModel
- Authors: Yuji Okamoto and Ryosuke Kojima
- License: MIT
- Local location: `dataset_interfaces/baseline_interfaces/deep_dissipative_model/`
- License copy: `third_party_licenses/DeepDissipativeModel-MIT.txt`

The retained upstream source is excluded from the project-wide Simone Betteti
authorship header.

## NanoDrone benchmark reference model

- Upstream: https://github.com/idsia-robotics/nanodrone-sysid-benchmark
- Authors: Riccardo Busetto, Elia Cereda, Marco Forgione, Gabriele Maroni,
  Dario Piga, and Daniele Palossi
- Paper: *Nonlinear system identification for a nano-drone benchmark*,
  Control Engineering Practice 172 (2026), 106871
- Local compatibility location:
  `dataset_interfaces/baseline_interfaces/nanodrone_bb/`

The upstream repository publicly distributes its data and reference
implementations, but no explicit repository license was identified during the
2026-10-13 audit. The local compatibility implementation and frozen project
checkpoint are retained to preserve reproducibility, but they are excluded from
the root MIT grant pending written license clarification or approval of an
IT4LIA policy exception. This exception is recorded in
`IT4LIA_COMPLIANCE_CHECKLIST.md` and must be resolved before an unqualified
public-release approval.

## Benchmark datasets

CED, Silverbox, and NanoDrone raw inputs are not redistributed in this IT4LIA
bundle because an explicit downstream redistribution license was not found.
Canonical sources, citations, expected paths, byte sizes, and SHA-256 hashes are
recorded in `datasets/EXTERNAL_DATA_MANIFEST.json`. Use
`datasets/fetch_external_datasets.py` for explicit acquisition and validation.

The two small upstream Silverbox README files already present in the established
repository are retained byte-for-byte under the project's immutable-README
constraint. Their presence is documented as an exception and does not imply a
license grant for the accompanying benchmark data, which are not bundled.

The BSD 3-Clause license included under `datasets/licenses/` covers the
`nonlinear_benchmarks` loader software, not the third-party datasets it fetches.
