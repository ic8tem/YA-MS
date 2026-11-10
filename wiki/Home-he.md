[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-BR) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · **עברית** · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-TW)

# YA-MS – תחזיות פיזור מטאורי ויעילות מטרים בזמן אמת

*מאת Costantino Cerrotta IC8TEM*

**YA-MS** היא תוכנה חינמית לחובבי רדיו העובדים ב**פיזור מטאורי (meteor scatter, MS) ב-50, 70, 144, 222 ו-432 MHz**. עבור הנתיב האמיתי בין הלוקייטור שלך לזה של תחנת ה-DX, היא מחשבת שעה אחר שעה עד כמה כל מטר מטאורים פעיל מסייע לנתיב (ה**יעילות** שלו), מאיזה צד של הנתיב מגיעות ההחזרות (**Hot A / Hot B**), לאן לכוון את האנטנה, ותחזית ניסיונית של מספר ההחזרות לשעה הנגזרת מ**מכ״ם מטאורים בזמן אמת** (Collm, גרמניה). היא פועלת ב-**Windows, Linux, Raspberry Pi ו-macOS** (.NET 8 + Avalonia), בממשק ב-36 שפות.

המקור העיקרי הוא המאמר של **C. Cerrotta IC8TEM ו-G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (גרסה 7). כל נוסחה וכל נתון בתוכנה מציינים את מקורם; ראו [מקורות](Sources-he).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="כיפת השמיים"></a><br><sub>כיפת השמיים</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="חישוב היעילות"></a><br><sub>חישוב היעילות</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="מכ״ם GRAVES"></a><br><sub>מכ״ם GRAVES</sub></td>
</tr></table>

## למי היא מיועדת

- למפעילים שרוצים לדעת **מתי** נתיב פיזור מטאורי פתוח ו**לאן** לכוון, מעבר לאמירה הכללית "שיא המטר הוא הלילה".
- לתחנות העובדות ב**נתיבים ארוכים ב-144 וב-432 MHz**, שבהם מיקום הרדיאנט קובע אם מטר מועיל או חסר תועלת.
- לכל מי שרוצה **לבדוק את המספרים**: מדריך החישובים וההסבר שבתוך התוכנה מציגים כל שלב עם מקורו: מקור שפורסם, בדיקה שנעשתה על התוכנה, או בחירה של התוכנה.

## הלשוניות

מאז גרסה 1.6 ללשוניות הראשיות יש **לשוניות משנה** (שורה בהירה יותר מתחת לשורה הראשית). בעת ההפעלה מוצג למשך 5 שניות מסך פתיחה עם מטר הפרסאידים מעל ה-VLT של ESO (צילום ESO/S. Guisard, CC BY 4.0).

| לשונית | לשונית משנה | מה היא מציגה |
|---|---|---|
| **חי ונתונים בזמן אמת** | [תעבורה בזמן אמת](Live-Traffic-he) | מפה אזימוטלית של כל תעבורת ה-MS שנאספה, עם ענן השובלים הסבירים ביותר לכל קשר, צבעי פסים, ספוטים חדשים מהבהבים |
| | [שטף מכ״ם](Radar-Flux-he) | ספירות מטאורים שעתיות וגובהי שובלים הנקראים ממכ״ם ה-SKiYMET ב-Collm, תמונת Sodankylä, הערכה עבור הפס שלך |
| | [מכ״ם GRAVES](GRAVES-Radar-he) | נתיב הפיזור הקדמי GRAVES → אליך: האזור השימושי באלומה, גזרה וצעד, המעבר הבא של האלומה, איך להאזין |
| | [איסוף נתונים](Data-Collection-he) | שלושה זרמי cluster ב-telnet (DX cluster, RBN, DM4X/PSKReporter) ומסנן ספוטי ה-MS |
| **חישוב תחזית** | [חישוב תחזית](Sky-View-he) | מפת מבט על של הנתיב עם Hot A / Hot B, אונת האנטנה, אזורי PREV והיסחפות המטרים; רשימת מטרים; כיפת שמיים קטנה עם הרדיאנטים וכיווני האנטנה הנכונים; חתך כפי שנראה מהאנטנה |
| | [גאומטריה והנחתה](Geometry-and-Path-Loss-he) | מרחק, נקודת אמצע, הגבהה, Hot A / Hot B, גבולות האזור המשותף, הנחתת נתיב 28–432 MHz, מאזן קישור, אנטנה |
| | [חישוב היעילות](Efficiency-Calculation-he) | כרטיסי סקירה מהירה, יעילות שעתית של כל מטר עם צד A/B, מדד נתיב, השוואה ל-DH9GCD, גרף |
| | [תחזיות ניסיוניות](Experimental-Forecasts-he) | שטף Collm מותאם ל-144 MHz (או לכל תדר) עם λ^k ומקדם התחנה K, תחזית ל-24 שעות, השוואה ל-RMOB |
| **מסמכים טכניים** | [מקורות](Sources-he) | כל המקורות; העיקרי הוא מאמר Cerrotta–Sartori |
| | [מפת המכ״מים האירופיים](European-Radar-Map-he) | היכן נמצאים Collm, Sodankylä, GRAVES ו-CMOR ביחס לתחנה שלך |
| | [יעילות - הסבר](Efficiency-Explanation-he) | מסמך המסביר צעד אחר צעד כיצד מחושבת היעילות, ניתן לייצוא ל-Word |
| [מטרים בזמן אמת](Live-Showers-he) | – | ZHR נמדד של Global Meteor Network ומפות רדיאנטים של CMOR |
| [מטרים](Showers-he) | – | קטלוג IMO עם השיא הבא (תאריך ושעה של IMO או מחושבים) |
| [מפת ריבועים](Grid-Square-Map-he) | – | ריבועי Maidenhead שבוצע בהם קשר ושאושרו, מתוך קובץ ADIF, לשונית לכל פס |

מעל הלשוניות יש שלוש שורות של פקדים (הלוקייטור שלך, תחנת DX, פס, אנטנה, גובה שובלים, שעה); ראו [צעדים ראשונים](Getting-Started-he). הכפתור **פקדים** מקפל אותן, והשפה וערכת הצבעים נבחרות בפינה הימנית העליונה; ראו [הגדרות ותיקיית נתונים](Settings-and-Data-Folder-he).

## בקצרה

- **נתיב אמיתי, לא כיוונים קבועים**: היעילות מחושבת עבור נתיב המעגל הגדול בין שני הלוקייטורים (תוכנות ישנות יותר השתמשו בארבעה כיוונים קבועים).
- **מודל החזרה ספקולרית** (McKinley) על נקודות בשכבת E כל 15 km, עם גובה השובלים הנקרא בזמן אמת ממכ״ם Collm.
- **Hot A / Hot B** במרחק 150 km משני צידי נקודת האמצע (ניתן לכוונון 30–400 km), המומלצת באדום, ואלו שכבר נמצאות בתוך אונת האנטנה שלך באפור.
- **מכ״ם בזמן אמת**: Collm נבדק כל 5 דקות, ורק מקורות שהשתנו מורדים מחדש; ללא חיבור התוכנה ממשיכה לעבוד עם הנתונים האחרונים שנשמרו.
- תחזית **ניסיונית** ב-50/144/432 MHz עם כלל ה-λ³ של SM6FHZ, ניתנת להשוואה לצופי RMOB.
- הכול בתיקיית **`data`** אחת ליד התוכנה: בלי AppData, בלי תיקיות מערכת.

> היעילות היא מודל ניסיוני (החזרה ספקולרית + שובלים תת-צפופים). השוו אותה ל-MCG_MS, ל-MS-Soft ולניסיון שלכם באוויר.

## מאיפה להתחיל

1. [התקנה](Installation-he)
2. [צעדים ראשונים](Getting-Started-he)
3. [פתרון תקלות ושאלות נפוצות](Troubleshooting-FAQ-he) אם משהו לא עובד.

הורדות: **[Releases](https://github.com/ic8tem/YA-MS/releases)** ב-GitHub.
