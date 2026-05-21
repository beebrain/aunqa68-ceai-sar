# AUNQA Evidence Gap Analysis Report

Analyzed New Directory: `sections/` (linked to `SAR-CEAI-2568.tex`)
Analyzed Old Directory: `sections_old/` (linked to `AUNQA68Report.tex`)
Reference evidence index: `aun-qa-wiki/summaries/evidence-index.md`

## 1. Summary of Statistics
| Metric | New `sections/` | Old `sections_old/` |
| --- | --- | --- |
| **Unique \evidence declarations** | 49 | 0 |
| **Unique AUNQA codes cited** | 53 | 43 |
| **Explicit `\marknote` tags** | 4 | 13 |
| **Unresolved placeholders** | 0 | 3 |

## 2. Explicit \marknote (Missing Items tagged in NEW LaTeX)
| File | Line | Content |
| --- | --- | --- |
| `03_spo_criteria.tex` | 34 | คะแนนข้างต้นเป็นการประเมินตนเองเบื้องต้น หลักสูตรใหม่ที่ยังไม่มีบัณฑิตจะได้คะแนนสูงสุดไม่เกิน 3/7 ในเกณฑ์ที่ต้องการผลลัพธ์จริง |
| `10_criteria7_facilities.tex` | 197 | กรอบสมรรถนะบุคลากรสายสนับสนุนด้านสิ่งอำนวยความสะดวกอยู่ระหว่างพัฒนาให้ชัดเจนและเป็นระบบมากขึ้น คาดว่าจะแล้วเสร็จในปีงบประมาณ~2569 |
| `11_criteria8_outcomes.tex` | 8 | หลักสูตรเป็นหลักสูตรใหม่ พ.ศ.~2568 เริ่มรับนักศึกษาครั้งแรกในภาคการศึกษา~2/2568 จำนวน~4 คน ณ ปีการศึกษา~2568 ยังไม่มีบัณฑิตสำเร็จการศึกษา ดังนั้นข้อมูลเชิงผลลัพธ์ระยะยาว (Pass Rate, Employability, PLO Achievement) จึงอยู่ในขั้น ``Established'' คือมีระบบและแผนวัดผลแล้ว แต่ยังไม่มีผลจริง ซึ่งเป็นข้อจำกัดเชิงโครงสร้างของหลักสูตรใหม่ทุกหลักสูตร มิใช่ความบกพร่องในการดำเนินงาน |
| `13_appendix.tex` | 134 | ตาราง PLO-CLO Mapping Matrix สมบูรณ์สำหรับทุกรายวิชา (33 วิชา) อยู่ใน รวมเล่ม CLO รายวิชา (AUNQA-1-3) ซึ่งแนบท้ายเป็นเอกสารแยก ตารางด้านล่างแสดงเฉพาะวิชาบังคับ~6 วิชาเพื่อให้เห็นภาพรวม |

## 3. Master SAR Evidence (AUNQA-X-Y) Missing from NEW LaTeX
These items are defined in `evidence-index.md` but are not declared or cited anywhere in the `sections/` directory:

| Code | Description |
| --- | --- |
| `AUNQA-4-1` | ประกาศอุทธรณ์ผลการประเมิน พ.ศ. 2567 |
| `AUNQA-4-2` | ข้อบังคับบัณฑิตศึกษา พ.ศ. 2566 |
| `AUNQA-4-3` | ประกาศส่งผลการประเมิน/กำกับติดตาม พ.ศ. 2567 |
| `AUNQA-5-1` | แผนบริหารทรัพยากรบุคคล 2565–2569 |
| `AUNQA-5-2` | ประกาศนโยบายพัฒนาคุณภาพอาจารย์ |
| `AUNQA-5-3` | ข้อบังคับบริหารงานบุคคล |
| `AUNQA-5-4` | รายงานพัฒนาอาจารย์/อบรม |
| `AUNQA-6-1` | ข้อบังคับบัณฑิตศึกษา พ.ศ. 2566 |
| `AUNQA-6-2` | ประกาศรับสมัครบัณฑิตศึกษา 2568 |
| `AUNQA-6-3` | ฐานข้อมูล/บริการสำนักวิทยบริการ |
| `AUNQA-6-4` | ความพึงพอใจ / แบบสำรวจหลักสูตร |
| `AUNQA-6-5` | ปฏิทินกิจกรรมเสริม |
| `AUNQA-7-1` | รายงานสิ่งอำนวยความสะดวกคณะ (อาคาร 10) |
| `AUNQA-7-2` | ฐานข้อมูล/สัญญา ห้องสมุด |
| `AUNQA-7-3` | แผนแม่บท IT ศูนย์คอมพิวเตอร์ |
| `AUNQA-7-4` | รายงานประเมินคุณภาพสิ่งอำนวยความสะดวก |
| `AUNQA-7-5` | บันทึกตรวจห้องปฏิบัติการก่อนเปิดภาค |
| `AUNQA-8-1` | สถิตินักศึกษา (REG) |
| `AUNQA-8-2` | แผน Alumni Tracking CE\&AI |
| `AUNQA-8-3` | ผลงานวิจัยอาจารย์ 5 ปี |
| `AUNQA-8-4` | สรุปผล CLO / ความก้าวหน้าวิทยานิพนธ์และข้อมูลระหว่างทางเชื่อม PLO |
| `AUNQA-8-5` | แบบสำรวจความพึงพอใจผู้มีส่วนได้ส่วนเสีย (แผนและผลรายภาค) |
| `AUNQA-9-1` | รายงานประชุม กมศ. หลักสูตร |
| `AUNQA-9-2` | Vision/Mission มหาวิทยาลัยและคณะ |
| `AUNQA-9-3` | ยุทธศาสตร์ 5 ปี |
| `AUNQA-9-4` | จำนวนนักศึกษาและบัณฑิต |

## 4. Granular Sub-evidence (AUNQA-C-S-N) Missing from NEW LaTeX
These items are defined in the support data index but are not cited anywhere in the `sections/` directory. These represent potential gaps where supporting details could be added:

| Code | Description | URL |
| --- | --- | --- |
| `AUNQA-5-4-2` | รายงานการประชุม กบ.วช. เพื่อพิจารณาการอนุมัติผู้สอน ประจำภาคเรียนต่าง ๆ | — |
| `AUNQA-5-5-2` | ข้อบังคับมหาวิทยาลัยราชภัฏอุตรดิตถ์ ว่าด้วย การเทียบตำแหน่งทางวิชาการของพนักงานม… | — |
| `AUNQA-5-5-3` | ข้อบังคับมหาวิทยาลัยราชภัฏอุตรดิตถ์ ว่าด้วย หลักเกณฑ์และวิธีการพิจารณาแต่งตั้งบุ… | — |
| `AUNQA-5-5-4` | ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง อัตราค่าตอบแทนการประชุมคณะกรรมการผู้ทรงค… | — |
| `AUNQA-5-5-5` | ประกาศคณะกรรมการพิจารณาตำแหน่งทางวิชาการ เรื่อง แนวปฏิบัติในการประเมินผลการสอนเพ… | — |
| `AUNQA-5-5-6` | ประกาศคณะกรรมการพิจารณาตำแหน่งทางวิชาการ เรื่อง ขั้นตอนและวิธีการเกี่ยวข้องกับผล… | — |
| `AUNQA-5-5-7` | ประกาศคณะกรรมการพิจารณาตำแหน่งทางวิชาการ เรื่อง ขั้นตอนและวิธีการเกี่ยวข้องกับกา… | — |
| `AUNQA-5-5-8` | ข้อบังคับมหาวิทยาลัยราชภัฏอุตรดิตถ์ ว่าด้วย หลักเกณฑ์ วิธีการ และเงื่อนไขการเพิ่… | — |
| `AUNQA-5-5-9` | ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง การกำหนดค่ากลาง ฐานในการคำนวณ และช่วงค่า… | — |
| `AUNQA-5-6-2` | สิทธิประโยชน์ของพนักงานราชการ พ.ศ. 2554 | — |
| `AUNQA-5-6-3` | ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง ขั้นตอนและแนวปฏิบัติในการลา | — |
| `AUNQA-5-6-4` | ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง วันและเวลาทำงาน วันหยุด และวันลาพนักงานห… | — |
| `AUNQA-5-6-5` | ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง วันและเวลาทำงาน วันหยุด และวันลาพนักงานห… | — |
| `AUNQA-5-6-6` | ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง สิทธิการลาของอาจารย์ชาวต่างประเทศ พ.ศ. 2… | — |
| `AUNQA-5-6-7` | ระเบียบมหาวิทยาลัยราชภัฏอุตรดิตถ์ ว่าด้วย การจัดสวัสดิการภายในมหาวิทยาลัย พ.ศ. 2… | — |
| `AUNQA-5-6-8` | ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง สวัสดิการเกี่ยวกับเงินช่วยเหลือครอบครัว … | — |
| `AUNQA-5-6-9` | ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง สวัสดิการเกี่ยวกับเงินฌาปนกิจสงเคราะห์ พ… | — |
| `AUNQA-5-6-10` | ประกาศสภามหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง การตรวจสุขภาพประจำปี พ.ศ. 2565 | — |
| `AUNQA-5-6-11` | ประกาศสภามหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง การประกันสุขภาพและอุบัติเหตุ พ.ศ. 256… | — |
| `AUNQA-5-6-12` | กองทุนสำรองเลี้ยงชีพ กลุ่มมหาวิทยาลัยราชภัฏ (SCB) | — |
| `AUNQA-5-6-13` | รายงานกองทุนสวัสดิการมหาวิทยาลัย | — |
| `AUNQA-5-6-14` | รายงานประกันสุขภาพกลุ่ม (ไทยสมุทรประกันชีวิต) | — |
| `AUNQA-5-7-2` | – ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง หลักเกณฑ์การจัดสรรทุนเพื่อการพัฒนาบุคล… | — |
| `AUNQA-5-7-3` | – ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง หลักเกณฑ์การจัดสรรทุนเพื่อการพัฒนาบุคล… | — |
| `AUNQA-5-7-4` | - ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่อง หลักเกณฑ์การจัดสรรทุนเพื่อการพัฒนาบุคล… | — |
| `AUNQA-6-1-3` | ระบบการรับนักศึกษาของมหาวิทยาลัยราชภัฏอุตรดิตถ์ | https://academic.uru.ac.th/SmartUru/ |
| `AUNQA-6-1-4` | เพจประชาสัมพันธ์รับสมัครนักศึกษาของมหาวิทยาลัย  Fnh94Gxp1JPcMOiU&share… | https://www.facebook.com/SmartURU?rdid= |
| `AUNQA-6-2-5` | แผนการจัดกิจกรรมพัฒนานักศึกษา มหาวิทยาลัยราชภัฏอุตรดิตถ์ ระยะ 5 ปี (พ.ศ. 2565-25… | — |
| `AUNQA-6-2-6` | แผนการจัดกิจกรรมพัฒนานักศึกษา มหาวิทยาลัยราชภัฏอุตรดิตถ์ ปีการศึกษา 2568 | — |
| `AUNQA-6-4-4` | แผนกลยุทธ์ทางการเงินมหาวิทยาลัยราชภัฏอุตรดิตถ์ พ.ศ.2565-2569 | — |
| `AUNQA-6-5-2` | ประกาศมหาวิทยาลัยราชภัฏอุตรดิตถ์ เรื่องเกณฑ์มาตรฐานความสามารถด้านภาษาสำหรับอาจาร… | — |
| `AUNQA-6-5-3` | ข้อมูลบุคลากรแยกหน่วยงาน | https://personnel.uru.ac.th/hrms_statistics/dep_person_support_all |
| `AUNQA-6-6-1` | ผลการประเมินระบบการรับนักศึกษาและระบบการรับสมัครเข้าเรียนของมหาวิทยาลั… | https://script.google.com/macros/s/AKfycbx3eBBGBek89qUaPH3x5QK6HrPTLIsOjz-MPiIDYEo8SzkkVrg8NjxnwSVOrdhLT1Vxfw/exec |
| `AUNQA-6-6-2` | ผลการประเมินการให้บริการและช่วยเหลือผู้เรียนต่อการจัดการศึกษา กิจกรรมส… | https://script.google.com/macros/s/AKfycbxBQsD4j6s27-82T4xLy-L4Y9IY208MvNAZ9I-sj_xbJYXGB2-tMmjiUkQ-otuuAhfs/exec |
| `AUNQA-7-1-2` | ระบบตรวจสอบ สถานะห้องเรียนแบบเรียลไทม์ | https://academic.uru.ac.th/appl/admin/check_room.asp |
| `AUNQA-7-1-3` | ระบบจองห้องเรียน/ เปลี่ยนแปลงห้องเรียนสำหรับผู้ใช้บริการ : | https://academic.uru.ac.th/AcademicWEB/teacher/src/login.php |
| `AUNQA-7-3-2` | เว็บไซต์รวบรวมลิงก์ฐานข้อมูลต่างประเทศ (Open Access) | https://sites.google.com/uru.ac.th/online-database/open-access?authuser=0 |
| `AUNQA-7-3-3` | เว็บไซต์รวบรวมลิงก์ฐานข้อมูลเพื่อบริการงานวิจัย | https://sites.google.com/uru.ac.th/research-support-services/home |
| `AUNQA-7-3-4` |  | https://drive.google.com/drive/folders/1Njqi4DCvD5Ky7djVhcV0-mFv8rVm5XC- |
| `AUNQA-7-4-2` | การให้สิทธิ์นักศึกษาใช้ software ถูกกฎหมาย (Microsoft) | — |
| `AUNQA-7-4-3` | ระบบ URU Exam Center สำหรับทดสอบทักษะดิจิทัลก่อนสำเร็จการศึกษา | — |
| `AUNQA-7-4-4` | ระบบ email ในการรับส่งจดหมายอิเล็กทรอนิกส์ (email@live.uru.ac.th) | — |
| `AUNQA-7-4-5` | ระบบบริหารจัดการเรียนการสอนออนไลน์ URU LMS – Life & Learn ( | https://lms.uru.ac.th) |
| `AUNQA-7-4-6` | ระบบจัดการเอกสารการประชุมอิเล็กทรอนิกส์ มหาวิทยาลัยราชภัฏอุตรดิตถ์ (E … | https://meeting.uru.ac.th) |
| `AUNQA-7-4-7` | ระบบสารสนเทศเพื่อสนับสนุนภาระงานคณาจารย์ มหาวิทยาลัยราชภัฏอุตรดิตถ์ ( | https://workload.uru.ac.th) |
| `AUNQA-7-4-8` | ระบบ URU Lifelong Learning สำหรับการจัดการศึกษาแบบการเรียนรู้ตลอดชีวิต… | https://lifelong.uru.ac.th) |
| `AUNQA-7-4-9` | ระบบสารสนเทศด้านเศรษฐกิจสร้างสรรค์ด้วยวัฒนธรรม ประเพณี ภูมิปัญญา แบบร่… | https://icac.uru.ac.th/) |
| `AUNQA-7-4-10` | ระบบประเมินภาวะซึมเศร้า มหาวิทยาลัยราชภัฏอุตรดิตถ์ ( | https://mentalhealth.uru.ac.th/) |
| `AUNQA-7-4-11` | ระบบอาจารย์ที่ปรึกษา ( | https://advisor.uru.ac.th) |
| `AUNQA-7-4-12` | ระบบระบบลงทะเบียนบัณฑิตมหาวิทยาลัยราชภัฏอุตรดิตถ์ ( | https://bundit.uru.ac.th/) |
| `AUNQA-7-4-13` | ระบบลงทะเบียนกิจกรรม ( | https://activity.uru.ac.th/login) |
| `AUNQA-7-4-14` | ระบบห้องสมุดอัตโนมัติ Walai Auto Lib พร้อมระบบสืบค้นออนไลน์ OPAC URU ( | https://opac.uru.ac.th) |
| `AUNQA-7-4-15` |  | https://drive.google.com/drive/folders/1Njqi4DCvD5Ky7djVhcV0-mFv8rVm5XC- |
| `AUNQA-7-6-2` | มาตรฐานบริการการให้คำปรึกษาวัยรุ่น สำหรับบุคลากรสาธารณสุข | — |
| `AUNQA-7-6-3` | ข้อบังคับว่าด้วยอุปกรณ์กีฬาว่ายน้ำของสหพันธ์ว่ายน้ำนานาชาติ | — |
| `AUNQA-7-6-4` | อุปกรณ์สำหรับบริการนักศึกษาพิการ | https://drive.google.com/drive/folders/1sSq4mhf0rCnX2Tf0zAka2VaCAaRophXv |
| `AUNQA-7-7-2` | สระว่ายน้ำเฉลิมราชภัฏ ศูนย์ออกกำลังกาย สนามกีฬา | — |
| `AUNQA-7-7-3` | หอพักนักศึกษา | — |
| `AUNQA-7-7-4` | ห้องปฐมพยาบาลเบื้องต้น ณ กองพัฒนานักศึกษา ชั้น 2 อาคารเรือนต้นสัก (อาคาร 12) | — |
| `AUNQA-7-7-5` | อุปกรณ์สำหรับบริการนักศึกษาพิการ | — |
| `AUNQA-7-7-6` | ร้านค้า และสิ่งอำนวยความสะดวกอื่นๆ | https://drive.google.com/drive/folders/1sSq4mhf0rCnX2Tf0zAka2VaCAaRophXv |
| `AUNQA-7-9-2` |  | https://drive.google.com/drive/folders/1Njqi4DCvD5Ky7djVhcV0-mFv8rVm5XC- |

## 5. Undefined Evidence Codes Used in NEW LaTeX
These codes are cited or declared in the LaTeX files but are NOT listed in the `evidence-index.md`:

| Code | File | Line | Context |
| --- | --- | --- | --- |
| `AUNQA-1-4b` | `04_criteria1_plos.tex` | 166 | \textbf{ผลการสำรวจความต้องการของผู้มีส่วนได้ส่วนเสีย (AUNQA-1-4b)} ดำเนินการเก็บข้อมูลผ่านแบบสอบถามออนไลน์ในช่วงเดือนมิถุนายน~2567 ได้รับแบบสอบถามคืน $n = 31$ ราย ประกอบด้วยผู้ที่กำลังศึกษาอยู่ 17~คน (54.8\%) และผู้สำเร็จการศึกษาและทำงานแล้ว 14~คน (45.2\%) มีสัดส่วนเพศชาย 21~คน (67.7\%) และเพศหญิง 10~คน (32.3\%) กระจายช่วงอายุตั้งแต่ 18 ปีจนถึงมากกว่า 35~ปี |
| `AUNQA-1-4b` | `04_criteria1_plos.tex` | 289 | \evidence{AUNQA-1-4b}{แบบสอบถามผู้มีส่วนได้ส่วนเสีย: ผลสำรวจ $n=31$ ราย (มิถุนายน 2567) --- AUNQA-1-4b\_stakeholder\_survey\_responses\_31คน.csv} |
| `AUNQA-1-4b` | `04_criteria1_plos.tex` | 289 | \evidence{AUNQA-1-4b}{แบบสอบถามผู้มีส่วนได้ส่วนเสีย: ผลสำรวจ $n=31$ ราย (มิถุนายน 2567) --- AUNQA-1-4b\_stakeholder\_survey\_responses\_31คน.csv} |
| `AUNQA-C6-STSAT-2568` | `04_criteria1_plos.tex` | 290 | \evidence{AUNQA-C6-STSAT-2568}{แบบสำรวจความพึงพอใจนักศึกษาและผู้มีส่วนได้ส่วนเสีย CE\&AI ปีการศึกษา~2568 ($n=4$): คะแนนความพึงพอใจต่อวัตถุประสงค์/PLO เฉลี่ย~4.75/5.00 --- student\_satisfaction\_survey\_2568.csv} |
| `AUNQA-C6-STSAT-2568` | `05_criteria2_structure.tex` | 171 | \evidence{AUNQA-C6-STSAT-2568}{แบบสำรวจความพึงพอใจนักศึกษาและผู้มีส่วนได้ส่วนเสีย CE\&AI ปีการศึกษา~2568 ($n=4$): คะแนนความพึงพอใจโครงสร้าง/เนื้อหาเฉลี่ย~4.75/5.00 --- student\_satisfaction\_survey\_2568.csv} |
| `AUNQA-C6-STSAT-2568` | `06_criteria3_teaching.tex` | 123 | \evidence{AUNQA-C6-STSAT-2568}{แบบสำรวจความพึงพอใจนักศึกษาและผู้มีส่วนได้ส่วนเสีย CE\&AI ปีการศึกษา~2568 ($n=4$): คะแนนด้านคุณภาพการสอน/ประเมิน~5.00/5.00 --- student\_satisfaction\_survey\_2568.csv} |
| `AUNQA-C6-STSAT-2568` | `07_criteria4_assessment.tex` | 165 | \evidence{AUNQA-C6-STSAT-2568}{แบบสำรวจความพึงพอใจนักศึกษาและผู้มีส่วนได้ส่วนเสีย CE\&AI ปีการศึกษา~2568 ($n=4$): คะแนนด้านความชัดเจนเกณฑ์ประเมินและกิจกรรม Practical~5.00/5.00 --- student\_satisfaction\_survey\_2568.csv} |
| `AUNQA-C6-STSAT-2568` | `08_criteria5_staff.tex` | 151 | \evidence{AUNQA-C6-STSAT-2568}{แบบสำรวจความพึงพอใจนักศึกษาและผู้มีส่วนได้ส่วนเสีย CE\&AI ปีการศึกษา~2568 ($n=4$): คะแนนด้านคุณภาพอาจารย์/บุคลากรสนับสนุน~5.00/5.00 --- student\_satisfaction\_survey\_2568.csv} |
| `AUNQA-C6-STSAT-2568` | `10_criteria7_facilities.tex` | 254 | \evidence{AUNQA-C6-STSAT-2568}{แบบสำรวจความพึงพอใจนักศึกษาและผู้มีส่วนได้ส่วนเสีย CE\&AI ปีการศึกษา~2568 ($n=4$): คะแนนด้านสิ่งสนับสนุนการเรียนรู้ (Lab/ฐานข้อมูล/WiFi/ห้องเรียน) ทุกรายการ~5.00/5.00 --- student\_satisfaction\_survey\_2568.csv} |
| `AUNQA-C6-STSAT-2568` | `11_criteria8_outcomes.tex` | 180 | \evidence{AUNQA-C6-STSAT-2568}{แบบสำรวจความพึงพอใจนักศึกษาและผู้มีส่วนได้ส่วนเสีย CE\&AI ปีการศึกษา~2568 ($n=4$): เฉลี่ยรวม~4.94/5.00; 100\% ระบุบัณฑิตสอดคล้องกับตลาดแรงงาน (สอดคล้องมาก/อย่างยิ่ง) --- student\_satisfaction\_survey\_2568.csv} |
| `AUNQA-2-7` | `05_criteria2_structure.tex` | 147 | \item \textbf{การทบทวนรายวิชาประจำปี} ผ่านการจัดทำ มคอ.5 (รายงานผลการดำเนินการของรายวิชา) เมื่อสิ้นสุดแต่ละภาคการศึกษา อาจารย์ผู้สอนรายงานผลการประเมิน วิเคราะห์ปัญหา และเสนอแนวทางปรับปรุง (อ้างอิง AUNQA-2-7) |
| `AUNQA-2-7` | `05_criteria2_structure.tex` | 170 | \evidence{AUNQA-2-7}{แบบรายงาน มคอ.5 ระบบการทบทวนรายวิชาประจำภาคการศึกษา} |
| `AUNQA-4-1-1` | `07_criteria4_assessment.tex` | 160 | \evidence{AUNQA-4-1-1}{ตาราง Assessment Methods รายวิชาบังคับ (มคอ.3 ทุกวิชา)} |
| `AUNQA-6-2-2` | `09_criteria6_studentsupport.tex` | 70 | นอกจากแผนระดับมหาวิทยาลัยแล้ว หลักสูตรได้จัดปฐมนิเทศนักศึกษาเมื่อวันที่~12 ตุลาคม~2568 โดยมีรองอธิการบดี รศ.ดร.อิสระ อินจันทร์ และคณบดีคณะเทคโนโลยีอุตสาหกรรม ผศ.ดร.ชัชพล เกษวิริยะกิจ เข้าร่วม ซึ่งเป็นส่วนหนึ่งของแผนระยะสั้นในการให้ข้อมูลหลักสูตร นโยบายมหาวิทยาลัย และแนวทางการศึกษาระดับบัณฑิตศึกษาแก่นักศึกษาใหม่ (อ้างอิง~AUNQA-6-2-2) |
| `AUNQA-6-2-2` | `09_criteria6_studentsupport.tex` | 251 | \evidence{AUNQA-6-2-2}{แผน IT 2568: \url{https://lifelong.uru.ac.th/} (AUNQA-6-2-2\_แผนIT\_2568.pdf)} |
| `AUNQA-6-2-2` | `09_criteria6_studentsupport.tex` | 251 | \evidence{AUNQA-6-2-2}{แผน IT 2568: \url{https://lifelong.uru.ac.th/} (AUNQA-6-2-2\_แผนIT\_2568.pdf)} |
| `AUNQA-6-2-2` | `13_appendix.tex` | 64 | AUNQA-6-2-2 & แผน IT 2568 (\url{https://lifelong.uru.ac.th}) & C6 \\ |
| `AUNQA-8-1-1` | `11_criteria8_outcomes.tex` | 174 | \evidence{AUNQA-8-1-1}{ข้อบังคับ มรอ. ว่าด้วยการศึกษาระดับบัณฑิตศึกษา พ.ศ.2566 (เกณฑ์สำเร็จการศึกษา)} |
| `AUNQA-8-3-1` | `11_criteria8_outcomes.tex` | 175 | \evidence{AUNQA-8-3-1}{ทุนวิจัย Fundamental Fund ผศ.ดร.พัชรี มณีรัตน์ ร่วมกับ รพ.อุตรดิตถ์} |
| `AUNQA-8-3-1` | `13_appendix.tex` | 84 | AUNQA-8-3-1 & ทุนวิจัย Fundamental Fund ผศ.ดร.พัชรี มณีรัตน์ (รพ.อุตรดิตถ์) & C8 \\ |
| `AUNQA-8-3-2` | `11_criteria8_outcomes.tex` | 176 | \evidence{AUNQA-8-3-2}{ทุนวิจัย สวก. ผศ.ดร.กาญจนา ดาวเด่น (ควบคุมด้วงมะพร้าว)} |
| `AUNQA-8-3-2` | `13_appendix.tex` | 86 | AUNQA-8-3-2 & ทุนวิจัย สวก. ผศ.ดร.กาญจนา ดาวเด่น (ควบคุมด้วงมะพร้าว) & C8 \\ |
| `AUNQA-8-3-3` | `11_criteria8_outcomes.tex` | 177 | \evidence{AUNQA-8-3-3}{รางวัลชนะเลิศงานวันเทคโนโลยีครั้งที่ 11 นายจิรกิตติ์ วราภรณ์ (ก.พ. 2569)} |
| `AUNQA-8-3-3` | `13_appendix.tex` | 88 | AUNQA-8-3-3 & รางวัลชนะเลิศงานวันเทคโนโลยีครั้งที่ 11 นายจิรกิตติ์ วราภรณ์ & C8 \\ |
| `AUNQA-8-4-1` | `11_criteria8_outcomes.tex` | 178 | \evidence{AUNQA-8-4-1}{ระบบ CLO Aggregation สำหรับวัด PLO Achievement (ผ่าน มคอ.5)} |
| `AUNQA-8-5-1` | `11_criteria8_outcomes.tex` | 179 | \evidence{AUNQA-8-5-1}{Facebook Page สถิติ: 491 followers, 99 posts, engagement 11 หน่วยงาน} |
| `AUNQA-8-5-1` | `13_appendix.tex` | 90 | AUNQA-8-5-1 & Facebook Page: 491 followers, 99 posts, 11 External SH engagement & C8 \\ |

## 6. Appendix Alignment Check for NEW LaTeX
- **Declared in body but missing in Appendix Table (13_appendix.tex)**:
  - `AUNQA-1-4b` (declared in `04_criteria1_plos.tex`, line 289)
  - `AUNQA-C6-STSAT-2568` (declared in `11_criteria8_outcomes.tex`, line 180)
  - `AUNQA-2-2` (declared in `05_criteria2_structure.tex`, line 167)
  - `AUNQA-2-3` (declared in `05_criteria2_structure.tex`, line 168)
  - `AUNQA-2-7` (declared in `05_criteria2_structure.tex`, line 170)
  - `AUNQA-3-2` (declared in `06_criteria3_teaching.tex`, line 119)
  - `AUNQA-3-3` (declared in `06_criteria3_teaching.tex`, line 120)
  - `AUNQA-3-4` (declared in `06_criteria3_teaching.tex`, line 121)
  - `AUNQA-3-5` (declared in `06_criteria3_teaching.tex`, line 122)
  - `AUNQA-4-1-1` (declared in `07_criteria4_assessment.tex`, line 160)
  - `AUNQA-6-1-2` (declared in `09_criteria6_studentsupport.tex`, line 249)
  - `AUNQA-7-7-1` (declared in `10_criteria7_facilities.tex`, line 252)
  - `AUNQA-8-1-1` (declared in `11_criteria8_outcomes.tex`, line 174)
  - `AUNQA-8-4-1` (declared in `11_criteria8_outcomes.tex`, line 178)
- **Present in Appendix Table but never cited in body files**:
  - None! All appendix items are cited or declared in the body.
