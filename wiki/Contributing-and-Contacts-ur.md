[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · **اردو** · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh)

# تعاون اور رابطہ

YA-MS ان لوگوں کی رپورٹوں سے بہتر ہوتا ہے جو اسے بینڈ پر استعمال کرتے ہیں۔ ہر تصحیح کا سہرا اس کے ماخذ کو دیا جاتا ہے۔

## رابطہ

| | |
|---|---|
| مصنف | Costantino Cerrotta **IC8TEM** |
| ای میل | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## مسئلے کی اطلاع دینا

**GitHub پر ایک issue** کھولیں یا ای میل لکھیں، ساتھ میں:

- آپریٹنگ سسٹم اور YA-MS کا ورژن (ونڈو کے عنوان میں)؛
- دونوں لوکیٹر، بینڈ اور UTC وقت؛
- آپ کو کیا توقع تھی اور کیا نظر آیا (اسکرین شاٹ مددگار ہے)؛
- ریڈار کے مسائل کے لیے، [ریڈار فلکس](Radar-Flux-ur) ٹیب میں دکھایا گیا پیغام۔

## خاص طور پر کیا مفید ہے

- **بینڈ کی رپورٹیں۔** وہ گھنٹے اور راستے جہاں کارکردگی یا پیش گوئی درست تھی – یا غلط۔ ماڈل تجرباتی ہے اور اسے حقیقی QSO اور MCG_MS / MS-Soft سے موازنے کی ضرورت ہے۔
- **RMOB موازنے۔** [RMOB موازنہ](Experimental-Forecasts-ur#rmob-موازنہ) سے آپ کو اسٹیشن فیکٹر K اور قوت نما k کی جو قدریں ملیں، اپنے بینڈ اور اسٹیشن کے ساتھ۔
- **ماخذ کے ساتھ ڈیٹا۔** ریڈیئنٹ کی بہتر حرکت، سرگرمی کے پروفائل، IMO کی نئی عروج کی تاریخیں (`data/massimi_imo.csv`)، اینٹینا کا ڈیٹا: ماخذ شامل کریں اور اس کا حوالہ دیا جائے گا۔
- **ریڈار گرافوں میں تبدیلیاں۔** اگر Collm گراف کا فارمیٹ بدلے تو تصویر کی ایک نقل (`data/radar/`) پڑھنے کے طریقے کی دوبارہ معیار بندی میں مدد دیتی ہے۔

## ترجمے

انٹرفیس کے ترجمے **`data/lingue/<code>.txt`** میں سادہ متنی فائلیں (UTF-8) ہیں اور **کوئی بھی ان کی تصحیح کر سکتا ہے**:

```
<Italian text><TAB><translation>
```

- ہر لائن میں ایک اندراج؛ `#` سے شروع ہونے والی لائنیں تبصرے ہیں۔
- دونوں کالموں میں دو حروف `\n` کا مطلب لائن بریک ہے۔
- placeholders `{0}`، `{1}`، … ان کے فارمیٹ کے ساتھ رکھیں (مثلاً `{0:F1}`، `{3:+0;-0}`)، اپنی زبان کی ضرورت کی ترتیب میں۔
- غائب یا خالی اندراجات اطالوی میں دکھائے جاتے ہیں۔ تمام کلیدوں کی فہرست `data/lingue/chiavi.txt` ہے (`tools/estrai_chiavi.py` سے بنی، اس میں ترمیم نہ کریں)۔

اپنی انسٹالیشن کے `data/lingue` فولڈر میں فائل میں ترمیم کریں اور نتیجہ دیکھنے کے لیے YA-MS دوبارہ شروع کریں (یا زبان بدلیں)۔ چونکہ یہ فائلیں **ہر تازہ کاری پر نئے ورژن سے بدل دی جاتی ہیں**، براہِ کرم اپنی **تصحیحات بھیج بھی دیں** – ای میل سے یا GitHub پر pull request کے طور پر (`data/lingue/`) – تاکہ وہ اگلی ریلیز میں شامل ہوں۔

یہ وکی English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文 میں موجود ہے؛ وکی کے صفحات کی تصحیحات بھی خوش آمدید ہیں۔
