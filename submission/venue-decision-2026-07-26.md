# Venue Decision Record
<!-- SUMMARY: Venue decision for the umbrella transparency paper: Language Sciences, APPROVED 2026-07-26; page-one reframe still owed, submission timing vs the pending sister paper still Brett's call (the ~4k-word cut condition is VOID: the journal has no word limit) · status: approved · updated: 2026-07-26 -->

## Record

- [x] Project: `papers/drafting/linguistic-transparency`
- [x] Manuscript title: Linguistic transparency as mediated accessibility
- [x] Venue: *Language Sciences* (Elsevier). **Approved 2026-07-26.** One condition still owed: the page-one reframe (see Risk Test).
- [x] Article type / section: Research Paper
- [x] Venue URL / author instructions checked: **partially.** ScienceDirect's guide-for-authors returns HTTP 403 to automated fetch (and `elsevier.com` 301s to it), so the length/abstract/format rules were **not** re-verified today. The working figure below is Brett's own project record, not a fresh reading of the guide. Open the guide in a browser before packaging.
- [x] Date checked: 2026-07-26 (scope evidence via OpenAlex; guide not readable)
- [x] Decision owner: Brett (co-author Jong-Bok Kim asked the question on 2026-07-26)
- [x] Assisting agent/model: Claude Opus 5 (1M context), Claude Code session
- [x] Recommendation status: **approved** (was proposed; confirmed by Brett 2026-07-26)
- [x] Final decision: ***Language Sciences*, approved by Brett 2026-07-26.** Still owed before packaging: the page-one reframe. Still Brett's call: whether to submit now or after the sister paper's decision lands. (The ~4,000-word cut originally listed here as a precondition is void; see the length item below.)

## Journal-Reader Contract

> This manuscript changes the problem of **what "transparency" picks out when linguists in different subfields use the word** for readers of ***Language Sciences*** by showing that the senses form one family of mediated-accessibility relations with a **falsifiable non-instance test** (a configuration counts only where the mediator's own default could have concealed the property, which excludes coordination), and that the resulting profiles, not the umbrella, are what support projection.

- [x] The debate/problem is visible in the title, abstract, and first two pages. Title carries "mediated accessibility"; the abstract states the non-instance requirement; §1 opens on CGEL number-transparent QNs.
- [ ] **The contribution is journal-local, not only topically adjacent.** This is the weak link and the standing-lesson wound (program-first drafting). The abstract currently closes on "grammatical kindhood is a downstream verdict of projectibility," which is the HPC programme's frame, not a *Language Sciences* debate. See Risk Test.
- [x] The expected reader can tell why the paper belongs here without relying on a cover letter, **provided** the comparative-concept framing (Haspelmath discipline, category diagnostics) leads and projectibility follows.
- [x] Reader's vocabulary decided. `check-terms.py main.tex` returns 0 flags. Split for this reader: **free** = transparency, agreement, comparative concept, descriptive category, construction, partitive/pseudo-partitive, mediator. **Earned (gloss at first use, already done)** = projectibility, projectibility profile, stabilizer, SPC, local kind, non-instance test. The earned list is exactly the programme vocabulary the standing lesson warns about; keep it downstream of the linguistic payoff.

## Fit Evidence

- [ ] Current aims/scope checked on the submission day. Scope evidence gathered from published content (below); the aims-and-scope text itself was not re-read today.
- [x] Article type, length, abstract, keywords, reference style, figures/tables, supplements, source-file expectations: length **checked and resolved 2026-07-26**. ~~Working length figure: 9,500–10,000 body words... roughly 40% over. Re-verify the figure, then cut.~~ **Struck.** The re-verification was done and it went the other way: *Language Sciences* has **no word limit**. Retrieved the full author guide via Wayback (2022, pre-Elsevier-SPA, 48,792 chars); the only length rule anywhere in it is 85 characters per highlights bullet. The 9,500–10,000 figure came from the sister paper's own compression note in `papers/queue/what-do-we-mean-by-language/STATUS.md` and was never a journal requirement, so it should not have been carried into this record as one. **The cut condition below is void.** The manuscript is now 44pp; length is not a submission obstacle and Brett confirmed on 2026-07-26 that it isn't a concern. Remaining sub-items (abstract, keywords, reference style, figures, supplements, source files) still unchecked (403 on the live page).
- [ ] AI-use, preprint, anonymity, data/code, simultaneous-submission policies: **not checked today.** Elsevier runs a disclosure model, which suits this paper. Manuscript side now compliant: the disclosure moved to page 1 via `\aidisclosure{}` on 2026-07-26 (**model list still needs Brett's confirmation**: currently "Claude Opus 4.7 & Opus 5 (1M context); OpenAI Codex 5.5; and GPT-5.6 Sol (pro)", assembled from the repo log rather than from Brett).
- [x] Recent venue articles making the match concrete.

Recent comparable venue articles or signals (OpenAlex, ISSN 0388-0001):

1. **"Challenging 'definite article' as a comparative concept: The case of Mopan Maya" (2022).** The closest precedent in the venue: a Haspelmath-style comparative-concept critique run through one language's descriptive category. §4 of this paper is the same move, generalized.
2. **"On the elusive nature of AGENT and agentive diagnostics: lessons from causee…" (2025)** and **"Support verbs that are not verbs" (2025).** Category-diagnostic papers: what a label picks out, tested against behaviour. That is §2's genre.
3. **"Four kinds of subjectivity: from speaking to communicating" (2025)**, **"Language ontologies and the worlding of language(s)/languaging" (2025)**, **"On uniqueness claims and the nature of language" (2026).** The sense-mapping / metatheory seam the sister paper was aimed at. It exists and is live.

Countervailing scope evidence, recorded honestly: of ~90 *Language Sciences* articles published since 2026-01-01, the clear majority are **ecolinguistics, ecological discourse analysis, pragmatics, multimodality, and Chinese-corpus metaphor** work. The metatheory seam above is real but thin, maybe five or six papers in eighteen months. A desk editor's default frame for this journal right now is not philosophy of grammatical categories. Searches for `projectibility` and `natural kind` inside the journal return no substantive in-venue conversation (hits are incidental), so §5 has no interlocutors there.

Editorial/reviewer fit:

- Likely editor or desk screen: same editorial office now handling `language-langsci` (*What do we mean by language*, submitted 2026-05-06, 81 days out, no decision).
- Plausible reviewer pool: comparative-concept/typology-methodology readers (the Mopan Maya lineage); CGEL-literate English-grammar readers for §2; a construction-grammar reader for §3.
- Reviewer pool mismatch risk: §5 (projectibility, SPC, Khalidi) has no natural reviewer at this venue. Expect it to be read as either optional or as the paper's real thesis, and the second reading is the dangerous one.

## Alternatives Considered

| Venue | Why plausible | Why not chosen now | Fallback status |
|---|---|---|---|
| *Linguistics* (De Gruyter Brill / Mouton) | Best content fit of the three: recent issues carry exactly this range (word-formation and productivity, expletive negation in Greek, Cushitic metrification and typology, Najdi Arabic topics). Kim knows the venue. QNs, TFRs, Tsez, and Korean would all land. | Two blockers. (1) **AI policy is prohibition-model** and current as of today: De Gruyter Brill "does not accept papers … generated by Artificial Intelligence," with disclosure required where AI output "significantly contributed." Honest human authorship plus disclosure satisfies that in principle, but this paper's acknowledgement reads "drafted with the assistance of large language models," which a strict desk editor can read as generation. House rule is not to soften a truthful disclosure. (2) `countability-linguistics` has been pending there since 2026-03-31 (117 days), and it is another HPC-application paper. | Live backup on content; resolve the AI-policy reading first |
| *Journal of Linguistics* (CUP) | General theoretical venue; §2 and §4 would read as conventional. | `definiteness-jol` pending since 2026-06-11 (45 days). Also the venue with the lowest recorded prior confidence (brett p_acc=0.25, claude 0.20), and §5 would have to shrink to a coda, a bigger rebuild than the length trim Kim is asking for. | Third choice |
| *Studies in Language* / *Linguistic Typology* | Own the comparative-concept move outright. | §4 doesn't dominate the paper, and won't after the appendix move. Typology venues will want more than three non-English languages in the body. *Linguistic Typology* is also De Gruyter, so it inherits the AI-policy question. | Only if the paper is rebuilt around §4 |
| *Cognitive Linguistics* | §3 (constructional and form–meaning accessibility) is nominally in scope. | Ruled out by a recorded outcome: the English-LBC paper was desk-rejected there on 2026-05-26 for using cognitive-linguistic themes without the usage-based background. §3 of this paper is thinner (770 words) than that paper's engagement was. | Rejected |
| *Glossa* | Open access, general linguistics, disclosure-model AI policy, no pending Reynolds submission. | Scope skews formal syntax/semantics; the metatheory fit is unverified. Needs a real scope check before it can be ranked. | Unranked backup; check scope if LS and Linguistics both fail |

## Risk Test

- **Strongest desk-rejection risk: length.** ~14,000 body words against a recorded ~10,000 budget, before the editor reads a line of the argument. This is Kim's worry, and he is right about it even though his proposed cuts (§4.7–4.8, 244 words between them) address about 6% of the overage.
- **Strongest reviewer-rejection risk: the §5 framing reads as the thesis.** A *Language Sciences* reviewer with no projectibility background who takes "kindhood is the downstream verdict" as the paper's claim will ask what a linguist gains, and the answer (a diagnostic that excludes coordination and a cluster that predicts QN behaviour) is currently delivered late.
- **Strongest "not motivated / no live problem" risk: moderate, and the mitigation is already half-built.** The non-instance test is a real falsifiable filter and §2.2's *bunch* demotion shows it biting. Both need to be visible on page one in the reader's terms, not in the schema's.
- **Strongest "opinion piece / no evidence" risk: low.** The COCA pilot (Appendix A), the CGEL locators, and the glossed Spanish/Tsez/Aleut/Chimane/Yucatec data are all source-grounded and verified against the PDFs.
- **Strongest "wrong literature / wrong methodology" risk: low at LS**, higher at any venue that owns one of the sub-literatures (the Cognitive Linguistics outcome is the precedent).
- **Doubling up with a pending sister submission.** `language-langsci` is the closest methodological twin of this paper and has been at *Language Sciences* for 81 days with no decision (ledger median for a reviewed decision in this class: 48 days). Two overlapping-methodology Reynolds papers in one editorial queue invites a redundancy read, and a framing-based rejection of the first would transfer straight to the second.

Resolution:

- [ ] Risks resolved in manuscript before package work.
- [ ] Risks accepted explicitly by Brett.
- [x] **Risks unresolved: pause.** Two stop conditions stand: the length overage and the page-one framing. Both are ordinary revision work, not venue problems, and both are owed for *any* of the top three venues, so the venue commitment can wait for them.

Sequencing this suggests: make the cut and clear Kim's outstanding citation items (2–4 weeks), by which point the *Language Sciences* decision on the sister paper should have landed and can inform the choice rather than being guessed at.

## Evidence And Motivation Test

- [x] The manuscript shows the problem is live: *CGEL* number transparency, CxG compositionality gradients, rated compound transparency, and masked-priming transparency are four existing literatures using one word for different relations, all cited and read.
- [x] The first two pages name the evidential standard (the non-instance requirement, with coordination as the worked exclusion).
- [x] Methodological engagement is current where it matters: Haspelmath 2010 against Newmeyer 2007, with Croft's RCG positioned.
- [x] Interdisciplinary ownership: the main payoff is claimed for descriptive/theoretical grammarians and typologists. The philosophy of science is instrumental. **The manuscript should say so earlier than it does.**

## Forecast (Prediction Ledger)

- Base rate for this venue class (`score.py`, 2026-07-26): **linguistics, n=12, desk survival 7/12 (58%), acceptance 3/12 (25%).** Reviewed-decision latency median 48 days (range 20–196).
- P(survives desk / reaches external review): **Brett to record.** Claude's estimate: 0.45 at current length, 0.65 after the cut and reframe.
- P(eventually accepted at this venue): **Brett to record.** Claude's estimate: 0.25.
- Expected first decision by: **Brett to record.**

Append `event` and `forecast` records to `Project-Management/prediction-ledger/ledger.jsonl` on submission, not before.

## Package Authorization

- [x] Venue decision approved before target-specific package work begins. **Approved 2026-07-26: *Language Sciences*.**
- [x] Brett has approved the target. He confirmed the venue was already agreed; this record had lagged behind the decision rather than the decision being open. **Timing is the one sub-question still live** (submit now vs. after the sister paper's *Language Sciences* decision lands, 81 days out), and the unsent reply to Kim currently says the latter.
- [x] Unresolved risks copied into the pre-submission checklist: ~~length cut to ~10,000 body words~~ (void, no word limit); page-one reframe; ~~page-one `\aidisclosure{}` migration~~ (**done 2026-07-26**, page 1 after the abstract, plural-responsibility variant defined locally since the repo's preamble snapshot predates the central macro; **model list still needs Brett's confirmation**); Kim's outstanding Korean citation (`% TODO(kim)` in `06-typological-transparency.tex`); confirmation of the citable form of the joint TFR work (Kim's own list gives it as a WRAPP Göttingen conference paper, the bib as a working note).
- Closed since this record was written: the §2 index-agreement citation (Kim 2004 plus Kim and Sells 2015, both verified and cited); the Kim book record (Taylor & Francis confirms *Form and Function **Mapping*** …, New York, 2026, 422 pp., DOI 10.4324/9781003711919, so `kim-2026-form-function` stands as written and the preprint's "Mismatches" title page is a stale artifact).
- [x] Linked from `DECISIONS.md`; `STATUS.md` updated.

Decision summary, logged to `DECISIONS.md` 2026-07-26:

```markdown
2026-07-26 - Venue decision: *Language Sciences* for "Linguistic transparency as mediated accessibility". Owner: Brett, agent-assisted (Claude Opus 5). Record: `submission/venue-decision-2026-07-26.md`. Reason: the journal-reader contract holds - the paper changes how descriptive and theoretical grammarians handle multi-sense grammatical labels by supplying a comparative concept with a non-instance test, and the venue publishes exactly this (incl. the 2022 piece challenging "definite article" as a comparative concept). Risks accepted: doubling up while a sister paper is pending there, so a framing rejection on the first could transfer; timing left to Brett.
```
