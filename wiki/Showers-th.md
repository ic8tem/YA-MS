[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-BR) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · **ไทย** · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-TW)

# ฝนดาวตก

*แท็บ: ฝนดาวตก*

[![Showers](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

แคตตาล็อกฝนดาวตกที่ใช้ในการคำนวณทั้งหมด: **ฝนดาวตก 45 กลุ่ม** จาก **IMO Meteor Shower Calendar 2026 และ 2027** (ตารางที่ 5 และ 7) บวกกับ **Antihelion Source** (ตารางที่ 6) แต่ละกลุ่มพร้อม **จุดสูงสุดครั้งถัดไป**

## คอลัมน์

| คอลัมน์ | ความหมาย |
|---|---|
| รหัส | รหัสของ IMO (QUA, PER, GEM, …) |
| ฝนดาวตก | ชื่อ |
| ช่วงกิจกรรม | ช่วงเวลาที่มีกิจกรรม (วัน/เดือน – วัน/เดือน) |
| λ max | ลองจิจูดสุริยะของจุดสูงสุด (J2000) จาก IMO |
| **ค่าสูงสุดครั้งถัดไป (UTC)** | วันที่และเวลาของจุดสูงสุดครั้งถัดไป (ดูด้านล่าง) |
| **แหล่งข้อมูลของค่าสูงสุด** | *IMO 2026* / *IMO 2027* = วันที่และเวลาที่ IMO เผยแพร่; *IMO 2026 (วัน)* = IMO ให้เพียงวัน เวลาที่แสดงเป็นค่าที่คำนวณ (*~hh:mm คำนวณ*); *คำนวณจาก λ* = ไม่มีค่าจาก IMO สำหรับปีนั้น |
| R.A., Dec. | จุดเรเดียนต์ ณ จุดสูงสุด (*เคลื่อนที่* สำหรับ Antihelion Source) |
| v km/s, r | ความเร็วเทียบกับโลกและดัชนีประชากร |
| ZHR | ZHR ที่จุดสูงสุด (*ไม่คงที่* = แปรผัน) |
| ประเภท | *มองเห็นด้วยตา* หรือ *วิทยุ กลางวัน* |

ฝนดาวตกที่ **มีกิจกรรมวันนี้ (UTC)** จะถูกเน้นด้วยพื้นสีเหลืองจาง ๆ และตัวหนา

## จุดสูงสุดครั้งถัดไป

โปรแกรมแสดงจุดสูงสุด **ครั้งถัดไป** เสมอ เมื่อ IMO เผยแพร่ปฏิทินของปีนั้นแล้ว โปรแกรมจะใช้ **วันที่และเวลาของ IMO** จาก `data/massimi_imo.csv` (มีปี 2026 และ 2027 อยู่แล้ว) มิฉะนั้นจะคำนวณขณะที่ดวงอาทิตย์ไปถึงลองจิจูดสุริยะของจุดสูงสุด (Meeus, *Astronomical Algorithms*, บทที่ 25 แก้ด้วยวิธีของนิวตัน)

**การตรวจสอบ:** การคำนวณตรงกับปฏิทินของ IMO ปี 2026 และ 2027 ภายในไม่กี่นาทีในกรณีที่ IMO ให้เวลาไว้ (เช่น Quadrantids 3/1/2026 21:13 เทียบกับ 21:00; Geminids 14/12/2027 19:51 เทียบกับ 20:00) ข้อยกเว้น: Daytime kappa Leonids 2026 ช้าไปหนึ่งวัน (26/9 แทน 25/9) และเวลาของ eta Aquariids 2027 (15:10 เทียบกับ 09:00 ของ IMO) – ในกรณีเหล่านี้จะใช้ค่าของ IMO

**การเพิ่มปี:** เมื่อ IMO เผยแพร่ปฏิทินใหม่ ให้เพิ่มแถวลงใน `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm` เว้นเวลาว่างไว้หาก IMO ให้เพียงวัน) จนกว่าจะเพิ่ม จุดสูงสุดจะเป็นค่าที่คำนวณ

## ฝนดาวตกขนาดเล็กและฝนดาวตกกลางวัน

แคตตาล็อกรวม **ฝนดาวตกขนาดเล็ก** ในรายการของ IMO – เช่น October Camelopardalids (OCT, ZHR 5 มีกิจกรรม 5–6 ตุลาคม) Andromedids และ gamma Ursae Minorids – และ **ฝนดาวตกกลางวันทางวิทยุ** ช่วงเมษายน–ตุลาคม (Daytime April Piscids, Daytime Arietids, Daytime zeta Perseids, Daytime beta Taurids, Daytime kappa Leonids, Daytime Sextantids, …) แม้มี ZHR ต่ำ ก็มีส่วนร่วมใน [ดัชนีเส้นทาง](Efficiency-Calculation-th#แบบจำลอง) และ [Hot ที่แนะนำ](Sky-View-th#hot-ที่แนะนำ) สำหรับฝนดาวตกกลางวันทางวิทยุ IMO ไม่ได้ให้ ZHR: ในกรณีที่ไม่มี โปรแกรมจะใช้ค่าทำงานเป็น 5

## โปรไฟล์กิจกรรมและการเคลื่อนของจุดเรเดียนต์

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

ZHR_max, α0, δ0 และ λ_max มาจากปฏิทินของ IMO ส่วนความชัน B (ต่างกันก่อนและหลังจุดสูงสุด) และการเคลื่อนรายวัน dα/dλ, dδ/dλ เป็น **ค่าที่ใช้ทำงาน** ที่เขียนไว้ใน `data/sciami.csv` (ยังไม่ได้ป้อนตารางการเคลื่อนของ IMO) *คู่มือ สมการ 9 และ 13* ตำแหน่งของ Antihelion Source ประมาณค่าในช่วงแบบเชิงเส้นระหว่างวันที่ในตารางที่ 6 ของ IMO (`data/ant_radiante.csv`; มีกิจกรรม 10 ธันวาคม – 20 กันยายน, ZHR ประมาณ 4)

## การแก้ไขแคตตาล็อก

`data/sciami.csv` เป็นไฟล์ข้อความธรรมดา (ตัวคั่น `;`) ที่คุณแก้ไขได้: รหัส ชื่อ วันเริ่มและวันสิ้นสุด (MM-DD) λ max, R.A., Dec. การเคลื่อน v, r, ZHR, B ก่อน/หลัง ประเภท (V มองเห็นด้วยตา, R วิทยุกลางวัน) หากบรรทัดใดผิด โปรแกรมจะแสดงข้อความตอนเริ่มต้นและข้ามบรรทัดนั้นไป

แหล่งอ้างอิง: International Meteor Organization – Meteor Shower Calendar 2026 และ 2027, [www.imo.net](https://www.imo.net) (ตารางที่ 5, 6 และ 7); Rossano IZ5TEK (scattertek)
