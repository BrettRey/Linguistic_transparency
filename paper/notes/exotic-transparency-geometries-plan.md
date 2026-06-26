# Exotic transparency geometries: integration plan
Created: 2026-06-26T00:01:25Z
## Working assumption
Brett's note is best treated as a request to integrate the "exotic topology" insight into the current umbrella paper, not as a request to restart the paper around Aleut, Kayardild, or Chamorro. The current draft already has the right landing zone in Section 6, after Spanish and Tsez, where it now says genuine head-marked NP transparency is not securely attested in the gathered sources. The plan below changes that from a negative aside into a more useful typological pressure test.
## Source check
- **Aleut**: Merchant's _Aleut case matters_ has the exact missing-possessor contrast. The trigger is "missing possessor of a non-subject": ordinary overt possessor gives regular agreement, while the omitted possessor correlates with relative marking on the subject and an anaphoric verbal suffix. This is the closest item to the original head-marked NP question, but Merchant analyzes the missing element as syntactically present pro moving into a local relation with T. So the paper should call this **null-source/anaphoric subpart accessibility**, not "transparency with no structure at all." Source: Jason Merchant 2011, _Pragmatics and Autolexical Grammar_, DOI `10.1075/la.176.12mer`.
  
- **Kayardild/Lardil**: Nordlinger and Sadler explicitly describe TAM marking on nominal dependents as the reverse of ordinary agreement: properties of the clausal head are reflected on dependent NPs. Kayardild complicates the simple "copy inward" picture because clausal TAM can arise from the composite contribution of verbal and nominal marking. This supports an **inward or centripetal topology**, but the paper should not treat it as simple feature copying. Source: Rachel Nordlinger and Louisa Sadler 2004, "Tense beyond the verb: Encoding clausal tense/aspect/mood on nominal dependents," _Natural Language and Linguistic Theory_ 22:597-641.
  
- **Chamorro**: Chung's wh-agreement work gives the path case. The wh-dependency is reflected by special verbal morphology tied to the grammatical relation/case of the extracted item, and in long-distance examples multiple predicates can show the relevant morphology. The draft already says extraction is left aside, so this should be a compact topology note, not a new case study. Source: Sandra Chung 1998, _The Design of Agreement: Evidence from Chamorro_; see also Chung 2004 on restructuring and wh-agreement.
  
- **Algonquian/Kutenai obviation**: Dryer gives the useful negative control: possessed nouns can bear obviation/proximation reflecting the possessor, while the possessed noun can still trigger obviative subject marking on the verb. This looks like possessor access, but the feature has been relayed onto the head; it is better treated as **feature relay**, not transparent access.
  
## Proposed manuscript move
1. **Retitle and widen the current Section 6 cross-linguistic subsection.**
  
  Change `Two cross-linguistic cases` to something like `Cross-linguistic cases and topologies`. Keep Spanish and Tsez as the two positive worked cases already in the paper, then add a short "topological pressure tests" paragraph.
  
2. **Add a compact topology table after Tsez and before the head-marked caution.**
  
  The table should have four columns: topology, schema pressure, example, status. Suggested rows:
  
  - outward endpoint accessibility: English QNs/TFRs/Tsez; already core.
    
  - null-source subpart accessibility: Aleut missing possessor; strongest new addition, but qualified by Merchant's pro-movement analysis.
    
  - inward accessibility: Lardil/Kayardild nominal TAM/case stacking; shows that `P` can originate outside the nominal dependent.
    
  - path accessibility: Chamorro wh-agreement; extraction-side topology, acknowledged but not developed.
    
  
  Keep this as a typological map, not a claim that all four are equally established projectibility profiles.
  
3. **Revise the head-marked paragraph rather than simply reversing it.**
  
  Current wording says genuine English-style NP transparency is not securely attested and apparent positives cluster around possessors. Replace it with a sharper distinction:
  
  - If the target is **overt NP-internal dependent controls clause-level agreement while remaining inside an intact NP**, the negative caution still stands.
    
  - Aleut shows a different and more interesting positive: **a recoverable but unpronounced possessor subpart can condition clause-level morphology**.
    
  - Therefore the paper should stop saying "no genuine head-marked NP transparency" without qualification; it should say the gathered sources separate overt intact-NP transparency from null/anaphoric possessor accessibility.
    
4. **Lightly revise the schema exposition in Section 6 and conclusion.**
  
  The draft sometimes paraphrases the schema as "an internal property escaping a mediator." That is fine for the core cases but too narrow after Kayardild and Chamorro. The durable version is: a property associated with, recoverable through, or distributed along a mediated configuration remains available to a relation that the mediator could otherwise have blocked or localized.
  
5. **Keep Section 2 stable.**
  
  Do not import Aleut/Kayardild/Chamorro into the main morphosyntactic-profile section. Section 2 is the delivered English result; Section 6 is the comparative-concept discipline and typological pressure-test zone.
  
6. **Add sources and source notes.**
  
  Add BibTeX entries for Merchant 2011, Nordlinger and Sadler 2004, Chung 1998, and probably Dryer 1992 if the feature-relay boundary case is mentioned. Add short source notes under `paper/sources/source-notes.md`. If possible, save accessible PDFs alongside the existing head-marked source folder, but do not block the prose edit on every PDF if reliable publisher pages/author PDFs are already verified.
  
7. **Verification after edits.**
  
  Run the house style check if available, `git diff --check`, and `make quick` or `make -B` depending on edit size. Expect current uncommitted changes in `DECISIONS.md`, `STATUS.md`, `main.pdf`, `paper/sections/06-typological-transparency.tex`, `paper/sources/source-notes.md`, `references-local.bib`, and `paper/sources/head-marked-transparency/`; preserve them.
  
## Proposed text-level thesis
The addition should make one new claim:

> The umbrella schema is not just an outward-access schema. Its values can be arranged as accessibility topologies: outward endpoint access, inward concord-like access, path-distributed access, and null-source anaphoric access. Those topologies do not collapse into one descriptive category, but they explain why the same comparative-concept question keeps reappearing in typologically distant systems.
## Open decisions for Brett
- {==Should Aleut become a named positive case in the main text==}{>>yes<<}{id="c1" by="user" at="2026-06-26T00:04:58.605Z"}, or only a pressure-test paragraph? My recommendation: named positive, but with the pro-movement qualification.
  
- Should Chamorro stay in a footnote because extraction is explicitly out of scope? My recommendation: {==one table row plus one sentence; no full example==}{>>agreed<<}{id="c2" by="user" at="2026-06-26T00:05:16.736Z"}.
  
- {==Should Kayardild be described under "case stacking/Suffixaufnahme" or under "nominal TAM"?==}{>>Are these very generative-centric analysises? Are the simpler ways to look at it?<<}{id="c3" by="user" at="2026-06-26T00:05:44.626Z"} My recommendation: lead with nominal TAM/case stacking and avoid making Suffixaufnahme carry more than it should.

---
comments:
  c4:
    body: map each of these explicitly into our X–P–R slots with falsification
      conditions (in the §2.3 sense).
    by: user
    at: 2026-06-26T00:06:52.949Z
