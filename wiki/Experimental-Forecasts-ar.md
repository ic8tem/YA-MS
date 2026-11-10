[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · **العربية** · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [ไทย](Experimental-Forecasts-th) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# تنبؤات تجريبية

*علامة التبويب: الحساب التنبؤي › تنبؤات تجريبية.*

[![تنبؤات تجريبية](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

تحوّل علامة التبويب هذه أعداد الشهب التي يرصدها **رادار Collm (36.2 MHz)** إلى تقدير لـ**عدد الانعكاسات في الساعة على نطاق هواة** (144 MHz افتراضياً، أو أي تردد من 28 إلى 1300 MHz)، وتتنبأ بـ**الساعات الـ 24 القادمة** لمسارك، وتتيح لك **مقارنة** التقدير مع راصد **RMOB** – مثلاً راصد يستمع إلى GRAVES على 143.050 MHz.

> كل ما هنا **تجريبي**: قاعدة التردد قاعدة تجريبية، ومعامل المحطة يعتمد على محطتك. استخدم الأرقام للمقارنة بين الساعات والأيام، وتحقق منها على الهواء.

## عناصر التحكم

| عنصر التحكم | الافتراضي | وظيفته |
|---|---|---|
| **التردد المستهدف MHz** | 144 | تردد التنبؤ (28–1300 MHz) |
| **أُس λ^k** | 3 | الأس k لقاعدة التردد (SM6FHZ: ‏3) |
| **معامل المحطة K** | 1 | يأخذ في الحسبان محطة الاستقبال (القدرة، الهوائيات)؛ يُستنتج بالمقارنة مع راصد RMOB على النطاق نفسه |
| **تحميل ملف RMOB من القرص...** | | يقرأ ملف RMOB نصياً شهرياً (انظر أدناه) |
| **استنتاج الأُس من ملف RMOB** | | يُوفّق k من الساعات المشتركة بين Collm وRMOB |
| **راصد RMOB** | فارغ | اسم الراصد كما يظهر في اسم الملف (مثلاً `NAME_112026rmob.TXT` → `NAME`) |
| **تنزيل RMOB الآن** | | ينزّل مرة واحدة ملف الشهر الحالي لذلك الراصد |
| **جلب تلقائي كل 5 دقائق (فعّله فقط بإذن من RMOB)** | **معطَّل** | انظر [RMOB والبرامج الآلية](#rmob-والبرامج-الآلية) |

يعرض السطر البرتقالي تحت عناصر التحكم القاعدة بالأرقام الحالية، مثلاً *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*، وتحويل المدة، وأقصى نبضة وفق IARU عند ذلك التردد.

## من الرادار إلى نطاق الهواة

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}\sec^2\varphi
```

**المصدر:** SM6FHZ، *"432 MHz Meteorscatter, Challenges and Techniques"*، 45th Nordic VUSHF، مايو 2025 – يتناسب عدد الانعكاسات وشدتها مع **λ³**، ومدتها مع **λ²** (432 MHz أدنى من 144 MHz بـ 14–15 dB وتدوم 1/9). **التحقق:** في معادلة McKinley تمثّل λ³ قدرة أثر واحد منخفض الكثافة، لا عدد الآثار؛ ومع مؤشر كتلة 2 يتناسب عدد الآثار فوق عتبة ثابتة تقريباً مع λ^1.5 ‏(IZ5TEK؛ OH5IY). يحتفظ البرنامج بـ k = 3، وهي القاعدة التجريبية لـ SM6FHZ، ويصرّح بذلك؛ وقيمة k المناسبة لمحطتك تأتي من المقارنة مع RMOB. وفي التشتت الأمامي تزداد المدة أيضاً مع sec²φ ‏(McKinley؛ OH5IY): يقيس Collm في التشتت الخلفي (φ = 0)، لذا يضرب التنبؤ في sec²φ عند نقطة منتصف المسار (×4 عند 60°، ×8.5 عند 70°، ×33 عند 80°). مع k = 3، تصبح 1000 شهاب/ساعة في Collm نحو **16 انعكاساً/ساعة عند 144 MHz**؛ ويعدّ راصدو RMOB لـ GRAVES على 143.050 MHz عادةً **من 20 إلى 140 صدى/ساعة** (نشرة RMOB، يونيو 2018): رتبة المقدار متوافقة، والفرق هو معامل المحطة K. (المعادلتان 44–45 في الدليل.)

## الساعات الـ 24 القادمة

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**الاستمرارية:** القيمة المحوَّلة للساعة نفسها من اليوم السابق (أو من قبل يومين إن لم تتوفر)، مصحَّحة بتغيّر **مؤشر زخات المسار** I (Σ ZHR × الكفاءة، انظر [حساب الكفاءة](Efficiency-Calculation-ar#النموذج)). يمثّل الثابت 10 خلفية الشهب المتفرقة ويحدّ من التصحيح عندما يكون المؤشر صغيراً. *اختيار خاص بالبرنامج (المعادلة 47 في الدليل).*

| اللوحة | المحتوى |
|---|---|
| **مقيس في Collm ومحوَّل إلى f MHz - أمس واليوم (UTC)** | شهب/ساعة من رادار Collm؛ القيم المحوَّلة (برتقالي، المقياس الأيمن)؛ أعداد RMOB إن حُمِّلت (أخضر، المقياس الأيمن) |
| **تنبؤ تجريبي للساعات الـ 24 القادمة عند f MHz لـ …** | الانعكاسات المتنبأ بها/ساعة (أعمدة) ومؤشر زخات المسار (المقياس الأيمن) |
| الجدول | وقت UTC · ‏Collm في الساعة نفسها · محوَّل · مؤشر زخات المسار · التنبؤ /ساعة · **التقييم** |

**التقييم:** *جيد* عندما يبلغ التنبؤ 1.3 × متوسط الـ 24 ساعة على الأقل، و*متوسط* ابتداءً من 0.8 ×، و*ضعيف* دون ذلك. يظهر التنبؤ نفسه في بطاقة **تنبؤ تجريبي** وفي الصف البرتقالي من [حساب الكفاءة](Efficiency-Calculation-ar)، وهو أساس الأصداء المتوقعة في علامة التبويب [رادار GRAVES](GRAVES-Radar-ar#الأصداء-المتوقعة-تجريبي).

## المقارنة مع RMOB

يجمع [RMOB](https://www.rmob.org) ‏(Radio Meteor Observatories On Line، ‏Pierre Terrier) الأعداد الساعية للشهب من الراصدين الراديويين؛ ويستمع كثيرون منهم في إيطاليا إلى GRAVES على 143.050 MHz (القبة الفلكية في البندقية، وفاينزا، وروفيريتو وغيرها).

**قراءة ملفات RMOB.** يُقبل تنسيقان نصيان:

| التنسيق | الشكل | ملاحظات |
|---|---|---|
| ملف شهري (Colorgramme / Spectrum Lab) | صف لكل يوم، `day| n| n| …` مع 24 قيمة ساعية | الملف المعتاد `NAME_MMYYYYrmob.TXT` |
| جدول النشرة | ترويسة ` UT |  1   2   3 …`، وصفوف `0h|175 166 …` | إذا تضمّن الملف عدة راصدين فإنهم يُقرؤون واحداً تلو الآخر: استخدم ملفاً لراصد واحد |

يؤخذ الشهر والسنة من اسم الملف (`…_MMYYYYrmob…`) أو من الترويسة؛ وإلا يُستخدم الشهر الحالي (ويذكر البرنامج ذلك).

**توفيق الأس.** مع K = 1، من وسيط نسب RMOB/Collm على الساعات المشتركة (3 على الأقل):

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*اختيار خاص بالبرنامج (المعادلة 46 في الدليل).* يعرض مربع الحوار الساعات المشتركة، والنسبة الوسيطة، وk؛ **نعم** يطبّق k (ويضبط K = 1)، و**لا** يُبقي k = 3 – ثم اضبط K يدوياً على القيمة المقترحة في مربع الحوار نفسه.

## RMOB والبرامج الآلية

يطلب RMOB من **البرامج الآلية عدم جلب ملفاته**. لهذا السبب يكون **الجلب التلقائي معطَّلاً** عند البدء، ولا ينبغي تفعيله **إلا بعد طلب الإذن من RMOB**. ومن دونه يمكنك دائماً استخدام **تحميل ملف RMOB من القرص...** أو الضغط على **تنزيل RMOB الآن** عند الحاجة.

عنوان التنزيل قالب في `config.ini` (المفتاح `rmob_url`، والافتراضي `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`، حيث `{NOME}` هو الراصد و`{MMAAAA}` الشهر والسنة)؛ وتُحفظ الملفات المنزَّلة في `data/radar/`.
