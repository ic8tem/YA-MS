[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · **ไทย** · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# การมีส่วนร่วมและการติดต่อ

YA-MS พัฒนาขึ้นได้จากรายงานของผู้ที่ใช้งานโปรแกรมออกอากาศจริง ทุกการแก้ไขจะให้เครดิตแก่แหล่งที่มา

## การติดต่อ

| | |
|---|---|
| ผู้เขียน | Costantino Cerrotta **IC8TEM** |
| อีเมล | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## การรายงานปัญหา

เปิด **issue บน GitHub** หรือส่งอีเมลพร้อมข้อมูลต่อไปนี้:

- ระบบปฏิบัติการและเวอร์ชันของ YA-MS (อยู่ที่แถบชื่อหน้าต่าง)
- locator ทั้งสอง ย่านความถี่ และเวลา UTC
- สิ่งที่คุณคาดหวังและสิ่งที่คุณเห็น (ภาพหน้าจอช่วยได้มาก)
- สำหรับปัญหาเกี่ยวกับเรดาร์ ให้แนบข้อความที่แสดงในแท็บ [ฟลักซ์เรดาร์](Radar-Flux-th)

## สิ่งที่มีประโยชน์เป็นพิเศษ

- **รายงานจากการออกอากาศจริง** ชั่วโมงและเส้นทางที่ประสิทธิภาพหรือพยากรณ์ถูกต้อง – หรือผิดพลาด แบบจำลองนี้เป็นเชิงทดลองและต้องเปรียบเทียบกับ QSO จริงและกับ MCG_MS / MS-Soft
- **การเปรียบเทียบกับ RMOB** ค่าตัวประกอบสถานี K และเลขชี้กำลัง k ที่คุณหาได้จาก [การเปรียบเทียบกับ RMOB](Experimental-Forecasts-th#การเปรียบเทียบกับ-rmob) พร้อมย่านความถี่และสถานีของคุณ
- **ข้อมูลพร้อมแหล่งที่มา** การเคลื่อนของจุดเรเดียนต์ที่ดีกว่า โปรไฟล์กิจกรรม วันที่จุดสูงสุดใหม่ของ IMO (`data/massimi_imo.csv`) ข้อมูลสายอากาศ: โปรดระบุแหล่งที่มาแล้วจะมีการอ้างอิงให้
- **การเปลี่ยนแปลงของกราฟเรดาร์** หากรูปแบบกราฟของ Collm เปลี่ยนไป สำเนาของภาพ (`data/radar/`) จะช่วยในการปรับเทียบการอ่านค่าใหม่

## การแปล

คำแปลของส่วนติดต่อผู้ใช้เป็นไฟล์ข้อความธรรมดาใน **`data/lingue/<code>.txt`** (UTF-8) และ **ทุกคนสามารถแก้ไขได้**:

```
<Italian text><TAB><translation>
```

- หนึ่งรายการต่อหนึ่งบรรทัด บรรทัดที่ขึ้นต้นด้วย `#` เป็นหมายเหตุ
- ในทั้งสองคอลัมน์ อักขระสองตัว `\n` หมายถึงการขึ้นบรรทัดใหม่
- คงตัวยึดตำแหน่ง `{0}`, `{1}`, … ไว้พร้อมรูปแบบของมัน (เช่น `{0:F1}`, `{3:+0;-0}`) โดยเรียงตามลำดับที่ภาษาของคุณต้องการ
- รายการที่ขาดหายหรือว่างเปล่าจะแสดงเป็นภาษาอิตาลี รายชื่อคีย์ทั้งหมดอยู่ที่ `data/lingue/chiavi.txt` (สร้างโดย `tools/estrai_chiavi.py` ห้ามแก้ไข)

แก้ไขไฟล์ในโฟลเดอร์ `data/lingue` ของการติดตั้งของคุณ แล้วเริ่ม YA-MS ใหม่ (หรือสลับภาษา) เพื่อดูผลลัพธ์ เนื่องจากไฟล์เหล่านี้ **จะถูกแทนที่ด้วยเวอร์ชันที่ใหม่กว่าทุกครั้งที่อัปเดต** โปรด **ส่งการแก้ไขของคุณ** มาด้วย – ทางอีเมลหรือเป็น pull request บน GitHub (`data/lingue/`) – เพื่อให้รวมอยู่ในรีลีสถัดไป

วิกินี้มีให้บริการใน 36 ภาษา (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, ไทย, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文, 中文 (繁體)) ยินดีรับการแก้ไขหน้าวิกิเช่นกัน
