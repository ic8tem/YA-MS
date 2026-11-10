[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · **اردو** · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [ไทย](Efficiency-Explanation-th) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# کارکردگی - وضاحت

*ٹیب: تکنیکی دستاویزات › کارکردگی - وضاحت۔*

[![کارکردگی - وضاحت](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

ایک تکنیکی دستاویز، *"Come YA-MS calcola l'efficienza di uno sciame"* (YA-MS کسی شہابی بارش کی کارکردگی کا حساب کیسے کرتا ہے)، جو پروگرام کے اندر ایک ہلکے صفحے کی صورت میں دکھائی جاتی ہے۔ یہ **قدم بہ قدم** وضاحت کرتی ہے کہ کارکردگی کیسے حاصل ہوتی ہے، اور ہر قدم کے لیے بتاتی ہے کہ **وہ کہاں سے آیا**۔ دستاویز فی الحال **اطالوی زبان میں** ہے؛ یہ وکی اس کا مواد اردو میں [کارکردگی کا حساب](Efficiency-Calculation-ur#ماڈل) اور [جیومیٹری اور راستے کا نقصان](Geometry-and-Path-Loss-ur) میں دیتی ہے۔

## لیبل

ہر قدم پر ایک رنگین لیبل ہوتا ہے:

| لیبل | رنگ | مطلب |
|---|---|---|
| **FONTE** (ماخذ) | نیلا | قدم کسی حوالہ شدہ ماخذ سے لیا گیا ہے؛ قوسین میں نمبر آخر کی فہرست کا حوالہ ہے |
| **RILIEVO** (جانچ) | سبز | پروگرام اور ذرائع کے درمیان موازنہ، نتیجے کے ساتھ |
| **SCELTA** (انتخاب) | نارنجی | پروگرام کا ایک انتخاب، کسی ماخذ سے نہیں لیا گیا: بینڈ پر تجربے سے جانچنا ہے |

## ابواب

| باب | مواد |
|---|---|
| 1. تعارف | مقصد، لیبل، کارکردگی سے کیا مراد ہے (OH5IY، MCG_MS؛ YA-MS حقیقی راستہ استعمال کرتا ہے) |
| 2. انعکاس کہاں ہوتا ہے: E تہہ | 80–120 km پر لکیریں؛ لکیروں کی اونچائی = Collm ہسٹوگرام کا موڈ (جانچ: 5/11/2026 کو 89.5 km) |
| 3. راستے کی جیومیٹری | زمین اور وسطی نقطہ؛ اینٹینا کا ارتفاع (مضمون کا فارمولا)؛ مشترکہ زون اور اس کی حدود؛ Hot A / Hot B؛ اینٹینا لوب (DL6WU، Kraus، W4RNL) |
| 4. شہابی بارش کا ریڈیئنٹ | ریڈیئنٹ کا مقام (IMO 2026/2027)، عروج کی تاریخ (IMO یا شمسی طول البلد)، سرگرمی کا پروفائل |
| 5. انعکاس کی شرط | آئینہ نما انعکاس (McKinley)، گاؤسی رواداری 0.05 rad، بہترین رخ (SM6FHZ)، DH9GCD فارمولا |
| 6. ایک نقطے سے کارکردگی تک | ہر 15 km پر انعکاس کے نقاط، ہر نقطے کا وزن، فیصد؛ QTFGUI (DJ5HG) سے موازنہ |
| 7. نتائج پڑھنا | جانب A / B، راستے کا اشاریہ، ریڈیئنٹس کے رنگ، PREV زون، اینٹینا سے نظر آنے والی عمودی تراش |
| 8. کام کی فریکوئنسی اور راستے کا نقصان | λ³ / λ² اصول، ریڈار سے شوقیہ بینڈ تک، راستے کے نقصان کے حوالے |
| 9. معلوم حدود | صرف کم کثافت لکیریں، isotropic اینٹینا، عملی قدریں |
| 10. ذرائع | 17 نمبر شدہ ذرائع |

## بٹن

| بٹن | کیا کرتا ہے |
|---|---|
| **Word میں برآمد کریں (.docx)...** | `data/efficienza_spiegazione.docx` کی ایک نقل آپ کی منتخب جگہ پر محفوظ کرتا ہے (تجویز کردہ نام *YA-MS - calcolo dell'efficienza.docx*) |
| **Word میں کھولیں** | Word دستاویزات کے پہلے سے طے شدہ پروگرام (Word، LibreOffice، …) سے وہی `.docx` کھولتا ہے |

## فائلیں

| فائل | مواد |
|---|---|
| `data/efficienza_spiegazione.txt` | ٹیب میں دکھایا جانے والا متن، ہر لائن میں ایک بلاک (`TITLE`، `SUB`، `H1`، `H2`، `P`، `TAG|FONTE|…`، `TAG|RILIEVO|…`، `TAG|SCELTA|…`، `EQ`، `LI`، `SRC`) |
| `data/efficienza_spiegazione.docx` | Word ورژن |
| `doc/YA-MS_manuale_calcoli.docx` | **حساب کا دستی کتابچہ**: تمام مساواتیں (Word کا مساوات ایڈیٹر)، نمبروں اور ذرائع کے ساتھ |

دونوں دستاویزات سورس سے `tools/build_spiegazione.py data` اور `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` کے ذریعے دوبارہ بنائی جاتی ہیں۔
