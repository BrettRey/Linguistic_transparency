# Access transparency in grammar

Working repository for a paper proposing **access transparency** as a comparative concept for mediated grammatical accessibility. The paper's primary grammatical case is English number-transparent quantificational nouns; transparent free relatives supply a second, conditional illustration. Projectibility is assessed as a secondary, profile-level question.

## Read first

- `STATUS.md` — current state and remaining coauthor decisions
- `DECISIONS.md` — append-only decisions log
- `CLAUDE.md` — source-grounding, style, terminology, and workflow instructions
- `PROJECT-BRIEF.md` — historical canonical brief; the current architecture is recorded in the manuscript and latest decisions

## Build

This is a LaTeX-native paper. Build the current PDF with:

```sh
make
```

The entry point is `main.tex`; section sources are in `paper/sections/`. The generated reviewer-facing PDF is `main.pdf`.

## Current architecture

The applicability protocol requires:

1. an independently diagnosable bearer of the property;
2. a distinct mediator;
3. evidence that the relation tracks the property; and
4. an independently established concealing counterpart in the same constructional family.

Cases receive positive, non-instance, or indeterminate relational verdicts. A positive relation does not automatically supply a projectible profile.

## Supplementary data

The corpus record is in `paper/data/`. Start with `paper/data/README.md`. The override audit is also available as the machine-readable `paper/data/override-audit.tsv`. The current data are exploratory and preserve the known asymmetry between predicted- and counter-direction filtering.

## Sister projects

- `papers/What_do_we_mean_by_language/` — closest predecessor methodologically.
- `papers/Field_relative_HPC_categories/` — closest predecessor argumentatively.
- `papers/HPC book/` chapter 7 — background for the projectibility framing.
- `papers/retarget/transparent-free-relatives/` — separate joint TFR project under development.
