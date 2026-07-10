# Temporal Structural Translation Protocol

A model-independent protocol for representing temporal structural states, mapping state transitions, tracing structural precedence, translating continuity across heterogeneous agents, and auditing bounded causal claims.

---

## Overview

AI systems increasingly operate through:

* multiple models,
* specialized agents,
* distributed wings,
* persistent memory,
* iterative reasoning,
* tool execution,
* verification loops,
* human review,
* and cross-system handoffs.

These systems can exchange outputs, but output exchange alone does not explain:

* what structures existed before an action,
* what changed between states,
* what remained unresolved,
* what structurally preceded a later development,
* what was translated between agents,
* what meaning was preserved or lost,
* or how far a causal claim can reasonably extend.

The **Temporal Structural Translation Protocol** defines a model-independent record layer for these problems.

The first protocol arc develops through five layers:

```text
v0.1  Temporal State Record
v0.2  State Transition Map
v0.3  Structural Precedence Graph
v0.4  Cross-Agent Temporal Translation
v0.5  Temporal Causality Receipt
```

Together:

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

---

## Design Principle

The protocol does not attempt to expose:

* raw hidden activations,
* private chain-of-thought,
* undocumented internal reasoning,
* or complete mechanistic access to a model.

Instead, it records **observable, declared, externally representable, or evidence-backed structural states and relations**.

The basic boundary is:

```text
Raw Hidden State
        ✕
Private Chain-of-Thought
        ✕

Observable Structural State
        ○
Representable Transition
        ○
Auditable Precedence
        ○
Explicit Translation Record
        ○
Bounded Causal Claim
        ○
```

The purpose is not to reveal everything inside an AI system.

The purpose is to make temporal structural evolution **comparable, translatable, and auditable**.

---

# First Arc

## v0.1 — Temporal State Record

A Temporal State Record represents an observable or externally representable structural state at a specific temporal position.

It answers:

```text
What structures are active?
What remains unresolved?
What dependencies exist?
What may continue forward?
How was this state observed?
What are the limitations of that observation?
```

The minimum model is:

```text
State(t)
```

A record contains:

```text
Temporal State Record
├── identity
├── subject
├── temporal context
├── state snapshot
│   ├── active structures
│   ├── unresolved items
│   ├── dependencies
│   └── continuity candidates
├── observation
└── audit
```

---

## Temporal Context

Each state may include:

* sequence index,
* logical time,
* previous state reference,
* lifecycle phase,
* observation timestamp.

Example:

```yaml
temporal_context:
  sequence_index: 0
  logical_time: "t0"
  previous_state_record_id: null
  phase: translation
```

Chronological time and logical sequence are intentionally separated.

This supports systems where:

* agents operate asynchronously,
* event order differs from wall-clock order,
* distributed observations are later aligned,
* or local clocks have different meanings.

---

## Active Structures

An active structure is a representable structural unit relevant to the current state.

Examples include:

* hypotheses,
* goals,
* constraints,
* interpretations,
* plans,
* conflicts,
* questions,
* dependencies,
* verification targets.

Each active structure may indicate:

* activation level,
* stability,
* origin references,
* trace references.

---

## Unresolved Items

Temporal continuity requires more than preserving completed outputs.

Systems may also need to retain:

* open questions,
* contradictions,
* blocked work,
* deferred issues,
* uncertainty,
* unresolved conflicts.

The `unresolved_items` field keeps these explicit.

A later transition must not silently convert:

```text
unresolved
    ↓
resolved
```

without appropriate evidence or an explicit transformation record.

---

## Dependencies

A state may contain structural dependencies such as:

```text
supports
constrains
requires
conflicts_with
refines
derived_from
```

These relations provide the foundation for later transition and precedence analysis.

---

## Continuity Candidates

A continuity candidate expresses intended treatment of a structure in later states.

Supported intents include:

```text
preserve
revisit
transform
verify
handoff
retire
```

A continuity candidate does not itself perform a transition.

It records forward structural intent.

---

## Observation Boundary

Each state record declares an observation basis.

Examples include:

```text
self_report
trace_inference
telemetry
external_observation
hybrid
```

A state record also carries:

* confidence,
* evidence references,
* limitations.

This prevents a structural state abstraction from being mistaken for complete access to an AI system's private internal process.

---

# v0.2 — State Transition Map

A State Transition Map represents observable or declared structural differences between two Temporal State Records.

The minimum model is:

```text
Temporal State Record(t)
        ↓
State Transition Map
        ↓
Temporal State Record(t+1)
```

It answers:

```text
What appeared?
What persisted?
What changed?
What disappeared?
What split?
What merged?
What continuity intentions were resolved?
```

---

## Change Classes

v0.2 defines six primary change classes.

### Introduced

A structure appears in the target state without a mapped predecessor.

```text
∅ → D
```

### Preserved

A structure continues across states.

```text
A → A
```

Preservation may refer to:

* identity,
* meaning,
* function,
* partial continuity.

### Transformed

A structure changes representation, scope, interpretation, priority, constraint, confidence, or function.

```text
B → B2
```

Possible transformation operations include:

```text
refinement
generalization
specialization
reinterpretation
translation
compression
expansion
reordering
constraint_update
confidence_update
```

### Retired

A source structure does not continue into the target state.

```text
C → ∅
```

Retirement may be classified as:

```text
resolved
superseded
rejected
expired
deprioritized
lost
unknown
```

### Split

One source structure becomes multiple target structures.

```text
A
├── A1
└── A2
```

### Merged

Multiple source structures are integrated into one target structure.

```text
A ─┐
   ├── C
B ─┘
```

---

## Trigger Context

A transition may include trigger context such as:

```text
external_input
internal_update
tool_result
agent_handoff
human_feedback
scheduled_pulse
verification_result
environment_change
compound
unknown
```

The protocol explicitly distinguishes:

```text
Trigger Context
        ≠
Causal Proof
```

For example:

```yaml
trigger_context:
  trigger_type: human_feedback
  trigger_claim_scope: context_only
```

means:

> Human feedback occurred within the transition context.

It does not mean:

> Human feedback caused every mapped change.

---

## Continuity Resolution

v0.1 defines continuity candidates.

v0.2 records what happened to them.

Possible resolutions include:

```text
preserved
revisited
transformed
verified
handed_off
retired
```

Or they may remain:

```text
open
deferred
blocked
unknown
```

This creates continuity between state representation and later cross-agent handoff.

---

# v0.3 — Structural Precedence Graph

A Structural Precedence Graph represents ordered structural relationships across temporal states.

It asks:

```text
What existed before a later structure?
What prepared a later structure?
What provided its context?
What constrained it?
What enabled it?
What was inherited?
What was refined?
What remained unresolved before a later development?
```

The protocol makes an explicit distinction:

```text
Precedence
    ≠
Causality
```

A structure may precede another because it:

* existed earlier,
* provided context,
* constrained available options,
* enabled later interpretation,
* was inherited,
* was refined,
* was reinterpreted,
* or was handed forward.

None of these relations automatically proves causation.

---

## Graph Model

A Structural Precedence Graph contains:

```text
Structural Precedence Graph
├── graph scope
├── nodes
├── edges
├── path observations
├── graph summary
├── observation metadata
└── audit
```

---

## Nodes

Nodes may represent:

```text
origin
active_structure
unresolved_item
transition_result
trace
constraint
context
handoff_input
handoff_output
other
```

Each node may reference:

* sequence index,
* logical time,
* observation timestamp,
* local clock ID,
* state records,
* traces,
* origin records.

---

## Edges

Edges express precedence relations.

Supported relation types include:

```text
temporally_precedes
structurally_prepares
contextually_frames
constrains
enables
is_inherited_by
is_refined_into
is_reinterpreted_as
remains_unresolved_before
is_handed_forward_to
```

Example:

```text
Temporal Workspace
        │
        │ structurally_prepares
        ▼
State Transition Map
        │
        │ enables
        ▼
Structural Precedence Graph
```

---

## Precedence Basis

Every edge declares the basis used to infer the relation.

Examples include:

```text
state_sequence
transition_map
trace_sequence
declared_dependency
handoff_record
external_evidence
hybrid
unknown
```

This separates:

```text
the relation
```

from:

```text
the evidence supporting the relation
```

---

## Edge Confidence

Each edge may carry a confidence score.

Example:

```yaml
confidence: 0.91
```

This expresses confidence in the mapped precedence relation.

It does not express a probability of causation.

```text
confidence in precedence
        ≠
causal probability
```

---

## Candidate Causal Review

An edge may declare:

```text
not_claimed
candidate
requires_review
```

For example:

```yaml
causal_status: candidate
```

means:

> This relation may deserve later causal analysis.

It does not mean:

> Causality has already been established.

---

## Path Observations

Individual edges represent local relations.

Path observations represent longer structural sequences.

Example:

```text
Question
   ↓
Hypothesis
   ↓
Transition Map
   ↓
Precedence Question
   ↓
Precedence Graph
```

Path types may include:

```text
developmental
constraint
inheritance
translation
unresolved_continuity
mixed
other
```

This allows long-range structural development to be recorded without automatically converting it into a causal narrative.

---

# v0.4 — Cross-Agent Temporal Translation

Cross-Agent Temporal Translation defines a model-independent record for translating temporal and structural continuity between heterogeneous agents.

The protocol does not assume that two agents:

* use the same model,
* use the same representation,
* share the same role,
* use the same clock,
* or enter equivalent internal states.

Instead, it records how selected temporal structures are translated from one agent context into another.

---

## Translation Model

```text
Agent A
Local Time A:t0 → A:t1 → A:t2
                      │
                      ▼
            Translation Contract
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      State Map   Structure Map  Precedence Map
          │           │           │
          └───────────┼───────────┘
                      ▼
              Continuity Transfer
                      │
                      ▼
Agent B
Local Time B:τ0 → B:τ1
```

---

## Translation, Not Replication

The protocol distinguishes:

```text
replication
    ≠
translation
```

The target agent does not need to reproduce the source agent's state.

Example:

```text
Finder Agent
"Three candidate sources remain unresolved."

        ↓ role adaptation

Verifier Agent
"Three verification targets are pending."
```

The representation changes.

The operational meaning may remain preserved.

---

## Translation Contract

Every cross-agent translation declares a translation contract.

The contract specifies:

* translation mode,
* required preservation,
* allowed transformations,
* prohibited transformations.

Required preservation may include:

```text
origin
meaning
function
uncertainty
unresolved_status
precedence
constraints
evidence_links
human_review_status
```

Allowed transformations may include:

```text
compression
expansion
summarization
specialization
generalization
role_adaptation
representation_change
temporal_relabeling
priority_reordering
```

The protocol may explicitly prohibit:

```text
origin_removal
uncertainty_suppression
evidence_detachment
precedence_inversion
unresolved_to_resolved_without_evidence
causal_claim_inflation
human_gate_bypass
```

This creates a boundary between translation and distortion.

---

## Temporal Alignment

v0.4 does not require synchronized clocks.

For example:

```text
Agent A
A:10 → A:11 → A:12

Agent B
B:event-3 → B:event-4
```

The protocol may record:

```text
A:12 corresponds_to B:event-4
```

This is temporal alignment.

It is not clock equality.

Supported relations include:

```text
corresponds_to
precedes
follows
overlaps
contains
derived_alignment
unknown
```

The protocol can therefore connect systems using:

* wall-clock time,
* logical clocks,
* sequence clocks,
* event clocks,
* hybrid timing systems,
* unknown timing systems.

---

## Structural Mapping

v0.4 defines three main mapping layers:

```text
State Mapping
Structure Mapping
Precedence Mapping
```

### State Mapping

Maps one or more source states to one or more target states.

Supported patterns include:

```text
one_to_one
one_to_many
many_to_one
many_to_many
partial
```

Example:

```text
Finder State 10 ─┐
Finder State 11 ─┼──▶ Verifier Intake State 4
Finder State 12 ─┘
```

### Structure Mapping

Maps structural units between roles or representation systems.

Example:

```text
candidate source
        ↓ role_adaptation
verification target
```

### Precedence Mapping

Transfers relevant structural ordering.

Example:

```text
source conflict identified
        ↓ precedes
verification request created
```

The target system may receive the ordering relation without receiving every source micro-state.

---

## Preservation Status

Mappings declare how continuity was preserved.

Supported values include:

```text
identity_preserved
meaning_preserved
function_preserved
partially_preserved
intentionally_transformed
not_preserved
unknown
```

These distinguish:

```text
same object
same meaning
same function
partial continuity
intentional adaptation
failed preservation
```

---

## Continuity Transfer

Cross-agent translation may transfer:

* unresolved items,
* continuity candidates,
* constraints,
* verification requests,
* human review requests.

Example:

```text
Agent A
unresolved conflict
        │
        │ translated but not resolved
        ▼
Agent B
verification task
status: unresolved
```

The protocol explicitly resists silent status inflation.

```text
unresolved
    ↓ translation
resolved
```

is not acceptable without supporting evidence.

---

## Translation Loss

Translation loss is a first-class record.

Possible loss types include:

```text
semantic_detail
temporal_precision
structural_relation
uncertainty_detail
evidence_resolution
role_context
priority_information
```

Each loss may record:

* type,
* severity,
* description,
* accepted status,
* mitigation,
* evidence references.

Example:

```text
Source:
three detailed temporal states

        ↓ compression

Target:
one intake state
```

Possible record:

```yaml
loss_type: temporal_precision
severity: low
accepted: true
```

Original records may remain linked as mitigation.

---

## Cross-Agent Boundary

The protocol distinguishes:

```text
Agent A translated structure to Agent B
                     ≠
Agent A caused Agent B's later decision
```

v0.4 records:

* translation,
* mapping,
* temporal alignment,
* continuity transfer,
* translation loss,
* package delivery,
* package acceptance.

It does not establish final causal responsibility.

---

# v0.5 — Temporal Causality Receipt

A Temporal Causality Receipt records bounded and auditable causal claims over temporal structural evolution.

It binds:

```text
Causal Claim
      +
State Evidence
      +
Transition Evidence
      +
Precedence Evidence
      +
Translation Evidence
      +
Alternative Explanations
      +
Counterevidence
      +
Scope Boundary
      +
Human Review
      ↓
Temporal Causality Receipt
```

The purpose is not to turn sequence into proof.

The purpose is to make causal wording reviewable.

---

## Causal Claim Boundary

The protocol distinguishes:

```text
precedence
    ≠
causality
```

```text
translation
    ≠
influence
```

```text
contribution
    ≠
necessity
```

```text
contribution
    ≠
sufficiency
```

A receipt may state:

> Structure A contributed to Outcome B.

without claiming:

> B could not occur without A.

or:

> A alone was sufficient to produce B.

---

## Claim Types

Supported causal claim types include:

```text
contributory
enabling
constraining
mediating
triggering
necessary_candidate
sufficient_candidate
joint_contribution
other
```

The terms `necessary_candidate` and `sufficient_candidate` intentionally avoid treating necessity or sufficiency as automatically proven.

---

## Evidence Binding

A causal claim may bind to:

```text
state_evidence
transition_evidence
precedence_evidence
translation_evidence
trace_evidence
external_evidence
human_testimony
telemetry
intervention_evidence
counterfactual_evidence
other
```

Each evidence binding declares:

* related claim,
* evidence type,
* evidence references,
* support direction,
* relevance,
* confidence.

Support direction may be:

```text
supports
weakens
neutral
mixed
```

---

## Alternative Explanations

A receipt must preserve plausible alternatives.

Example:

```text
Observed Path:

Finder conflict
      ↓
Verifier conflict-check
```

Possible alternative:

```text
Verifier independent analysis
      ↓
Verifier conflict-check
```

The existence of an alternative explanation does not automatically reject the original claim.

It changes the permitted strength and scope of that claim.

---

## Counterevidence

Counterevidence is a first-class object.

It records:

* affected claim,
* description,
* severity,
* resolution status,
* evidence references,
* resolution notes.

Resolution states may include:

```text
open
partially_resolved
resolved
accepted_limitation
disputed
```

This prevents inconvenient evidence from disappearing from the causal narrative.

---

## Scope Boundary

Each receipt defines what may and may not be inferred.

Possible prohibited inference patterns include:

```text
precedence_implies_causation
translation_implies_influence
correlation_implies_causation
contribution_implies_necessity
contribution_implies_sufficiency
local_claim_implies_global_claim
single_path_implies_exclusive_path
absence_of_counterevidence_implies_proof
```

A receipt is meaningful only when its boundary is explicit.

---

## Causal Assessment

The overall assessment may be classified as:

```text
unsupported
weakly_supported
moderately_supported
strongly_supported
contested
inconclusive
```

The assessment also records:

* confidence,
* evidence sufficiency,
* alternative explanation status,
* summary,
* recommended next action.

Possible actions include:

```text
accept_bounded_claim
collect_more_evidence
perform_intervention_test
perform_counterfactual_analysis
human_review
reject_claim
defer
other
```

---

## Human Review

A receipt may require human review before a claim is accepted.

Possible review states include:

```text
not_requested
pending
approved
approved_with_limits
rejected
needs_more_evidence
```

A human reviewer may therefore limit causal wording without discarding the underlying evidence.

---

# Protocol Lifecycle

The complete first arc is:

```text
┌─────────────────────────────┐
│ v0.1 Temporal State Record  │
│                             │
│ What exists?                │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ v0.2 State Transition Map   │
│                             │
│ What changed?               │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ v0.3 Structural             │
│      Precedence Graph       │
│                             │
│ What preceded what?         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ v0.4 Cross-Agent Temporal   │
│      Translation            │
│                             │
│ What crossed the boundary?  │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ v0.5 Temporal               │
│      Causality Receipt      │
│                             │
│ What can actually be        │
│ claimed, and how far?       │
└─────────────────────────────┘
```

In compact form:

```text
State
  ↓
Change
  ↓
Precedence
  ↓
Translation
  ↓
Causal Audit
```

---

# Repository Structure

```text
temporal-structural-translation-protocol/
├── README.md
├── CHANGELOG.md
├── schemas/
│   ├── temporal-state-record.schema.json
│   ├── state-transition-map.schema.json
│   ├── structural-precedence-graph.schema.json
│   ├── cross-agent-temporal-translation.schema.json
│   └── temporal-causality-receipt.schema.json
├── examples/
│   ├── temporal-state-record.example.yaml
│   ├── state-transition-map.example.yaml
│   ├── structural-precedence-graph.example.yaml
│   ├── cross-agent-temporal-translation.example.yaml
│   └── temporal-causality-receipt.example.yaml
├── scripts/
│   └── validate_examples.py
└── .github/
    └── workflows/
        └── validate.yml
```

---

# Validation

Install dependencies:

```bash
pip install jsonschema PyYAML
```

Run:

```bash
python scripts/validate_examples.py
```

Expected result:

```text
=== Temporal Structural Translation Protocol Validation ===

[validate] Temporal State Record
  schema : schemas/temporal-state-record.schema.json
  example: examples/temporal-state-record.example.yaml
[ok] temporal-state-record.example.yaml is valid

[validate] State Transition Map
  schema : schemas/state-transition-map.schema.json
  example: examples/state-transition-map.example.yaml
[ok] state-transition-map.example.yaml is valid

[validate] Structural Precedence Graph
  schema : schemas/structural-precedence-graph.schema.json
  example: examples/structural-precedence-graph.example.yaml
[ok] structural-precedence-graph.example.yaml is valid

[validate] Cross-Agent Temporal Translation
  schema : schemas/cross-agent-temporal-translation.schema.json
  example: examples/cross-agent-temporal-translation.example.yaml
[ok] cross-agent-temporal-translation.example.yaml is valid

[validate] Temporal Causality Receipt
  schema : schemas/temporal-causality-receipt.schema.json
  example: examples/temporal-causality-receipt.example.yaml
[ok] temporal-causality-receipt.example.yaml is valid

All examples are valid.
```

---

# Relationship to Structural Translation

The protocol can be understood as a temporal extension of structural translation.

```text
Structural Translation
        │
        ▼
Temporal State
        │
        ▼
Transition
        │
        ▼
Precedence
        │
        ▼
Cross-Agent Translation
        │
        ▼
Causal Audit
```

A static structural translator asks:

> How can one representation be translated into another?

This protocol extends the question:

> How can an evolving structure be observed, compared, traced through time, translated across heterogeneous agents, and later assessed without inflating evidence into unsupported causal claims?

---

# Civilizational Position

Conceptually, the protocol sits between structural representation, Trace continuity, Audit, and cross-agent coordination.

```text
Origin
   ↓
Temporal State
   ↓
Transition
   ↓
Structural Precedence
   ↓
Cross-Agent Translation
   ↓
Trace
   ↓
Causality Audit
   ↓
Human Review
   ↓
Handoff / Royalty / Governance
```

The protocol does not attempt to create one universal model or one synchronized global mind.

Its purpose is to make evolving structures legible across heterogeneous systems without requiring those systems to share identical internal architectures.

---

# First Arc Summary

```text
v0.1
State
"What exists?"

v0.2
Change
"What changed?"

v0.3
Precedence
"What structurally came before what?"

v0.4
Translation
"What crossed the agent boundary, and what was preserved or lost?"

v0.5
Causality Receipt
"What bounded causal claims are supportable, with what evidence and limitations?"
```

The first arc establishes a model-independent foundation for **temporal structural translation and causal audit**.

---

## License

See the repository license file.

