# Deploy main pushes through GitHub Actions

Status: Accepted and implemented.
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

Workflow: .github/workflows/static.yml. Build script: scripts/build.py. Production-branch resolver: scripts/pages-production-branch.py. Actions are pinned to verified upstream commit SHAs; Wrangler is pinned to 4.148.0. GitHub permissions are contents:read and deployments:write. The local build produced exactly four files identical to source; actionlint v1.7.12 passed.

The owner confirmed token creation and storage in GitHub Secrets. The account-owned token has only Pages Write permission in the website account. The temporary transfer file was deleted after saving the secret. The first push-triggered run [37607231701](https://github.com/ZeitFlow/zeitflow.github.io/actions/runs/37607231701), commit `62d8815`, completed successfully and deployed production branch main to https://b62867e8.zeitflow-website.pages.dev/. Homepage and legal pages returned HTTPS 200 after deployment.

Related: README.md; adr-20261007-cloudflare-pages.md; AFFiNE Project — ZeitFlow website and ZeitFlow website — Hosting and HTTPS runbook. Shared ADR title: ZeitFlow website — ADR-20261007-github-deploy — Deploy main pushes through GitHub Actions.
