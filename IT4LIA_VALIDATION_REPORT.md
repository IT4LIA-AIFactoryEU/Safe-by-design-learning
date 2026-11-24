# IT4LIA release validation report

Validation date: 2026-10-13  
Candidate version: `1.0.0-it4lia.1`  
Source archive: `Safe_by_Design_EBM_GitHub.zip`

## Outcome

Repository-side IT4LIA requirements, syntax checks, structural validation, and
frozen-artifact integrity checks pass. Full JAX inference could not be executed
in the packaging environment because JAX, JAXlib, and Optax were unavailable
and the restricted package index exposed no installable distributions. This is
reported as an environment blocker, not a successful test or a repository
failure.

The candidate remains subject to the legal and GitHub-organization release
gates recorded in `IT4LIA_COMPLIANCE_CHECKLIST.md`.

## Validation matrix

| Check | Result | Evidence |
|---|---|---|
| Python compilation | PASS | All 137 Python files compiled with bytecode redirected outside the repository. |
| IT4LIA repository validator | PASS | 109 project-owned Python files have the uniform MIT/author header; 9 immutable README files match their original SHA-256 values. |
| Structural release validator | PASS | Six dataset layouts and all required checkpoints, scripts, runtime files, and certificate indexes were found; 340 release files inspected. |
| PortHNN-u frozen artifacts | PASS | Four checkpoints contain finite, non-empty arrays; stored Duffing and three-link metrics were recomputed, while CED and Silverbox records were validated. |
| HNER99 frozen artifacts | PASS | Nine reports and nine artifact-index entries validated; documented historical provenance gaps remain explicit. |
| JSON and YAML parsing | PASS | All bundled JSON, YAML, GitHub workflow, and issue-template files parsed successfully. |
| Secret-pattern scan | PASS | No private-key marker, AWS secret field, generic API-key assignment, or generic secret assignment was found in text files. |
| Binary-artifact preservation | PASS | 51 retained model/data/figure binary artifacts are byte-identical to the input archive; no retained binary changed. |
| External raw-data policy | PASS | Exactly 20 raw benchmark binary/text data files were excluded. The two pre-existing Silverbox README files remain byte-identical under the immutable-README constraint. |
| External-data restoration paths | PASS | The previously audited manifest contains paths, sizes, and SHA-256 values; isolated materialization tests reproduced all 22 manifest records. |
| Full pH-EBM inference | BLOCKED | `ModuleNotFoundError: No module named 'jax'`. Required versions are declared in `requirements.txt`. |
| PortHNN-u runtime smoke test | BLOCKED | Same missing-JAX environment blocker. |

## Commands executed

```bash
PYTHONPYCACHEPREFIX=<temporary-directory> python -m compileall -q Safe_by_Design_EBM_IT4LIA
python Safe_by_Design_EBM_IT4LIA/scripts/validate_it4lia_compliance.py
python Safe_by_Design_EBM_IT4LIA/validate_release.py --structural
python Safe_by_Design_EBM_IT4LIA/datasets/fetch_external_datasets.py verify
```

For the full validation attempt, a private temporary copy was populated with
the audit-held CED, Silverbox, and NanoDrone raw files and the following command
was run:

```bash
PYTHONDONTWRITEBYTECODE=1 python <temporary-copy>/validate_release.py
```

The structural and frozen-artifact sections passed in that copy. The inference
and PortHNN-u runtime sections stopped before model execution because JAX was
not installed.

An installation attempt was made without changing the repository:

```bash
python -m pip install jax==0.9.2 jaxlib==0.9.2 optax==0.2.5
```

The restricted environment returned no available distributions. No broad
exception handling or silent skip was added to production code.

## Exact completion command

In a network-enabled Python 3.11 environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python datasets/fetch_external_datasets.py all
python datasets/fetch_external_datasets.py verify
python validate_release.py
python scripts/validate_it4lia_compliance.py
```

The full command must pass before the Git tag and GitHub Release are created.

## Preserved scientific artifacts

The comparison against the input archive found 51 common binary scientific
artifacts and zero byte changes. The only removed binary/data artifacts are the
20 download-only CED, Silverbox, and NanoDrone raw files listed in
`datasets/EXTERNAL_DATA_MANIFEST.json`. No checkpoint, learned parameter,
configuration, certificate report, or figure was modified.

## Remaining publication gates

1. Validate the legal copyright-holder wording in `LICENSE`.
2. Resolve the NanoDrone compatibility-code license or approve a documented
   IT4LIA derogation.
3. Approve the placement exception caused by the immutable root README, which
   lacks policy-required owner/support references and retains its historical
   directory command.
4. Configure least-privilege access, issue labels, Dependabot alerts, private
   vulnerability reporting, and protected `main` settings in GitHub.
5. Require structural validation and CodeQL status checks.
6. Complete the JAX end-to-end commands above.
7. Create tag `v1.0.0-it4lia.1` and publish the corresponding GitHub Release.
