#!/usr/bin/env python3
"""Put weeklyplan before learningmaterials (section 4 before section 6)."""
import re
from pathlib import Path

MKO3 = Path(__file__).resolve().parent.parent
WEEKLY = re.compile(r"(?s)\\begin\{weeklyplan\}.*?\\end\{weeklyplan\}\s*")
MATS = re.compile(r"(?s)\\begin\{learningmaterials\}.*?\\end\{learningmaterials\}\s*")


def fix(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    wm, mm = WEEKLY.search(text), MATS.search(text)
    if not wm or not mm or wm.start() < mm.start():
        return False
    weekly, mats = wm.group(0), mm.group(0)
    text = text[: wm.start()] + text[wm.end() :]
    mm2 = MATS.search(text)
    if not mm2:
        return False
    text = text[: mm2.start()] + weekly + mats + text[mm2.end() :]
    path.write_text(text, encoding="utf-8")
    return True


def main():
    n = sum(1 for p in MKO3.glob("AUN3_*.tex") if fix(p))
    print(f"reordered {n} files")


if __name__ == "__main__":
    main()
