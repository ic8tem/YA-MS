[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · **עברית** · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh)

# איסוף נתונים

*לשונית: חי ונתונים בזמן אמת › איסוף נתונים.*

[![איסוף נתונים](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## שלושה זרמי cluster

הלשונית אוספת **ספוטים של פיזור מטאורי** משלושה זרמי telnet, כל אחד בלשונית משנה משלו:

| לשונית משנה | ברירת מחדל | הערות |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | cluster לבחירתכם. ב-ON0DXK פסי ה-VHF מסוננים: הפעילו אותם עם `set/filter dxbm/pass 6` (ואחר כך 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (‏7000 = CW/RTTY, ‏7001 = FT8). ה-skimmers מפענחים לעיתים רחוקות אופני MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | ה-cluster של DM4X הנושא את ספוטי **PSKReporter**: פענוחי ה-MSK144 של WSJT-X ו-MSHV מגיעים לכאן. |
| **ספוטי MS שנאספו** | – | טבלת הספוטים שהתקבלו, החדשים ראשונים. |

לכל זרם יש מארח, פורט, פקודות הנשלחות אחרי ההתחברות, *התחבר מחדש*, *התחבר בהפעלה*, מסוף ושורה לשליחת פקודות. כתבו את **אות הקריאה להתחברות** למעלה. רצועה מציגה את מצב שלושת החיבורים (נקודה ירוקה = מחובר). החיבורים נשארים פתוחים כשמחליפים שפה או ערכת צבעים.

## המסנן (40 % מהחלון)

- **מסנן מקומי אופציונלי:** שורות cluster מתחת ל-**27990.0 kHz** נדחות מיד (לא מוצגות, לא נשמרות).
- **קריטריון 1 – תדרי MS אופייניים:** ‏50190–50300, ‏70100–70400, ‏144290–144399 kHz. ספוט בחלונות אלה מתקבל גם בלי שם האופן, אלא אם ההערה מצהירה על התפשטות אחרת: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. ניתן לערוך את החלונות ואת התגיות.
- **קריטריון 2 – אופני MS:** מחוץ לחלונות, או עם אחת מאותן תגיות, ספוט נשמר רק אם הוא מכיל **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (אופנים ספרתיים המשמשים רק ל-MS) או **\<MS\>**, באותיות גדולות, קטנות או מעורבות. ניתן לכבות, להוסיף ולהסיר מילים; לכל אחת יש מונה.
- **פסים** 28, 50, 70, 144, 222, 432 MHz; **בדיקת המסנן** על שורה מודבקת; **מונים**.

## לוקייטורים ואחסון

לוקייטורים חסרים, או בני 4 תווים בלבד, נלקחים מארכיון **CALL3** (`data/call3.txt`, קובץ JTDX, יותר ממיליון אותות קריאה), שתמיד גובר על לוקייטור בן 4 תווים. ספוטים שהתקבלו נשמרים ב-`data/spot_ms`, קובץ CSV אחד ליום, ומזינים את מפת [תעבורה בזמן אמת](Live-Traffic-he).
