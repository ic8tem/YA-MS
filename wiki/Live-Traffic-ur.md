[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-BR) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · **اردو** · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-TW)

# براہِ راست ٹریفک

*ٹیب: لائیو اور ریئل ٹائم ڈیٹا › براہِ راست ٹریفک۔*

[![براہِ راست ٹریفک](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## کیا دکھاتا ہے

آپ کے اسٹیشن پر مرکوز ایک **سمتی مساوی الفاصلہ نقشہ** (مرکز سے فاصلہ = حقیقی فاصلہ، زاویہ = سمتیہ) جس پر [ڈیٹا جمع کرنا](Data-Collection-ur) سے حاصل شدہ **تمام meteor scatter ٹریفک** ہوتی ہے۔ ہر رابطے کے لیے پروگرام بناتا ہے:

- دونوں اسٹیشنوں کے درمیان **راستہ**، اس کے بینڈ کے رنگ میں: 28 MHz بھورا، 50 MHz سبز، 70 MHz فیروزی، 144 MHz نارنجی، 222 MHz گلابی، 432 MHz بنفشی؛
- راستے کے دونوں سروں پر دو **اسٹیشن**؛
- **بادل**: اس راستے اور اس وقت کے لیے سب سے ممکنہ شہابی لکیریں جہاں مرکوز ہیں۔

جن اسپاٹ کا کوئی اسٹیشن **نقشے سے باہر** ہو وہ رد کر دیے جاتے ہیں۔ جو اسپاٹ **ابھی آیا ہو** (3 منٹ سے زیادہ پرانا نہیں) وہ **ایک منٹ تک جھلملاتا ہے**، تاکہ نئی سرگرمی ایک نظر میں نمایاں ہو۔

## بادل کا حساب کیسے ہوتا ہے

ہر اسپاٹ کے لیے پروگرام دونوں لوکیٹروں کے درمیان راستہ بناتا ہے (وہی جیومیٹری جو آپ کے اپنے راستے کے لیے ہے، دیکھیں [جیومیٹری اور راستے کا نقصان](Geometry-and-Path-Loss-ur)) اور اسپاٹ کے وقت پر E تہہ کے نقطہ بہ نقطہ **ہر فعال شہابی بارش کے آئینہ نما انعکاس کے حصے** جمع کرتا ہے، اس کے ZHR سے وزن دے کر – بالکل [آسمانی گنبد](Sky-View-ur) کے **PREV زون** والا حساب۔ راستے کی جس جانب کل کا کم از کم 15 % ہو، وہاں بادل ایک **بیضوی** ہے: مرکز نقاط کے وزنی اوسط پر، نصف محور ان کے پھیلاؤ کی ذاتی قدروں (eigenvalues) کے جذرِ مربع کا 1.5 گنا، بڑا محور مرکزی ذاتی سمتیے کے ساتھ۔ جب کوئی شہابی بارش حصہ نہ ڈالے (صرف منتشر شہابیے) تو بادل دو روایتی **hot spot** ہوتے ہیں، ڈیشڈ لکیروں سے بنے ہوئے۔ مکمل مساواتیں حساب کے دستی کتابچے کے باب 10 میں ہیں۔

## کنٹرول

| کنٹرول | مطلب |
|---|---|
| **نقشے کا رداس** | آپ کے اسٹیشن سے 600–3500 km۔ |
| **دکھانے کے لیے اسپاٹ** | آخری 15 یا 30 منٹ، آخری گھنٹہ، آخری 3 گھنٹے، آخری 24 گھنٹے۔ |
| **جدول** | نقشے پر موجود رابطے، نئے پہلے، بینڈ کے رنگ میں؛ *بادل* مرکزی جانب انعکاسات کا حصہ دکھاتا ہے، یا *منتشر*۔ |
| **کلک** | کسی راستے یا جدول کی قطار پر: رابطہ نمایاں ہو جاتا ہے اور خانے میں بادل کے مرکز کا لوکیٹر، اس کا حصہ، سائز اور محور دکھائی دیتا ہے۔ |
