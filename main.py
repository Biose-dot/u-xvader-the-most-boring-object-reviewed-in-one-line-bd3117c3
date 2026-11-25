#!/usr/bin/env python3
"""Write this entry's one-liner to /output/entry.txt.

Pure Python 3 stdlib, no network, no randomness: reads entry.txt
shipped next to this file, writes it to $MAKEFUN_OUTPUT_DIR
(default /output), and prints it.

Run:  python3 main.py
"""

import os


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    with open(src, "r", encoding="utf-8") as f:
        text = f.read().strip("\n")
    if not text.strip():
        raise ValueError("entry.txt is empty")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
