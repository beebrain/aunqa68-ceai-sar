#!/usr/bin/env python3
"""
Build static AUN-QA reference site from aun-qa-wiki/ into docs/ (GitHub Pages).
Run from repo root: python3 website/build.py
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "aun-qa-wiki"
OUT = ROOT / "docs"
STATIC = Path(__file__).resolve().parent / "static"

SKIP_FILES = {"index.md", "log.md", "SCHEMA.md"}

# Friendly URL slugs for key pages
SLUG_OVERRIDES: dict[str, str] = {
    "entities/หลักสูตรวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์-บัณฑิตศึกษา": "program",
    "entities/มหาวิทยาลัยราชภัฏอุตรดิตถ์": "university",
    "concepts/aun-qa": "aun-qa",
    "concepts/criterion-1-plo": "criteria/1",
    "concepts/criterion-2-structure": "criteria/2",
    "concepts/criterion-3-teaching-learning": "criteria/3",
    "concepts/criterion-4-student-assessment": "criteria/4",
    "concepts/criterion-5-academic-staff": "criteria/5",
    "concepts/criterion-6-student-support": "criteria/6",
    "concepts/criterion-7-facilities": "criteria/7",
    "concepts/criterion-8-output-outcomes": "criteria/8",
    "summaries/clo-all-courses": "clo",
    "summaries/evidence-index": "evidence",
    "summaries/teaching-activities": "teaching",
    "summaries/support-data-summary": "support",
    "summaries/example-sar-mbm-66": "example-sar",
    "summaries/clo-ylo-mapping": "clo-mapping",
    "summaries/clo-all-courses-detailed": "clo-detailed",
    "guidelines/00_overview": "guidelines/overview",
    "guidelines/01_criterion1_plo": "guidelines/1",
    "guidelines/02_criterion2_structure": "guidelines/2",
    "guidelines/03_criterion3_teaching": "guidelines/3",
    "guidelines/04_criterion4_assessment": "guidelines/4",
    "guidelines/05_criterion5_staff": "guidelines/5",
    "guidelines/06_criterion6_support": "guidelines/6",
    "guidelines/07_criterion7_facilities": "guidelines/7",
    "guidelines/08_criterion8_outcomes": "guidelines/8",
    "raw/example66-mbm-extract": "example-sar-structure",
}

NAV = [
    {
        "label": "หลักสูตร",
        "items": [
            ("program", "ข้อมูลหลักสูตร CE&AI"),
            ("university", "มหาวิทยาลัยราชภัฏอุตรดิตถ์"),
            ("aun-qa", "AUN-QA"),
        ],
    },
    {
        "label": "เกณฑ์ (SAR)",
        "items": [(f"criteria/{i}", f"Criterion {i}") for i in range(1, 9)],
    },
    {
        "label": "แนวทาง (อ.ที่ปรึกษา)",
        "items": [
            ("guidelines/overview", "ภาพรวม & Rating Scale"),
        ]
        + [(f"guidelines/{i}", f"แนวทาง C{i}") for i in range(1, 9)],
    },
    {
        "label": "ข้อมูล & หลักฐาน",
        "items": [
            ("clo", "CLO ทุกรายวิชา"),
            ("clo-mapping", "CLO–YLO–PLO Mapping"),
            ("teaching", "กิจกรรมการสอน"),
            ("evidence", "ดัชนีหลักฐาน"),
            ("support", "ข้อมูลสายสนับสนุน"),
            ("example-sar", "ตัวอย่าง SAR (MBM 66)"),
        ],
    },
]

CRITERION_LABELS = {
    1: "Expected Learning Outcomes",
    2: "Programme Structure & Content",
    3: "Teaching & Learning",
    4: "Student Assessment",
    5: "Academic Staff",
    6: "Student Support",
    7: "Facilities & Infrastructure",
    8: "Output & Outcomes",
}


def ensure_markdown() -> None:
    try:
        import markdown  # noqa: F401
    except ImportError:
        venv_dir = Path(__file__).parent / ".venv"
        venv_python = venv_dir / "bin" / "python"
        if not venv_python.exists():
            subprocess.check_call([sys.executable, "-m", "venv", str(venv_dir)])
            subprocess.check_call(
                [str(venv_python), "-m", "pip", "install", "-q", "-r", str(Path(__file__).parent / "requirements.txt")]
            )
        if str(venv_dir / "lib") not in sys.path[0]:
            site = venv_dir / "lib"
            for p in site.glob("python*/site-packages"):
                sys.path.insert(0, str(p))
                break
        import markdown  # noqa: F401


def slug_for(rel_key: str) -> str:
    if rel_key in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[rel_key]
    return rel_key.replace("/", "-")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}, text
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    body = text[m.end() :]
    return meta, body


def discover_pages() -> list[tuple[Path, str, str]]:
    """Return (path, rel_key, slug) for each wiki page."""
    pages: list[tuple[Path, str, str]] = []
    if not WIKI.is_dir():
        print(f"ERROR: Wiki not found at {WIKI}", file=sys.stderr)
        sys.exit(1)
    for md in sorted(WIKI.rglob("*.md")):
        if md.name in SKIP_FILES:
            continue
        rel = md.relative_to(WIKI).as_posix()
        rel_key = rel[:-3] if rel.endswith(".md") else rel
        pages.append((md, rel_key, slug_for(rel_key)))
    return pages


def build_alias_map(pages: list[tuple[Path, str, str]]) -> dict[str, str]:
    aliases: dict[str, str] = {}
    for _path, rel_key, slug in pages:
        html = f"{slug}.html"
        stem = Path(rel_key).name
        aliases[stem] = html
        aliases[rel_key] = html
        aliases[rel_key.replace("/", "-")] = html
        # Thai entity names
        if "หลักสูตร" in stem:
            aliases["หลักสูตรวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์-บัณฑิตศึกษา"] = html
        if "มหาวิทยาลัย" in stem:
            aliases["มหาวิทยาลัยราชภัฏอุตรดิตถ์"] = html
    for name, slug in [
        ("AUN-QA", "aun-qa.html"),
        ("CLO", "clo.html"),
        ("PLO", "concepts-plo.html"),
        ("PLO-CLO Summary", "concepts-plo-clo-summary.html"),
        ("มคอ.2", "concepts-มคอ-2.html"),
        ("Bloom's Taxonomy", "concepts-plo.html"),
    ]:
        if name not in aliases:
            aliases[name] = slug
    # summaries paths
    for prefix in ("summaries/", "guidelines/", "raw/"):
        for _p, rel_key, slug in pages:
            if rel_key.startswith(prefix.rstrip("/") + "/") or rel_key.startswith(prefix):
                short = rel_key.split("/", 1)[-1] if "/" in rel_key else rel_key
                aliases[f"{prefix}{short}"] = f"{slug}.html"
                label = rel_key.split("/")[-1]
                aliases[label] = f"{slug}.html"
    return aliases


def fix_wikilinks(text: str, aliases: dict[str, str]) -> str:
    def repl(m: re.Match) -> str:
        target = m.group(1).strip()
        label = m.group(2).strip() if m.group(2) else target
        href = aliases.get(target)
        if not href:
            # try without path prefix
            href = aliases.get(target.split("/")[-1])
        if href:
            return f"[{label}]({href})"
        return f"**{label}**"

    text = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", repl, text)
    return text


def md_to_html(body: str) -> str:
    import markdown as md

    return md.markdown(
        body,
        extensions=["tables", "fenced_code", "nl2br", "sane_lists"],
        output_format="html5",
    )


def strip_html(html: str) -> str:
    return re.sub(r"<[^>]+>", " ", re.sub(r"\s+", " ", html)).strip()


def render_page(
    title: str,
    content_html: str,
    slug: str,
    meta: dict,
    nav_html: str,
) -> str:
    subtitle = meta.get("type", "")
    return f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — CE&AI AUN-QA</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&family=IBM+Plex+Sans+Thai:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{asset_href(slug)}assets/site.css">
</head>
<body>
  <header class="site-header">
    <div class="brand">
      <a href="{asset_href(slug)}index.html" class="brand-link">
        <span class="brand-uni">ม.ร.อ.</span>
        <span class="brand-title">วศ.ม. วิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์</span>
        <span class="brand-sub">AUN-QA SAR Reference · 2568</span>
      </a>
    </div>
    <button class="nav-toggle" type="button" aria-label="เปิดเมนู" data-nav-toggle>☰</button>
  </header>
  <div class="layout">
    <nav class="sidebar" data-sidebar>
      {nav_html}
    </nav>
    <main class="content">
      <article class="prose">
        <header class="page-header">
          <h1>{title}</h1>
          {f'<p class="page-meta">{subtitle}</p>' if subtitle else ''}
        </header>
        {content_html}
      </article>
    </main>
  </div>
  <script src="{asset_href(slug)}assets/search.js" defer></script>
</body>
</html>"""


def asset_href(slug: str) -> str:
    depth = slug.count("/") + (0 if slug else 0)
    return "../" * depth if depth else "./"


def render_nav(current_slug: str) -> str:
    parts = ['<div class="nav-search"><input type="search" placeholder="ค้นหา..." data-search-input aria-label="ค้นหา"></div>']
    prefix = asset_href(current_slug)
    for section in NAV:
        parts.append(f'<p class="nav-section">{section["label"]}</p><ul>')
        for slug, label in section["items"]:
            href = f"{prefix}{slug}.html"
            active = " active" if slug == current_slug else ""
            parts.append(f'<li><a href="{href}" class="nav-link{active}">{label}</a></li>')
        parts.append("</ul>")
    parts.append(
        f'<p class="nav-section">เอกสาร</p><ul>'
        f'<li><a href="https://github.com/beebrain/aunqa68-ceai-sar" class="nav-link" target="_blank" rel="noopener">GitHub Repo</a></li>'
        f"</ul>"
    )
    return "\n".join(parts)


def render_home(nav_html: str) -> str:
    cards = [
        ("program.html", "หลักสูตร", "PEO/PLO, โครงสร้างหน่วยกิต, อาจารย์, รายวิชา"),
        ("criteria/1.html", "เกณฑ์ 1–8", "สรุป SAR ตาม AUN-QA v4 พร้อมหลักฐานอ้างอิง"),
        ("guidelines/overview.html", "แนวทางอ.ที่ปรึกษา", "เนื้อเกณฑ์ที่พึงพิจารณา + Rating Scale"),
        ("clo.html", "CLO รายวิชา", "33 รายวิชา — คำอธิบายและ CLO ทุกข้อ"),
        ("evidence.html", "ดัชนีหลักฐาน", "รหัส AUNQA-X-Y และ AUNQA-C-S-N"),
        ("teaching.html", "การจัดการเรียนการสอน", "Learning Environment 32 วิชา"),
    ]
    card_html = "".join(
        f'<a class="card" href="{href}"><h3>{title}</h3><p>{desc}</p></a>'
        for href, title, desc in cards
    )
    criteria_rows = "".join(
        f'<tr><td><a href="criteria/{i}.html">C{i}</a></td>'
        f"<td>{CRITERION_LABELS[i]}</td>"
        f'<td><a href="guidelines/{i}.html">แนวทาง</a></td></tr>'
        for i in range(1, 9)
    )
    return f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CE&AI AUN-QA Reference — ม.ร.อ. 2568</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&family=IBM+Plex+Sans+Thai:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/site.css">
</head>
<body class="home">
  <header class="site-header">
    <div class="brand">
      <span class="brand-uni">มหาวิทยาลัยราชภัฏอุตรดิตถ์</span>
      <h1 class="hero-title">วศ.ม. วิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์</h1>
      <p class="hero-sub">คลังข้อมูลอ้างอิงสำหรับจัดทำ SAR AUN-QA Version 4.0 · ปีการศึกษา 2568</p>
    </div>
    <button class="nav-toggle" type="button" aria-label="เปิดเมนู" data-nav-toggle>☰</button>
  </header>
  <div class="layout">
    <nav class="sidebar" data-sidebar>
      {nav_html}
    </nav>
    <main class="content home-content">
      <section class="hero-cards">
        {card_html}
      </section>
      <section class="prose">
        <h2>เกณฑ์ AUN-QA ทั้ง 8 ข้อ</h2>
        <table>
          <thead><tr><th>เกณฑ์</th><th>ชื่อ</th><th>แนวทาง</th></tr></thead>
          <tbody>{criteria_rows}</tbody>
        </table>
        <p class="build-note">สร้างจาก <code>aun-qa-wiki/</code> เมื่อ {date.today().isoformat()} — รัน <code>python3 website/build.py</code> เพื่ออัปเดต</p>
      </section>
    </main>
  </div>
  <script src="assets/search.js" defer></script>
</body>
</html>"""


def main() -> None:
    ensure_markdown()
    pages = discover_pages()
    aliases = build_alias_map(pages)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / "assets").mkdir()
    shutil.copytree(STATIC, OUT / "assets", dirs_exist_ok=True)
    (OUT / ".nojekyll").touch()

    nav_home = render_nav("")
    (OUT / "index.html").write_text(render_home(nav_home), encoding="utf-8")

    search_entries: list[dict] = [
        {
            "title": "หน้าแรก",
            "url": "index.html",
            "text": "วศ.ม. วิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ AUN-QA SAR",
        }
    ]

    for md_path, rel_key, slug in pages:
        raw = md_path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        body = fix_wikilinks(body, aliases)
        content_html = md_to_html(body)

        title = meta.get("title") or body.lstrip().split("\n", 1)[0].lstrip("# ").strip()
        out_path = OUT / f"{slug}.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        nav = render_nav(slug)
        out_path.write_text(render_page(title, content_html, slug, meta, nav), encoding="utf-8")

        url = f"{slug}.html"
        search_entries.append(
            {
                "title": title,
                "url": url,
                "text": strip_html(content_html)[:2000],
            }
        )
        print(f"  {rel_key} -> {url}")

    (OUT / "search-index.json").write_text(
        json.dumps(search_entries, ensure_ascii=False, indent=0),
        encoding="utf-8",
    )
    print(f"\nBuilt {len(pages) + 1} pages -> {OUT}")


if __name__ == "__main__":
    main()
