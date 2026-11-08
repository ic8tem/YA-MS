**English** · [Русский](Installation-ru) · [Deutsch](Installation-de) · [日本語](Installation-ja)

# انسٹالیشن

تمام پیکیج **[Releases](https://github.com/ic8tem/YA-MS/releases)** صفحے پر ہیں (نیچے فائلوں کے ناموں میں `x.y.z` ورژن ہے، مثلاً `1.2.0`)۔ کچھ بھی کمپائل کرنے یا الگ سے انسٹال کرنے کی ضرورت نہیں: ہر پیکیج میں .NET 8 رن ٹائم شامل ہے۔

| سسٹم | فائل | کہاں انسٹال ہوتا ہے |
|---|---|---|
| Windows (64-بٹ) | `YA-MS-x.y.z-windows-x64-setup.exe` (انسٹالر) | `C:\YA-MS` |
| Windows (64-بٹ)، پورٹیبل | `YA-MS-x.y.z-windows-x64-portatile.zip` | کوئی بھی فولڈر جس میں آپ لکھ سکیں |
| Windows (32-بٹ، Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` یا `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-بٹ) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5، 400/500 (Raspberry Pi OS 64-بٹ) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-بٹ) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS، Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS، Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**پروگرام اور اس کا `data` فولڈر ہمیشہ ایک ساتھ** YA-MS فولڈر میں رہتے ہیں: تمام ڈیٹا اور ترتیبات وہیں ہیں (نہ AppData، نہ سسٹم فولڈر)۔ دیکھیں [ترتیبات اور ڈیٹا فولڈر](Settings-and-Data-Folder-ur)۔

## Windows

### انسٹالر
1. `YA-MS-x.y.z-windows-x64-setup.exe` ڈاؤن لوڈ کر کے چلائیں۔
2. اگر **SmartScreen** "Windows protected your PC" دکھائے: *More info* → *Run anyway* (پروگرام تجارتی سرٹیفکیٹ سے دستخط شدہ نہیں)۔
3. YA-MS **`C:\YA-MS`** میں انسٹال ہوتا ہے، **ایڈمنسٹریٹر حقوق کے بغیر**، Start مینو میں آئیکن کے ساتھ اور نشان لگانے پر ڈیسک ٹاپ آئیکن بھی۔

### پورٹیبل
`YA-MS-x.y.z-windows-x64-portatile.zip` کو جہاں چاہیں نکالیں (ایسا فولڈر جس میں آپ لکھ سکیں، *Program Files* نہیں) اور `YA-MS.exe` چلائیں۔ پورا فولڈر USB اسٹک یا دوسرے کمپیوٹر پر کاپی کیا جا سکتا ہے۔

## Linux

1. `YA-MS-x.y.z-linux-x64.tar.gz` نکالیں۔
2. نکالے گئے فولڈر سے چلائیں:
   ```sh
   ./installa.sh
   ```
3. اسکرپٹ YA-MS کو **`~/YA-MS`** میں کاپی کرتا ہے (root کی ضرورت نہیں) اور ایپلیکیشن مینو میں **YA-MS** شامل کرتا ہے (زمرہ *HamRadio*)۔ آپ اسے `~/YA-MS/YA-MS` سے بھی چلا سکتے ہیں۔

جاپانی متن کے لیے Noto CJK فونٹ درکار ہو سکتے ہیں: دیکھیں [مسائل کا حل](Troubleshooting-FAQ-ur#linux-جاپانی-متن-خانوں-کی-صورت-میں-دکھائی-دیتا-ہے)۔

## Raspberry Pi

Linux والا طریقہ: `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (یا 32-بٹ Raspberry Pi OS پر `-32bit`) نکالیں اور نکالے گئے فولڈر سے `./installa.sh` چلائیں۔

- آپ کا سسٹم کون سا ہے، یہ جاننے کے لیے ٹرمینل میں `uname -m` لکھیں: `aarch64` → 64-بٹ پیکیج، `armv7l` → 32-بٹ پیکیج۔
- معاون: Raspberry Pi 2 (صرف 32-بٹ)، 3، 4، 5، 400 اور 500، Raspberry Pi OS کے ڈیسک ٹاپ ورژن کے ساتھ۔ **معاون نہیں:** Pi Zero / Zero W اور Pi 1 (ARMv6 پروسیسر، ان پر .NET نہیں چلتا)؛ Pi Zero 2 W 64-بٹ پیکیج کے ساتھ چلتا ہے لیکن 512 MB RAM تنگ ہے۔
- کم از کم 2 GB RAM والا Pi 4 یا 5 تجویز کیا جاتا ہے؛ پہلی بار چلنے میں PC کی نسبت چند سیکنڈ زیادہ لگتے ہیں۔

## macOS

1. درست فائل منتخب کریں: M1/M2/M3/M4 پروسیسروں کے لیے `-mac-apple-silicon.dmg`، Intel Mac کے لیے `-mac-intel.dmg`۔
2. `.dmg` کھولیں، **"Installa YA-MS.command" پر دایاں کلک → Open** کریں اور تصدیق کریں۔
3. اسکرپٹ `YA-MS.app` کو **`~/YA-MS`** میں کاپی کر کے کھول دیتا ہے۔

پروگرام Apple سے دستخط شدہ نہیں، اس لیے پہلی بار macOS تصدیق مانگتا ہے؛ دیکھیں [مسائل کا حل](Troubleshooting-FAQ-ur#macos-نامعلوم-ڈویلپر-کی-وجہ-سے-کھولا-نہیں-جا-سکتا)۔

## پہلی بار چلانا

- **یورپ کا نقشہ** (Natural Earth کی ساحلی لکیریں اور سرحدیں) پہلی بار خودکار طور پر `data/mappa` میں ڈاؤن لوڈ ہوتا ہے: ایک بار انٹرنیٹ کنکشن درکار ہے۔
- **ریڈار ڈیٹا** (Collm، Sodankylä) فوراً ڈاؤن لوڈ ہوتا ہے اور پھر ہر 5 منٹ بعد جانچا جاتا ہے۔
- انٹرفیس آپ کے سسٹم کی زبان میں شروع ہوتا ہے اگر وہ چھ دستیاب زبانوں میں سے ہو، ورنہ اطالوی میں؛ اسے اوپر دائیں جانب بدلیں (دیکھیں [ترتیبات](Settings-and-Data-Folder-ur#زبان))۔

## اپ ڈیٹ کرنا

نیا ورژن **پرانے کے اوپر** انسٹال کریں (وہی انسٹالر، وہی فولڈر)۔ ترتیبات (`config.ini`)، فلکس کے آرکائیو اور نقشہ `data` میں محفوظ رہتے ہیں۔ `data/lingue` کی ترجمہ فائلیں اس وقت بدلی جاتی ہیں جب نئی فائلیں زیادہ تازہ ہوں۔

## سورس سے بنانا (صرف ڈویلپرز کے لیے)

انسٹالر GitHub Actions (`.github/workflows/build.yml`) کے ذریعے `release` برانچ کی ہر تازہ کاری پر بنتے ہیں (ورژن `VERSION` فائل سے لیا جاتا ہے)، جو `vX.Y.Z` ریلیز بھی بناتا ہے۔ مقامی طور پر:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # یا linux-x64، linux-arm64، linux-arm، osx-arm64
```

دستاویزات `tools/build_spiegazione.py data` اور `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` سے دوبارہ بنائی جاتی ہیں۔

اگلا: [آغاز](Getting-Started-ur)۔
