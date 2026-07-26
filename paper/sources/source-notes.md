# Source notes

Curation document for `sources.bib`. For each source, this file records summary, supportable claims, exact quotations, warning notes, and relevance rating. Sources do not enter `sources.bib` until they have been read and an entry here exists.

## Template

```
### [citation key]

**Full bibliographic entry:** [author, year, title, venue, pages, DOI/URL]

**Status:** [unread / partial / read]

**Relevance:** core / useful / background

**Summary (3–6 bullets):**

- ...
- ...

**Claims this source can support:**

- ...

**Quotations (≤25 words each, with page citation):**

- "..." (p. NN)

**Warnings / overinterpretation risks:**

- ...

**Cross-references:** [other sources in this set that bear on the same point]
```

---

## Verification checklist (from PROJECT-BRIEF.md)

The brief surfaces seven citations. **All carried `?utm_source=chatgpt.com` URL parameters**, indicating LLM-search-surfacing rather than hand verification. Each was verified 2026-04-30 against publisher pages and crosschecked against on-disk literature.

### CGEL number transparency

- [x] **The brief mis-attributes the term.** "Number transparent" is canonically from CGEL itself (Huddleston & Pullum 2002), §3.3 of the noun chapter and §18.2 of the agreement chapter. The *Cambridge Dictionary of English Grammar* (Peters 2013, DOI 10.1017/CBO9781139050623) is a separate book; whether Peters reproduces the term was not verified, but the substantive treatment is in CGEL. **Use CGEL; drop Peters.**

### Construction Grammar

- [x] **Goldberg, Construction Grammar overview** — the Princeton page resolves to Goldberg, A. E. (2006), "Construction Grammar," in *Encyclopedia of Cognitive Science*, ed. Nadel, Wiley (DOI 10.1002/0470018860.s00216). 4-page entry. Not on disk; substitutable with Goldberg (2006) *Constructions at Work* ch. 1, which is on disk and makes the same form-meaning-pairings claim more substantively.
- [x] **Goldberg (1995), *Constructions: A Construction Grammar Approach to Argument Structure*** (UChicago Press). Not on disk; the 1995 monograph's argument-structure claims are restated in Goldberg (2006) ch. 1 (which Goldberg herself cross-references: "In an earlier book, *Constructions*, I focused primarily on arguments for adopting a constructionist approach to argument structure"). Skip 1995 unless an argument needs the original formulation.

### Semantic transparency in compounds

- [x] **Bell & Schäfer (2016)**, "Modelling semantic transparency," *Morphology* 26(2): 157–199, DOI 10.1007/s11525-016-9286-3. Open access. Downloaded to `literature/Bell_Schaefer_2016_modelling_semantic_transparency.pdf`.

### Processing transparency

- [x] **Heyer & Kornishova (2018)**, "Semantic transparency affects morphological priming . . . eventually," *Quarterly Journal of Experimental Psychology* 71(5): 1112–1124, DOI 10.1080/17470218.2017.1310915. On disk at `literature/heyerkornishova2018.pdf`. Specific paleness/business example confirmed; longer-SOA finding confirmed.

### Typology

- [x] **Haspelmath (2010)**, "Comparative concepts and descriptive categories in crosslinguistic studies," *Language* 86(3): 663–687, JSTOR 40961695. On disk (three duplicate copies; canonical is `haspelmath2010.md`). The Zenodo record `1303024` is a deposit of this paper.

### Metaphysics of natural kinds

- [x] **Khalidi (2018, online 2015)**, "Natural kinds as nodes in causal networks," *Synthese* 195(4): 1379–1396, DOI 10.1007/s11229-015-0841-y. On disk at `khalidi2015.md`/`.pdf` (the OnlineFirst version). PhilPapers KHANKA-4 corresponds to this paper.

---

## To inherit from sister project

`papers/Field_relative_HPC_categories/paper/sources/sources.bib` has verified HPC-theory entries:

- `boyd1991` — Boyd, "Realism, Anti-Foundationalism and the Enthusiasm for Natural Kinds"
- `boyd1999` — Boyd, "Homeostasis, Species, and Higher Taxa"
- `khalidi2013` — Khalidi, *Natural Categories and Human Kinds*
- `hacking1999` — Hacking, *The Social Construction of What?*
- `reynolds2025hpcbook` — Brett's HPC book

Decision pending (per `DECISIONS.md`): whether to import these as the metaphysical foundation here, or maintain a separate set tuned to the brief's Khalidian framing. The Khalidi 2018 paper read here explicitly loosens Boyd's HPC by dropping mechanism and homeostasis; the choice is non-trivial.

---

## Quine 1956 (added 2026-04-30 for §4.3 controlled mention)

Bibliographic data verified via JSTOR (53(5): 177–187, 1956); full text not read. Citation is used as a *historical pointer* for the de re/de dicto philosophical-semantics tradition, not as a content claim about Quine's argument. If the §4.3 boundary case is later expanded substantively, the paper should be sourced and read first.

## Korean data sources

The brief's §2 table lists Korean case stacking and Korean scrambling as morphosyntactic-transparency cases, but no specific sources. Either Brett source-grounds these against existing literature on Korean syntax, or the project becomes a Reynolds-Kim collaboration and Jongbok contributes the Korean sections. Decision noted in `DECISIONS.md`.

**Update 2026-07-26 (Kim's email).** Kim supplied the §4.5 Korean material: the dative-nominative case-stacking example with subject honorification (now example (20)), plus an external-possession construction he offered to cut. Two grounding points:

1. **Kim's draft cited "Kim 2026" for the dative-experiencer baseline. That citation can't carry it.** `kim-2026-form-function` is *Form and Function Mapping in English Syntax* (Routledge, 2026), and the preprint at `papers/retarget/transparent-free-relatives/form-function-book-2025-routledge-preprint-final-11-12-Trimbox.pdf` has no Korean case-stacking, honorification, `caki`, or external-possession content (checked by grep over the full extracted text; 17 hits for "Korean," all incidental cross-references to Kim 2016b and to super-category argumentation). The pointer was dropped from the draft rather than guessed at, and a `% TODO(kim)` in `06-typological-transparency.tex` asks him for the actual reference and page. Likely candidates on his own shelf: *The Syntactic Structure of Korean* (CUP 2016) or *English and Korean in Contrast* (Wiley 2023). Neither is in `literature/`; neither has been read.
2. **`aranovich-kim-2024-external-possession` verified** against the Benjamins record (jbe-platform, via DOI 10.1075/lic.00047.ara), 2026-07-26: Raúl Aranovich and Jong-Bok Kim, "Contrasts in the Spanish and Korean external possession constructions: A Construction Grammar approach," *Languages in Contrast* 24(2), 271–296, 2024. Exactly as Kim reported it. Abstract only (article paywalled); the full text has **not** been read, so it can't yet support a claim about the Korean analysis beyond what the abstract states: the authors treat external possessors as unselected arguments licensed through conventional implicature, and contrast Korean with Spanish on case marking, grammatical role, distribution, and alienability. That "unselected external argument" analysis is why the external-possession case sits with §4.4's externalized near misses (Deal 2017) rather than with the NP-internal transparency pattern.

## Korean case stacking: published sources located 2026-07-26

Searched to see whether Kim's §4.5 data is already in print, so the section needn't wait on him. It is, and the published analysis complicates our framing. **§4.5 should not be revised until Park and Kim 2022 has been read** (see below).

### yoon-2004-case-stacking (read)

James Hye Suk Yoon, "Non-nominative (major) subjects and case stacking in Korean," ch. 13 of *Non-nominative Subjects*, Typological Studies in Language, 265–314. Amsterdam: John Benjamins, 2004. DOI 10.1075/tsl.61.15yoo (author, title, container, pages, publisher, year verified via Crossref; Crossref returns no editor list, so the editors are **not** yet verified and shouldn't be typed into a bib entry from memory).

**The copy read is the author's manuscript**, saved to `literature/yoon-2004-non-nominative-subjects-case-stacking-korean-ms.pdf` (47 pp., Word-generated, dated July 2003), freely posted at `faculty.las.illinois.edu/jyoon/Papers/yoo.pdf`. Its pagination is its own, not the published 265–314, so cite by section number, not page.

- **Kim's construction is standard and published.** Yoon's (12) gives dative-nominative stacking on experiencers with the same predicate as Kim's (20): `Cheli-hanthey-ka ton-i philyoha-ta` (C-DAT-NOM money-NOM necessary-DECL) 'It is Cheli who needs money', alongside `Cheli-eykey-ka ton-i manh-ta` 'It is Cheli who has a lot of money'. Yoon's clefted translations match Kim's, which is presumably where the cleft in his gloss comes from.
- **Stacking is marginal and dialectally variable.** Yoon, §3.1: "Case Stacking is somewhat marginal to begin with," and "speakers appear to have genuine differences in their idiolects/dialects concerning the acceptability of crucial sentences." His notation (§4.2): `*` = "ungrammatical in all dialects", `%` = "acceptable in permissive dialects".
- **The honorification diagnostic is one of the contested ones.** In the argument list of §3.1, "stacked Nominative fails to trigger Honorific Agreement or license a Nom-marked Floated Quantifier **for some speakers**." Yoon's honorific examples with a dative experiencer, plain and stacked, both carry `%`.
- **Stacked nominative is not restricted to subjects.** Yoon's (20) has it on a locative (`cipan-eyse-ka` 'in the house'), a source (`ku kulus-eyse-ka` 'from that bowl'), and a temporal (`ecey-pwuthe-ka` 'from yesterday'). His Case Extension Rule explicitly puts nominative "on a temporal or locative adjunct."
- **Yoon's positive analysis is Major Subject, not Grammatical Subject** (§5.1, §5.2): nominative stacks on major subjects, a function distinct from the grammatical subject that subjecthood tests pick out.
- **The point that bears hardest on our §4.5** (§6.3): "Nominative is not assigned by agreement in Korean … This is what allows Subject Agreement to be controlled by the Grammatical Subject, regardless of how it is case-marked." If that's right, dative case never conceals subjecthood from honorification, there is nothing for the construction to override, and the honorification half of §4.5 is a **non-instance** by the paper's own §2.3 test, not a positive case.
- **Bonus, and it supports the external-possession cut.** Yoon §6.4 analyses `Cheli-ka Yenghi-lul son-ul cap-ass-ta` 'Cheli caught Yenghi by the hand', which is Kim's cut example (21), as Major Object plus Grammatical Object, with the possessor as the non-selected major object rather than as an argument accessed through the possessum NP.

### Is there a better Korean construction? (searched 2026-07-26)

Brett asked whether a different Korean construction fits the schema better than the dative-subject case. Searches run: Kim's own reference lists in the Routledge book and the indeterminacy manuscript (his Korean self-citations are Kim 2016b *The syntactic structures of Korean*, Kim 2013/2015 on Korean sluicing, Kim 2003b on focus projections; nothing on honorification or case stacking); portfolio-wide grep for honorification and plural `-tul`; then web searches on possessor-internal honorification and on the extrinsic plural marker. Result: the honorification route is closed, and the live candidates use case rather than agreement as $R$.

**The honorification route is closed, and now on the record.** `literature/kim-findlay-2023-subject-honorific-si-korean.pdf` = Yoolim Kim and Jamie Y. Findlay, "On the 'subject' honorific *-si-* in Korean," *Proceedings of the Linguistic Society of America* 8(1): 5534, 2023, doi 10.3765/plsa.v8i1.5534 (verified via Crossref). Read.

- Their (12) is the topology the paper wants: `halmeni-uy chascan-i alumda-usi-ta` (grandmother-POSS cup-SUBJ be.lovely-SI) 'Grandmother's cup is lovely', where a genitive possessor **inside** the subject NP controls `-si-`. Their (11) `halmeni-kkeyse pal-i apu-si-ta` is the inalienable version, and their (3), from Yeon and Brown 2011: 189, is `halapeci-nun pang-i khu-si-ta`.
- But their thesis is that **honorification isn't agreement**: `-si-` is optional and contextually determined where agreement is lexically controlled and obligatory; the target can be an entity the sentence never mentions (their (4)); and in service encounters it marks respect to the addressee (their (5), from Brown 2015: 310). Their positive account makes the target the closest human referent to the subject under a pragmatic PROXIMITY relation.
- They cite **Kim and Sells 2007: 310, 312ff.** making the same anti-agreement points and proposing the "maximal human referent" of the subject. That is our co-author's own earlier position, so the objection isn't an outside one.
- Consequence: `-si-` is the wrong $R$ for a mediated-accessibility case, because the target isn't reached *through* the subject NP but identified pragmatically. This independently confirms the §4.5 reframe and rules out the obvious repair (swapping in the possessor-internal honorification data). Cited in §4.5 in one clause.

**Live candidates, all unread, all using case rather than honorification as $R$:**

1. **Raising of major arguments.** Yoon, James H. 2007. "Raising of major arguments in Korean and Japanese." *Natural Language & Linguistic Theory* 25: 615–653, doi 10.1007/s11049-007-9020-2 (a companion chapter version is doi 10.1007/978-1-4020-6176-9_4, 71–107, in *New Horizons in the Analysis of Control and Raising*). Cited by Park and Kim 2022 on major subjects. Prospective shape: $X$ = the embedded clause, $P$ = the embedded argument's status, $R$ = matrix accusative marking, with the non-raised variant as the language-internal default-conceal. That is the Tsez long-distance-agreement topology with case in place of agreement, which is the one topology the paper already works.
2. **Nominative-nominative case stacking.** Levin, Theodore. 2017. "Successive-cyclic case assignment: Korean nominative-nominative case-stacking." *Natural Language & Linguistic Theory* 35: 447–498, doi 10.1007/s11049-016-9342-z. Also cited by Park and Kim. Case assignment reaching across a clause boundary is structurally mediated in the way honorification isn't.
3. **Extrinsic plural marker.** `literature/kim-ogrady-deen-2014-extrinsic-plural-marker-korean.pdf` = Chae Eun Kim, William O'Grady and Kamil Deen, "The extrinsic plural marker in Korean: Five studies," *Korean Linguistics* 16(1): 1–17, 2014, doi 10.1075/kl.16.1.01kim. Skimmed, not read through. `-tul` copies onto non-subject hosts including direct objects, adverbs, nominalized verbs, PPs, and complementizers, and is licensed by a plural subject, which is the Lardil/Kayardild inward-dependent-access shape. **Caution:** the literature treats it as a distributive marker (Song 1975, Kuh 1987, Song 1997), and their experiment found adults accept it in distributive contexts at over 90% against 20% in non-distributive ones, so $P$ would be distributivity rather than plain subject number, and the concealment question needs care. It is also rare: they report it occurs far less often than the intrinsic plural.
4. **Scrambling and scope**, the half of the test Kim still owes.

### park-kim-2022-nominative-objects (read 2026-07-26)

Chongwon Park and Jong-Bok Kim, "Nominative objects in Korean," *Linguistics* 60(5): 1487–1537, 2022. DOI 10.1515/ling-2020-0248 (authors, title, journal, volume, issue, pages, year verified via Crossref; note author order, Park first). **Gold open access, CC-BY** per Unpaywall, DOAJ, and Semantic Scholar, but the only OA location is De Gruyter's own PDF endpoint, which answers automated requests with a 202 and an empty body, and the Wayback Machine has no snapshot of it. It needs to be opened in a browser.

Brett supplied the PDF; filed as `literature/park-kim-2022-nominative-objects-korean.{pdf,md}` with the image folder renamed and the `.md` image links rewritten to match. Read. It is a Cognitive Grammar analysis of the Nominative Object Construction `[N-NOM N-NOM PSYCH-PRED]`, so the *stacked* dative-nominative pattern of Kim's (20) is not in it; that is Yoon's territory. What it does supply, in §4.1, is the dative-subject diagnostic our §4.5 needs, together with Kim's own limits on it.

- **p. 1504, example (32).** `apeci-eykey ton-i manh-usi-ta` (father-DAT money-NOM be.much-HON-DECL) '(My) father has a lot of money.' Their reading: "The subject of (32) is the dative-marked nominal, apeci 'father' … The subjecthood of apeci becomes apparent because of the honorific marker -(u)si-. The inanimate entity ton 'money' cannot be honorified, and the only candidate for the honorification is apeci 'father' in (32), though it is marked dative."
- **p. 1504, the framing sentence that cuts against our concealment story:** "There is no denying that a typical subject in Korean is marked nominative. However, **the case marker itself does not determine subjecthood**; there are many instances where the subject appears with non-nominative markers."
- **p. 1505, their own caution:** "That said, this test needs to be used with great caution. Honorification is a discourse phenomenon, and the agreement pattern often defies a grammatical relation." Their (35), `ton-i manh-usi-neyyo` '(You) must be rich' (uttered while looking at someone driving a BMW), has `-usi-` with an inanimate nominative subject, which they take to support Lim's (2000) addressee-honorific analysis. Footnote 16: "It is generally believed that the honorific marker agrees with the subject. However … this assumption is not foolproof."
- **pp. 1504--1505, examples (33)/(34):** `apeci-ka Gio-ka philyoha-si-ta` '(My) father is in need of Gio' versus `*Gio-ka apeci-ka philyoha-si-ta`, the same `philyoha-` predicate as Kim's (20).
- **Judgment methodology** (§1): 12 naive native speakers, Likert 1--6; asterisk below an average of 2, acceptable at 4.5 or above, one or two question marks in between.
- They engage the major-subject literature directly (Yoon 2007 on major subjects and SOR; Levin 2017 on Korean nominative-nominative case stacking), so the major-subject question is live in Kim's own framing, not an outside objection.

**Consequence, implemented in §4.5 on 2026-07-26.** Both sources agree, in different vocabularies, that case marking doesn't determine subjecthood in Korean. That removes the concealment the schema needs: if dative marking never hides subjecthood from subject-oriented morphosyntax, there is no override, and the construction is a non-instance by the §2.3 test rather than a positive instance. §4.5 now reports both constructions with both sources, states the three qualifications, and leaves the verdict open, naming what would settle it (whether $R$ tracks grammatical subjecthood or major-subject status). §4.6 uses the open verdict as evidence that the baseline is fixed language-internally: an English-shaped default would have returned a confident yes.

## kim-2026-indeterminacy-free-relatives (added 2026-07-26)

`literature/kim-indeterminacy-free-relatives-2026-04-11.pdf`. Jong-Bok Kim, "Indeterminacy in English Grammar: Focusing on Free Relative Clauses." Unpublished manuscript, 56 pp., LaTeX, PDF created 11 April 2026 (no author line or dateline in the document itself; the date in the bib entry is the file's, and the affiliation is deliberately omitted). Digits survive extraction in this PDF, unlike `kim2015binominal`, so page numbers below come from the manuscript's own table of contents and running text.

Read for §2.5. Section 5 is entirely on transparent free relatives and revises the analysis in the Routledge book (§5.9.4: "Key revision from Kim (2025)").

- **§5.5, pp. 36–39: six transparency effects.** Agreement (p. 36), selection (p. 37), coordination (p. 38), definiteness (p. 38), binding (p. 39), idiom (p. 39). Kim's gloss: phenomena "in which the matrix predicate, agreement, or binding relations are determined not by the wh-clause but by the nucleus outside the clause."
- **Selection transparency (p. 37) is wider than our "syntactic-category transparency."** Kim's cases include NP nuclei satisfying a preposition's requirement (*He speaks in [what linguists call a Northern dialect]*, COCA 1994 FIC) as well as an AP nucleus satisfying a copula (*This corruption is now [what they call systemic]*, COCA 2000 SPOK). Our label picked out only the non-NP sub-case.
- **§5.6, p. 40: verb classes are attributional vs evidential.** Attributional: *call, consider, describe as, regard as, take to be, refer to as, characterize as, interpret as*; licenses non-NP nuclei (AP, PP, AdvP, VP-*ing*). Evidential: *seem (to be), appear (to be), happen to be*; NP nuclei only. The exhaustive COCA result (zero non-NP nuclei with *seem*/*appear* against 178 hits for attributional verbs) is credited to Kim and Reynolds 2026, i.e. our own joint note.
- **§5.9.2, p. 46: the inheritance hierarchy.** Parent licenses agreement, selection, binding, and coordination transparency across both verb classes, with NP nuclei for all verbs; the attributional daughter adds non-NP nuclei and the attributional-frame conventional implicature; the evidential daughter inherits only the shared properties. **This corrected a mis-assignment in our §2.5**, which had put selection/category transparency wholly at the daughter level.
- **Book record settled 2026-07-26 (Brett supplied the Taylor & Francis page).** `kim-2026-form-function` is correct as it stands and needs no edit: *Form and Function Mapping in English Syntax: A Construction Grammar Perspective*, Jong-Bok Kim, 1st edn, first published 2026, Pub. Location New York, imprint Routledge, 422 pp., DOI 10.4324/9781003711919, eBook published 28 July 2026 (eBook ISBN 9781003711919; the bib carries the print ISBN 9781041194613). So the "Mismatches" / "Construction-Grammar" wording on the preprint's inner title page is a stale artifact, and "Mapping" is right. The 422-page extent is consistent with the pp. 98--103 and ch. 6.8 locators used in §2.
- **Bibliographic finding.** The reference list carries two works with almost the same title: Kim 2017, "Free relative clause constructions," in Kim (ed.), *Form and Function Mapping in English Syntax* (Seoul: Kyung Hee University Press), and Kim 2025, *Form and Function Mapping in English Syntax: A Construction Grammar Perspective* (London: Routledge). The second is our `kim-2026-form-function`, dated 2025 and placed in London there against the copyright page's New York and Routledge's 29 July 2026 publication date. That stray 2025 is the likely source of Kim's "change Kim 2025 to Kim 2026" note. The list also cites the joint TFR work as a WRAPP workshop paper (Göttingen, 8 April 2026) titled "Polyfunctionality of *what* in English transparent free relative constructions," which may or may not be the same output as our `kim-reynolds-2026-tfr-two-kinds`; asked in correspondence.
- **Stale cross-references in the manuscript** (flagged to Kim): §5.5.2 refers to "(a)"/"(b)" for examples (169)/(170), §5.5.5 to "(66a)"/"(66b)" for (180)/(181), §5.5.6 to "(67a)" for (182).

## kim-sells-2015-binominal-nps and kim-2004-hybrid-agreement (added 2026-07-26)

`literature/kim2015binominal.pdf`. Kim and Sells, "English binominal NPs: A construction-based perspective," *Journal of Linguistics* 51(1): 41–73, doi 10.1017/S002222671400005X (verified via Crossref). The paper is about the *those fools of a crew* binominal, not pseudo-partitives, but pp. 64–65 run the morpho-syntactic/index agreement distinction on exactly our measure and collective cases: *[Four pounds] was quite a bit of money in 1950* (morphosyntactically plural, index singular) and *[this team] have/has trained* (morphosyntactically singular, plural index available).

p. 64 credits the two-level analysis to Kathol (1999) and **Kim (2004), "Hybrid agreement in English," *Linguistics* 42(6): 1105–1128**, doi 10.1515/ling.2004.42.6.1105. That closes the old `% TODO(brett)` for "the exact Jong-Bok Kim forthcoming citation for the index-agreement analysis": it isn't forthcoming. Crossref confirms author, title, journal, volume, issue, and year; Crossref has no page field, so the page range comes from Kim and Sells's reference list (p. 72). Note their list prints the title as "Hybrid English agreement," with the words transposed against the publisher deposit; the bib follows the publisher.

Extraction warning: both the `.md` conversion and the PDF text layer of `kim2015binominal` silently drop numerals ("Kathol () and Kim ()"), so years, volumes, and page numbers were read off rendered pages, not extracted text. Kim 2004 itself has not been read.

---

## Head-marked agreement and possessor near misses (added 2026-06-25)

PDFs are stored in `paper/sources/head-marked-transparency/`. The purpose of this source cluster is narrow: it supports the caution in §6 that head-marked agreement does not by itself guarantee English-style NP transparency. The positive-looking cases are mostly possessor constructions, and the strongest analyses introduce a clause-level relation.

### ritchie-2014-chimane-possessor-agreement

**Full bibliographic entry:** Sandy Ritchie (2014), "Possessor co-reference marking and agreement in Chimane," in Aicha Belkadi, Kakia Chatsiou, and Kirsty Rowan (eds.), *Proceedings of Conference on Language Documentation and Linguistic Theory 4*, London: SOAS, 133--148.

**Status:** partial (front matter, introduction, Chimane example, and analysis framing read)

**Relevance:** useful (strongest near-positive head-marked case)

**Summary:**

- Chimane predicate-possessor agreement lets possessors that appear internal to possessive object NPs control object agreement on the verb.
- The core example has masculine verbal agreement tracking possessor Benjamin while the possessed noun `frog' is feminine.
- Ritchie treats the construction as formally different from standard external possession but still discourse-sensitive, especially to possessor topicality.

**Claims this source can support:**

- Chimane is a surface-positive near case for embedded possessor control of verbal agreement.
- The source itself presents the construction as locality-challenging and not a straightforward English-style transparency case.

**Quotations (≤25 words each):**

- "possessors which appear to be internal to possessive object NPs can control object agreement on the verb" (p. 133)
- "What we appear to have here is an internal possessor which can control object agreement on the verb" (p. 134)

**Warnings / overinterpretation risks:**

- Do not present Chimane as a clean positive for intact-NP transparency. Ritchie's later HPSG/LFG paper introduces a clause-level proxy.

### ritchie-2016-prominent-internal-possessors

**Full bibliographic entry:** Sandy Ritchie (2016), "Two cases of prominent internal possessor constructions," in Doug Arnold, Miriam Butt, Berthold Crysmann, Tracy Holloway King, and Stefan Müller (eds.), *Proceedings of the Joint 2016 Conference on Head-driven Phrase Structure Grammar and Lexical Functional Grammar*, Stanford, CA: CSLI Publications, 620--640. DOI 10.21248/hpsg.2016.32.

**Status:** partial (abstract, introduction, Chimane analysis, and conclusion read)

**Relevance:** useful (analysis of why Chimane is mediated)

**Summary:**

- PIPCs involve an apparently non-local agreement relation between verbs and possessors internal to possessive NPs.
- In Chimane, the possessor agreement pattern is restricted to object NPs and accompanied by applicative-like verbal morphology.
- Ritchie analyzes the controller relation through a clause-level proxy object of the internal possessor, tied to secondary-topic status.

**Claims this source can support:**

- Chimane is the strongest near case, but Ritchie's analysis explicitly mediates the agreement through a clause-level proxy.
- Prominent internal possessors are information-structure-sensitive, not simple probes into arbitrary NP-internal dependents.

**Quotations (≤25 words each):**

- "internal possessors are able to control object agreement via a clause-level 'proxy' of the internal possessor" (p. 621)
- "possessors in PIPCs can participate in phrase-external syntax" (p. 622)

**Warnings / overinterpretation risks:**

- The paper includes Maithili as well as Chimane; cite only for the Chimane claims unless the Maithili comparison is developed.

### deal-2013-possessor-raising

**Full bibliographic entry:** Amy Rose Deal (2013), "Possessor Raising," *Linguistic Inquiry* 44(3): 391--432. DOI 10.1162/LING_a_00133.

**Status:** partial (abstract, introduction, diagnostic summary, and conclusion read)

**Relevance:** core negative control

**Summary:**

- Nez Perce object possessor raising has the right surface shape for transparency: the possessor controls object agreement.
- Deal argues the possessor moves from a possessum-DP-internal position to an athematic A-position in vP.
- The construction is diagnosed by objective case on the possessor, plural object agreement, separability of possessor and possessum, and special possessor-raising morphology.

**Claims this source can support:**

- Some strong surface positives are not transparency, because the possessor is no longer merely embedded inside the possessive DP.
- Nez Perce is a negative control for the diagnostic.

**Quotations (≤25 words each):**

- "The possessor phrase moves from a possessum-DP-internal position to an athematic A-position within vP" (p. 391)
- "controls plural object agreement" (p. 392)

**Warnings / overinterpretation risks:**

- Nez Perce is mixed in the relevant domain: objective case and object agreement both matter.

### deal-2017-external-possession

**Full bibliographic entry:** Amy Rose Deal (2017), "External possession and possessor raising," in Martin Everaert and Henk C. van Riemsdijk (eds.), *The Wiley Blackwell Companion to Syntax*, 2nd ed. DOI 10.1002/9781118358733.wbsyncom047.

**Status:** partial (introduction, historical analysis, Swahili/Mohawk sections, conclusion read)

**Relevance:** useful typological frame

**Summary:**

- External possession mismatches syntax and possession semantics: the possessor behaves syntactically as a verbal dependent but semantically as possessor of a co-argument.
- Deal surveys possessor raising, external possession, incorporation, control-like, raising-like, and other dependency types.
- The survey supports treating many apparent possessor-agreement effects as clause-level syntax rather than intact-NP transparency.

**Claims this source can support:**

- Apparent head-marked possessor transparency is often external possession, possessor raising, incorporation, or a related clause-level dependency.

**Quotations (≤25 words each):**

- "External possession is a phenomenon where a nominal is syntactically encoded as a verbal dependent" (p. 1)
- "Two major types of external possession constructions have emerged" (p. 30)

**Warnings / overinterpretation risks:**

- The chapter is a survey and theoretical synthesis; use language-specific primary sources for detailed claims where possible.

### bohnemeyer-butler-jaeger-2015-yucatec-head-marking

**Full bibliographic entry:** Jürgen Bohnemeyer, Lindsay K. Butler, and T. Florian Jaeger (2015), "Head-marking and agreement: Evidence from Yucatec Maya," in Jens Fleischhauer, Anja Latrouite, and Rainer Osswald (eds.), *Exploring the Syntax-Semantics-Pragmatics Interface*, Düsseldorf: Düsseldorf University Press, 49--82.

**Status:** partial (introduction and §2.2 read)

**Relevance:** background negative-control language type

**Summary:**

- Yucatec Maya is described as exclusively head-marking, with no nominal case marking.
- Cross-reference markers appear on predicates and on possessed nominals.

**Claims this source can support:**

- Yucatec is an appropriate head-marking backdrop for the typological check.

**Quotations (≤25 words each):**

- "Yucatec is an exclusively head-marking language" (p. 51)
- "there is no nominal case marking of any kind" (p. 51)

**Warnings / overinterpretation risks:**

- This source is not itself about transparency or possessor raising. Pair it with Lehmann for the possession-specific point.

### lehmann-2002-yucatec-possession

**Full bibliographic entry:** Christian Lehmann (2002), *Possession in Yucatec Maya*, 2nd rev. ed., ASSidUE 10, Erfurt: Seminar für Sprachwissenschaft der Universität Erfurt. ISSN 1612-0612.

**Status:** partial (front matter; §4 and §5.2 targeted by text search)

**Relevance:** useful negative-control possession source

**Summary:**

- Lehmann distinguishes internal and external possessor strategies.
- Yucatec Maya consistently uses the internal possessor strategy in situations of indirect possessor affection.
- The verbal grammar generally provides no place for an independent possessor constituent apart from the existential `yàan' construction.

**Claims this source can support:**

- In a head-marking Mayan language, ordinary possessor sensitivity does not automatically create clause-level transparency.

**Quotations (≤25 words each):**

- "YM consistently uses the internal possessor strategy" (p. 117)
- "There is no possessive dative outside ascription of possession in YM" (p. 121)
- "possessors of inalienable possessa are not dissociated from these" (p. 128)

**Warnings / overinterpretation risks:**

- The source is a detailed grammar of Yucatec possession, not a typological survey of head-marked transparency.

### merchant-2011-aleut-case-matters

**Full bibliographic entry:** Jason Merchant (2011), "Aleut case matters," in Etsuyo Yuasa, Tista Bagchi, and Katharine Beals (eds.), *Pragmatics and Autolexical Grammar: In Honor of Jerry Sadock*, Linguistik Aktuell/Linguistics Today 176, Amsterdam: John Benjamins, 193--210. DOI 10.1075/la.176.12mer.

**Status:** partial (abstract, core alternation, missing-possessor example, and analysis read)

**Relevance:** core typological pressure test

**Summary:**

- Aleut has a case/agreement alternation when a non-subject argument is syntactically unexpressed.
- The missing-possessor example contrasts an overt possessor, with ordinary agreement, and an unpronounced possessor, with relative marking on the subject and an anaphoric suffix on the verb.
- Merchant analyzes the missing element as syntactically present pro that moves into a local relation with T.
- The case is therefore a strong null-source/anaphoric accessibility case, but not a simple case of an overt NP-internal dependent controlling verbal morphology while remaining in place.

**Claims this source can support:**

- Aleut supplies a named positive case where a recoverable possessor subpart conditions clause-level morphology.
- The source status of `P' can be null/anaphoric rather than overt.

**Quotations (<=25 words each):**

- "Further examples illustrating the Aleut Effect are given in (6)--(8)" (p. 195)
- "Missing possessor of a non-subject" (p. 195)

**Warnings / overinterpretation risks:**

- Do not call this transparency "without structure" without qualification. Merchant's analysis rests on unpronounced syntactic pro.

### nordlinger-sadler-2004-tense-beyond-verb

**Full bibliographic entry:** Rachel Nordlinger and Louisa Sadler (2004), "Tense beyond the verb: Encoding clausal tense/aspect/mood on nominal dependents," *Natural Language and Linguistic Theory* 22(3): 597--641. DOI 10.1023/B:NALA.0000027720.41506.fe.

**Status:** partial (abstract, Lardil and Kayardild sections read)

**Relevance:** core inward-topology comparison

**Summary:**

- The paper surveys languages in which nominal dependents carry tense/aspect/mood morphology interpreted with respect to the clause.
- In Lardil, verbal TAM marking can require matching tense marking on non-subject NPs.
- In Kayardild, non-subject NPs carry modal case, and clausal TAM can be computed from both verbal and nominal morphology.
- The descriptive fact is independent of the LFG analysis: clausal information is morphologically visible on dependent nominals.

**Claims this source can support:**

- Mediated accessibility needn't be only inward-to-outward. Clause-level features can be visible on embedded/dependent nominals.
- Kayardild should be treated as an inward or concord-like topology, not as simple copying.

**Quotations (<=25 words each):**

- "properties of the clausal head ... being marked on clausal dependents" (p. 602)
- "clausal TAM features arise as a composite" (p. 602)

**Warnings / overinterpretation risks:**

- Avoid making the paper depend on a generative or LFG analysis. The typology claim uses the surface distribution and its interpretation.

### chung-1998-design-agreement / chung-2004-restructuring-chamorro

**Full bibliographic entry:** Sandra Chung (1998), *The Design of Agreement: Evidence from Chamorro*, Chicago: University of Chicago Press. Supporting source: Sandra Chung (2004), "Restructuring and verb-initial order in Chamorro," *Syntax* 7(3): 199--233.

**Status:** partial (publisher record for 1998; 2004 wh-agreement and restructuring sections read)

**Relevance:** useful path-topology comparison

**Summary:**

- Chung's Chamorro work treats wh-agreement as special morphology associated with wh-dependencies.
- The morphology varies with the grammatical relation/case of the extracted item.
- Long-distance examples can show agreement morphology on multiple predicates along the dependency path.
- The current paper leaves extraction aside, so Chamorro is best used as one typology row and one sentence.

**Claims this source can support:**

- Some accessibility relations are path-distributed rather than located at a single endpoint.
- Chamorro should remain a scoped comparison, not a new worked case in this paper.

**Quotations (<=25 words each):**

- "the special agreement characteristic of wh-dependencies in Chamorro" (Chung 2004, p. 209)
- "wh-agreement must occur" (Chung 2004, p. 210)

**Warnings / overinterpretation risks:**

- The 2004 article is generative in analysis. For this paper, use it only for the observable morphology and locality contrast.

### dryer-1992-kutenai-algonquian-obviation

**Full bibliographic entry:** Matthew S. Dryer (1992), "A Comparison of the Obviation Systems of Kutenai and Algonquian," in William Cowan (ed.), *Papers of the Twenty-Third Algonquian Conference*, Ottawa: Carleton University, 119--163.

**Status:** partial (possessor/possessed-noun obviation comparison read)

**Relevance:** useful boundary case

**Summary:**

- Dryer compares Kutenai and Algonquian obviation systems.
- In the relevant comparison, possessed nouns can bear obviation morphology reflecting the possessor.
- The possessed noun can still be syntactically obviative and can trigger obviative subject marking on the verb.
- This looks like possessor access at first, but it is better treated as feature relay through the possessed noun.

**Claims this source can support:**

- Algonquian/Kutenai obviation is a negative control: the possessor's feature is transformed/relayed onto the head rather than directly accessed by the predicate.

**Quotations (<=25 words each):**

- "the possessed noun bears obviative marking if and only if the possessor is obviative" (p. 125)
- "the verbs in both (19) and (20) inflect for an obviative subject" (p. 125)

**Warnings / overinterpretation risks:**

- This is a boundary case, not evidence for a fourth positive transparency topology.

---

## Curation

### huddleston-pullum-2002

**Full bibliographic entry:** Huddleston, Rodney, and Geoffrey K. Pullum (2002). *The Cambridge Grammar of the English Language*. Cambridge: Cambridge University Press. ISBN 978-0521431460. (CGEL.)

**Status:** partial (focused passages read: §3.3 of the noun chapter, the *number-transparent quantificational nouns* subsection; §18.2 of the agreement chapter, "Semantically motivated overrides with collective and number-transparent nouns")

**Relevance:** core (empirical anchor for §1 of the paper)

**Summary:**

- A small class of nouns (*lot, plenty, lots, bags, heaps, loads, oodles, stacks, remainder, rest, number, couple*) is *number-transparent*: agreement on the verb is determined by the *of*-complement, not by the surface number of the head.
- The class is divided structurally into singular forms taking *a*-determiner (*lot, number, couple*), plural-only forms without determiner (*lots, bags, heaps, ...*), and *the*-only forms (*remainder, rest*).
- The override is *obligatory* in the number-transparent construction (contrast with collectives, where the override is optional and reflects a meaning difference).
- CGEL takes the analysis as head + *of*-complement, not as complex quantifier; *number* is the head, *of protesters* is the complement; this requires positing a feature percolation / agreement-override mechanism rather than treating *a number of* as a flat quantifier.
- *Percent* is also classed here, taking number from its oblique (*a lot of students are*, *a lot of the cheese is*).

**Claims this source can support:**

- That number transparency is a recognised, well-described English phenomenon, with a closed lexical class and a defined structural skeleton.
- That at least *a lot of money is* and *a lot of tourists are* are not isolated agreement quirks but a systematic construction with count/non-count-sensitive agreement on the complement.
- That the construction supports the umbrella schema of the brief: the determiner-position complex (*a lot of*) is the mediator X; the number/count profile of the complement is the property P; agreement is the relation R.

**Quotations (≤25 words each):**

- "The main number-transparent nouns are as follows: lot plenty / lots bags heaps loads oodles stacks / remainder rest / number couple" (CGEL §3.3, around the table at example [57]).
- "Two of the most common overrides of the simple agreement rule are found with singular collective nouns and with the number-transparent quantificational noun construction" (CGEL §18.2).
- "The essential difference between the two constructions is that with collectives the override is optional, whereas in the number-transparent construction it is obligatory" (CGEL §18.2).
- "The clear cases of number-transparent singular nouns are *lot*, *number*, and *couple*. *Majority* and *minority* are borderline cases" (CGEL §18.2).

**Warnings / overinterpretation risks:**

- The term *number-transparent* is CGEL's own coinage; it should not be cited as if it were a generally-shared term in the wider linguistics literature without that context.
- The brief originally attributed the term to the *Cambridge Dictionary of English Grammar* (Peters 2013). That attribution is unverified and probably wrong; cite CGEL.
- Pages numbers cannot be quoted from the on-disk markdown extraction — verify against a paper copy of CGEL before submission.
- The CGEL analysis is structurally compositional (head + complement, plus override). A CxG-friendly reframing would treat the whole *a-NUM-of-NP* pattern as a form-meaning pairing without override; the choice of formal apparatus is something the paper will need to flag.

**Cross-references:** Goldberg (2006) for the CxG-style alternative to CGEL's override mechanism. Bell & Schäfer (2016) for an analogous *gradient-not-binary* treatment in a different morphological domain (compounds). Heyer & Kornishova (2018) cite CGEL (Bauer & Huddleston 2002, the lexical-word-formation chapter) as their linguistic baseline for English -*ness* nominalisations, providing an independent bridge between this paper and the priming literature.

### goldberg-2006

**Full bibliographic entry:** Goldberg, Adele E. (2006). *Constructions at Work: The Nature of Generalization in Language*. Oxford: Oxford University Press. ISBN 978-0199268511. DOI 10.1093/acprof:oso/9780199268511.001.0001.

**Status:** partial (chapter 1, "Overview," pp. 3–18, read in full; rest of book skimmed via the brief's framing)

**Relevance:** core (CxG framework underpins §3 of the paper)

**Summary:**

- Constructions are *learned form-meaning-or-discourse-function pairings*, ranging from morphemes to fully general phrasal patterns. Examples span morpheme (*pre-, -ing*), word, partly filled idiom (*jog <someone's> memory*), Covariational Conditional (*the Xer the Yer*), Ditransitive, Passive (Table 1.1, pp. 5).
- Argument structure is provided by the construction, not by the verb alone: *slice* in transitive, caused-motion, ditransitive, way, and resultative constructions has the same lexical meaning, but the constructions provide the argument-structure semantics.
- Constructions are stored if some aspect is non-predictable, *or* if they are fully predictable but sufficiently frequent (i.e. usage-based, not minimalist).
- Constructionist grammar is "what you see is what you get": no derivations, no underlying levels, no phonologically null elements.
- Subtle aspects of construal (e.g., DITRANSITIVE entails animate recipient, distinguishing *Liza sent Stan a book* from *??Liza sent storage a book*) are construction-specific, not lexical.
- "It's constructions all the way down."

**Claims this source can support:**

- That CxG treats constructions as form-meaning pairings whose internal organisation can be more or less *transparent* (predictable from parts) — directly the constructional-transparency case in the paper's §3.
- That a graded-compositionality scale across the constructicon (fully compositional → frozen idiom) is native to the CxG framework, not a foreign overlay.
- That a *number-transparent* NP can be re-stated as a construction (*[a NUMBER-NOUN of NP]*) carrying its own agreement specification, without a feature-override mechanism.

**Quotations (≤25 words each):**

- "Constructions—form and meaning pairings—have been the basis of major advances in the study of grammar since the days of the ancient Stoics." (Goldberg 2006: 3)
- "All levels of grammatical analysis involve constructions: learned pairings of form with semantic or discourse function." (Goldberg 2006: 5)
- "Any linguistic pattern is recognized as a construction as long as some aspect of its form or function is not strictly predictable from its component parts" (Goldberg 2006: 5)
- "Constructions are combined freely to form actual expressions as long as they are not in conflict." (Goldberg 2006: 10)
- "It's constructions all the way down." (Goldberg 2006: 18)

**Warnings / overinterpretation risks:**

- Goldberg's chapter is a programmatic overview, not a worked argument; substantive evidence is referenced but located in later chapters (e.g. ch. 2 on argument structure, ch. 3 on usage-based learning).
- "What you see is what you get" is a slogan; the chapter does posit inheritance hierarchies and argument-structure-construction abstractions that some critics would call covert structure.
- The chapter does not engage Haspelmath's descriptive/comparative-concept distinction. Goldberg's typological remarks operate as if categories like DITRANSITIVE travel cross-linguistically; for a Haspelmath-aware paper, that's a tension to flag (see the *Cross-paper tensions* section below).

**Cross-references:** CGEL §3.3 / §18.2 (number-transparent NPs as a candidate construction). Bell & Schäfer (2016) for a quantitative graded-transparency study within a constructionist-friendly framework. Khalidi (2018) for the metaphysical question of whether a CxG construction (a form-meaning pairing) is a *kind* of any sort.

### bell-schafer-2016

**Full bibliographic entry:** Bell, Melanie J., and Martin Schäfer (2016). "Modelling semantic transparency." *Morphology* 26(2): 157–199. DOI 10.1007/s11525-016-9286-3. Open access.

**Status:** partial (introduction, lit review, semantic-relations and methodology sections read in full; statistical models section skimmed; conclusion not yet read)

**Relevance:** core (compound semantic transparency, §4 of the paper)

**Summary:**

- Semantic transparency is treated as a *scalar* (continuous) variable, not the binary or four-fold category of earlier work (Sandra 1990; Libben et al. 2003).
- Central hypothesis: perceived semantic transparency = degree of *expectedness* in the compound's internal semantic structure.
- Three predictors of greater transparency: (1) higher frequency of N1 in the language; (2) higher frequency of the compound's semantic relation given N1; (3) higher productivity of N2 as the head of NN compounds.
- Whole-compound transparency is a function of constituent transparencies, but N1 and N2 contribute asymmetrically.
- Operationalisation: Reddy et al.'s (2011) database of 90 NN compounds with 8,100 human transparency ratings, scored against Levi's (1978) nine semantic relations (CAUSE1, CAUSE2, HAVE1, HAVE2, MAKE1, MAKE2, USE, BE, IN, FOR, FROM, ABOUT).
- Bottom line: "perceived transparency may itself be a reflex of ease of processing" — the predictors of transparency are also independent predictors of processing speed.

**Claims this source can support:**

- That compound semantic transparency is well-modelled as a graded variable, not a binary or four-fold one.
- That a quantitative model of transparency can be built from corpus-derivable predictors plus a small inventory of semantic relations.
- That perceived transparency is plausibly grounded in processing — supporting the paper's metaphysical claim that some transparency profiles are *projectible local kinds* in Khalidi's sense (causally grounded, processing-relevant).
- That CxG-style intuitions about graded compositionality are operationalisable.

**Quotations (≤25 words each):**

- "We view semantic transparency as falling on a continuum, with meaning predictability constituting one end of the scale and total semantic opacity, i.e. no discernible synchronic relation between the meaning of a complex word and the meaning of any of its constituents, constituting the other end." (Bell & Schäfer 2016: 158)
- "Our central hypothesis is that the perceived semantic transparency of a compound can be understood as the degree of expectedness in its internal semantic structure" (Bell & Schäfer 2016: 158)
- "Since all the significant predictors in our models of compound transparency are also known predictors of processing speed, perceived transparency may itself be a reflex of ease of processing." (Bell & Schäfer 2016: 157, abstract)

**Warnings / overinterpretation risks:**

- The paper is about NN compounds in English. Generalising to other compound types or other languages is the authors' speculation, not their finding.
- Their model fits Reddy et al.'s ratings well; whether ratings *are* the right operationalisation of transparency is a separate question (psycholinguistic transparency may dissociate from rated transparency at short SOAs — see Heyer & Kornishova 2018).
- Levi's (1978) relations are a coding scheme adopted from earlier work; their adequacy is debated (Downing 1977, Fanselow 1981 are cited as critics). Don't cite Levi without acknowledging the controversy.

**Cross-references:** Heyer & Kornishova (2018) for processing-time evidence about when transparency matters. Goldberg (2006) for the CxG side of graded compositionality. Reddy et al. (2011), cited within Bell & Schäfer, for the underlying ratings database.

### heyer-kornishova-2018

**Full bibliographic entry:** Heyer, Vera, and Dana Kornishova (2018). "Semantic transparency affects morphological priming . . . eventually." *Quarterly Journal of Experimental Psychology* 71(5): 1112–1124. DOI 10.1080/17470218.2017.1310915.

**Status:** read (full paper, 13 pp.)

**Relevance:** useful (processing-transparency evidence, §5 of the paper)

**Summary:**

- Two masked-priming experiments: English -*ness* nominalisations (49 native speakers; SOAs 39 ms vs 77 ms) and Russian -*ost'* nominalisations (61 native speakers; SOAs 33 ms vs 67 ms).
- Targets are adjective bases (*pale, dark, business-busy*); primes are: nominalisation (related), simplex noun (unrelated control), or adjective itself (identity).
- Transparency was rated continuously by separate native-speaker pre-test groups (28 for English; 38 for Russian); items range across the transparency scale.
- At short SOA: morphological priming is constant across the transparency scale (priming effects are 37-ms English, 16-ms Russian, but not modulated by transparency).
- At long SOA: morphological priming *increases with transparency* (51-ms English, 35-ms Russian, with positive Transparency × Prime Type interaction); a three-way interaction Transparency × Prime Type × SOA confirms the SOA-dependent modulation.
- Authors interpret this as evidence for an initial *morpho-orthographic* (semantically blind) decomposition phase, with semantic information entering only at later stages.
- Aligns with the Rastle-and-Davis 2008 / Davis-and-Rastle 2010 camp; argues against Feldman et al.'s (2009, 2012, 2015) claim that morpho-semantic information is utilised immediately.

**Claims this source can support:**

- That semantic transparency is *cognitively consequential* (it affects processing), not merely an analyst-imposed gradient.
- That transparency is a *time-course-sensitive* variable: which transparency distinctions show up depends on the processing window. This is a useful caveat for the paper's metaphysical claim that transparency-as-such is not a single psychological variable.
- That priming-style transparency effects are robust across languages with quite different morphological systems (English -*ness*; Russian -*ost'*).
- That CGEL's lexical-word-formation chapter (Bauer & Huddleston 2002) is the cited linguistic baseline for English -*ness* nominalisations, providing a within-paper bridge to CGEL.

**Quotations (≤25 words each):**

- "We found increased morphological priming for nominalisations at the transparent end of the scale (e.g. *paleness* – *pale*) in comparison to items at the opaque end (e.g. *business* – *busy*) but only at longer prime durations." (p. 1112, abstract)
- "The present findings are in line with models that posit an initial phase of morpho-orthographic (semantically blind) decomposition." (p. 1112, abstract)
- "It takes longer to access semantic information." (p. 1120, general discussion)
- "Morpho-orthographic information is utilised before morpho-semantic information." (p. 1120, conclusion)

**Warnings / overinterpretation risks:**

- The paper is about masked priming with -*ness* / -*ost'* nominalisations in two specific languages. It does not license general claims about "all transparency processing".
- The conclusion about a "semantically blind" first stage is contested (Feldman et al. cited internally are the rival camp); the meta-table on p. 1121 shows that the literature is genuinely mixed.
- Effect sizes are modest (e.g. transparent-vs-opaque difference of 14 ms in English long-SOA — see Table 3 column "Difference"; statistical significance is the relevant measure, not absolute size).

**Cross-references:** Bell & Schäfer (2016) for a non-priming, ratings-based approach to transparency that yields large effects without a time-course story. CGEL via Bauer & Huddleston (2002) for the linguistic description of -*ness*.

### haspelmath-2010

**Full bibliographic entry:** Haspelmath, Martin (2010). "Comparative concepts and descriptive categories in crosslinguistic studies." *Language* 86(3): 663–687. JSTOR 40961695. (Also deposited at Zenodo record `1303024`.)

**Status:** partial (abstract, §1 introduction, §2 setup read in full; §3–§9 not yet read)

**Relevance:** core (typological methodology, §6 of the paper)

**Summary:**

- *Categorial particularism*: each language's grammatical categories are defined by language-internal distribution; categories cannot be equated across languages.
- *Comparative concepts* are analyst-created tools for crosslinguistic comparison; they are not language-particular descriptive categories and are not psychologically real.
- Comparative concepts must be universally applicable; they are built from conceptual-semantic concepts, general formal concepts (e.g. "phonological word"), and other comparative concepts.
- Relationship between comparative concepts and descriptive categories is many-to-many: one comparative concept can be realised by several descriptive categories within a language; one descriptive category can correspond to several comparative concepts.
- Targets the *categorial universalist* assumption (categories like ADJECTIVE, PASSIVE, ACCUSATIVE travel across languages); critiques Newmeyer 2007 in particular.
- Applies whether or not "typology" or "comparative linguistics" is the preferred label; Haspelmath uses them interchangeably.

**Claims this source can support:**

- That a paper claiming any cross-linguistic generalisation about *transparency* must distinguish the comparative concept (analyst's tool) from the language-particular descriptive categories it abstracts over.
- That number-transparent-quantifier NPs in English and case-stacking transparency in Korean (if discussed) instantiate the same comparative concept of *mediated accessibility* without thereby being "the same category" in either language.
- That the brief's umbrella schema (X transparent w.r.t. P for relation R) is a comparative concept in Haspelmath's sense, not a universal category.

**Quotations (≤25 words each):**

- "Each language has its own categories, and to describe a language, a linguist must create a set of descriptive categories for it." (p. 664)
- "Comparative concepts are concepts created by comparative linguists for the specific purpose of crosslinguistic comparison." (p. 665)
- "Unlike descriptive categories, they are not part of language systems and are not needed by descriptive linguists or by speakers. They are not psychologically real, and they cannot be right or wrong." (p. 665)

**Warnings / overinterpretation risks:**

- Haspelmath frames this as a programmatic distinction; he allows that in practice typologists already operate this way (Greenberg, Comrie, Croft, Dryer). The paper's polemical force is against the *categorial universalist* assumption embedded in much generative typology.
- The descriptive/comparative split is itself contested (Newmeyer 2007 is the explicit foil; defenders of crosslinguistic categories include LFG and some HPSG work). Cite Haspelmath's framework in a way that acknowledges this.
- The boundary between "general formal concepts" (admissible building blocks) and "language-particular formal categories" (not admissible across languages) is sharper in the abstract than in practice.

**Cross-references:** Goldberg (2006) for a CxG framework that does work cross-linguistically without adopting Haspelmath's terminology — a tension to flag. Khalidi (2018) for the metaphysical question of whether comparative concepts can be *natural kinds* (Haspelmath would say no; Khalidi's framework leaves the question open at the local-kind level).

### khalidi-2018

**Full bibliographic entry:** Khalidi, Muhammad Ali (2018). "Natural kinds as nodes in causal networks." *Synthese* 195(4): 1379–1396. DOI 10.1007/s11229-015-0841-y. (Online first 2015; print 2018.)

**Status:** partial (sections 1–4 read in full; sections 5 and references not yet read)

**Relevance:** useful (metaphysical refinement for §7 of the paper, where transparency profiles have causal-processing grounding; not the umbrella — see Slater 2015 below and `DECISIONS.md` 2026-04-30 entry)

**Summary:**

- Natural-kind terms are projectible because the kinds themselves are implicated in causal processes.
- Each natural kind is identified with one or more *core causal properties* that, when instantiated, cause the instantiation of *derivative properties* in structured causal networks.
- Boyd's HPC view requires loosening: drop the *mechanism* and *homeostasis* requirements; keep the causal grounding. Boyd's view fits biological kinds with feedback loops better than chemical elements.
- Kinds can have fuzzy boundaries; degrees of naturalness along two dimensions (generality of projections; variety of projections), corresponding to two ontological dimensions of causal connection.
- Distinct from copying-based kinds (Millikan): copied kinds are still causal but the causal process is reproduction-plus-environmental-pressure-plus-function rather than mechanism-driven homeostasis.
- "Pure" copied kinds (artefacts produced by fiat without function) are weak natural-kind candidates because their properties aren't causally structured.
- Section 5 (not yet read) extends the account to kinds based in causal *history* rather than causal *power*.

**Claims this source can support:**

- That projectibility is a useful necessary-condition criterion for natural-kindhood.
- That whether the umbrella concept of *transparency* picks out a natural kind reduces to whether it is grounded in causal-network structure rich enough to support projectible generalisations across the senses. (The brief's argument: it is not.)
- That whether *local* transparency profiles (number-transparent NPs; compound-transparency-with-priming-effects; constructional compositionality gradients) are local kinds reduces to whether each is grounded in a recurrent causal network — answerable case-by-case.
- That natural-kind boundaries can be fuzzy without compromising kindhood — useful for the boundary-phenomena cluster of the wider HPC programme.

**Quotations (≤25 words each):**

- "Natural kinds are not just concatenations of properties but ordered hierarchies of properties, whose instances are related to one another as causes and effects in recurrent causal processes." (p. 1379, abstract)
- "Boyd's account has to be loosened in such a way as to retain the emphasis on causality without the mechanism or the homeostasis." (Khalidi 2018, online p. 6)
- "What enables natural kind categories to play the role that they do in our inductive, explanatory, and taxonomic practices is that they consist of highly connected nodes in causal networks." (online p. 7)
- "The account I am proposing is very similar to Boyd's when one drops the mechanism and homeostasis." (online p. 7, fn. 7)

**Warnings / overinterpretation risks:**

- Khalidi's causal-hierarchy commitment is strained for kinds whose stability is conventional, inherited, or multi-sourced. For most linguistic kinds — number-transparent NPs, constructional compositionality gradients — there is no clean "core property causes derivative properties" hierarchy; stability is overdetermined by entrenchment, learnability, processing, function, and convention. The paper uses Khalidi as a refinement for cases where stability *is* causal-processing-shaped (compound transparency, priming-graded morphological transparency), not as the umbrella.
- "Causal network" is a powerful but elastic notion. Without commitments about what counts as a node, an edge, or a network, "transparency profiles are local nodes in causal networks" can become unfalsifiable.
- The directed-causal-graph formalism (Fig. 1) is a sketch, not a worked-out framework; importing it into a linguistics paper is a choice that risks formalism-creep.
- Khalidi 2018 ≠ Khalidi 2013 (the book *Natural Categories and Human Kinds*) — they are mutually consistent but the 2018 paper is the more focused statement of the causal-network view.

**Cross-references:** Slater 2015 (in the central literature folder; entry below) for the maintenance/SPC umbrella the paper adopts. Boyd 1991, 1999 (in the central literature folder, not yet entered into this project) for the HPC view both Slater and Khalidi loosen, in different directions. Khalidi 2013 (in the central literature folder) for the book-length development.

### slater-2015

**Full bibliographic entry:** Slater, Matthew H. (2015). "Natural kindness." *British Journal for the Philosophy of Science* 66(2): 375–411. DOI 10.1093/bjps/axt033. (On disk at `literature/slater2015.md`/`.pdf`. The introduction names the view "Stable Property Cluster" account and credits its "Boydian origins.")

**Status:** partial (introduction and §§1–4.1 read; §§4.2–7 not yet read)

**Relevance:** core (metaphysical umbrella, §7 of the paper)

**Summary:**

- Proposes the *Stable Property Cluster* (SPC) account: a natural kind is a property cluster whose stability underwrites projection, regardless of *how* the stability is maintained.
- Boyd's HPC retains causal-mechanism and homeostasis commitments that are sometimes false and often vague; SPC drops both, keeping just the cluster + stability.
- Four motivations for the move: (i) methodological neutrality about the metaphysics of causation; (ii) HPC's mechanism-talk doesn't always accommodate epistemic practice; (iii) "homeostasis" is variably literal and metaphorical in Boyd's own writing; (iv) some kinds (quarks, electrons; some biological kinds) don't fit any precise causal-homeostatic-mechanism story.
- Argues SPC can be the *general* account of natural kinds, with HPC kinds and essentialist kinds as special cases, rather than HPC being a parallel "kind of natural kind."
- Stability is anchored to projectibility: a cluster is stable enough to count as a kind if it underwrites reliable inductive inference. The mechanism behind the stability — homeostasis, microstructural essence, conventional reproduction, usage entrenchment — is a downstream empirical question.

**Claims this source can support:**

- That natural-kindhood is most ontologically honestly stated as stable property clustering, with the source of stability left as a separate question.
- That linguistic kinds, whose stability is multi-sourced (entrenchment, learnability, processing, function, convention), are a natural fit for SPC and an awkward fit for both Boyd's HPC and Khalidi's causal-hierarchy account.
- That asking "is this transparency profile a local kind?" reduces to: is the cluster stable enough to project over? — answerable case-by-case, with the source of stability identified empirically rather than stipulated.
- That Slater's framework absorbs HPC and essentialist kinds as special cases, allowing the paper to remain neutral on the deeper metaphysics of causation while still doing real ontological work.

**Quotations (≤25 words each):**

- "Rather than emphasizing homeostasis or causal mechanism, the SPC account emphasizes the stability of a property cluster over the various ways stability may be maintained." (Slater 2015: §1)
- "Homeostatic causal mechanisms are but one way to achieve the stability of a bunch of clustered properties." (Slater 2015: §4)
- "It is, I think, an attractive candidate for a general natural kind concept, able to accommodate the diversity of natural kinds we find in the world." (Slater 2015: §1)

**Warnings / overinterpretation risks:**

- "Stability" is itself elastic; without an anchor in projectibility (Slater's anchor) it can sound trivial. Be precise about what stability the paper is claiming for each transparency profile.
- Slater is more honest about *what* natural-kindhood requires; Khalidi is more honest about *why* a particular cluster earns kindhood. The paper uses Slater as umbrella but should not be silent about the source of stability for each profile — that's where Khalidi (or usage-based-linguistics vocabulary) earns its keep.
- Slater 2015 is an article-length development of an extended argument; the bibliographic source includes the on-disk markdown but the publisher-of-record metadata should be re-confirmed against the BJPS page before submission. The version on disk is dated "Draft of 10 April 2011"; the published version may differ in places.

**Cross-references:** Khalidi 2018 (above) for the rival loosening of Boyd. Boyd 1991, 1999 (central literature folder) for the original HPC view. Brett's HPC book ch.~7 (NPI-as-class-not-kind passage) for the closest in-house structural analogue: a cluster of properties that doesn't earn natural-kindhood at the umbrella because the stability isn't there at the right grain.

---

## Cross-paper tensions

These are the contradictions and methodological mismatches surfaced by the intake. Use them to navigate the literature, not as a hit-list to settle in this paper.

### Time course of semantic transparency in lexical processing

**Heyer & Kornishova (2018)** versus **Bell & Schäfer (2016)**.

Heyer & Kornishova find that morpho-semantic information is *not* used at short SOAs (33–39 ms) and only becomes effective at longer SOAs (67–77 ms); the first decomposition stage is "semantically blind." Bell & Schäfer report that "perceived transparency may itself be a reflex of ease of processing," appealing to Marelli & Luzzatti's (2012) finding that semantic-transparency effects appear in *very early* stages of compound processing.

Direct empirical contradiction. The paper cannot uncritically claim "transparency affects processing" without flagging which stage of processing and which morphological domain is meant. Suggested resolution: present transparency as cognitively consequential (Bell & Schäfer's bottom line), but note Heyer & Kornishova's stage-specific qualification when discussing the time-course.

### CxG vs CGEL on agreement override

**Goldberg (2006)** versus **CGEL (Huddleston & Pullum 2002)**.

CGEL analyses the number-transparent NP as head + complement plus a feature-override on the simple agreement rule. CxG's "what you see is what you get" approach prefers to state the whole pattern as a form-meaning pairing without override.

Methodological/terminological mismatch, not direct contradiction. Both reject Abney-style DPs and both treat the construction as a proper object of analysis. The choice of formalism does not affect the data. The paper should be explicit about its choice.

### Slater vs Khalidi on what natural-kindhood requires (resolved)

**Slater (2015)** asserts clustering + stability; the source of stability is a separate empirical question. **Khalidi (2018)** asserts clustering + causal hierarchy (core properties cause derivative properties).

Both loosen Boyd's HPC, in different directions. Slater is more honest about *what* natural-kindhood requires (asserts only what observation warrants); Khalidi is more honest about *why* a particular cluster earns kindhood (gives an ontological account of projectibility). The most ontologically honest move depends on the question being asked: for stating the criterion, Slater; for explaining why a particular kind meets it, Khalidi.

**Resolved 2026-04-30 (see `DECISIONS.md`):** Slater's SPC + maintenance-as-umbrella is the metaphysical umbrella for this paper, with Khalidi 2018 as a finer-grain refinement for cases whose stability has identifiable causal-processing grounding. This matches the sister paper `Field_relative_HPC_categories/` and Brett's HPC book; it also fits linguistic kinds better, since their stability is overdetermined by entrenchment, learnability, processing, communicative function, and conventional inheritance, with no single mechanism constitutive.

### Goldberg's cross-linguistic remarks vs Haspelmath's particularism

**Goldberg (2006)** versus **Haspelmath (2010)**.

Goldberg's chapter uses category labels (DITRANSITIVE, PASSIVE, ARGUMENT-STRUCTURE-CONSTRUCTION) cross-linguistically without flagging the descriptive/comparative-concept distinction. Haspelmath would say these are comparative concepts and should be labelled as such.

Scope disagreement. Inferred — neither paper engages the other directly. The paper's §6 should follow Haspelmath's discipline; if §3 leans on Goldberg's CxG framework, the connection between language-particular constructions and the comparative concept of *mediated accessibility* needs to be made explicit.

### Aggregate ratings models vs stage-specific processing models

**Bell & Schäfer (2016)** versus the priming/eye-tracking literature cited within both Bell & Schäfer and Heyer & Kornishova (Libben 1998; Frisson et al. 2008; Marelli & Luzzatti 2012).

Bell & Schäfer's quantitative model fits aggregate transparency ratings well (R² up to ~0.95 in Reddy et al.'s combined-constituent model). The priming and eye-tracking literature reveals stage-specific exceptions that ratings can't see (e.g. opaque-component compounds suppressed by whole-word meaning).

Scope disagreement, not direct contradiction. Different operationalisations of transparency are sensitive to different things. The paper should treat ratings-based and processing-based transparency as complementary measurements of the same underlying gradient, not as competitors.
