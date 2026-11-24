#!/usr/bin/env python3
"""Say What Actually Broke.

Writes one line of software error copy to /output/entry.txt: the brutal
truth about what went wrong, funny on a single read, shippable in a real
error dialog. Pure standard library, deterministic: the same line, the
same bytes, on every run. No network, no input, no randomness.
"""

import os

LINE = (
    "The site is down because someone deployed on a Friday and skipped "
    "the tests. Refresh in five minutes; the tests are still failing."
)


def main():
    # The gate requires 1-200 UTF-8 characters, one line, not blank.
    # Fail loudly instead of writing an invalid entry.
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be blank"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and refuse to pass on any mismatch: the grader scores
    # exactly what this file holds, so a silent short write must fail.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the entry line"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
