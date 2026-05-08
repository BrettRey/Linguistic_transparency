# STATUS

## Current state (2026-04-30)

Project scaffolded per `PROJECT-BRIEF.md`. No drafting started. No sources verified. No bibliography built.

## What exists

- `PROJECT-BRIEF.md` — Brett's full project package preserved verbatim (canonical brief)
- `CLAUDE.md` — role, purpose, source-grounding, sister-project relationships, style, terminology, workflow, non-negotiable argumentative discipline
- `STATUS.md` — this file
- `DECISIONS.md` — initial decisions logged
- `README.md` — orientation
- `paper/sources/sources.bib` — empty placeholder
- `paper/sources/source-notes.md` — curation template + checklist of brief's seven citations + sister-paper bib entries to inherit
- `paper/draft/00-abstract.md` through `paper/draft/08-conclusion.md` — nine section stubs, each with section-level argument-map sketch from the brief + TODO marker
- `paper/notes/argument-map.md` — section-by-section argument plus the umbrella schema as the single piece all sections must trace back to
- `paper/notes/claims-to-verify.md` — every brief citation needs verification (LLM-surfaced)
- `paper/notes/terminology.md` — technical-term decisions
- `paper/notes/possible-venues.md` — venue list

## What does not exist yet

- LaTeX scaffolding (Makefile, `.house-style/` snapshot, `references.bib` symlink). Deferred to step 4 (conversion stage).
- Verified bibliography. The brief's seven citations all need verification before they enter `sources.bib`.
- Worked examples for each sense.
- Korean data with sources. Cases in §2 of the brief are placeholders; either Brett sources-grounds them or co-author Jongbok contributes.
- A 1,500-word expanded proposal.
- Risk register.
- A git repository (local or remote).

## Next action

Recommend in order:

1. Verify the brief's seven citations against publishers' authoritative pages. Drop or replace any that don't survive verification. Particular attention to Bell & Schäfer and Heyer & Kornishova; LLM web-search citation tools regularly mis-author or mis-date psycholinguistics papers.
2. Decide the Korean question with Jongbok: solo-authored with brief-mention Korean cases vs. co-authored with substantive Korean section. This decision shapes §2's scope significantly.
3. Decide on the metaphysical framing: pure Khalidian (per brief) or HPC-book's maintenance/SPC framework (for consistency with sister papers). This is a §7-and-conclusion decision; can stay open until then but shouldn't drift.
4. Build out the worked example for *a lot of* (the brief's anchor case) source-grounded against CGEL.

## Open carryovers

- Project folder name `Linguistic_transparency/` to be confirmed.
- GitHub repo decision pending.
- Bell & Schäfer reference: confirm authors, year, journal volume, DOI, and that the paper actually says what the brief reports.
- Heyer & Kornishova reference: same.
- Whether to import HPC-theory bib entries from `papers/Field_relative_HPC_categories/paper/sources/sources.bib` (Boyd 1991, Boyd 1999, Khalidi 2013, Hacking 1999, Reynolds HPC book) or maintain a separate set.

## Submission target

*Language Sciences* (per sister-paper precedent and the metaphysical-linguistic shape of the argument). Subject to revision.

## Sister projects

- `papers/What_do_we_mean_by_language/` — preprint LingBuzz 009947 / PhilArchive REYWDW (posted 2026-04-28). Closest predecessor methodologically.
- `papers/Field_relative_HPC_categories/` — drafting. Closest predecessor argumentatively.
- `papers/HPC book/` — chapter 7 (projectibility) is load-bearing for the metaphysical framing. The NPI-as-class-not-kind passage in chapter 7 is the structural analogue.
