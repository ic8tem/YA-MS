[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-BR) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · **हिन्दी** · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-TW)

# दक्षता - व्याख्या

*टैब: तकनीकी दस्तावेज़ › दक्षता - व्याख्या।*

[![दक्षता - व्याख्या](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

एक तकनीकी दस्तावेज़, *"Come YA-MS calcola l'efficienza di uno sciame"* (YA-MS किसी उल्का वर्षा की दक्षता की गणना कैसे करता है), जो प्रोग्राम के भीतर हल्के रंग के पेज के रूप में दिखता है। यह **चरण-दर-चरण** समझाता है कि दक्षता कैसे प्राप्त होती है, और हर चरण के लिए बताता है कि वह **कहाँ से आता है**। दस्तावेज़ फ़िलहाल **इतालवी में** है; यह विकि इसकी सामग्री हिंदी में [दक्षता की गणना](Efficiency-Calculation-hi#मॉडल) और [ज्यामिति और क्षीणन](Geometry-and-Path-Loss-hi) में देता है।

## लेबल

हर चरण पर एक रंगीन लेबल होता है:

| लेबल | रंग | अर्थ |
|---|---|---|
| **FONTE** (स्रोत) | नीला | चरण किसी उद्धृत स्रोत से लिया गया है; कोष्ठक की संख्या अंत की सूची को दर्शाती है |
| **RILIEVO** (जाँच) | हरा | प्रोग्राम और स्रोतों के बीच तुलना, परिणाम सहित |
| **SCELTA** (चयन) | नारंगी | प्रोग्राम का अपना चयन, किसी स्रोत से नहीं लिया गया: बैंड पर अनुभव से जाँचना है |

## अध्याय

| अध्याय | सामग्री |
|---|---|
| 1. परिचय | उद्देश्य, लेबल, दक्षता का अर्थ (OH5IY, MCG_MS; YA-MS वास्तविक पथ उपयोग करता है) |
| 2. परावर्तन कहाँ होते हैं: E परत | 80–120 km पर ट्रेल; ट्रेल ऊँचाई = Collm हिस्टोग्राम का बहुलक (जाँच: 5/11/2026 को 89.5 km) |
| 3. पथ ज्यामिति | पृथ्वी और मध्य बिंदु; ऐंटेना उन्नयन (लेख का सूत्र); साझा क्षेत्र और उसकी सीमाएँ; Hot A / Hot B; ऐंटेना लोब (DL6WU, Kraus, W4RNL) |
| 4. उल्का वर्षा का रेडिएंट | रेडिएंट की स्थिति (IMO 2026/2027), शिखर की तिथि (IMO या सौर देशांतर), गतिविधि प्रोफ़ाइल |
| 5. परावर्तन की शर्त | दर्पणी परावर्तन (McKinley), गॉसियन सहनशीलता 0.05 rad, सर्वोत्तम दिशा (SM6FHZ), DH9GCD सूत्र |
| 6. एक बिंदु से दक्षता तक | हर 15 km पर परावर्तन बिंदु, हर बिंदु का भार, प्रतिशत; QTFGUI (DJ5HG) से तुलना |
| 7. परिणाम पढ़ना | पक्ष A / B, पथ सूचकांक, रेडिएंट के रंग, PREV क्षेत्र, ऐंटेना से दिखता अनुभाग |
| 8. कार्य आवृत्ति और पथ क्षीणन | λ³ / λ² नियम, रडार से शौकिया बैंड तक, पथ क्षीणन के संदर्भ |
| 9. ज्ञात सीमाएँ | केवल अल्प-घनत्व ट्रेल, समदैशिक ऐंटेना, कार्यकारी मान |
| 10. स्रोत | 17 क्रमांकित स्रोत |

## बटन

| बटन | क्या करता है |
|---|---|
| **Word (.docx) में निर्यात करें...** | `data/efficienza_spiegazione.docx` की एक प्रति आपकी चुनी जगह सहेजता है (सुझाया गया नाम *YA-MS - calcolo dell'efficienza.docx*) |
| **Word में खोलें** | वही `.docx` Word दस्तावेज़ों के डिफ़ॉल्ट प्रोग्राम (Word, LibreOffice, …) से खोलता है |

## फ़ाइलें

| फ़ाइल | सामग्री |
|---|---|
| `data/efficienza_spiegazione.txt` | टैब में दिखाया गया पाठ, हर पंक्ति में एक ब्लॉक (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Word संस्करण |
| `doc/YA-MS_manuale_calcoli.docx` | **गणना पुस्तिका**: सभी समीकरण (Word समीकरण संपादक), क्रमांकित, अपने स्रोतों सहित |

दोनों दस्तावेज़ सोर्स से `tools/build_spiegazione.py data` और `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` द्वारा फिर से बनाए जाते हैं।
