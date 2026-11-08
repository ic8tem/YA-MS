[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · **العربية** · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh)

# الإعدادات ومجلد البيانات

## شريط علامات التبويب

عند الطرف الأيمن من شريط علامات التبويب، من اليمين إلى اليسار:

| عنصر التحكم | وظيفته |
|---|---|
| **اللغة** (قائمة) | لغة الواجهة؛ انظر [اللغة](#اللغة) |
| **السمة** (قائمة) | نظام الألوان؛ انظر [أنظمة الألوان](#أنظمة-الألوان) |
| **عناصر التحكم ▴ / ▾** | يطوي صفوف عناصر التحكم الثلاثة فوق علامات التبويب أو يبسطها؛ انظر [الخط وعناصر التحكم](#الخط-وعناصر-التحكم) |

يؤدي تغيير اللغة أو السمة إلى حفظ الإعدادات و**إعادة بناء النافذة** في الموضع والحجم نفسيهما، وعلى علامة التبويب نفسها: لا حاجة إلى إعادة التشغيل.

## اللغة

ست لغات للواجهة:

| اللغة | الرمز | الملف |
|---|---|---|
| Italiano | `it` | لا يوجد: الإيطالية هي اللغة الأساسية (المفاتيح) |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

عند التشغيل الأول يستخدم YA-MS **لغة النظام** إن كانت إحدى هذه اللغات، وإلا فالإيطالية. تتبع الأرقام والتواريخ اللغة المختارة (مثلاً النقطة العشرية في الإنجليزية، والفاصلة في الإيطالية والألمانية). أي نص ناقص في ملف الترجمة يُعرض بالإيطالية. على Linux تحتاج اليابانية إلى خطوط مناسبة: انظر [حل المشكلات](Troubleshooting-FAQ-ar#linux-النص-الياباني-يظهر-مربعات).

وثيقة [الكفاءة - شرح](Efficiency-Explanation-ar) ودليل الحسابات بالإيطالية.

## أنظمة الألوان

تقدّم قائمة **السمة** 12 نظاماً، هي نفسها الموجودة في برنامج EME الخاص بالمؤلف YAEC إضافة إلى لوحة ألوان YA-MS الأصلية:

| النظام | الوصف |
|---|---|
| **فاتح** | الافتراضي |
| **ليلي** | درجات أزرق داكنة، للاستخدام ليلاً |
| **أسود** | خلفية سوداء، للظلام ولشاشات OLED |
| باستيل أزرق فاتح · باستيل برتقالي · باستيل زبرجدي · باستيل أخضر · باستيل وردي · باستيل ليلكي · باستيل نيلي · باستيل بني | ثمانية أنظمة باستيل فاتحة |
| **أثر نيزكي** | الأسلوب الأصلي لـ YA-MS (حتى الإصدار 1.2.0): بنفسجي ليلي مع أزرق فاتح وبنفسجي وأخضر فاتح وأصفر وبرتقالي |

ينطبق النظام على جميع علامات التبويب ويُحفظ في `config.ini` (المفتاح `tema`).

## الخط وعناصر التحكم

- **الخط** (في نهاية الصف الأول من عناصر التحكم): يكبّر **كل النصوص** من **100 إلى 300 %** بخطوات من 10 %؛ وتحافظ الخطوط والدوائر والخرائط على حجمها. مع الخطوط الكبيرة تلتف علامات التبويب على سطر ثانٍ وتكبر البطاقات.
- **عناصر التحكم**: مع الخطوط الكبيرة أو الشاشة الصغيرة، اطوِ صفوف عناصر التحكم الثلاثة لإفساح المجال للخرائط والمخططات. وتُحفظ الحالة.

## مجلد البيانات

جميع البيانات والإعدادات في مجلد **`data`** واحد **بجانب البرنامج** – لا AppData ولا مجلدات نظام:

| النظام | البرنامج | البيانات |
|---|---|---|
| Windows (مثبِّت) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (محمول) | حيثما فككت ضغطه | `data` بجانب `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (بجانب التطبيق) |

عند بدء التشغيل ينشئ البرنامج المجلد عند الحاجة وينسخ فقط ملفات البدء **الناقصة**: الملفات التي عدّلتها لا يُكتب فوقها أبداً. ملفات الترجمة في `data/lingue` ملفات خاصة بالبرنامج وتُستبدل عندما تكون ملفات الإصدار الجديد أحدث.

### ملفات يمكنك تعديلها

| الملف | المحتوى |
|---|---|
| `sciami.csv` | فهرس الزخات (قيم IMO وقيم العمل)؛ انظر [الزخات](Showers-ar#تعديل-الفهرس) |
| `massimi_imo.csv` | تواريخ الذروات وأوقاتها المنشورة من IMO ‏(2026، 2027): **أضف السنوات الجديدة** هنا |
| `ant_radiante.csv` | موضع مصدر مقابل الشمس (الجدول 6 من IMO) |
| `fonti_radar.csv` | عناوين الرادارات؛ `attivo=1` للتنزيل، و`0` للتجاهل |
| `regole_sperimentali.csv` | الثوابت والقواعد المستخدمة، كل منها مع مصدره (مرجع) |
| `lingue/<code>.txt` | ترجمات الواجهة؛ انظر [المساهمة](Contributing-and-Contacts-ar#الترجمات) |
| `config.ini` | الإعدادات (انظر أدناه) |

### ملفات ينشئها البرنامج

| الملف / المجلد | المحتوى |
|---|---|
| `config.ini` | الإعدادات |
| `flusso_collm.csv` | أرشيف ساعي لتدفق Collm |
| `quote_collm.csv` | أرشيف ارتفاعات الآثار |
| `radar/` | آخر صور الرادار وملفات RMOB |
| `mappa/` | السواحل والحدود من Natural Earth (تُنزَّل عند التشغيل الأول) |
| `adif_quadrati.csv` | المربعات من آخر ملف ADIF محمَّل |
| `efficienza_spiegazione.txt`، `.docx` | [وثيقة الشرح](Efficiency-Explanation-ar) |

## config.ini

نص بسيط، `key=value` واحد في كل سطر (الأسطر التي تبدأ بـ `#` أو `;` تعليقات). يكتبه البرنامج عند إغلاقه، لذا **عدّله وYA-MS مغلق**. المفاتيح التي قد ترغب في معرفتها:

| المفتاح | الافتراضي | المعنى |
|---|---|---|
| `mio_locator`، `mia_quota_m` | JN70CN، 62 | محدد موقعك وارتفاعك (m) |
| `dx_locator`، `dx_quota_m` | JO62QM، 50 | محدد موقع المحطة المقابلة وارتفاعها (m) |
| `banda_MHz` | 144 | النطاق (28، 50، 70، 144، 222، 432) |
| `quota_scie_km`، `quota_da_radar` | 90، 1 | ارتفاع الآثار (km)؛ 1 = استخدام منوال Collm |
| `elevazione_lobo_gradi` | 0 | زاوية ارتفاع الفص (°) |
| `boom_m` | 4.6 | طول ذراع Yagi ‏(m) |
| `hot_spot_km` | 150 | بُعد Hot A / Hot B عن نقطة المنتصف (30–400 km) |
| `lingua` | النظام / `it` | رمز اللغة (`it`، `en`، `ru`، `ja`، `de`، `nl`) |
| `tema` | `chiaro` | نظام الألوان: `chiaro` (فاتح)، `scuro` (ليلي)، `nero` (أسود)، `pastello-azzurro`، `pastello-arancione`، `pastello-acquamarina`، `pastello-verde`، `pastello-rosa`، `pastello-lilla`، `pastello-indaco`، `pastello-marrone`، `scia` (أثر نيزكي) |
| `carattere_pct` | 100 | حجم الخط (100–300 %) |
| `comandi_visibili` | 1 | 1 = صفوف عناصر التحكم ظاهرة، 0 = مطوية |
| `mostra_mappa`، `vista_alto` | 1، 1 | خريطة أوروبا، والمنظر العلوي في القبة السماوية |
| `aggiornamento_automatico` | 1 | فحص تلقائي للمصادر كل 5 دقائق |
| `esponente_lambda` | 3 | أس λ في علامة التبويب تدفق الرادار |
| `potenza_W`، `guadagno_dBi`، `sensibilita_dBm`، `densita_esponente_q` | 400، 14، −130، 14 | مُدخلات ميزانية الوصلة |
| `prev_frequenza_MHz`، `prev_esponente`، `prev_fattore_stazione` | 144، 3، 1 | التنبؤ التجريبي: التردد، k، ‏K |
| `rmob_osservatore` | فارغ | اسم راصد RMOB |
| `rmob_automatico` | 0 | الجلب التلقائي لـ RMOB (فعّله فقط بإذن من RMOB) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | قالب عنوان RMOB |
| `graves_sequenza` | 0 | تتابع حزمة GRAVES: ‏0 = 0.8 s ‏(2021)، 1 = 3.2 s ‏(2007) |

## الخصوصية

لا يجمع YA-MS أي بيانات ولا يعرض أي إعلانات. لا يتصل بالإنترنت إلا لتنزيل بيانات عامة: صور رادارَي Collm وSodankylä، وخريطة Natural Earth (عند التشغيل الأول)، وملف RMOB إذا طلبته.
