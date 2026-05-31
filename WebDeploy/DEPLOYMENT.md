# WebDeploy — Production Deployment Folder

> **⚠️ Important:** This folder contains all files ready for production deployment. Do NOT modify files here directly — update `website/` folder instead, then sync to this folder.

---

## สิ่งที่ต้องทราบ

| สิ่ง | รายละเอียด |
|------|-----------|
| **Purpose** | ไฟล์สำเร็จรูปพร้อม Deploy ไปยัง `syweb.kidcbc.work` (Synology NAS) |
| **Source** | `website/` folder (Edit here, ❌ ไม่ใช่ WebDeploy/) |
| **Deploy To** | `beebrain@100.78.170.75:/volume1/docker/ci4_web_system/apps/default/public/` |
| **Sync Method** | `rsync -avz --delete WebDeploy/ beebrain@100.78.170.75:...` |
| **GitHub Pages** | Also served from this folder via `/WebDeploy` path |

---

## Folder Structure

```
WebDeploy/
├── Eviden_aunqa68/          ← หลักฐาน AUNQA (46+ ไฟล์)
│   ├── index.html           ← หน้าแรกหลักฐาน (updated 22 May 2569)
│   ├── มคอ3_รายวิชาบังคับ/  ← TQF 3 ทั้ง 4 วิชา
│   ├── มคอ5_รายวิชาบังคับ/  ← TQF 5 ทั้ง 4 วิชา
│   ├── AUNQA-*.pdf          ← บันทึกการประชุม, รายงาน
│   ├── AUNQA-*.md           ← ร่าง SAR
│   └── ...
├── index.html               ← หน้าแรกหลักสูตร CE&AI
├── courses.html             ← หน้ารายวิชา
├── staff.html               ← หน้าอาจารย์
├── output.css               ← Tailwind CSS
├── *.jpg, *.png             ← ภาพ (อาจารย์, etc.)
├── .nojekyll                ← GitHub Pages marker (ไม่ลบ!)
└── ...

```

---

## Deployment Steps

### 1️⃣ Update Content (DO THIS in `website/`, not here)
```bash
cd website/
# Edit HTML, CSS, or add evidence files
# Test locally
```

### 2️⃣ Sync to WebDeploy (after making changes)
```bash
# Copy from website/ → WebDeploy/
cp -r website/* WebDeploy/
```

### 3️⃣ Commit & Push to GitHub
```bash
git add WebDeploy/
git commit -m "Update WebDeploy: [what changed]"
git push origin main
```

### 4️⃣ Deploy to Synology NAS (via Tailscale SSH)
```bash
rsync -avz --delete WebDeploy/ beebrain@100.78.170.75:/volume1/docker/ci4_web_system/apps/default/public/
```

---

## Important Files & Markers

| File | Purpose | Edit? |
|------|---------|-------|
| `Eviden_aunqa68/index.html` | หลักฐาน index | ❌ Generate from website/ |
| `.nojekyll` | GitHub Pages config | ❌ Don't delete |
| `index.html` | Main site | ❌ Use website/index.html |
| `.DS_Store` | macOS metadata | ❌ Ignore (in .gitignore) |

---

## GitHub Pages Access

Files in WebDeploy/ are accessible via:
- **Production (NAS):** `https://syweb.kidcbc.work/[path]`
- **GitHub Pages:** `https://beebrain.github.io/aunqa68-ceai-sar/[path]`

Example evidence links:
- `https://syweb.kidcbc.work/Eviden_aunqa68/index.html`
- `https://beebrain.github.io/aunqa68-ceai-sar/Eviden_aunqa68/index.html`

---

## For Agents: Workflow

### If you need to update website content:
1. Edit files in `website/` folder ✓
2. Test changes locally
3. After approval: Run sync command above
4. Commit & push
5. Notify deployment team for rsync to NAS

### Do NOT:
- ❌ Edit files directly in `WebDeploy/`
- ❌ Delete `.nojekyll` or `.DS_Store`
- ❌ Add `node_modules/` or `.venv/` here
- ❌ Push uncommitted changes

---

## Last Updated
- **Date:** 22 May 2569 (2026-05-22)
- **Changes:** Rebuilt `Eviden_aunqa68/index.html` with complete evidence catalog (46+ files organized by Criterion C1-C8)
- **Sync Source:** `website/` folder
- **Status:** ✅ Ready for deployment

---

## Questions?
Contact: beebrain or check `website/README.md` for build instructions
