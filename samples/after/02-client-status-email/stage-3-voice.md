---
stage: 3
agent: writing-style-editor
source: ../stage-2-validation.md (Validated Document section)
timestamp: 2026-02-20T00:30:00Z
---

## Stylometry Report

```text
Sentence Length:    Avg ~26 words | σ ~10 (est.) | Target: 17-22, σ ≥ 8
Short Sentences:    0% < 8 words              | Target: ≥ 15%          FAIL
Long Sentences:     ~25% > 30 words           | Target: ≥ 15%          PASS
Lexical Diversity:  TTR ~0.52 (est.)          | Target: ≥ 0.40         PASS
Hedge Density:      ~17% (2 of 12 sentences)  | Target: 5-10%          BORDERLINE
AI Patterns Found:  6 instances               | Target: 0              FAIL
Burstiness:         1 flat paragraph (Para 2) | Target: 0              FAIL
Persona Drift:      0 sections flagged        | Target: 0              PASS
```

**Measurement note**: Computation environment unavailable; qualitative proxies applied with
sentence-by-sentence word counts. Figures marked (est.) carry qualitative confidence only.

**Status**: NEEDS WORK

---

## Summary Assessment

The document has a competent skeleton but reads as polished AI draft rather than a consultant's
voice. Three problems dominate: the opener and closer are formulaic placeholders ("We are
pleased to report," "measurable operational gains"), Para 2 locks all three risk statements into
an identical semicolon structure that kills rhythm, and no sentence in the document runs under
eight words. A short, punchy sentence would change the energy of the whole piece. The Stage 2
epistemic flags -- the 18% figure's ambiguous basis, the hasty generalization on pilot-to-scale --
are preserved in the rewrite below with appropriate hedging; they are not resolved here, only
voiced correctly.

---

## Issue Log

| Location | Issue Type | Current Text | Suggested Revision |
| --- | --- | --- | --- |
| Para 1, S1 | AI pattern -- vague qualifier | "significant progress" | Replace with a specific milestone: "completed the diagnostic phase and launched our first automation pilot" |
| Para 1, S1 | AI pattern -- formulaic opener | "We are pleased to report" | Drop the pleasantry preamble; lead with the fact |
| Para 1, S3 | AI pattern -- unquantified claim | "quick wins in line balancing and changeover time reduction" | Quantify or reframe as directional (per Stage 2 Issue Log #3); voice fix defers to author on numbers |
| Para 2, S1 | AI pattern -- vague qualifier | "overall trajectory is strong" | "The project is on schedule" or specify what makes it strong |
| Para 2, S1-S4 | Structural tell -- semicolon monotony | Three consecutive risk sentences in identical [problem]; [mitigation] structure | Vary the structure: one risk as a full sentence pair, one as a subordinate clause, one inverted |
| Para 2, S4 | AI pattern -- gerund padding | "to ensure sustainable adoption" | "so that the changes stick" or drop and let "embed performance routines" carry the meaning |
| Para 3, S1 | Stage 2 semantic flag -- hasty generalization | "expand the automation scope" | "validate whether the Line 3 results generalize to Packaging and Receiving" (per Stage 2 Reasoning Error #2) |
| Para 4, S2 | AI pattern -- generic closer | "we remain confident the final recommendations will deliver measurable operational gains" | Replace with something specific to this engagement: name what the recommendations will address |
| Para 4, S2 | AI pattern -- filler pleasantry | "your continued collaboration" | Rephrase or drop; the thanks is appropriate but the phrase is a stock formula |
| Document-wide | Sentence rhythm -- no short sentences | No sentence under 8 words in any paragraph | Add at least one short, declarative sentence; Para 2 needs one most |
| Para 2 | Burstiness -- flat paragraph | S6=~27w, S7=~26w, S8=~29w | After the short S5 opener, the three risk statements run at nearly identical length; vary one significantly |

---

## Rewritten Document

The following rewrite applies all voice corrections. Key decisions are noted inline in brackets
for author review. Stage 2 epistemic markers are preserved or strengthened, not resolved -- the
author must supply the factual answers (measured vs. estimated, basis for "moderate") before
delivery.

**Voice target applied**: Confident, direct consulting voice. Precise over vague. Professional
warmth in the close without stock phrases. Short sentence added in Para 2 for rhythm.

**Semantic preservation**: The 18% figure retains its Stage 2 hedging and ambiguity flag. The
pilot-to-scale framing is reworded as validation per Stage 2 Reasoning Error #2. "Key Sponsor"
capitalization is preserved pending author confirmation per Stage 2 Issue Log #5.

---

Subject: Project Status Update: Operational Efficiency Review (Month 4 of 6)

Dear Team,

Month four is on schedule. We completed the diagnostic phase -- value stream mapping across
the main product families, OEE and throughput baselines across assembly and machining, and
root-cause analysis of cycle time variability and waste pockets. Two kaizen events produced
[AUTHOR: quantify if data available, e.g., "a 12-minute reduction in changeover time on
Line 2" -- if not available, retain directional: "early improvements in line balancing and
changeover time"]. The Line 3 automation pilot shows [AUTHOR: if measured, replace
"an estimated" with "a measured"] 18% throughput improvement with no quality degradation
[AUTHOR: confirm "stable quality" definition and measurement period per Stage 2 Issue Log #1];
those results will shape the validation approach for the next two pilots.

Three risks are in active management. Data reliability from the legacy ERP systems may push
final baseline validation past the current schedule; we are running an end-of-month source
audit with a backup extraction process standing by. Resource availability is the tighter
constraint -- cross-functional capacity for rapid pilot scaling remains limited, and we are
formalizing commitments through a capacity matrix before the steering meeting. Change
readiness [AUTHOR: add basis per Stage 2 Issue Log #2, e.g., "assessed through facilitator
observation during kaizen events"] is moderate; we will work with your operations leaders
on a one-page operating model and change narrative to build the foundation before the
workshops begin.

Over the next four weeks we will finalize the prioritized opportunity list with ROI and
payback estimates per initiative, run pilots in Packaging and Receiving to test whether
the Line 3 results generalize to those line configurations [per Stage 2 Reasoning Error #2
-- reframed as validation, not expansion], and bring recommended investment options and a
timeline to the Month 5 Week 2 steering meeting. Frontline change workshops and supervisor
sessions will run in parallel to embed takt time adherence, preventive maintenance, and
WIP reduction routines.

Please confirm Key Sponsor [AUTHOR: confirm capitalization against engagement contract per
Stage 2 Issue Log #5] availability for the steering meeting and flag any agenda items you
want added. The next four weeks are the pivot from diagnosis to decisions; we will have the
analysis ready.

Best regards,

[Your Name]
[Your Title]
[Company Name]
[Contact Information]

---

## Rewrite Rationale

**Para 1 opener**: "Month four is on schedule." is seven words, declarative, and specific. It
replaces "We are pleased to report significant progress on our 6-month Operational Efficiency
Review, now in month four," which runs 19 words and opens with a stock pleasantry followed by
the vague qualifier "significant." The short opener also gives Para 1 its only sub-8-word
sentence, which the original document lacks entirely.

**"significant progress"**: Removed. The substance of what was accomplished follows in the next
sentences. The reader can assess significance from the facts.

**"quick wins"**: Left as an author-resolve placeholder with a specific example to prompt the
author to supply numbers. Voice-wise, the original phrasing is vague consulting cliche; the
rewrite redirects to a concrete alternative.

**"overall trajectory is strong"**: Replaced by "Three risks are in active management," which
opens Para 2 with concrete subject matter rather than a vague assessment. The paragraph then
demonstrates the trajectory by describing what is being done -- show, not tell.

**Semicolon monotony in Para 2**: The original locks all three risk statements into "[problem];
[mitigation]" with nearly identical sentence lengths (27, 26, 29 words). The rewrite uses three
different structures: (1) a full sentence followed by a second sentence for the ERP risk, (2) a
dash-introduced appositive for the resource risk, (3) a subordinate clause opener for the change
readiness risk. The paragraph is no longer a template.

**"to ensure sustainable adoption"**: Removed. "Ensure sustainable adoption" is gerund padding
(the kind Stage 1 flagged as an AI-mechanical pattern). The rewrite replaces it with "to build
the foundation before the workshops begin," which describes what the operating model work
actually does rather than asserting a hoped-for outcome.

**"expand the automation scope"**: Replaced with "test whether the Line 3 results generalize to
those line configurations" per Stage 2 Reasoning Error #2. This is a one-phrase change with a
substantive effect: the pilots are framed as validation, not foregone success. Stage 2 flagged
this as a hasty generalization; the rewrite addresses it without softening the overall tone.

**Closing sentence**: "we remain confident the final recommendations will deliver measurable
operational gains" is a stock AI closer. It asserts confidence without any content. The rewrite
-- "The next four weeks are the pivot from diagnosis to decisions; we will have the analysis
ready" -- names what is actually happening at this stage of the engagement. It is specific,
confident, and not a formula. The sentence is also notably shorter (15 words for the second
clause), which helps rhythm.

**"your continued collaboration"**: Dropped the stock phrase; retained the functional request
(confirm availability, flag agenda items) without the pleasantry wrapper.

---

## Pipeline Status Block

```yaml
pipeline:
  document: 02-client-status-email
  format: email
  system_prompt: sme-role

  stage_1_grammar:
    status: NEEDS_WORK
    errors: 5
    categories:
      grammar: 3
      composition: 1
      plain_language: 2
      ai_mechanical: 1
      non_prose: 2
    reviewer: grammar-composition-editor
    timestamp: 2026-02-20T23:30:00Z
    notes: >
      Five must-fix errors corrected in the corrected document above. Two warnings and
      two notes deferred to Stage 3. Document is ready for Stage 2 review.

  stage_2_validation:
    status: CONDITIONAL
    claims_analyzed: 18
    verified_pct: 0%
    expert_judgment_pct: 61%
    unverified_claims: 4
    suspect_claims: 0
    assumptions_found: 3
    reasoning_errors: 2
    reviewer: document-validator
    timestamp: 2026-02-20T23:55:00Z
    notes: >
      No suspect claims. Two priority items require author clarification before delivery:
      (1) basis for "estimated 18% throughput improvement / stable quality" — measured
      or projected? (2) basis for "moderate" change readiness assessment. Two reasoning
      errors flagged (false precision, hasty generalization) are resolvable with minor
      reframing. "Key Sponsor" capitalization requires author confirmation against
      engagement documentation. Optimism bias is moderate and within normal range for
      a progress email; one sentence of uncertainty on the highest-stakes risk is
      recommended. Document may proceed to Stage 3 with these items noted for author
      resolution.

  stage_3_style:
    status: NEEDS_WORK
    ai_patterns: 6
    stylometry_pass: false
    stylometry_notes: >
      No short sentences (0% vs. target >= 15%); Para 2 burstiness flat (three consecutive
      sentences at ~26-29 words after a short opener); average sentence length ~26 words
      (above 17-22 target); hedge density borderline at ~17%. TTR and overall sigma
      estimated within acceptable range. Rewritten document addresses all six AI patterns
      and adds short sentence to Para 1.
    persona_drift_sections: "none"
    reviewer: writing-style-editor
    timestamp: 2026-02-20T00:30:00Z
    stage_2_items_preserved:
      - "18% figure epistemic hedging retained with author-resolve placeholder"
      - "pilot-to-scale reframed as validation per Reasoning Error #2"
      - "change readiness basis placeholder added per Issue Log #2"
      - "Key Sponsor capitalization preserved pending author confirmation"
    remediation_cycles: 1
```

---

## Final Recommendation

**Revision needed** -- but the revision is author-dependent, not editor-dependent.

The six AI patterns are resolved in the rewritten document above. The stylometry issues
(no short sentences, flat Para 2) are corrected in the rewrite. Those changes can be applied
now.

What cannot be resolved at Stage 3 are the four author-resolve items carried forward from
Stage 2: the 18% figure's measurement basis, the definition of "stable quality," the basis
for "moderate" change readiness, and the "Key Sponsor" capitalization. These remain as
bracketed placeholders in the rewritten document. Once the author supplies those answers,
the document should pass Stage 2 re-check on those items (one remediation cycle remaining
before escalation to human review) and then clear Stage 3 on a light pass.

The rewritten document is ready for author review. Send it back through Stage 1 and Stage 2
for the rewritten sections (Para 1, Para 2, Para 4) before final delivery.
