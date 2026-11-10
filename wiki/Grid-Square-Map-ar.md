[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · **العربية** · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# خريطة المربعات

*علامة التبويب: خريطة المربعات.*

[![خريطة المربعات](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

مربعات Maidenhead (4 أحرف) التي **تم الاتصال** بها والتي **تأكدت**، مقروءة من ملف ADIF الخاص بسجلك، على خريطة لأوروبا – **علامة تبويب فرعية لكل نطاق: 50 و70 و144 و222 و432 MHz**.

## عناصر التحكم

| عنصر التحكم | وظيفته |
|---|---|
| **تحميل ملف ADIF...** | يقرأ ملف `.adi` / `.adif`. ملف ADIF الجديد **يستبدل** البيانات السابقة. |
| **مسح الذاكرة** | يحذف جميع المربعات المحمَّلة من ADIF (يطلب التأكيد). |
| الفأرة | **العجلة = تكبير، السحب = تحريك، الفأرة فوق مربع = اتصالات QSO** (حتى ستة رموز نداء مع التاريخ، و*(مؤكَّد)* عند التأكيد) |

بعد التحميل تعرض الحالة *قُرئ … QSO، … مربع QSO في نطاقات 50-432 MHz، استُبعد … QSO (نطاقات أخرى أو بلا مربع)*. ولكل خريطة نطاق التعليق *… مربعاً تم الاتصال بها، … مؤكَّدة*.

| اللون | المعنى |
|---|---|
| برتقالي | تم الاتصال |
| أخضر | مؤكَّد (QSL أو LoTW) |

## كيف يُقرأ ملف ADIF

- الحقول المستخدمة: `CALL`، `GRIDSQUARE`، `VUCC_GRIDS`، `BAND`، `FREQ`، `QSO_DATE`، `QSL_RCVD`، `LOTW_QSL_RCVD` (مواصفة ADIF).
- النطاق من `BAND`، أو من التردد: 50–54 MHz = 6 m، ‏69.9–71.5 MHz = 4 m، ‏144–148 MHz = 2 m، ‏219–225 MHz = 1.25 m، ‏420–450 MHz = 70 cm.
- يكون المربع **مؤكَّداً** إذا كان فيه اتصال QSO واحد على الأقل بقيمة `QSL_RCVD = Y` أو `LOTW_QSL_RCVD = Y`.
- تُحفظ المربعات في `data/adif_quadrati.csv` حتى تحمّل ملفاً آخر أو تضغط **مسح الذاكرة**.

لا **يتصل** YA-MS بـ LoTW: صدّر ملف ADIF من برنامج السجل لديك (أو من LoTW) وحمّله هنا.
