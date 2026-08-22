# Publication-gate passes 2--7: execution plan
<!-- SUMMARY: Approved execution plan for publication-gate passes 2--7 on the umbrella and TFR companion papers · status: approved · updated: 2026-08-22 -->

## Scope and exclusions

Run the requested publication-gate work on both current manuscripts:

- umbrella: `main.tex` plus all included sections and appendices;
- companion: `two-kinds.tex` only, not the other LaTeX roots in its repository.

External-review triage and the email draft are excluded at Brett's request. No commits, pushes, corpus queries, or new empirical claims are authorized by these passes.

The current manuscripts control where the April project brief has been superseded by later source work and co-author decisions. In particular, the umbrella now treats QNs as the principal demonstrated profile, TFRs as conditional and analysis-relative, and the form--meaning cases as boundary applications. A pass may clarify or align those claims but may not silently restore the brief's broader local-kind thesis.

Baseline: umbrella 33 pages and 15,266 board-count words; companion 12 pages and 5,060 `texcount` words (`passes.py` currently counts the wrong root in the multi-root companion repository). Both PDFs build cleanly before these passes.

## Ordered work

### 1. Contribution alignment

Read title, abstract, keywords, introduction, headings, and conclusion first, then compare them with the bodies. Check both papers separately and as a two-paper set. Apply local alignment fixes. Stop for review if alignment would require choosing a different central contribution.

Artifacts:

- umbrella `notes/passes/2026-08-22-contribution-alignment.md`;
- companion `notes/passes/2026-08-22-contribution-alignment.md`.

### 2. Conceptual and scholarly-engagement audits

Run and report:

- projectibility: explicit source, target, population, warrant, revision rule, and strongest supported world-side commitment;
- level/category: relation versus diagnostic, corpus distribution versus grammar, comparative concept versus language-particular category, profile versus mechanism/stabilizer;
- terminology: trace each local contrast through the whole text and across the pair;
- charitable engagement: source-checked characterizations of Haspelmath, Newmeyer, Leufkens, Slater, Khalidi, Boyd, Grosu, Wilder, van Riemsdijk, and Kim where criticised or contrasted.

Apply local repairs that preserve the existing claim. Put any change to the central projectibility claim or to a rival's substantive characterization into the later Roughdraft cohesion review before applying it.

### 3. Evidence audits

Run a complete numerical inventory of manuscript statistics, counts, percentages, totals, and derived comparisons. An independent second model will compare the inventory with the archived corpus files; its output remains a candidate and will be checked row-for-row locally before any result is accepted. Record the auditing model in the report and disclosure if it is not already listed.

Also:

- check every table value and caption against the prose and source archive;
- audit negative and novelty claims, narrowing or cutting unevidenced claims;
- verify every source quotation verbatim and resolve its page from the local source;
- reread the three-to-eight load-bearing sources for each paper;
- validate every citation key and cited entry, including the local working-paper entry and bibliography symlink.

The manuscripts contain tables but no data figures or conceptual diagrams. If a final source scan confirms that, record the registered figures pass as not applicable and retain table QA under the numbers/render audits.

### 4. Coherence, cohesion, and reader pass

Map one question and result per section, then read both manuscripts straight through in order. Use a sliding three-paragraph window to identify broken joins, ambiguous antecedents, duplicated verdicts, late definitions, and promises no longer kept.

Because the registered cohesion procedure requires approval before flow edits, prepare one companion Markdown review file with the proposed exact edits in Roughdraft CriticMarkup. After Brett clicks Done Reviewing, apply accepted changes to the `.tex` sources. This is the second checkpoint, for the separate cohesion stage; the present checkpoint approves only the audit plan.

### 5. Final mechanics

After all accepted source edits:

- repeat the read-only proofreading audit on both exact texts;
- repeat editorial-scar, house-style, terminology, quotation, and bibliography checks;
- rebuild with XeLaTeX/Biber until stable;
- scan logs for unresolved citations/references and overfull boxes;
- render and inspect every PDF page, especially tables, floats, headings, and front matter;
- rerun word/page counts, manuscript inventory, stale-term searches, and `git diff --check`;
- update pass artifacts and record only genuinely completed passes against the correct manuscript root.

The companion's multi-root ledger defect will not be worked around by recording against `sem-syn.tex`; its dated artifacts will remain authoritative unless a safe `two-kinds.tex` pin is confirmed.

## Edit boundary

Directly apply corrections whose right answer follows from the manuscript or archive: mismatched counts, stale terminology, broken cross-references, unsupported scope wording, duplicated verdicts, ambiguous antecedents, and mechanical faults. Do not invent examples, sources, data, or theoretical resolutions. Leave genuinely unresolved empirical or co-author decisions explicit.
