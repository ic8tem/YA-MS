[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · **עברית** · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# איסוף נתונים

*לשונית: חי ונתונים בזמן אמת › איסוף נתונים.*

[![איסוף נתונים](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## ארבעה מקורות

הלשונית אוספת **ספוטים של פיזור מטאורי** משלושה זרמי telnet ומזרם ה-MQTT של PSKReporter, כל אחד בלשונית משנה משלו:

| לשונית משנה | ברירת מחדל | הערות |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | cluster לבחירתכם. ב-ON0DXK פסי ה-VHF מסוננים: הפעילו אותם עם `set/filter dxbm/pass 6` (ואחר כך 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (‏7000 = CW/RTTY, ‏7001 = FT8). ה-skimmers מפענחים לעיתים רחוקות אופני MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | ה-cluster של DM4X הנושא את ספוטי **PSKReporter**: פענוחי ה-MSK144 של WSJT-X ו-MSHV מגיעים לכאן. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | ספוטים חיים של PSKReporter דרך **MQTT** (שירות של M0LTE): ללא התחברות, כל ספוט כבר נושא את הלוקייטורים של התחנה המשדרת ושל התחנה הקולטת. נושאי ברירת המחדל: MSK144 ב-6 m, ‏4 m, ‏2 m, ‏1.25 m, ‏70 cm ו-FSK441 ב-2 m (`pskr/filter/v2/band/mode/#`); *נושאי ברירת המחדל* משחזר אותם. |
| **ספוטי MS שנאספו** | – | טבלת הספוטים שהתקבלו, החדשים ראשונים. |

לכל זרם יש מארח, פורט, פקודות הנשלחות אחרי ההתחברות, *התחבר מחדש*, *התחבר בהפעלה*, מסוף ושורה לשליחת פקודות. כתבו את **אות הקריאה להתחברות** למעלה. למקור ה-MQTT יש מארח, פורט, נושאים (אחד בכל שורה או מופרדים ב-`;`), *התחבר מחדש* ו-*התחבר בהפעלה* (כבוי כברירת מחדל) ומסוף עם הספוטים שהתקבלו; הספוטים שלו עוברים דרך אותו מסנן. רצועה מציגה את מצב ארבעת המקורות (נקודה ירוקה = מחובר). החיבורים נשארים פתוחים כשמחליפים שפה או ערכת צבעים.

## המסנן (40 % מהחלון)

- **מסנן מקומי אופציונלי:** שורות cluster מתחת ל-**27990.0 kHz** נדחות מיד (לא מוצגות, לא נשמרות).
- ספוטים של CW מושלכים מיד (CW או WPM בהערה, או 28000-28070 kHz): הם לא מופיעים בקונסולה ולא נשמרים, אלא אם הם מסומנים <MS>. אפשר לכבות את התיבה.

מאגר CALL3 עם הכללים של LIVETROPOVHF. „עדכן עכשיו" מוריד את CALL3.TXT מ-MMMonVHF (לפחות 100,000 שורות תקינות, הקודם נשאר ב-data/call3.bak); עם „עדכון עצמי כל 7 ימים" זה קורה בהפעלה. מעל הקובץ חלים לפי הסדר: רשומות ידניות (data/CALL3-MANUALE.TXT), תיקונים מהקלסטר (הלוקטור בן 6 התווים שהמדווח מצהיר על עצמו), קבצים שנוספו (data/CALL3-AGGIUNTE), ואחר כך CALL3.TXT ולוקטורים בני 6 תווים שנלמדו בשידור חי (data/LOC6.TXT). לוקטור שהתקבל בן 4 תווים, או שמסתיים ב-LL או MM, מוחלף בלוקטור בן 6 התווים מהמאגר; ניידים (עם לוכסן) רק ברשומה מדויקת.
- ספוטים בין תחנות במרחק של פחות מ-500 ק"מ מושלכים מיד, כי במרחק כזה הקשר ישיר או טרופוספרי ולא meteor scatter: הם לא מופיעים בקונסולה ולא נשמרים. אם חסר לוקטור, הספוט נשאר. את המרחק משנים מתחת לתיבה.
- **קריטריון 1 – תדרי MS אופייניים:** ‏50190–50300, ‏70100–70400, ‏144290–144399 kHz. ספוט בחלונות אלה מתקבל גם בלי שם האופן, אלא אם ההערה מצהירה על התפשטות אחרת: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. ניתן לערוך את החלונות ואת התגיות.
- **קריטריון 2 – אופני MS:** מחוץ לחלונות, או עם אחת מאותן תגיות, ספוט נשמר רק אם הוא מכיל **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (אופנים ספרתיים המשמשים רק ל-MS) או **\<MS\>**, באותיות גדולות, קטנות או מעורבות. ניתן לכבות, להוסיף ולהסיר מילים; לכל אחת יש מונה.
- **פסים** 28, 50, 70, 144, 222, 432 MHz; **בדיקת המסנן** על שורה מודבקת; **מונים**.

## לוקייטורים ואחסון

לוקייטורים חסרים, או בני 4 תווים בלבד, נלקחים מארכיון **CALL3** (`data/call3.txt`, קובץ JTDX, יותר ממיליון אותות קריאה), שתמיד גובר על לוקייטור בן 4 תווים. ספוטים שהתקבלו נשמרים ב-`data/spot_ms`, קובץ CSV אחד ליום, ומזינים את מפת [תעבורה בזמן אמת](Live-Traffic-he).
