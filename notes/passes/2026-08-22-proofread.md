# Proofread report: *Access transparency in grammar*

Date: 2026-08-22
Scope: `main.tex` and every included section/appendix
Mode: read-only audit; no manuscript source was edited

## Verdict

Resolved 2026-08-22. The visible placeholder and all consistency, grounding, cross-reference, bibliography, and terminology blockers below were corrected. The manuscript is ready for co-author review; U8 remains optional density polish rather than a circulation blocker.

## Final publication-gate rerun

A fresh read after the coherence and scar-tissue revisions found no remaining grammar, spelling, cross-reference, placeholder, or source-grounding defect. It did expose an omission in this report: the Keizer terms cited at p. 109 had not been included in the quotation audit. Page 109 was retrieved and checked; it gives the five pseudo-partitive subtypes and uses *collection-noun constructions*, exactly as the footnote reports. The abstract now also glosses QNs, projectibility, and stabilizers at first use. The final 33-page PDF has no overfull boxes, unresolved citations, or unresolved references.

## Resolution update

- U1: restored the intended words and recast the objection/reply passage directly.
- U2: corrected the cross-reference to §2.4.
- U3: synchronized the residual TFR work with the companion paper's current evidence.
- U4: added a distinct local entry for the 22 August working paper and used it in the manuscript and data-availability statement.
- U5: replaced the like-for-like claim with a descriptive comparison of archived candidate rows and stated the query-design limitation.
- U6: standardized the send set on `AdjP`.
- U7: defined *mediated accessibility* as the broad pattern and *access transparency* as the narrower grammatical relation.
- Final XeLaTeX build: no unresolved citations/references or overfull boxes; `git diff --check` clean.

## Findings

### U1. Empty quotation in the typology objection

- **Location:** `paper/sections/06-typological-transparency.tex:78`
- **Category:** quality / LaTeX
- **Severity:** critical
- **Current text:** `The reply isn't that the schema is \enquote{               }:`
- **Suggested fix:** Restore the missing words. The following sentence makes `\enquote{just a question}` the contextually supported reading.

### U2. Wrong cross-reference for the *piles* prospective test

- **Location:** `paper/sections/A1-appendix-a.tex:21`
- **Category:** LaTeX / grounding
- **Severity:** major
- **Current text:** `it generalizes the \mention{piles} result of §\ref{sec:2-5}`
- **Suggested fix:** Point to §2.4, where the candidate-member test is reported, rather than §2.5, the TFR subsection: `§\ref{sec:2-4}`.

### U3. The account of the unfinished TFR work is now out of date

- **Locations:** `paper/sections/02-morphosyntactic-transparency.tex:289`; `paper/sections/08-conclusion.tex:9`
- **Category:** quality / grounding
- **Severity:** major
- **Current text:** `The category-discriminating environments and judgments remain to be added to the joint paper.` The conclusion similarly says the result remains provisional until `category-discriminating environments, judgments, and rival analyses are handled`.
- **Problem:** The companion paper already reports several naturally occurring category-discriminating environments, and the umbrella itself mentions the coordinated attributive token at line 283. What remains is systematic judgment work in those environments and adjudication of the rival analyses.
- **Suggested fix:** Use wording such as: `The few attested category-discriminating environments now require systematic judgments; rival analyses remain to be adjudicated in the joint paper.` Make the conclusion match.

### U4. The companion-paper citation resolves to the WRAPP presentation

- **Locations:** `main.tex:97`; `references.bib:18823--18828`
- **Category:** grounding / bibliography
- **Severity:** major
- **Current text:** The data-availability statement calls `kim-reynolds-2026-tfr-two-kinds` a `companion working paper`, but the bibliography entry prints *Polyfunctionality of what ...* as a conference presentation dated 8 April 2026.
- **Suggested fix:** Create or repoint the key to the 22 August working paper, *Two Kinds of Transparency: Category Flexibility and the Verb Inventory in Transparent Free Relatives*, and retain the WRAPP presentation under a separate key. If that bibliographic change is intentionally awaiting Kim's approval, avoid calling the cited item a working paper in this draft.

### U5. `Like-for-like` overstates the comparability of the corpus rates

- **Location:** `paper/sections/02-morphosyntactic-transparency.tex:285`
- **Category:** grounding
- **Severity:** major
- **Current text:** `The like-for-like gap is 144/485 ... against at most 3/733 ...`
- **Problem:** The companion paper itself notes that the query forms are not uniform. The 733 denominator is a sum of candidate-row returns from several query designs, not an independently sampled set of unique tokens generated by the same template as the *call* denominator.
- **Suggested fix:** Call this a `row-level contrast in predicative outcomes` rather than a like-for-like rate comparison, retain `candidate rows`, and state that the roughly seventy-fold figure is descriptive rather than an inferential rate estimate.

### U6. AP/AdjP terminology differs across the send set

- **Locations:** `paper/sections/02-morphosyntactic-transparency.tex:279, 283, 285, 291`; companion paper throughout
- **Category:** style / terminology
- **Severity:** minor
- **Current text:** The umbrella uses `AP`; the companion uses `AdjP`.
- **Suggested fix:** Choose one label for both papers, or explicitly note the equivalence once if the difference is intentional.

### U7. `Mediated accessibility` is prominent but only loosely related to the defined term

- **Locations:** `main.tex:7, 11, 73`; `paper/sections/01-introduction.tex:50, 58`
- **Category:** quality / terminology
- **Severity:** minor
- **Current text:** The subtitle and keywords foreground `mediated accessibility`, while the abstract and formal schema define `access transparency`; the former receives only a comparative gloss late in the introduction.
- **Suggested fix:** Either define `mediated accessibility` as the plain-language superordinate/synonym in the abstract or early introduction, or remove it from the subtitle and keywords. This is the only actionable item among the terminology checker's front-matter flags; the other flagged technical terms are defined in the introduction.

### U8. Several core paragraphs are too dense for a co-author review copy

- **Locations:** especially `paper/sections/02-morphosyntactic-transparency.tex:270` (about 220 words), `:291` (about 170), `paper/sections/06-typological-transparency.tex:82` (about 190), and `paper/sections/A1-appendix-a.tex:21` (about 210)
- **Category:** quality
- **Severity:** minor
- **Current text:** Each paragraph carries multiple argumentative or evidential moves.
- **Suggested fix:** Split at the transition from setup to qualification or from result to consequence. This can wait until after the substantive co-author pass if time is tight.

## Checks that passed

- XeLaTeX build completed: 33 pages.
- No undefined citations, undefined references, duplicate labels, or overfull boxes were found.
- Four underfull boxes are cosmetic and do not block circulation.
- The style linter's contraction and `wh-` flags were checked in context; most were intentional contrasts, technical forms, or quoted linguistic data and are not reported as errors.
