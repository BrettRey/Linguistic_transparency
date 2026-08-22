# Numbers and tables audit: umbrella paper

Date: 2026-08-22
Verdict: pass

## QN evidence

The agreement table matches `paper/data/override-audit.tsv` cell for cell. The two non-perfect rates recompute as 4,195/4,280 = 98.0% and 90/91 = 98.9%; the remaining tested cells are 100% in the predicted direction. The manuscript preserves the important asymmetry warning for the large `a lot of people` counter-direction cell.

The Appendix A aggregates also recompute:

- determined plural-only wildcard: 465 tokens and 374 distinct complements;
- six-form combined run plus `plenty`: 622 tokens and 502 distinct complements;
- `rest`/`remainder`: 100 bare, 3,365 determined, one indefinite; determined share 97.1% on the matched complement inventory;
- `piles`: 54/91 tokens in object or PP-complement position, hence at least 59%; the COCA+COHA agreement cell is three tokens, one singular and two plural.

Ox Alpha independently returned PASS on these arithmetic claims after the input was stated in predicted/counter-predicted order.

## TFR evidence repeated in the umbrella

The companion archive and arithmetic replay confirm every number repeated in §2.5: 185/485 genuine AdjP rows, 144 externally predicative, 733 evidential adjective/adverb rows (296 + 379 + 58), three ambiguous candidates, 46 PP rows, and the 29.7% versus at-most-0.4% comparison. The exact rate ratio is 72.54, supporting “roughly seventy-fold”.

## Data mapping

One reproducibility sentence falsely said that the supplementary README records the manuscript commit. It does not record a hash. The sentence now says what the archive actually does: map counts to queries, with the repository version serving as the current reproducibility anchor.
