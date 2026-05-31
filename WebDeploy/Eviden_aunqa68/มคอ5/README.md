# มคอ.5 — รายงานการสัมฤทธิ์ผลของผู้เรียนระดับรายวิชา

แม่แบบ Word: `mko5template.docx`  
Class LaTeX: `mko5.cls` (รูปแบบเดียวกับ `มคอ3/mko3.cls`, คอมไพล์ด้วย **XeLaTeX**)

## คอมไพล์ตัวอย่าง

```bash
cd มคอ5
xelatex example.tex
xelatex example.tex
```

ผลลัพธ์: `example.pdf`

## รายวิชาจริง

```bash
./compile_all.sh
# หรือ: xelatex AUN3_7015101.tex (รันสองครั้งต่อไฟล์)
```

| ไฟล์ | ภาค | รายวิชา |
|------|-----|---------|
| `AUN3_7015101` | 2/2568 | เทคโนโลยีอุบัติใหม่ฯ (4 นศ., CLO1--5 ผ่าน 100\%) |
| `AUN3_7015906` | 2/2568 | ระเบียบวิธีวิจัย (CLO4 ผ่านทุกคน) |
| `AUN3_4095101` | 1/2568 | ปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง |
| `AUN3_4095102` | 1/2568 | การเขียนโปรแกรมขั้นสูงสำหรับ ML |

สำเนาหลักฐาน: `ข้อมูลหลักฐานที่ต้องการ/มคอ5_รายวิชาบังคับ/` (`AUN3_*_มคอ5.pdf`)

**ยังต้องจัดทำ:** 7015907, 7015908 (รอ มคอ.3 ก่อน)

## โครงสร้างรายงาน (ตาม template)

1. ข้อมูลหัวรายงาน — `\mkoheaderinfo` (หลังตั้ง `\coursecode`, `\coursename`, …)
2. กิจกรรมที่ดำเนินการจริง — `teachingactualtable` / `\actualrow`
3. วิธีการวัดผล — `assessmentusedtable` / `\assessusedrow`
4. สรุปสัมฤทธิ์ผล — `\closummaryblock` + `\achievementpass` / `\achievementfail`
5. ปัญหา/อุปสรรค — `\mkosectionfour` + `mkotextblock`
6. แผนปรับปรุง — `\mkosectionfive`
7. ข้อเสนอแนะ — `\mkosectionsix`
8. ลงลายมือชื่อ — `\mkosignaturepair`
