# IT4LIA repository policy checklist

Policy basis: *Policy per la gestione dei repository GitHub di IT4LIA*, v1.1.
Assessment date: 2026-10-13.

`Implemented` means evidence is present in this archive. `External action`
means the requirement must be configured or approved in the GitHub organization
and cannot be proven by repository files alone. `Exception` requires formal
IT4LIA approval before publication.

| ID | Applicable | Status | Evidence / required action |
|---|---|---|---|
| REQ-001 | Yes | Partial | `GOVERNANCE.md` identifies Simone Betteti as owner/admin and maintainer. Confirm the Admin role after import. |
| REQ-002 | Yes | External action | Apply the least-privilege role model in `GOVERNANCE.md`; prefer IT4LIA teams. |
| REQ-003 | Yes | External action | Organization administrator must review visibility, collaboration, and security settings. |
| REQ-004 | Yes | Exception | Existing README files are intentionally immutable. The root README supplies description, context, and usage but does not contain the required owner/support references. Those references are in `GOVERNANCE.md`, `CONTRIBUTING.md`, and `SECURITY.md`; approve this documented placement derogation or authorize a later README update. |
| REQ-005 | Yes | Partial | Root `LICENSE` contains MIT and the IT4LIA project statement. The final legal-entity holder configuration requires competent legal approval. |
| REQ-006 | Yes | Partial | Project-owned Python source has a uniform MIT disclaimer and author. DDM retains upstream MIT terms. NanoDrone compatibility code is an unresolved third-party exception documented in `THIRD_PARTY_NOTICES.md`. |
| REQ-007 | Yes | Implemented | `SECURITY.md` defines supported versions, private channels, and response targets. |
| REQ-008 | Yes | Implemented | `CONTRIBUTING.md` defines bug/feature reporting, workflow, validation, and code style. |
| REQ-009 | Yes | External action | Configure GitHub permissions according to `GOVERNANCE.md`. |
| REQ-010 | Yes | Implemented | Security contact route is defined in `SECURITY.md`. |
| REQ-011 | Yes | External action | `.github/dependabot.yml` is present; an admin must enable Dependabot alerts and confirm repository security features. |
| REQ-012 | Yes | Partial | README placement, immutable upstream Silverbox README files, and NanoDrone licensing exceptions are documented here; formal approval remains required. |
| REQ-013 | Yes | External action | Templates are present; enable GitHub Issues and apply the operating model in `GOVERNANCE.md`. |
| REQ-014 | Yes | External action | Minimum taxonomy is defined in `GOVERNANCE.md`; create the labels in GitHub. |
| REQ-015 | Yes | External action | Protect `main`: require PRs and one approval; block force pushes and deletion. |
| REQ-016 | Yes | External action | Require the structural-validation and CodeQL status checks after their first successful run. |
| REQ-017 | Yes | Implemented | `.github/pull_request_template.md` records context, impacts, and verification. |
| REQ-018 | Yes | Partial | `VERSION`, `CHANGELOG.md`, and release instructions are present. Create the tag and GitHub Release only after final approval. |
| REQ-019 | Yes | Partial | All known exceptions are documented above; obtain IT4LIA approval before publication. |

