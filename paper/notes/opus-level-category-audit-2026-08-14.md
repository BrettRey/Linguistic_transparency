# Narrow level/category audit

Read-only; no files touched. Findings ordered by severity.

## Substantive

**1. Coordination is failed at the wrong gate (bearer vs mediator).**
- §1: "Coordination fails the second gate: in *Bob and Jane are happy*, plural agreement sums the conjuncts' features, and no mediator stands between a bearer and the relation." §2-3: "Coordination fails the test for want of a mediator." Table 3: "Coordination | summed number, borne by no single conjunct".
- Mismatch: the table locates the failure at gate 1, not gate 2. If *P* is summed plurality and no single element bears it, there is no bearer, and gate 2 (bearer and mediator distinct) never gets a chance to fail. The contrast built on this ("Coordination fails the test for want of a mediator; this fails for want of a bearer") then collapses, because both would fail for want of a bearer.
- Repair: either (a) define *P* as the conjuncts' number features jointly and say gate 1 admits distributed bearers, keeping the gate-2 verdict; or (b) keep *P* as summed plurality and record coordination as a gate-1 failure of a different shape from deferred reference (no single bearer vs no internal bearer). Option (a) preserves the contrast and needs one clause.

**2. "Conceal" is used for two different things: the mediator element and the counterpart construction.**
- §2-2: "The schema requires one element within $X$ to bear $P$ and another to conceal it." §2-3: "The schema requires that $X$ \mention{could have} made $P$ inaccessible."
- Mismatch: in §1 concealment is a property of the *concealing counterpart*, an independently established sibling construction (gate 4). The mediator's job is to intervene, not to conceal. §2-2 assigns concealment to a co-constituent, §2-3 assigns it to $X$ itself, and Table 3 gives collectives "—" in both the mediator and the counterpart columns, so the reader cannot tell which role was empty.
- Repair: reserve *conceal* for the counterpart throughout; use *intervene* or *mediate* for the element. §2-2 becomes "requires one element within $X$ to bear $P$ and a distinct element to mediate access to it".

**3. Tsez: the mediator slot is filled by $X$.**
- §6: "$X$ is the embedded clause, $P$ is the noun class of the embedded absolutive, and $R$ is matrix verb agreement." Table 3: "Tsez complement clause | ... | Mediator: the clause".
- Mismatch: gate 2 requires the mediator be distinct from the bearer and internal to $X$. Here mediator = $X$, so the configuration is doing duty as an element and gate 2 is vacuously satisfied. Compare the QN row, where $X$ is the NP and the mediator is the head noun inside it.
- Repair: name the class-IV-bearing element as the mediator (the nominalized clausal head, `-łi`), which is what the class IV default is registered on, and leave $X$ as the clause.

**4. Configurations in the mediator column generally.**
- Table 3: "the extraction path" (Chamorro), "the dependency domain" (Lardil/Kayardild), "the clause" (Tsez).
- Mismatch: gate 2 licenses "expressions or independently motivated structural positions". A path and a domain are neither; they are configurations, and a configuration cannot be the thing a property remains accessible *across* in the sense the QN and TFR rows use. The Chamorro row also leaves the bearer unnamed while giving *P* as "grammatical relation of the extractee", which is a relational property whose bearer would be the extractee.
- Repair: widen gate 2 explicitly to admit independently motivated domains and paths, with a stated individuation criterion, or mark these mediator cells as unfilled, consistent with their Indeterminate verdicts.

**5. HPSG paragraph re-imports collectives after ruling them out.**
- §2-2: "That's a different formal encoding of the same accessibility relation."
- Mismatch: the paragraph opens correctly with "encodes the same *observation*", then upgrades to "the same accessibility relation". On the paper's own verdict two sentences earlier, collectives are not an accessibility relation; index/concord mismatch is precisely what a one-sign competition looks like when formalized.
- Repair: end at "observation", and add that the index/concord split formalizes the single-sign diagnosis rather than converting collectives into schema instances.

**6. TFR attributional daughter: the counterpart cell holds a distributional restriction, not a concealment.**
- Table 3: "TFR, attributional daughter | ... | Concealing counterpart: evidential daughter, NP nuclei only".
- Mismatch: gate 4 requires a counterpart in which $R$ tracks the mediator or $X$ *instead of* the bearer. An NP-only nucleus restriction is an environment where mediator and bearer category coincide, so nothing is concealed; it is neutralization, not control. This is the same defect the paper itself catches for (\ref{ex:tfr-r-relations}c) and predicative position.
- Repair: mark the daughter's counterpart gate unmet and its category-flexibility verdict indeterminate pending a category-discriminating environment, or supply a fused-relative environment where selection tracks *what*'s NP category against a non-NP nucleus.

**7. Aleut: the qualification names the wrong gate.**
- Table 4: "Positive with qualification under Merchant's analysis of a null possessor." Table 3 counterpart: "overt-possessor alternant".
- Mismatch: the stated qualification and the counterpart cell both address gate 4. The live risk is gate 1: with the possessor unpronounced, *P* may be diagnosable only through the anaphoric verb morphology that constitutes $R$, which is the circularity gate 1 exists to block. The overt alternant is what would discharge it.
- Repair: state the qualification as gate 1, and say whether the overt-possessor alternant supplies the independent diagnosis or only a paradigm neighbour.

**8. Analysis-relativity is marked asymmetrically in Table 4.**
- TFR: "Positive conditional on Kim's constructional analysis". Coordination: "Non-instance: no mediator conceals the summed features", flat, though the §2-3 footnote concedes that a closest-conjunct analysis returns an instance.
- Mismatch: a conditional positive and an unconditional negative resting on equally contested prior syntax.
- Repair: "Non-instance under a headless analysis; indeterminate where one conjunct is the head."

## Minor

**9. Bunch: complement-conditioned variation stated as a lexical property.** §2-2, "it tilts collective for inanimate aggregates but transparent for groups of people". Animacy is borne by the *of*-complement, not by *bunch*, so unlike *couple*₁/*couple*₂ this is not a sense split. Repair: describe it as complement-denotation-sensitive alternation on one lexeme.

**10. "Doesn't project" overstated from a sparse sample.** §2-2, "what it shows is that the inanimate-collective pattern doesn't project as a corpus regularity", where the reported evidence is that inanimate *bunch* is rare in subject position with a few plural tokens. Low N supports "no corpus support in this pilot", not a negative projection result. Repair: "the pilot returns no corpus support for the inanimate half."

**11. Deferred reference bearer cell.** Table 3 fills "Property, and its bearer" with "number, borne by the designatum" while §2-3 says "the *bearer* cell is empty". The designatum is a referent, not an element within $X$. Repair: "borne by the designatum, outside $X$".

**12. Obviation relation cell contains the verdict.** Table 3, Relation: "predicate tracks the head's derived feature". That is the relay diagnosis, which is the row's verdict. Repair: relation = predicate agreement (proximate/obviative); move the relay to the verdict column.

**13. "Descriptive category" spans three object types.** §7-4 lists "English number-transparent QNs" (a lexical class), "Spanish partitive subjects" (a construction), "Tsez long-distance agreement" (a phenomenon). The comparative/language-particular level is right; the sortal is loose. Repair: "language-particular categories, constructions, and patterns".

## Already controlled, no error

- Property vs bearer, relation vs diagnostic, counterpart independence: stated explicitly in §1 and held in the QN worked table.
- (\ref{ex:tfr-r-relations}c) is flagged as showing the nucleus's category rather than establishing a category-discriminating environment. Correct and unusually careful.
- "Coordination transparency" as Kim's TFR diagnostic is explicitly walled off from §2-3's verdict on coordinate NPs.
- The *bunch* corpus result is correctly separated from a grammaticality claim ("corpus absence of a constructed example isn't ungrammaticality"), apart from the overreach in item 10.
- Spanish's dispreferred singular counterpart is licensed by gate 4's own provision that a weaker counterpart is admissible if its evidential strength is stated, and §6 states it.
- Comparative concept with a language-internal control is consistent, and §6 says the control is fixed language-internally.
- Framework-internal questions (covert movement vs LDA; rival TFR analyses) are bracketed rather than adjudicated, and the schema's dependence on prior syntax is admitted as "a real limitation on the paper's central instrument".

Two items outside the audit's remit, noted only: the Tsez speaker figure ("about seven thousand") and the *mayoría*/*majority* "cognates" characterization are both factual claims worth checking against sources.

**Verdict: substantive problems.** Items 1 to 8 are genuine role and level mismatches, though every one has a local repair; none requires rebuilding the schema.
