# Held-out projection test: quantificational *piles*
<!-- SUMMARY: Pre-registered candidate-member test for the QN profile; predictions fixed before COCA queries, Google Books pre-test already partly disconfirming · status: awaiting hand-run COCA/COHA queries · updated: 2026-07-26 -->

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

**P1 is not confirmed and looks disconfirmed.** With non-count *money*, singular takes about 22% of finite-*be* tokens (1.01 against 3.52), so plural dominates roughly 3.5:1. The profile predicts the reverse.

**But the direction of the contrast survives.** Singular's share is ~22% with non-count *money* against 0–9% with count *books*/*papers*. So the complement's count status does shift agreement the predicted way; it simply doesn't produce the near-categorical override that core members show. On this evidence *piles* looks like a **weak or boundary member**, not a core one.

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
