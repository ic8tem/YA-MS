[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · **עברית** · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh)

# הגדרות ותיקיית נתונים

## סרגל הלשוניות

בקצה הימני של סרגל הלשוניות, מימין לשמאל:

| פקד | מה הוא עושה |
|---|---|
| **שפה** (רשימה) | שפת הממשק; ראו [שפה](#שפה) |
| **ערכת נושא** (רשימה) | ערכת הצבעים; ראו [ערכות צבעים](#ערכות-צבעים) |
| **פקדים ▴ / ▾** | מקפל או פורש את שלוש שורות הפקדים שמעל הלשוניות; ראו [גופן ופקדים](#גופן-ופקדים) |

החלפת שפה או ערכת נושא שומרת את ההגדרות ו**בונה מחדש את החלון** באותו מיקום ובאותו גודל, באותה לשונית: אין צורך בהפעלה מחדש.

## שפה

שש שפות ממשק:

| שפה | קוד | קובץ |
|---|---|---|
| Italiano | `it` | אין: האיטלקית היא שפת הבסיס (המפתחות) |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

בהפעלה הראשונה YA-MS משתמשת ב**שפת המערכת** אם היא אחת מאלה, אחרת באיטלקית. מספרים ותאריכים עוקבים אחר השפה שנבחרה (למשל נקודה עשרונית באנגלית, פסיק באיטלקית ובגרמנית). כל טקסט החסר בקובץ תרגום מוצג באיטלקית. ב-Linux, יפנית דורשת גופנים מתאימים: ראו [פתרון תקלות](Troubleshooting-FAQ-he#linux-טקסט-יפני-מוצג-כריבועים).

המסמך [יעילות - הסבר](Efficiency-Explanation-he) ומדריך החישובים הם באיטלקית.

## ערכות צבעים

הרשימה **ערכת נושא** מציעה 12 ערכות, אותן ערכות של תוכנת ה-EME של המחבר, YAEC, וכן הפלטה המקורית של YA-MS:

| ערכה | תיאור |
|---|---|
| **בהיר** | ברירת מחדל |
| **לילה** | גוונים כחולים כהים, לשימוש בלילה |
| **שחור** | רקע שחור, לחושך ולמסכי OLED |
| פסטל תכלת · פסטל כתום · פסטל אקוומרין · פסטל ירוק · פסטל ורוד · פסטל לילך · פסטל אינדיגו · פסטל חום | שמונה ערכות פסטל בהירות |
| **שובל מטאורי** | הסגנון המקורי של YA-MS (עד גרסה 1.2.0): סגול לילי עם תכלת, סגול, ירוק בהיר, צהוב וכתום |

הערכה חלה על כל הלשוניות ונשמרת ב-`config.ini` (המפתח `tema`).

## גופן ופקדים

- **גופן** (בסוף השורה הראשונה של הפקדים): מגדיל את **כל הטקסט** מ-**100 עד 300 %** בצעדים של 10 %; קווים, עיגולים ומפות שומרים על גודלם. עם גופנים גדולים הלשוניות נשברות לשורה שנייה והכרטיסים גדלים.
- **פקדים**: עם גופנים גדולים או מסך קטן, קפלו את שלוש שורות הפקדים כדי לפנות מקום למפות ולגרפים. המצב נשמר.

## תיקיית הנתונים

כל הנתונים וההגדרות נמצאים בתיקיית **`data`** אחת **ליד התוכנה** – בלי AppData, בלי תיקיות מערכת:

| מערכת | תוכנה | נתונים |
|---|---|---|
| Windows (מתקין) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (נייד) | היכן שחילצתם אותה | `data` ליד `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (ליד היישום) |

בהפעלה התוכנה יוצרת את התיקייה במידת הצורך ומעתיקה רק את קובצי ההתחלה **החסרים**: קבצים ששיניתם לעולם אינם נדרסים. קובצי התרגום ב-`data/lingue` הם קובצי תוכנה ומוחלפים כאשר הקבצים של הגרסה החדשה עדכניים יותר.

### קבצים שאפשר לערוך

| קובץ | תוכן |
|---|---|
| `sciami.csv` | קטלוג המטרים (ערכי IMO וערכי עבודה); ראו [מטרים](Showers-he#עריכת-הקטלוג) |
| `massimi_imo.csv` | תאריכי ושעות השיא שפורסמו על ידי IMO ‏(2026, 2027): **הוסיפו שנים חדשות** כאן |
| `ant_radiante.csv` | מיקום מקור אנטי-הליון (טבלה 6 של IMO) |
| `fonti_radar.csv` | כתובות המכ״מים; `attivo=1` מוריד, `0` מתעלם |
| `regole_sperimentali.csv` | הקבועים והכללים שבשימוש, כל אחד עם מקורו (לעיון) |
| `lingue/<code>.txt` | תרגומי הממשק; ראו [תרומה](Contributing-and-Contacts-he#תרגומים) |
| `config.ini` | הגדרות (ראו להלן) |

### קבצים שהתוכנה יוצרת

| קובץ / תיקייה | תוכן |
|---|---|
| `config.ini` | הגדרות |
| `flusso_collm.csv` | ארכיון שעתי של שטף Collm |
| `quote_collm.csv` | ארכיון גובהי השובלים |
| `radar/` | תמונות המכ״ם האחרונות וקובצי RMOB |
| `mappa/` | קווי חוף וגבולות של Natural Earth (מורדים בהפעלה הראשונה) |
| `adif_quadrati.csv` | הריבועים מקובץ ה-ADIF האחרון שנטען |
| `efficienza_spiegazione.txt`, `.docx` | [מסמך ההסבר](Efficiency-Explanation-he) |

## config.ini

טקסט פשוט, `key=value` אחד בכל שורה (שורות המתחילות ב-`#` או ב-`;` הן הערות). התוכנה כותבת אותו כשהיא נסגרת, ולכן **ערכו אותו כש-YA-MS סגורה**. המפתחות שאולי תרצו להכיר:

| מפתח | ברירת מחדל | משמעות |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | הלוקייטור והגובה שלך (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | הלוקייטור והגובה של תחנת ה-DX ‏(m) |
| `banda_MHz` | 144 | פס (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | גובה השובלים (km); ‏1 = שימוש בשכיח של Collm |
| `elevazione_lobo_gradi` | 0 | הגבהת האונה (°) |
| `boom_m` | 4.6 | אורך בום היאגי (m) |
| `hot_spot_km` | 150 | המרחק של Hot A / Hot B מנקודת האמצע (30–400 km) |
| `lingua` | מערכת / `it` | קוד שפה (`it`, `en`, `ru`, `ja`, `de`, `nl`) |
| `tema` | `chiaro` | ערכת צבעים: `chiaro` (בהיר), `scuro` (לילה), `nero` (שחור), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (שובל מטאורי) |
| `carattere_pct` | 100 | גודל גופן (100–300 %) |
| `comandi_visibili` | 1 | ‏1 = שורות הפקדים מוצגות, 0 = מקופלות |
| `mostra_mappa`, `vista_alto` | 1, 1 | מפת אירופה, מבט על בכיפת השמיים |
| `aggiornamento_automatico` | 1 | בדיקה אוטומטית של המקורות כל 5 דקות |
| `esponente_lambda` | 3 | מעריך λ בלשונית שטף מכ״ם |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | קלטי מאזן הקישור |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | תחזית ניסיונית: תדר, k, ‏K |
| `rmob_osservatore` | ריק | שם צופה ה-RMOB |
| `rmob_automatico` | 0 | הורדת RMOB אוטומטית (להפעיל רק ברשות RMOB) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | תבנית כתובת RMOB |
| `graves_sequenza` | 0 | רצף אלומת GRAVES: ‏0 = 0.8 s ‏(2021), 1 = 3.2 s ‏(2007) |

## פרטיות

YA-MS אינה אוספת נתונים ואינה מציגה פרסומות. היא מתחברת לאינטרנט רק כדי להוריד נתונים ציבוריים: תמונות המכ״מים של Collm ו-Sodankylä, מפת Natural Earth (בהפעלה הראשונה) וגם, אם תבקשו, קובץ RMOB.
