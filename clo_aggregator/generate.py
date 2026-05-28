#!/usr/bin/env python3
"""CLO Aggregation System — CPE&AI มรอ.
Usage: python3 generate.py [scores_2568.csv]
"""
import csv, os, subprocess, sys
from collections import defaultdict

FONTS_PATH = "/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68/fonts/"

CLO_PLO_MAP = {
    ("4095101","CLO1"):[1], ("4095101","CLO2"):[1], ("4095101","CLO3"):[3],
    ("4095101","CLO4"):[3], ("4095101","CLO5"):[1],
    ("7015906","CLO1"):[2], ("7015906","CLO2"):[3], ("7015906","CLO3"):[3],
    ("7015906","CLO4"):[4], ("7015906","CLO5"):[5],
#    ("7015907","CLO1"):[2,3], ("7015907","CLO2"):[2,5], ("7015907","CLO3"):[2,5],
#    ("7015907","CLO4"):[4],   ("7015907","CLO5"):[2,5],
    ("4095102","CLO1"):[1],   ("4095102","CLO2"):[1,2], ("4095102","CLO3"):[2,3],
    ("4095102","CLO4"):[4],   ("4095102","CLO5"):[1,3],
    ("7015101","CLO1"):[1],   ("7015101","CLO2"):[1],   ("7015101","CLO3"):[2],
    ("7015101","CLO4"):[1],   ("7015101","CLO5"):[1],
}

COURSE_NAMES = {
    "4095101": "ปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง",
    "7015906": "ระเบียบวิธีวิจัยทางวิทยาศาสตร์และวิศวกรรมศาสตร์",
    "7015907": "สัมมนา CPE&AI",
    "4095102": "การเขียนโปรแกรมขั้นสูงสำหรับการเรียนรู้ของเครื่อง",
    "7015101": "เทคโนโลยีอุบัติใหม่ทางวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์",
}

PLO_DESC = {
    1: "สร้างสรรค์ผลงาน/นวัตกรรมด้วยซอฟต์แวร์/ฮาร์ดแวร์",
    2: "ประยุกต์ใช้ความรู้แก้ปัญหาองค์กร/ชุมชน",
    3: "สร้างองค์ความรู้/ต้นแบบนวัตกรรมด้าน AI",
    4: "จรรยาบรรณวิชาชีพ",
    5: "คิดวิเคราะห์/สื่อสาร/ทำงานร่วมกัน/เรียนรู้ตลอดชีวิต",
}

PASS_THRESHOLD   = 0.60
PLO_PASS_RATE    = 0.70
PLO_CLO_COVERAGE = 0.70

def read_scores(path):
    records = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            records.append({
                "sid":   row["student_id"], "sname": row["student_name"],
                "course":row["course_code"],"sem":   row["semester"],
                "clo":   row["clo"],
                "score": float(row["score"]), "max": float(row["max_score"]),
            })
    return records

def aggregate(records):
    score_map = defaultdict(lambda: defaultdict(dict))
    students  = {}
    for r in records:
        score_map[r["sid"]][r["course"]][r["clo"]] = r["score"] / r["max"]
        students[r["sid"]] = r["sname"]
    plo_map = defaultdict(list)
    for (course, clo), plos in CLO_PLO_MAP.items():
        for p in plos:
            plo_map[p].append((course, clo))
    stu_plo = {}
    for sid in students:
        stu_plo[sid] = {}
        for plo in range(1, 6):
            mapped = plo_map[plo]
            passed = sum(1 for (c,cl) in mapped
                         if score_map[sid].get(c,{}).get(cl,0) >= PASS_THRESHOLD)
            stu_plo[sid][plo] = passed / len(mapped) if mapped else 0
    plo_rate = {}
    for plo in range(1, 6):
        n_pass = sum(1 for sid in students if stu_plo[sid][plo] >= PLO_CLO_COVERAGE)
        plo_rate[plo] = n_pass / len(students) if students else 0
    return students, score_map, stu_plo, plo_rate, plo_map

def e(s):
    return s.replace("&","\\&").replace("%","\\%").replace("_","\\_")

def short(name):
    parts = name.split()
    return parts[0][:5] if parts else name[:5]

def build_latex(records, year_label, out_tex):
    students, score_map, stu_plo, plo_rate, plo_map = aggregate(records)
    sid_list = sorted(students.keys())
    fp = FONTS_PATH.rstrip("/") + "/"

    L = []
    def a(x): L.append(x)

    a(r"\documentclass[12pt,a4paper]{article}")
    a(r"\usepackage{fontspec}")
    a(r"\usepackage{polyglossia}")
    a(r"\setdefaultlanguage{thai}")
    a(r"\setotherlanguage{english}")
    a(f"\\setmainfont{{THSarabunNew}}[Path={fp},Extension=.ttf,UprightFont=*,BoldFont=* Bold,ItalicFont=* Italic,BoldItalicFont=* BoldItalic]")
    a(f"\\newfontfamily\\thaifont{{THSarabunNew}}[Path={fp},Extension=.ttf,UprightFont=*,BoldFont=* Bold,ItalicFont=* Italic,BoldItalicFont=* BoldItalic]")
    a(r"\XeTeXlinebreaklocale ""th""")
    a(r"\XeTeXlinebreakskip = 0pt plus 1pt")
    a(r"\usepackage{geometry}\geometry{margin=2cm,top=2cm,bottom=2.5cm}")
    a(r"\usepackage{booktabs,longtable,array,xcolor,multirow,hyperref,colortbl}")
    a(r"\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}")
    a(r"\definecolor{hdr}{RGB}{30,80,140}")
    a(r"\definecolor{pass}{RGB}{200,240,200}")
    a(r"\definecolor{fail}{RGB}{255,215,215}")
    a(r"\definecolor{hi}{RGB}{240,248,255}")
    a(r"\begin{document}")
    a(r"\begin{center}")
    a(r"{\Large\bfseries รายงานผลการประเมิน CLO--PLO Achievement}\\[4pt]")
    a(r"{\large หลักสูตร วศ.ม. วิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์}\\[2pt]")
    a(f"{{\\large มหาวิทยาลัยราชภัฏอุตรดิตถ์ \\quad ปีการศึกษา {year_label}}}\\\\[2pt]")
    a(r"{\normalsize รหัสหลักฐาน: AUNQA-8-4-1}")
    a(r"\end{center}")
    a(r"\vspace{0.2cm}")
    a(r"\noindent\textbf{คำชี้แจงและแหล่งข้อมูลหลักฐาน:} ข้อมูลคะแนนและผลสัมฤทธิ์การประเมินผลลัพธ์การเรียนรู้รายวิชา (CLO) ของนักศึกษารายบุคคลในรายงานฉบับนี้ รวบรวมมาจากรายงานผลการดำเนินการของรายวิชา (มคอ. 5) ทั้งหมด 4 วิชาบังคับของหลักสูตร วศ.ม. วิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ ปีการศึกษา 2568 (ภาคเรียนที่ 1--2) โดยใช้ระดับคะแนนประเมินอิงเกณฑ์ตามเกณฑ์รูบริก (Rubrics Score 4 ระดับ: 1 = ควรปรับปรุง, 2 = พอใช้, 3 = ดี, 4 = ดีเยี่ยม) ที่มีกำหนดไว้ในแผนการสอน (มคอ. 3) ของแต่ละรายวิชา")
    a(r"\vspace{0.3cm}")

    # Section 1: CLO-PLO map
    a(r"\section*{1. ความสัมพันธ์ CLO--PLO (ภาพรวมรายวิชา ปีการศึกษา 2568)}")
    a(r"\begin{longtable}{|l|p{6.5cm}|c|c|}")
    a(r"\hline")
    a(r"\rowcolor{hdr}\color{white}\textbf{รหัสวิชา} & \color{white}\textbf{ชื่อวิชา} & \color{white}\textbf{CLO} & \color{white}\textbf{PLO} \\ \hline")
    a(r"\endfirsthead \multicolumn{4}{c}{\tablename\ (ต่อ)} \\ \hline")
    a(r"\rowcolor{hdr}\color{white}\textbf{รหัสวิชา} & \color{white}\textbf{ชื่อวิชา} & \color{white}\textbf{CLO} & \color{white}\textbf{PLO} \\ \hline \endhead")
    for code in ["4095101","7015906","4095102","7015101"]:
        clos = sorted([(cl, ps) for (c,cl),ps in CLO_PLO_MAP.items() if c==code])
        cname = COURSE_NAMES.get(code, code)
        for i,(clo,plos) in enumerate(clos):
            pstr = ", ".join(f"PLO{p}" for p in sorted(plos))
            nm = e(cname) if i==0 else ""
            cd = code if i==0 else ""
            a(f"  {cd} & {nm} & {clo} & {pstr} \\\\")
        a(r"  \hline")
    a(r"\end{longtable}")

    # Section 2: per-student PLO
    a(r"\section*{2. ผลการประเมิน PLO รายนักศึกษา}")
    a(r"\textbf{เกณฑ์:} คะแนน CLO $\geq 60\%$ = ผ่าน และผ่าน $\geq 70\%$ ของ CLO ที่เชื่อมโยง = บรรลุ PLO\\[4pt]")
    cols = "|c|p{6.2cm}|" + "c|"*len(sid_list)
    a(f"\\begin{{longtable}}{{{cols}}}")
    a(r"\hline")
    hdr_names = " & ".join(f"\\color{{white}}\\textbf{{{short(students[s])}}}" for s in sid_list)
    a(r"\rowcolor{hdr}\color{white}\textbf{PLO} & \color{white}\textbf{คำอธิบาย} & " + hdr_names + r" \\ \hline")
    a(r"\endfirsthead \multicolumn{" + str(2+len(sid_list)) + r"}{c}{\tablename\ (ต่อ)} \\ \hline \endhead")
    for plo in range(1,6):
        cells = []
        for sid in sid_list:
            pct = stu_plo[sid][plo]
            col = "pass" if pct>=PLO_CLO_COVERAGE else "fail"
            cells.append(f"\\cellcolor{{{col}}}{pct*100:.0f}\\%")
        a(f"  PLO{plo} & {e(PLO_DESC[plo])} & " + " & ".join(cells) + r" \\ \hline")
    a(r"\end{longtable}")

    # Section 3: program-level
    a(r"\section*{3. อัตราการบรรลุ PLO ระดับหลักสูตร (Program-Level Achievement)}")
    a(r"\textbf{เกณฑ์หลักสูตร:} นักศึกษา $\geq 70\%$ ต้องสำเร็จ PLO นั้น\\[4pt]")
    a(r"\begin{longtable}{|c|p{7cm}|c|c|c|}")
    a(r"\hline")
    a(r"\rowcolor{hdr}\color{white}\textbf{PLO} & \color{white}\textbf{คำอธิบาย} & \color{white}\textbf{จำนวน CLO} & \color{white}\textbf{อัตราสำเร็จ} & \color{white}\textbf{ผล} \\ \hline")
    a(r"\endfirsthead \multicolumn{5}{c}{\tablename\ (ต่อ)} \\ \hline \endhead")
    for plo in range(1,6):
        n_clo  = len(plo_map[plo])
        rate   = plo_rate[plo]
        ok     = rate >= PLO_PASS_RATE
        col    = "pass" if ok else "fail"
        status = r"\textbf{ผ่าน}" if ok else r"\textbf{ไม่ผ่าน}"
        n_num  = int(rate * len(sid_list))
        a(f"  \\cellcolor{{{col}}}PLO{plo} & {e(PLO_DESC[plo])} & {n_clo} & "
          f"{rate*100:.0f}\\% ({n_num}/{len(sid_list)}) & \\cellcolor{{{col}}}{status} \\\\ \\hline")
    a(r"\end{longtable}")

    # Section 4: score detail per course
    a(r"\section*{4. คะแนน CLO รายวิชา — ปีการศึกษา 2568}")
    for code in ["4095101","7015906","4095102","7015101"]:
        cname  = COURSE_NAMES.get(code, code)
        sem_lb = "1/2568" if code in ["4095101","7015906"] else "2/2568"
        a(f"\\subsection*{{{code} {e(cname)} (ภาค {sem_lb})}}")
        clos = sorted({cl for (c,cl) in CLO_PLO_MAP if c==code})
        a(r"\begin{longtable}{|p{4.5cm}|" + "c|"*len(clos) + "}")
        a(r"\hline")
        hdr_c = " & ".join(f"\\color{{white}}\\textbf{{{cl}}}" for cl in clos)
        a(r"\rowcolor{hdr}\color{white}\textbf{นักศึกษา} & " + hdr_c + r" \\ \hline")
        a(r"\endfirsthead \hline \endhead")
        for sid in sid_list:
            cells2 = []
            for cl in clos:
                pct = score_map[sid].get(code,{}).get(cl,None)
                if pct is None:
                    cells2.append("—")
                else:
                    col2 = "pass" if pct>=PASS_THRESHOLD else "fail"
                    cells2.append(f"\\cellcolor{{{col2}}}{pct*100:.0f}\\%")
            a(f"  {e(students[sid])} & " + " & ".join(cells2) + r" \\ \hline")
        a(r"\end{longtable}")

    # Footer
    n_all = sum(1 for sid in sid_list if all(stu_plo[sid][p]>=PLO_CLO_COVERAGE for p in range(1,6)))
    a(r"\vspace{0.3cm}\noindent\rule{\linewidth}{0.4pt}")
    a(f"\\noindent\\textbf{{สรุป:}} นักศึกษาที่บรรลุ PLO ครบ 5 รายการ: \\textbf{{{n_all}/{len(sid_list)} คน}} ({n_all/len(sid_list)*100:.0f}\\%)\\\\")
    a(r"\noindent\textit{ข้อมูล ณ สิ้นปีการศึกษา 2568 (ภาค 1--2) — CLO Aggregation System v1.0 | อัปเดตทุกสิ้นปีการศึกษา}")
    a(r"\end{document}")

    with open(out_tex, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"Written: {out_tex}")

if __name__ == "__main__":
    csv_path   = sys.argv[1] if len(sys.argv) > 1 else "scores_2568.csv"
    year       = "2568"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_abs    = os.path.join(script_dir, csv_path)
    out_dir    = os.path.join(script_dir, "output")
    out_tex    = os.path.join(out_dir, f"clo_report_{year}.tex")
    os.makedirs(out_dir, exist_ok=True)

    records = read_scores(csv_abs)
    build_latex(records, year, out_tex)

    print("Compiling (xelatex pass 1)...")
    for _ in range(2):
        r = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", f"clo_report_{year}.tex"],
            cwd=out_dir, capture_output=True, text=True
        )
    if r.returncode == 0 or os.path.exists(os.path.join(out_dir, f"clo_report_{year}.pdf")):
        pdf = os.path.join(out_dir, f"clo_report_{year}.pdf")
        size = os.path.getsize(pdf)
        print(f"PDF ready: {pdf}  ({size//1024} KB)")
    else:
        print("ERROR:")
        print("\n".join(r.stdout.splitlines()[-15:]))
        sys.exit(1)
