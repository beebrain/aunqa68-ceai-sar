import os
import re
import urllib.parse
from pathlib import Path

# Setup paths
root = Path("/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68")
wiki = root / "aun-qa-wiki"
summaries = wiki / "summaries"

# 1. Scan directories
dirs_to_scan = {
    "หลักฐานสายสนับสนุน": root / "หลักฐานสายสนับสนุน",
    "หลักฐานการประชุม/01_ระดับหลักสูตร": root / "หลักฐานการประชุม/01_ระดับหลักสูตร",
    "หลักฐานการประชุม/02_ระดับคณะ": root / "หลักฐานการประชุม/02_ระดับคณะ",
    "หลักฐานการประชุม/03_ระดับมหาวิทยาลัย": root / "หลักฐานการประชุม/03_ระดับมหาวิทยาลัย",
    "ระเบียบข้อบังคับและประกาศอื่นๆ": root / "ระเบียบข้อบังคับและประกาศอื่นๆ"
}

all_files = []

for label, path in dirs_to_scan.items():
    if not path.exists():
        print(f"Directory does not exist: {path}")
        continue
    for f in path.iterdir():
        if f.is_file() and not f.name.startswith('.'):
            # Calculate file URL
            file_url = f"file://{urllib.parse.quote(str(f))}"
            all_files.append({
                "category": label,
                "name": f.name,
                "size_kb": round(f.stat().st_size / 1024, 2),
                "path": str(f),
                "url": file_url
            })

print(f"Total files found across all directories: {len(all_files)}")

# 2. Match files to AUN-QA codes
file_registry = []

for f in all_files:
    name = f["name"]
    code = "AUNQA-PENDING"
    desc = ""
    criterion = ""
    
    # Matching logic based on filename and codes
    
    # Meeting minutes (ระดับหลักสูตร)
    if "กมศ_" in name:
        date_match = re.search(r'กมศ_(\d{4}-\d{2}-\d{2})_(.*)\.pdf', name)
        if date_match:
            date_str = date_match.group(1)
            topic = date_match.group(2).replace('_', ' ')
            code = "AUNQA-1-2" # กมศ meeting minutes
            desc = f"รายงานการประชุม กมศ. หลักสูตร วันที่ {date_str} เรื่อง {topic}"
            criterion = "C1, C2, C5, C6, C8"
        else:
            code = "AUNQA-1-2"
            desc = f"รายงานการประชุม กมศ. หลักสูตร ({name})"
            criterion = "C1, C2, C5, C6, C8"
            
    # Meeting minutes (ระดับคณะ)
    elif "คณะ_" in name:
        code = "AUNQA-5-สมอ08-REF"
        desc = f"รายงาน/เอกสารการประชุมระดับคณะ: {name.replace('_', ' ')}"
        criterion = "C5, C2"
        
    # Meeting minutes (ระดับมหาวิทยาลัย)
    elif "มรอ_สภามหาวิทยาลัย_" in name:
        code = "AUNQA-1-4"
        desc = "รายงานการประชุมสภามหาวิทยาลัยราชภัฏอุตรดิตถ์"
        criterion = "C1, C2"
    elif "มรอ_สมอ08_" in name:
        code = "AUNQA-5-สมอ08"
        desc = "หลักฐาน สมอ.08 รับรองการเพิ่มอาจารย์ประจำหลักสูตรเป็น 10 คน"
        criterion = "C5"
        
    # Specific AUNQA prefixes in names
    elif "AUNQA-3-1-1" in name or "AUNQA-3-1" in name or "ประกาศIEL" in name:
        code = "AUNQA-3-1"
        desc = "ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง ปรัชญาการจัดการศึกษา (IEL)"
        criterion = "C3.1"
    elif "AUNQA-4-1-2" in name or "ประกาศภาระงานขั้นต่ำ" in name and "5-2-1" not in name:
        code = "AUNQA-4-1-2"
        desc = "ประกาศ มรอ. เรื่อง หลักเกณฑ์การวัดและประเมินผลการศึกษาของรายวิชา พ.ศ. 2567"
        criterion = "C4.1"
    elif "AUNQA-4-2-1" in name or "ประกาศอุทธรณ์" in name:
        code = "AUNQA-4-1"
        desc = "ประกาศ มรอ. เรื่อง ระบบและแนวทางการอุทธรณ์ เกี่ยวกับผลการประเมินผลการศึกษาของนักศึกษา พ.ศ. 2567"
        criterion = "C4.2"
    elif "AUNQA-4-3-1" in name or "ข้อบังคับบัณฑิตศึกษา_2566" in name:
        code = "AUNQA-4-2"
        desc = "ข้อบังคับมหาวิทยาลัยราชภัฏอุตรดิตถ์ ว่าด้วย การศึกษาระดับบัณฑิตศึกษา พ.ศ. 2566"
        criterion = "C4.3, C6.1, C2.3, C3.4"
    elif "AUNQA-4-3-2" in name or "ข้อบังคับบัณฑิตศึกษาฉ2" in name:
        code = "AUNQA-4-2b"
        desc = "ข้อบังคับมหาวิทยาลัยราชภัฏอุตรดิตถ์ ว่าด้วย การศึกษาระดับบัณฑิตศึกษา (ฉบับที่ 2) พ.ศ. 2566"
        criterion = "C4.3, C6.1"
    elif "AUNQA-4-7-1" in name or "แนวปฏิบัติส่งผลประเมิน" in name:
        code = "AUNQA-4-3"
        desc = "ประกาศ มรอ. เรื่อง แนวปฏิบัติและการกำกับติดตามการส่งผลการประเมินผลการศึกษาของนักศึกษา พ.ศ. 2567"
        criterion = "C4.7"
    elif "AUNQA-5-1-1" in name or "แผนบริหารทรัพยากรบุคคล" in name:
        code = "AUNQA-5-1"
        desc = "แผนบริหารทรัพยากรบุคคล มหาวิทยาลัยราชภัฏอุตรดิตถ์ ปีงบประมาณ 2565-2569"
        criterion = "C5.1"
    elif "AUNQA-5-2-1" in name or "ประกาศภาระงานขั้นต่ำ_2566" in name:
        code = "AUNQA-5-2-1"
        desc = "ประกาศ มรอ. เรื่อง ภาระงานขั้นต่ำของคณาจารย์ประจำ พ.ศ. 2566"
        criterion = "C5.2, C5.4"
    elif "AUNQA-5-3-1" in name or "เสรีภาพทางวิชาการ" in name:
        code = "AUNQA-5-2"
        desc = "ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง นโยบายเสรีภาพทางวิชาการ"
        criterion = "C5.3"
    elif "AUNQA-5-5-1" in name or "ข้อบังคับการแต่งตั้งตำแหน่งทางวิชาการ" in name:
        code = "AUNQA-5-6-5"
        desc = "ข้อบังคับ มรอ. ว่าด้วย หลักเกณฑ์และวิธีการพิจารณาแต่งตั้งบุคคลให้ดำรงตำแหน่ง ผศ., รศ., ศ. พ.ศ. 2565"
        criterion = "C5.5"
    elif "AUNQA-5-6-2" in name or "ระเบียบการจัดสวัสดิการภายในมหาวิทยาลัย" in name:
        code = "AUNQA-5-6-2"
        desc = "ระเบียบมหาวิทยาลัยราชภัฏอุตรดิตถ์ ว่าด้วย การจัดสวัสดิการภายในมหาวิทยาลัย พ.ศ. 2565"
        criterion = "C5.6"
    elif "AUNQA-5-6-4" in name or "ประกาศหลักเกณฑ์การสรรหาและบรรจุพนักงานมหาวิทยาลัย" in name:
        code = "AUNQA-5-6-4"
        desc = "ประกาศ มรอ. เรื่อง หลักเกณฑ์และวิธีการสรรหาและบรรจุบุคคลเข้าเป็นพนักงานมหาวิทยาลัย พ.ศ. 2562"
        criterion = "C5.5, C5.6, C6.5"
    elif "AUNQA-5-7-1" in name or "แผนพัฒนาบุคลากร" in name:
        code = "AUNQA-5-4"
        desc = "แผนพัฒนาบุคลากร มหาวิทยาลัยราชภัฏอุตรดิตถ์ ปีงบประมาณ 2565-2569"
        criterion = "C5.7"
    elif "AUNQA-6-1-1" in name or "นโยบายรับนักศึกษา" in name:
        code = "AUNQA-6-2a"
        desc = "ประกาศ มรอ. เรื่อง นโยบายและแนวทางการรับนักศึกษาเข้าศึกษาในหลักสูตร พ.ศ. 2567"
        criterion = "C6.1"
    elif "AUNQA-6-1-5" in name or "ประกาศมาตรฐานความสามารถภาษาอังกฤษนักศึกษา" in name:
        code = "AUNQA-6-2b"
        desc = "ประกาศ มรอ. เรื่อง มาตรฐานความสามารถทางภาษาอังกฤษสำหรับนักศึกษา พ.ศ. 2569"
        criterion = "C6.2, C6.3"
    elif "AUNQA-6-2-2" in name or "แผนIT" in name:
        code = "AUNQA-7-3"
        desc = "แผนการจัดหา IT แผนปฏิบัติราชการและงบประมาณรายจ่ายประจำปีงบประมาณ พ.ศ. 2568 (ARIT)"
        criterion = "C6.3, C7.3, C7.4, C7.5"
    elif "AUNQA-8-4-1" in name or "CLO_PLO_Achievement" in name:
        code = "AUNQA-8-4-1"
        desc = "ตารางรายงานผลการสัมฤทธิ์ CLO/PLO รายวิชาบังคับ ประจำปีการศึกษา 2568"
        criterion = "C8.4"
    elif "AUNQA-1-4b" in name or "stakeholder_survey" in name:
        code = "AUNQA-1-4b"
        desc = "แบบสอบถามผู้มีส่วนได้ส่วนเสีย: ผลสำรวจดิบ n=31 ราย (มิถุนายน 2567)"
        criterion = "C1.4"
    elif "AUNQA-1-4c" in name or "บทสัมภาษณ์ผู้มีส่วนได้ส่วนเสียภายนอก" in name:
        code = "AUNQA-1-4c"
        desc = "รายงานผลการสัมภาษณ์ผู้มีส่วนได้ส่วนเสียภายนอกหลักสูตร 9 หน่วยงาน (พฤศจิกายน 2566)"
        criterion = "C1.4"
    elif "AUNQA-1-5" in name or "ปฐมนิเทศนักศึกษาบัณฑิตศึกษา" in name:
        code = "AUNQA-1-5"
        desc = "คู่มือและภาพบรรยากาศการปฐมนิเทศนักศึกษาบัณฑิตศึกษา มรอ. ปีการศึกษา 2568"
        criterion = "C1.5, C6.2"
    elif "รายละเอียดผลลัพธ์การเรียนรู้ 65" in name or "gmo-learning-outcomes" in name:
        code = "AUNQA-C1-GMO"
        desc = "รายละเอียดผลลัพธ์การเรียนรู้ตามกรอบมาตรฐานแห่งชาติ พ.ศ. 2565 (กมอ.)"
        criterion = "C1.1"
    elif "เกณฑ์มาตรฐานหลักสูตรระดับบัณฑิตศึกษา" in name or "gmo-grad-program-standards" in name:
        code = "AUNQA-C2-GMO"
        desc = "เกณฑ์มาตรฐานหลักสูตรระดับบัณฑิตศึกษา พ.ศ. 2565 (กระทรวง อว.)"
        criterion = "C2.1, C2.3"
    elif "ประกาศ กมอ. เรื่อง หลักเกณฑ์การตีพิมพ์เผยแพร่" in name or "gmo-thesis-publication" in name:
        code = "AUNQA-C8-GMO"
        desc = "ประกาศ กมอ. เรื่อง หลักเกณฑ์การตีพิมพ์เผยแพร่ผลงานวิทยานิพนธ์ พ.ศ. 2565"
        criterion = "C8.1, C8.2"
    elif "FTES" in name:
        code = "AUNQA-C5-FTES"
        desc = "ตารางฐานข้อมูลและสรุปภาระงานอาจารย์และค่า FTES ประจำปีการศึกษา 2567"
        criterion = "C5.2"
    
    file_registry.append({
        "code": code,
        "name": name,
        "desc": desc if desc else name,
        "category": f["category"],
        "size_kb": f["size_kb"],
        "url": f["url"],
        "criterion": criterion if criterion else "General"
    })

# 3. Read existing evidence-index.md or create new one
# We will write a brand new, highly robust evidence-index.md that integrates these physical files beautifully!

index_content = f"""---
title: Evidence Index — AUNQA (SAR + ดัชนีย่อยสายสนับสนุนและประชุม)
created: 2026-05-12
updated: 2026-05-26
type: summary
tags: [aun-qa, evidence, sar, aunqa-x-y, supporting-files, meeting-minutes, regulations]
sources: [raw/support-data-extract.md, summaries/meeting-minutes-ceai.md]
confidence: high
contested: false
---

# Evidence Index — หลักฐาน AUN-QA (ระบบประสานข้อมูลหลักฐานจริง)

> **อัปเดตล่าสุด: 26 พฤษภาคม 2569**
> เอกสารฉบับนี้เป็นพอร์ทัลกลางในการประสานเชื่อมโยง **รหัสหลักฐานอ้างอิงในเล่ม SAR (AUNQA-X-Y)** เข้ากับ **ไฟล์หลักฐานจริงในเครื่อง Local** 
> หลักฐานทั้งหมดถูกแบ่งออกเป็น 3 โฟลเดอร์หลักและจัดหมวดหมู่ตามเกณฑ์ AUN-QA ไว้อย่างเป็นระบบ

---

## 🏛️ สถิติการจัดระบบไฟล์หลักฐานจริงในเครื่อง (Local Evidence Stats)

*   **โฟลเดอร์หลักฐานสายสนับสนุน:** {len(list(filter(lambda x: 'หลักฐานสายสนับสนุน' in x['category'], file_registry)))} ไฟล์
*   **โฟลเดอร์หลักฐานการประชุม:** {len(list(filter(lambda x: 'หลักฐานการประชุม' in x['category'], file_registry)))} ไฟล์ (แบ่งตามระดับหลักสูตร, ระดับคณะ และมหาวิทยาลัย)
*   **โฟลเดอร์ระเบียบข้อบังคับและประกาศอื่นๆ:** {len(list(filter(lambda x: 'ระเบียบข้อบังคับและประกาศอื่นๆ' in x['category'], file_registry)))} ไฟล์
*   **รวมหลักฐานจริงสะสมในระบบ:** {len(file_registry)} ไฟล์ (เชื่อมโยงเปิดไฟล์ได้ทางตรงจากรายงาน)

---

## 📌 ตารางจับคู่รหัสหลักฐานในเล่ม SAR (SAR Master Evidence Table)

ตารางนี้ใช้เป็นดัชนีหลักท้ายรายงาน SAR เพื่อชี้เป้าหมายไฟล์จริงสำหรับผู้ตรวจประเมิน:

| รหัส SAR | รายการหลักฐานในเล่ม SAR | ไฟล์หลักฐานจริงในเครื่อง (คลิกเพื่อเปิดไฟล์ตรง) | ขนาด | เกณฑ์ที่เกี่ยวข้อง |
| :---: | :--- | :--- | :---: | :---: |
"""

# Group matching files by SAR codes
grouped_by_code = {}
for r in file_registry:
    if r["code"] != "AUNQA-PENDING":
        if r["code"] not in grouped_by_code:
            grouped_by_code[r["code"]] = []
        grouped_by_code[r["code"]].append(r)

# Write Master Registry sorted by code name alphabetically (safer than sorting混合)
sorted_codes = sorted(grouped_by_code.keys())

for code in sorted_codes:
    items = grouped_by_code[code]
    for i, item in enumerate(items):
        code_cell = f"`{code}`" if i == 0 else ""
        desc_cell = item["desc"] if i == 0 else ""
        link_cell = f"[{item['name']}]({item['url']})"
        index_content += f"| {code_cell} | {desc_cell} | {link_cell} | {item['size_kb']} KB | {item['criterion']} |\n"

index_content += """
---

## 📂 รายการหลักฐานแยกตามรายโฟลเดอร์ (Physical File Registry)

ด้านล่างนี้คือรายการของไฟล์หลักฐานจริงที่มีการจัดเก็บในเครื่องระดับ Local แยกตามโฟลเดอร์เพื่อให้สามารถค้นหาและจัดระเบียบไฟล์ได้ง่าย:

"""

# Write by Category
categories = sorted(list(set(r["category"] for r in file_registry)))
for cat in categories:
    cat_items = list(filter(lambda x: x["category"] == cat, file_registry))
    index_content += f"### 📁 โฟลเดอร์: {cat} (รวม {len(cat_items)} ไฟล์)\n\n"
    index_content += "| ชื่อไฟล์จริงในเครื่อง | รหัสหลักฐาน AUN-QA | คำอธิบายหลักฐาน | ขนาดไฟล์ |\n"
    index_content += "| :--- | :---: | :--- | :---: |\n"
    for item in sorted(cat_items, key=lambda x: x["name"]):
        index_content += f"| [{item['name']}]({item['url']}) | `{item['code']}` | {item['desc']} | {item['size_kb']} KB |\n"
    index_content += "\n"

# Write out the file
out_path = summaries / "evidence-index.md"
out_path.write_text(index_content, encoding="utf-8")
print(f"Wrote updated index to: {out_path}")

# 4. Append to wiki index
print("Index updated in wiki summaries successfully.")

