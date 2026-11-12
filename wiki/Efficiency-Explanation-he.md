[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · **עברית** · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# הסבר חישוב היעילות

*לשונית: מסמכים טכניים › הסבר חישוב היעילות.*

[![הסבר חישוב היעילות](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

מסמך טכני, *"Come YA-MS calcola l'efficienza di uno sciame"* (איך YA-MS מחשבת את היעילות של מטר), המוצג בתוך התוכנה כדף בהיר. הוא מסביר **צעד אחר צעד** כיצד מתקבלת היעילות, ומציין לכל צעד **מאין הוא בא**. התוכנה מציגה אותו **בשפת הממשק** (בכל 36 השפות), וכך גם את מדריך החישובים; ויקי זו מביאה את תוכנו גם ב[חישוב היעילות](Efficiency-Calculation-he#המודל) וב[גאומטריה והנחתה](Geometry-and-Path-Loss-he).

## תוויות

כל צעד נושא תווית צבעונית:

| תווית | צבע | משמעות |
|---|---|---|
| **FONTE** (מקור) | כחול | הצעד מאמץ מקור מצוטט; המספר בסוגריים מפנה לרשימה שבסוף |
| **RILIEVO** (בדיקה) | ירוק | השוואה בין התוכנה למקורות, עם התוצאה |
| **SCELTA** (בחירה) | כתום | בחירה של התוכנה, שלא נלקחה ממקור: יש לבדוק אותה בניסיון באוויר |

## פרקים

| פרק | תוכן |
|---|---|
| 1. מבוא | מטרה, תוויות, מה פירוש יעילות (OH5IY, ‏MCG_MS; ‏YA-MS משתמשת בנתיב האמיתי) |
| 2. היכן מתרחשות ההחזרות: שכבת E | שובלים ב-80–120 km; גובה השובלים = השכיח של ההיסטוגרמה של Collm (בדיקה: 89.5 km ב-5/11/2026) |
| 3. גאומטריית הנתיב | כדור הארץ ונקודת האמצע; הגבהת האנטנה (נוסחת המאמר); האזור המשותף וגבולותיו; Hot A / Hot B; אונת האנטנה (DL6WU, ‏Kraus, ‏W4RNL) |
| 4. הרדיאנט של המטר | מיקום הרדיאנט (IMO 2026/2027), תאריך השיא (IMO או אורך שמשי), פרופיל הפעילות |
| 5. תנאי ההחזרה | החזרה ספקולרית (McKinley), סובלנות גאוסית 0.05 rad, כיוון מיטבי (SM6FHZ), נוסחת DH9GCD |
| 6. מנקודה אחת ליעילות | נקודות החזרה כל 15 km, משקל כל נקודה, אחוז; השוואה ל-QTFGUI ‏(DJ5HG) |
| 7. קריאת התוצאות | צד A / B, מדד נתיב, צבעי הרדיאנטים, אזורי PREV, חתך כפי שנראה מהאנטנה |
| 8. תדר עבודה והנחתת נתיב | כללי λ³ / λ², מהמכ״ם לפס החובבים, מקורות להנחתת נתיב |
| 9. מגבלות ידועות | שובלים תת-צפופים בלבד, אנטנות איזוטרופיות (באזימוט; דיאגרמה אנכית לבחירה), ערכי עבודה |
| 10. מקורות | 17 מקורות ממוספרים |

## כפתורים

| כפתור | מה הוא עושה |
|---|---|
| **ייצא ל-Word (.docx)...** | שומר עותק של `data/efficienza_spiegazione.docx` היכן שתבחרו (שם מוצע *YA-MS - calcolo dell'efficienza.docx*) |
| **פתח ב-Word** | פותח את אותו `.docx` בתוכנת ברירת המחדל למסמכי Word ‏(Word, ‏LibreOffice, …) |

## קבצים

| קובץ | תוכן |
|---|---|
| `data/efficienza_spiegazione.txt` | הטקסט המוצג בלשונית, בלוק אחד לכל שורה (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | גרסת ה-Word |
| `data/spiegazione/efficienza_spiegazione_<code>.txt` / `.docx` | אותו מסמך ב-35 השפות האחרות (למשל `_en`, `_de`, `_pt-br`) |
| `doc/YA-MS_manuale_calcoli.docx` | **מדריך החישובים** (איטלקית): כל המשוואות (עורך המשוואות של Word), ממוספרות, עם מקורותיהן |
| `doc/manuali/YA-MS_manuale_calcoli_<code>.docx` | מדריך החישובים ב-35 השפות האחרות |

שני המסמכים נוצרים מחדש מהמקור עם `tools/build_spiegazione.py data [code]` ו-`node tools/build_manuale.js <file.docx> [code]`. התרגומים נמצאים ב-`tools/traduzioni_doc/` (`tools/build_documenti.sh` בונה מחדש את כל השפות).
