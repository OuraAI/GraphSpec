#!/usr/bin/env python3
"""Sync labels from .github/labels.yml to a GitHub repository using gh CLI."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def parse_scalar(raw: str) -> str:
    value = raw.strip()
    if not value:
        return ""
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_labels(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"labels file not found: {path}")

    lines = path.read_text(encoding="utf-8").splitlines()
    labels_started = False
    labels: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue

        if stripped == "labels:":
            labels_started = True
            continue

        if not labels_started:
            continue

        if stripped.startswith("- "):
            if current is not None:
                labels.append(current)
            current = {}
            stripped = stripped[2:].strip()
        elif current is None:
            raise ValueError(f"invalid labels file at line {lineno}: field found before label item")

        if ":" not in stripped:
            raise ValueError(f"invalid labels file at line {lineno}: expected key:value pair")

        key, raw_value = stripped.split(":", 1)
        key = key.strip()

        if key not in {"name", "color", "description"}:
            continue

        current[key] = parse_scalar(raw_value)

    if current is not None:
        labels.append(current)

    if not labels:
        raise ValueError("invalid labels file: expected non-empty top-level 'labels' array")

    validated: list[dict[str, str]] = []
    for index, label in enumerate(labels, start=1):
        if not isinstance(label, dict):
            raise ValueError(f"invalid label at index {index}: expected mapping")

        name = label.get("name", "").strip()
        color = label.get("color", "").strip()
        description = label.get("description", "").strip()

        if not name or not color:
            raise ValueError(
                f"invalid label at index {index}: 'name' and 'color' are required, got {label!r}"
            )

        validated.append(
            {
                "name": name,
                "color": color,
                "description": description,
            }
        )

    return validated


def sync_labels(repo: str | None, labels: list[dict[str, str]]) -> None:
    for label in labels:
        cmd = [
            "gh",
            "label",
            "create",
            label["name"],
            "--color",
            label["color"],
            "--description",
            label["description"],
            "--force",
        ]
        if repo:
            cmd.extend(["--repo", repo])

        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            sys.stderr.write(result.stderr or result.stdout)
            raise SystemExit(result.returncode)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync labels from .github/labels.yml to a GitHub repository using gh CLI."
    )
    parser.add_argument("--repo", help="GitHub repository in OWNER/REPO format")
    parser.add_argument(
        "--file",
        default=".github/labels.yml",
        help="Path to labels.yml (default: .github/labels.yml)",
    )
    args = parser.parse_args()

    try:
        labels = parse_labels(Path(args.file))
    except ValueError as exc:
        sys.stderr.write(f"error: {exc}\n")
        return 1

    sync_labels(args.repo, labels)
    print(f"synced {len(labels)} labels")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
