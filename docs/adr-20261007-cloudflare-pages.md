# Host the static website on Cloudflare Pages

Status: Accepted. Date: 2026-10-07.

## Context

GitHub Pages served this static site behind Cloudflare's DNS proxy. HTTPS returned 526 because GitHub's origin certificate did not match zeitflow.de. Restarting custom-domain provisioning did not resolve the mismatch. The owner authorized migration.

## Decision

Use Pages project `zeitflow-website` in the account owning the apex zone. Attach zeitflow.de and www.zeitflow.de through Pages, replacing only their conflicting DNS records. Preserve certificate validation and the existing GitHub repository as source. Deploy using Direct Upload.

## Alternatives

- Wait for GitHub certificate provisioning: uncertain recovery time after an unsuccessful restart.
- Reduce origin TLS validation: unnecessary loss of hostname validation.
- Add Git-integrated deployment: future automation requires separate setup; Direct Upload restores this small static site immediately.

## Consequences

The website no longer depends on GitHub origin TLS. GitHub commits do not automatically deploy to Pages; upload the complete static bundle. Cloudflare's global hosting is reflected in the privacy notice. Mail and other subdomains remain independent.

## Verification

Original HTML matched byte-for-byte at pages.dev before switching DNS. Both custom domains became Active with SSL enabled and returned HTTPS 200 with certificate validation. DNS now uses proxied CNAMEs to zeitflow-website.pages.dev. Legal-page additions use the same deployment process.

Related: README.md; AFFiNE Project — ZeitFlow website; ZeitFlow website — Hosting and HTTPS runbook. Shared ADR title: ZeitFlow website — ADR-20261007-cloudflare-pages — Host the static website on Cloudflare Pages.
