#!/usr/bin/env python3
"""
Generate report_meeting_*.tex from meeting_*.md — รูปแบบ กบ.วช. (อ้างอิง 145731สรุปบันทึกการประชุม ครั้งที่ 8/2568)
Run: python3 scripts/md_to_report_tex.py [--compile] [--force] [slug ...]
"""
from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_UNLESS_FORCE = {"meeting_2569-03-27_semester2-closeout"}
COMMITTEE_PROGRAM = "คณะกรรมการบริหารหลักสูตร วิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ (บัณฑิตศึกษา)"
COMMITTEE_UNI = "คณะกรรมการ/มติระดับมหาวิทยาลัย (สรุปที่เกี่ยวข้องกับหลักสูตร CPE\\&AI)"

SPECIAL = {
    "meeting_2566-11-20_stakeholder-consultation": (
        "รายงานสรุปการสัมภาษณ์ผู้มีส่วนได้ส่วนเสีย (หลักสูตร CPE\\&AI)",
        True,
    ),
    "meeting_2567-03-04_grad-committee-mko2": (COMMITTEE_UNI, False),
    "meeting_2567-03-21_academic-council-mko2": (COMMITTEE_UNI, False),
    "meeting_2567-12-11_faculty-committee-approval": (COMMITTEE_UNI, False),
    "meeting_2568-04-04_university-council-approval": (COMMITTEE_UNI, False),
}

MONTHS = {
    "มกราคม": 1, "กุมภาพันธ์": 2, "มีนาคม": 3, "เมษายน": 4, "พฤษภาคม": 5,
    "มิถุนายน": 6, "กรกฎาคม": 7, "สิงหาคม": 8, "กันยายน": 9, "ตุลาคม": 10,
    "พฤศจิกายน": 11, "ธันวาคม": 12,
}
DOW = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]


def escape_tex(s: str) -> str:
    s = s.replace("\\", "\\textbackslash{}")
    for a, b in [
        ("&", "\\&"), ("%", "\\%"), ("$", "\\$"), ("#", "\\#"),
        ("_", "\\_"), ("{", "\\{"), ("}", "\\}"),
        ("~", "\\textasciitilde{}"),
    ]:
        s = s.replace(a, b)
    return s


def thai_digits(s: str) -> str:
    return s.translate(str.maketrans("0123456789", "๐๑๒๓๔๕๖๗๘๙"))


def strip_md_inline(s: str) -> str:
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"\*([^*]+)\*", r"\1", s)
    return s.strip()


def format_time(t: str) -> str:
    t = thai_digits(t.strip())
    if "น." not in t:
        t = t + " น."
    return t


def format_meeting_date(raw: str) -> str:
    raw = raw.strip()
    if "พ.ศ." in raw or "วัน" in raw[:4]:
        return thai_digits(raw)
    m = re.match(r"(\d{1,2})\s+(\S+)\s+(\d{4})", raw)
    if m:
        d, mon, y = int(m.group(1)), m.group(2), int(m.group(3))
        if mon in MONTHS:
            # weekday optional — omit if unknown
            return f"วันที่ {thai_digits(str(d))} {mon} พ.ศ. {thai_digits(str(y))}"
    return thai_digits(raw)


def parse_participants(text: str) -> tuple[list[tuple], str]:
    rows = []
    pt = re.search(
        r"### ผู้เข้าร่วมประชุม\s*\n\n(\|.+\|(?:\n\|[^\n]+\|)+)",
        text,
        re.DOTALL,
    )
    if pt:
        lines = [ln for ln in pt.group(1).strip().split("\n") if ln.strip().startswith("|")]
        for ln in lines[2:]:
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if len(cells) >= 3 and cells[0].isdigit():
                name = cells[1]
                mtg_role = cells[2]  # ประธาน / กรรมการ
                org = cells[3] if len(cells) > 3 else ""
                rows.append((cells[0], name, org, mtg_role))
    absent = "ไม่มี"
    ab = re.search(r"\*\*ผู้ขาดประชุม:\*\*\s*(.+)", text)
    if ab:
        absent = ab.group(1).strip()
    return rows, absent


def extract_agenda_section(text: str) -> str:
    m = re.search(
        r"### ระเบียบวาระการประชุม\s*\n(.*?)(?=\n\*\*ปิดการประชุม|\n---\s*\n\*\*ปิด|\Z)",
        text,
        re.DOTALL,
    )
    return m.group(1) if m else ""


def parse_agenda_blocks(section: str) -> list[dict]:
    """Parse วาระที่ N (top) with optional N.M / N.M.K sub-items."""
    tops = list(re.finditer(r"^\*\*วาระที่\s*(\d+)\s*:\s*(.+?)\*\*\s*$", section, re.M))
    if not tops:
        return []

    blocks = []
    for i, m in enumerate(tops):
        num = m.group(1)
        title = strip_md_inline(m.group(2))
        start = m.end()
        end = tops[i + 1].start() if i + 1 < len(tops) else len(section)
        body = section[start:end]
        items = []
        pos = 0
        # Sub-agenda headers **4.1 title** or **4.1.1 title**
        sub_pat = re.compile(
            r"^\*\*(\d+\.\d+(?:\.\d+)?)\s+(.+?)\*\*\s*$",
            re.M,
        )
        subs = list(sub_pat.finditer(body))
        if not subs:
            items.append({"kind": "body", "text": body})
        else:
            if subs[0].start() > 0:
                items.append({"kind": "body", "text": body[: subs[0].start()]})
            for j, sm in enumerate(subs):
                sub_num = sm.group(1)
                sub_title = strip_md_inline(sm.group(2))
                s_start = sm.end()
                s_end = subs[j + 1].start() if j + 1 < len(subs) else len(body)
                sub_body = body[s_start:s_end]
                items.append(
                    {"kind": "sub", "num": sub_num, "title": sub_title, "text": sub_body}
                )
        blocks.append({"num": num, "title": title, "items": items})
    return blocks


def render_body(tex_lines: list, text: str) -> None:
    text = text.strip()
    if not text:
        return
    # Remove horizontal rules and signature blocks
    text = re.sub(r"^---+\s*$", "", text, flags=re.M)
    text = re.sub(r"\*ลงชื่อ\*.*", "", text, flags=re.DOTALL)

    chunks = re.split(r"\n\s*\n", text)
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk or chunk == "---":
            continue
        # Resolution inline in chunk
        res_m = re.match(r"^\*\*มติที่ประชุม:\*\*\s*(.+)$", chunk, re.S)
        if res_m:
            tex_lines.append(f"\\resolution{{{escape_tex(strip_md_inline(res_m.group(1)))}}}")
            continue
        if re.match(r"^-\s*ย้ายไป", chunk):
            tex_lines.append(f"\\agendanote{{{escape_tex(strip_md_inline(chunk.lstrip('- ')))}}}")
            continue

        lines = chunk.split("\n")
        # Numbered list block (1. ... 2. ...)
        if all(re.match(r"^\d+\.\s+", ln.strip()) or not ln.strip() for ln in lines if ln.strip()):
            numbered = [ln for ln in lines if re.match(r"^\d+\.\s+", ln.strip())]
            if numbered:
                tex_lines.append("\\begin{thailist}")
                for ln in numbered:
                    item = strip_md_inline(re.sub(r"^\d+\.\s+", "", ln.strip()))
                    tex_lines.append(f"  \\item {escape_tex(item)}")
                tex_lines.append("\\end{thailist}")
                continue

        # Bullet list
        if all(ln.strip().startswith("- ") or not ln.strip() for ln in lines if ln.strip()):
            bullets = [ln for ln in lines if ln.strip().startswith("- ")]
            if bullets:
                tex_lines.append("\\begin{itemize}")
                for ln in bullets:
                    tex_lines.append(f"  \\item {escape_tex(strip_md_inline(ln[2:].strip()))}")
                tex_lines.append("\\end{itemize}")
                continue

        # Inline bullets on one line: "foo: - a - b - c"
        if " - " in chunk and not chunk.strip().startswith("-"):
            head, *rest = re.split(r"\s+-\s+", chunk)
            if rest:
                if head.strip():
                    tex_lines.append(f"{escape_tex(strip_md_inline(head))}\n")
                tex_lines.append("\\begin{itemize}")
                for it in rest:
                    tex_lines.append(f"  \\item {escape_tex(strip_md_inline(it))}")
                tex_lines.append("\\end{itemize}")
                continue

        para = strip_md_inline(re.sub(r"\s+", " ", " ".join(ln.strip() for ln in lines)))
        if para:
            tex_lines.append(f"{escape_tex(para)}\n")


def parse_md(text: str) -> dict:
    meta = {}
    for key in ("วันที่", "เวลา", "สถานที่", "ประธาน", "เลขานุการ"):
        m = re.search(rf"\*\*{key}:\*\*\s*(.+)", text)
        if m:
            meta[key] = m.group(1).strip()

    title_m = re.search(r"^##\s+(.+)$", text, re.M)
    title = title_m.group(1).strip() if title_m else "การประชุม"

    participants, absent = parse_participants(text)

    close_m = re.search(r"\*\*ปิดการประชุม:\*\*\s*(.+)", text)
    close_time = close_m.group(1).strip() if close_m else ""

    agenda_section = extract_agenda_section(text)
    agenda_blocks = parse_agenda_blocks(agenda_section)

    return {
        "title": title,
        "meta": meta,
        "participants": participants,
        "absent": absent,
        "close_time": close_time,
        "agenda_blocks": agenda_blocks,
    }


def meeting_number_from_title(title: str) -> tuple[str, str]:
    m = re.search(r"ครั้งที่\s*([^\s—/]+)", title)
    no = thai_digits(m.group(1).strip()) if m else "๑"
    y = "๒๕๖๘"
    if "2569" in title:
        y = "๒๕๖๙"
    elif "2567" in title:
        y = "๒๕๖๗"
    elif "2566" in title:
        y = "๒๕๖๖"
    return no, y


def time_range(meta: dict) -> tuple[str, str]:
    t = meta.get("เวลา", "13.00 – 16.00 น.")
    if "–" in t or "-" in t:
        a, b = re.split(r"[–\-]", t, maxsplit=1)
        return format_time(a), format_time(b)
    return format_time(t), format_time(t)


def build_tex(slug: str, data: dict) -> str:
    committee, _is_report = SPECIAL.get(slug, (COMMITTEE_PROGRAM, False))
    meta = data["meta"]
    date_str = format_meeting_date(meta.get("วันที่", ""))
    place = escape_tex(meta.get("สถานที่", "ห้องประชุมคณะเทคโนโลยีอุตสาหกรรม มรอ."))
    chair_raw = meta.get("ประธาน", "")
    chair = escape_tex(chair_raw)
    secretary = escape_tex(meta.get("เลขานุการ", ""))
    mno, myear = meeting_number_from_title(data["title"])
    tstart, tend = time_range(meta)
    if data["close_time"]:
        tend = format_time(data["close_time"])

    lines = [
        f"% Auto-generated from {slug}.md (กบ.วช. format v2)",
        "\\documentclass{meetingminutes}",
        f"\\meetingcommittee{{{committee}}}",
        f"\\meetingnumber{{{mno}}}{{{myear}}}",
        f"\\meetingdate{{{date_str}}}",
        f"\\meetingplace{{{place}}}",
        f"\\meetingstart{{{tstart}}}",
        f"\\meetingend{{{tend}}}",
        "",
        "\\begin{document}",
        "\\maketitle",
        "",
        "\\psection{ผู้มาประชุม}",
        "\\begin{participants}",
    ]

    for i, (num, name, org, mtg_role) in enumerate(data["participants"], 1):
        n = thai_digits(str(num)) if str(num).isdigit() else thai_digits(str(i))
        name_tex = escape_tex(name)
        org_tex = escape_tex(org)
        role_tex = escape_tex(mtg_role)
        if len(org_tex) > 32:
            lines.append(f"  \\pmemberL{{{n}}}{{{name_tex}}}{{{org_tex}}}{{{role_tex}}}")
        else:
            lines.append(f"  \\pmember{{{n}}}{{{name_tex}}}{{{org_tex}}}{{{role_tex}}}")

    lines.append("\\end{participants}")
    lines.append("")
    if data["absent"] and data["absent"] != "ไม่มี":
        lines += ["\\psection{ผู้ไม่มาประชุม}", f"\\noindent {escape_tex(data['absent'])}\\par", ""]
    else:
        lines += ["\\psection{ผู้ไม่มาประชุม}", "\\noindent ไม่มี\\par", ""]

    lines += [
        "\\startmeeting",
        f"\\openingchair{{{chair}}}{{กล่าวเปิดการประชุมและดำเนินการประชุมตามระเบียบวาระ ดังนี้}}",
        "",
    ]

    for block in data["agenda_blocks"]:
        nth = thai_digits(block["num"])
        lines.append(f"\\agenda{{{nth}}}{{{escape_tex(block['title'])}}}")
        for item in block["items"]:
            if item["kind"] == "sub":
                parts = item["num"].split(".")
                if len(parts) == 3:
                    lines.append(
                        f"\\subsubagenda{{{thai_digits(item['num'])}}}{{{escape_tex(item['title'])}}}"
                    )
                else:
                    lines.append(
                        f"\\subagenda{{{thai_digits(item['num'])}}}{{{escape_tex(item['title'])}}}"
                    )
                render_body(lines, item["text"])
            else:
                render_body(lines, item["text"])
        lines.append("")

    lines += [
        "\\adjournmeeting",
        "",
        "\\begin{sigblock}",
        f"\\typist{{{secretary}}}",
        f"\\reviewer{{{escape_tex(meta.get('ประธาน', 'กรรมการ'))}}}{{กรรมการ}}",
        f"\\chairsig{{{chair}}}{{ประธานการประชุม}}",
        "\\end{sigblock}",
        "",
        "\\end{document}",
        "",
    ]
    return "\n".join(lines)


def compile_tex(tex_path: Path) -> bool:
    for _ in range(2):
        subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-output-directory", str(tex_path.parent), str(tex_path)],
            cwd=tex_path.parent,
            capture_output=True,
            text=True,
        )
    return (tex_path.parent / (tex_path.stem + ".pdf")).exists()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--compile", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("slugs", nargs="*")
    args = ap.parse_args()

    mds = sorted(ROOT.glob("meeting_*.md"))
    if args.slugs:
        mds = [ROOT / f"{s}.md" if not s.endswith(".md") else ROOT / s for s in args.slugs]

    ok = 0
    for md_path in mds:
        slug = md_path.stem
        if slug in SKIP_UNLESS_FORCE and not args.force:
            print(f"  skip {slug} (hand-crafted)")
            continue
        out = ROOT / f"report_{slug}.tex"
        data = parse_md(md_path.read_text(encoding="utf-8"))
        out.write_text(build_tex(slug, data), encoding="utf-8")
        print(f"  wrote {out.name}")
        if args.compile and compile_tex(out):
            print("    pdf OK")
        ok += 1
    print(f"\nDone: {ok}/{len(mds)}")


if __name__ == "__main__":
    main()
