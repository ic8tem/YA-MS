[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · **ไทย** · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# การเก็บข้อมูล

*แท็บ: ข้อมูลสดและตามเวลาจริง › การเก็บข้อมูล*

[![การเก็บข้อมูล](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## สตรีมคลัสเตอร์สามสาย

แท็บนี้เก็บรวบรวม **สปอต meteor scatter** จากสตรีม telnet สามสาย แต่ละสายอยู่ในแท็บย่อยของตัวเอง:

| แท็บย่อย | ค่าเริ่มต้น | หมายเหตุ |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | คลัสเตอร์ที่คุณเลือก บน ON0DXK ย่านความถี่ VHF ถูกกรองไว้: เปิดใช้ด้วย `set/filter dxbm/pass 6` (แล้วตามด้วย 4, 2…) |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8) สคิมเมอร์ (skimmer) แทบไม่ถอดรหัสโหมด MS |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | คลัสเตอร์ DM4X ที่ส่งต่อสปอตของ **PSKReporter**: ผลการถอดรหัส MSK144 ของ WSJT-X และ MSHV จะมาถึงที่นี่ |
| **สปอต MS ที่เก็บรวบรวม** | – | ตารางของสปอตที่ได้รับการยอมรับ ใหม่สุดก่อน |

แต่ละสตรีมมีโฮสต์ พอร์ต คำสั่งที่ส่งหลังเข้าสู่ระบบ *เชื่อมต่อใหม่* *เชื่อมต่อเมื่อเริ่มโปรแกรม* คอนโซล และบรรทัดสำหรับส่งคำสั่ง เขียน **สัญญาณเรียกขานสำหรับเข้าสู่ระบบ** ของคุณที่ด้านบน แถบหนึ่งแสดงสถานะของทั้งสามเซสชัน (จุดสีเขียว = เชื่อมต่อแล้ว) เซสชันจะยังคงเปิดอยู่เมื่อคุณเปลี่ยนภาษาหรือชุดสี

## ตัวกรอง (40 % ของหน้าต่าง)

- **ตัวกรองภายในเครื่องแบบเลือกได้:** บรรทัดจากคลัสเตอร์ที่ต่ำกว่า **27990.0 kHz** จะถูกทิ้งทันที (ไม่แสดง ไม่จัดเก็บ)
- **เกณฑ์ที่ 1 – ความถี่ทั่วไปของ MS:** 50190–50300, 70100–70400, 144290–144399 kHz สปอตในหน้าต่างความถี่เหล่านี้จะได้รับการยอมรับแม้ไม่มีชื่อโหมด เว้นแต่หมายเหตุระบุการแพร่กระจายแบบอื่น: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>` หน้าต่างความถี่และแท็กแก้ไขได้
- **เกณฑ์ที่ 2 – โหมด MS:** นอกหน้าต่างความถี่ หรือเมื่อมีแท็กใดแท็กหนึ่งข้างต้น สปอตจะถูกเก็บไว้ก็ต่อเมื่อมี **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (โหมดดิจิทัลที่ใช้เฉพาะกับ MS) หรือ **\<MS\>** ไม่ว่าจะเป็นตัวพิมพ์ใหญ่ ตัวพิมพ์เล็ก หรือผสมกัน คำต่าง ๆ ปิดใช้ เพิ่ม และลบได้ แต่ละคำมีตัวนับของตัวเอง
- **ย่านความถี่** 28, 50, 70, 144, 222, 432 MHz; **ทดสอบตัวกรอง** กับบรรทัดที่วางลงไป; **ตัวนับ**

## โลเคเตอร์และการจัดเก็บ

โลเคเตอร์ที่ขาดหาย หรือโลเคเตอร์ที่มีเพียง 4 ตัวอักษร จะนำมาจากคลังข้อมูล **CALL3** (`data/call3.txt` ไฟล์ของ JTDX มีสัญญาณเรียกขานมากกว่าหนึ่งล้านรายการ) ซึ่งมีลำดับความสำคัญเหนือโลเคเตอร์ 4 ตัวอักษรเสมอ สปอตที่ได้รับการยอมรับจะถูกบันทึกใน `data/spot_ms` หนึ่งไฟล์ CSV ต่อวัน และใช้ป้อนแผนที่ [ทราฟฟิกสด](Live-Traffic-th)
