[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-BR) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · **اردو** · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [ไทย](Experimental-Forecasts-th) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-TW)

# تجرباتی پیش گوئیاں

*ٹیب: پیش گوئی کا حساب › تجرباتی پیش گوئیاں۔*

[![تجرباتی پیش گوئیاں](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

یہ ٹیب **Collm ریڈار (36.2 MHz)** کی شہابی گنتیوں کو **کسی شوقیہ بینڈ پر فی گھنٹہ انعکاسات** کے تخمینے میں بدلتا ہے (پہلے سے 144 MHz، 28 سے 1300 MHz تک کوئی بھی فریکوئنسی)، آپ کے راستے کے لیے **اگلے 24 گھنٹوں** کی پیش گوئی کرتا ہے اور تخمینے کا کسی **RMOB** مشاہد سے **موازنہ** کرنے دیتا ہے – مثلاً 143.050 MHz پر GRAVES سننے والا کوئی۔

> یہاں سب کچھ **تجرباتی** ہے: فریکوئنسی کا اصول ایک تجربی اصول ہے، اور اسٹیشن فیکٹر آپ کے اسٹیشن پر منحصر ہے۔ اعداد کو گھنٹوں اور دنوں کے موازنے کے لیے استعمال کریں، اور بینڈ پر ان کی جانچ کریں۔

## کنٹرول

| کنٹرول | پہلے سے طے شدہ | کیا کرتا ہے |
|---|---|---|
| **ہدف فریکوئنسی MHz** | 144 | پیش گوئی کی فریکوئنسی (28–1300 MHz) |
| **λ^k قوت نما** | 3 | فریکوئنسی اصول کی قوت نما k (SM6FHZ: 3) |
| **اسٹیشن فیکٹر K** | 1 | وصول کنندہ اسٹیشن (طاقت، اینٹینا) کو مدِنظر رکھتا ہے؛ اسی بینڈ پر کسی RMOB مشاہد سے موازنے سے حاصل ہوتا ہے |
| **ڈسک سے RMOB فائل لوڈ کریں...** | | ایک ماہانہ RMOB متنی فائل پڑھتا ہے (نیچے دیکھیں) |
| **RMOB فائل سے قوت نما اخذ کریں** | | Collm اور RMOB کے مشترکہ گھنٹوں سے k نکالتا ہے |
| **RMOB مشاہد** | خالی | مشاہد کا نام جیسا فائل کے نام میں ہے (مثلاً `NAME_112026rmob.TXT` → `NAME`) |
| **RMOB ابھی ڈاؤن لوڈ کریں** | | اس مشاہد کی موجودہ مہینے کی فائل ایک بار ڈاؤن لوڈ کرتا ہے |
| **ہر 5 منٹ بعد خودکار ڈاؤن لوڈ (صرف RMOB کی اجازت سے فعال کریں)** | **بند** | دیکھیں [RMOB اور خودکار پروگرام](#rmob-اور-خودکار-پروگرام) |

کنٹرولز کے نیچے نارنجی لائن موجودہ اعداد کے ساتھ اصول دکھاتی ہے، مثلاً *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*، دورانیے کی منتقلی اور اس فریکوئنسی پر IARU زیادہ سے زیادہ پنگ۔

## ریڈار سے شوقیہ بینڈ تک

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}\sec^2\varphi
```

**ماخذ:** SM6FHZ، *"432 MHz Meteorscatter, Challenges and Techniques"*، 45th Nordic VUSHF، مئی 2025 – انعکاسات کی تعداد اور شدت **λ³** کے تناسب سے، دورانیہ **λ²** کے تناسب سے (432 MHz، 144 MHz سے 14–15 dB کم ہے اور 1/9 وقت رہتا ہے)۔ **جانچ:** McKinley کی مساوات میں λ³ ایک کم کثافت لکیر کی طاقت ہے، لکیروں کی تعداد نہیں؛ کمیتی اشاریہ 2 کے لیے کسی مقررہ حد سے اوپر لکیروں کی تعداد تقریباً λ^1.5 کے تناسب سے بدلتی ہے (IZ5TEK؛ OH5IY)۔ پروگرام SM6FHZ کا تجرباتی اصول k = 3 برقرار رکھتا ہے اور یہ بات واضح کرتا ہے؛ آپ کے اسٹیشن کے لیے درست k، RMOB سے موازنے سے حاصل ہوتا ہے۔ آگے کی طرف انتشار میں دورانیہ sec²φ کے ساتھ بھی بڑھتا ہے (McKinley؛ OH5IY): Collm پیچھے کی طرف انتشار (φ = 0) میں ناپتا ہے، اس لیے پیش گوئی راستے کے وسطی نقطے پر sec²φ سے ضرب دیتی ہے (60° پر ×4، 70° پر ×8.5، 80° پر ×33)۔ k = 3 کے ساتھ Collm پر 1000 شہابیے/گھنٹہ، **144 MHz پر تقریباً 16 انعکاس/گھنٹہ** بنتے ہیں؛ 143.050 MHz پر GRAVES کے RMOB مشاہدین عموماً **20 سے 140 بازگشت/گھنٹہ** گنتے ہیں (RMOB بلیٹن، جون 2018): مقدار کا درجہ ہم آہنگ ہے، اور فرق اسٹیشن فیکٹر K ہے۔ (دستی کتابچے کی مساوات 44–45۔)

## اگلے 24 گھنٹے

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**تسلسل (persistence):** پچھلے دن کے اسی گھنٹے کی منتقل شدہ قدر (موجود نہ ہو تو دو دن پہلے کی)، **راستے کے شہابی بارش اشاریے** I (Σ ZHR × کارکردگی، دیکھیں [کارکردگی کا حساب](Efficiency-Calculation-ur#ماڈل)) کی تبدیلی سے درست کی گئی۔ مستقل 10 منتشر پس منظر کی نمائندگی کرتا ہے اور اشاریہ چھوٹا ہو تو تصحیح کو محدود رکھتا ہے۔ *پروگرام کا انتخاب (دستی کتابچے کی مساوات 47)۔*

| پینل | مواد |
|---|---|
| **Collm پر ناپا گیا اور f MHz پر منتقل کیا گیا – کل اور آج (UTC)** | Collm ریڈار کے شہابیے/گھنٹہ؛ منتقل شدہ قدریں (نارنجی، دائیں پیمانہ)؛ لوڈ ہوں تو RMOB کی گنتیاں (سبز، دائیں پیمانہ) |
| **… کے لیے f MHz پر اگلے 24 گھنٹوں کی تجرباتی پیش گوئی** | پیش گوئی شدہ انعکاس/گھنٹہ (بار) اور راستے کا شہابی بارش اشاریہ (دائیں پیمانہ) |
| جدول | UTC وقت · Collm اسی گھنٹے · منتقل شدہ · راستے کا شہابی بارش اشاریہ · پیش گوئی /گھنٹہ · **درجہ بندی** |

**درجہ بندی:** *اچھا* جب پیش گوئی 24 گھنٹے کے اوسط کی کم از کم 1.3 گنا ہو، 0.8 گنا سے *درمیانہ*، اس سے نیچے *کمزور*۔ یہی پیش گوئی **تجرباتی پیش گوئی** کارڈ میں اور [کارکردگی کا حساب](Efficiency-Calculation-ur) کی نارنجی قطار میں آتی ہے، اور [GRAVES ریڈار](GRAVES-Radar-ur#متوقع-بازگشت-تجرباتی) ٹیب کی متوقع بازگشت کی بنیاد ہے۔

## RMOB موازنہ

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line، Pierre Terrier) ریڈیو مشاہدین کی گھنٹہ وار شہابی گنتیاں جمع کرتا ہے؛ اٹلی میں بہت سے 143.050 MHz پر GRAVES سنتے ہیں (Venice Planetarium، Faenza، Rovereto اور دیگر)۔

**RMOB فائلیں پڑھنا۔** دو متنی فارمیٹ قبول ہیں:

| فارمیٹ | شکل | نوٹ |
|---|---|---|
| ماہانہ فائل (Colorgramme / Spectrum Lab) | ہر دن کی ایک قطار، `day| n| n| …` 24 گھنٹہ وار قدروں کے ساتھ | معمول کی `NAME_MMYYYYrmob.TXT` |
| بلیٹن کا جدول | ہیڈر ` UT |  1   2   3 …`، قطاریں `0h|175 166 …` | اگر فائل میں کئی مشاہدین ہوں تو ایک کے بعد ایک پڑھے جاتے ہیں: ایک ہی مشاہد والی فائل استعمال کریں |

مہینہ اور سال فائل کے نام (`…_MMYYYYrmob…`) یا ہیڈر سے آتے ہیں؛ ورنہ موجودہ مہینہ استعمال ہوتا ہے (اور پروگرام یہ بتاتا ہے)۔

**قوت نما اخذ کرنا۔** K = 1 کے ساتھ، مشترکہ گھنٹوں (کم از کم 3) پر RMOB/Collm تناسبات کے وسطانیے سے:

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*پروگرام کا انتخاب (دستی کتابچے کی مساوات 46)۔* ڈائیلاگ مشترکہ گھنٹے، وسطانی تناسب اور k دکھاتا ہے؛ **ہاں** k لاگو کرتا ہے (اور K = 1 رکھتا ہے)، **نہیں** k = 3 رکھتا ہے – پھر K کو اسی ڈائیلاگ میں تجویز کردہ قدر کے مطابق ہاتھ سے مقرر کریں۔

## RMOB اور خودکار پروگرام

RMOB **خودکار پروگراموں سے کہتا ہے کہ اس کی فائلیں نہ اٹھائیں**۔ اسی وجہ سے آغاز پر **خودکار ڈاؤن لوڈ بند** ہوتا ہے اور اسے **صرف RMOB سے اجازت لینے کے بعد** فعال کرنا چاہیے۔ اس کے بغیر آپ ہمیشہ **ڈسک سے RMOB فائل لوڈ کریں...** استعمال کر سکتے ہیں یا ضرورت پڑنے پر **RMOB ابھی ڈاؤن لوڈ کریں** دبا سکتے ہیں۔

ڈاؤن لوڈ کا پتا `config.ini` میں ایک سانچہ ہے (کلید `rmob_url`، پہلے سے `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`، جہاں `{NOME}` مشاہد ہے اور `{MMAAAA}` مہینہ اور سال)؛ ڈاؤن لوڈ شدہ فائلیں `data/radar/` میں رکھی جاتی ہیں۔
