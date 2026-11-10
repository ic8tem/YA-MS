[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-BR) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · **हिन्दी** · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-TW)

# इंस्टॉलेशन

सभी पैकेज **[Releases](https://github.com/ic8tem/YA-MS/releases)** पेज पर हैं (नीचे के फ़ाइल नामों में `x.y.z` संस्करण है, उदा. `1.2.0`)। कुछ भी कंपाइल करने की ज़रूरत नहीं और कुछ और इंस्टॉल करने की भी नहीं: हर पैकेज में .NET 8 रनटाइम शामिल है।

| सिस्टम | फ़ाइल | कहाँ इंस्टॉल होता है |
|---|---|---|
| Windows (64-बिट) | `YA-MS-x.y.z-windows-x64-setup.exe` (इंस्टॉलर) | `C:\YA-MS` |
| Windows (64-बिट), पोर्टेबल | `YA-MS-x.y.z-windows-x64-portatile.zip` | कोई भी फ़ोल्डर जहाँ आप लिख सकते हैं |
| Windows (32-बिट, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` या `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-बिट): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (पहली बार शुरू करने पर वहाँ कॉपी होता है) |
| Linux (64-बिट), कोई भी डिस्ट्रीब्यूशन | `YA-MS-x.y.z-linux-x64.tar.gz` (पोर्टेबल या `./installa.sh` के साथ) | `~/YA-MS` या कोई भी फ़ोल्डर |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-बिट) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-बिट) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian पैकेज | `ya-ms_x.y.z_arm64.deb` (64-बिट) या `ya-ms_x.y.z_armhf.deb` (32-बिट) | `~/YA-MS` (पहली बार शुरू करने पर वहाँ कॉपी होता है) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, केवल एप्लिकेशन | `YA-MS-x.y.z-mac-apple-silicon-app.zip` या `...-mac-intel-app.zip` | वह फ़ोल्डर जहाँ आप `YA-MS.app` निकालते हैं |

**प्रोग्राम और उसका `data` फ़ोल्डर हमेशा साथ रहते हैं**, YA-MS फ़ोल्डर में: सारा डेटा और सारी सेटिंग्स वहीं हैं (न AppData, न सिस्टम फ़ोल्डर)। देखें [सेटिंग्स और डेटा फ़ोल्डर](Settings-and-Data-Folder-hi)।

## Windows

### इंस्टॉलर
1. `YA-MS-x.y.z-windows-x64-setup.exe` डाउनलोड करें और चलाएँ।
2. यदि **SmartScreen** "Windows protected your PC" दिखाए: *More info* → *Run anyway* (प्रोग्राम किसी व्यावसायिक प्रमाणपत्र से हस्ताक्षरित नहीं है)।
3. YA-MS **`C:\YA-MS`** में इंस्टॉल होता है, **बिना एडमिनिस्ट्रेटर अधिकारों के**, Start मेनू आइकन के साथ और, यदि आप चुनें, डेस्कटॉप आइकन के साथ।

### पोर्टेबल
`YA-MS-x.y.z-windows-x64-portatile.zip` को अपनी पसंद की जगह निकालें (ऐसा फ़ोल्डर जहाँ आप लिख सकें, *Program Files* नहीं) और `YA-MS.exe` चलाएँ। पूरे फ़ोल्डर को USB स्टिक या दूसरे कंप्यूटर पर कॉपी किया जा सकता है।

## Linux

1. `YA-MS-x.y.z-linux-x64.tar.gz` को निकालें।
2. निकाले गए फ़ोल्डर से चलाएँ:
   ```sh
   ./installa.sh
   ```
3. स्क्रिप्ट YA-MS को **`~/YA-MS`** में कॉपी करती है (root की ज़रूरत नहीं) और **YA-MS** को एप्लिकेशन मेनू में जोड़ती है (श्रेणी *HamRadio*)। आप इसे `~/YA-MS/YA-MS` से भी चला सकते हैं।

### Debian पैकेज (.deb)
Debian, Ubuntu, Mint और Raspberry Pi OS पर आप इसके बजाय `ya-ms_x.y.z_amd64.deb` इंस्टॉल कर सकते हैं (Raspberry Pi पर `_arm64.deb` / `_armhf.deb`):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
पैकेज प्रोग्राम को `/opt/ya-ms` में रखता है और **YA-MS** को मेनू में जोड़ता है। पहली बार शुरू करने पर (और हर नए संस्करण के बाद) यह खुद को **`~/YA-MS`** में कॉपी करता है और वहीं से चलता है, ताकि `data` फ़ोल्डर प्रोग्राम के साथ रहे और आपकी सेटिंग्स बनी रहें।

### पोर्टेबल
`.tar.gz` बिना इंस्टॉल किए भी काम करता है: इसे किसी भी ऐसी जगह निकालें जहाँ आप लिख सकें और उसी फ़ोल्डर से `./YA-MS` चलाएँ।

जापानी पाठ के लिए Noto CJK फ़ॉन्ट की ज़रूरत पड़ सकती है: देखें [समस्या निवारण](Troubleshooting-FAQ-hi#linux-जापानी-पाठ-बक्सों-के-रूप-में-दिखता-है)।

## Raspberry Pi

प्रक्रिया Linux जैसी ही है: `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (या 32-बिट Raspberry Pi OS पर `-32bit`) निकालें और निकाले गए फ़ोल्डर से `./installa.sh` चलाएँ।

- आपका सिस्टम कौन-सा है, यह जानने के लिए टर्मिनल में `uname -m` लिखें: `aarch64` → 64-बिट पैकेज, `armv7l` → 32-बिट पैकेज।
- समर्थित: Raspberry Pi 2 (केवल 32-बिट), 3, 4, 5, 400 और 500, Raspberry Pi OS के डेस्कटॉप संस्करण के साथ। **समर्थित नहीं:** Pi Zero / Zero W और Pi 1 (ARMv6 प्रोसेसर, उन पर .NET नहीं चलता); Pi Zero 2 W 64-बिट पैकेज के साथ चलता है, पर 512 MB RAM कम पड़ती है।
- कम से कम 2 GB RAM वाला Pi 4 या 5 अनुशंसित है; पहली बार शुरू होने में PC की तुलना में कुछ सेकंड अधिक लगते हैं।

## macOS

1. सही फ़ाइल चुनें: M1/M2/M3/M4 प्रोसेसर के लिए `-mac-apple-silicon.dmg`, Intel Mac के लिए `-mac-intel.dmg`।
2. `.dmg` खोलें, **"Installa YA-MS.command" पर दायाँ क्लिक → Open** करें और पुष्टि करें।
3. स्क्रिप्ट `YA-MS.app` को **`~/YA-MS`** में कॉपी करके खोल देती है।

वैकल्पिक रूप से, `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` में केवल `YA-MS.app` होता है: इसे अपनी पसंद के किसी फ़ोल्डर में निकालें (जहाँ आप लिख सकें); `data` फ़ोल्डर `YA-MS.app` के बगल में बनता है। पहली बार: दायाँ क्लिक → **Open**।

प्रोग्राम Apple द्वारा हस्ताक्षरित नहीं है, इसलिए पहली बार macOS पुष्टि माँगता है; देखें [समस्या निवारण](Troubleshooting-FAQ-hi#macos-अज्ञात-डेवलपर-का-होने-के-कारण-नहीं-खुलता)।

## पहली बार शुरू करना

- **यूरोप का मानचित्र** (Natural Earth की तटरेखाएँ और सीमाएँ) पहली बार अपने आप `data/mappa` में डाउनलोड होता है: इंटरनेट कनेक्शन एक बार चाहिए।
- **रडार डेटा** (Collm, Sodankylä) तुरंत डाउनलोड होता है और फिर हर 5 मिनट में जाँचा जाता है।
- यदि आपकी सिस्टम भाषा 36 उपलब्ध भाषाओं में से एक है तो इंटरफ़ेस उसी में शुरू होता है, अन्यथा इतालवी में; इसे ऊपर दाईं ओर बदलें (देखें [सेटिंग्स](Settings-and-Data-Folder-hi#भाषा))।

## अपडेट करना

नया संस्करण **पुराने के ऊपर ही** इंस्टॉल करें (वही इंस्टॉलर, वही फ़ोल्डर)। सेटिंग्स (`config.ini`), फ्लक्स संग्रह और मानचित्र `data` में बने रहते हैं। `data/lingue` की अनुवाद फ़ाइलें तब बदल दी जाती हैं जब नई फ़ाइलें अधिक हाल की हों।

## सोर्स से बिल्ड करना (केवल डेवलपरों के लिए)

इंस्टॉलर GitHub Actions (`.github/workflows/build.yml`) द्वारा `release` ब्रांच के हर अपडेट पर बनाए जाते हैं (संस्करण `VERSION` फ़ाइल से लिया जाता है), जो रिलीज़ `vX.Y.Z` भी बनाता है। स्थानीय रूप से:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # या linux-x64, linux-arm64, linux-arm, osx-arm64
```

दस्तावेज़ (सभी भाषाओं में) `tools/build_documenti.sh` से फिर से बनाए जाते हैं।

आगे: [शुरुआत](Getting-Started-hi)।
