# Repository governance

## Responsibility

- Owner and administrator: Simone Betteti
- Operational maintainer: Simone Betteti
- Security point of contact: the channels defined in `SECURITY.md`
- IT4LIA organization support: `support-it4lia@cineca.it`

The repository owner is accountable for access reviews, repository settings,
issue and pull-request triage, release management, and escalation to the IT4LIA
GitHub organization administrators.

## Access model

Access must follow least privilege:

- **Read** for consultation;
- **Triage** for issue and pull-request management without code writes;
- **Write** for active contributors;
- **Maintain** for operational repository management;
- **Admin** only for the owner and specifically authorized organization staff.

Prefer IT4LIA teams over direct user assignments. Review access at least every
six months and whenever a contributor joins, leaves, changes role, or a security
incident occurs.

## Changes and reviews

Non-trivial changes must be proposed through pull requests. Changes to
`.github/`, `SECURITY.md`, `CONTRIBUTING.md`, `LICENSE`, release configuration,
or other governance material require an approving review before merge.

The `main` branch must prohibit force pushes and deletion, require a pull
request and one approving review, and require the repository validation status
checks. These controls are GitHub settings and must be enabled by an
administrator after import into the IT4LIA organization.

## Issue taxonomy

The minimum label taxonomy is:

- `bug`: reproducible defects;
- `enhancement`: new capability proposals;
- `question`: clarification and support requests;
- `security`: internal triage only; vulnerabilities must follow `SECURITY.md`;
- `documentation`: documentation-only changes;
- `dependencies`: dependency maintenance.

Operational work belongs in issues. General discussion and brainstorming
should use GitHub Discussions if that feature is enabled.

## Releases

Releases follow Semantic Versioning. Every public release must identify one
commit with a Git tag, be published through GitHub Releases, and include release
notes describing changes and any compatibility impact. Conventional Commits
are recommended for commit messages.
