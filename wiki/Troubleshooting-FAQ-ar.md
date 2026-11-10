[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-BR) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · **العربية** · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-TW)

# حل المشكلات والأسئلة الشائعة

## التثبيت وبدء التشغيل

### يقول Windows SmartScreen "Windows protected your PC"
البرنامج غير موقَّع بشهادة تجارية. انقر *More info* → *Run anyway*. لا تنزّله إلا من صفحة [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: لا يمكن فتحه لأنه من مطوِّر غير معروف
YA-MS غير موقَّع من Apple، لذا يحظره **Gatekeeper** في المرة الأولى. في ملف `.dmg`، **انقر بزر الفأرة الأيمن على "Installa YA-MS.command" → Open** وأكّد. يزيل السكربت علامة الحجر "downloaded from the internet" عن `~/YA-MS/YA-MS.app` ويفتحه. إذا استمر macOS في الرفض، افتح *System Settings → Privacy & Security* واضغط *Open Anyway*.

### macOS: أي ملف ‎.dmg؟
`-mac-apple-silicon.dmg` لمعالجات M1/M2/M3/M4، و`-mac-intel.dmg` لأجهزة Mac بمعالج Intel (قائمة Apple ← *About This Mac* تخبرك بنوع جهازك).

### Linux: لا يظهر YA-MS في قائمة التطبيقات
شغّل `./installa.sh` من المجلد المستخرَج (لا من `~/YA-MS`). تحتاج بعض بيئات سطح المكتب إلى تسجيل خروج ثم دخول لإظهار العناصر الجديدة. ويمكنك دائماً تشغيله بالأمر `~/YA-MS/YA-MS`.

### خريطة أوروبا مفقودة
*خريطة أوروبا غير متاحة (يلزم اتصال بالشبكة عند أول تشغيل).* تُنزَّل خريطة Natural Earth إلى `data/mappa` عند التشغيل الأول. اتصل بالإنترنت وأعد تشغيل YA-MS.

## العرض

### Linux: النص الياباني يظهر مربعات
نظامك يفتقر إلى خطوط CJK (الصينية واليابانية والكورية). ثبّت خطوط **Noto CJK** وأعد تشغيل YA-MS. ويحدث الأمر نفسه مع العربية والعبرية والأردية والهندية والبنغالية: على Debian وUbuntu وRaspberry Pi OS ثبّت أيضاً `fonts-noto-core`.

| التوزيعة | الأمر |
|---|---|
| Debian، Ubuntu، Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### النص صغير جداً، أو لا يوجد متسع للمخططات
استخدم منزلق **الخط** (100–300 %) واطوِ الصفوف بزر **عناصر التحكم**. انظر [الإعدادات](Settings-and-Data-Folder-ar#الخط-وعناصر-التحكم).

### الشاشة ساطعة جداً ليلاً
اختر **ليلي** أو **أسود** من قائمة **السمة**.

## الإنترنت وبيانات الرادار

### رسالة "لا يوجد اتصال بالإنترنت"
يعرضها YA-MS **مرة واحدة** عندما يتعذر الوصول إلى أي مصدر؛ ويتحول شريط الحالة إلى الأحمر. يواصل البرنامج العمل بـ**آخر البيانات المحفوظة** ويعيد المحاولة تلقائياً كل 5 دقائق؛ وتظهر *عاد الاتصال.* عند عودة الشبكة. لا شيء عليك فعله.

### تنبيه برتقالي في تدفق الرادار: "تتعذر قراءة المقياس الرأسي للتدفق …"
يغيّر رادار Collm مقياسه الرأسي كل يوم، ويقرؤه YA-MS من تسميات المخطط. إذا تعذرت قراءة تسمية، يستخدم البرنامج المقياس المعايَر 0–1200 شهب/ساعة وينبّه إلى أن **القيم تحتاج إلى تحقق**. عادةً يُقرأ المخطط الساعي التالي بشكل صحيح. إذا رأيت *تغيّر تنسيق الرسم البياني* أو *لم يُعثر على محاور التدفق في الموضع المتوقع* لساعات كثيرة، فقد غيّر الرادار تنسيق مخططه: يُرجى [الإبلاغ عن ذلك](Contributing-and-Contacts-ar).

### "تغيّر مقياس مخطط الارتفاعات"
تبقى إحصاءات الارتفاع (المنوال، المتوسط، الوسيط) صالحة؛ أما الأعداد المطلقة في المدرج التكراري للارتفاعات فلا.

### "تدفق الرادار: لا بيانات"
اضغط **تنزيل الآن** في [تدفق الرادار](Radar-Flux-ar)، وتحقق من أن `data/fonti_radar.csv` يتضمن `attivo=1` لـ Collm.

### RMOB: لماذا الجلب التلقائي معطَّل؟
يطلب RMOB من **البرامج الآلية عدم جلب ملفاته**. لا تفعّل *جلب تلقائي كل 5 دقائق* إلا بعد أن يمنحك RMOB الإذن. وفي الأثناء استخدم **تنزيل RMOB الآن** أو **تحميل ملف RMOB من القرص...**. انظر [التنبؤات التجريبية](Experimental-Forecasts-ar#rmob-والبرامج-الآلية).

### RMOB: "لم يُتعرَّف على تنسيق الملف" أو قُرئت ساعات قليلة
استخدم الملف النصي الشهري للراصد (`NAME_MMYYYYrmob.TXT`) أو جدول نشرة لراصد واحد. يحتاج توفيق الأس إلى 3 ساعات على الأقل مشتركة مع بيانات Collm (أمس واليوم).

## الحسابات

### "محدد موقع المحطة غير صالح" / "محدد موقع المحطة المقابلة غير صالح"
يجب أن يتألف محدد الموقع من 4 أو 6 أو 8 أحرف (مثلاً `JN70`، `JN70CN`، `JN70CN12`).

### "لا توجد منطقة مشتركة في الطبقة E"
المسار أطول من ضعف المدى عند ارتفاع الآثار (نحو 2 × 1062 km مع الفص عند 0° والآثار على 89.5 km): لا تستطيع قفزة تشتت نيزكي واحدة تغطيته. ورفع **زاوية ارتفاع الفص** يقصّر المدى أكثر.

### Hot A / Hot B باللون الرمادي
إنهما يقعان أصلاً **داخل فص هوائيك** عند توجيهه نحو المحطة المقابلة: لا حاجة إلى إدارته. انظر [القبة السماوية](Sky-View-ar#التنبيهات).

### الكفاءة تختلف عن MCG_MS أو MS-Soft
يستخدم YA-MS المسار الحقيقي ونموذجه الخاص؛ ومقياس OH5IY وMCG_MS غير موثّق بالتفصيل. قارن الساعات والاتجاهات العامة بدلاً من النسب المئوية المطلقة، وانظر [النموذج](Efficiency-Calculation-ar#النموذج).

### يبدو مرور حزمة GRAVES مُزاحاً
يُحسب تتابع الحزمة من ساعة الحاسوب: زامنها مع خادم NTP. كما تُزيح محطة التحكم في GRAVES التتابع أحياناً ببضع خطوات؛ والتفاصيل تنبؤ يجب تأكيده بالاستماع.

## أسئلة أخرى

**هل YA-MS مجاني؟** نعم، إنه برنامج مجاني لهواة الراديو.

**هل يتحكم في المدوِّر (rotator) أو جهاز الراديو لدي؟** لا. YA-MS أداة للتنبؤ والتخطيط؛ استخدم برنامج الأنماط الرقمية لديك (مثل MSHV أو WSJT-X) لإجراء الاتصال QSO.

**هل يعمل فوق 432 MHz؟** تتوقف قائمة النطاقات عند 432 MHz (28، 50، 70، 144، 222، 432). يقبل التنبؤ التجريبي أي تردد من 28 إلى 1300 MHz، لكن قواعد SM6FHZ التي يستخدمها مستمدة من الخبرة على 144 و432 MHz.

**حدث خطأ ما.** اكتب إلى المؤلف ذاكراً نظام تشغيلك، وإصدار YA-MS، وما فعلته: انظر [المساهمة وجهات الاتصال](Contributing-and-Contacts-ar).
