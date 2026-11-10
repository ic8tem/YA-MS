[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · **বাংলা** · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [ไทย](Contributing-and-Contacts-th) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# অবদান ও যোগাযোগ

যাঁরা ব্যান্ডে YA-MS ব্যবহার করেন তাঁদের প্রতিবেদনের মাধ্যমেই এটি উন্নত হয়। প্রতিটি সংশোধন তার উৎসকে কৃতিত্ব দিয়ে উল্লেখ করা হয়।

## যোগাযোগ

| | |
|---|---|
| লেখক | Costantino Cerrotta **IC8TEM** |
| ই-মেইল | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## সমস্যা জানানো

**GitHub-এ একটি issue** খুলুন অথবা ই-মেইল লিখুন, সাথে দিন:

- অপারেটিং সিস্টেম ও YA-MS-এর সংস্করণ (উইন্ডোর শিরোনামে);
- দুটি লোকেটর, ব্যান্ড ও UTC সময়;
- আপনি কী আশা করেছিলেন আর কী দেখেছেন (একটি স্ক্রিনশট সাহায্য করে);
- রাডারের সমস্যার ক্ষেত্রে, [রাডার ফ্লাক্স](Radar-Flux-bn) ট্যাবে দেখানো বার্তা।

## বিশেষভাবে যা কাজে লাগে

- **ব্যান্ডের প্রতিবেদন।** যে ঘণ্টা ও পথে দক্ষতা বা পূর্বাভাস সঠিক ছিল – অথবা ভুল। মডেলটি পরীক্ষামূলক এবং প্রকৃত QSO ও MCG_MS / MS-Soft-এর সাথে তুলনা প্রয়োজন।
- **RMOB তুলনা।** [RMOB তুলনা](Experimental-Forecasts-bn#rmob-তুলনা) দিয়ে আপনি স্টেশন গুণক K ও সূচক k-এর যে মান পেয়েছেন, আপনার ব্যান্ড ও স্টেশনসহ।
- **উৎসসহ তথ্য।** বিকিরণ বিন্দুর আরও ভালো সরণ, সক্রিয়তার প্রোফাইল, IMO-র নতুন সর্বোচ্চের তারিখ (`data/massimi_imo.csv`), অ্যান্টেনার তথ্য: উৎস উল্লেখ করুন, তা উদ্ধৃত করা হবে।
- **রাডার চার্টের পরিবর্তন।** Collm চার্টের ফরম্যাট বদলালে ছবির একটি কপি (`data/radar/`) পড়ার পদ্ধতি আবার ক্যালিব্রেট করতে সাহায্য করে।

## অনুবাদ

ইন্টারফেসের অনুবাদগুলো **`data/lingue/<code>.txt`**-এ সাধারণ টেক্সট ফাইল (UTF-8) এবং **যে কেউ এগুলো সংশোধন করতে পারেন**:

```
<Italian text><TAB><translation>
```

- প্রতি লাইনে একটি এন্ট্রি; `#` দিয়ে শুরু হওয়া লাইন মন্তব্য।
- দুই কলামেই `\n` দুটি অক্ষর মানে লাইন বিরতি।
- প্লেসহোল্ডার `{0}`, `{1}`, … তাদের ফরম্যাটসহ রাখুন (যেমন `{0:F1}`, `{3:+0;-0}`), আপনার ভাষার প্রয়োজনীয় ক্রমে।
- অনুপস্থিত বা খালি এন্ট্রি ইতালীয় ভাষায় দেখানো হয়। সব কী-র তালিকা হলো `data/lingue/chiavi.txt` (`tools/estrai_chiavi.py` দিয়ে তৈরি, সম্পাদনা করবেন না)।

আপনার ইনস্টলেশনের `data/lingue` ফোল্ডারে ফাইলটি সম্পাদনা করে YA-MS আবার চালু করুন (অথবা ভাষা বদলান) ফলাফল দেখতে। যেহেতু এই ফাইলগুলো **প্রতিটি হালনাগাদে নতুন সংস্করণ দিয়ে প্রতিস্থাপিত হয়**, অনুগ্রহ করে আপনার **সংশোধনগুলো পাঠিয়েও দিন** – ই-মেইলে অথবা GitHub-এ pull request হিসেবে (`data/lingue/`) – যাতে সেগুলো পরবর্তী রিলিজে যায়।

এই উইকি English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文-তে আছে; উইকির পাতাগুলোর সংশোধনও স্বাগত।
