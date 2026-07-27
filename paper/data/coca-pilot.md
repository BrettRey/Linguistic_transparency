# COCA pilot — partitive vs non-partitive *of*-complements for number-transparent QNs

Run: 2026-05-02. Source: COCA (https://www.english-corpora.org/coca/).
Queries are surface strings; counts are raw COCA frequencies unless marked as filtered. Caveats are noted per cell where relevant. Follow-up KWIC checks are archived in `paper/data/kwic-checks.md`.

## Plural-only forms (*lots, bags, heaps, loads, oodles, stacks, piles*)

### Non-partitive (X of N)

| Query | Count |
| --- | ---: |
| LOTS OF PEOPLE | 3878 |
| LOTS OF MONEY | 1376 |
| LOTS OF TIME | 703 |
| LOADS OF MONEY | 109 |
| PILES OF MONEY | 91 |
| LOADS OF PEOPLE | 90 |
| LOADS OF TIME | 34 |
| HEAPS OF MONEY | 15 |
| HEAPS OF PEOPLE | 7 |
| LOTS OF DAY | 3 |
| HEAPS OF TIME | 3 |
| PILES OF TIME | 1 |
| PILES OF PEOPLE | 1 |
| **Total** | **6311** |

KWIC check: *lots of day* hits are modifier uses (*day-to-day*, *day hikes*, *day trips*). *Heaps of time* and *piles of time* are genuine mass-complement uses; *piles of people* is literal piling rather than the quantificational use. Filtering the modifier/literal cells doesn't change the headline contrast (~6,300 non-partitive vs 13 partitive).

### Partitive (X of the N)

| Query | Count |
| --- | ---: |
| LOTS OF THE TIME | 7 |
| LOTS OF THE PEOPLE | 5 |
| LOADS OF THE DAY | 1 |
| **Total** | **13** |

**Superseded as a measure of availability.** These four hand-picked complements (*day, afternoon, time, people*) understate the frame by a factor of ~36. See the wildcard sweep below.

### Partitive, wildcard sweep (X of the \*) — run 2026-07-26

One query per form, all unique complement types returned (COCA reported TOTAL 622 / UNIQUE 502 for the six forms below run together; the per-form sums reconcile exactly to those figures). *Piles* is from the earlier held-out test (`piles-heldout-test.md`).

| Query | Tokens | Distinct complements |
| --- | ---: | ---: |
| LOTS OF THE \* | 313 | 235 |
| STACKS OF THE \* | 47 | 42 |
| LOADS OF THE \* | 38 | 33 |
| BAGS OF THE \* | 38 | 35 |
| HEAPS OF THE \* | 14 | 14 |
| PILES OF THE \* | 12 | 12 |
| OODLES OF THE \* | 3 | 3 |
| **Total (plural-only subgroup)** | **465** | **374** |

(`PLENTY OF THE *` = 169 / 140 is tabulated under *Plenty* below. The 622/502 COCA totals cover the six plural-only forms plus *plenty*; *piles* was queried separately.)

Leading complements per form:

- **lots**: the same 11, the time 7, the women 5, the other 5, the people 5, the little 4, the things 4, the big 4; then *the drug* 3, *the steroid* 2, *the plasma* 1, *the methylprednisolone* 1 (pharmaceutical batch sense).
- **stacks**: the library 4, the feed 2, the mill 2; singletons in *the plant, the power, the coal, the oil, the factories, the museum, the university, the Inquirer*. Library stacks and smokestacks, not the quantificational sense.
- **loads**: the stuff 3, the same 2, the items 2; literal cargo in *the soil, the biosolids, the shellfish, the yard, the seaward*.
- **bags**: the stuff 3, the chips 2; the rest literal containers (*the greens, the dried, the crop, the toys, the washers*).
- **heaps**: 14 singletons; *the stuff* is quantificational, the rest literal (*the dead, the brush, the dross, the discarded*, and colliery spoil in *the Rhondda, the Shropshire*).
- **oodles**: the cute, the sheeple, the stuff — all three quantificational. *Oodles* has no literal homonym.

**Finding.** The partitive frame is attested for every member of the subgroup, so the earlier zeros were artefacts of the complement set. But the determined frame recruits the literal homonym wherever a member has one, replicating the *piles* result across the subgroup; *oodles*, the only member with no literal homonym, returns quantificational hits exclusively. The clearly quantificational partitives concentrate on complements naming an already-established set: *the same* (lots 11, loads 2), *the stuff* (lots 3, bags 3, loads 3, heaps 1, oodles 1), *the latter*, *the usual*, *the other*, and definite human plurals (*the women, the people, the kids, the guests, the members, the children*). Sense assignment here is read off the complement types, not off inspected concordance lines.

**No partitive share is computable from these numbers.** The numerator (wildcard, all complements) and the denominator (four hand-picked complements) come from different inventories. Either both frames need a wildcard sweep or the comparison stays qualitative.

### Indefinite-NP complement (X of a N)

| Query | Count |
| --- | ---: |
| LOTS OF A DAY | 0 |
| PILES OF A DAY | 0 |
| HEAPS OF A DAY | 0 |
| LOADS OF A DAY | 0 |
| LOTS OF AN AFTERNOON | 0 |
| PILES OF AN AFTERNOON | 0 |
| HEAPS OF AN AFTERNOON | 0 |
| LOADS OF AN AFTERNOON | 0 |
| **Total** | **0** |

No indefinite-determiner complement turned up for any plural-only form tested. That is a null result over eight specific strings, not evidence that the frame is unavailable: the definite-determiner cells in the wildcard sweep above are non-zero for every form, so the subgroup does admit *of [Det NP]*. Testing the indefinite frame properly would need its own wildcard sweep.

## *Plenty*

### Non-partitive

| Query | Count |
| --- | ---: |
| PLENTY OF TIME | 4017 |
| PLENTY OF PEOPLE | 1563 |
| PLENTY OF MONEY | 668 |
| PLENTY OF DAY | 4 |
| **Total** | **6252** |

### Partitive

| Query | Count |
| --- | ---: |
| PLENTY OF THE TIME | 1 |
| PLENTY OF THE PEOPLE | 1 |
| **Total (two hand-picked complements)** | **2** |
| PLENTY OF THE \* (wildcard, 2026-07-26) | 169 |

The wildcard returns 169 tokens across 140 distinct complements, led by *the latter* 7, *the same* 6, *the usual* 4, *the things* 4, *the tools* 3, *the real* 3, *the old* 3, *the most* 2, *the good* 2, *the women* 2, *the world* 2. Both hand-picked strings sit at 1, confirming that the reported near-absence of partitive *plenty* was an artefact of testing two complements. *Plenty* has no literal homonym, so the sense confound that affects *stacks, heaps, bags, loads*, and *piles* does not arise here.

No ratio is given, for the reason stated in the plural-only section: the two frames were sampled over different complement inventories.

## *Rest, remainder*

**Classification corrected 2026-07-26.** These are not quantity nouns, so they have **no pseudo-partitive use at all**, and the two frames below are not a partitive/pseudo-partitive contrast. Van Eynde & Kim (2023: 271) define the pseudo-partitive as [N1 *of* N2] where "N1 denotes a quantity or amount of whatever it is that N2 denotes", and treat the bare N2 as the *characteristic* property distinguishing it from a genuine partitive, "in which N2 is introduced by a definite determiner". *Rest* and *remainder* denote the complement subset of a presupposed whole, not a quantity of it: *the remainder of time* is what is left of time, not an amount of time. So the semantic criterion (which defines the construction) and the syntactic one (which diagnoses it) come apart here, and the semantic one governs. Both frames below are partitive in the relevant sense; they differ only in whether the whole carries a determiner. Earlier versions of this file and of Appendix A.2 mislabelled the bare-complement rows as pseudo-partitive.

### Bare complement (the X of N)

| Query | Count |
| --- | ---: |
| THE REST OF TIME | 75 |
| THE REST OF PEOPLE | 12 |
| THE REST OF DAY | 7 |
| THE REMAINDER OF TIME | 3 |
| THE REMAINDER OF DAY | 2 |
| THE REST OF MONEY | 1 |
| **Total (four hand-picked complements)** | **100** |

### Bare complement, wildcard sweep — run 2026-07-26

`the rest of [nn*]` and `the remainder of [nn*]`, COCA reporting TOTAL 2,946 / UNIQUE 792 for the two run together. Per-form split (reconciles exactly):

| Query | Tokens | Distinct bare complements |
| --- | ---: | ---: |
| THE REST OF [nn\*] | 2820 | 696 |
| THE REMAINDER OF [nn\*] | 126 | 96 |
| **Total** | **2946** | **792** |

Leading complements, *rest*: society 442, humanity 248, US 187, life 150, nature 78, mankind 77, time 75, eternity 73, world 63, creation 42, Americans 41, government 31, baseball 26, civilization 26, Congress 21, class 15, science 15, humankind 14.
Leading complements, *remainder*: life 5, class 4, then *Mr, page, part, president, season, section, time* at 3 each.

**This overturns the starred examples, though not the `×` itself.** The `×` in Table 1's pseudo-partitive column was substantively right, since the construction isn't available to these nouns; what was wrong was starring *the rest of time* as ungrammatical to justify it. The four hand-picked strings captured 100 of 2,946 attestations, about 3%. The bare-complement frame is not rejected: it is common and productive across ~790 distinct complements. What the leading complements share is that none needs a determiner to denote uniquely — non-count generics (*society, humanity, life, nature, time, eternity, creation*), kind-denoting bare plurals (*Americans*), and institution nouns definite without an article (*Congress, government, class, school*). So *rest* and *remainder* do not require an overtly determined complement; they require one whose denotation is already uniquely identifiable. What they resist is a bare complement that would have to introduce a novel indefinite whole. The condition is semantic, on the complement's denotation, not syntactic, on the presence of a determiner.

Caveat on the wildcard: `[nn*]` matches a string position, so some hits are the first word of a longer nominal (*the rest of day one*, *the rest of tuition/books/housing*), and *the rest of US* is mostly the country rather than the pronoun. The top of the list (*society, humanity, life, nature, mankind*) is unambiguous and carries the finding on its own.

KWIC check on the four hand-picked cells: the raw non-partitive total is conservative. *The rest of time* is mostly fixed or duration-level temporal use (*for the rest of time*, *spend the rest of time*), not the partitive-count contrast targeted here. *The rest of people* contains possessives and non-standard "other people" uses. *The rest of day* is temporal ellipsis or *day* as a modifier. The *remainder* hits are technical or duration expressions.

### Determined complement (the X of the N) — genuine partitive on both criteria

| Query | Count |
| --- | ---: |
| THE REST OF THE DAY | 1932 |
| THE REST OF THE TIME | 830 |
| THE REST OF THE PEOPLE | 272 |
| THE REST OF THE MONEY | 222 |
| THE REMAINDER OF THE DAY | 75 |
| THE REMAINDER OF THE TIME | 21 |
| THE REMAINDER OF THE MONEY | 13 |
| **Total** | **3365** |

### Indefinite-NP complement (boundary)

| Query | Count |
| --- | ---: |
| THE REMAINDER OF A DAY | 1 |
| **Total** | **1** |

Determined-complement share **on matched complements only**: 3365 / (3365 + 100 + 1) ≈ 97.1% (raw). Numerator and denominator draw on the same four complements (*day, time, people, money*), so this one is a genuine matched comparison. But note what it compares: **not** partitive vs pseudo-partitive (this subgroup has no pseudo-partitive use) but whether the whole carries a determiner, within one construction. For those four the determiner is strongly preferred. It says nothing about the ~790 bare complements in the wildcard sweep above.

## Override direction

Subject NP + finite verb agreement, by complement number/count. Tests the "near-obligatory in central cases" claim.

| Subject | Predicted | Plural agr. | Singular agr. | % predicted |
| --- | --- | ---: | ---: | ---: |
| *a lot of people* | plural | 4,195 (ARE 3,406; WERE 789) | 85 (IS 72; WAS 13) | 98.0% |
| *a lot of money* | singular | 1 (ARE 1, filtered) | 90 (IS 61; WAS 29) | 98.9% |
| *a number of people* | plural | 100 (ARE 52; WERE 48) | 0 (4 false positives) | 100% |
| *lots of people* | plural | 348 (ARE 288; WERE 60) | 0 (6 false positives/non-standard) | 100% |
| *lots of money* | singular | 0 (1 false positive) | 24 (IS 19; WAS 5) | 100% |
| *plenty of people* | plural | 79 (ARE 65; WERE 14) | 0 | 100% |
| *plenty of money* | singular | 0 | 6 (IS 4; WAS 2) | 100% |
| *the rest of the people* | plural | 19 (ARE 15; WERE 4) | 0 | 100% |
| *the rest of the money* | singular | 0 | 19 (IS 10; WAS 9) | 100% |

Override is in the predicted direction at 98–100% across all tested QN+complement combinations after filtering. *A lot of money* required the most filtering: of 13 raw plural-agreement hits, 10 were parse-shifted (the surface string *a lot of money are* appearing inside relative clauses modifying a plural-noun head, e.g., *people who earn a lot of money are successful*; *movies that make a lot of money are the biggest help*; *times when we... make a lot of money are gone*), 1 was the irrealis *were* (*if a lot of money were at stake*; not plural agreement, see CGEL §3.5.1), and 1 *'s* hit was singular *has* (matches prediction); only 1 hit was a genuine plural override (*a lot of money are being raised*). Filtered count: 1 plural / 90 singular = 98.9% singular.

The other checked counter-direction cells are artefacts. *A number of people is/was* is headed by *condition*, *suggestion*, *ability*, or *counsel*, not by *number*. *Lots of people is/was* is headed by expressions such as *murder*, *hauling*, or *disappearance*, with one non-standard existential hit. *Lots of money are* occurs inside a PP modifying plural *men*. The large *a lot of people is/was* cell remains unfiltered, so the 98.0% row is conservative.

## *Bunch*: animate vs inanimate aggregates

Tests CGEL's claim that *bunch* tilts collective for inanimate aggregates and transparent for groups of people. Queries via the wrapper at `tools/english-corpora/bin/ecorg.mjs`; follow-up KWIC checks were done manually.

| Subject | Total tokens | *was* | *were* |
| --- | ---: | ---: | ---: |
| **Animate aggregates** | | | |
| *a bunch of people* | 1,421 | 0 | 28 |
| *a bunch of kids* | 448 | 0 | 12 |
| *a bunch of hooligans* | 12 | 0 | 0 |
| **Inanimate aggregates** | | | |
| *a bunch of flowers* | 68 | 0 | 0 |
| *a bunch of cars* | – | 0 | 1 |
| *a bunch of papers* | – | 0 | 0 |
| *a bunch of leaves* | – | 0 | 0 |
| *a bunch of things* | – | 0 | 1 |

Animates: 40 plural / 0 singular = 100% plural. KWIC checks found no parse-shift confound in these animate-plural hits. The CGEL "transparent for groups of people" claim is supported.

Inanimates: 2 plural / 0 singular. The CGEL "tilts collective for inanimate aggregates" claim is not supported — there are no singular-agreement hits with inanimate complements. Inanimate-bunch is mostly absent from subject position (typical use is as object: *she gave him a bunch of flowers*); the two inanimate-bunch hits in subject position both took plural rather than the CGEL-predicted singular. *A bunch of flowers was presented to the teacher* (the CGEL example) returns 0 hits in COCA.

## Negative control: referential `the number of` vs quantificational `a number of` (June 2026)

COCA list queries, finite-verb adjacency (is / are):

- the number of people: is 3, are 1
- the number of cases: is 20, are 1
- the number of women: is 0, are 1
- the number of students: is 0, are 0
- a number of people: is 0, are 52
- a number of cases: is 0, are 3
- a number of women: are 5
- a number of students: are 0

`the number of X` is head-driven (singular); `a number of X` shows categorical plural override. Counts small (bare subject-verb adjacency is rare); the clean, non-zero cells are people and cases. The contrast sits on one lexeme (`number`), so the override is construction-specific, not lexical or a general N-of-N attraction effect. The rare plural with `the number of` is at attraction level (1 token each).
