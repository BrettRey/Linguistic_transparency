# Linguistic transparency as mediated accessibility

Working repository for a paper arguing that *transparency* in linguistics is a family of mediated-accessibility relations, not a unitary syntactic property. Some local transparency profiles may be projectible kinds in Khalidi's sense; the umbrella is not.

## Read first

- `PROJECT-BRIEF.md` — Brett's full project package (canonical brief)
- `CLAUDE.md` — role, source-grounding, sister-project relationships, style, terminology, workflow, argumentative discipline
- `STATUS.md` — current state, what exists, what doesn't, next action
- `DECISIONS.md` — decisions log

## Layout

```
Linguistic_transparency/
├── PROJECT-BRIEF.md     # canonical brief
├── CLAUDE.md            # agent guidance
├── STATUS.md            # state and next action
├── DECISIONS.md         # decisions log
├── README.md            # this file
└── paper/
    ├── sources/
    │   ├── sources.bib       # project bibliography (empty until source-grounded)
    │   └── source-notes.md   # source curation: summaries, claims, quotations, warnings
    ├── draft/
    │   ├── 00-abstract.md
    │   ├── 01-introduction.md
    │   ├── 02-morphosyntactic-transparency.md
    │   ├── 03-constructional-transparency.md
    │   ├── 04-semantic-transparency.md
    │   ├── 05-processing-transparency.md
    │   ├── 06-typological-transparency.md
    │   ├── 07-metaphysical-framing.md
    │   └── 08-conclusion.md
    ├── notes/
    │   ├── argument-map.md
    │   ├── claims-to-verify.md
    │   ├── terminology.md
    │   └── possible-venues.md
    └── output/
        ├── paper-draft.md     # combined draft (not yet built)
        └── paper-draft.tex    # converted LaTeX (not yet built)
```

## Workflow

Markdown-first. Sections are drafted in `paper/draft/`, combined into `paper/output/paper-draft.md`, then converted to LaTeX in `paper/output/paper-draft.tex`. LaTeX scaffolding will be added at the conversion stage.

## Sister projects

- `papers/What_do_we_mean_by_language/` (preprint, LingBuzz 009947) — closest predecessor methodologically.
- `papers/Field_relative_HPC_categories/` (drafting) — closest predecessor argumentatively.
- `papers/HPC book/` chapter 7 — load-bearing for the metaphysical framing; the NPI-as-class-not-kind passage is the structural analogue.

## Umbrella schema

> X is transparent with respect to property P for relation R when P remains accessible through X for the purposes of R.

Every case study in the paper should be re-expressible in this form. If it can't, it's the wrong case or the schema needs revision.
