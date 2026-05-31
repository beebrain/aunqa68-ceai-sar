#!/usr/bin/env python3
"""Apply curated teaching rows to all AUN3_*.tex files."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from teaching_curated import DATA, IEL  # noqa: E402

MKO3 = Path(__file__).resolve().parents[1]

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


def build_block(clos: dict, tex: str) -> str:
    order = re.findall(r"\\cloitem\{(CLO\d+)\}", tex)
    rows = []
    for clo in order:
        if clo not in clos:
            continue
        teach, assess = clos[clo]
        if IEL not in teach:
            teach = teach + IEL
        teach = teach.replace("&", "\\&")
        assess = assess.replace("&", "\\&")
        rows.append(f"  \\teachrow{{{clo}}}{{{teach}}}{{{assess}}}")
    return (
        "% ----- 5. Teaching & assessment -----\n"
        "\\begin{teachingtable}\n"
        + "\n".join(rows)
        + "\n\\end{teachingtable}"
    )


def main():
    for tex_file in sorted(MKO3.glob("AUN3_*.tex")):
        m = re.search(r"AUN3_(\d+)\.tex", tex_file.name)
        if not m:
            continue
        wiki = TEX_TO_WIKI.get(m.group(1))
        if not wiki or wiki not in DATA:
            print(f"SKIP {tex_file.name}: no curated data")
            continue
        content = tex_file.read_text(encoding="utf-8")
        block = build_block(DATA[wiki], content)
        pattern = (
            r"% ----- 5\. Teaching & assessment -----\n"
            r"\\begin\{teachingtable\}.*?\\end\{teachingtable\}"
        )
        if not re.search(pattern, content, re.DOTALL):
            print(f"SKIP {tex_file.name}: no teachingtable")
            continue
        new_content = re.sub(pattern, lambda _: block, content, count=1, flags=re.DOTALL)
        tex_file.write_text(new_content, encoding="utf-8")
        print(f"OK {tex_file.name}")


if __name__ == "__main__":
    main()
