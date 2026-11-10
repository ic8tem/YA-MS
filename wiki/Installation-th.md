[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · **ไทย** · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# การติดตั้ง

แพ็กเกจทั้งหมดอยู่ในหน้า **[Releases](https://github.com/ic8tem/YA-MS/releases)** (ในชื่อไฟล์ด้านล่าง `x.y.z` คือเวอร์ชัน เช่น `1.2.0`) ไม่ต้องคอมไพล์และไม่ต้องติดตั้งสิ่งอื่นใดเพิ่ม: แต่ละแพ็กเกจมี .NET 8 runtime อยู่ในตัว

| ระบบ | ไฟล์ | ติดตั้งลงใน |
|---|---|---|
| Windows (64 บิต) | `YA-MS-x.y.z-windows-x64-setup.exe` (ตัวติดตั้ง) | `C:\YA-MS` |
| Windows (64 บิต) แบบพกพา | `YA-MS-x.y.z-windows-x64-portatile.zip` | โฟลเดอร์ใดก็ได้ที่คุณเขียนได้ |
| Windows (32 บิต, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` หรือ `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 บิต) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 บิต) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 บิต) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**โปรแกรมและโฟลเดอร์ `data` ของมันจะอยู่ด้วยกันเสมอ** ในโฟลเดอร์ YA-MS: ข้อมูลและการตั้งค่าทั้งหมดอยู่ที่นั่น (ไม่มี AppData ไม่มีโฟลเดอร์ระบบ) ดู [การตั้งค่าและโฟลเดอร์ข้อมูล](Settings-and-Data-Folder-th)

## Windows

### ตัวติดตั้ง
1. ดาวน์โหลด `YA-MS-x.y.z-windows-x64-setup.exe` แล้วเรียกใช้
2. หาก **SmartScreen** แสดง "Windows protected your PC": *More info* → *Run anyway* (โปรแกรมไม่ได้ลงนามด้วยใบรับรองเชิงพาณิชย์)
3. YA-MS จะถูกติดตั้งลงใน **`C:\YA-MS`** **โดยไม่ต้องใช้สิทธิ์ผู้ดูแลระบบ** พร้อมไอคอนในเมนู Start และไอคอนบนเดสก์ท็อปหากคุณเลือกไว้

### แบบพกพา
แตกไฟล์ `YA-MS-x.y.z-windows-x64-portatile.zip` ไว้ที่ใดก็ได้ตามต้องการ (โฟลเดอร์ที่คุณเขียนได้ ไม่ใช่ *Program Files*) แล้วเรียกใช้ `YA-MS.exe` คุณสามารถคัดลอกทั้งโฟลเดอร์ไปยังแฟลชไดรฟ์ USB หรือคอมพิวเตอร์เครื่องอื่นได้

## Linux

1. แตกไฟล์ `YA-MS-x.y.z-linux-x64.tar.gz`
2. จากโฟลเดอร์ที่แตกออกมา ให้รัน:
   ```sh
   ./installa.sh
   ```
3. สคริปต์จะคัดลอก YA-MS ไปยัง **`~/YA-MS`** (ไม่ต้องใช้ root) และเพิ่ม **YA-MS** ลงในเมนูแอปพลิเคชัน (หมวด *HamRadio*) คุณยังสามารถเริ่มโปรแกรมด้วย `~/YA-MS/YA-MS` ได้ด้วย

สำหรับข้อความภาษาญี่ปุ่น คุณอาจต้องใช้ฟอนต์ Noto CJK: ดู [การแก้ไขปัญหา](Troubleshooting-FAQ-th#linux-ข้อความภาษาญี่ปุ่นแสดงเป็นกล่องสี่เหลี่ยม)

## Raspberry Pi

ขั้นตอนเหมือนกับ Linux: แตกไฟล์ `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (หรือ `-32bit` บน Raspberry Pi OS 32 บิต) แล้วรัน `./installa.sh` จากโฟลเดอร์ที่แตกออกมา

- หากต้องการดูว่าคุณใช้ระบบใด ให้พิมพ์ `uname -m` ในเทอร์มินัล: `aarch64` → แพ็กเกจ 64 บิต, `armv7l` → แพ็กเกจ 32 บิต
- รองรับ: Raspberry Pi 2 (เฉพาะ 32 บิต), 3, 4, 5, 400 และ 500 ที่ใช้ Raspberry Pi OS รุ่นเดสก์ท็อป **ไม่รองรับ:** Pi Zero / Zero W และ Pi 1 (หน่วยประมวลผล ARMv6 ซึ่ง .NET ทำงานไม่ได้) ส่วน Pi Zero 2 W ใช้กับแพ็กเกจ 64 บิตได้ แต่ RAM 512 MB ค่อนข้างตึง
- แนะนำ Pi 4 หรือ 5 ที่มี RAM อย่างน้อย 2 GB การเริ่มโปรแกรมครั้งแรกจะใช้เวลานานกว่าบน PC ไม่กี่วินาที

## macOS

1. เลือกไฟล์ให้ถูกต้อง: `-mac-apple-silicon.dmg` สำหรับหน่วยประมวลผล M1/M2/M3/M4, `-mac-intel.dmg` สำหรับ Mac ที่ใช้ Intel
2. เปิด `.dmg` แล้ว **คลิกขวาที่ "Installa YA-MS.command" → Open** และยืนยัน
3. สคริปต์จะคัดลอก `YA-MS.app` ไปยัง **`~/YA-MS`** แล้วเปิดโปรแกรม

โปรแกรมไม่ได้ลงนามโดย Apple ดังนั้นในครั้งแรก macOS จะขอการยืนยัน ดู [การแก้ไขปัญหา](Troubleshooting-FAQ-th#macos-ไม่สามารถเปิดได้เพราะมาจากนักพัฒนาที่ไม่ระบุตัวตน)

## การเริ่มโปรแกรมครั้งแรก

- **แผนที่ยุโรป** (แนวชายฝั่งและเส้นพรมแดนจาก Natural Earth) จะถูกดาวน์โหลดลงใน `data/mappa` โดยอัตโนมัติในครั้งแรก: ต้องเชื่อมต่ออินเทอร์เน็ตหนึ่งครั้ง
- **ข้อมูลเรดาร์** (Collm, Sodankylä) จะถูกดาวน์โหลดทันที แล้วตรวจสอบทุก 5 นาที
- อินเทอร์เฟซจะเริ่มในภาษาของระบบของคุณ หากเป็นหนึ่งใน 36 ภาษาที่มีให้ มิฉะนั้นจะเป็นภาษาอิตาลี เปลี่ยนได้ที่มุมขวาบน (ดู [การตั้งค่า](Settings-and-Data-Folder-th#ภาษา))

## การอัปเดต

ติดตั้งเวอร์ชันใหม่ **ทับเวอร์ชันเก่า** (ตัวติดตั้งเดียวกัน โฟลเดอร์เดียวกัน) การตั้งค่า (`config.ini`) คลังข้อมูลฟลักซ์ และแผนที่ยังคงอยู่ใน `data` ไฟล์คำแปลใน `data/lingue` จะถูกแทนที่เมื่อไฟล์ใหม่ใหม่กว่า

## การสร้างจากซอร์สโค้ด (สำหรับนักพัฒนาเท่านั้น)

ตัวติดตั้งสร้างโดย GitHub Actions (`.github/workflows/build.yml`) ทุกครั้งที่มีการอัปเดตแบรนช์ `release` (เวอร์ชันนำมาจากไฟล์ `VERSION`) ซึ่งจะสร้างรีลีส `vX.Y.Z` ด้วย สำหรับการสร้างในเครื่อง:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

เอกสารสร้างใหม่ได้ด้วย `tools/build_spiegazione.py data` และ `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`

ถัดไป: [เริ่มต้นใช้งาน](Getting-Started-th)
