[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · **اردو** · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – meteor scatter کی پیش گوئیاں اور شہابی بارشوں کی براہِ راست کارکردگی

*از Costantino Cerrotta IC8TEM*

**YA-MS** ریڈیو شوقیہ آپریٹروں کے لیے ایک مفت پروگرام ہے جو **50، 70، 144، 222 اور 432 MHz پر meteor scatter (MS)** کرتے ہیں۔ آپ کے لوکیٹر اور DX اسٹیشن کے لوکیٹر کے درمیان حقیقی راستے کے لیے یہ گھنٹہ بہ گھنٹہ حساب لگاتا ہے کہ ہر فعال شہابی بارش راستے کی کتنی مدد کرتی ہے (اس کی **کارکردگی**)، انعکاس راستے کی کس جانب سے آتے ہیں (**Hot A / Hot B**)، اینٹینا کس طرف رکھنا ہے، اور ایک **براہِ راست شہابی ریڈار** (Collm، جرمنی) سے اخذ کردہ فی گھنٹہ انعکاسات کی ایک تجرباتی پیش گوئی۔ یہ **Windows، Linux، Raspberry Pi اور macOS** پر چلتا ہے (.NET 8 + Avalonia)، انٹرفیس کی 36 زبانوں میں۔

مرکزی ماخذ **C. Cerrotta IC8TEM اور G. Sartori IV3GTH** کا مضمون ہے: *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (ورژن 7)۔ پروگرام کا ہر فارمولا اور ہر ڈیٹا اپنے ماخذ کا حوالہ دیتا ہے؛ دیکھیں [ذرائع](Sources-ur)۔

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="آسمانی گنبد"></a><br><sub>آسمانی گنبد</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="کارکردگی کا حساب"></a><br><sub>کارکردگی کا حساب</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES ریڈار"></a><br><sub>GRAVES ریڈار</sub></td>
</tr></table>

## یہ کس کے لیے ہے

- وہ آپریٹر جو جاننا چاہتے ہیں کہ meteor scatter کا راستہ **کب** کھلا ہے اور اینٹینا **کہاں** رکھنا ہے – عام سی بات "آج رات شہابی بارش عروج پر ہے" سے آگے۔
- وہ اسٹیشن جو **144 اور 432 MHz پر لمبے راستے** کرتے ہیں، جہاں ریڈیئنٹ کا مقام طے کرتا ہے کہ کوئی شہابی بارش کارآمد ہے یا بے کار۔
- ہر وہ شخص جو **اعداد کی جانچ** کرنا چاہتا ہے: حساب کا دستی کتابچہ اور پروگرام کے اندر کی وضاحت ہر قدم اس کے ماخذ کے ساتھ دیتے ہیں: کوئی شائع شدہ ماخذ، پروگرام پر کی گئی جانچ، یا پروگرام کا اپنا انتخاب۔

## ٹیب

ورژن 1.6 سے مرکزی ٹیبوں کے **ذیلی ٹیب** ہیں (مرکزی قطار کے نیچے ایک ہلکی قطار)۔ آغاز پر 5 سیکنڈ کی ایک اسپلیش اسکرین ESO کے VLT کے اوپر پرسیئڈز دکھاتی ہے (تصویر ESO/S. Guisard، CC BY 4.0)۔

| ٹیب | ذیلی ٹیب | کیا دکھاتا ہے |
|---|---|---|
| **لائیو اور ریئل ٹائم ڈیٹا** | [براہِ راست ٹریفک](Live-Traffic-ur) | جمع شدہ تمام MS ٹریفک کا سمتی نقشہ، ہر رابطے کے لیے سب سے ممکنہ شہابی لکیروں کا بادل، بینڈ کے رنگ، نئے اسپاٹ جھلملاتے ہوئے |
| | [ریڈار فلکس](Radar-Flux-ur) | Collm SKiYMET ریڈار سے پڑھی گئی شہابیوں کی گھنٹہ وار گنتی اور لکیروں کی اونچائیاں، Sodankylä کی تصویر، آپ کے بینڈ پر تخمینہ |
| | [GRAVES ریڈار](GRAVES-Radar-ur) | GRAVES → آپ forward-scatter راستہ: بیم میں مفید زون، سیکٹر اور قدم، بیم کا اگلا گزر، کیسے سنیں |
| | [ڈیٹا جمع کرنا](Data-Collection-ur) | تین telnet cluster سلسلے (DX cluster، RBN، DM4X/PSKReporter) اور MS اسپاٹس کا فلٹر |
| **پیش گوئی کا حساب** | [پیش گوئی کا حساب](Sky-View-ur) | Hot A / Hot B، اینٹینا لوب، PREV زون اور شہابی بارش کی حرکت کے ساتھ راستے کا اوپر سے منظر؛ شہابی بارشوں کی فہرست؛ ریڈیئنٹس اور درست اینٹینا سمتوں کے ساتھ چھوٹا آسمانی گنبد؛ اینٹینا سے نظر آنے والی عمودی تراش |
| | [جیومیٹری اور راستے کا نقصان](Geometry-and-Path-Loss-ur) | فاصلہ، وسطی نقطہ، ارتفاع، Hot A / Hot B، مشترکہ زون کی حدود، 28–432 MHz راستے کا نقصان، لنک بجٹ، اینٹینا |
| | [کارکردگی کا حساب](Efficiency-Calculation-ur) | ایک نظر کے کارڈ، جانب A/B کے ساتھ ہر شہابی بارش کی گھنٹہ وار کارکردگی، راستے کا اشاریہ، DH9GCD موازنہ، گراف |
| | [تجرباتی پیش گوئیاں](Experimental-Forecasts-ur) | λ^k اور اسٹیشن فیکٹر K کے ساتھ 144 MHz (یا کسی بھی فریکوئنسی) پر منتقل کیا گیا Collm فلکس، 24 گھنٹے کی پیش گوئی، RMOB موازنہ |
| **تکنیکی دستاویزات** | [ذرائع](Sources-ur) | تمام ذرائع؛ مرکزی ماخذ Cerrotta–Sartori مضمون ہے |
| | [یورپی ریڈاروں کا نقشہ](European-Radar-Map-ur) | آپ کے اسٹیشن کے لحاظ سے Collm، Sodankylä، GRAVES اور CMOR کہاں ہیں |
| | [کارکردگی - وضاحت](Efficiency-Explanation-ur) | کارکردگی کا حساب کیسے ہوتا ہے، اس کی قدم بہ قدم دستاویز، Word میں برآمد کے قابل |
| [براہِ راست شہابی بارشیں](Live-Showers-ur) | – | Global Meteor Network کے ناپے گئے ZHR اور CMOR کے ریڈیئنٹ نقشے |
| [شہابی بارشیں](Showers-ur) | – | اگلے عروج کے ساتھ IMO کی فہرست (IMO کی تاریخ اور وقت، یا حساب شدہ) |
| [مربعوں کا نقشہ](Grid-Square-Map-ur) | – | ADIF فائل سے رابطہ شدہ اور تصدیق شدہ Maidenhead مربعے، ہر بینڈ کا ایک ٹیب |

ٹیبوں کے اوپر کنٹرول کی تین قطاریں ہیں (آپ کا لوکیٹر، DX اسٹیشن، بینڈ، اینٹینا، لکیروں کی اونچائی، وقت)؛ دیکھیں [آغاز](Getting-Started-ur)۔ **کنٹرول** بٹن انہیں سمیٹ دیتا ہے، اور زبان اور رنگ سکیم اوپر دائیں جانب منتخب کی جاتی ہیں؛ دیکھیں [ترتیبات اور ڈیٹا فولڈر](Settings-and-Data-Folder-ur)۔

## مختصراً

- **حقیقی راستہ، مقررہ سمتیں نہیں**: کارکردگی دونوں لوکیٹروں کے درمیان عظیم دائرے کے راستے کے لیے حساب کی جاتی ہے (پرانے پروگرام چار مقررہ سمتیں استعمال کرتے تھے)۔
- **آئینہ نما انعکاس کا ماڈل** (McKinley) E تہہ کے ہر 15 km پر نقاط کے لیے، لکیروں کی اونچائی Collm ریڈار سے براہِ راست پڑھی جاتی ہے۔
- وسطی نقطے کے دونوں طرف 150 km پر **Hot A / Hot B** (30–400 km تک قابلِ تبدیل)، تجویز کردہ سرخ میں، اور جو پہلے ہی آپ کے اینٹینا لوب کے اندر ہیں وہ سرمئی میں۔
- **براہِ راست ریڈار**: Collm ہر 5 منٹ بعد جانچا جاتا ہے، صرف بدلے ہوئے ذرائع دوبارہ ڈاؤن لوڈ ہوتے ہیں؛ آف لائن ہونے پر پروگرام آخری محفوظ ڈیٹا کے ساتھ کام جاری رکھتا ہے۔
- SM6FHZ کے λ³ اصول کے ساتھ 50/144/432 MHz پر **تجرباتی** پیش گوئی، RMOB مشاہدین سے قابلِ موازنہ۔
- سب کچھ پروگرام کے ساتھ ایک ہی **`data`** فولڈر میں: نہ AppData، نہ سسٹم فولڈر۔

> کارکردگی ایک تجرباتی ماڈل ہے (آئینہ نما انعکاس + کم کثافت لکیریں)۔ اسے MCG_MS، MS-Soft اور بینڈ پر اپنے تجربے سے موازنہ کریں۔

## کہاں سے شروع کریں

1. [انسٹالیشن](Installation-ur)
2. [آغاز](Getting-Started-ur)
3. اگر کچھ کام نہ کرے تو [مسائل کا حل اور عمومی سوالات](Troubleshooting-FAQ-ur)۔

ڈاؤن لوڈ: GitHub پر **[Releases](https://github.com/ic8tem/YA-MS/releases)**۔
