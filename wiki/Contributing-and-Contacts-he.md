[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · **עברית** · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [ไทย](Contributing-and-Contacts-th) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# תרומה ויצירת קשר

YA-MS משתפרת בזכות הדיווחים של מי שמשתמשים בה באוויר. כל תיקון מיוחס למקורו.

## יצירת קשר

| | |
|---|---|
| מחבר | Costantino Cerrotta **IC8TEM** |
| דוא״ל | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## דיווח על בעיה

פתחו **issue ב-GitHub** או כתבו דוא״ל עם:

- מערכת ההפעלה וגרסת YA-MS (בכותרת החלון);
- שני הלוקייטורים, הפס ושעת UTC;
- מה ציפיתם ומה ראיתם (צילום מסך עוזר);
- לבעיות מכ״ם, ההודעה המוצגת בלשונית [שטף מכ״ם](Radar-Flux-he).

## מה מועיל במיוחד

- **דיווחים מהאוויר.** שעות ונתיבים שבהם היעילות או התחזית היו נכונות – או שגויות. המודל ניסיוני ודורש השוואה עם קשרי QSO אמיתיים ועם MCG_MS / MS-Soft.
- **השוואות ל-RMOB.** ערכי מקדם התחנה K והמעריך k שמצאתם בעזרת [ההשוואה ל-RMOB](Experimental-Forecasts-he#השוואה-ל-rmob), עם הפס והתחנה שלכם.
- **נתונים עם מקור.** היסחפויות רדיאנט טובות יותר, פרופילי פעילות, תאריכי שיא חדשים של IMO ‏(`data/massimi_imo.csv`), נתוני אנטנות: צרפו את המקור והוא יצוטט.
- **שינויים בגרפי המכ״ם.** אם תבנית הגרף של Collm משתנה, עותק של התמונה (`data/radar/`) עוזר לכייל מחדש את הקריאה.

## תרגומים

תרגומי הממשק הם קובצי טקסט פשוטים ב-**`data/lingue/<code>.txt`** ‏(UTF-8) ו**כל אחד יכול לתקן אותם**:

```
<Italian text><TAB><translation>
```

- רשומה אחת בכל שורה; שורות המתחילות ב-`#` הן הערות.
- בשתי העמודות שני התווים `\n` פירושם מעבר שורה.
- שמרו על מצייני המקום `{0}`, `{1}`, … עם התבנית שלהם (למשל `{0:F1}`, `{3:+0;-0}`), בסדר שהשפה שלכם צריכה.
- רשומות חסרות או ריקות מוצגות באיטלקית. רשימת כל המפתחות היא `data/lingue/chiavi.txt` (נוצרת על ידי `tools/estrai_chiavi.py`, אין לערוך אותה).

ערכו את הקובץ בתיקייה `data/lingue` של ההתקנה שלכם והפעילו מחדש את YA-MS (או החליפו שפה) כדי לראות את התוצאה. מאחר שקבצים אלה **מוחלפים בגרסאות חדשות יותר בכל עדכון**, אנא גם **שלחו את התיקונים שלכם** – בדוא״ל או כ-pull request ב-GitHub ‏(`data/lingue/`) – כדי שייכנסו לגרסה הבאה.

ויקי זו קיימת ב-36 שפות (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, ไทย, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文, 中文 (繁體)); גם תיקונים לדפי הוויקי יתקבלו בברכה.
