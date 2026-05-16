# วิธีรัน OBE/AUN-QA Agent

## ขั้นตอน

### 1. API Key — อ่านอัตโนมัติจาก `~/.continue/config.yaml`
ไม่ต้องตั้งค่าอะไรเพิ่ม — script จะอ่าน MiniMax API key จาก config ของ Continue โดยอัตโนมัติ

> fallback: `export MINIMAX_API_KEY='sk-cp-...'`

### 2. รัน Agent
```bash
cd "/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68"
python3 obe_qa_agent.py
```

---

## คำสั่งใน Agent

| คำสั่ง | ความหมาย |
|--------|----------|
| `/help` | แสดงคำสั่งทั้งหมด |
| `/criteria 1` | เน้นตอบ Criterion 1 (เปลี่ยน 1–8 ได้) |
| `/write` | สลับโหมดร่างคำตอบ SAR (5 ส่วน) |
| `/review` | สลับโหมด Auditor ตรวจคำตอบ |
| `/ask` | กลับโหมดถาม-ตอบปกติ |
| `/evidence` | แสดง evidence codes AUNQA-X-Y |
| `/save` | บันทึกประวัติสนทนาเป็น JSON |
| `/clear` | ล้างประวัติสนทนา เริ่มใหม่ |
| `/exit` | ออกจากโปรแกรม |

---

## ตัวอย่างการใช้งาน

```
คุณ: PLO ของหลักสูตร CE&AI มีกี่ข้อ?

คุณ: /criteria 3
คุณ: อธิบาย Teaching & Learning Approach ที่ใช้ในหลักสูตร

คุณ: /write
คุณ: ร่างคำตอบ Criterion 1.1 เรื่อง ELO

คุณ: /review
คุณ: [วางคำตอบที่ต้องการตรวจ]
```

---

## Knowledge Base ที่โหลดอัตโนมัติ

- PLO / CLO ทุกรายวิชา (32 วิชา)
- YLO1 / YLO2 / YLO2b mapping
- Teaching Activities ครบ 32 วิชา
- Evidence Index 92 รายการ (AUNQA-C-S-N)
- SAR evidence codes (AUNQA-X-Y)
- Support data Criteria 4–7
- AUN-QA 8 Criteria knowledge
