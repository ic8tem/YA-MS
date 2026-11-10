[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · **العربية** · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh)

# المساهمة وجهات الاتصال

يتحسن YA-MS بفضل بلاغات من يستخدمونه على الهواء. كل تصحيح يُنسب إلى مصدره.

## جهات الاتصال

| | |
|---|---|
| المؤلف | Costantino Cerrotta **IC8TEM** |
| البريد الإلكتروني | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## الإبلاغ عن مشكلة

افتح **issue على GitHub** أو اكتب رسالة بريد إلكتروني تتضمن:

- نظام التشغيل وإصدار YA-MS (في عنوان النافذة)؛
- محددي الموقع، والنطاق، ووقت UTC؛
- ما كنت تتوقعه وما رأيته (لقطة شاشة تساعد)؛
- لمشكلات الرادار، الرسالة المعروضة في علامة التبويب [تدفق الرادار](Radar-Flux-ar).

## ما هو مفيد بشكل خاص

- **بلاغات من الهواء.** الساعات والمسارات التي كانت فيها الكفاءة أو التنبؤ صحيحة – أو خاطئة. النموذج تجريبي ويحتاج إلى مقارنة مع اتصالات QSO حقيقية ومع MCG_MS / MS-Soft.
- **المقارنات مع RMOB.** قيم معامل المحطة K والأس k التي وجدتها عبر [المقارنة مع RMOB](Experimental-Forecasts-ar#المقارنة-مع-rmob)، مع ذكر نطاقك ومحطتك.
- **بيانات مع مصدرها.** انجرافات أفضل لنقاط الإشعاع، منحنيات النشاط، تواريخ ذروة جديدة من IMO (`data/massimi_imo.csv`)، بيانات الهوائيات: أرفق المصدر وسيُذكر.
- **تغييرات مخططات الرادار.** إذا تغيّر تنسيق مخطط Collm، فإن نسخة من الصورة (`data/radar/`) تساعد على إعادة معايرة القراءة.

## الترجمات

ترجمات الواجهة ملفات نصية بسيطة في **`data/lingue/<code>.txt`** ‏(UTF-8) و**يمكن لأي شخص تصحيحها**:

```
<Italian text><TAB><translation>
```

- مُدخل واحد في كل سطر؛ والأسطر التي تبدأ بـ `#` تعليقات.
- في كلا العمودين يعني الحرفان `\n` فاصل سطر.
- حافظ على العناصر النائبة `{0}`، `{1}`، … مع تنسيقها (مثلاً `{0:F1}`، `{3:+0;-0}`)، بالترتيب الذي تحتاجه لغتك.
- المُدخلات المفقودة أو الفارغة تُعرض بالإيطالية. قائمة جميع المفاتيح هي `data/lingue/chiavi.txt` (يولّدها `tools/estrai_chiavi.py`، لا تعدّلها).

عدّل الملف في مجلد `data/lingue` في تثبيتك وأعد تشغيل YA-MS (أو بدّل اللغة) لرؤية النتيجة. ولأن هذه الملفات **تُستبدل بنسخ أحدث عند كل تحديث**، يُرجى أيضاً **إرسال تصحيحاتك** – بالبريد الإلكتروني أو كطلب سحب (pull request) على GitHub ‏(`data/lingue/`) – لتدخل في الإصدار التالي.

هذه الويكي متاحة English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文؛ والتصحيحات على صفحات الويكي مرحَّب بها أيضاً.
