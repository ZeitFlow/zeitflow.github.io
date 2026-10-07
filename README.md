# ZeitFlow website

Last updated: 2026-10-07

Public website: https://zeitflow.de/ (also https://www.zeitflow.de/).
Source repository: https://github.com/ZeitFlow/zeitflow.github.io, branch `main`.

## Hosting

Cloudflare Pages project: `zeitflow-website`.
Production preview: https://zeitflow-website.pages.dev/.
Dashboard: https://dash.cloudflare.com/64962783605a1e749a4ea11b02405af0/pages/view/zeitflow-website.

The project uses the Pages Direct Upload API through GitHub Actions. `.github/workflows/static.yml` deploys pushes to `main` and can also be run manually from Actions. The repository secret is configured. The previous GitHub Pages deployment workflow is replaced.

First verified push deployment: [Actions run 37607231701](https://github.com/ZeitFlow/zeitflow.github.io/actions/runs/37607231701), commit `62d8815`, production branch `main`, completed successfully on 2026-10-07. Deployment: https://b62867e8.zeitflow-website.pages.dev/. Homepage and both legal pages returned HTTPS 200 afterward.

Deploy in the personal account owning zeitflow.de (account ID `64962783605a1e749a4ea11b02405af0`, zone ID `6f2b6722489ed4d2591d95bbcb3d80bd`). Local Wrangler was authenticated to a separate ZeitFlow UG account during migration; check the account before any CLI deployment.

Both domains are Active Pages custom domains with SSL enabled. DNS uses proxied CNAMEs to `zeitflow-website.pages.dev`; the four GitHub A and four AAAA records were replaced. Mail and unrelated subdomains were preserved. Both website domains serve content directly.

## Files and updates

- `index.html`: landing page, inline styles, contacts, legal links.
- `impressum/index.html`: German company notice.
- `privacy/index.html`: German privacy notice scoped to this website.
- `legal.css`: shared legal-page styles.

No application build, forms, analytics, external fonts or application cookies are used. Cloudflare injects an email-protection script and may use security cookies. Keep the privacy notice synchronized with future service changes. The owner confirmed company details on 2026-10-07.

## Automatic deployment

Create a Cloudflare API token with `Account -> Cloudflare Pages -> Edit`, restricted to the account above. Store it only as the `CLOUDFLARE_API_TOKEN` Actions secret in this GitHub repository. Never commit it, put it in documentation, or paste it into a workflow. The account ID is public configuration and is set explicitly in the workflow.

The workflow prepares `dist/` with `python3 scripts/build.py`, reads the existing Pages production branch with `scripts/pages-production-branch.py`, and deploys with the official Wrangler action. Reading the project branch avoids accidentally publishing a preview when the project's production branch differs from GitHub's `main`. The token grants account-level Pages access; Cloudflare's token permission is not restricted to one Pages project.

GitHub permissions are limited to reading repository contents and recording deployments. The workflow does not run on pull requests. Production deployments run serially. Actions are pinned to commit SHAs and Wrangler is pinned to 4.148.0. Update these pins deliberately.

```sh
python3 scripts/build.py
git add <changed-files>
git commit -m 'Update website'
git push origin main
```

When adding website assets, extend the explicit file list in `scripts/build.py`. The deploy directory contains only website assets; source tooling and documentation are excluded. Check the Actions run and Pages production deployment after each push. A missing token or API authorization error fails the workflow rather than reporting a successful deployment.

## Manual recovery deployment

Prepare `dist/` with the build script, ZIP its contents preserving their directory structure, then select Create deployment -> Production in the Pages dashboard. Verify pages and navigation afterward. Use the dashboard's production rollback to return to a previously successful deployment if necessary.

```sh
curl -I https://zeitflow.de/
curl -I https://www.zeitflow.de/
curl -I https://zeitflow.de/impressum/
curl -I https://zeitflow.de/privacy/
```

Retain certificate verification. If a new hostname is temporarily missing from the local resolver cache, use `curl --resolve hostname:443:<confirmed Cloudflare IP>` without `-k`, then repeat the ordinary request after cache expiry.

## Incident and migration

On 2026-10-07 public HTTPS returned Cloudflare 526. The edge certificate was valid, but GitHub Pages served CN `*.github.io` for SNI zeitflow.de. Re-adding the GitHub custom domain did not restore origin HTTPS. The owner authorized migration. The original HTML (GitHub blob `5b569b6e0116b6b753899a2bca6ffe9fb6b286c0`) was deployed unchanged first and verified byte-for-byte at the Pages endpoint. Both custom domains were then attached. Origin certificate validation was not weakened. Legal pages were added afterward at the owner's request.

Shared AFFiNE documents: Project — ZeitFlow website; ZeitFlow website — Hosting and HTTPS runbook; ZeitFlow website — ADR-20261007-cloudflare-pages — Host the static website on Cloudflare Pages; ZeitFlow website — ADR-20261007-github-deploy — Deploy main pushes through GitHub Actions. Local ADRs are in `docs/`.
