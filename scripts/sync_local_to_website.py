import shutil
from pathlib import Path

# Setup paths
root = Path("/Users/boobee/Library/CloudStorage/OneDrive-UttaraditRajabhatUniversity/Computer Engineering Master Startup - AunQA68")
website_dir = root / "website"
website_evidence_dir = website_dir / "Eviden_aunqa68"

# 1. Root local folders to sync
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

def sync():
    print("=" * 60)
    print("เริ่มต้นซิงโครไนซ์ไฟล์หลักฐานฝั่ง Local ไปยังโฟลเดอร์เว็บไซต์")
    print("=" * 60)
    
    if not website_evidence_dir.exists():
        website_evidence_dir.mkdir(parents=True, exist_ok=True)
        print(f"สร้างโฟลเดอร์หลักฐานเว็บ: {website_evidence_dir}")
        
    copied_count = 0
    
    for label, path in local_folders.items():
        if not path.exists():
            print(f"⚠️ โฟลเดอร์/ไฟล์ในเครื่องไม่พบ: {path}")
            continue
            
        if path.is_file():
            # Copy single file
            dest_file = website_evidence_dir / path.name
            if not dest_file.exists():
                shutil.copy2(path, dest_file)
                print(f"✨ คัดลอกไฟล์สำเร็จ: {path.name} -> {dest_file.relative_to(root)}")
                copied_count += 1
        else:
            # Sync directory recursively
            # For each file in the local directory, determine the relative path
            # and copy it to website_evidence_dir / foldername / subpath
            for f in path.rglob("*"):
                if f.is_file() and not f.name.startswith('.'):
                    # Compute relative path to root directory
                    rel_path = f.relative_to(root)
                    dest_file = website_evidence_dir / rel_path
                    
                    # Create parent directories if they don't exist
                    dest_file.parent.mkdir(parents=True, exist_ok=True)
                    
                    if not dest_file.exists():
                        shutil.copy2(f, dest_file)
                        print(f"✨ คัดลอกไฟล์สำเร็จ: {f.name} -> {dest_file.relative_to(root)}")
                        copied_count += 1
                        
    print("-" * 60)
    print(f"🎉 เสร็จสิ้น! ซิงค์ไฟล์ใหม่สำเร็จทั้งหมด {copied_count} ไฟล์")
    print("=" * 60)

if __name__ == "__main__":
    sync()
