[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-BR) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · **עברית** · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [ไทย](Experimental-Forecasts-th) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-TW)

# תחזיות ניסיוניות

*לשונית: חישוב תחזית › תחזיות ניסיוניות.*

[![תחזיות ניסיוניות](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

לשונית זו הופכת את ספירות המטאורים של **מכ״ם Collm (36.2 MHz)** להערכה של **מספר ההחזרות לשעה בפס חובבים** (144 MHz כברירת מחדל, כל תדר מ-28 עד 1300 MHz), חוזה את **24 השעות הבאות** עבור הנתיב שלך ומאפשרת **להשוות** את ההערכה לצופה **RMOB** – למשל צופה המאזין ל-GRAVES ב-143.050 MHz.

> כל מה שכאן **ניסיוני**: כלל התדר הוא כלל אמפירי, ומקדם התחנה תלוי בתחנה שלך. השתמשו במספרים כדי להשוות שעות וימים, ובדקו אותם באוויר.

## פקדים

| פקד | ברירת מחדל | מה הוא עושה |
|---|---|---|
| **תדר יעד MHz** | 144 | תדר התחזית (28–1300 MHz) |
| **מעריך λ^k** | 3 | המעריך k של כלל התדר (SM6FHZ: ‏3) |
| **מקדם תחנה K** | 1 | מביא בחשבון את תחנת הקליטה (הספק, אנטנות); נגזר מהשוואה לצופה RMOB באותו פס |
| **טען קובץ RMOB מהדיסק...** | | קורא קובץ טקסט חודשי של RMOB (ראו להלן) |
| **גזור את המעריך מקובץ ה-RMOB** | | מתאים את k מהשעות המשותפות של Collm ו-RMOB |
| **צופה RMOB** | ריק | שם הצופה כפי שהוא מופיע בשם הקובץ (למשל `NAME_112026rmob.TXT` → `NAME`) |
| **הורד RMOB עכשיו** | | מוריד פעם אחת את קובץ החודש הנוכחי של אותו צופה |
| **הורדה אוטומטית כל 5 דקות (להפעיל רק ברשות RMOB)** | **כבוי** | ראו [RMOB ותוכנות אוטומטיות](#rmob-ותוכנות-אוטומטיות) |

הקו הכתום מתחת לפקדים מציג את הכלל עם המספרים הנוכחיים, למשל *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, את התאמת המשך ואת הפינג המרבי לפי IARU באותו תדר.

## מהמכ״ם לפס החובבים

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}\sec^2\varphi
```

**מקור:** SM6FHZ, ‏*"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, מאי 2025 – מספר ההחזרות ועוצמתן משתנים לפי **λ³**, ומשכן לפי **λ²** (‏432 MHz נמוך ב-14–15 dB מ-144 MHz ונמשך 1/9). **בדיקה:** במשוואה של McKinley ‏λ³ הוא ההספק של שובל תת-צפוף יחיד, לא מספר השובלים; עם אינדקס מסה 2, מספר השובלים מעל סף קבוע משתנה בקירוב לפי λ^1.5 ‏(IZ5TEK; OH5IY). התוכנה שומרת על k = 3, הכלל הניסויי של SM6FHZ, ואומרת זאת; ה-k הנכון לתחנה שלך נובע מההשוואה ל-RMOB. בפיזור קדמי המשך גדל גם לפי sec²φ ‏(McKinley; OH5IY): ‏Collm מודד בפיזור לאחור (φ = 0), ולכן התחזית מוכפלת ב-sec²φ בנקודת האמצע של הנתיב (×4 ב-60°, ×8.5 ב-70°, ×33 ב-80°). עם k = 3, ‏1000 מטאורים/שעה ב-Collm הופכים לכ-**16 החזרות/שעה ב-144 MHz**; צופי RMOB של GRAVES ב-143.050 MHz סופרים בדרך כלל **20 עד 140 הדים/שעה** (עלון RMOB, יוני 2018): סדר הגודל תואם, וההפרש הוא מקדם התחנה K. (משוואות 44–45 במדריך.)

## 24 השעות הבאות

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**התמדה:** הערך המותאם של אותה שעה ביום הקודם (או יומיים קודם אם חסר), מתוקן לפי השינוי ב**מדד המטרים לנתיב** I ‏(Σ ZHR × יעילות, ראו [חישוב היעילות](Efficiency-Calculation-he#המודל)). הקבוע 10 מייצג את רקע הספורדיים ומגביל את התיקון כשהמדד קטן. *בחירה של התוכנה (משוואה 47 במדריך).*

| חלונית | תוכן |
|---|---|
| **נמדד ב-Collm והותאם ל-f MHz - אתמול והיום (UTC)** | מטאורים/שעה של מכ״ם Collm; ערכים מותאמים (כתום, סולם ימני); ספירות RMOB אם נטענו (ירוק, סולם ימני) |
| **תחזית ניסיונית ל-24 השעות הבאות ב-f MHz עבור …** | החזרות/שעה חזויות (עמודות) ומדד המטרים לנתיב (סולם ימני) |
| טבלה | שעת UTC · ‏Collm באותה שעה · מותאם · מדד המטרים לנתיב · תחזית /שעה · **הערכה** |

**הערכה:** *טוב* כשהתחזית היא לפחות פי 1.3 מהממוצע של 24 השעות, *בינוני* מפי 0.8, *חלש* מתחת לכך. אותה תחזית מופיעה בכרטיס **תחזית ניסיונית** ובשורה הכתומה של [חישוב היעילות](Efficiency-Calculation-he), והיא הבסיס להדים הצפויים בלשונית [מכ״ם GRAVES](GRAVES-Radar-he#הדים-צפויים-ניסיוני).

## השוואה ל-RMOB

[RMOB](https://www.rmob.org) ‏(Radio Meteor Observatories On Line, ‏Pierre Terrier) אוסף את ספירות המטאורים השעתיות של צופי רדיו; רבים באיטליה מאזינים ל-GRAVES ב-143.050 MHz (הפלנטריום של ונציה, פאנצה, רוברטו ואחרים).

**קריאת קובצי RMOB.** מתקבלות שתי תבניות טקסט:

| תבנית | מראה | הערות |
|---|---|---|
| קובץ חודשי (Colorgramme / Spectrum Lab) | שורה לכל יום, `day| n| n| …` עם 24 ערכים שעתיים | הקובץ הרגיל `NAME_MMYYYYrmob.TXT` |
| טבלת עלון | כותרת ` UT |  1   2   3 …`, שורות `0h|175 166 …` | אם הקובץ מכיל כמה צופים הם נקראים בזה אחר זה: השתמשו בקובץ עם צופה יחיד |

החודש והשנה נלקחים משם הקובץ (`…_MMYYYYrmob…`) או מהכותרת; אחרת משתמשים בחודש הנוכחי (והתוכנה מציינת זאת).

**התאמת המעריך.** עם K = 1, מהחציון של היחסים RMOB/Collm על פני השעות המשותפות (לפחות 3):

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*בחירה של התוכנה (משוואה 46 במדריך).* תיבת הדו-שיח מציגה את השעות המשותפות, את היחס החציוני ואת k; **כן** מחיל את k (וקובע K = 1), **לא** משאיר k = 3 – ואז כווננו את K ידנית לערך המוצע באותה תיבת דו-שיח.

## RMOB ותוכנות אוטומטיות

RMOB מבקש מ**תוכנות אוטומטיות לא להוריד את הקבצים שלו**. מסיבה זו **ההורדה האוטומטית כבויה** בהתחלה ויש להפעיל אותה **רק לאחר שביקשתם רשות מ-RMOB**. בלעדיה תמיד אפשר להשתמש ב-**טען קובץ RMOB מהדיסק...** או ללחוץ **הורד RMOB עכשיו** כשצריך.

כתובת ההורדה היא תבנית ב-`config.ini` (המפתח `rmob_url`, ברירת מחדל `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, כאשר `{NOME}` הוא הצופה ו-`{MMAAAA}` החודש והשנה); הקבצים שהורדו נשמרים ב-`data/radar/`.
