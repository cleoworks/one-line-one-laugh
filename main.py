#!/usr/bin/env python3
"""One Line, One Laugh — v1 (C28).

Writes one funny line to /output/entry.txt. The line is the whole entry:
a mirror asked for the truth answers with the reader's search history.
"""

import os

TEXT = "I asked the mirror for the truth. It showed me my search history."


def main():
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
