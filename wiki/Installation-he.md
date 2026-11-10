[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · **עברית** · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh)

# התקנה

כל החבילות נמצאות בדף **[Releases](https://github.com/ic8tem/YA-MS/releases)** (בשמות הקבצים שלהלן `x.y.z` הוא מספר הגרסה, למשל `1.2.0`). אין צורך לקמפל דבר ואין צורך להתקין שום דבר נוסף: כל חבילה כוללת את סביבת הריצה ‎.NET 8.

| מערכת | קובץ | מותקן ב- |
|---|---|---|
| Windows (64-bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (מתקין) | `C:\YA-MS` |
| Windows (64-bit), נייד | `YA-MS-x.y.z-windows-x64-portatile.zip` | כל תיקייה שיש לך הרשאת כתיבה בה |
| Windows (32-bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` או `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-bit): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (מועתק לשם בהפעלה הראשונה) |
| Linux (64-bit), כל הפצה | `YA-MS-x.y.z-linux-x64.tar.gz` (נייד או עם `./installa.sh`) | `~/YA-MS` או כל תיקייה |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, חבילת Debian | `ya-ms_x.y.z_arm64.deb` (64-bit) או `ya-ms_x.y.z_armhf.deb` (32-bit) | `~/YA-MS` (מועתק לשם בהפעלה הראשונה) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, היישום בלבד | `YA-MS-x.y.z-mac-apple-silicon-app.zip` או `...-mac-intel-app.zip` | התיקייה שאליה חילצתם את `YA-MS.app` |

**התוכנה ותיקיית ה-`data` שלה נשארות תמיד יחד** בתיקיית YA-MS: כל הנתונים וההגדרות נמצאים שם (בלי AppData, בלי תיקיות מערכת). ראו [הגדרות ותיקיית נתונים](Settings-and-Data-Folder-he).

## Windows

### מתקין
1. הורידו את `YA-MS-x.y.z-windows-x64-setup.exe` והפעילו אותו.
2. אם **SmartScreen** מציג "Windows protected your PC": *More info* → *Run anyway* (התוכנה אינה חתומה בתעודה מסחרית).
3. YA-MS מותקנת ב-**`C:\YA-MS`**, **ללא הרשאות מנהל**, עם סמל בתפריט התחל, ואם תסמנו זאת, גם סמל בשולחן העבודה.

### נייד
חלצו את `YA-MS-x.y.z-windows-x64-portatile.zip` היכן שתרצו (בתיקייה שיש לכם הרשאת כתיבה בה, לא ב-*Program Files*) והפעילו את `YA-MS.exe`. אפשר להעתיק את כל התיקייה לדיסק USB או למחשב אחר.

## Linux

1. חלצו את `YA-MS-x.y.z-linux-x64.tar.gz`.
2. מתוך התיקייה שחולצה הריצו:
   ```sh
   ./installa.sh
   ```
3. הסקריפט מעתיק את YA-MS אל **`~/YA-MS`** (אין צורך ב-root) ומוסיף את **YA-MS** לתפריט היישומים (קטגוריה *HamRadio*). אפשר גם להפעיל אותה עם `~/YA-MS/YA-MS`.

### חבילת Debian ‏(.deb)
ב-Debian, ‏Ubuntu, ‏Mint וב-Raspberry Pi OS אפשר במקום זאת להתקין את `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` ב-Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
החבילה מציבה את התוכנה ב-`/opt/ya-ms` ומוסיפה את **YA-MS** לתפריט. בהפעלה הראשונה (ואחרי כל גרסה חדשה) היא מעתיקה את עצמה אל **`~/YA-MS`** ופועלת משם, כך שתיקיית ה-`data` נשארת לצד התוכנה וההגדרות שלכם נשמרות.

### נייד
קובץ ה-`.tar.gz` עובד גם בלי התקנה: חלצו אותו בכל מקום שיש לכם הרשאת כתיבה בו והריצו `./YA-MS` מתוך אותה תיקייה.

להצגת טקסט יפני ייתכן שתזדקקו לגופני Noto CJK: ראו [פתרון תקלות](Troubleshooting-FAQ-he#linux-טקסט-יפני-מוצג-כריבועים).

## Raspberry Pi

אותו הליך כמו ב-Linux: חלצו את `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (או `-32bit` ב-Raspberry Pi OS ‏32-bit) והריצו `./installa.sh` מתוך התיקייה שחולצה.

- כדי לדעת איזו מערכת יש לכם, הקלידו `uname -m` במסוף: `aarch64` ← חבילת 64-bit, `armv7l` ← חבילת 32-bit.
- נתמכים: Raspberry Pi 2 (‏32-bit בלבד), 3, 4, 5, 400 ו-500, עם גרסת שולחן העבודה של Raspberry Pi OS. **לא נתמכים:** Pi Zero / Zero W ו-Pi 1 (מעבד ARMv6, ‏.NET אינו רץ עליו); Pi Zero 2 W עובד עם חבילת ה-64-bit, אבל 512 MB של RAM הם צפופים.
- מומלץ Pi 4 או 5 עם 2 GB של RAM לפחות; ההפעלה הראשונה אורכת כמה שניות יותר מאשר במחשב אישי.

## macOS

1. בחרו את הקובץ הנכון: `-mac-apple-silicon.dmg` למעבדי M1/M2/M3/M4, ‏`-mac-intel.dmg` למחשבי Mac עם Intel.
2. פתחו את ה-`.dmg`, **לחצו לחיצה ימנית על "Installa YA-MS.command" → Open** ואשרו.
3. הסקריפט מעתיק את `YA-MS.app` אל **`~/YA-MS`** ופותח אותה.

לחלופין, `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` מכיל רק את `YA-MS.app`: חלצו אותו לתיקייה לבחירתכם (שיש לכם הרשאת כתיבה בה); תיקיית ה-`data` נוצרת לצד `YA-MS.app`. בפעם הראשונה: לחיצה ימנית → **Open**.

התוכנה אינה חתומה על ידי Apple, ולכן בפעם הראשונה macOS מבקש אישור; ראו [פתרון תקלות](Troubleshooting-FAQ-he#macos-לא-ניתן-לפתוח-כי-היא-ממפתח-לא-מזוהה).

## הפעלה ראשונה

- **מפת אירופה** (קווי חוף וגבולות של Natural Earth) מורדת אוטומטית אל `data/mappa` בפעם הראשונה: נדרש חיבור לאינטרנט פעם אחת.
- **נתוני המכ״ם** (Collm, ‏Sodankylä) מורדים מיד ולאחר מכן נבדקים כל 5 דקות.
- הממשק נפתח בשפת המערכת שלכם אם היא אחת מתוך 28 השפות הזמינות, אחרת באיטלקית; שנו אותה בפינה הימנית העליונה (ראו [הגדרות](Settings-and-Data-Folder-he#שפה)).

## עדכון

התקינו את הגרסה החדשה **מעל הישנה** (אותו מתקין, אותה תיקייה). ההגדרות (`config.ini`), ארכיוני השטף והמפה נשארים ב-`data`. קובצי התרגום ב-`data/lingue` מוחלפים כאשר החדשים עדכניים יותר.

## בנייה מקוד המקור (למפתחים בלבד)

המתקינים נוצרים על ידי GitHub Actions ‏(`.github/workflows/build.yml`) בכל עדכון של הענף `release` (הגרסה נלקחת מהקובץ `VERSION`), שגם יוצר את השחרור `vX.Y.Z`. באופן מקומי:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # או linux-x64, linux-arm64, linux-arm, osx-arm64
```

המסמכים נוצרים מחדש עם `tools/build_spiegazione.py data` ו-`node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

הבא: [צעדים ראשונים](Getting-Started-he).
