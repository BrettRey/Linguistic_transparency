# Supplementary data map

This directory contains the corpus record used by the number-transparent QN discussion and Appendix A. The manuscript's claims are exploratory attestations, not estimates of grammatical rates.

## Files

- `coca-pilot.md` records the partitive, bare-complement, override, *bunch*, and negative-control queries and their aggregate results.
- `kwic-checks.md` contains the pasted concordance batches and manual checks used to identify parse shifts, modifier contamination, and literal homonyms.
- `override-audit.tsv` gives the raw plural- and singular-agreement counts reproduced in Table~\ref{tab:override-audit}.
- `piles-heldout-test.md` records the candidate-member criteria, predictions, corpus checks, and the final partial-support/feasibility-failure verdict.

## Provenance and limits

The queries were run through the local English-corpora wrapper or the ordinary corpus interface, as specified in the individual files. Dates, query forms, and filtering notes are recorded there. Counter-direction cells received more manual checking than predicted-direction cells because scripted KWIC retrieval failed during the pilot. The counts therefore document attestation and identified false positives; they do not estimate grammatical probabilities.

No independent second-coder audit has been completed. The rare and counter-direction cells were checked by the manuscript author and adjudicated within that audit. Any submission release should preserve this limitation and add second-coder results only after that audit has actually been run.

The repository commit containing the manuscript and this directory is the reproducibility anchor for the current draft. A citable archive and any formal release tag remain submission-package work.
