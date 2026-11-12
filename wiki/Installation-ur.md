[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · **اردو** · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# انسٹالیشن

تمام پیکیج **[Releases](https://github.com/ic8tem/YA-MS/releases)** صفحے پر ہیں (نیچے فائلوں کے ناموں میں `x.y.z` ورژن ہے، مثلاً `1.2.0`)۔ کچھ بھی کمپائل کرنے یا الگ سے انسٹال کرنے کی ضرورت نہیں: ہر پیکیج میں .NET 8 رن ٹائم شامل ہے۔

| سسٹم | فائل | کہاں انسٹال ہوتا ہے |
|---|---|---|
| Windows (64-بٹ) | `YA-MS-x.y.z-windows-x64-setup.exe` (انسٹالر) | `C:\YA-MS` |
| Windows (64-بٹ)، پورٹیبل | `YA-MS-x.y.z-windows-x64-portatile.zip` | کوئی بھی فولڈر جس میں آپ لکھ سکیں |
| Windows (32-بٹ، Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` یا `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| ARM پر Windows (64 بٹ، Snapdragon والے PC) | `YA-MS-x.y.z-windows-arm64-setup.exe` یا `...-windows-arm64-portatile.zip` | `C:\YA-MS` |
| Linux (64-بٹ): Debian، Ubuntu، Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (پہلے آغاز پر وہاں کاپی ہو جاتا ہے) |
| Linux (64-بٹ)، کوئی بھی ڈسٹری بیوشن | `YA-MS-x.y.z-linux-x64.tar.gz` (پورٹیبل یا `./installa.sh` کے ساتھ) | `~/YA-MS` یا کوئی بھی فولڈر |
| Linux (64 بٹ): Fedora، openSUSE | `ya-ms-x.y.z.x86_64.rpm` (x86_64), `ya-ms-x.y.z.aarch64.rpm` (ARM64), `ya-ms-x.y.z.armv7hl.rpm` (ARM 32) | `~/YA-MS` (پہلے آغاز پر وہاں کاپی ہو جاتا ہے) |
| Arch, Manjaro, EndeavourOS, Arch Linux ARM | `ya-ms-x.y.z-1-x86_64.pkg.tar.zst`, `ya-ms-x.y.z-1-aarch64.pkg.tar.zst` | `~/YA-MS` (پہلے آغاز پر وہاں کاپی ہو جاتا ہے) |
| Slackware64, Slackware ARM64 | `ya-ms-x.y.z-x86_64-1_ic8tem.txz`, `ya-ms-x.y.z-aarch64-1_ic8tem.txz` | `~/YA-MS` (پہلے آغاز پر وہاں کاپی ہو جاتا ہے) |
| AppImage (x86_64, aarch64) | `YA-MS-x.y.z-x86_64.AppImage`, `YA-MS-x.y.z-aarch64.AppImage` | `~/YA-MS` (پہلے آغاز پر وہاں کاپی ہو جاتا ہے) |
| Alpine Linux (musl) | `YA-MS-x.y.z-alpine-x64.tar.gz`, `YA-MS-x.y.z-alpine-arm64.tar.gz` | `~/YA-MS` یا کوئی بھی فولڈر |
| Raspberry Pi 3/4/5، 400/500 (Raspberry Pi OS 64-بٹ) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-بٹ) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi، Debian پیکیج | `ya-ms_x.y.z_arm64.deb` (64-بٹ) یا `ya-ms_x.y.z_armhf.deb` (32-بٹ) | `~/YA-MS` (پہلے آغاز پر وہاں کاپی ہو جاتا ہے) |
| Linux ARM 64 بٹ، کوئی بھی ڈسٹری بیوشن (مثلاً Slackware ARM64) | `YA-MS-x.y.z-linux-arm64.tar.gz` (پورٹیبل یا `./installa.sh` کے ساتھ) | `~/YA-MS` یا کوئی بھی فولڈر |
| Linux armv7l (ARM 32 بٹ)، کوئی بھی ڈسٹری بیوشن | `YA-MS-x.y.z-linux-armv7l.tar.gz` (پورٹیبل یا `./installa.sh` کے ساتھ) | `~/YA-MS` یا کوئی بھی فولڈر |
| macOS، Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS، Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS، صرف ایپلیکیشن | `YA-MS-x.y.z-mac-apple-silicon-app.zip` یا `...-mac-intel-app.zip` | وہ فولڈر جس میں آپ `YA-MS.app` نکالیں |

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

### Debian پیکیج (.deb)
Debian، Ubuntu، Mint اور Raspberry Pi OS پر آپ اس کے بجائے `ya-ms_x.y.z_amd64.deb` انسٹال کر سکتے ہیں (Raspberry Pi پر `_arm64.deb` / `_armhf.deb`):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
پیکیج پروگرام کو `/opt/ya-ms` میں رکھتا ہے اور مینو میں **YA-MS** شامل کرتا ہے۔ پہلے آغاز پر (اور ہر نئے ورژن کے بعد) یہ خود کو **`~/YA-MS`** میں کاپی کرتا ہے اور وہیں سے چلتا ہے، تاکہ `data` فولڈر پروگرام کے ساتھ رہے اور آپ کی ترتیبات محفوظ رہیں۔

### پورٹیبل
`.tar.gz` انسٹال کیے بغیر بھی کام کرتا ہے: اسے کسی بھی ایسی جگہ نکالیں جہاں آپ لکھ سکیں اور اسی فولڈر سے `./YA-MS` چلائیں۔

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

متبادل کے طور پر، `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` میں صرف `YA-MS.app` ہوتا ہے: اسے اپنی پسند کے کسی فولڈر میں نکالیں (جس میں آپ لکھ سکیں)؛ `data` فولڈر `YA-MS.app` کے ساتھ بن جاتا ہے۔ پہلی بار: دایاں کلک → **Open**۔

پروگرام Apple سے دستخط شدہ نہیں، اس لیے پہلی بار macOS تصدیق مانگتا ہے؛ دیکھیں [مسائل کا حل](Troubleshooting-FAQ-ur#macos-نامعلوم-ڈویلپر-کی-وجہ-سے-کھولا-نہیں-جا-سکتا)۔

## پہلی بار چلانا

- **یورپ کا نقشہ** (Natural Earth کی ساحلی لکیریں اور سرحدیں) پہلی بار خودکار طور پر `data/mappa` میں ڈاؤن لوڈ ہوتا ہے: ایک بار انٹرنیٹ کنکشن درکار ہے۔
- **ریڈار ڈیٹا** (Collm، Sodankylä) فوراً ڈاؤن لوڈ ہوتا ہے اور پھر ہر 5 منٹ بعد جانچا جاتا ہے۔
- انٹرفیس آپ کے سسٹم کی زبان میں شروع ہوتا ہے اگر وہ 36 دستیاب زبانوں میں سے ہو، ورنہ اطالوی میں؛ اسے اوپر دائیں جانب بدلیں (دیکھیں [ترتیبات](Settings-and-Data-Folder-ur#زبان))۔

## اپ ڈیٹ کرنا

نیا ورژن **پرانے کے اوپر** انسٹال کریں (وہی انسٹالر، وہی فولڈر)۔ ترتیبات (`config.ini`)، فلکس کے آرکائیو اور نقشہ `data` میں محفوظ رہتے ہیں۔ `data/lingue` کی ترجمہ فائلیں اس وقت بدلی جاتی ہیں جب نئی فائلیں زیادہ تازہ ہوں۔

**1.8.0 سے YA-MS خود کو خود اپ ڈیٹ کرتا ہے۔** شروع ہونے پر، دن میں ایک بار، یہ GitHub پر دیکھتا ہے کہ نیا ورژن ہے یا نہیں اور اسے پیش کرتا ہے؛ نیچے کی پٹی کا بٹن **اپ ڈیٹس** ہاتھ سے چیک کرتا ہے۔ *ابھی اپ ڈیٹ کریں* آپ کے سسٹم کا پورٹیبل پیکیج ڈاؤن لوڈ کرتا ہے، پروگرام کی فائلیں بدلتا ہے، `data` فولڈر رکھتا ہے (بدلنے والی پروگرام فائلیں پہلے `data/backup/v<پرانا ورژن>` میں کاپی ہوتی ہیں) اور دوبارہ شروع ہوتا ہے؛ پروگرام کے فولڈر میں لکھنا ممکن ہونا چاہیے۔ اگر شروع ہونے پر پروگرام کی فائلیں غائب ہوں (`data` یا `doc` میں) تو ایک ونڈو ان کی فہرست دکھاتی ہے اور انہیں GitHub سے دوبارہ ڈاؤن لوڈ کرنے کی پیشکش کرتی ہے۔ نئے ورژن تلاش نہ کرنے کے لیے `config.ini` میں `controlla_aggiornamenti=0` لکھیں۔

## سورس سے بنانا (صرف ڈویلپرز کے لیے)

انسٹالر GitHub Actions (`.github/workflows/build.yml`) کے ذریعے `release` برانچ کی ہر تازہ کاری پر بنتے ہیں (ورژن `VERSION` فائل سے لیا جاتا ہے)، جو `vX.Y.Z` ریلیز بھی بناتا ہے۔ مقامی طور پر:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # یا linux-x64، linux-arm64، linux-arm، osx-arm64
```

دستاویزات (تمام زبانوں میں) `tools/build_documenti.sh` سے دوبارہ بنائی جاتی ہیں۔

اگلا: [آغاز](Getting-Started-ur)۔
