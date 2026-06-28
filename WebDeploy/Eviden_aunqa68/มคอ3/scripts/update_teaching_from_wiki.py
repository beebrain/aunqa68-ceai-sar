#!/usr/bin/env python3
"""Update teachingtable in มคอ.3 .tex files from aun-qa-wiki/summaries/teaching-activities.md"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "aun-qa-wiki" / "summaries" / "teaching-activities.md"
MKO3 = ROOT / "มคอ3"

TEX_TO_WIKI = {
    "4095101": "7015101",
    "4095102": "7015102",
    "4095103": "7015104",
    "4095104": "7015105",
    "4095105": "7015106",
    "4095106": "7015107",
    "4095107": "7015108",
    "4095108": "7015109",
    "4095109": "7015110",
    "4095110": "7015111",
    "4095111": "7015120",
    "4095112": "7015121",
    "7015101": "7015103",
    "7015102": "7015112",
    "7015103": "7015113",
    "7015104": "7015114",
    "7015105": "7015115",
    "7015106": "7015116",
    "7015107": "7015117",
    "7015108": "7015118",
    "7015109": "7015119",
    "7015110": "7015122",
    "7015111": "7015123",
    "7015112": "7015124",
    "7015901": "7015901",
    "7015902": "7015902",
    "7015903": "7015903",
    "7015904": "7015904",
    "7015905": "7015905",
    "7015906": "7015906",
    "7015907": "7015907",
    "7015908": "7015908",
}

# Teaching verbs (teacher activities) vs assessment markers
TEACH_VERBS = (
    "บรรยาย",
    "สาธิต",
    "แนะนำ",
    "ให้คำ",
    "มอบหมาย",
    "จัดกิจกรรม",
    "อภิปราย",
    "ยกตัวอย่าง",
    "นำเสนอ",
    "สอน",
    "เชิญ",
    "วิเคราะห์กรณี",
    "สร้างบรรยากาศ",
    "ติดตาม",
    "กำหนด",
    "ฝึก",
    "อธิบาย",
    "ใช้คำถาม",
    "Problem-based",
    "Project-based",
    "workshop",
    "Workshop",
)


def bullets_to_dash(text: str) -> str:
    items = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        line = re.sub(r"^[-–]\s*", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            items.append(line)
    return " - ".join(items)


def split_table_cells(block: str) -> list[str]:
    """Split a markdown table row block into cells by ' | ' boundaries."""
    cells: list[str] = []
    current: list[str] = []
    for line in block.splitlines():
        if " | " in line:
            parts = line.split(" | ")
            # First part continues current cell
            if current:
                current.append(parts[0].strip().lstrip("|").strip())
                cells.append("\n".join(current).strip())
                current = []
            else:
                if parts[0].strip():
                    current.append(parts[0].strip().lstrip("|").strip())
            for p in parts[1:]:
                cells.append(p.strip().rstrip("|").strip())
            current = []
        else:
            line = line.strip().lstrip("|").strip()
            if line:
                current.append(line)
    if current:
        cells.append("\n".join(current).strip())
    return [c for c in cells if c]


def parse_clo_block(block: str) -> tuple[str, str]:
    """Return (teaching_activities, assessment_methods) from a CLO table block."""
    cells = split_table_cells(block)
    # cells[0] is often CLO label; then env, teaching, learning, assessment
    if not cells:
        return "", ""
    # Drop CLO id cell
    start = 1 if re.match(r"CLO", cells[0], re.I) else 0
    rest = cells[start:]
    if len(rest) >= 3:
        teaching = bullets_to_dash(rest[1] if len(rest) >= 4 else rest[0])
        assessment = bullets_to_dash(rest[-1])
        return teaching, assessment
    if len(rest) == 2:
        # guess: teaching + assessment merged in learning/assess
        a, b = rest[0], rest[1]
        if any(m in b for m in ("การสอบ", "รายงาน", "โครงงาน", "แบบทดสอบ", "ประเมิน")):
            return bullets_to_dash(a), bullets_to_dash(b)
        return bullets_to_dash(a), bullets_to_dash(b)
    text = bullets_to_dash(rest[0])
    return text, ""


def parse_wiki_sections(text: str) -> dict[str, dict[str, tuple[str, str]]]:
    sections: dict[str, dict[str, tuple[str, str]]] = {}
    parts = re.split(r"\n---\n", text)
    for part in parts:
        m = re.search(r"^###\s+(\d{7})\s+", part, re.MULTILINE)
        if not m:
            continue
        code = m.group(1)
        clos: dict[str, tuple[str, str]] = {}
        for cm in re.finditer(r"\|\s*(CLO[\d,:]+[^|]*)\s*\|", part):
            clo_label = cm.group(1).strip()
            clo_keys = re.findall(r"CLO\d+", clo_label)
            start = cm.start()
            nxt = re.search(r"\n\|\s*CLO", part[cm.end() :])
            block = part[start : cm.end() + nxt.start()] if nxt else part[start:]
            teaching, assessment = parse_clo_block(block)
            # Fallback: extract lines with teach verbs for teaching column
            if not teaching or len(teaching) < 10:
                teach_lines = []
                assess_lines = []
                for line in block.splitlines():
                    l = line.strip().lstrip("-").strip()
                    if not l or l.startswith("CLO"):
                        continue
                    if any(
                        x in l
                        for x in (
                            "การสอบ",
                            "แบบทดสอบ",
                            "รายงาน",
                            "โครงงาน",
                            "ประเมิน",
                            "Portfolio",
                            "คุณภาพ",
                            "แฟ้ม",
                            "บทความ",
                            "แผน",
                            "ทักษะ",
                        )
                    ):
                        assess_lines.append(l)
                    elif any(v in l for v in TEACH_VERBS):
                        teach_lines.append(l)
                if teach_lines:
                    teaching = " - ".join(teach_lines)
                if assess_lines:
                    assessment = " - ".join(assess_lines)
            for ck in clo_keys:
                clos[ck] = (teaching, assessment)
        if clos:
            sections[code] = clos
    return sections


def add_iel_context(teaching: str, coursename: str) -> str:
    """Append short IEL / program alignment note once per course style."""
    if "IEL" in teaching:
        return teaching
    extras = []
    if any(
        w in teaching.lower()
        for w in ("project", "ปฏิบัติ", "workshop", "กรณีศึกษา", "โครงงาน")
    ):
        extras.append("ประสบการณ์เชิงบูรณาการ (IEL)")
    if "ท้องถิ่น" in coursename or "กรณีศึกษา" in teaching:
        extras.append("เชื่อมโยงการพัฒนาท้องถิ่น")
    if extras:
        return f"{teaching} [{', '.join(extras)}]"
    return teaching


def build_teaching_block(
    clos: dict[str, tuple[str, str]], tex_path: Path, coursename: str
) -> str:
    tex = tex_path.read_text(encoding="utf-8")
    clo_order = re.findall(r"\\cloitem\{(CLO\d+)\}", tex)
    rows = []
    for clo in clo_order:
        teach, assess = "", ""
        if clo in clos:
            teach, assess = clos[clo]
        else:
            for k, v in clos.items():
                if clo in re.findall(r"CLO\d+", k):
                    teach, assess = v
                    break
            else:
                continue
        teach = add_iel_context(teach, coursename)
        teach = teach.replace("&", "\\&")
        assess = assess.replace("&", "\\&")
        rows.append(f"  \\teachrow{{{clo}}}{{{teach}}}{{{assess}}}")
    body = "\n".join(rows)
    return (
        "% ----- 5. Teaching & assessment -----\n"
        "\\begin{teachingtable}\n"
        f"{body}\n"
        "\\end{teachingtable}"
    )


def replace_teaching_table(tex: str, new_block: str) -> str:
    pattern = (
        r"% ----- 5\. Teaching & assessment -----\n"
        r"\\begin\{teachingtable\}.*?\\end\{teachingtable\}"
    )
    if not re.search(pattern, tex, flags=re.DOTALL):
        raise ValueError("teachingtable block not found")
    return re.sub(pattern, lambda _: new_block, tex, count=1, flags=re.DOTALL)


def is_good_row(teach: str, assess: str) -> bool:
    """Detect already-complete teaching rows."""
    if not teach or not assess:
        return False
    if "|" in teach or "|" in assess:
        return False
    if any(v in teach for v in TEACH_VERBS) and len(assess) > 5:
        return True
    return False


def main():
    wiki_text = WIKI.read_text(encoding="utf-8")
    wiki_data = parse_wiki_sections(wiki_text)
    updated = []
    skipped = []
    for tex_file in sorted(MKO3.glob("AUN3_*.tex")):
        m = re.search(r"AUN3_(\d+)\.tex", tex_file.name)
        if not m:
            continue
        tex_code = m.group(1)
        wiki_code = TEX_TO_WIKI.get(tex_code)
        content = tex_file.read_text(encoding="utf-8")
        coursename_m = re.search(r"\\coursename\{([^}]+)\}", content)
        coursename = coursename_m.group(1) if coursename_m else ""

        # Keep files that already have complete teaching tables
        existing = re.findall(
            r"\\teachrow\{(CLO\d+)\}\{([^}]*)\}\{([^}]*)\}", content
        )
        if existing and all(is_good_row(t, a) for _, t, a in existing):
            skipped.append(f"{tex_file.name} (already complete)")
            continue

        if not wiki_code or wiki_code not in wiki_data:
            skipped.append(f"{tex_file.name} (no wiki data)")
            continue

        clos = wiki_data[wiki_code]
        new_block = build_teaching_block(clos, tex_file, coursename)
        try:
            new_content = replace_teaching_table(content, new_block)
        except ValueError as e:
            skipped.append(f"{tex_file.name}: {e}")
            continue
        tex_file.write_text(new_content, encoding="utf-8")
        updated.append(tex_file.name)

    print(f"Updated {len(updated)} files:")
    for u in updated:
        print(f"  {u}")
    if skipped:
        print(f"\nSkipped {len(skipped)}:")
        for s in skipped:
            print(f"  {s}")


if __name__ == "__main__":
    main()
