#!/usr/bin/env python3
"""Reorder AUN3_*.tex blocks to SU217 + required headings layout."""
import re
from pathlib import Path

MKO3 = Path(__file__).resolve().parent.parent

BLOCK_PATTERNS = [
    ("header", r"(?s)\A.*?\\courseinfotable"),
    ("courseinfotable", r"\\courseinfotable\s*"),
    ("mkocoursedesc", r"\\mkocoursedesc\s*"),
    ("courseobjectives", r"(?s)\\begin\{courseobjectives\}.*?\\end\{courseobjectives\}\s*"),
    ("postoutcomes", r"(?s)\\begin\{postoutcomes\}.*?\\end\{postoutcomes\}\s*"),
    ("learningmaterials", r"(?s)\\begin\{learningmaterials\}.*?\\end\{learningmaterials\}\s*"),
    ("courseactivities", r"(?s)\\begin\{courseactivities\}.*?\\end\{courseactivities\}\s*"),
    ("clodomain", r"(?s)\\begin\{clodomaintable\}.*?\\end\{clodomaintable\}\s*"),
    ("cloplo", r"(?s)\\begin\{cloplotable\}.*?\\end\{cloplotable\}\s*"),
    ("bloom", r"(?s)\\begin\{bloomtable\}.*?\\end\{bloomtable\}\s*"),
    ("content", r"(?s)\\begin\{contentanalysistable\}.*?\\end\{contentanalysistable\}\s*"),
    ("teaching", r"(?s)\\begin\{teachingtable\}.*?\\end\{teachingtable\}\s*"),
    ("assessment", r"(?s)\\begin\{assessmenttable\}.*?\\end\{assessmenttable\}\s*"),
    ("support", r"(?s)\\begin\{supporttable\}.*?\\end\{supporttable\}\s*"),
    ("weekly", r"(?s)\\begin\{weeklyplan\}.*?\\end\{weeklyplan\}\s*"),
    ("footer", r"(?s)(\\signatureblock\{.*?\}\s*\\end\{document\})"),
]

ORDER = [
    "header",
    "courseobjectives",
    "postoutcomes",
    "clodomain",
    "cloplo",
    "bloom",
    "content",
    "mkocoursedesc",
    "courseactivities",
    "teaching",
    "assessment",
    "learningmaterials",
    "support",
    "weekly",
    "footer",
]


def extract(text: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    rest = text
    for name, pat in BLOCK_PATTERNS:
        m = re.search(pat, rest)
        if not m:
            continue
        if name == "footer":
            blocks[name] = m.group(1)
        else:
            blocks[name] = m.group(0)
        rest = rest[: m.start()] + rest[m.end() :]
    return blocks


def reorder_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    blocks = extract(text)
    if "header" not in blocks or "footer" not in blocks:
        print("skip (parse failed):", path.name)
        return False

    out = [blocks["header"]]
    for key in ORDER[1:-1]:
        if key in blocks:
            out.append(blocks[key])

    out.append(blocks["footer"])
    new_text = "".join(out)

    # Update section comments
    new_text = new_text.replace(
        "% ----- 1.1 วัตถุประสงค์ -----",
        "% ----- หมวดที่ 2: วัตถุประสงค์ / ผลที่ได้รับ / CLOs -----",
    )
    new_text = new_text.replace(
        "% ----- 1.2 ผลที่ได้รับหลังเรียน -----",
        "",
    )
    new_text = new_text.replace(
        "% ----- 1.3 เอกสารประกอบการเรียน -----",
        "% ----- หมวดที่ 6: เอกสารและสื่อ -----",
    )
    new_text = new_text.replace(
        "% ----- 1.4 กิจกรรมในรายวิชา -----",
        "% ----- หมวดที่ 3: คำอธิบาย / กิจกรรม -----",
    )
    new_text = new_text.replace(
        "% ----- 8. แผนการจัดการเรียนรู้รายสัปดาห์ -----",
        "% ----- หมวดที่ 4: แผนการจัดการเรียนรู้รายสัปดาห์ -----",
    )

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main():
    n = 0
    for path in sorted(MKO3.glob("AUN3_*.tex")):
        if reorder_file(path):
            n += 1
            print("reordered", path.name)
    print(f"done: {n} files")


if __name__ == "__main__":
    main()
