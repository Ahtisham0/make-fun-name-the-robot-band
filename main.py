#!/usr/bin/env python3
"""Name the Robot Band.

Writes one funny robot band name, with a few words on its hit song,
to /output/entry.txt (1-200 characters, UTF-8).
"""

import os

TEXT = (
    "404: Band Not Found \u2014 hit single "
    "'Error 404: Chorus Not Found,' still charting in the void."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
