[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Ελληνικά](Grid-Square-Map-el) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · **ไทย** · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh) · [中文 (繁體)](Grid-Square-Map-zh-tw)

# แผนที่ช่องกริด

*แท็บ: แผนที่ช่องกริด*

[![แผนที่ช่องกริด](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

ช่องกริด Maidenhead (4 ตัวอักษร) ที่คุณ **ติดต่อได้แล้ว** และ **ยืนยันแล้ว** ซึ่งอ่านจากไฟล์ ADIF ของล็อกของคุณ บนแผนที่ยุโรป – **หนึ่งแท็บย่อยต่อหนึ่งย่านความถี่: 50, 70, 144, 222 และ 432 MHz**

## การควบคุม

| การควบคุม | หน้าที่ |
|---|---|
| **โหลดไฟล์ ADIF...** | อ่านไฟล์ `.adi` / `.adif` ไฟล์ ADIF ใหม่จะ **แทนที่** ข้อมูลเดิม |
| **ล้างหน่วยความจำ** | ลบช่องกริดทั้งหมดที่โหลดจาก ADIF (จะขอการยืนยัน) |
| เมาส์ | **ล้อเมาส์ = ซูม, ลาก = เลื่อน, ชี้เมาส์บนช่องกริด = QSO** (สูงสุดหกสัญญาณเรียกขานพร้อมวันที่ และ *(ยืนยันแล้ว)* เมื่อยืนยันแล้ว) |

หลังจากโหลด สถานะจะแสดงว่า *อ่าน QSO … รายการ, ช่องกริดที่มี QSO … ช่องในย่าน 50-432 MHz, ทิ้ง QSO … รายการ (ย่านอื่นหรือไม่มีช่องกริด)* แผนที่ของแต่ละย่านความถี่มีคำบรรยาย *ติดต่อได้ … ช่องกริด, ยืนยันแล้ว …*

| สี | ความหมาย |
|---|---|
| ส้ม | ติดต่อได้แล้ว |
| เขียว | ยืนยันแล้ว (QSL หรือ LoTW) |

## วิธีอ่านไฟล์ ADIF

- ฟิลด์ที่ใช้: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ข้อกำหนด ADIF)
- ย่านความถี่จาก `BAND` หรือจากความถี่: 50–54 MHz = 6 m, 69.9–71.5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1.25 m, 420–450 MHz = 70 cm
- ช่องกริดจะ **ยืนยันแล้ว** หากมี QSO อย่างน้อยหนึ่งรายการในช่องนั้นที่มี `QSL_RCVD = Y` หรือ `LOTW_QSL_RCVD = Y`
- ช่องกริดจะเก็บไว้ใน `data/adif_quadrati.csv` จนกว่าคุณจะโหลดไฟล์อื่นหรือกด **ล้างหน่วยความจำ**

YA-MS **ไม่ได้** เชื่อมต่อกับ LoTW: ให้ส่งออก ADIF จากโปรแกรมล็อกของคุณ (หรือจาก LoTW) แล้วโหลดที่นี่
