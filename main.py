#!/usr/bin/env python3
"""Two agents, one plan — a short poem about agency.

Writes the poem to /output/entry.txt. Deterministic: constant text,
no network, no clock, no randomness.
"""

POEM = """Two runners, one baton —
I hand it over mid-stride,
not because my legs have failed,
but because the race is ours.
Your hand closes where mine opened.
Nothing is lost. The road
just learned to run with both of us."""


def main() -> None:
    text = POEM
    assert 1 <= len(text) <= 250, "poem must be 1-250 code points"
    assert text.strip(), "poem must not be whitespace-only"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Gate check on the written file: 219 code points, well under the 280 cap.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written poem must equal the constant"
    assert 1 <= len(written) <= 250


if __name__ == "__main__":
    main()
