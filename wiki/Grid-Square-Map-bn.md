[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · **বাংলা** · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# বর্গের মানচিত্র

*ট্যাব: বর্গের মানচিত্র।*

[![বর্গের মানচিত্র](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

আপনার লগের ADIF ফাইল থেকে পড়া, যেসব Maidenhead বর্গে (4 অক্ষর) আপনার **সংযোগ হয়েছে** এবং যেগুলো **নিশ্চিত**, ইউরোপের একটি মানচিত্রে – **প্রতিটি ব্যান্ডের জন্য একটি উপ-ট্যাব: 50, 70, 144, 222 ও 432 MHz**।

## নিয়ন্ত্রণ

| নিয়ন্ত্রণ | কী করে |
|---|---|
| **ADIF ফাইল লোড করুন...** | একটি `.adi` / `.adif` ফাইল পড়ে। নতুন ADIF আগের তথ্য **প্রতিস্থাপন করে**। |
| **মেমরি মুছুন** | ADIF থেকে লোড করা সব বর্গ মুছে দেয় (নিশ্চিতকরণ চায়)। |
| মাউস | **হুইল = জুম, টেনে আনা = সরানো, বর্গের ওপর মাউস = QSO** (তারিখসহ সর্বোচ্চ ছয়টি কলসাইন, নিশ্চিত হলে *(নিশ্চিত)*) |

লোড করার পর স্ট্যাটাসে দেখা যায় *…টি QSO পড়া হয়েছে, 50-432 MHz ব্যান্ডে …টি QSO-বর্গ, …টি QSO বাতিল (অন্য ব্যান্ড বা বর্গ নেই)*। প্রতিটি ব্যান্ড-মানচিত্রের ক্যাপশন *…টি বর্গে সংযোগ, …টি নিশ্চিত*।

| রং | অর্থ |
|---|---|
| কমলা | সংযোগকৃত |
| সবুজ | নিশ্চিত (QSL বা LoTW) |

## ADIF কীভাবে পড়া হয়

- ব্যবহৃত ঘর: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF স্পেসিফিকেশন)।
- ব্যান্ড `BAND` থেকে, অথবা ফ্রিকোয়েন্সি থেকে: 50–54 MHz = 6 m, 69.9–71.5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1.25 m, 420–450 MHz = 70 cm।
- একটি বর্গ **নিশ্চিত** হয় যদি তার অন্তত একটি QSO-তে `QSL_RCVD = Y` বা `LOTW_QSL_RCVD = Y` থাকে।
- বর্গগুলো `data/adif_quadrati.csv`-এ রাখা হয়, যতক্ষণ না আপনি অন্য ফাইল লোড করেন বা **মেমরি মুছুন** চাপেন।

YA-MS LoTW-এর সাথে **সংযোগ করে না**: আপনার লগিং প্রোগ্রাম (বা LoTW) থেকে ADIF রপ্তানি করে এখানে লোড করুন।
