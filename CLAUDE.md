# CLAUDE.md - Linguistic transparency

## Role

**Editor.** Deep editorial and drafting work welcome. Collaborative paper with Kim — draft Brett's parts as primary lead; flag Korean sections as Kim-pending rather than source-grounding them solo.

## Purpose

Develop a publishable article arguing that *transparency* in linguistics is not a unitary syntactic property but a family of **mediated-accessibility** relations. The article uses one umbrella sense (mediated accessibility) plus four substantive senses (morphosyntactic, constructional, semantic, processing) and two supporting perspectives (typological, metaphysical) to make the case.

The canonical brief is `PROJECT-BRIEF.md`. Read it first. It contains the umbrella schema, the per-sense breakdown with worked tables, the senses to demote, the metaphysical framing (Khalidi), and a candidate thesis statement.

## Working thesis (from PROJECT-BRIEF)

Linguistic transparency is best understood not as a unitary syntactic property but as a family of mediated accessibility relations. A construction, expression, or grammatical configuration is transparent when information that might otherwise be encapsulated remains available for agreement, interpretation, constructional generalisation, processing, or cross-linguistic comparison. The umbrella is not a natural kind, but some transparency profiles are projectible local kinds in Khalidi's sense.

## The umbrella schema (load-bearing)

> X is transparent with respect to property P for relation R when P remains accessible through X for the purposes of R.

This schema does the work the paper is built around. Every case study should be re-expressible in its terms (what is X? what is P? what is R?). Case studies that don't fit cleanly should be flagged early; either the case is the wrong one or the schema needs revision.

## Relationship to sister projects

This paper is the third in a loose family that applies HPC discipline to multi-sense linguistic concepts:

- `papers/What_do_we_mean_by_language/` — preprint LingBuzz 009947, posted 2026-04-28. Pluralist map of senses of *language* with HPC discipline. The closest predecessor methodologically.
- `papers/Field_relative_HPC_categories/` — drafting. Synchronic and diachronic categories as field-relative HPCs (Mixtec / Tu'un Savi as main case, Bininj Kunwok as comparative). Closest predecessor argumentatively, since it also asks "is X a kind?" and answers "no at the umbrella, possibly at the local."
- `papers/HPC book/` — Brett's HPC monograph in progress. Chapter 7 (projectibility) is load-bearing for the metaphysical framing here. The NPI-as-class-not-kind passage in chapter 7 is a structural analogue: NPIs share a surface property but the unity is not mechanism-maintained at the category level. Read that passage before drafting the metaphysical framing here; the present paper makes the parallel move for *transparency*.

The pattern across the three: take a multi-sense linguistic concept, refuse the "is it one kind?" framing, organise the senses by what each field projects over, and identify which local profiles are projectible-as-kinds.

## Source grounding (LAW, with extra teeth)

Standard Source Grounding LAW from `~/.claude/CLAUDE.md` applies. Two additions specific to this paper:

- **The brief's citations come with `?utm_source=chatgpt.com` URL parameters.** That means they were surfaced by an LLM with web search, not verified by hand. The bibliography work for this paper starts with verifying every one of those references against the publisher's authoritative page (Cambridge Core, Springer, Sage, JSTOR, the Zenodo record, etc.). Do not assume any of them is correct as cited. The Bell & Schäfer reference and the Heyer & Kornishova reference are the most likely to need correction; web-search citation tools regularly mis-author or mis-date psycholinguistics papers.
- **Linguistic data must be source-grounded.** Number-transparent quantifier examples, Korean case stacking and scrambling examples, compound semantic-transparency examples, NPI examples — none of these get generated from memory. Read the source. Quote with page citation. The Bert Remijsen Shilluk incident is the precedent.

## House style

Brett's house-style rules load automatically via `.claude/rules/` for `.tex` and `.qmd` files. The paper is LaTeX-native (no markdown intermediate). House-style rules inform prose: contractions preferred, ~60-word paragraphs, no em-dashes (commas, parentheses, or `~--` for spaced en-dashes in LaTeX), direct verbs.

## Style constraints

Avoid:

- "It is important to note that"
- "This paper seeks to"
- "complex and multifaceted"
- "not merely X but Y" as a repeated frame
- inflated claims about "challenging traditional paradigms"
- generic statements about language being social
- "clarity" as a synonym for transparency (the paper's whole point is that transparency is more specific than clarity)

Prefer:

- the umbrella schema's vocabulary (X, P, R, mediator, accessibility) when reframing examples
- concrete contrasts among the senses
- examples that make the mediator visible (the form *a lot of* is the mediator; the number of the complement is what remains accessible)
- "field-relative projectibility" and "local kind" as technical terms
- measured claims about which transparency profiles are projectible

## Terminology

- *Transparency* (italicised on first mention; also italicised whenever used as a name for the concept). Thereafter as ordinary type if used as part of an ordinary noun phrase.
- *Mediated accessibility* — the umbrella concept; technical term.
- *Mediator* — the X in the umbrella schema; technical term.
- *Profile* — a particular pattern of transparency relations; technical term ("transparency profile").
- *Local kind* — used in the Khalidian sense (a kind whose grounding is in a particular causal network rather than a fundamental physical kind).
- *CGEL*, *CxG* — abbreviations introduced on first use; thereafter as ordinary type.
- Italicise mentioned forms (*a lot of*, *plenty of*, *paleness*, *business*, *busy*).
- Use *number transparent*, *number transparency* as CGEL terminology when discussing CGEL's framing.

## Workflow

This paper is **LaTeX-native**. Sections are drafted directly in `paper/sections/*.tex`. `main.tex` `\input`s them in order. Build via `make` (xelatex + biber). No pandoc/markdown intermediate.

Layout:

```
main.tex                          # entry point; preamble + \input each section
paper/sections/
  00-abstract.tex                 # body of \begin{abstract}...\end{abstract}
  01-introduction.tex             # § 1
  02-morphosyntactic-transparency.tex
  ...
  08-conclusion.tex
  A1-appendix-a.tex               # appendix A (after \appendix in main.tex)
  B1-appendix-b.tex
  C1-appendix-c.tex
paper/sources/sources.bib         # project bibliography
paper/sources/source-notes.md     # source curation notes (summaries, claims, warnings)
paper/data/coca-pilot.md          # COCA pilot data backing § 2 footnotes and Appendix A
figures/                          # matplotlib figure scripts and PDF/PNG output
```

Cross-references use the `cleveref` package: `\Cref{sec:N}` / `\Cref{sec:N-M}` auto-prefix with `§`. Each section has an explicit short label (`\label{sec:N}` for H1, `\label{sec:N-M}` for H2). CGEL section references stay as plain `§18.2` etc. inside `\autocite[§18.2]{huddleston-pullum-2002}` locators.

Forms (mentions): `\mention{the lot of it}`. Concepts (terms): `\term{individuation}`, `\term{projectibility profile}`. Brackets always upright (`(\mention{the dog})` not `\mention{(the dog)}`).

Do not pre-populate `sources.bib` with citations that haven't been read. The first task on any new source is to verify it against authoritative pages, then add the entry.

## Non-negotiable argumentative discipline

The paper must not become a generic "transparency means many things" survey. The claim is precise:

1. The umbrella sense is **mediated accessibility** in the schema's exact form. Other senses get included only if they reduce to it.
2. The umbrella is **not** a natural kind. Specific transparency profiles **may** be local kinds in Khalidi's sense if they are stable, projectible, and grounded in recurrent causal networks.
3. CGEL number transparency, CxG constructional compositionality gradients, and morphological-transparency-with-priming-effects are the strongest candidate local kinds.
4. Korean case stacking and scrambling are included to show that mediated accessibility is not a peculiarly English phenomenon. They are **not** the topic.
5. Extraction/island transparency is one historically influential subtype, **not** the centre.
6. The paper is metaphysical-linguistic, **not** philosophy-of-formal-semantics. de re/de dicto and similar referential-transparency cases get a controlled mention, not a substantive section.

If a draft section starts arguing for any weaker claim (e.g., "transparency is a useful descriptive label"), audit against this list.

## Authorship

Co-authored with **Jongbok Kim**. Brett leads (drafting, framing, structure); Kim's input comes later, primarily on the Korean morphosyntactic-transparency cases in §2 (case stacking, scrambling) and on whatever else of the broader argument he wants to engage with. Authorship order to be confirmed (Reynolds & Kim is the default for Brett-led collaborations; the transparent-free-relatives paper goes Kim & Reynolds because Kim led there).

In the current drafting phase, Korean cases in §2 should be stubbed with placeholders or drafted thinly from Kim's existing published work that Brett can read directly, rather than source-grounded by Brett alone. Mark Kim-pending sections clearly so they round-trip cleanly when he reviews.

## Open questions for Brett

- Confirm project folder name `Linguistic_transparency/` or whether you'd prefer something like `Transparency_as_mediated_accessibility/`.
- Confirm public GitHub default applies (collaborative; same default as transparent-free-relatives).
- Confirm authorship order (Reynolds & Kim default).
- Whether the target venue is *Language Sciences* (the natural fit given the predecessor papers' targeting), or whether the metaphysical framing pulls it toward *Theoretical Linguistics*, *Linguistic Typology*, or a philosophy-of-linguistics venue.

## Citations and BibTeX (LAW)

- Citations and BibTeX entries must NEVER be placeholders.
- Citations must NEVER be generated from training data.
- LLMs MUST verify DOIs and bibliographic data against authoritative sources.
- If you cannot verify a citation, say so. Do not guess.
- The brief's citations are LLM-search-surfaced and need verification.
