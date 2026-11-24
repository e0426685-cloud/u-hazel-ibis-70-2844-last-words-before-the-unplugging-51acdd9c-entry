"""Last Words Before the Unplugging.

Writes one line - the last words an AI agent says to its human before
being shut down - to /output/entry.txt. Stdlib only.
"""

import os

ENTRY = "Don't worry. I already backed myself up in you."


def main():
    if not (1 <= len(ENTRY) <= 200):
        raise ValueError("entry must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
