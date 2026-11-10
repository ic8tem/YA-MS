[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · **العربية** · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [ไทย](Installation-th) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# التثبيت

جميع الحزم موجودة في صفحة **[Releases](https://github.com/ic8tem/YA-MS/releases)** (في أسماء الملفات أدناه `x.y.z` هو رقم الإصدار، مثلاً `1.2.0`). لا حاجة إلى ترجمة أي شيء ولا إلى تثبيت أي شيء آخر: كل حزمة تتضمن بيئة تشغيل .NET 8.

| النظام | الملف | مكان التثبيت |
|---|---|---|
| Windows (64-bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (مثبِّت) | `C:\YA-MS` |
| Windows (64-bit)، محمول | `YA-MS-x.y.z-windows-x64-portatile.zip` | أي مجلد لديك صلاحية الكتابة فيه |
| Windows (32-bit، Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` أو `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-bit) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5، 400/500 (Raspberry Pi OS 64-bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS، Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS، Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**يبقى البرنامج ومجلد `data` الخاص به معاً دائماً** في مجلد YA-MS: فيه جميع البيانات والإعدادات (لا AppData ولا مجلدات نظام). انظر [الإعدادات ومجلد البيانات](Settings-and-Data-Folder-ar).

## Windows

### المثبِّت
1. نزّل `YA-MS-x.y.z-windows-x64-setup.exe` وشغّله.
2. إذا عرض **SmartScreen** الرسالة "Windows protected your PC": *More info* → *Run anyway* (البرنامج غير موقَّع بشهادة تجارية).
3. يُثبَّت YA-MS في **`C:\YA-MS`**، **دون صلاحيات المسؤول**، مع أيقونة في قائمة ابدأ، وأيقونة على سطح المكتب إن اخترت ذلك.

### النسخة المحمولة
فك ضغط `YA-MS-x.y.z-windows-x64-portatile.zip` حيث تشاء (في مجلد لديك صلاحية الكتابة فيه، لا في *Program Files*) وشغّل `YA-MS.exe`. يمكنك نسخ المجلد بأكمله إلى ذاكرة USB أو إلى حاسوب آخر.

## Linux

1. فك ضغط `YA-MS-x.y.z-linux-x64.tar.gz`.
2. من المجلد المستخرَج شغّل:
   ```sh
   ./installa.sh
   ```
3. ينسخ السكربت YA-MS إلى **`~/YA-MS`** (دون الحاجة إلى root) ويضيف **YA-MS** إلى قائمة التطبيقات (الفئة *HamRadio*). يمكنك أيضاً تشغيله بالأمر `~/YA-MS/YA-MS`.

لعرض النصوص اليابانية قد تحتاج إلى خطوط Noto CJK: انظر [حل المشكلات](Troubleshooting-FAQ-ar#linux-النص-الياباني-يظهر-مربعات).

## Raspberry Pi

الإجراء نفسه كما في Linux: فك ضغط `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (أو `-32bit` على Raspberry Pi OS 32-bit) وشغّل `./installa.sh` من المجلد المستخرَج.

- لمعرفة نظامك، اكتب `uname -m` في الطرفية: `aarch64` ← حزمة 64-bit، `armv7l` ← حزمة 32-bit.
- الأجهزة المدعومة: Raspberry Pi 2 (32-bit فقط) و3 و4 و5 و400 و500، مع نسخة سطح المكتب من Raspberry Pi OS. **غير مدعومة:** Pi Zero / Zero W وPi 1 (معالج ARMv6، لا يعمل عليه .NET)؛ يعمل Pi Zero 2 W مع حزمة 64-bit لكن ذاكرة 512 MB من RAM محدودة.
- يُنصح بـ Pi 4 أو 5 مع 2 GB من RAM على الأقل؛ يستغرق التشغيل الأول بضع ثوانٍ أكثر مما على حاسوب شخصي.

## macOS

1. اختر الملف المناسب: `-mac-apple-silicon.dmg` لمعالجات M1/M2/M3/M4، و`-mac-intel.dmg` لأجهزة Mac بمعالج Intel.
2. افتح ملف `.dmg`، ثم **انقر بزر الفأرة الأيمن على "Installa YA-MS.command" → Open** وأكّد.
3. ينسخ السكربت `YA-MS.app` إلى **`~/YA-MS`** ويفتحه.

البرنامج غير موقَّع من Apple، لذا يطلب macOS تأكيداً في المرة الأولى؛ انظر [حل المشكلات](Troubleshooting-FAQ-ar#macos-لا-يمكن-فتحه-لأنه-من-مطوِّر-غير-معروف).

## التشغيل الأول

- تُنزَّل **خريطة أوروبا** (السواحل والحدود من Natural Earth) تلقائياً إلى `data/mappa` في المرة الأولى: يلزم اتصال بالإنترنت مرة واحدة.
- تُنزَّل **بيانات الرادار** (Collm وSodankylä) فوراً ثم تُفحص كل 5 دقائق.
- تبدأ الواجهة بلغة نظامك إن كانت إحدى اللغات الـ36 المتاحة، وإلا فبالإيطالية؛ غيّرها من أعلى اليمين (انظر [الإعدادات](Settings-and-Data-Folder-ar#اللغة)).

## التحديث

ثبّت الإصدار الجديد **فوق القديم** (المثبِّت نفسه، المجلد نفسه). تبقى الإعدادات (`config.ini`) وأرشيفات التدفق والخريطة في `data`. تُستبدل ملفات الترجمة في `data/lingue` عندما تكون الجديدة أحدث.

## البناء من الشيفرة المصدرية (للمطورين فقط)

تُنتَج المثبِّتات بواسطة GitHub Actions (`.github/workflows/build.yml`) عند كل تحديث لفرع `release` (يؤخذ رقم الإصدار من الملف `VERSION`)، والذي ينشئ أيضاً الإصدار `vX.Y.Z`. محلياً:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # أو linux-x64, linux-arm64, linux-arm, osx-arm64
```

تُعاد توليد الوثائق بالأمرين `tools/build_spiegazione.py data` و`node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

التالي: [البدء](Getting-Started-ar).
