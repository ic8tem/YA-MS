[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · **हिन्दी** · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# वर्ग मानचित्र

*टैब: वर्ग मानचित्र।*

[![वर्ग मानचित्र](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

आपके लॉग की ADIF फ़ाइल से पढ़े गए **संपर्कित** और **पुष्ट** Maidenhead वर्ग (4 अक्षर), यूरोप के मानचित्र पर – **हर बैंड के लिए एक उप-टैब: 50, 70, 144, 222 और 432 MHz**।

## नियंत्रण

| नियंत्रण | क्या करता है |
|---|---|
| **ADIF फ़ाइल लोड करें...** | एक `.adi` / `.adif` फ़ाइल पढ़ता है। नई ADIF पिछले डेटा को **बदल देती है**। |
| **मेमोरी साफ़ करें** | ADIF से लोड किए गए सभी वर्ग हटाता है (पुष्टि माँगता है)। |
| माउस | **व्हील = ज़ूम, खींचना = पैन, वर्ग पर माउस = QSO** (तिथि सहित अधिकतम छह कॉलसाइन, पुष्ट होने पर *(पुष्ट)*) |

लोड करने के बाद स्थिति दिखाती है *… QSO पढ़े गए, 50-432 MHz बैंडों में … QSO वर्ग, … QSO अस्वीकृत (अन्य बैंड या कोई वर्ग नहीं)*। हर बैंड मानचित्र का कैप्शन है *… वर्ग संपर्कित, … पुष्ट*।

| रंग | अर्थ |
|---|---|
| नारंगी | संपर्कित |
| हरा | पुष्ट (QSL या LoTW) |

## ADIF कैसे पढ़ी जाती है

- उपयोग किए गए फ़ील्ड: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF विनिर्देश)।
- बैंड `BAND` से, या आवृत्ति से: 50–54 MHz = 6 m, 69.9–71.5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1.25 m, 420–450 MHz = 70 cm।
- कोई वर्ग **पुष्ट** है यदि उसमें कम से कम एक QSO का `QSL_RCVD = Y` या `LOTW_QSL_RCVD = Y` हो।
- वर्ग `data/adif_quadrati.csv` में तब तक रखे जाते हैं जब तक आप दूसरी फ़ाइल लोड न करें या **मेमोरी साफ़ करें** न दबाएँ।

YA-MS LoTW से **कनेक्ट नहीं** होता: अपने लॉगिंग प्रोग्राम (या LoTW) से ADIF निर्यात करें और यहाँ लोड करें।
