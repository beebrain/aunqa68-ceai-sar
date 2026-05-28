# CLAUDE.md — AUN-QA SAR Project

## บทบาทและ Context

โปรเจกต์นี้จัดทำ **SAR (Self-Assessment Report) AUN-QA Version 4.0** ระดับหลักสูตร สำหรับ วศ.ม. วิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ มหาวิทยาลัยราชภัฏอุตรดิตถ์ ปีการศึกษา 2568

## อ่านก่อนทำงานทุกครั้ง

```
aun-qa-wiki/SCHEMA.md   ← คำสั่งฉบับเต็มสำหรับ ingest / query / lint
aun-qa-wiki/index.md    ← catalog ทุก page ใน wiki (อ่านก่อน query)
aun-qa-wiki/log.md      ← ประวัติว่า ingest อะไรไปแล้วบ้าง
```

## Wiki Structure

```
aun-qa-wiki/
├── SCHEMA.md           ← agent instructions (อ่านก่อน)
├── index.md            ← page catalog
├── log.md              ← ingest history
├── guidelines/         ← ground truth: "เนื้อเกณฑ์ที่พึงพิจารณา" ของ ผศ.ดร.ขวัญดาว (Criterion 1-8)
├── concepts/           ← criterion-1 ถึง criterion-8 + CLO/PLO concepts
├── summaries/          ← CLO ทุกวิชา, evidence index, teaching activities, support data
├── entities/           ← มรอ., หลักสูตร CPE&AI
└── raw/                ← extracted text จาก source documents
```

## ไฟล์ SAR หลัก

- `SAR-CEAI-2568.tex` — LaTeX SAR draft (compile ด้วย `latexmkrc`)
- `sections/` — LaTeX sections แยกแต่ละ criterion (04–11)
- `มคอ3/` — มคอ.3 ทุกรายวิชา (LaTeX)

## Source Documents (ยังไม่ได้ ingest ครบ)

| สถานะ | ไฟล์ |
|-------|------|
| ✓ ingest แล้ว | `เอกสารอบรม...ผศ.ดร.ขวัญดาว.pdf`, `มคอ 2...docx`, `รวมเล่ม CLO.docx`, `ข้อมูลพื้นฐาน AUN-QA...docx`, `from_report68.docx` |
| ✓ ingest แล้ว | `66-AUNQAการจัดการธุรกิจสมัยใหม่...pdf` → `aun-qa-wiki/summaries/example-sar-mbm-66.md` |
| ⬜ ยังค้าง | `มคอ3/*.tex` (26 วิชา) |

## Workflow สำหรับ Agent

**Ingest source ใหม่:**
1. อ่าน `aun-qa-wiki/SCHEMA.md` — ดูขั้นตอน Ingest
2. อ่าน `aun-qa-wiki/log.md` — ตรวจว่า ingest แล้วหรือยัง
3. ดำเนินการตาม SCHEMA.md Ingest workflow

**ตอบคำถาม AUN-QA:**
1. อ่าน `aun-qa-wiki/index.md` — หา pages ที่เกี่ยวข้อง
2. อ่าน `aun-qa-wiki/guidelines/[criterion].md` ก่อนเสมอ (ground truth)
3. เสริมด้วย `concepts/` และ `summaries/` สำหรับ evidence จริง

**เขียน/แก้ SAR:**
1. อ่าน guideline ของ criterion นั้น
2. อ่าน evidence จาก summaries/
3. เขียนลงใน `sections/` ไฟล์ที่เกี่ยวข้อง
