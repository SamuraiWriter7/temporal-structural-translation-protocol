# Changelog

All notable changes to this project will be documented in this file.

The project follows an experimental protocol-development lifecycle.

---

## [0.5.0-candidate] - 2026-07-10

### Added

* Initial Temporal Causality Receipt specification.
* JSON Schema for bounded and auditable temporal causal claims.
* Example YAML causality receipt.
* Causal claim scope representation.
* Temporal claim-range representation.
* Outcome reference binding.
* Causal claim classification:

  * contributory,
  * enabling,
  * constraining,
  * mediating,
  * triggering,
  * necessary_candidate,
  * sufficient_candidate,
  * joint_contribution,
  * other.
* Claim strength classification.
* Claim status classification.
* Mechanism summary field.
* Claim scope notes.
* Evidence binding layer.
* Evidence type classification:

  * state evidence,
  * transition evidence,
  * precedence evidence,
  * translation evidence,
  * trace evidence,
  * external evidence,
  * human testimony,
  * telemetry,
  * intervention evidence,
  * counterfactual evidence,
  * other.
* Evidence support-direction classification.
* Evidence relevance classification.
* Evidence-binding confidence.
* Overall evidence completeness classification.
* Alternative explanation records.
* Alternative plausibility classification.
* Alternative explanation status tracking.
* Counterevidence records.
* Counterevidence severity classification.
* Counterevidence resolution tracking.
* Explicit causal scope boundaries.
* Permitted claim declarations.
* Prohibited inference declarations.
* Generalization status classification.
* Overall causal assessment.
* Evidence sufficiency assessment.
* Alternative explanation assessment.
* Recommended next-action classification.
* Human causal review layer.
* Review outcome classification.
* Receipt finality states.
* Receipt supersession support.
* Trace references for receipt auditability.
* Updated validation script for v0.1 through v0.5.

### Changed

* Protocol model expanded from cross-agent temporal translation to bounded causal claim auditing.
* Validation now covers:

  * Temporal State Record,
  * State Transition Map,
  * Structural Precedence Graph,
  * Cross-Agent Temporal Translation,
  * Temporal Causality Receipt.
* README updated to mark the first protocol arc as complete.
* Protocol lifecycle now spans:

  * state observation,
  * change mapping,
  * precedence analysis,
  * cross-agent translation,
  * causal claim auditing.

### Design Boundary

v0.5 may record and assess bounded causal claims.

It does not treat the following as automatic proof of causality:

* temporal precedence,
* structural precedence,
* translation,
* correlation,
* handoff acceptance,
* trace continuity,
* absence of counterevidence.

A Temporal Causality Receipt may express:

* contribution,
* enabling conditions,
* constraints,
* mediation,
* triggering relationships,
* candidate necessity,
* candidate sufficiency,
* joint contribution.

Claims of necessity or sufficiency require evidence beyond simple temporal ordering.

### First Arc Complete

```text
v0.1  State
v0.2  Change
v0.3  Precedence
v0.4  Translation
v0.5  Causality Receipt
```

The first arc establishes a model-independent temporal structural translation and causal audit lifecycle.

---

## [0.4.0-candidate] - 2026-07-10

### Added

* Initial Cross-Agent Temporal Translation specification.
* JSON Schema for model-independent temporal structural translation between heterogeneous agents.
* Example YAML cross-agent translation record.
* Source and target agent context representation.
* Agent-local clock context representation.
* Representation-profile metadata.
* Translation contract layer.
* Translation mode classification.
* Required preservation declarations.
* Allowed transformation declarations.
* Prohibited transformation declarations.
* Explicit protection against:

  * origin removal,
  * uncertainty suppression,
  * evidence detachment,
  * precedence inversion,
  * unsupported unresolved-to-resolved conversion,
  * causal claim inflation,
  * human gate bypass.
* Temporal alignment layer.
* Cross-clock alignment pair representation.
* Alignment mode classification.
* Alignment relation classification:

  * corresponds_to,
  * precedes,
  * follows,
  * overlaps,
  * contains,
  * derived_alignment,
  * unknown.
* Ordering preservation classification.
* Alignment confidence.
* State mapping layer.
* Structure mapping layer.
* Precedence mapping layer.
* State mapping patterns:

  * one_to_one,
  * one_to_many,
  * many_to_one,
  * many_to_many,
  * partial.
* Preservation-status classification:

  * identity_preserved,
  * meaning_preserved,
  * function_preserved,
  * partially_preserved,
  * intentionally_transformed,
  * not_preserved,
  * unknown.
* Continuity transfer layer.
* Explicit transfer support for:

  * unresolved items,
  * continuity candidates,
  * constraints,
  * verification requests,
  * human review requests.
* Deferred continuity item representation.
* Rejected continuity item representation.
* Translation loss records.
* Translation loss type classification.
* Translation loss severity classification.
* Translation loss mitigation records.
* Handoff package representation.
* Delivery status tracking.
* Acceptance status tracking.
* Explicit causal-claim prohibition within the v0.4 audit boundary.
* Updated validation script for v0.1 through v0.4.

### Changed

* Protocol model expanded from single-system temporal lineage analysis to cross-agent temporal structural interoperability.
* Validation now covers:

  * Temporal State Record,
  * State Transition Map,
  * Structural Precedence Graph,
  * Cross-Agent Temporal Translation.
* README roadmap updated to mark v0.4 as implemented.

### Design Boundary

v0.4 represents temporal and structural translation across heterogeneous agent contexts.

It may describe:

* source and target agent roles,
* local clock contexts,
* temporal alignment,
* state mappings,
* structure mappings,
* precedence mappings,
* continuity transfer,
* translation loss,
* handoff package delivery,
* handoff acceptance.

v0.4 does not establish:

* internal-state identity,
* synchronized agent clocks,
* semantic equivalence unless explicitly evidenced,
* causal necessity,
* causal sufficiency,
* causal responsibility,
* intervention-based causal proof,
* counterfactual causal proof.

Final causal synthesis is reserved for v0.5.

---

## [0.3.0-candidate] - 2026-07-10

### Added

* Initial Structural Precedence Graph specification.
* JSON Schema for temporal and structural precedence representation.
* Example YAML precedence graph.
* Graph scope representation.
* Scope types for:

  * single transition,
  * multi-transition analysis,
  * lifecycle segments,
  * cross-agent analysis,
  * cross-system analysis.
* Structural node representation.
* Temporal node positioning.
* Logical time support.
* Sequence index support.
* Observation timestamp support.
* Local clock identifier placeholder for later cross-agent alignment.
* Directed precedence edges.
* Precedence relation classification:

  * temporally_precedes,
  * structurally_prepares,
  * contextually_frames,
  * constrains,
  * enables,
  * is_inherited_by,
  * is_refined_into,
  * is_reinterpreted_as,
  * remains_unresolved_before,
  * is_handed_forward_to,
  * other.
* Precedence basis classification.
* Edge strength classification.
* Edge-level confidence.
* Explicit causal-status boundary:

  * not_claimed,
  * candidate,
  * requires_review.
* Multi-node path observations.
* Path classification:

  * developmental,
  * constraint,
  * inheritance,
  * translation,
  * unresolved continuity,
  * mixed,
  * other.
* Graph-level precedence findings.
* Unresolved precedence question tracking.
* Candidate causal path references.
* Updated validation script for v0.1, v0.2, and v0.3.

### Changed

* Protocol model expanded from state comparison to structural lineage analysis.
* Validation now covers:

  * Temporal State Record,
  * State Transition Map,
  * Structural Precedence Graph.
* README roadmap updated to mark v0.3 as implemented.

### Design Boundary

v0.3 represents structural precedence.

It may describe:

* temporal ordering,
* structural preparation,
* contextual framing,
* constraint relations,
* enabling relations,
* inheritance,
* refinement,
* reinterpretation,
* unresolved continuity,
* forward handoff precedence.

v0.3 does not treat precedence alone as proof of causality.

The following remain outside the scope of v0.3:

* causal necessity,
* causal sufficiency,
* intervention-based causal proof,
* counterfactual causal testing,
* cross-agent semantic equivalence,
* cross-agent temporal alignment,
* synchronized clocks,
* final temporal causality receipts.

---

## [0.2.0-candidate] - 2026-07-10

### Added

* Initial State Transition Map specification.
* JSON Schema for structural change mapping between temporal states.
* Example YAML transition map.
* Explicit source state references.
* Explicit target state references.
* Transition window representation.
* Logical interval representation.
* Optional duration metadata.
* Trigger context representation.
* Trigger type classification.
* Trigger claim-scope boundary.
* Six structural change classes:

  * introduced,
  * preserved,
  * transformed,
  * retired,
  * split,
  * merged.
* Preservation-level classification.
* Transformation operation classification.
* Meaning-retention indicator.
* Retirement classification.
* Split transformation representation.
* Merge transformation representation.
* Continuity candidate resolution.
* Open continuity candidate tracking.
* Transition observation confidence.
* Comparison method metadata.
* Evidence references.
* Explicit observation limitations.
* Updated validation script for v0.1 and v0.2 records.

### Changed

* Validation now covers:

  * Temporal State Record,
  * State Transition Map.
* README roadmap updated to mark v0.2 as implemented.
* Temporal sequence model expanded from isolated state observation to state-to-state structural comparison.

### Design Boundary

v0.2 maps structural change between two temporal state records.

It may record:

* structures that appeared,
* structures that persisted,
* structures that transformed,
* structures that were retired,
* structures that split,
* structures that merged,
* continuity intentions that were resolved.

v0.2 does not establish:

* causal proof,
* causal necessity,
* causal sufficiency,
* long-range precedence,
* cross-agent temporal equivalence,
* synchronized agent clocks,
* temporal causality receipts.

Trigger context remains descriptive unless later layers provide stronger evidence.

---

## [0.1.0-candidate] - 2026-07-10

### Added

* Initial Temporal State Record specification.
* JSON Schema for model-independent temporal state representation.
* Example YAML Temporal State Record.
* Subject identity representation.
* Subject role representation.
* Implementation metadata.
* Temporal context fields:

  * sequence index,
  * logical time,
  * previous state reference,
  * lifecycle phase.
* State snapshot representation.
* Active structure records.
* Structure activation classification.
* Change-readiness classification.
* Origin references.
* Trace references.
* Unresolved item representation.
* Unresolved status classification.
* Blocking reason support.
* Structural dependency representation.
* Dependency relation classification.
* Continuity candidate representation.
* Continuity intent classification:

  * preserve,
  * revisit,
  * transform,
  * verify,
  * handoff,
  * retire.
* Observation basis classification.
* Observation confidence.
* Evidence references.
* Explicit observation limitations.
* Human review metadata.
* Audit metadata.
* Python validation script.
* GitHub Actions validation workflow.

### Design Boundary

v0.1 records an externally representable structural state at a temporal position.

It does not define:

* state transition semantics,
* causal transformation claims,
* temporal precedence graphs,
* cross-agent clock synchronization,
* cross-agent temporal translation,
* temporal causality receipts.

These capabilities are introduced in later versions.

---

# First Arc Summary

```text
v0.1 — Temporal State Record

State
What exists?
```

```text
v0.2 — State Transition Map

Change
What changed?
```

```text
v0.3 — Structural Precedence Graph

Precedence
What structurally came before what?
```

```text
v0.4 — Cross-Agent Temporal Translation

Translation
What crossed the agent boundary,
and what was preserved, transformed, or lost?
```

```text
v0.5 — Temporal Causality Receipt

Causal Audit
What bounded causal claims can be supported,
with what evidence and limitations?
```

Lifecycle:

```text
Observe State
      ↓
Map Change
      ↓
Trace Precedence
      ↓
Translate Across Agents
      ↓
Audit Causal Claims
```

The first arc establishes a model-independent foundation for temporal structural translation, cross-agent continuity, and bounded causal audit.
