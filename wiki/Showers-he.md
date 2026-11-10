[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · **עברית** · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh)

# מטרים

*לשונית: מטרים.*

[![מטרים](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

קטלוג המטרים שבו משתמשים כל החישובים: **45 מטרים** מתוך **IMO Meteor Shower Calendar 2026 ו-2027** (טבלאות 5 ו-7) וכן **מקור אנטי-הליון (Antihelion Source)** (טבלה 6), כל אחד עם **השיא הבא** שלו.

## עמודות

| עמודה | משמעות |
|---|---|
| קוד | קוד IMO ‏(QUA, PER, GEM, …) |
| מטר | שם |
| פעילות | תקופת הפעילות (יום/חודש – יום/חודש) |
| λ max | האורך השמשי של השיא (J2000), מ-IMO |
| **השיא הבא (UTC)** | תאריך ושעה של השיא הבא (ראו להלן) |
| **מקור השיא** | *IMO 2026* / *IMO 2027* = תאריך ושעה שפורסמו על ידי IMO; *IMO 2026 (יום)* = IMO נותן רק את היום, השעה המוצגת מחושבת (*~hh:mm מחושב*); *מחושב מ-λ* = אין ערך של IMO לאותה שנה |
| עלייה ישרה, נטייה | הרדיאנט בשיא (*נע* עבור מקור אנטי-הליון) |
| v km/s, ‏r | מהירות גאוצנטרית ומדד האוכלוסייה |
| ZHR | ZHR בשיא (*משתנה* = משתנה) |
| סוג | *חזותי* או *רדיו, יומי* |

המטרים **הפעילים היום (UTC)** מסומנים בהדגשה צהובה שקופה ובגופן מודגש.

## השיא הבא

התוכנה מציגה תמיד את השיא **הבא**. כאשר IMO פרסם את לוח השנה של אותה שנה, היא משתמשת ב**תאריך ובשעה של IMO** מתוך `data/massimi_imo.csv` (‏2026 ו-2027 כלולים); אחרת היא מחשבת את הרגע שבו השמש מגיעה לאורך השמשי של השיא (Meeus, ‏*Astronomical Algorithms*, פרק 25, בפתרון בשיטת ניוטון).

**בדיקה:** החישוב תואם את לוחות IMO של 2026 ו-2027 בטווח של דקות ספורות היכן ש-IMO נותן את השעה (למשל קוודרנטידים 3/1/2026 21:13 לעומת 21:00; ג׳מינידים 14/12/2027 19:51 לעומת 20:00). חריגים: קאפה לאונידים יומיים 2026 יום אחד מאוחר יותר (26/9 במקום 25/9) והשעה של אטא אקווארידים 2027 (15:10 לעומת 09:00 של IMO) – במקרים אלה משתמשים בערך של IMO.

**הוספת שנה:** כאשר IMO מפרסם לוח שנה חדש, הוסיפו את שורותיו ל-`data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, השעה ריקה אם IMO נותן רק את היום). עד אז השיא מחושב.

## מטרים משניים ויומיים

הקטלוג כולל את **המטרים המשניים** של רשימת IMO – למשל קמלופרדלידים של אוקטובר (OCT, ‏ZHR 5, פעילים 5–6 באוקטובר), אנדרומדידים, גמא אורסה מינורידים – ואת **מטרי הרדיו היומיים** של אפריל–אוקטובר (פיסידים של אפריל יומיים, אריאטידים יומיים, זטא פרסאידים יומיים, בטא טאורידים יומיים, קאפה לאונידים יומיים, סקסטנטידים יומיים, …). גם עם ZHR קטן הם תורמים ל[מדד הנתיב](Efficiency-Calculation-he#המודל) ול[Hot המומלץ](Sky-View-he#hot-מומלץ). עבור מטרי הרדיו היומיים IMO אינו נותן ZHR: היכן שאין ערך, התוכנה משתמשת בערך עבודה של 5.

## פרופיל הפעילות והיסחפות הרדיאנט

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

ZHR_max, ‏α0, ‏δ0 ו-λ_max מלוח השנה של IMO; השיפועים B (שונים לפני השיא ואחריו) וההיסחפויות היומיות dα/dλ, ‏dδ/dλ הם **ערכי עבודה** הרשומים ב-`data/sciami.csv` (טבלת ההיסחפות של IMO טרם הוזנה). *משוואות 9 ו-13 במדריך.* מיקום מקור אנטי-הליון מאונטרפל לינארית בין התאריכים של טבלה 6 של IMO ‏(`data/ant_radiante.csv`; פעיל מ-10 בדצמבר עד 20 בספטמבר, ZHR כ-4).

## עריכת הקטלוג

`data/sciami.csv` הוא קובץ טקסט פשוט (מפריד `;`) שאפשר לערוך: קוד, שם, התחלה וסיום (MM-DD), ‏λ max, עלייה ישרה, נטייה, היסחפויות, v, ‏r, ‏ZHR, ‏B לפני/אחרי, סוג (V חזותי, R רדיו יומי). אם שורה שגויה, התוכנה מציגה הודעה בהפעלה ומתעלמת ממנה.

מקורות: International Meteor Organization – Meteor Shower Calendar 2026 ו-2027, ‏[www.imo.net](https://www.imo.net) (טבלאות 5, 6 ו-7); ‏Philip G0ISW (קצבים שעתיים מרביים ברדיו); Rossano IZ5TEK ‏(scattertek).
