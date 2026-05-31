# Synology Docker 8080 + syweb.kidcbc.work

## อาการ

- `https://syweb.kidcbc.work/` → HTTP 500 (Cloudflare → NAS port 8080)
- ภายใน NAS: ปิด `apps/.htaccess` แล้ว `curl http://127.0.0.1:8080/default/public/index.html` → 200
- เปิด `.htaccess` แล้ว root และ `/SSVT/` → 500

## โครงสร้าง

| Path | เนื้อหา |
|------|---------|
| `/volume1/docker/ci4_web_system/apps/.htaccess` | routing หลัก |
| `.../apps/default/public/` | static CE&AI site (rsync จาก `docs/`) |
| `.../apps/SSVT/` | ระบบ SSVT (CodeIgniter) |

## แนวทางแก้ (root = static, `/SSVT/` = CI4)

แก้ `apps/.htaccess` ให้แยกชัด:

```apache
RewriteEngine On
RewriteBase /

# SSVT — ส่งเข้า front controller
RewriteRule ^SSVT/(.*)$ SSVT/public/index.php/$1 [L,QSA]

# ไฟล์ static ที่มีอยู่จริง
RewriteCond %{REQUEST_FILENAME} -f [OR]
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^ - [L]

# root → static site
RewriteRule ^$ default/public/index.html [L]
RewriteRule ^(.+)$ default/public/$1 [L]
```

## ตรวจสอบก่อน Cloudflare

```bash
ssh beebrain@100.78.170.75
curl -sI -H 'Host: syweb.kidcbc.work' http://127.0.0.1:8080/ | head -3
curl -sI -H 'Host: syweb.kidcbc.work' http://127.0.0.1:8080/SSVT/ | head -3
```

Deploy static:

```bash
rsync -avz docs/ beebrain@100.78.170.75:/volume1/docker/ci4_web_system/apps/default/public/
```

GitHub Pages (ทางเลือก): เปิด Settings → Pages → `/docs` จาก branch `main`.
