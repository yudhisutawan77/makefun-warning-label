"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
<ENTRY_OUT>/entry.txt (ENTRY_OUT defaults to /output).

The label is one joke, built like a real printed product warning:
a defective-product setup, then the punch lands in the last few words.
"""

import os

ENTRY_TEXT = (
    "WARNING: This human ships with no manual, no warranty, "
    "and one (1) unresolved childhood. Handle with sarcasm."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY_TEXT.strip()
    if not (1 <= len(text) <= 160) or not text.strip():
        raise SystemExit("entry fails the 1-160 character gate")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
