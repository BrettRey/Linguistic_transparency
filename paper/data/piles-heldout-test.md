# Held-out projection test: quantificational *piles*
<!-- SUMMARY: Pre-registered candidate-member test for the QN profile; determiner-frame prediction confirmed and sense-discriminating, agreement prediction untestable for subject-position rarity · status: P4/P5/control still to run · updated: 2026-07-26 -->

The QN profile's weakness is that projection has only been shown over known members, which is close to lexical lookup. This is the candidate-member test the paper has specified but not run. *Piles* is the right subject: it is **not** on *CGEL*'s [57] core list, and it entered the appendix totals only because it appeared to pattern with the plural-only subgroup.

**Predictions are stated below before any COCA query is run.** The Google Books pre-test in §3 was run first and is reported honestly, including where it disconfirms.

## 1. Input evidence, using no target behaviour

Quantificational *piles* is identified on two criteria only, neither of which is among the predicted targets:

- **Quantity meaning.** *Piles of* can mean 'a large amount of' rather than 'physical heaps of'.
- **Frequent *of*-complement distribution.** COCA has PILES OF MONEY 91, and the KWIC check confirms PILES OF TIME as a genuine pseudo-partitive non-count use (`kwic-checks.md`, l. 439).

Nothing about determiners, agreement, partitives, ellipsis, or modification is used as input. Those are the withheld targets.

## 2. Predictions, from the plural-only subgroup profile

| # | Prediction | Confirmed if | Disconfirmed if |
|---|---|---|---|
| P1 | **Agreement override, singular direction.** With a non-count complement, agreement is singular despite the plural head. This is the discriminating cell. | Singular clearly dominates with non-count complements | Plural dominates, or the split is near even |
| P2 | **Agreement, count complement.** With a count-plural complement, agreement is plural. | Plural dominates | Singular competitive |
| P3 | **Determiner frame.** Bare *piles of N* dominant; no singular determiner. | `a piles of` ≈ 0 | `a piles of` attested in edited prose |
| P4 | **Partitive strongly dispreferred**, as for the rest of the subgroup (≈0.2%). | `piles of the N` is a small fraction of `piles of N` | Comparable rates |
| P5 | **Premodification is available**, as for other plural-only forms (*huge piles of money*). | Attested | Absent |

**P2 does not discriminate.** Literal *piles* with a count complement also takes plural agreement, since the piles themselves are then the subject. Only P1 separates the quantificational reading from the literal one, so P1 carries the test.

**Negative control.** A container noun that is *not* a quantifier, with the same non-count complement: *sacks/boxes of money*. Prediction: head-driven plural agreement only, with no singular override available. If the control behaves like *piles*, the singular pattern isn't diagnostic of class membership.

## 3. Google Books pre-test (run 2026-07-26, mean relative frequency 1990–2019, `en-2019`)

Not a substitute for COCA: different register and period mix, no KWIC filtering, exact-string counts only, and Google Books carries OCR noise. Reported because it bears on P1.

| String | Mean rel. freq. |
|---|---|
| piles of money **is** | 1.01e-10 |
| piles of money **are** | 1.65e-10 |
| piles of money **was** | 0.0 |
| piles of money **were** | 1.87e-10 |
| piles of the money | 0.0 |
| a piles of | 1.76e-10 |
| piles of books **were** / **was** | 4.96e-10 / 0.0 |
| piles of papers **were** / **was** | 3.90e-10 / 3.99e-11 |

**P1 is not confirmed here.** With non-count *money*, singular takes about 22% of finite-*be* tokens (1.01 against 3.52), so plural dominates roughly 3.5:1, where the profile predicts the reverse. The direction of the contrast does survive: singular's share is ~22% with non-count *money* against 0–9% with count *books*/*papers*.

**Reinterpreted after the COCA run in §6, this reading doesn't hold up either way.** The COCA determiner data shows that literal *piles* is productive across 174 complements while the quantificational use concentrates on a handful, so most Google Books tokens of *piles of money are* are plausibly literal (stacks of banknotes), which would give plural agreement without bearing on the quantificational use at all. Exact-string frequency can't separate the senses, and that is the limitation, not the profile.

P4 is consistent (`piles of the money` below threshold). P3 is contradicted by a non-zero `a piles of`, which is almost certainly OCR or scanning noise, and is a reason to distrust small Google Books cells rather than to conclude anything about English.

**Read `0.0` as "below the corpus threshold", not as "unattested".** That is the mistake Appendix A.2 previously made.

## 4. COCA queries to run by hand

The `ecorg.mjs` wrapper is Turnstile-blocked (portfolio `CLAUDE.md`, 2026-07-12), so these need the normal browser interface. Paste as-is; `[be]` catches all finite forms of *be* in one query.

**P1, the discriminating cell (non-count complements):**

```
piles of money [be]
piles of cash [be]
piles of paperwork [be]
piles of work [be]
piles of debt [be]
piles of snow [be]
```

For each, record the singular/plural split. **KWIC every hit**: the parse-shift confound documented in Appendix A.1 inflates counter-direction cells, and with counts this small it will dominate if unchecked.

**P2, count complements:**

```
piles of books [be]
piles of papers [be]
piles of bodies [be]
```

**P3, determiner frame:**

```
a piles of
some piles of
the piles of *
piles of *
```

**P4, partitive:**

```
piles of the *
piles of the money
piles of the cash
```

**P5, premodification:**

```
* piles of money
huge piles of money
```

**Negative control:**

```
sacks of money [be]
boxes of money [be]
crates of money [be]
```

**COHA, for the diachronic prediction** that members enter the class by grammaticalization rather than arbitrary addition:

```
piles of money [be]          (by decade)
piles of *                   (by decade, to see whether abstract/non-count complements rise)
```

## 5. How to read the outcome

- **P1 confirmed in COCA**: the paper has a genuine held-out projection, and *piles* is a core member discovered from input criteria alone. The QN profile's claim to support inductive extension is then demonstrated rather than specified.
- **P1 disconfirmed, contrast direction intact** (what Google Books suggests): *piles* is a boundary member. That is still a real result, and arguably a better one, because it shows the profile makes graded predictions that can be wrong. The paper would report *piles* alongside *majority*/*minority* as a boundary case and keep the claim at "specifies a falsifiable basis for inductive extension".
- **No contrast at all, or the control behaves the same**: the input criteria don't pick out class membership, and the profile claim should be weakened further.

Either of the first two outcomes is publishable. The third would matter a great deal, which is the point of running it.

## 6. COCA results (run by hand, 2026-07-26)

### P1/P2, agreement: the test cannot be run on *piles*

The combined `[be]` queries returned **five hits in total** across all nine complements:

| String | Freq |
|---|---|
| PILES OF MONEY **IS** | 1 |
| PILES OF SNOW **ARE** | 1 |
| PILES OF PAPERS **WERE** | 1 |
| PILES OF BOOKS **ARE** | 1 |
| PILES OF BODIES **WERE** | 1 |

- **Discriminating cell (non-count complement): n = 2, split 1–1.** *Piles of money is* and *piles of snow are*.
- Count complements: 3/3 plural, as predicted, but this cell never discriminated.

**P1 is untestable, not disconfirmed.** Two tokens support no verdict either way, and the Google Books ~22%/78% split in §3 was on a similarly thin base with no way to separate literal from quantificational uses. Reading either result as evidence against the profile would repeat exactly the error Appendix A.2 used to make.

**Why the data isn't there, and why that matters.** COCA has 91 tokens of *piles of money*, of which **one** is followed by a finite form of *be*. Quantificational *piles* almost never appears as a subject; its typical use is as an object (*he made piles of money*). This is structurally the same problem as inanimate *bunch* (§2.2), and it generalises: **the agreement-override prediction is only corpus-testable for class members that occur in subject position**, which is a real limitation on the profile's testability rather than a fact about *piles*. Candidate-member discovery may need acceptability judgments rather than corpus frequency.

### P3, determiner frame: confirmed, and it discriminates the two senses

- `a piles of` = **0**. Confirmed: no singular determiner, as the plural-only subgroup predicts.
- `some piles of` = **8**. Attested. *Some* is not a singular determiner, so this doesn't violate the prediction, but it does distinguish *piles* from *lot*, where §2.1 reports \*_some lot of it_ as blocked. Worth checking whether *some* is generally available across the plural-only subgroup.
- `the piles of [n*]` = **340 tokens, 174 unique complements**.

That last figure is the most informative result in the whole test, and it wasn't among the predictions. The determined frame is robustly available and highly productive, but its complements are overwhelmingly **concrete**: paper 17, books 14, papers 13, debris 12, junk 9, boxes 8, clothes 8, cash 7, garbage 7, rubble 7, sand 6, laundry 5, bodies 5, trash 5, corpses 4, stones 4, snow 4, leaves 4. Eighteen of the top nineteen denote physical objects or substances that can literally be heaped.

So *the piles of N* selects the **literal** reading, where bare *piles of money* leans quantificational. The determiner frame separates the two senses of *piles*, and the productivity is lopsided: the literal use spreads across 174 complements, while the quantificational use concentrates on a handful (*money*, *cash*, *time*).

**That is a genuine held-out result.** The input criteria (quantity meaning plus frequent *of*-complement distribution) picked out a use that a withheld behaviour does distinguish. It just isn't the withheld behaviour the profile leads with.

### Still to run

- **P4, partitive:** `piles of the *`, `piles of the money`, `piles of the cash`. Note this is *not* the same query as `the piles of [n*]` above: P4 puts the determiner on the complement, testing partitivity, where the query already run puts it on *piles*.
- **P5, premodification:** `* piles of money`, `huge piles of money`.
- **Negative control:** `sacks of money [be]`, `boxes of money [be]`, `crates of money [be]`. Given the P1 sparsity, expect these to be empty too, which would confirm that the emptiness is about subject position rather than about *piles*.

### Verdict so far

*Piles* is a **partially confirmed candidate member**. The determiner-frame prediction holds and does real work; the agreement prediction is untestable on this member for reasons that generalise to any member rare in subject position. The paper's claim should stay at "specifies a falsifiable basis for inductive extension", with the added and more interesting point that the basis is falsifiable only where the corpus supplies subject-position tokens.
