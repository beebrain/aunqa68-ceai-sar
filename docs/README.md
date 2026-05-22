# AUN-QA Reference Website (Static)

เว็บอ้างอิงสำหรับจัดทำ SAR หลักสูตร วศ.ม. วิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ ม.ร.อ. — build จาก `aun-qa-wiki/` (local only, ไม่ commit wiki)

## Build

```bash
python3 website/build.py
```

ผลลัพธ์อยู่ที่ `docs/` (พร้อม deploy บน GitHub Pages)

## GitHub Pages

1. Repo Settings → Pages → Source: **Deploy from branch**
2. Branch: `main`, folder: **`/docs`**
3. หลัง push จะได้ URL ประมาณ `https://beebrain.github.io/aunqa68-ceai-sar/`

## อัปเดตเนื้อหา

แก้ไข `aun-qa-wiki/` แล้วรัน build ใหม่ → commit `docs/` แล้ว push
