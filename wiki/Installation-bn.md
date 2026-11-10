[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-BR) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · **বাংলা** · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-TW)

# ইনস্টলেশন

সব প্যাকেজ **[Releases](https://github.com/ic8tem/YA-MS/releases)** পাতায় আছে (নিচের ফাইলের নামে `x.y.z` হলো সংস্করণ, যেমন `1.2.0`)। কিছু কম্পাইল করতে হয় না, আলাদা করে কিছু ইনস্টল করতেও হয় না: প্রতিটি প্যাকেজে .NET 8 রানটাইম রয়েছে।

| সিস্টেম | ফাইল | কোথায় ইনস্টল হয় |
|---|---|---|
| Windows (64-বিট) | `YA-MS-x.y.z-windows-x64-setup.exe` (ইনস্টলার) | `C:\YA-MS` |
| Windows (64-বিট), পোর্টেবল | `YA-MS-x.y.z-windows-x64-portatile.zip` | যেকোনো ফোল্ডার যেখানে আপনি লিখতে পারেন |
| Windows (32-বিট, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` অথবা `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-বিট): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (প্রথম চালুতে সেখানে কপি হয়) |
| Linux (64-বিট), যেকোনো ডিস্ট্রিবিউশন | `YA-MS-x.y.z-linux-x64.tar.gz` (পোর্টেবল বা `./installa.sh` দিয়ে) | `~/YA-MS` অথবা যেকোনো ফোল্ডার |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-বিট) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-বিট) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian প্যাকেজ | `ya-ms_x.y.z_arm64.deb` (64-বিট) অথবা `ya-ms_x.y.z_armhf.deb` (32-বিট) | `~/YA-MS` (প্রথম চালুতে সেখানে কপি হয়) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, শুধু অ্যাপ্লিকেশন | `YA-MS-x.y.z-mac-apple-silicon-app.zip` অথবা `...-mac-intel-app.zip` | যে ফোল্ডারে আপনি `YA-MS.app` এক্সট্র্যাক্ট করেন |

**প্রোগ্রাম ও তার `data` ফোল্ডার সর্বদা একসাথে** YA-MS ফোল্ডারে থাকে: সব তথ্য ও সেটিংস সেখানেই (কোনো AppData নয়, কোনো সিস্টেম ফোল্ডার নয়)। দেখুন [সেটিংস ও ডেটা ফোল্ডার](Settings-and-Data-Folder-bn)।

## Windows

### ইনস্টলার
1. `YA-MS-x.y.z-windows-x64-setup.exe` ডাউনলোড করে চালান।
2. **SmartScreen** যদি "Windows protected your PC" দেখায়: *More info* → *Run anyway* (প্রোগ্রামটি বাণিজ্যিক সার্টিফিকেট দিয়ে স্বাক্ষরিত নয়)।
3. YA-MS ইনস্টল হয় **`C:\YA-MS`**-এ, **অ্যাডমিনিস্ট্রেটর অধিকার ছাড়াই**, Start মেনুতে একটি আইকনসহ এবং টিক দিলে ডেস্কটপেও একটি আইকন।

### পোর্টেবল
`YA-MS-x.y.z-windows-x64-portatile.zip` যেখানে খুশি এক্সট্র্যাক্ট করুন (এমন ফোল্ডার যেখানে আপনি লিখতে পারেন, *Program Files* নয়) এবং `YA-MS.exe` চালান। পুরো ফোল্ডারটি USB স্টিক বা অন্য কম্পিউটারে কপি করা যায়।

## Linux

1. `YA-MS-x.y.z-linux-x64.tar.gz` এক্সট্র্যাক্ট করুন।
2. এক্সট্র্যাক্ট করা ফোল্ডার থেকে চালান:
   ```sh
   ./installa.sh
   ```
3. স্ক্রিপ্টটি YA-MS-কে **`~/YA-MS`**-এ কপি করে (root লাগে না) এবং অ্যাপ্লিকেশন মেনুতে **YA-MS** যোগ করে (*HamRadio* বিভাগে)। `~/YA-MS/YA-MS` দিয়েও চালু করা যায়।

### Debian প্যাকেজ (.deb)
Debian, Ubuntu, Mint ও Raspberry Pi OS-এ এর বদলে `ya-ms_x.y.z_amd64.deb` ইনস্টল করতে পারেন (Raspberry Pi-তে `_arm64.deb` / `_armhf.deb`):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
প্যাকেজটি প্রোগ্রামকে `/opt/ya-ms`-এ রাখে এবং মেনুতে **YA-MS** যোগ করে। প্রথম চালুতে (এবং প্রতিটি নতুন সংস্করণের পরে) এটি নিজেকে **`~/YA-MS`**-এ কপি করে সেখান থেকেই চলে, ফলে `data` ফোল্ডার প্রোগ্রামের পাশে থাকে এবং আপনার সেটিংস অক্ষুণ্ণ থাকে।

### পোর্টেবল
`.tar.gz` ইনস্টল না করেও চলে: যেখানে লিখতে পারেন এমন যেকোনো জায়গায় এক্সট্র্যাক্ট করে সেই ফোল্ডার থেকে `./YA-MS` চালান।

জাপানি লেখার জন্য Noto CJK ফন্ট লাগতে পারে: দেখুন [সমস্যা সমাধান](Troubleshooting-FAQ-bn#linux-জাপানি-লেখা-বাক্স-হিসেবে-দেখায়)।

## Raspberry Pi

Linux-এর মতোই প্রক্রিয়া: `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (অথবা 32-বিট Raspberry Pi OS-এ `-32bit`) এক্সট্র্যাক্ট করে এক্সট্র্যাক্ট করা ফোল্ডার থেকে `./installa.sh` চালান।

- আপনার সিস্টেম কোনটি জানতে টার্মিনালে `uname -m` লিখুন: `aarch64` → 64-বিট প্যাকেজ, `armv7l` → 32-বিট প্যাকেজ।
- সমর্থিত: Raspberry Pi 2 (কেবল 32-বিট), 3, 4, 5, 400 ও 500, Raspberry Pi OS-এর ডেস্কটপ সংস্করণসহ। **সমর্থিত নয়:** Pi Zero / Zero W ও Pi 1 (ARMv6 প্রসেসর, সেখানে .NET চলে না); Pi Zero 2 W 64-বিট প্যাকেজে চলে, তবে 512 MB RAM টানাটানি।
- কমপক্ষে 2 GB RAM-সহ Pi 4 বা 5 প্রস্তাবিত; প্রথমবার চালু হতে PC-র চেয়ে কয়েক সেকেন্ড বেশি লাগে।

## macOS

1. সঠিক ফাইল বেছে নিন: M1/M2/M3/M4 প্রসেসরের জন্য `-mac-apple-silicon.dmg`, Intel Mac-এর জন্য `-mac-intel.dmg`।
2. `.dmg` খুলুন, **"Installa YA-MS.command"-এ ডান ক্লিক → Open** করে নিশ্চিত করুন।
3. স্ক্রিপ্টটি `YA-MS.app`-কে **`~/YA-MS`**-এ কপি করে খুলে দেয়।

বিকল্পভাবে, `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip`-এ শুধু `YA-MS.app` থাকে: এটি আপনার পছন্দের কোনো ফোল্ডারে (যেখানে লিখতে পারেন) এক্সট্র্যাক্ট করুন; `data` ফোল্ডারটি `YA-MS.app`-এর পাশে তৈরি হয়। প্রথমবার: ডান ক্লিক → **Open**।

প্রোগ্রামটি Apple দ্বারা স্বাক্ষরিত নয়, তাই প্রথমবার macOS নিশ্চিতকরণ চায়; দেখুন [সমস্যা সমাধান](Troubleshooting-FAQ-bn#macos-অজ্ঞাত-ডেভেলপারের-বলে-খোলা-যাচ্ছে-না)।

## প্রথমবার চালু

- **ইউরোপের মানচিত্র** (Natural Earth-এর উপকূলরেখা ও সীমানা) প্রথমবার স্বয়ংক্রিয়ভাবে `data/mappa`-তে ডাউনলোড হয়: একবার ইন্টারনেট সংযোগ দরকার।
- **রাডারের তথ্য** (Collm, Sodankylä) সঙ্গে সঙ্গে ডাউনলোড হয়, তারপর প্রতি 5 মিনিটে পরীক্ষা করা হয়।
- ইন্টারফেস আপনার সিস্টেমের ভাষায় শুরু হয় যদি সেটি 28টি উপলব্ধ ভাষার একটি হয়, নইলে ইতালীয় ভাষায়; ডান দিকের ওপরে পরিবর্তন করুন (দেখুন [সেটিংস](Settings-and-Data-Folder-bn#ভাষা))।

## হালনাগাদ

নতুন সংস্করণ **পুরোনোটির ওপরেই** ইনস্টল করুন (একই ইনস্টলার, একই ফোল্ডার)। সেটিংস (`config.ini`), ফ্লাক্সের আর্কাইভ ও মানচিত্র `data`-তে থেকে যায়। `data/lingue`-র অনুবাদ ফাইলগুলো নতুনগুলো সাম্প্রতিকতর হলে প্রতিস্থাপিত হয়।

## সোর্স থেকে বিল্ড (কেবল ডেভেলপারদের জন্য)

ইনস্টলারগুলো GitHub Actions (`.github/workflows/build.yml`) তৈরি করে `release` শাখার প্রতিটি হালনাগাদে (সংস্করণ নেওয়া হয় `VERSION` ফাইল থেকে), যা `vX.Y.Z` রিলিজও তৈরি করে। স্থানীয়ভাবে:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # অথবা linux-x64, linux-arm64, linux-arm, osx-arm64
```

নথিগুলো আবার তৈরি করা হয় `tools/build_spiegazione.py data` ও `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` দিয়ে।

পরবর্তী: [শুরু করা](Getting-Started-bn)।
