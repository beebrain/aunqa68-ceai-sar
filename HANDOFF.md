# HANDOFF LOG
Generated : 2026-05-12 (session 2)
AI_Model  : claude-sonnet-4-6
Project   : AunQA68 — SAR หลักสูตรวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ มรอ.

---

## CONTEXT
โปรเจกต์จัดทำ SAR (Self-Assessment Report) AUN-QA หลักสูตร วศ.ม. วิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ มหาวิทยาลัยราชภัฏอุตรดิตถ์ พ.ศ. 2568 มี vault `aun-qa-wiki` เป็น knowledge base และ `SAR-CEAI-2568.tex` เป็น output หลัก Session นี้ ingest ข้อมูลสายสนับสนุน (Criteria 4–7) ครบแล้ว และสกัด teaching activities + evidence index จาก DOCX ทั้งหมด

---

## DONE ✓
- `aun-qa-wiki/summaries/teaching-activities.md` — สร้างใหม่: ตาราง Teaching Activities ครบ 32 วิชา (4 คอลัมน์: สภาพแวดล้อม, กิจกรรมอาจารย์, กิจกรรมนักศึกษา, วิธีประเมิน) ← ใช้สำหรับ Criterion 3
- `aun-qa-wiki/summaries/evidence-index.md` — สร้างใหม่: ดัชนีหลักฐาน 92 รายการ (C4:3, C5:35, C6:19, C7:35) พร้อม URL 38 ลิงก์ จัดตาม Criteria/Sub-criterion
- `aun-qa-wiki/summaries/support-data-summary.md` — สร้างใหม่: สรุป Criteria 4–7 พร้อมตัวเลข (เจ้าหน้าที่ 143 คน, WiFi 795 จุด, คอมพิวเตอร์ 277 เครื่อง)
- `aun-qa-wiki/raw/support-data-extract.md` — raw extraction จาก ข้อมูลพื้นฐาน AUN-QA-สายสนับสนุน30042569(1).docx (609 paragraphs, 4 tables)
- `aun-qa-wiki/concepts/yleo.md` — เขียนใหม่: YLO1/YLO2/YLO2b พร้อมตารางรายวิชาและ PLO coverage matrix
- `aun-qa-wiki/index.md` — อัปเดต: total pages 12 (เพิ่ม 4 entries ใหม่)
- `aun-qa-wiki/log.md` — append entries ทั้งหมด session นี้
- `scripts/extract_evidence_index.py` — parse AUNQA-C-S-N codes + URLs จาก raw extract
- `scripts/extract_clo_teaching_activities.py` — pair teaching activity tables กับ course list
- `scripts/extract_support_raw.py` — raw extraction จาก support DOCX

---

## PROBLEMS → SOLUTIONS
- Teaching activities body-walk: การ walk XML body elements เพื่อหา course header ไม่ทำงาน (ได้เพียง 1 course) → เปลี่ยนเป็น pair tables กับ course list จาก clo-all-courses-detailed.md ตาม index position [FIXED]
- Teaching activities script KeyError 'code': current_course dict ไม่มี key เมื่อสร้างจาก inline path → refactor โดย init dict ให้ถูกต้อง [FIXED]

---

## CURRENT STATE
- STATUS: Knowledge base ครบทุกด้าน — CLO/PLO/YLO mapping + support data (C4-C7) + teaching activities + evidence index พร้อมใช้; SAR-CEAI-2568.tex ยังไม่ได้ populate
- BUILD: SAR-CEAI-2568.tex ยังไม่ได้ compile ใน session นี้
- BRANCH: N/A (ไม่ใช่ git repo)
- vault: 12 pages (summaries 5 หน้า, concepts 4 หน้า, entities 2 หน้า, raw 2 หน้า)

---

## PENDING ⏳
1. Populate `SAR-CEAI-2568.tex` Criterion 3 — ใช้ `clo-ylo-mapping.md` + `teaching-activities.md` เติม CLO-PLO alignment matrix และ Teaching & Learning Approach
2. Populate `SAR-CEAI-2568.tex` Criteria 4–7 — ใช้ `support-data-summary.md` + `evidence-index.md` เติมข้อความ + ตารางตัวเลข + cite หลักฐาน AUNQA-X-Y-Z
3. ตรวจสอบ course #20 (duplicate data mining ไม่มีรหัส) ใน `clo-all-courses-detailed.md`
4. Ingest DOCX ที่ยังไม่ได้ทำ: `from_report68.docx`, `from_report68_original.docx`, `mko2-comment.docx`
5. ตรวจสอบ SAR-CEAI-2568.tex และ compile ด้วย xelatex

---

## KEY FILES
- `aun-qa-wiki/summaries/clo-ylo-mapping.md` → CLO–YLO–PLO mapping + elective matrix + cross-reference (ใช้สำหรับ Criterion 3)
- `aun-qa-wiki/summaries/teaching-activities.md` → ตาราง Teaching Activities ครบ 32 วิชา (ใช้สำหรับ Criterion 3 + 4)
- `aun-qa-wiki/summaries/evidence-index.md` → AUNQA-C-S-N ดัชนีหลักฐาน 92 รายการ + URL (ใช้ cite ใน SAR)
- `aun-qa-wiki/summaries/support-data-summary.md` → Criteria 4–7 สรุปพร้อมตัวเลข
- `aun-qa-wiki/summaries/clo-all-courses-detailed.md` → CLO รายข้อ + Bloom's + PLO ครบ 32 วิชา
- `aun-qa-wiki/index.md` → index ทุกหน้า (12 pages, อัปเดตแล้ว)
- `aun-qa-wiki/log.md` → บันทึก ingest actions ทั้งหมด
- `SAR-CEAI-2568.tex` → LaTeX SAR หลัก (ยังไม่ได้ populate)
- `scripts/extract_evidence_index.py` → parse AUNQA codes + URLs
- `scripts/extract_clo_teaching_activities.py` → extract teaching activity tables
- `scripts/generate_clo_ylo_map.py` → regenerate clo-ylo-mapping.md

---

## SKILLS & TOOLS IN USE
- python-docx — parse .docx (Thai filename: copy to ASCII name first)
- Bloom's codes — U, Ap, An, E, Cr, Va, O, In, A, P, Re, Rs
- AUN-QA Criteria 3–7 — focus หลักของ SAR
- Obsidian vault format — wikilinks [[...]], YAML frontmatter
- AUNQA-C-S-N — รหัสหลักฐาน format ที่ใช้ cite ใน SAR

---

## QUICK START
> อ่าน `SAR-CEAI-2568.tex` เพื่อดูโครงสร้างและ section ที่ต้องเติม จากนั้น populate Criterion 3 โดยนำข้อมูลจาก `aun-qa-wiki/summaries/clo-ylo-mapping.md` (CLO-PLO matrix) และ `aun-qa-wiki/summaries/teaching-activities.md` (teaching methods) มาเขียนเป็น LaTeX table + paragraph ตามเกณฑ์ AUN-QA

---

## MEMORY REFS
- `C:\Users\brand\.claude\projects\F--Uttaradit-Rajabhat-University-Computer-Engineering-Master-Startup---General-AunQA68\memory\` — project memory files
