# Temporal Structural Translation Protocol

A model-independent protocol for representing temporal structural states,
state evolution, causal transitions, structural precedence, and continuity
across heterogeneous AI systems and agents.

## Current Version

**v0.1 — Temporal State Record**

The first version defines a minimal record for representing an observable
or externally representable structural state at a specific temporal
position.

The protocol does not attempt to expose raw hidden activations or private
chain-of-thought.

Instead, it records structural information that can be represented,
compared, translated, handed off, and audited.

---

## Why This Protocol Exists

AI systems increasingly operate through:

- multiple models,
- specialized agents,
- distributed wings,
- persistent memory,
- iterative reasoning,
- tool execution,
- human review,
- and cross-system handoffs.

These systems may exchange outputs while still lacking a common protocol
for expressing how structural state changes over time.

A static artifact can show what exists.

A trace can show what was recorded.

A handoff can show what was transferred.

But a temporal system also needs to express:

- what structures were active at a given point,
- what remained unresolved,
- what depended on what,
- what should continue,
- and later, what changed between states.

The Temporal Structural Translation Protocol addresses this layer.

---

## Core Model

The protocol begins with the following minimal sequence:

```text
State(t)
   ↓
Transition
   ↓
State(t+1)

v0.1 specifies only the state representation:

Temporal State Record

Later versions may formalize transitions, precedence, cross-agent temporal
translation, and causal receipts.

v0.1 — Temporal State Record

A Temporal State Record represents:

What structures are active?
What remains unresolved?
What dependencies exist?
What may continue into a later state?
How was this state observed?
What are the limits of that observation?

A state record is a structural abstraction.

It is not:

raw model activations,
hidden reasoning extraction,
private chain-of-thought,
or a claim of complete mechanistic interpretability.
Record Structure
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
Temporal Context

Each state may contain:

a sequence index,
logical time,
previous state reference,
and lifecycle phase.

Example:

temporal_context:
  sequence_index: 0
  logical_time: "t0"
  previous_state_record_id: null
  phase: translation

The protocol separates chronological timestamps from logical sequence.

This allows implementations to represent systems where:

multiple agents operate asynchronously,
logical state order differs from wall-clock order,
or distributed observations must later be aligned.
Active Structures

An active structure is an externally representable structural unit that is
relevant to the current state.

Example categories may include:

hypotheses,
constraints,
goals,
interpretations,
plans,
conflicts,
unresolved questions,
or structural relations.

Each active structure may indicate:

activation level,
stability,
origin references,
and trace references.
Unresolved Items

Temporal continuity requires more than preserving completed outputs.

Systems also need to retain:

open questions,
conflicts,
deferred issues,
blocked work,
and unresolved uncertainty.

The unresolved_items field makes these explicit.

Dependencies

The protocol may describe structural relationships such as:

supports
constrains
requires
conflicts_with
refines
derived_from

These relationships provide a foundation for later temporal comparison.

v0.1 records dependencies within a state.

Later versions may describe how those dependencies change between states.

Continuity Candidates

A continuity candidate indicates what should happen to a structure after
the current state.

Supported intents are:

preserve
revisit
transform
verify
handoff
retire

This does not itself perform the transition.

It records forward continuity intent.

Observation Boundary

Every state record declares an observation basis.

Supported values include:

self_report
trace_inference
telemetry
external_observation
hybrid

The record must also carry a confidence value.

Implementations should explicitly document limitations.

This boundary prevents a structural state abstraction from being mistaken
for complete access to an AI system's internal reasoning process.

Example Validation

Install dependencies:

pip install jsonschema PyYAML

Run:

python scripts/validate_examples.py

Expected result:

=== Temporal Structural Translation Protocol Validation ===

[validate] Temporal State Record
  schema : schemas/temporal-state-record.schema.json
  example: examples/temporal-state-record.example.yaml
[ok] temporal-state-record.example.yaml is valid

All examples are valid.
Roadmap
v0.1  Temporal State Record
v0.2  State Transition Map
v0.3  Structural Precedence Graph
v0.4  Cross-Agent Temporal Translation
v0.5  Temporal Causality Receipt

The first arc moves from:

state
→ change
→ precedence
→ translation
→ causality
Civilizational Position

The protocol is designed as a temporal layer between structural
representation and trace continuity.

Conceptually:

Origin
   ↓
Structural State
   ↓
Temporal Transition
   ↓
Trace
   ↓
Audit
   ↓
Handoff
   ↓
Royalty

The purpose is not to create a single universal mind.

The purpose is to make evolving structures legible across heterogeneous
systems without requiring those systems to share identical internal
representations.

License

See the repository license file.
