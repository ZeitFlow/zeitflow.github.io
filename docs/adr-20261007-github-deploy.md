# Deploy main pushes through GitHub Actions

Status: Accepted; credential activation and first production run pending.
Date: 2026-10-07.

## Context

The owner requested automatic deployment after migrating the static website to Pages project `zeitflow-website`. The project uses Direct Upload. Recreating it for native Git integration would require moving working custom domains again.

## Decision

Replace the old GitHub Pages workflow with GitHub Actions deploying to the existing Pages project. Trigger on pushes to main and manual dispatch. Build an explicit list of website assets into dist/ and use the official Wrangler action. Read the project's actual production branch before deploying. Use a Cloudflare Pages Edit token restricted to the zone-owning account and stored as a GitHub repository Actions secret.

## Alternatives

- Recreate a Git-integrated project: extra domain migration and access setup, with no benefit for this small static site.
- Continue manual ZIP uploads: does not meet the requested push deployment.
- Deploy the entire repository: would expose documentation and tooling as public website files.

## Consequences

Source and deployment configuration are versioned in one repository. Changes on main can publish automatically; pull requests cannot access the token through this workflow. The Pages token is account-scoped, not project-scoped, so its authority includes other Pages projects in that account. Revoking the token disables automatic publishing. The token must remain only in GitHub Secrets and be rotated there when needed. Existing domains, DNS and website processing behavior are unchanged.

## Implementation and verification

Workflow: .github/workflows/static.yml. Build script: scripts/build.py. Production-branch resolver: scripts/pages-production-branch.py. Actions are pinned to verified upstream commit SHAs; Wrangler is pinned to 4.148.0. GitHub permissions are contents:read and deployments:write. The local build produced exactly four files identical to source; actionlint v1.7.12 passed. Activation requires the token secret and a successful push-triggered production run.

Related: README.md; adr-20261007-cloudflare-pages.md; AFFiNE Project — ZeitFlow website and ZeitFlow website — Hosting and HTTPS runbook. Shared ADR title: ZeitFlow website — ADR-20261007-github-deploy — Deploy main pushes through GitHub Actions.
