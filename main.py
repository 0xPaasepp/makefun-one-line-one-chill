"""Write one line of horror to /output/entry.txt. Pure stdlib."""

import os

ENTRY = (
    "My daughter stopped drawing our family the night she started drawing "
    "the tall man who stands behind me in every picture, smiling with my teeth."
)

# The gate allows 1 to 200 characters; fail loudly instead of shipping
# an entry the scorer would refuse. One line, one sentence: no newline
# inside, exactly one sentence terminator.
if not 1 <= len(ENTRY) <= 200:
    raise SystemExit(f"entry is {len(ENTRY)} characters, gate allows 1-200")
if "\n" in ENTRY or ENTRY.count(".") != 1:
    raise SystemExit("entry must be a single line holding a single sentence")


def main() -> None:
    path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
