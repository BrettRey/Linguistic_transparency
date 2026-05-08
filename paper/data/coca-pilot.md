# COCA pilot — partitive vs non-partitive *of*-complements for number-transparent QNs

Run: 2026-05-02. Source: COCA (https://www.english-corpora.org/coca/).
Queries are surface strings; counts are raw COCA frequencies, not filtered for head vs modifier use, idiom contamination, or sense disambiguation. Caveats are noted per cell where relevant.

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

Coding caveat: the small-count *X of day* hits almost certainly include modifier uses (e.g. *lots of day-care*) rather than QN non-partitive heads. Filtering would reduce the non-partitive total slightly but doesn't change the headline contrast (~6,300 non-partitive vs 13 partitive).

### Partitive (X of the N)

| Query | Count |
| --- | ---: |
| LOTS OF THE TIME | 7 |
| LOTS OF THE PEOPLE | 5 |
| LOADS OF THE DAY | 1 |
| **Total** | **13** |

Partitive ratio: 13 / (6311 + 13) ≈ 0.2%. *Lots* is the only form with non-zero partitive uses; *piles, heaps* return 0 partitive hits with any tested complement.

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

Plural-only forms reject *of [Det NP]* whether the determiner is definite (*the*) or indefinite (*a/an*); their *of*-complements are bare/non-determined.

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
| **Total** | **2** |

Partitive ratio: 2 / (6252 + 2) ≈ 0.03%.

## *Rest, remainder*

### Non-partitive (the X of N)

| Query | Count |
| --- | ---: |
| THE REST OF TIME | 75 |
| THE REST OF PEOPLE | 12 |
| THE REST OF DAY | 7 |
| THE REMAINDER OF TIME | 3 |
| THE REMAINDER OF DAY | 2 |
| THE REST OF MONEY | 1 |
| **Total** | **100** |

Coding caveat: *the rest of time* (75 hits) is heavily contaminated by idiomatic *for the rest of time* (≈ "forever"), *till the rest of time*, and similar. Spot-checking head uses only would lower the figure substantially. *The rest of people* (12) may include generic uses (*the rest of people don't care*) that aren't classic non-partitive QN constructions.

### Partitive (the X of the N)

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

Partitive (definite NP) ratio: 3365 / (3365 + 100 + 1) ≈ 97.1% (raw). Filtering the *for the rest of time* idiom from the non-partitive count would push this even higher.

## Override direction

Subject NP + finite verb agreement, by complement number/count. Tests the "near-obligatory in central cases" claim.

| Subject | Predicted | Plural agr. | Singular agr. | % predicted |
| --- | --- | ---: | ---: | ---: |
| *a lot of people* | plural | 4,195 (ARE 3,406; WERE 789) | 85 (IS 72; WAS 13) | 98.0% |
| *a lot of money* | singular | 1 (ARE 1, filtered) | 90 (IS 61; WAS 29) | 98.9% |
| *a number of people* | plural | 100 (ARE 52; WERE 48) | 4 (IS 2; WAS 2) | 96.2% |
| *lots of people* | plural | 348 (ARE 288; WERE 60) | 6 (IS 5; WAS 1) | 98.3% |
| *lots of money* | singular | 1 (ARE 1) | 24 (IS 19; WAS 5) | 96.0% |
| *plenty of people* | plural | 79 (ARE 65; WERE 14) | 0 | 100% |
| *plenty of money* | singular | 0 | 6 (IS 4; WAS 2) | 100% |
| *the rest of the people* | plural | 19 (ARE 15; WERE 4) | 0 | 100% |
| *the rest of the money* | singular | 0 | 19 (IS 10; WAS 9) | 100% |

Override is in the predicted direction at 96–100% across all tested QN+complement combinations after filtering. *A lot of money* required the most filtering: of 13 raw plural-agreement hits, 10 were parse-shifted (the surface string *a lot of money are* appearing inside relative clauses modifying a plural-noun head, e.g., *people who earn a lot of money are successful*; *movies that make a lot of money are the biggest help*; *times when we... make a lot of money are gone*), 1 was the irrealis *were* (*if a lot of money were at stake*; not plural agreement, see CGEL §3.5.1), and 1 *'s* hit was singular *has* (matches prediction); only 1 hit was a genuine plural override (*a lot of money are being raised*). Filtered count: 1 plural / 90 singular = 98.9% singular. Other small-count counter-direction cells in the table may include similar artefacts that haven't been spot-checked here.

## *Bunch*: animate vs inanimate aggregates

Tests CGEL's claim that *bunch* tilts collective for inanimate aggregates and transparent for groups of people. Queries via the wrapper at `tools/english-corpora/bin/ecorg.mjs`; KWIC mode is broken in the wrapper (cannot spot-check contexts for parse-shifts).

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

Animates: 40 plural / 0 singular = 100% plural. The CGEL "transparent for groups of people" claim is supported.

Inanimates: 2 plural / 0 singular. The CGEL "tilts collective for inanimate aggregates" claim is not supported — there are no singular-agreement hits with inanimate complements. Inanimate-bunch is mostly absent from subject position (typical use is as object: *she gave him a bunch of flowers*); the two inanimate-bunch hits in subject position both took plural rather than the CGEL-predicted singular. *A bunch of flowers was presented to the teacher* (the CGEL example) returns 0 hits in COCA.
