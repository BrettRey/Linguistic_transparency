# Bibliography validation: umbrella paper

Date: 2026-08-22
Verdict: pass with one non-blocking metadata warning

- Biber resolves all 53 cited keys across the shared bibliography and `references-local.bib`; no citation key is missing.
- The one project-local entry, `kim-reynolds-2026-two-kinds-transparency`, is cited and contains author, title, date, type, and URL.
- `biber --validate-datamodel main` reports one warning: the shared-library `@online` entry `rae-concordancia-mayoria` has no publication `date` or `year`. The entry does have author, title, organization, URL, and an access date. The RAE page exposes no publication date, so this is a legitimate `n.d.` source rather than a broken citation; it is not a pre-JB blocker.
- Unused entries in the shared central bibliography are expected and were not treated as manuscript-local debris. There are no unused project-local entries.
