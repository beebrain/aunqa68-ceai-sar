"""Generate CLO-YLO mapping page from clo-all-courses-detailed.md + course schedule."""
from __future__ import annotations
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
wiki = root / "aun-qa-wiki"

# ---------- Load CLO data from generated summary ----------
clo_src = wiki / "summaries" / "clo-all-courses-detailed.md"
content = clo_src.read_text(encoding="utf-8")

# Parse courses: each section starts with "### <code> <name>"
course_blocks = re.split(r"\n(?=### \d{7})", content)

def parse_block(block: str) -> dict | None:
    m = re.match(r"### (\d{7})\s+(.+)", block)
    if not m:
        return None
    code = m.group(1)
    name = m.group(2).strip()

    credits_m = re.search(r"\*\*หน่วยกิต\*\*:\s*(.+)", block)
    credits = credits_m.group(1).strip() if credits_m else "–"

    desc_m = re.search(r"#### คำอธิบายรายวิชา\n\n(.+?)(?=\n\n|####)", block, re.DOTALL)
    desc = desc_m.group(1).strip()[:120] if desc_m else ""

    # CLO table rows: | CLOn | text | Bloom | PLO |
    clos = []
    for row in re.finditer(r"\|\s*(CLO\d+)\s*\|\s*(.+?)\s*\|\s*(\S+)\s*\|\s*(.+?)\s*\|", block):
        clos.append({
            "id": row.group(1),
            "text": row.group(2).strip(),
            "bloom": row.group(3).strip(),
            "plo": [p.strip() for p in row.group(4).split(",") if p.strip() != "–"],
        })
    return {"code": code, "name": name, "credits": credits, "desc": desc, "clos": clos}

courses: dict[str, dict] = {}
for block in course_blocks:
    parsed = parse_block(block)
    if parsed:
        courses[parsed["code"]] = parsed

# ---------- Course schedule ----------
# Source: yleo.md + raw extract Table 7
SCHEDULE = {
    "ปีที่ 1 ภาค 1": ["7015101", "7015906", "7015907"],
    "ปีที่ 1 ภาค 2": ["7015102", "7015103", "7015908"],
    "ปีที่ 2 ภาค 1 (แผน 1)": ["7015901"],
    "ปีที่ 2 ภาค 2 (แผน 1)": ["7015902"],
    "ปีที่ 2 ภาค 3 (แผน 1)": ["7015903"],
    "ปีที่ 2 ภาค 1 (แผน 2)": ["7015904"],
    "ปีที่ 2 ภาค 2 (แผน 2)": ["7015905"],
}

# Elective pool
ELECTIVES = [
    "7015104", "7015105", "7015106", "7015107", "7015108", "7015109",
    "7015110", "7015111", "7015112", "7015113", "7015114", "7015115",
    "7015116", "7015117", "7015118", "7015119", "7015120", "7015121",
    "7015122", "7015123", "7015124",
]

# PLO descriptions (short)
PLO_DESC = {
    "PLO1": "สร้างสรรค์ผลงาน/นวัตกรรมด้วยซอฟต์แวร์/ฮาร์ดแวร์",
    "PLO2": "ประยุกต์ใช้ความรู้แก้ปัญหาองค์กร/ชุมชน",
    "PLO3": "สร้างองค์ความรู้/ต้นแบบนวัตกรรมด้าน AI",
    "PLO4": "จรรยาบรรณวิชาชีพ",
    "PLO5": "คิดวิเคราะห์/สื่อสาร/ทำงานร่วมกัน/เรียนรู้ตลอดชีวิต",
}

# YLO derivations
YLO = {
    "YLO1": {
        "label": "ผลการเรียนรู้ปีที่ 1 — ฐานความรู้และทักษะ AI/ML + วิจัย",
        "desc": "หลังสิ้นปีที่ 1 ผู้เรียนสามารถอธิบาย/ประยุกต์/วิเคราะห์ AI&ML "
                "เขียนโปรแกรม ML ทำงานวิจัยตามระเบียบวิธี ติดตามเทคโนโลยีใหม่ "
                "และนำเสนอบทความวิจัยในสัมมนาได้",
        "plos": ["PLO1", "PLO2", "PLO3", "PLO4", "PLO5"],
        "sems": ["ปีที่ 1 ภาค 1", "ปีที่ 1 ภาค 2"],
    },
    "YLO2": {
        "label": "ผลการเรียนรู้ปีที่ 2 — วิจัย/นวัตกรรมเชิงลึก (แผน 1: วิทยานิพนธ์)",
        "desc": "หลังสิ้นปีที่ 2 แผน 1 ผู้เรียนสามารถออกแบบ/ดำเนิน/รายงานงานวิจัย "
                "สร้างบทความวิชาการ และนำเสนอผลงานในการประชุมวิชาการได้",
        "plos": ["PLO1", "PLO2", "PLO3", "PLO4", "PLO5"],
        "sems": ["ปีที่ 2 ภาค 1 (แผน 1)", "ปีที่ 2 ภาค 2 (แผน 1)", "ปีที่ 2 ภาค 3 (แผน 1)"],
    },
    "YLO2b": {
        "label": "ผลการเรียนรู้ปีที่ 2 — พัฒนานวัตกรรมประยุกต์ใช้งาน (แผน 2: สารนิพนธ์)",
        "desc": "หลังสิ้นปีที่ 2 แผน 2 ผู้เรียนสามารถนำความรู้ไปพัฒนาสารนิพนธ์ "
                "ประยุกต์ใช้งานจริง วิเคราะห์ข้อมูล และนำเสนอผลงานสอบป้องกันได้",
        "plos": ["PLO1", "PLO2", "PLO3", "PLO4", "PLO5"],
        "sems": ["ปีที่ 2 ภาค 1 (แผน 2)", "ปีที่ 2 ภาค 2 (แผน 2)"],
    },
}

# ---------- Build aggregate PLO coverage per semester ----------
def get_plos_covered(codes: list[str]) -> dict[str, list[str]]:
    """Return {PLO: [CLO descriptions]} for a set of courses."""
    coverage: dict[str, list[str]] = {}
    for code in codes:
        c = courses.get(code)
        if not c:
            continue
        for clo in c["clos"]:
            for plo in clo["plo"]:
                if plo not in coverage:
                    coverage[plo] = []
                coverage[plo].append(f"{code} {clo['id']}")
    return coverage


# ---------- Render ----------
lines: list[str] = [
    "---",
    "title: CLO–YLO Mapping (ความสัมพันธ์ CLO กับผลการเรียนรู้รายปี)",
    "created: 2026-05-11",
    "updated: 2026-05-11",
    "type: summary",
    "tags: [curriculum, clo, plo, mapping, aun-qa]",
    "sources: [summaries/clo-all-courses-detailed.md, concepts/yleo.md]",
    "confidence: high",
    "contested: false",
    "---",
    "",
    "# CLO–YLO Mapping",
    "",
    "> แสดงความสัมพันธ์ระหว่าง CLO (Course Learning Outcomes) ของแต่ละรายวิชา กับ YLO "
    "(Year Learning Outcomes — ผลการเรียนรู้รายปี ที่ derive จากโครงสร้างหลักสูตร) "
    "และ PLO (Program Learning Outcomes)",
    "",
    "## โครงสร้างความสัมพันธ์",
    "",
    "```",
    "PEO  →  PLO1–PLO5  →  YLO1 / YLO2 / YLO2b",
    "                         ↑",
    "              CLO (รายวิชา แต่ละ CLO → PLO)",
    "```",
    "",
    "## PLOs ของหลักสูตร",
    "",
]

for plo, desc in PLO_DESC.items():
    lines.append(f"- **{plo}**: {desc}")
lines.append("")

# ---- YLO sections ----
for ylo_key, ylo in YLO.items():
    lines.append(f"---")
    lines.append(f"## {ylo_key}: {ylo['label']}")
    lines.append("")
    lines.append(f"> {ylo['desc']}")
    lines.append("")

    # Collect all courses for this YLO
    all_codes: list[str] = []
    for sem in ylo["sems"]:
        all_codes.extend(SCHEDULE.get(sem, []))

    # Per semester
    for sem in ylo["sems"]:
        codes = SCHEDULE.get(sem, [])
        if not codes:
            continue
        lines.append(f"### {sem}")
        lines.append("")
        for code in codes:
            c = courses.get(code)
            if not c:
                lines.append(f"- {code} (ไม่พบข้อมูล)")
                continue
            lines.append(f"#### {code} {c['name']}")
            lines.append("")
            if c.get("desc"):
                lines.append(f"> {c['desc'][:100]}...")
                lines.append("")
            if c["clos"]:
                lines.append("| CLO | คำอธิบาย (ย่อ) | Bloom's | PLO |")
                lines.append("|-----|----------------|---------|-----|")
                for clo in c["clos"]:
                    txt = clo["text"][:70] + ("…" if len(clo["text"]) > 70 else "")
                    plo_str = ", ".join(clo["plo"]) if clo["plo"] else "–"
                    lines.append(f"| {clo['id']} | {txt} | {clo['bloom']} | {plo_str} |")
                lines.append("")
            else:
                lines.append("_(ไม่มีข้อมูล CLO)_")
                lines.append("")

    # PLO coverage summary for this YLO
    coverage = get_plos_covered(all_codes)
    lines.append(f"### PLO Coverage สรุป ({ylo_key})")
    lines.append("")
    lines.append("| PLO | ความหมาย | CLO ที่รองรับ |")
    lines.append("|-----|----------|-------------|")
    for plo in ["PLO1", "PLO2", "PLO3", "PLO4", "PLO5"]:
        plo_desc = PLO_DESC.get(plo, "")
        clo_list = coverage.get(plo, [])
        clo_str = ", ".join(clo_list[:6])
        if len(clo_list) > 6:
            clo_str += f" (+{len(clo_list)-6})"
        mark = "✓" if clo_list else "–"
        lines.append(f"| {plo} | {plo_desc} | {mark} {clo_str} |")
    lines.append("")

# ---- Elective CLO-PLO matrix ----
lines += [
    "---",
    "## วิชาเฉพาะด้านเลือก — CLO–PLO Matrix",
    "",
    "> วิชาเลือกจะถูกเลือกเรียนในปีที่ 2 ตามแผนการศึกษา "
    "ผู้เรียนควรเลือกวิชาที่ทำให้ PLO ที่ยังขาดได้รับการรองรับ",
    "",
    "| รหัส | ชื่อวิชา | PLO1 | PLO2 | PLO3 | PLO4 | PLO5 |",
    "|------|----------|:----:|:----:|:----:|:----:|:----:|",
]
for code in ELECTIVES:
    c = courses.get(code)
    if not c:
        continue
    covered: set[str] = set()
    for clo in c["clos"]:
        covered.update(clo["plo"])
    row = [
        code,
        c["name"][:40],
        "✓" if "PLO1" in covered else "",
        "✓" if "PLO2" in covered else "",
        "✓" if "PLO3" in covered else "",
        "✓" if "PLO4" in covered else "",
        "✓" if "PLO5" in covered else "",
    ]
    lines.append("| " + " | ".join(row) + " |")
lines.append("")

# ---- Full CLO-PLO cross-reference table ----
lines += [
    "---",
    "## ตารางรวม CLO–PLO ทุกวิชา (Cross-reference)",
    "",
    "> ตารางนี้รวม CLO ทุกรายวิชา พร้อม Bloom's level และ PLO ที่สนับสนุน "
    "เพื่อใช้ตรวจสอบ alignment ตามเกณฑ์ AUN-QA",
    "",
    "| รหัส | ชื่อวิชา | CLO | Bloom's | PLO |",
    "|------|----------|-----|---------|-----|",
]
ordered_codes = (
    ["7015101", "7015102", "7015906", "7015103", "7015907", "7015908"]
    + ["7015901", "7015902", "7015903", "7015904", "7015905"]
    + ELECTIVES
)
for code in ordered_codes:
    c = courses.get(code)
    if not c:
        continue
    name_short = c["name"][:35]
    for clo in c["clos"]:
        plo_str = ", ".join(clo["plo"]) if clo["plo"] else "–"
        txt = clo["text"][:55] + ("…" if len(clo["text"]) > 55 else "")
        lines.append(f"| {code} | {name_short} | {clo['id']} | {clo['bloom']} | {plo_str} |")
lines.append("")

# ---- Write ----
out = wiki / "summaries" / "clo-ylo-mapping.md"
out.write_text("\n".join(lines), encoding="utf-8")
print(f"WROTE {out}")
print(f"Lines: {len(lines)}")
print(f"Courses processed: {len([c for c in ordered_codes if c in courses])}")
