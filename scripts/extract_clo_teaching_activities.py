"""Extract teaching activity tables from CLO DOCX.
Strategy: teaching activity tables appear 3rd in each course block (CLO, Bloom's, Activities).
Match them in order against the course list from clo-all-courses-detailed.md."""
from __future__ import annotations
from pathlib import Path
import re
import docx

root = Path(__file__).resolve().parents[1]
wiki = root / "aun-qa-wiki"
src = root / "clo-courses-temp.docx"

doc = docx.Document(str(src))

# ---------- Extract all tables ----------
def table_to_rows(tbl) -> list[list[str]]:
    rows = []
    for row in tbl.rows:
        cells, prev = [], None
        for cell in row.cells:
            t = cell.text.strip()
            if t != prev:
                cells.append(t)
            prev = t
        rows.append(cells)
    return rows

TEACHING_ACT_HEADERS = {
    "Learning Environment", "Leaning Environment",
    "กิจกรรมการเรียนการสอน", "สภาพแวดล้อมการเรียนรู้",
}

def is_teaching_activity_table(rows):
    if not rows:
        return False
    r0 = " ".join(rows[0])
    return any(h in r0 for h in TEACHING_ACT_HEADERS)

all_tables = [table_to_rows(t) for t in doc.tables]
act_tables = [r for r in all_tables if is_teaching_activity_table(r)]
print(f"Teaching activity tables: {len(act_tables)}")

# ---------- Get course order from clo-all-courses-detailed.md ----------
detailed = (wiki / "summaries" / "clo-all-courses-detailed.md").read_text(encoding="utf-8")
course_blocks = re.split(r"\n(?=### \d{7})", detailed)

ordered_courses: list[dict] = []
for block in course_blocks:
    m = re.match(r"### (\d{7})\s+(.+)", block)
    if m:
        ordered_courses.append({"code": m.group(1), "name": m.group(2).strip()})

print(f"Courses in detailed.md: {len(ordered_courses)}")

# ---------- Pair tables with courses ----------
# If counts match, pair by index; otherwise best-effort
pairs: list[tuple[dict, list[list[str]]]] = []
if len(act_tables) == len(ordered_courses):
    pairs = list(zip(ordered_courses, act_tables))
elif len(act_tables) < len(ordered_courses):
    # Fewer tables: skip courses without data
    pairs = list(zip(ordered_courses[:len(act_tables)], act_tables))
else:
    pairs = list(zip(ordered_courses, act_tables[:len(ordered_courses)]))

print(f"Pairs created: {len(pairs)}")

# ---------- Collect all unique activity types ----------
all_activity_types: set[str] = set()
SKIP_HEADERS = {"Learning Environment", "Leaning Environment",
                "กิจกรรมการเรียนการสอน", "Activity"}

for course, rows in pairs:
    for row in rows[1:]:  # skip header
        if row and row[0].strip():
            t = row[0].strip()
            if t not in SKIP_HEADERS:
                all_activity_types.add(t)

# ---------- Build output ----------
out_lines: list[str] = [
    "---",
    "title: กิจกรรมการเรียนการสอน (Teaching & Learning Activities) — ทุกรายวิชา",
    "created: 2026-05-12",
    "updated: 2026-05-12",
    "type: summary",
    "tags: [curriculum, teaching, clo, learning-environment, aun-qa, criterion-3]",
    "sources: [รวมเล่ม CLO รายวิชา.docx]",
    "confidence: high",
    "contested: false",
    "---",
    "",
    "# กิจกรรมการเรียนการสอน (Teaching & Learning Activities)",
    "",
    "> สกัดจากตาราง Learning Environment / กิจกรรมการเรียนการสอน ในเอกสาร CLO รายวิชา",
    "> ใช้อ้างอิงสำหรับ AUN-QA **Criterion 3** (Teaching & Learning Approach) และ **Criterion 4** (Student Assessment)",
    "",
    f"> **รวม {len(pairs)} รายวิชา**",
    "",
]

for course, rows in pairs:
    out_lines.append("---")
    out_lines.append(f"### {course['code']} {course['name']}")
    out_lines.append("")
    if not rows or len(rows) < 2:
        out_lines.append("_(ไม่มีข้อมูล)_")
        out_lines.append("")
        continue

    header = rows[0]
    col_count = len(header)
    out_lines.append("| " + " | ".join(str(h)[:50] for h in header) + " |")
    out_lines.append("|" + "|".join(["---"] * col_count) + "|")
    for row in rows[1:]:
        while len(row) < col_count:
            row.append("")
        out_lines.append("| " + " | ".join(str(c)[:60] for c in row[:col_count]) + " |")
    out_lines.append("")

# ---------- Summary of activity types ----------
out_lines += [
    "---",
    "## สรุปรูปแบบกิจกรรมการสอนที่ใช้ในหลักสูตร (ทุกรายวิชา)",
    "",
    "> รวบรวมจากทุกรายวิชา — แสดงความหลากหลายของ Teaching Methods",
    "",
]
for act in sorted(all_activity_types):
    if act:
        out_lines.append(f"- {act}")
out_lines.append("")

# Write
out_path = wiki / "summaries" / "teaching-activities.md"
out_path.write_text("\n".join(out_lines), encoding="utf-8")
print(f"WROTE {out_path}")
print(f"Lines: {len(out_lines)}")
print(f"Unique activity types: {len(all_activity_types)}")

# Cleanup
import os
if src.exists():
    os.remove(src)
    print("Cleaned up temp file")
