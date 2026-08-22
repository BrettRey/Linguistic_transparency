# Build-integrity gate: *Access transparency in grammar*

Date: 2026-08-22
Verdict: pass

- `manuscript_fingerprint.py` resolves `main.tex` and all ten included files: 32 sections, 15,284 words, and no unresolved input.
- `references.bib` is the expected symlink to the central bibliography; the local auxiliary bibliography is intentionally regular.
- No hard-coded TeX Live path or unresolved placeholder occurs in manuscript source.
- The full XeLaTeX–Biber–XeLaTeX–XeLaTeX build completes successfully.
- The final PDF is 33 US-letter pages with synchronized title and keyword metadata.
- The log contains no package error, undefined citation/reference, rerun request, or overfull box. Four underfull boxes are cosmetic; rendered inspection shows no visible defect at them.
- `git diff --check` passes.
- All 33 pages were rendered and inspected in contact sheets; title/abstract, dense tables, appendices, data availability, and references were also inspected at page resolution. No clipping, overlap, broken rule, orphaned heading, or bad pagination was found.
