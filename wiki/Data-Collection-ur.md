[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · **اردو** · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# ڈیٹا جمع کرنا

*ٹیب: لائیو اور ریئل ٹائم ڈیٹا › ڈیٹا جمع کرنا۔*

[![ڈیٹا جمع کرنا](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## چار ذرائع

یہ ٹیب تین telnet سلسلوں اور PSKReporter کی MQTT فیڈ سے **meteor scatter اسپاٹ** جمع کرتا ہے، ہر ایک اپنے ذیلی ٹیب میں:

| ذیلی ٹیب | پہلے سے طے شدہ | نوٹ |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | اپنی پسند کا کوئی cluster۔ ON0DXK پر VHF بینڈ فلٹر ہوتے ہیں: انہیں `set/filter dxbm/pass 6` (پھر 4، 2…) سے فعال کریں۔ |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY، 7001 = FT8)۔ اسکمر شاذ و نادر ہی MS موڈ ڈی کوڈ کرتے ہیں۔ |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | **PSKReporter** کے اسپاٹ لانے والا DM4X cluster: WSJT-X اور MSHV کے MSK144 ڈی کوڈ یہاں آتے ہیں۔ |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | **MQTT** کے ذریعے PSKReporter کے لائیو اسپاٹ (M0LTE کی سروس): لاگ اِن نہیں، ہر اسپاٹ میں پہلے ہی بھیجنے والے اور وصول کرنے والے اسٹیشن کے لوکیٹر ہوتے ہیں۔ پہلے سے طے شدہ ٹاپکس: 6 m، 4 m، 2 m، 1.25 m، 70 cm پر MSK144 اور 2 m پر FSK441 (`pskr/filter/v2/band/mode/#`)؛ *پہلے سے طے شدہ ٹاپکس* انہیں بحال کرتا ہے۔ |
| **جمع شدہ MS اسپاٹ** | – | قبول شدہ اسپاٹس کا جدول، نئے پہلے۔ |

ہر سلسلے میں ہوسٹ، پورٹ، لاگ اِن کے بعد بھیجی جانے والی کمانڈز، *دوبارہ جوڑیں*، *آغاز پر جوڑیں*، ایک کنسول اور کمانڈ بھیجنے کی ایک لائن ہے۔ اوپر اپنا **لاگ اِن کے لیے کال سائن** لکھیں۔ MQTT ذریعے میں ہوسٹ، پورٹ، ٹاپکس (ہر لائن میں ایک یا `;` سے الگ)، *دوبارہ جوڑیں* اور *آغاز پر جوڑیں* (پہلے سے بند) اور موصول شدہ اسپاٹس والا ایک کنسول ہے؛ اس کے اسپاٹ بھی اسی فلٹر سے گزرتے ہیں۔ ایک پٹی چاروں ذرائع کی حالت دکھاتی ہے (سبز نقطہ = منسلک)۔ زبان یا رنگ سکیم بدلنے پر سیشن کھلے رہتے ہیں۔

## فلٹر (ونڈو کا 40 %)

- **اختیاری مقامی فلٹر:** **27990.0 kHz** سے نیچے کی cluster لائنیں فوراً رد کر دی جاتی ہیں (نہ دکھائی جاتی ہیں، نہ محفوظ ہوتی ہیں)۔
- CW اسپاٹس فوراً رد کر دیے جاتے ہیں (تبصرے میں CW یا WPM، یا 28000-28070 kHz): جب تک ان پر <MS> نہ ہو، یہ کنسول میں نظر نہیں آتے اور محفوظ نہیں ہوتے۔ خانہ بند کیا جا سکتا ہے۔
- **پہلا معیار – MS کی عام فریکوئنسیاں:** 50190–50300، 70100–70400، 144290–144399 kHz۔ ان ونڈوز میں کوئی اسپاٹ موڈ کے نام کے بغیر بھی قبول ہوتا ہے، الا یہ کہ تبصرہ کسی اور پھیلاؤ (propagation) کا اعلان کرے: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`۔ ونڈوز اور ٹیگ قابلِ ترمیم ہیں۔
- **دوسرا معیار – MS موڈ:** ونڈوز سے باہر، یا ان میں سے کسی ٹیگ کے ساتھ، اسپاٹ صرف تب رکھا جاتا ہے جب اس میں **MSK144، FSK441، FSK41، PSK2K، JTMS، JT6M** (صرف MS کے لیے استعمال ہونے والے ڈیجیٹل موڈ) یا **\<MS\>** ہو، بڑے، چھوٹے یا ملے جلے حروف میں۔ الفاظ بند کیے، شامل کیے اور ہٹائے جا سکتے ہیں؛ ہر ایک کا اپنا کاؤنٹر ہے۔
- **بینڈ** 28، 50، 70، 144، 222، 432 MHz؛ چسپاں کی گئی لائن پر **فلٹر کی جانچ**؛ **کاؤنٹر**۔

## لوکیٹر اور محفوظ کرنا

غائب لوکیٹر، یا صرف 4 حروف والے لوکیٹر، **CALL3** آرکائیو سے لیے جاتے ہیں (`data/call3.txt`، JTDX فائل، دس لاکھ سے زیادہ کال سائن)، جو 4 حروف والے لوکیٹر پر ہمیشہ ترجیح رکھتا ہے۔ قبول شدہ اسپاٹ `data/spot_ms` میں محفوظ ہوتے ہیں، ہر دن کی ایک CSV فائل، اور [براہِ راست ٹریفک](Live-Traffic-ur) کے نقشے کو ڈیٹا فراہم کرتے ہیں۔
