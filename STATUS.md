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

### 2026-05-21 Session Notes

- Revised and shipped the paper after Brett's style, framing, and KWIC evidence pass: syntax remains the central field, the paper asks the naturalization question locally, and projectibility profiles carry the result.
- Added `paper/data/kwic-checks.md`; updated Appendix A, `paper/data/coca-pilot.md`, `figures/fig_override.py`, `figures/fig_override.pdf`, and `figures/fig_override.png` so the COCA pilot reports KWIC-filtered override evidence and flags conservative unfiltered cells.
- Replaced the Korean placeholder with an explicit deferred-extension section, so Korean is no longer treated as present evidence before Kim's contribution.
- Corrected the acknowledgement to OpenAI Codex 5.5 after Brett caught the stale Codex 5.3 wording.
- Verification completed: `check-style.py --strict --no-ai paper/sections/*.tex`, `git diff --check`, and `make -B` all passed/build completed; the PDF was 41 pages. Remaining build noise is ordinary EB Garamond microtype slot warnings, `fancyhdr` `E` option without `twoside`, and underfull boxes.
- Shipped `0b8b554` (`Revise transparency evidence and KWIC audit`) and `a0e5788` (`Correct Codex model acknowledgement`) to `origin/main`; the current latest commit later showed `a770d9d` (`Format numbered examples and references`) on `main`.
- Local carryover: untracked `paper/sections/main.tex` remains untouched. `DECISIONS.md` has the pre-existing 2026-05-11 Kim-sharing note plus the 2026-05-21 shutdown entries.

### 2026-06-16 Session Notes

- Committed to the umbrella-paper framing (not a number-transparent-QN paper); Korean is the committed cross-linguistic test, to be run by Kim. The umbrella's contribution is reframed as a comparative concept plus the non-instance "could-have-made-P-inaccessible" diagnostic (§1, §6, §7).
- Ran a redundant review board (7 Opus + 7 Codex reviewers; `reviews/` is gitignored scratch): unanimous Revise & Resubmit; both boards identify the non-instance diagnostic as the paper's genuine contribution.
- Board-driven revisions: surfaced the *bunch* demotion into §2.2 body, then softened it to a projectibility-claim localization; recoded Table 1 rest/remainder to complement-controlled; weakened SPC cliquishness claims and the §7.1 "mechanism" wording; demoted the §7.4 count-cluster Khalidi claim to a cross-reference (3A); strengthened the §6 cross-linguistic defence with a language-internal decision procedure and a direct Newmeyer engagement (5B).
- Source-grounding: added verified Kay & Fillmore 1999 and reattributed the *What's X doing Y?* example (§3.3); obtained Feldman et al. 2015 (Frontiers) and Newmeyer 2007 (library) into `literature/`, and verified §5.3 and §6.4 against them.
- Open: TFR "syntactic-category transparency" relabel (Kim pass); pre-existing "the present paper" self-references flagged by check-style (10+ instances); three duplicate bib keys (`/push-bib` or prune).
- Later the same day: the schema sentence now embeds the conceal-variant in all five statements (abstract, §1, §6, §7, §8); §6 gains two cross-linguistic cases (Tsez, a verified head-marking case with an attested conceal/transparent minimal pair; a Spanish *mayoría* nod); Swahili checked against Zerbian & Krifka and rejected (no concealing variant); unverified leads parked in `paper/notes/cross-linguistic-qn-leads.md` for the Korean extension.
- **Structural restructure (decision B): form--meaning material spun out.** Old §§3--5 + appendices B/C/D compressed to one §3 (\enquote{Form--meaning transparency}); substance moved to new sibling repo `papers/Form-meaning_transparency/` (seed: scaffold + migrated sections + `paper/notes/migration-notes.md` + STATUS). Umbrella structure now: §1 intro, §2 morphosyntactic (delivered result), §3 form--meaning (compressed, defers to the new paper), §4 typological (was §6), §5 projectibility profiles (was §7), §6 conclusion (was §8), Appendix A only. All cross-refs fixed; clean build, 31 pp. **Both repos have uncommitted changes** (umbrella revision; new-paper seed beyond the auto initial commit) — not yet shipped.
