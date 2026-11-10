[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-BR) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Ελληνικά](Grid-Square-Map-el) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · **اردو** · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [ไทย](Grid-Square-Map-th) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh) · [中文 (繁體)](Grid-Square-Map-zh-TW)

# مربعوں کا نقشہ

*ٹیب: مربعوں کا نقشہ۔*

[![مربعوں کا نقشہ](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

وہ Maidenhead مربعے (4 حروف) جن سے آپ کا **رابطہ ہوا** اور جو **تصدیق شدہ** ہیں، آپ کے لاگ کی ADIF فائل سے پڑھ کر، یورپ کے نقشے پر – **ہر بینڈ کا ایک ذیلی ٹیب: 50، 70، 144، 222 اور 432 MHz**۔

## کنٹرول

| کنٹرول | کیا کرتا ہے |
|---|---|
| **ADIF فائل لوڈ کریں...** | ایک `.adi` / `.adif` فائل پڑھتا ہے۔ نئی ADIF پچھلے ڈیٹا کی **جگہ لے لیتی ہے**۔ |
| **میموری صاف کریں** | ADIF سے لوڈ کیے گئے تمام مربعے حذف کرتا ہے (تصدیق مانگتا ہے)۔ |
| ماؤس | **پہیہ = زوم، گھسیٹنا = سرکانا، مربع پر ماؤس = QSO** (تاریخ کے ساتھ زیادہ سے زیادہ چھ کال سائن، تصدیق شدہ ہو تو *(تصدیق شدہ)*) |

لوڈ کرنے کے بعد اسٹیٹس دکھاتا ہے *… QSO پڑھے گئے، 50-432 MHz بینڈوں میں … QSO مربعے، … QSO مسترد (دیگر بینڈ یا بغیر مربع)*۔ ہر بینڈ کے نقشے کی عبارت ہے *… مربعوں سے رابطہ، … تصدیق شدہ*۔

| رنگ | مطلب |
|---|---|
| نارنجی | رابطہ شدہ |
| سبز | تصدیق شدہ (QSL یا LoTW) |

## ADIF کیسے پڑھی جاتی ہے

- استعمال ہونے والے خانے: `CALL`، `GRIDSQUARE`، `VUCC_GRIDS`، `BAND`، `FREQ`، `QSO_DATE`، `QSL_RCVD`، `LOTW_QSL_RCVD` (ADIF تفصیل)۔
- بینڈ `BAND` سے، یا فریکوئنسی سے: 50–54 MHz = 6 m، 69.9–71.5 MHz = 4 m، 144–148 MHz = 2 m، 219–225 MHz = 1.25 m، 420–450 MHz = 70 cm۔
- کوئی مربع **تصدیق شدہ** ہے اگر اس کے کم از کم ایک QSO میں `QSL_RCVD = Y` یا `LOTW_QSL_RCVD = Y` ہو۔
- مربعے `data/adif_quadrati.csv` میں رکھے جاتے ہیں جب تک آپ دوسری فائل لوڈ نہ کریں یا **میموری صاف کریں** نہ دبائیں۔

YA-MS، LoTW سے **رابطہ نہیں کرتا**: اپنے لاگنگ پروگرام (یا LoTW) سے ADIF برآمد کریں اور یہاں لوڈ کریں۔
