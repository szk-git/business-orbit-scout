#!/usr/bin/env python3
import os
from pathlib import Path


def redact_env_line(line: str) -> str:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return line
    if "=" not in line:
        return line
    key, _value = line.split("=", 1)
    return f"{key}=REDACTED\n"


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    env_path = root / ".env"
    example_path = root / ".env.example"

    if not env_path.exists():
        print("No .env found; create one locally with your secrets first.")
        return 1

    with env_path.open("r", encoding="utf-8") as handle:
        lines = handle.readlines()

    redacted = [redact_env_line(line) for line in lines]

    with example_path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.writelines(redacted)

    print(f"Wrote redacted env to {example_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
