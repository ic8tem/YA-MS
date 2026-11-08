[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · **עברית** · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh)

# פתרון תקלות ושאלות נפוצות

## התקנה והפעלה

### Windows SmartScreen אומר "Windows protected your PC"
התוכנה אינה חתומה בתעודה מסחרית. לחצו *More info* → *Run anyway*. הורידו אותה רק מדף ה-[Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: לא ניתן לפתוח כי היא ממפתח לא מזוהה
YA-MS אינה חתומה על ידי Apple, ולכן **Gatekeeper** חוסם אותה בפעם הראשונה. ב-`.dmg`, **לחצו לחיצה ימנית על "Installa YA-MS.command" → Open** ואשרו. הסקריפט מסיר את סימון ההסגר "downloaded from the internet" מ-`~/YA-MS/YA-MS.app` ופותח אותה. אם macOS עדיין מסרב, פתחו *System Settings → Privacy & Security* ולחצו *Open Anyway*.

### macOS: איזה ‎.dmg?
`-mac-apple-silicon.dmg` למעבדי M1/M2/M3/M4, ‏`-mac-intel.dmg` למחשבי Mac עם Intel (תפריט Apple ← *About This Mac* יגיד לכם איזה).

### Linux: YA-MS אינה בתפריט היישומים
הריצו `./installa.sh` מתוך התיקייה שחולצה (לא מ-`~/YA-MS`). בחלק משולחנות העבודה נדרשים יציאה וכניסה מחדש כדי להציג פריטים חדשים. תמיד אפשר להפעיל אותה עם `~/YA-MS/YA-MS`.

### מפת אירופה חסרה
*מפת אירופה אינה זמינה (נדרשת רשת בהפעלה הראשונה).* מפת Natural Earth מורדת אל `data/mappa` בהפעלה הראשונה. התחברו לאינטרנט והפעילו מחדש את YA-MS.

## תצוגה

### Linux: טקסט יפני מוצג כריבועים
במערכת שלכם חסרים גופני CJK. התקינו את גופני **Noto CJK** והפעילו מחדש את YA-MS:

| הפצה | פקודה |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### הטקסט קטן מדי, או שאין מקום לגרפים
השתמשו במחוון **גופן** (100–300 %) וקפלו את השורות עם **פקדים**. ראו [הגדרות](Settings-and-Data-Folder-he#גופן-ופקדים).

### המסך בהיר מדי בלילה
בחרו **לילה** או **שחור** ברשימה **ערכת נושא**.

## אינטרנט ונתוני מכ״ם

### ההודעה "אין חיבור לאינטרנט"
YA-MS מציגה אותה **פעם אחת** כשאף מקור אינו נגיש; שורת המצב הופכת לאדומה. התוכנה ממשיכה לעבוד עם **הנתונים האחרונים שנשמרו** ומנסה שוב בעצמה כל 5 דקות; *החיבור חודש.* מופיע כשהרשת חוזרת. אין צורך לעשות דבר.

### אזהרה כתומה בשטף מכ״ם: "לא ניתן לקרוא את הסולם האנכי של השטף …"
מכ״ם Collm משנה את הסולם האנכי שלו מדי יום ו-YA-MS קוראת אותו מתוויות הגרף. אם אי אפשר לקרוא תווית, התוכנה משתמשת בסולם המכויל 0–1200 מטאורים/שעה ומזהירה ש**יש לבדוק את הערכים**. בדרך כלל הגרף השעתי הבא נקרא כראוי. אם אתם רואים *תבנית הגרף השתנתה* או *צירי השטף לא נמצאו במיקום הצפוי* במשך שעות רבות, המכ״ם שינה את תבנית הגרף שלו: אנא [דווחו על כך](Contributing-and-Contacts-he).

### "סולם גרף הגבהים השתנה"
סטטיסטיקות הגובה (שכיח, ממוצע, חציון) נשארות תקפות; רק הספירות המוחלטות של היסטוגרמת הגבהים לא.

### "שטף מכ״ם: אין נתונים"
לחצו **הורד עכשיו** ב[שטף מכ״ם](Radar-Flux-he), ובדקו ש-`data/fonti_radar.csv` מכיל `attivo=1` עבור Collm.

### RMOB: למה ההורדה האוטומטית כבויה?
RMOB מבקש מ**תוכנות אוטומטיות לא להוריד את הקבצים שלו**. הפעילו את *הורדה אוטומטית כל 5 דקות* רק לאחר ש-RMOB נתן לכם רשות. בינתיים השתמשו ב-**הורד RMOB עכשיו** או ב-**טען קובץ RMOB מהדיסק...**. ראו [תחזיות ניסיוניות](Experimental-Forecasts-he#rmob-ותוכנות-אוטומטיות).

### RMOB: "תבנית הקובץ לא זוהתה" או שנקראו מעט שעות
השתמשו בקובץ הטקסט החודשי של הצופה (`NAME_MMYYYYrmob.TXT`) או בטבלת עלון עם צופה יחיד. התאמת המעריך דורשת לפחות 3 שעות משותפות עם נתוני Collm (אתמול והיום).

## חישובים

### "לוקייטור התחנה אינו תקין" / "לוקייטור תחנת ה-DX אינו תקין"
לוקייטורים חייבים להיות בני 4, 6 או 8 תווים (למשל `JN70`, `JN70CN`, `JN70CN12`).

### "אין אזור משותף בשכבת E"
הנתיב ארוך מפעמיים הטווח בגובה השובלים (כ-2 × 1062 km עם האונה ב-0° ושובלים ב-89.5 km): קפיצת פיזור מטאורי אחת אינה יכולה לכסות אותו. הגדלת **הגבהת האונה** מקצרת את הטווח עוד יותר.

### Hot A / Hot B אפורות
הן כבר נמצאות **בתוך אונת האנטנה שלכם** כשהיא מכוונת ל-DX: אין צורך לסובב. ראו [כיפת השמיים](Sky-View-he#אזהרות).

### היעילות שונה מזו של MCG_MS או MS-Soft
YA-MS משתמשת בנתיב האמיתי ובמודל משלה; הסולם של OH5IY ושל MCG_MS אינו מתועד בפירוט. השוו שעות ומגמות ולא אחוזים מוחלטים, וראו את [המודל](Efficiency-Calculation-he#המודל).

### מעבר האלומה של GRAVES נראה מוזז
רצף האלומה מחושב משעון המחשב: סנכרנו אותו עם שרת NTP. גם תחנת הבקרה של GRAVES מזיזה לעיתים את הרצף בכמה צעדים; הפירוט הוא תחזית שיש לאשר בהאזנה.

## שאלות אחרות

**האם YA-MS חינמית?** כן, זוהי תוכנה חינמית לחובבי רדיו.

**האם היא שולטת ברוטור או במכשיר הקשר שלי?** לא. YA-MS היא כלי חיזוי ותכנון; השתמשו בתוכנת האופנים הספרתיים שלכם (למשל MSHV, ‏WSJT-X) לקשר עצמו.

**האם היא עובדת מעל 432 MHz?** רשימת הפסים נעצרת ב-432 MHz ‏(28, 50, 70, 144, 222, 432). התחזית הניסיונית מקבלת כל תדר מ-28 עד 1300 MHz, אבל כללי SM6FHZ שבהם היא משתמשת באים מניסיון ב-144 וב-432 MHz.

**משהו השתבש.** כתבו למחבר וציינו את מערכת ההפעלה, את גרסת YA-MS ואת מה שעשיתם: ראו [תרומה ויצירת קשר](Contributing-and-Contacts-he).
