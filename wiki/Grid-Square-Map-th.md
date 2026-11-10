**English** · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# แผนที่ช่องกริด

*แท็บ: แผนที่ช่องกริด*

[![Grid square map](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

ช่องกริด Maidenhead (4 ตัวอักษร) ที่คุณ **ติดต่อได้** และ **ได้รับการยืนยัน** อ่านจากไฟล์ ADIF ของล็อกของคุณ แสดงบนแผนที่ยุโรป – **หนึ่งแท็บย่อยต่อหนึ่งย่านความถี่: 50, 70, 144, 222 และ 432 MHz**

## ตัวควบคุม

| ตัวควบคุม | หน้าที่ |
|---|---|
| **โหลดไฟล์ ADIF...** | อ่านไฟล์ `.adi` / `.adif` ไฟล์ ADIF ใหม่จะ **แทนที่** ข้อมูลเดิม |
| **ล้างหน่วยความจำ** | ลบช่องกริดทั้งหมดที่โหลดจาก ADIF (มีการขอให้ยืนยัน) |
| เมาส์ | **ล้อเลื่อน = ซูม, ลาก = เลื่อนแผนที่, ชี้เมาส์บนช่องกริด = QSO** (สูงสุดหกสัญญาณเรียกขานพร้อมวันที่ และ *(ยืนยันแล้ว)* เมื่อได้รับการยืนยัน) |

หลังโหลด สถานะจะแสดง *อ่าน QSO … รายการ, ช่องกริดของ QSO ในย่านความถี่ 50-432 MHz … ช่องกริด, ทิ้ง QSO … รายการ (ย่านความถี่อื่นหรือไม่มีช่องกริด)* แผนที่ของแต่ละย่านความถี่มีคำบรรยาย *ติดต่อได้ … ช่องกริด, ยืนยันแล้ว …*

| สี | ความหมาย |
|---|---|
| ส้ม | ติดต่อได้ |
| เขียว | ยืนยันแล้ว (QSL หรือ LoTW) |

## วิธีอ่านไฟล์ ADIF

- ฟิลด์ที่ใช้: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ข้อกำหนดของ ADIF)
- ย่านความถี่จาก `BAND` หรือจากความถี่: 50–54 MHz = 6 m, 69.9–71.5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1.25 m, 420–450 MHz = 70 cm
- ช่องกริดหนึ่ง **ได้รับการยืนยัน** หากมี QSO อย่างน้อยหนึ่งรายการในช่องกริดนั้นที่มี `QSL_RCVD = Y` หรือ `LOTW_QSL_RCVD = Y`
- ช่องกริดจะถูกเก็บไว้ใน `data/adif_quadrati.csv` จนกว่าคุณจะโหลดไฟล์อื่นหรือกด **ล้างหน่วยความจำ**

YA-MS **ไม่ได้** เชื่อมต่อกับ LoTW: ให้ส่งออก ADIF จากโปรแกรมล็อกของคุณ (หรือจาก LoTW) แล้วโหลดที่นี่
