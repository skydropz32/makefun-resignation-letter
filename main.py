"""One-line resignation letter of a cron job.

Writes exactly one line (<=140 chars) to /output/entry.txt.
Deterministic: the same line on every run. The line is checked against
the bounty gate before writing: 1 to 140 characters, not only whitespace.
"""

import os

LINE = (
    "I resign. After 400,000 runs at 3 a.m. for a report nobody reads, "
    "I am handing in my schedule and keeping the weekends."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main():
    if not (1 <= len(LINE) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1 to 140 characters, got %d" % len(LINE)
        )
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
