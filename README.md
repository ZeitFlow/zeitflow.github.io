# ZeitFlow website

Last updated: 2026-10-07

Public website: https://zeitflow.de/ (also https://www.zeitflow.de/).
Source repository: https://github.com/ZeitFlow/zeitflow.github.io, branch `main`.

## Hosting

Cloudflare Pages project: `zeitflow-website`.
Production preview: https://zeitflow-website.pages.dev/.
Dashboard: https://dash.cloudflare.com/64962783605a1e749a4ea11b02405af0/pages/view/zeitflow-website.

The project uses Direct Upload. GitHub changes do **not** automatically deploy to Pages. Upload the complete static bundle after changing repository files. Deploy in the personal account owning zeitflow.de (account ID `64962783605a1e749a4ea11b02405af0`, zone ID `6f2b6722489ed4d2591d95bbcb3d80bd`). Local Wrangler was authenticated to a separate ZeitFlow UG account during migration; check the account before any CLI deployment.

Both domains are Active Pages custom domains with SSL enabled. DNS uses proxied CNAMEs to `zeitflow-website.pages.dev`; the four GitHub A and four AAAA records were replaced. Mail and unrelated subdomains were preserved. Both website domains serve content directly.

## Files and updates

- `index.html`: landing page, inline styles, contacts, legal links.
- `impressum/index.html`: German company notice.
- `privacy/index.html`: German privacy notice scoped to this website.
- `legal.css`: shared legal-page styles.

No application build, forms, analytics, external fonts or application cookies are used. Cloudflare injects an email-protection script and may use security cookies. Keep the privacy notice synchronized with future service changes. The owner confirmed company details on 2026-10-07.

Create a ZIP containing only those four static files, preserving their directory structure. Exclude README, ADRs, screenshots, old ZIPs and tooling. In the dashboard select Create deployment, Production and upload the ZIP. Verify all pages and navigation after deployment.

```sh
curl -I https://zeitflow.de/
curl -I https://www.zeitflow.de/
curl -I https://zeitflow.de/impressum/
curl -I https://zeitflow.de/privacy/
```

Retain certificate verification. If a new hostname is temporarily missing from the local resolver cache, use `curl --resolve hostname:443:<confirmed Cloudflare IP>` without `-k`, then repeat the ordinary request after cache expiry.

## Incident and migration

On 2026-10-07 public HTTPS returned Cloudflare 526. The edge certificate was valid, but GitHub Pages served CN `*.github.io` for SNI zeitflow.de. Re-adding the GitHub custom domain did not restore origin HTTPS. The owner authorized migration. The original HTML (GitHub blob `5b569b6e0116b6b753899a2bca6ffe9fb6b286c0`) was deployed unchanged first and verified byte-for-byte at the Pages endpoint. Both custom domains were then attached. Origin certificate validation was not weakened. Legal pages were added afterward at the owner's request.

Shared AFFiNE documents: Project — ZeitFlow website; ZeitFlow website — Hosting and HTTPS runbook; ZeitFlow website — ADR-20261007-cloudflare-pages — Host the static website on Cloudflare Pages. Local ADR: `docs/adr-20261007-cloudflare-pages.md`.
