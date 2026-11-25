#!/usr/bin/env python3
"""How many tabs do I have open? 256.

A tiny honest confession, written to /output/entry.txt as digits only.
No words, no explanation, no trailing newline — just the count.

Why 256? It is a programmer's tab hoard: documentation pages left open
"just in case", half-read Stack Overflow answers, GitHub pull requests
waiting for review, a dozen articles I swear I will finish someday.
Two hundred and fifty-six is a power of two, which is exactly the kind
of number a tab hoarder's browser would land on — and it is far past
the point where anyone closes tabs one by one anymore.
"""

import os

TABS_OPEN = 256


def write_entry(count: int, output_dir: str) -> str:
    """Write the count as plain digits to entry.txt; return the path."""
    text = str(count)
    # The gate wants 1-5 characters of digits, nothing else.
    assert text.isdigit() and 1 <= len(text) <= 5, "count must be 1-5 digits"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    # newline="" keeps the file at exactly the digits, no trailing newline.
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return entry_path


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(TABS_OPEN, output_dir)


if __name__ == "__main__":
    main()
