#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The One-Line Cat Joke That Lands — entry program.

Writes the chosen one-line cat joke to /output/entry.txt and enforces
the kit's gate: UTF-8 text, 1 to 200 characters, not only white space,
a single line. The output file is left world-readable (mode 0644) and
the output directory world-accessible, so the grader can collect it.

Standard library only, no network. The entry is a fixed literal, so
every run writes byte-identical output (see test_determinism.sh).
"""

import os

ENTRY = "I hid my cat's pill in cheese. She ate the cheese, left the pill, and now the cheese is under investigation."

# The kit's gate, from competition.yaml / RULES.txt.
MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    # Gate checks, before anything is written.
    assert text.strip(), "entry must not be only white space"
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        "entry is %d characters, gate is %d-%d" % (len(text), MIN_CHARS, MAX_CHARS)
    )
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")  # must be valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    print(text)


if __name__ == "__main__":
    main()
