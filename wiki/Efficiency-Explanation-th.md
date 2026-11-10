**English** · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh)

# ประสิทธิภาพ - คำอธิบาย

*แท็บ: เอกสารทางเทคนิค › ประสิทธิภาพ - คำอธิบาย*

[![Efficiency - explanation](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

เอกสารทางเทคนิค *"Come YA-MS calcola l'efficienza di uno sciame"* (YA-MS คำนวณประสิทธิภาพของฝนดาวตกอย่างไร) แสดงภายในโปรแกรมเป็นหน้าพื้นสว่าง เอกสารอธิบาย **ทีละขั้นตอน** ว่าได้ค่าประสิทธิภาพมาอย่างไร และบอกสำหรับแต่ละขั้นตอนว่า **มาจากไหน** โปรแกรมแสดงเอกสารนี้ **ในภาษาของส่วนติดต่อผู้ใช้** (ครบทั้ง 36 ภาษา) เช่นเดียวกับคู่มือการคำนวณ วิกินี้ก็ให้เนื้อหาไว้ใน [การคำนวณประสิทธิภาพ](Efficiency-Calculation-th#ANCHOR_MODEL) และ [เรขาคณิตและการสูญเสียตามเส้นทาง](Geometry-and-Path-Loss-th) ด้วย

## ป้ายกำกับ

ทุกขั้นตอนมีป้ายกำกับสี:

| ป้ายกำกับ | สี | ความหมาย |
|---|---|---|
| **FONTE** (แหล่งอ้างอิง) | น้ำเงิน | ขั้นตอนนี้นำมาจากแหล่งที่อ้างอิง ตัวเลขในวงเล็บหมายถึงรายการท้ายเอกสาร |
| **RILIEVO** (การตรวจสอบ) | เขียว | การเปรียบเทียบระหว่างโปรแกรมกับแหล่งอ้างอิง พร้อมผลลัพธ์ |
| **SCELTA** (การเลือก) | ส้ม | การเลือกของโปรแกรม ไม่ได้นำมาจากแหล่งอ้างอิง: ต้องตรวจสอบกับประสบการณ์ออกอากาศจริง |

## บทต่าง ๆ

| บท | เนื้อหา |
|---|---|
| 1. บทนำ | วัตถุประสงค์ ป้ายกำกับ ความหมายของประสิทธิภาพ (OH5IY, MCG_MS; YA-MS ใช้เส้นทางจริง) |
| 2. การสะท้อนเกิดขึ้นที่ไหน: ชั้น E | รอยดาวตกที่ 80–120 km ความสูงของรอยดาวตก = ฐานนิยมของฮิสโทแกรม Collm (ตรวจสอบ: 89.5 km เมื่อ 5/11/2026) |
| 3. เรขาคณิตของเส้นทาง | โลกและจุดกึ่งกลาง มุมเงยของสายอากาศ (สูตรจากบทความ) โซนร่วมและขอบเขต Hot A / Hot B โลบสายอากาศ (DL6WU, Kraus, W4RNL) |
| 4. จุดเรเดียนท์ของฝนดาวตก | ตำแหน่งของจุดเรเดียนท์ (IMO 2026/2027) วันที่จุดสูงสุด (IMO หรือลองจิจูดสุริยะ) โปรไฟล์กิจกรรม |
| 5. เงื่อนไขการสะท้อน | การสะท้อนแบบสเปคูลาร์ (McKinley) ค่าคลาดเคลื่อนแบบเกาส์เซียน 0.05 rad ทิศที่ดีที่สุด (SM6FHZ) สูตรของ DH9GCD |
| 6. จากจุดหนึ่งสู่ประสิทธิภาพ | จุดสะท้อนทุก 15 km น้ำหนักของแต่ละจุด เปอร์เซ็นต์ การเปรียบเทียบกับ QTFGUI (DJ5HG) |
| 7. การอ่านผลลัพธ์ | ด้าน A / B ดัชนีเส้นทาง สีของจุดเรเดียนท์ โซน PREV ภาพตัดขวางที่มองจากสายอากาศ |
| 8. ความถี่ใช้งานและการสูญเสียตามเส้นทาง | กฎ λ³ / λ² จากเรดาร์สู่แบนด์สมัครเล่น ค่าอ้างอิงการสูญเสียตามเส้นทาง |
| 9. ข้อจำกัดที่ทราบ | รอยดาวตกแบบ underdense เท่านั้น สายอากาศไอโซทรอปิก ค่าที่ใช้ทำงาน |
| 10. แหล่งอ้างอิง | แหล่งอ้างอิง 17 รายการที่มีหมายเลขกำกับ |

## ปุ่มต่าง ๆ

| ปุ่ม | หน้าที่ |
|---|---|
| **ส่งออกเป็น Word (.docx)...** | บันทึกสำเนาของ `data/efficienza_spiegazione.docx` ไว้ในที่ที่คุณเลือก (ชื่อที่แนะนำ *YA-MS - calcolo dell'efficienza.docx*) |
| **เปิดใน Word** | เปิดไฟล์ `.docx` เดียวกันด้วยโปรแกรมเริ่มต้นสำหรับเอกสาร Word (Word, LibreOffice, …) |

## ไฟล์

| ไฟล์ | เนื้อหา |
|---|---|
| `data/efficienza_spiegazione.txt` | ข้อความที่แสดงในแท็บ หนึ่งบล็อกต่อบรรทัด (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | เวอร์ชัน Word |
| `data/spiegazione/efficienza_spiegazione_<code>.txt` / `.docx` | เอกสารเดียวกันในอีก 35 ภาษา (เช่น `_en`, `_de`, `_pt-BR`) |
| `doc/YA-MS_manuale_calcoli.docx` | **คู่มือการคำนวณ** (ภาษาอิตาลี): สมการทั้งหมด (ตัวแก้ไขสมการของ Word) มีหมายเลขกำกับ พร้อมแหล่งอ้างอิง |
| `doc/manuali/YA-MS_manuale_calcoli_<code>.docx` | คู่มือการคำนวณในอีก 35 ภาษา |

เอกสารทั้งสองสร้างใหม่จากซอร์สได้ด้วย `tools/build_spiegazione.py data [code]` และ `node tools/build_manuale.js <file.docx> [code]` คำแปลอยู่ใน `tools/traduzioni_doc/` (`tools/build_documenti.sh` สร้างใหม่ทุกภาษา)
