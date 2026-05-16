# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

## [2026-05-07] create | AUN-QA Wiki initialized
- Domain: AUN-QA for Computer Engineering programs at Thai Rajabhat Universities
- Structure created with SCHEMA.md, index.md, log.md
- Source files in: /mnt/e/onedrive/OneDrive - Uttaradit Rajabhat University/Computer Engineering Master Startup - AunQA68/

## [2026-05-07] ingest | Initial sources
- Created entities: มหาวิทยาลัยราชชัยอุดรธานี, หลักสูตรวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์
- Created concepts: AUN-QA, CLO, PLO, มคอ.2
- Added to index.md: 6 pages total

## [2026-05-07] ingest | มคอ.2 หลักสูตรบัณฑิตศึกษา
- Extracted data from: มคอ 2 หลักสูตรวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ ผ่านสภา 2.docx (64 MB)
- Created entity: หลักสูตรวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์-บัณฑิตศึกษา
- Includes: PEOs (4), PLOs (5), รายวิชา, กลยุทธ์การสอน
- Updated index.md: 7 pages total

## [2026-05-07] ingest | CLO รายวิชา
- Extracted from: รวมเล่ม CLO รายวิชา.docx
- Created concept: plo-clo-summary.md (รายวิชา, PLOs, PEO-PLO mapping)
- Updated entity: หลักสูตรวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์-บัณฑิตศึกษา.md
  - แก้ไข PLOs แยกตามแผน 1 และแผน 2 (PLO3 ต่างกัน)
  - เพิ่ม PEOs แยกตามแผน
  - เพิ่มตาราง PEO-PLO mapping ทั้ง 2 แผน
  - เพิ่มอาจารย์ประจำหลักสูตร 7 คน (พร้อมคุณวุฒิ/มหาวิทยาลัย/ปี)
  - เพิ่มอาจารย์ผู้สอน 6 คน (พร้อมคุณวุฒิ/มหาวิทยาลัย/ปี)
  - ระบุอาจารย์พิเศษ: ไม่มี
  - แก้ไข linked entity เป็น [[มหาวิทยาลัยราชภัฏอุตรดิตถ์]]

## [2026-05-11] update | CLO รายวิชาแบบละเอียด (ทุกวิชา)
- Created summary page: summaries/clo-all-courses-detailed.md
- Purpose: เพิ่มโครงสร้างรายละเอียดรายวิชา เพื่อรองรับการตอบคำถาม CLO–PLO alignment แบบลงลึก

## [2026-05-11] ingest | รวมเล่ม CLO รายวิชา.docx (full re-ingest)
- Source: รวมเล่ม CLO รายวิชา.docx (758 KB) — สกัดด้วย scripts/generate_clo_wiki.py
- Updated: summaries/clo-all-courses-detailed.md
- ครบทุกรายวิชา 33 วิชา (บังคับ 6, วิทยานิพนธ์/สารนิพนธ์ 5, เลือก 22)
- เพิ่ม CLO รายข้อ + Bloom's level + CLO→PLO mapping ครบทุกวิชา
- Created: raw/clo-all-courses-extract.md (raw extraction)

## [2026-05-12] create | CLO–YLO mapping
- Created summary page: summaries/clo-ylo-mapping.md (396 lines)
- Derived YLO1, YLO2, YLO2b จากโครงสร้างแผนการศึกษา (ไม่มี YLO ทางการ)
- Generated via scripts/generate_clo_ylo_map.py

## [2026-05-12] update | index.md + concepts/yleo.md
- index.md: เพิ่ม entry clo-ylo-mapping.md ใต้ Summaries, อัปเดต total pages เป็น 9
- concepts/yleo.md: เขียนใหม่ทั้งหมด — เพิ่มสรุป YLO1/YLO2/YLO2b พร้อมตาราง PLO coverage และ link ไป [[summaries/clo-ylo-mapping]]

## [2026-05-12] ingest | ข้อมูลพื้นฐาน AUN-QA-สายสนับสนุน30042569(1).docx
- Source: ข้อมูลพื้นฐาน AUN-QA-สายสนับสนุน30042569(1).docx (609 paragraphs, 4 tables)
- Created raw: raw/support-data-extract.md
- Created summary: summaries/support-data-summary.md
- ครอบคลุม Criteria 4.2/4.3/4.7, 5.1–5.8, 6.1–6.6, 7.1/7.3/7.4/7.5/7.6/7.7/7.9
- ข้อมูลสำคัญ: เจ้าหน้าที่สนับสนุน 143 คน, WiFi 795 จุด, คอมพิวเตอร์ 277 เครื่อง, คะแนนประเมินสิ่งอำนวยความสะดวก 4.34
- Updated index.md: total pages 10

## [2026-05-12] create | evidence-index.md + teaching-activities.md
- Created: summaries/evidence-index.md — AUNQA evidence codes ทั้งหมด 92 รายการ (C4: 3, C5: 35, C6: 19, C7: 35) พร้อม URL 38 ลิงก์ จัดตาม Criteria/Sub-criterion
- Created: summaries/teaching-activities.md — ตาราง Teaching Activities ครบ 32 วิชา (Learning Environment, Teaching Methods, Learning Activities, Assessment Methods)
- Scripts: scripts/extract_evidence_index.py, scripts/extract_clo_teaching_activities.py
- Updated index.md: total pages 12