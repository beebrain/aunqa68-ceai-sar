"""Extract AUNQA-X-Y-Z evidence codes + URLs from support-data-extract.md
and write a structured evidence-index.md wiki page."""
from __future__ import annotations
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
wiki = root / "aun-qa-wiki"

raw = (wiki / "raw" / "support-data-extract.md").read_text(encoding="utf-8")

# Pattern: AUNQA-C-S-N  description  optional_url
CODE_RE = re.compile(
    r"AUNQA-(\d+)-(\d+[a-z]?)-(\d+[a-z]?)\s+(.*?)(?:\s+(https?://\S+))?$",
    re.MULTILINE,
)

# Also catch lines that are just a URL after an AUNQA line
# Some evidence items have the URL on the next line or inline in paragraph text

# First pass: collect all evidence lines
evidence: list[dict] = []
lines = raw.splitlines()

i = 0
while i < len(lines):
    line = lines[i].strip()
    # strip [PNNNN] [Style] prefix
    m_prefix = re.match(r"\[P\d+\]\s+\[.+?\]\s+(.*)", line)
    content = m_prefix.group(1) if m_prefix else line

    m = re.match(
        r"(AUNQA-(\d+)-(\d+[a-z]?)-(\d+[a-z]?))\s*(.*)", content
    )
    if m:
        code = m.group(1)
        criteria = m.group(2)
        sub = m.group(3)
        num = m.group(4)
        rest = m.group(5).strip()

        # Extract URL from rest
        url_m = re.search(r"(https?://\S+)", rest)
        url = url_m.group(1) if url_m else ""
        desc = re.sub(r"https?://\S+", "", rest).strip()

        # Check next non-empty line for bare URL if we didn't find one
        if not url:
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                next_content = lines[j].strip()
                np = re.match(r"\[P\d+\]\s+\[.+?\]\s+(.*)", next_content)
                nc = np.group(1) if np else next_content
                if re.match(r"https?://", nc.strip()):
                    url = nc.strip()

        evidence.append({
            "code": code,
            "criteria": criteria,
            "sub": sub,
            "num": num,
            "desc": desc,
            "url": url,
        })
    i += 1

# Group by criteria → sub-criterion
from collections import defaultdict
by_criteria: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
for ev in evidence:
    key = f"C{ev['criteria']}.{ev['sub']}"
    by_criteria[ev["criteria"]][key].append(ev)

# Criteria labels
CRITERIA_LABELS = {
    "4": "Criteria 4 — การประเมินผู้เรียน (Student Assessment)",
    "5": "Criteria 5 — บุคลากรสายวิชาการ (Academic Staff)",
    "6": "Criteria 6 — บริการสนับสนุนผู้เรียน (Student Support Service)",
    "7": "Criteria 7 — สิ่งอำนวยความสะดวกและโครงสร้างพื้นฐาน (Facilities and Infrastructure)",
}

SUB_LABELS = {
    "4.2": "นโยบายการประเมินและการอุทธรณ์",
    "4.3": "มาตรฐานและกระบวนการประเมินความก้าวหน้า",
    "4.7": "ทบทวนและปรับปรุงการประเมินต่อเนื่อง",
    "5.1": "แผนอัตรากำลังอาจารย์",
    "5.2": "ภาระงานอาจารย์",
    "5.3": "สมรรถนะอาจารย์",
    "5.4": "การจัดสรรภาระงานตามคุณสมบัติ",
    "5.5": "การเลื่อนตำแหน่งบนฐานคุณธรรม",
    "5.6": "สิทธิ สวัสดิการ บทบาทและความรับผิดชอบ",
    "5.7": "การฝึกอบรมและพัฒนาบุคลากร",
    "5.8": "การบริหารผลการปฏิบัติงาน",
    "6.1": "นโยบายและกระบวนการรับนักศึกษา",
    "6.2": "แผนระยะสั้น/ยาวสำหรับบริการสนับสนุน",
    "6.3": "ระบบติดตามความก้าวหน้าผู้เรียน",
    "6.4": "กิจกรรมเสริมหลักสูตรและการแข่งขัน",
    "6.5": "สมรรถนะเจ้าหน้าที่สนับสนุนผู้เรียน",
    "6.6": "การประเมินบริการสนับสนุนผู้เรียน",
    "7.1": "ทรัพยากรทางกายภาพ (อุปกรณ์/ห้องเรียน/IT)",
    "7.3": "ห้องสมุดดิจิทัล",
    "7.4": "ระบบเทคโนโลยีสารสนเทศ",
    "7.5": "โครงสร้างพื้นฐานคอมพิวเตอร์และเครือข่าย",
    "7.6": "สิ่งแวดล้อม สุขภาพ ความปลอดภัย และผู้พิการ",
    "7.7": "สภาพแวดล้อมที่เอื้อต่อการเรียนรู้",
    "7.8": "สมรรถนะเจ้าหน้าที่สนับสนุนสิ่งอำนวยความสะดวก",
    "7.9": "การประเมินและปรับปรุงคุณภาพสิ่งอำนวยความสะดวก",
}

# Build output
out_lines: list[str] = [
    "---",
    "title: Evidence Index — AUNQA หลักฐานสายสนับสนุน (Criteria 4–7)",
    "created: 2026-05-12",
    "updated: 2026-05-12",
    "type: summary",
    "tags: [aun-qa, evidence, criteria-4, criteria-5, criteria-6, criteria-7]",
    "sources: [raw/support-data-extract.md]",
    "confidence: high",
    "contested: false",
    "---",
    "",
    "# Evidence Index — หลักฐาน AUN-QA สายสนับสนุน (Criteria 4–7)",
    "",
    "> ดัชนีหลักฐานทั้งหมดจากเอกสาร `ข้อมูลพื้นฐาน AUN-QA-สายสนับสนุน30042569(1).docx`",
    "> จัดตาม Criteria → Sub-criterion → รหัสหลักฐาน (AUNQA-C-S-N) พร้อมชื่อเอกสารและ URL",
    "",
    f"> **รวมหลักฐานทั้งหมด: {len(evidence)} รายการ**",
    "",
]

total_with_url = sum(1 for e in evidence if e["url"])
out_lines.append(f"> มี URL ที่เข้าถึงได้ออนไลน์: **{total_with_url} รายการ**")
out_lines.append("")

for criteria_key in sorted(by_criteria.keys()):
    label = CRITERIA_LABELS.get(criteria_key, f"Criteria {criteria_key}")
    out_lines.append(f"---")
    out_lines.append(f"## {label}")
    out_lines.append("")

    sub_dict = by_criteria[criteria_key]
    for sub_key in sorted(sub_dict.keys(), key=lambda x: [int(p) if p.isdigit() else p for p in re.split(r'[.\-]', x)]):
        sub_num = sub_key.replace("C", "")  # e.g. "4.2"
        sub_label = SUB_LABELS.get(sub_num, "")
        header = f"### {sub_key}" + (f" — {sub_label}" if sub_label else "")
        out_lines.append(header)
        out_lines.append("")
        out_lines.append("| รหัส | เอกสาร/ชื่อหลักฐาน | URL |")
        out_lines.append("|------|---------------------|-----|")

        for ev in sub_dict[sub_key]:
            desc = ev["desc"][:80] + ("…" if len(ev["desc"]) > 80 else "")
            url_cell = f"[เปิด]({ev['url']})" if ev["url"] else "—"
            out_lines.append(f"| `{ev['code']}` | {desc} | {url_cell} |")

        out_lines.append("")

# Quick access: evidence with URLs only
out_lines += [
    "---",
    "## ดัชนีลิงก์ออนไลน์ทั้งหมด (เรียงตามรหัส)",
    "",
    "| รหัส | ชื่อเอกสาร | URL |",
    "|------|-----------|-----|",
]
for ev in sorted(evidence, key=lambda e: e["code"]):
    if ev["url"]:
        desc = ev["desc"][:70] + ("…" if len(ev["desc"]) > 70 else "")
        out_lines.append(f"| `{ev['code']}` | {desc} | {ev['url']} |")
out_lines.append("")

# Stats
out_lines += [
    "---",
    "## สถิติหลักฐาน",
    "",
    f"| Criteria | จำนวนหลักฐาน | มี URL |",
    "|----------|-------------|--------|",
]
for ck in sorted(by_criteria.keys()):
    items = [e for sub in by_criteria[ck].values() for e in sub]
    with_url = sum(1 for e in items if e["url"])
    out_lines.append(f"| C{ck} | {len(items)} | {with_url} |")
out_lines.append(f"| **รวม** | **{len(evidence)}** | **{total_with_url}** |")
out_lines.append("")

# Write
out_path = wiki / "summaries" / "evidence-index.md"
out_path.write_text("\n".join(out_lines), encoding="utf-8")
print(f"WROTE {out_path}")
print(f"Total evidence items: {len(evidence)}")
print(f"Items with URL: {total_with_url}")
for ck in sorted(by_criteria.keys()):
    items = [e for sub in by_criteria[ck].values() for e in sub]
    print(f"  C{ck}: {len(items)} items")
