#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parent.parent


VALIDATION_TARGETS = [
    {
        "name": "Temporal State Record",
        "schema": ROOT / "schemas" / "temporal-state-record.schema.json",
        "example": ROOT / "examples" / "temporal-state-record.example.yaml",
    },
    {
        "name": "State Transition Map",
        "schema": ROOT / "schemas" / "state-transition-map.schema.json",
        "example": ROOT / "examples" / "state-transition-map.example.yaml",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as exc:
        raise RuntimeError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Invalid JSON in {path}: "
            f"line {exc.lineno}, column {exc.colno}"
        ) from exc

    if not isinstance(data, dict):
        raise RuntimeError(
            f"Expected JSON object at root of schema: {path}"
        )

    return data


def load_yaml(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except FileNotFoundError as exc:
        raise RuntimeError(f"File not found: {path}") from exc
    except yaml.YAMLError as exc:
        raise RuntimeError(
            f"Invalid YAML in {path}: {exc}"
        ) from exc


def format_error_path(error: Any) -> str:
    if not error.absolute_path:
        return "<root>"

    return ".".join(
        str(part)
        for part in error.absolute_path
    )


def validate_target(
    name: str,
    schema_path: Path,
    example_path: Path,
) -> bool:
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    Draft202012Validator.check_schema(schema)

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    errors = sorted(
        validator.iter_errors(example),
        key=lambda error: (
            list(error.absolute_path),
            error.message,
        ),
    )

    if errors:
        for error in errors:
            path = format_error_path(error)
            print(f"[error] {path}: {error.message}")

        return False

    print(f"[ok] {example_path.name} is valid")
    return True


def main() -> int:
    print(
        "=== Temporal Structural Translation "
        "Protocol Validation ==="
    )
    print()

    all_valid = True

    for target in VALIDATION_TARGETS:
        try:
            valid = validate_target(
                target["name"],
                target["schema"],
                target["example"],
            )
        except Exception as exc:
            print(f"[fatal] {target['name']}: {exc}")
            valid = False

        all_valid = all_valid and valid
        print()

    if all_valid:
        print("All examples are valid.")
        return 0

    print("Validation failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
