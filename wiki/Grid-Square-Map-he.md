[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Ελληνικά](Grid-Square-Map-el) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · **עברית** · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [ไทย](Grid-Square-Map-th) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh) · [中文 (繁體)](Grid-Square-Map-zh-tw)

# מפת ריבועים

*לשונית: מפת ריבועים.*

[![מפת ריבועים](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

ריבועי Maidenhead (‏4 תווים) ש**בוצע** בהם קשר ושאושרו, הנקראים מקובץ ה-ADIF של הלוג שלך, על מפת אירופה – **לשונית משנה לכל פס: 50, 70, 144, 222 ו-432 MHz**.

## פקדים

| פקד | מה הוא עושה |
|---|---|
| **טען קובץ ADIF...** | קורא קובץ `.adi` / `.adif`. קובץ ADIF חדש **מחליף** את הנתונים הקודמים. |
| **נקה זיכרון** | מוחק את כל הריבועים שנטענו מ-ADIF (מבקש אישור). |
| עכבר | **גלגלת = זום, גרירה = הזזה, עכבר מעל ריבוע = QSO** (עד שישה אותות קריאה עם תאריך, *(מאושר)* כשאושר) |

לאחר הטעינה, המצב מציג *… QSO נקראו, … ריבועי QSO בפסים 50-432 MHz, … QSO נדחו (פסים אחרים או ללא ריבוע)*. לכל מפת פס יש הכיתוב *… ריבועים בוצעו, … מאושרים*.

| צבע | משמעות |
|---|---|
| כתום | בוצע קשר |
| ירוק | מאושר (QSL או LoTW) |

## איך נקרא קובץ ה-ADIF

- שדות בשימוש: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (מפרט ADIF).
- הפס מתוך `BAND`, או מהתדר: 50–54 MHz = 6 m, ‏69.9–71.5 MHz = 4 m, ‏144–148 MHz = 2 m, ‏219–225 MHz = 1.25 m, ‏420–450 MHz = 70 cm.
- ריבוע **מאושר** אם לפחות QSO אחד בו מכיל `QSL_RCVD = Y` או `LOTW_QSL_RCVD = Y`.
- הריבועים נשמרים ב-`data/adif_quadrati.csv` עד שתטענו קובץ אחר או תלחצו **נקה זיכרון**.

YA-MS **אינה** מתחברת ל-LoTW: ייצאו את ה-ADIF מתוכנת הלוג שלכם (או מ-LoTW) וטענו אותו כאן.
