[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-BR) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · **हिन्दी** · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-TW)

# डेटा संग्रह

*टैब: लाइव और रियल-टाइम डेटा › डेटा संग्रह।*

[![डेटा संग्रह](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## चार स्रोत

यह टैब तीन टेलनेट स्ट्रीमों और PSKReporter की MQTT फ़ीड से **मीटियोर स्कैटर स्पॉट** एकत्र करता है, हर एक अपने उप-टैब में:

| उप-टैब | डिफ़ॉल्ट | टिप्पणी |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | आपकी पसंद का क्लस्टर। ON0DXK पर VHF बैंड फ़िल्टर किए जाते हैं: उन्हें `set/filter dxbm/pass 6` (फिर 4, 2…) से सक्रिय करें। |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8)। स्किमर MS मोड शायद ही डिकोड करते हैं। |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X का क्लस्टर जो **PSKReporter** के स्पॉट लाता है: WSJT-X और MSHV के MSK144 डिकोड यहाँ आते हैं। |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | **MQTT** के ज़रिए PSKReporter के लाइव स्पॉट (M0LTE की सेवा): कोई लॉगिन नहीं, हर स्पॉट में पहले से ही प्रेषक और प्राप्तकर्ता स्टेशन के लोकेटर होते हैं। डिफ़ॉल्ट टॉपिक: 6 m, 4 m, 2 m, 1.25 m, 70 cm पर MSK144 और 2 m पर FSK441 (`pskr/filter/v2/band/mode/#`); *डिफ़ॉल्ट टॉपिक* इन्हें बहाल करता है। |
| **एकत्रित MS स्पॉट** | – | स्वीकृत स्पॉट की तालिका, नवीनतम पहले। |

हर स्ट्रीम में होस्ट, पोर्ट, लॉगिन के बाद भेजे जाने वाले कमांड, *पुनः कनेक्ट करें*, *आरंभ पर कनेक्ट करें*, एक कंसोल और कमांड भेजने की एक पंक्ति है। ऊपर अपना **लॉगिन के लिए कॉलसाइन** लिखें। MQTT स्रोत में होस्ट, पोर्ट, टॉपिक (हर पंक्ति में एक या `;` से अलग), *पुनः कनेक्ट करें* और *आरंभ पर कनेक्ट करें* (डिफ़ॉल्ट रूप से बंद) और प्राप्त स्पॉट वाला एक कंसोल है; इसके स्पॉट भी उसी फ़िल्टर से गुज़रते हैं। एक पट्टी चारों स्रोतों की स्थिति दिखाती है (हरा बिंदु = कनेक्टेड)। भाषा या रंग योजना बदलने पर सत्र खुले रहते हैं।

## फ़िल्टर (विंडो का 40 %)

- **वैकल्पिक स्थानीय फ़िल्टर:** **27990.0 kHz** से नीचे की क्लस्टर पंक्तियाँ तुरंत हटा दी जाती हैं (न दिखाई जाती हैं, न सहेजी जाती हैं)।
- **पहला मानदंड – सामान्य MS आवृत्तियाँ:** 50190–50300, 70100–70400, 144290–144399 kHz। इन विंडो में आया स्पॉट मोड का नाम न होने पर भी स्वीकार होता है, जब तक टिप्पणी कोई और प्रसार घोषित न करे: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`। विंडो और टैग संपादित किए जा सकते हैं।
- **दूसरा मानदंड – MS मोड:** विंडो के बाहर, या इनमें से किसी टैग के साथ, स्पॉट तभी रखा जाता है जब उसमें **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (केवल MS के लिए उपयोग होने वाले डिजिटल मोड) या **\<MS\>** हो, बड़े, छोटे या मिले-जुले अक्षरों में। शब्द बंद किए, जोड़े और हटाए जा सकते हैं; हर एक का अपना काउंटर है।
- **बैंड** 28, 50, 70, 144, 222, 432 MHz; चिपकाई गई पंक्ति पर **फ़िल्टर परीक्षण**; **काउंटर**।

## लोकेटर और भंडारण

अनुपस्थित लोकेटर, या केवल 4 अक्षरों वाले लोकेटर, **CALL3** संग्रह (`data/call3.txt`, JTDX फ़ाइल, दस लाख से अधिक कॉलसाइन) से लिए जाते हैं, जो 4-अक्षर लोकेटर पर हमेशा प्राथमिकता पाता है। स्वीकृत स्पॉट `data/spot_ms` में सहेजे जाते हैं, हर दिन एक CSV फ़ाइल, और [लाइव ट्रैफ़िक](Live-Traffic-hi) मानचित्र को डेटा देते हैं।
