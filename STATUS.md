# STATUS
<!-- SUMMARY: Umbrella transparency paper (Reynolds & Kim); Kim's second (2026-07-23) review implemented (data/glosses/SPC/bib); awaiting Kim's Korean draft + tracked-changes round · status: revising with coauthor · updated: 2026-07-23 -->

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

### 2026-06-16 (night) Session Notes — spin-out shipped + polish round

- Form--meaning material spun out to new public repo **github.com/BrettRey/Form-meaning_transparency** (seed: scaffold + migrated §§3--5 + appendices B/C/D + `paper/notes/migration-notes.md` + Levi citation). Umbrella now 6 sections (§1 intro, §2 morphosyntactic, §3 form--meaning, §4 typological, §5 projectibility profiles, §6 conclusion, Appendix A); 31 pp.
- Polish: gloss convention (`..' not `\enquote{}`); category-vs-class footnote (Haspelmath descriptive vs HPC kind, §6.1); Croft 2001 + Hoeksema 2012 + Levi 1978 citations (web-verified) and §6.1 name-drop trim and "the present" fix; the label-isn't-projectible point made explicit (abstract/§1/§7); redundancy pass (6 trims); Table 1 reformatted with `\multicolumn` sub-group rows.
- Venue: see `paper/notes/possible-venues.md` (targets *Language Sciences*, Elsevier). Discussed LSA *Language* as a higher-bar aim contingent on de-encumbering the framework and delivering the Korean test.
- Both repos shipped this session.

### 2026-06-17 Session Notes — rhetoric/clarity pass (intro, conclusion, §2)

- Two-part rhetoric/clarity/exposition pass on the umbrella paper. §1 (intro) + §6 (conclusion) shipped as `562d721`; §2 (morphosyntactic) edited but **uncommitted** at shutdown (4 edits in the working tree, pending ship).
- §6 conclusion now names the non-instance "could-have-concealed-P" diagnostic as the schema's distinctive contribution (both review boards flagged it as the genuine contribution; it was previously only implied). §1's QN-cluster preview aligned to §2's canonical wording (partitive availability / restricted premodification).
- §1 clarity fixes: opaque "across mediators with opposite morphological number" rephrased; gapping fix in the contribution sentence; clause-initial comma; articles. Cadence thinned 4→3 openers.
- §2 edits (uncommitted): trimmed a back-to-back "P is on the complement, not the head" restatement (§2.1); "Where the non-singular construal is sourced differs" → "The source of the non-singular construal differs" (§2.2); contractions (§2.2); fixed a garbled §2.4 sentence (doubled "within-domain" + a clause that had §2.4 cross-referencing its own falsification condition).
- Judgment calls held (logged): "lexical class" kept (HPC term, check-style false positive per the category-vs-class decision); §2's 9-opener "The X is Y" cadence warning left as a length artifact rather than mechanically rewriting board-approved prose.
- Build clean throughout (single-pass XeLaTeX, no errors). DECISIONS.md current for both passes.
- Next: ship the §2 working-tree changes (`DECISIONS.md`, `main.pdf`, `paper/sections/02-morphosyntactic-transparency.tex`); untracked `paper/sections/main.tex` remains the known carryover.
- Kim replied later on 2026-06-17: he wants to coauthor the umbrella paper as well as the TFR-focused companion, accepts the stage-setting direction, and will read carefully in early July after travel; unavailable until July 8.


### 2026-06-25 Session Notes — head-marked transparency check

- Incorporated Bert/Otto's Shilluk result as a negative: no transparency in the serialization diagnostic; the pronominal subject had to be singular and plural was rejected despite the embedded plural possessor. The Shilluk fact is not currently added as a main-text example, but it guides the interpretation.
- Added a short §6 paragraph on head-marked agreement systems after the Tsez discussion. The paragraph says genuine English-style NP transparency is not securely attested in the gathered head-marked sources; apparent positives cluster around possessors and are usually possessor raising, external possession, applicative promotion, incorporation, or null-argument mediation.
- Gathered valid PDFs under `paper/sources/head-marked-transparency/`; added six BibTeX entries to `references-local.bib`; added source notes for Ritchie/Chimane, Deal/external possession and possessor raising, Bohnemeyer et al./Yucatec, and Lehmann/Yucatec. The attempted Tyler/Choctaw PDF was HTML, so it was not copied.
- Drafted an email to Pedro Mateo Pedro asking whether Yucatec Maya allows an NP-internal possessor to control clause-level agreement while remaining inside the possessed NP.
- Build: `make quick` completed and final log check found no unresolved citation/reference/biblatex warnings. Current working tree remains uncommitted: `main.pdf`, `paper/sections/06-typological-transparency.tex`, `paper/sources/source-notes.md`, `references-local.bib`, and untracked `paper/sources/head-marked-transparency/`.

### 2026-06-26 Session Notes — exotic transparency topologies

- Used Roughdraft to review the integration plan at `paper/notes/exotic-transparency-geometries-plan.md`; Brett approved Aleut as a named main-text positive, agreed Chamorro should stay scoped to one table row/one sentence, and asked for explicit $X$--$P$--$R$ mappings with falsification conditions.
- Reworked §6 from "two cross-linguistic cases" to "cross-linguistic cases and topologies." Added Table 2 with outward endpoint, null-source subpart, inward dependent, path-distributed, and feature-relay boundary topologies.
- Added Aleut as a positive null-source/anaphoric subpart case with the Merchant pro-movement qualification; kept the overt intact-NP head-marking caution for Chimane/Nez Perce/Yucatec.
- Added source notes and BibTeX entries for Merchant 2011, Nordlinger & Sadler 2004, Chung 1998/2004, and Dryer 1992; downloaded accessible PDFs for Merchant, Nordlinger/Sadler, Chung 2004, and Dryer into `paper/sources/head-marked-transparency/`.
- Verification: `git diff --check` passed; `make -B` rebuilt `main.pdf` (34 pp.) with no undefined citations/references and no overfull boxes. Remaining warnings are pre-existing duplicate local bib keys and ordinary underfull boxes.

### 2026-06-25 Evening Shutdown — topology integration shipped

- Shipped the §6 topology integration as `7e48eee` (`Integrate exotic transparency topologies`) and then updated the abstract, introduction, and conclusion to match the new topology map.
- The framing update is shipped as `5a5dba7` (`Update framing for transparency topology`) on `main`. It keeps English QNs and TFRs as the worked syntactic core while naming Spanish/Tsez, Aleut, Lardil/Kayardild, Chamorro, and Algonquian/Kutenai as topology pressure tests or boundaries.
- Verification before the framing commit: `git diff --check`, a focused house-style scan, and `make -B` passed; final log scan found no undefined citations/references, no overfull boxes, and no rerun loop. Remaining warnings are the known duplicate local bib keys, package warnings, and underfull boxes.
- Current open carryovers: decide whether to send/revise the Pedro Mateo Pedro Yucatec Maya query; duplicate local bib keys remain for later bibliography cleanup.

### 2026-07-14 Session Notes — Kim's review round implemented

- Triaged Kim's line-numbered July comments (`reviews/kim-2026-07-triage.md`): ~22 adopts, 6 adapts, 0 rejections. Brett ratified the scope compromise (fold §2.6 into §4, compress §1 typology preview, keep §4 intact), Kim drafts the Korean himself, and Kim's book stays 2026-with-asterisk in the bib.
- Implemented across all six sections. Highlights: sentential examples added wherever agreement is the point (Kim's *a lot of* pair, CGEL [53i], CGEL [8]/[10] verbatim, per-sub-group sentences after Table 1); CGEL locators now carry verified page numbers; "fused-head behaviour" corrected to "complement ellipsis" per CGEL's own analysis (pp. 349, 412, 503) with a disambiguating footnote; projectibility-profile intro rebuilt around the (1a) worked example; §3 restructured (no lone subsection); §4 gains "Korean as the deferred cross-linguistic test" (`sec:6-korean`) as Kim's landing pad; QN-vs-quantifier-noun terminology footnote (VE&K 2023 verified, PDF now in `literature/`); Kim's measure/quantity/collection classification cited (flagged `% VERIFY` pending his chapter); loose-property list corrected against Reynolds 2026a.
- Verification: `make -B` clean (35 pp., no undefined citations/references, no overfull boxes); check-style flags only pre-existing held judgment calls.
- Scar-tissue pass over the round's own edits (see DECISIONS), then shipped as `3d502b5` to origin/main.
- Reply to Kim sent 2026-07-14 (`correspondence/2026-07-14-reply-to-kim-july-comments.md`). Awaiting from Kim: Korean draft into §4.5; book chapter pp. 98–103 + pub year (2026 vs 2027); OK on CGEL pair replacing his suggested sentences. He'll use track changes next round.

### 2026-07-23 Session Notes — Kim's second review round implemented

- Triaged and implemented Kim's second round of line-numbered comments (~10 items; full log in DECISIONS 2026-07-23). Kim also sent his book (Routledge, releasing 2026-07-29) as the source for the pseudo-partitive examples.
- Mechanical fixes: umbrella schema de-numbered; ungrammatical examples italicised (`\ungram`+`\mention`); one-sentence paragraph merged; *nurse/nurses* pair enumerated; "both routes" named; "rare" not "zero" for inanimate *bunch*; §3.1 three/two/three counts spelled out.
- Source-grounded additions (verified against primaries via three extraction agents + hand-check of every gloss): §2.1 three-subtype example from Kim's book (COCA, pp. 99–102), `% VERIFY` cleared; §4.1 Haspelmath's own examples (dative, future); §4.5 glossed examples for Spanish (*mayoría*), Aleut (Merchant 2011: 195), Chimane (Ritchie 2016: 622–623, framed as applicative-mediated), Yucatec (Lehmann 2002: 110), matching the existing Tsez interlinear.
- §5: light concretize (Brett's call) — SPC definition sharpened with Slater's wording; cliquishness made concrete via the QN cluster. Structure and the non-instance contribution kept.
- Terminology: "collective" (Kim's book) in §2, "collection" (Van Eynde & Kim 2023) in §1 footnote — the sources differ, each cited to its own term.
- Bib: corrected the central `kim-2026-form-function` entry in place (title "Mapping" not "Mismatches" / "Construction Grammar" not "Construction-Grammar"; place "New York" not the wrong "New York and London"; dropped the redundant `edition`; added DOI; year 2026). Applied via a targeted script scoped to the one entry, since `/push-bib` can't correct existing keys.
- Build clean (`make`, no undefined citations/references, 36 pp.). Not yet shipped; awaiting Kim's Korean draft + track-changes round.
