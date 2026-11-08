**English** · [Русский](Installation-ru) · [Deutsch](Installation-de) · [日本語](Installation-ja)

# इंस्टॉलेशन

सभी पैकेज **[Releases](https://github.com/ic8tem/YA-MS/releases)** पेज पर हैं (नीचे के फ़ाइल नामों में `x.y.z` संस्करण है, उदा. `1.2.0`)। कुछ भी कंपाइल करने की ज़रूरत नहीं और कुछ और इंस्टॉल करने की भी नहीं: हर पैकेज में .NET 8 रनटाइम शामिल है।

| सिस्टम | फ़ाइल | कहाँ इंस्टॉल होता है |
|---|---|---|
| Windows (64-बिट) | `YA-MS-x.y.z-windows-x64-setup.exe` (इंस्टॉलर) | `C:\YA-MS` |
| Windows (64-बिट), पोर्टेबल | `YA-MS-x.y.z-windows-x64-portatile.zip` | कोई भी फ़ोल्डर जहाँ आप लिख सकते हैं |
| Windows (32-बिट, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` या `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-बिट) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-बिट) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-बिट) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

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

प्रोग्राम Apple द्वारा हस्ताक्षरित नहीं है, इसलिए पहली बार macOS पुष्टि माँगता है; देखें [समस्या निवारण](Troubleshooting-FAQ-hi#macos-अज्ञात-डेवलपर-का-होने-के-कारण-नहीं-खुलता)।

## पहली बार शुरू करना

- **यूरोप का मानचित्र** (Natural Earth की तटरेखाएँ और सीमाएँ) पहली बार अपने आप `data/mappa` में डाउनलोड होता है: इंटरनेट कनेक्शन एक बार चाहिए।
- **रडार डेटा** (Collm, Sodankylä) तुरंत डाउनलोड होता है और फिर हर 5 मिनट में जाँचा जाता है।
- यदि आपकी सिस्टम भाषा छह उपलब्ध भाषाओं में से एक है तो इंटरफ़ेस उसी में शुरू होता है, अन्यथा इतालवी में; इसे ऊपर दाईं ओर बदलें (देखें [सेटिंग्स](Settings-and-Data-Folder-hi#भाषा))।

## अपडेट करना

नया संस्करण **पुराने के ऊपर ही** इंस्टॉल करें (वही इंस्टॉलर, वही फ़ोल्डर)। सेटिंग्स (`config.ini`), फ्लक्स संग्रह और मानचित्र `data` में बने रहते हैं। `data/lingue` की अनुवाद फ़ाइलें तब बदल दी जाती हैं जब नई फ़ाइलें अधिक हाल की हों।

## सोर्स से बिल्ड करना (केवल डेवलपरों के लिए)

इंस्टॉलर GitHub Actions (`.github/workflows/build.yml`) द्वारा `release` ब्रांच के हर अपडेट पर बनाए जाते हैं (संस्करण `VERSION` फ़ाइल से लिया जाता है), जो रिलीज़ `vX.Y.Z` भी बनाता है। स्थानीय रूप से:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # या linux-x64, linux-arm64, linux-arm, osx-arm64
```

दस्तावेज़ `tools/build_spiegazione.py data` और `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` से फिर से बनाए जाते हैं।

आगे: [शुरुआत](Getting-Started-hi)।
