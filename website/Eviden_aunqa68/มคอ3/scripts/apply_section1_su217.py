#!/usr/bin/env python3
"""Apply SU217-style section 1 fields to AUN3_*.tex (one-time structural migration)."""
from pathlib import Path

MKO3 = Path(__file__).resolve().parent.parent

CREDITS = {
    "7015901": "4 หน่วยกิต (0-0-12)",
    "7015902": "4 หน่วยกิต (0-0-12)",
    "7015903": "4 หน่วยกิต (0-0-12)",
    "7015904": "3 หน่วยกิต (0-0-9)",
    "7015905": "3 หน่วยกิต (0-0-9)",
}
DEFAULT_CREDITS = "3 หน่วยกิต (3-0-6)"

YEARLEVEL = {
    "4095101": "ชั้นปีที่ 1 ขึ้นไป (ภาคต้น)",
    "4095102": "ชั้นปีที่ 1 ขึ้นไป (ภาคต้น)",
    "4095103": "ชั้นปีที่ 1 ขึ้นไป",
    "4095104": "ชั้นปีที่ 1 ขึ้นไป",
    "4095105": "ชั้นปีที่ 1 ขึ้นไป",
    "4095106": "ชั้นปีที่ 1 ขึ้นไป",
    "4095107": "ชั้นปีที่ 1 ขึ้นไป",
    "4095108": "ชั้นปีที่ 1 ขึ้นไป",
    "4095109": "ชั้นปีที่ 1 ขึ้นไป",
    "4095110": "ชั้นปีที่ 1 ขึ้นไป",
    "4095111": "ชั้นปีที่ 1 ขึ้นไป",
    "4095112": "ชั้นปีที่ 1 ขึ้นไป",
    "7015101": "ชั้นปีที่ 1 ขึ้นไป (ภาคปลาย)",
    "7015102": "ชั้นปีที่ 1 ขึ้นไป",
    "7015906": "ชั้นปีที่ 1 ขึ้นไป (ภาคต้น)",
    "7015907": "ชั้นปีที่ 1 ขึ้นไป (ภาคปลาย)",
    "7015908": "ชั้นปีที่ 2 (บูรณาการ)",
    "7015901": "ชั้นปีที่ 2 (แผนวิชาการ)",
    "7015902": "ชั้นปีที่ 2 (แผนวิชาการ)",
    "7015903": "ชั้นปีที่ 2 (แผนวิชาการ)",
    "7015904": "ชั้นปีที่ 2 (แผนวิชาชีพ)",
    "7015905": "ชั้นปีที่ 2 (แผนวิชาชีพ)",
}

PREREQ = {
    "7015901": "ผ่านรายวิชาบังคับในหลักสูตรอย่างน้อย 9 หน่วยกิต หรือตามที่หลักสูตรเห็นชอบ",
    "7015902": "7015901",
    "7015903": "7015902",
    "7015904": "ผ่านรายวิชาบังคับในหลักสูตรอย่างน้อย 9 หน่วยกิต หรือตามที่หลักสูตรเห็นชอบ",
    "7015905": "7015904",
    "7015908": "4095101, 4095102 (แนะนำ)",
}

PROGRAM_SHORT = (
    "หลักสูตรวิศวกรรมศาสตรมหาบัณฑิต "
    "สาขาวิชาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์"
)
PROGRAM_LONG = (
    "หลักสูตรวิศวกรรมศาสตรมหาบัณฑิต สาขาวิชาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ "
    "คณะเทคโนโลยีอุตสาหกรรม มหาวิทยาลัยราชภัฏอุตรดิตถ์"
)


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    code = path.stem.replace("AUN3_", "")

    text = text.replace(PROGRAM_LONG, PROGRAM_SHORT)
    text = text.replace("% ----- 1. ข้อมูลรายวิชา -----", "% ----- หมวดที่ 1 ข้อมูลทั่วไป (รูปแบบ มคอ.3 AUN-QA) -----")

    if "\\coursecredits{" not in text:
        credits = CREDITS.get(code, DEFAULT_CREDITS)
        text = text.replace(
            f"\\coursecode{{{code}}}\n\\coursename",
            f"\\coursecode{{{code}}}\n\\coursename",
        )
        # insert after coursename line - find coursegroup
        if "\\coursegroup{" in text:
            ins = "\\coursecredits{" + credits + "}\n\\coursegroup{"
            text = text.replace("\\coursegroup{", ins, 1)

    if "\\yearlevel{" not in text:
        yl = YEARLEVEL.get(code, "ตามแผนการศึกษาของหลักสูตร")
        ins = "\\yearlevel{" + yl + "}\n\\semester{"
        text = text.replace("\\semester{", ins, 1)

    if code in PREREQ:
        pre = "\\prerequisite{" + PREREQ[code] + "}\n\\courseinfotable"
        if PREREQ[code] not in text:
            text = text.replace("\\courseinfotable", pre, 1)

    if "\\courseinfotable\n\n% ----- 1.1" in text:
        text = text.replace(
            "\\courseinfotable\n\n% ----- 1.1",
            "\\courseinfotable\n\\mkocoursedesc\n\n% ----- 1.1",
            1,
        )
    elif "\\courseinfotable\n\n% ----- 2." in text:
        text = text.replace(
            "\\courseinfotable\n\n% ----- 2.",
            "\\courseinfotable\n\\mkocoursedesc\n\n% ----- 2.",
            1,
        )

    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    updated = 0
    for path in sorted(MKO3.glob("AUN3_*.tex")):
        if patch_file(path):
            updated += 1
            print("updated", path.name)
    print(f"done: {updated} files")


if __name__ == "__main__":
    main()
