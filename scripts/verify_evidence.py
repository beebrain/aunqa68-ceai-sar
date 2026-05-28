import os
import re
import urllib.parse
import json
from pathlib import Path

# Setup paths
root = Path("/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68")
website_dir = root / "website"
eviden_html_path = website_dir / "eviden.html"
website_evidence_dir = website_dir / "Eviden_aunqa68"

# 1. Root local folders to compare
local_folders = {
    "หลักฐานสายสนับสนุน": root / "หลักฐานสายสนับสนุน",
    "หลักฐานการประชุม/01_ระดับหลักสูตร": root / "หลักฐานการประชุม/01_ระดับหลักสูตร",
    "หลักฐานการประชุม/02_ระดับคณะ": root / "หลักฐานการประชุม/02_ระดับคณะ",
    "หลักฐานการประชุม/03_ระดับมหาวิทยาลัย": root / "หลักฐานการประชุม/03_ระดับมหาวิทยาลัย",
    "ระเบียบข้อบังคับและประกาศอื่นๆ": root / "ระเบียบข้อบังคับและประกาศอื่นๆ",
    "มคอ3": root / "มคอ3",
    "มคอ5": root / "มคอ5",
    "มคอ 2 หลักสูตรวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ ผ่านสภา 2 เพิ่ม Comment สภา และ มติสภา.pdf": root / "มคอ 2 หลักสูตรวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ ผ่านสภา 2 เพิ่ม Comment สภา และ มติสภา.pdf",
    "รวมเล่ม CLO รายวิชา.pdf": root / "รวมเล่ม CLO รายวิชา.pdf"
}

def get_all_local_files():
    files = {}
    for label, path in local_folders.items():
        if not path.exists():
            continue
        if path.is_file():
            # It's a single file
            rel_path = str(path.relative_to(root))
            files[rel_path] = {
                "source": "root",
                "abs_path": path,
                "label": label,
                "size": path.stat().st_size
            }
        else:
            # It's a directory, scan recursively
            for f in path.rglob("*"):
                if f.is_file() and not f.name.startswith('.'):
                    rel_path = str(f.relative_to(root))
                    files[rel_path] = {
                        "source": "root",
                        "abs_path": f,
                        "label": label,
                        "size": f.stat().st_size
                    }
    return files

def get_all_website_files():
    files = {}
    if not website_evidence_dir.exists():
        print("Website evidence directory does not exist!")
        return files
    
    for f in website_evidence_dir.rglob("*"):
        if f.is_file() and not f.name.startswith('.'):
            # Path relative to website_evidence_dir
            rel_path = str(f.relative_to(website_evidence_dir))
            files[rel_path] = {
                "source": "website_folder",
                "abs_path": f,
                "size": f.stat().st_size
            }
    return files

def parse_eviden_html_js():
    if not eviden_html_path.exists():
        print("eviden.html not found!")
        return []
    
    content = eviden_html_path.read_text(encoding="utf-8")
    
    # Let's extract the JS array 'const documents = [ ... ]'
    # We will search for 'const documents = [' and capture until the array ends.
    # Since there might be nested braces, let's find the match.
    match = re.search(r'const\s+documents\s*=\s*\[(.*?)\]\s*;', content, re.DOTALL)
    if not match:
        # Try finding it without the trailing semicolon if it varies
        match = re.search(r'const\s+documents\s*=\s*\[(.*?)\]\s*(?=\n|\r|//|\}\s*</script>)', content, re.DOTALL)
        if not match:
            print("Could not find const documents array in eviden.html!")
            return []
        
    array_content = match.group(1)
    
    # We can parse the array content using a regex that extracts individual objects {...}
    # Each object has keys: code, criterion, type, path, th, en.
    # Let's parse them individually.
    object_matches = re.finditer(r'\{\s*(.*?)\s*\},?\s*(?=\{|\]|\Z)', array_content, re.DOTALL)
    
    parsed_docs = []
    for obj in object_matches:
        obj_text = obj.group(1)
        
        # Extract path
        path_match = re.search(r'"path"\s*:\s*"(.*?)"', obj_text)
        if not path_match:
            path_match = re.search(r"'path'\s*:\s*'(.*?)'", obj_text)
            
        if path_match:
            raw_path = path_match.group(1)
            # URL decode the path to get actual file path
            # Remove the "Eviden_aunqa68/" prefix from the path for easier comparison
            clean_path = raw_path
            if clean_path.startswith("Eviden_aunqa68/"):
                clean_path = clean_path[len("Eviden_aunqa68/"):]
            
            decoded_path = urllib.parse.unquote(clean_path)
            
            # Extract code
            code_match = re.search(r'"code"\s*:\s*"(.*?)"', obj_text)
            code = code_match.group(1) if code_match else "N/A"
            
            # Extract th title
            title_match = re.search(r'"title"\s*:\s*"(.*?)"', obj_text)
            title = title_match.group(1) if title_match else "N/A"
            
            parsed_docs.append({
                "raw_path": raw_path,
                "decoded_path": decoded_path,
                "code": code,
                "title": title,
                "raw_obj": obj_text
            })
            
    return parsed_docs

def main():
    print("=" * 60)
    print("เริ่มระบบตรวจสอบความถูกต้องของไฟล์หลักฐานบนเว็บไซต์")
    print("=" * 60)
    
    # Get all actual files
    local_files = get_all_local_files()
    web_files = get_all_website_files()
    html_docs = parse_eviden_html_js()
    
    print(f"1. สรุปข้อมูลเบื้องต้น:")
    print(f"   - จำนวนไฟล์หลักฐานในเครื่อง (Local Root Folders): {len(local_files)} ไฟล์")
    print(f"   - จำนวนไฟล์ที่อัปโหลดไว้บนเว็บไซต์ (Eviden_aunqa68/): {len(web_files)} ไฟล์")
    print(f"   - จำนวนรายการหลักฐานที่ลงทะเบียนในโค้ดเว็บ (eviden.html): {len(html_docs)} รายการ")
    print("-" * 60)
    
    # ----------------------------------------------------
    # เปรียบเทียบที่ 1: ไฟล์ใน Eviden_aunqa68 กับรายการใน eviden.html
    # ----------------------------------------------------
    print(f"\n2. ตรวจสอบไฟล์ในโฟลเดอร์เว็บ (Eviden_aunqa68/) เทียบกับ รายการใน eviden.html:")
    
    html_paths = {doc["decoded_path"]: doc for doc in html_docs}
    
    missing_physical_files = [] # Registered in HTML but missing physically
    for dec_path, doc in html_paths.items():
        if dec_path not in web_files:
            missing_physical_files.append((dec_path, doc))
            
    unregistered_physical_files = [] # Physical file exists but not registered in HTML
    for rel_path, f_info in web_files.items():
        if rel_path not in html_paths:
            unregistered_physical_files.append((rel_path, f_info))
            
    if not missing_physical_files:
        print("   ✅ ไฟล์ที่ลงทะเบียนใน eviden.html ทั้งหมด มีตัวตนอยู่จริงในโฟลเดอร์ Eviden_aunqa68/")
    else:
        print(f"   ❌ พบ {len(missing_physical_files)} ไฟล์ ที่ลงทะเบียนในหน้าเว็บแต่ไม่มีไฟล์จริงในโฟลเดอร์:")
        for idx, (path, doc) in enumerate(missing_physical_files, 1):
            print(f"      {idx}. รหัส: {doc['code']} | ชื่อ: {doc['title']}")
            print(f"         เส้นทางไฟล์ที่เว็บระบุ: {path}")
            
    if not unregistered_physical_files:
        print("   ✅ ไม่มีไฟล์ที่ตกหล่น (ทุกไฟล์ในโฟลเดอร์ Eviden_aunqa68/ ถูกลงทะเบียนบนเว็บแล้ว)")
    else:
        print(f"   ⚠️ พบ {len(unregistered_physical_files)} ไฟล์ ในโฟลเดอร์ Eviden_aunqa68/ ที่ไม่ได้ลงทะเบียนในหน้าเว็บ (ตกหล่น/ยังไม่แสดงผล):")
        for idx, (path, f_info) in enumerate(unregistered_physical_files, 1):
            print(f"      {idx}. เส้นทางไฟล์จริง: Eviden_aunqa68/{path} (ขนาด {f_info['size']/1024:.2f} KB)")

    # ----------------------------------------------------
    # เปรียบเทียบที่ 2: ไฟล์หลักฐานในเครื่อง (Local Root) กับ ไฟล์ใน Eviden_aunqa68 (Website Folder)
    # ----------------------------------------------------
    print("-" * 60)
    print(f"\n3. ตรวจสอบความซิงค์ระหว่างไฟล์ในเครื่อง (Local) กับไฟล์บนเว็บ (Eviden_aunqa68/):")
    
    unsynced_local_files = [] # Exists in local but not in website folder
    for rel_path, f_info in local_files.items():
        if rel_path not in web_files:
            unsynced_local_files.append((rel_path, f_info))
            
    extra_website_files = [] # Exists in website folder but not in local
    for rel_path, f_info in web_files.items():
        if rel_path not in local_files:
            extra_website_files.append((rel_path, f_info))
            
    if not unsynced_local_files:
        print("   ✅ ไฟล์หลักฐานในเครื่องทั้งหมด ถูกคัดลอกไปยังโฟลเดอร์เว็บไซต์ Eviden_aunqa68/ แล้ว")
    else:
        print(f"   ❌ พบ {len(unsynced_local_files)} ไฟล์ในเครื่อง ที่ยังไม่ถูกอัปเดตหรือยังไม่มีบนเว็บไซต์:")
        for idx, (path, f_info) in enumerate(unsynced_local_files, 1):
            print(f"      {idx}. หมวดหมู่: {f_info['label']}")
            print(f"         ชื่อไฟล์: {path}")
            
    if not extra_website_files:
        print("   ✅ โฟลเดอร์เว็บไซต์ Eviden_aunqa68/ ไม่มีไฟล์ส่วนเกินที่ไม่มีในเครื่อง")
    else:
        print(f"   ⚠️ พบ {len(extra_website_files)} ไฟล์บนเว็บไซต์ ที่ไม่มีอยู่จริงในโฟลเดอร์หลักฐานฝั่ง Local (อาจเป็นไฟล์เก่าหรือค้าง):")
        for idx, (path, f_info) in enumerate(extra_website_files, 1):
            print(f"      {idx}. เส้นทาง: {path}")
            
    print("=" * 60)
    print("สิ้นสุดการตรวจสอบ")
    print("=" * 60)

if __name__ == "__main__":
    main()
