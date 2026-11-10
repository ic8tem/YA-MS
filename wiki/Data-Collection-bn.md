[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · **বাংলা** · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# ডেটা সংগ্রহ

*ট্যাব: লাইভ ও রিয়েল-টাইম তথ্য › ডেটা সংগ্রহ।*

[![ডেটা সংগ্রহ](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## চারটি উৎস

ট্যাবটি তিনটি টেলনেট প্রবাহ এবং PSKReporter-এর MQTT ফিড থেকে **মিটিওর স্ক্যাটার স্পট** সংগ্রহ করে, প্রতিটি তার নিজস্ব উপ-ট্যাবে:

| উপ-ট্যাব | ডিফল্ট | মন্তব্য |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | আপনার পছন্দের একটি ক্লাস্টার। ON0DXK-এ VHF ব্যান্ড ফিল্টার করা থাকে: `set/filter dxbm/pass 6` (তারপর 4, 2…) দিয়ে সেগুলো চালু করুন। |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8)। স্কিমারগুলো কদাচিৎ MS মোড ডিকোড করে। |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | **PSKReporter**-এর স্পট বহনকারী DM4X ক্লাস্টার: WSJT-X ও MSHV-র MSK144 ডিকোড এখানে আসে। |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | **MQTT**-এর মাধ্যমে PSKReporter-এর সরাসরি স্পট (M0LTE-এর পরিষেবা): লগইন লাগে না, প্রতিটি স্পটে আগে থেকেই প্রেরক ও গ্রাহক স্টেশনের লোকেটর থাকে। ডিফল্ট টপিক: 6 m, 4 m, 2 m, 1.25 m, 70 cm-এ MSK144 এবং 2 m-এ FSK441 (`pskr/filter/v2/band/mode/#`); *ডিফল্ট টপিক* সেগুলো ফিরিয়ে আনে। |
| **সংগৃহীত MS স্পট** | – | গৃহীত স্পটের টেবিল, নতুনগুলো আগে। |

প্রতিটি প্রবাহে আছে হোস্ট, পোর্ট, লগইনের পরে পাঠানো কমান্ড, *পুনঃসংযোগ করুন*, *শুরুতেই সংযোগ*, একটি কনসোল এবং কমান্ড পাঠানোর একটি লাইন। ওপরে আপনার **লগইনের কলসাইন** লিখুন। MQTT উৎসে আছে হোস্ট, পোর্ট, টপিক (প্রতি লাইনে একটি অথবা `;` দিয়ে আলাদা), *পুনঃসংযোগ করুন* ও *শুরুতেই সংযোগ* (ডিফল্টে বন্ধ) এবং প্রাপ্ত স্পটসহ একটি কনসোল; এর স্পটগুলোও একই ফিল্টারের মধ্য দিয়ে যায়। একটি পট্টি চারটি উৎসের অবস্থা দেখায় (সবুজ বিন্দু = সংযুক্ত)। ভাষা বা রঙের থিম বদলালেও সেশনগুলো খোলা থাকে।

## ফিল্টার (উইন্ডোর 40 %)

- **ঐচ্ছিক স্থানীয় ফিল্টার:** **27990.0 kHz**-এর নিচের ক্লাস্টার লাইন সঙ্গে সঙ্গে বাদ দেওয়া হয় (দেখানো হয় না, সংরক্ষিত হয় না)।
- **প্রথম মানদণ্ড – MS-এর সাধারণ ফ্রিকোয়েন্সি:** 50190–50300, 70100–70400, 144290–144399 kHz। এই উইন্ডোগুলোর মধ্যে একটি স্পট মোডের নাম ছাড়াও গৃহীত হয়, যদি না মন্তব্যে অন্য কোনো প্রোপাগেশন ঘোষিত থাকে: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`। উইন্ডো ও ট্যাগ সম্পাদনা করা যায়।
- **দ্বিতীয় মানদণ্ড – MS মোড:** উইন্ডোর বাইরে, বা ওই ট্যাগগুলোর কোনোটি থাকলে, একটি স্পট কেবল তখনই রাখা হয় যদি তাতে **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (কেবল MS-এ ব্যবহৃত ডিজিটাল মোড) অথবা **\<MS\>** থাকে – বড়, ছোট বা মিশ্র হাতের অক্ষরে। শব্দগুলো বন্ধ করা, যোগ করা ও সরানো যায়; প্রতিটির নিজস্ব কাউন্টার আছে।
- **ব্যান্ড** 28, 50, 70, 144, 222, 432 MHz; পেস্ট করা লাইনে **ফিল্টার পরীক্ষা**; **কাউন্টার**।

## লোকেটর ও সংরক্ষণ

অনুপস্থিত লোকেটর, অথবা কেবল 4 অক্ষরের লোকেটর, নেওয়া হয় **CALL3** আর্কাইভ থেকে (`data/call3.txt`, JTDX ফাইল, দশ লক্ষেরও বেশি কলসাইন), যা 4 অক্ষরের লোকেটরের ওপর সর্বদা প্রাধান্য পায়। গৃহীত স্পটগুলো `data/spot_ms`-এ সংরক্ষিত হয়, প্রতিদিন একটি CSV ফাইল, এবং [সরাসরি ট্রাফিক](Live-Traffic-bn) মানচিত্রে তথ্য জোগায়।
