[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · **ไทย** · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# ประสิทธิภาพ - คำอธิบาย

*แท็บ: เอกสารทางเทคนิค › ประสิทธิภาพ - คำอธิบาย*

[![ประสิทธิภาพ - คำอธิบาย](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

เอกสารทางเทคนิค *"Come YA-MS calcola l'efficienza di uno sciame"* (YA-MS คำนวณประสิทธิภาพของฝนดาวตกอย่างไร) แสดงภายในโปรแกรมเป็นหน้าพื้นสว่าง เอกสารอธิบาย **ทีละขั้นตอน** ว่าได้ประสิทธิภาพมาอย่างไร และบอกในแต่ละขั้นตอนว่า **มาจากที่ใด** ขณะนี้เอกสาร **เป็นภาษาอิตาลี**; วิกินี้ให้เนื้อหาเป็นภาษาไทยไว้ใน [การคำนวณประสิทธิภาพ](Efficiency-Calculation-th#แบบจำลอง) และ [เรขาคณิตและการสูญเสียตามเส้นทาง](Geometry-and-Path-Loss-th)

## ป้ายกำกับ

ทุกขั้นตอนมีป้ายกำกับสี:

| ป้ายกำกับ | สี | ความหมาย |
|---|---|---|
| **FONTE** (แหล่งที่มา) | น้ำเงิน | ขั้นตอนนี้นำมาจากแหล่งข้อมูลที่อ้างถึง ตัวเลขในวงเล็บอ้างอิงรายการท้ายเอกสาร |
| **RILIEVO** (การตรวจสอบ) | เขียว | การเปรียบเทียบระหว่างโปรแกรมกับแหล่งข้อมูล พร้อมผลลัพธ์ |
| **SCELTA** (การเลือก) | ส้ม | การเลือกของโปรแกรม ไม่ได้นำมาจากแหล่งข้อมูล: ต้องตรวจสอบกับประสบการณ์บนอากาศ |

## บทต่าง ๆ

| บท | เนื้อหา |
|---|---|
| 1. บทนำ | จุดประสงค์ ป้ายกำกับ ความหมายของประสิทธิภาพ (OH5IY, MCG_MS; YA-MS ใช้เส้นทางจริง) |
| 2. การสะท้อนเกิดที่ไหน: ชั้น E | รอยทางที่ 80–120 km; ความสูงของรอยทาง = ฐานนิยมของฮิสโทแกรม Collm (การตรวจสอบ: 89.5 km ในวันที่ 5/11/2026) |
| 3. เรขาคณิตของเส้นทาง | โลกและจุดกึ่งกลาง; มุมเงยของสายอากาศ (สูตรจากบทความ); โซนร่วมและขอบเขต; Hot A / Hot B; ลำคลื่นสายอากาศ (DL6WU, Kraus, W4RNL) |
| 4. จุดกระจายของฝนดาวตก | ตำแหน่งจุดกระจาย (IMO 2026/2027) วันที่ของจุดสูงสุด (IMO หรือลองจิจูดของดวงอาทิตย์) โปรไฟล์กิจกรรม |
| 5. เงื่อนไขการสะท้อน | การสะท้อนแบบกระจกเงา (McKinley) ค่าคลาดเคลื่อนแบบเกาส์เซียน 0.05 rad ทิศที่ดีที่สุด (SM6FHZ) สูตร DH9GCD |
| 6. จากจุดหนึ่งสู่ประสิทธิภาพ | จุดสะท้อนทุก 15 km น้ำหนักของแต่ละจุด เปอร์เซ็นต์; การเปรียบเทียบกับ QTFGUI (DJ5HG) |
| 7. การอ่านผลลัพธ์ | ด้าน A / B ดัชนีเส้นทาง สีของจุดกระจาย โซน PREV ภาพตัดที่มองจากสายอากาศ |
| 8. ความถี่ใช้งานและการสูญเสียตามเส้นทาง | กฎ λ³ / λ² จากเรดาร์สู่ย่านความถี่สมัครเล่น ค่าอ้างอิงของการสูญเสียตามเส้นทาง |
| 9. ข้อจำกัดที่ทราบ | เฉพาะรอยทางแบบ underdense สายอากาศไอโซทรอปิก ค่าที่ใช้งาน |
| 10. แหล่งที่มา | แหล่งที่มา 17 รายการพร้อมหมายเลข |

## ปุ่ม

| ปุ่ม | หน้าที่ |
|---|---|
| **ส่งออกเป็น Word (.docx)...** | บันทึกสำเนาของ `data/efficienza_spiegazione.docx` ไว้ในตำแหน่งที่คุณเลือก (ชื่อที่แนะนำ *YA-MS - calcolo dell'efficienza.docx*) |
| **เปิดใน Word** | เปิด `.docx` เดียวกันด้วยโปรแกรมเริ่มต้นสำหรับเอกสาร Word (Word, LibreOffice, …) |

## ไฟล์

| ไฟล์ | เนื้อหา |
|---|---|
| `data/efficienza_spiegazione.txt` | ข้อความที่แสดงในแท็บ หนึ่งบล็อกต่อบรรทัด (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | ฉบับ Word |
| `doc/YA-MS_manuale_calcoli.docx` | **คู่มือการคำนวณ**: สมการทั้งหมด (ตัวแก้ไขสมการของ Word) พร้อมหมายเลขและแหล่งที่มา |

เอกสารทั้งสองสร้างใหม่จากซอร์สด้วย `tools/build_spiegazione.py data` และ `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`
