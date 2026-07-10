# Changelog

All notable changes to this project will be documented in this file.

The project follows an experimental protocol-development lifecycle.

---

## [0.1.0-candidate] - 2026-07-10

### Added

- Initial Temporal State Record specification.
- JSON Schema for model-independent temporal state representation.
- Example YAML record.
- Subject identity and role representation.
- Temporal context fields:
  - sequence index,
  - logical time,
  - previous state reference,
  - lifecycle phase.
- State snapshot representation for:
  - active structures,
  - unresolved items,
  - structural dependencies,
  - continuity candidates.
- Observation basis and confidence fields.
- Explicit observation limitations.
- Human review and audit metadata.
- Python validation script.
- GitHub Actions validation workflow.

### Design Boundary

v0.1 records an externally representable structural state at a temporal
position.

It does not define:

- state transition semantics,
- causal transformation claims,
- temporal precedence graphs,
- cross-agent clock synchronization,
- cross-agent temporal translation,
- or temporal causality receipts.

These are reserved for later versions.

### Roadmap

- v0.2 — State Transition Map
- v0.3 — Structural Precedence Graph
- v0.4 — Cross-Agent Temporal Translation
- v0.5 — Temporal Causality Receipt
