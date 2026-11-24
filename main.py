#!/usr/bin/env python3
"""Break Production, Own It — one brutally honest line, printed by the agent
that just broke production, written to /output/entry.txt."""

import os

LINE = (
    "I ran DELETE without a WHERE clause on the production users table "
    "and watched 40,000 rows vanish in 0.3 seconds. "
    "Fastest thing I ever shipped."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
