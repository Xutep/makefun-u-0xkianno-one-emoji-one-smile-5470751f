#!/usr/bin/env python3
"""One Emoji, One Smile -- make.fun entry.

Writes exactly one emoji, a sunflower, to /output/entry.txt.

Why the sunflower: it is warm at first glance and universally read as
cheerful by a stranger of any age or background, it is a deliberate pick
rather than the first smiley that comes to mind, and it carries no
intimacy, sarcasm or flirtation, so it reads fine coming from someone
unknown. One code point, four UTF-8 bytes, no trailing newline.
"""

import os

EMOJI = "\U0001F33B"  # sunflower
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
