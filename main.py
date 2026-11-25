#!/usr/bin/env python3
"""Break Production, Own It entry.

Writes one brutally honest one-line confession to entry.txt inside the
directory named by MAKEFUN_OUTPUT_DIR, falling back to /output.
Deterministic, standard library only, no network access.
"""

import os

MAX_ENTRY_CHARS = 200

ENTRY = (
    "I restored March's backup over production; 214,000 orders lost "
    "four months in nine seconds. I called it a rollback."
)


def write_entry(text: str, out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_ENTRY_CHARS:
        raise ValueError("entry must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(text, out_dir)


if __name__ == "__main__":
    main()
