[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · **العربية** · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# جمع البيانات

*علامة التبويب: مباشر وبيانات الوقت الفعلي › جمع البيانات.*

[![جمع البيانات](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## أربعة مصادر

تجمع علامة التبويب **بلاغات التشتت النيزكي** من ثلاثة تدفقات telnet ومن تغذية PSKReporter MQTT، لكل منها علامة تبويب فرعية خاصة:

| علامة التبويب الفرعية | الافتراضي | ملاحظات |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | cluster من اختيارك. في ON0DXK تكون نطاقات VHF مرشَّحة: فعّلها بالأمر `set/filter dxbm/pass 6` (ثم 4، 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY، 7001 = FT8). نادراً ما تفك أجهزة skimmer أنماط MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | cluster ‏DM4X الذي ينقل بلاغات **PSKReporter**: تصل إليه فكّات MSK144 من WSJT-X وMSHV. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | بلاغات PSKReporter المباشرة عبر **MQTT** (خدمة من M0LTE): بلا تسجيل دخول، ويحمل كل بلاغ مسبقاً محددات مواقع المحطة المرسِلة والمحطة المستقبِلة. المواضيع الافتراضية: MSK144 على 6 m و4 m و2 m و1.25 m و70 cm وFSK441 على 2 m (`pskr/filter/v2/band/mode/#`)؛ ويستعيدها زر *المواضيع الافتراضية*. |
| **بلاغات MS المجمَّعة** | – | جدول البلاغات المقبولة، الأحدث أولاً. |

لكل تدفق: المضيف، والمنفذ، والأوامر المرسلة بعد تسجيل الدخول، و*إعادة الاتصال*، و*الاتصال عند بدء التشغيل*، ووحدة تحكم (console)، وسطر لإرسال الأوامر. اكتب **رمز النداء لتسجيل الدخول** في الأعلى. لمصدر MQTT: المضيف، والمنفذ، والمواضيع (موضوع في كل سطر أو مفصولة بـ `;`)، و*إعادة الاتصال* و*الاتصال عند بدء التشغيل* (معطّل افتراضياً)، ووحدة تحكم تعرض البلاغات المستلمة؛ وتمر بلاغاته عبر المرشِّح نفسه. يعرض شريط حالة المصادر الأربعة (نقطة خضراء = متصل). تبقى الجلسات مفتوحة عند تغيير اللغة أو نظام الألوان.

## المرشِّح (40 % من النافذة)

- **مرشِّح محلي اختياري:** تُستبعد فوراً أسطر cluster التي يقل ترددها عن **27990.0 kHz** (لا تُعرض ولا تُحفظ).
- تُستبعد نقاط CW فورًا (CW أو WPM في التعليق، أو 28000-28070 kHz): لا تظهر في وحدة التحكم ولا تُحفظ، ما لم تكن موسومة <MS>. يمكن إلغاء تفعيل المربع.
- **المعيار الأول – الترددات النموذجية لـ MS:** ‏50190–50300، 70100–70400، 144290–144399 kHz. يُقبل البلاغ الواقع في هذه النوافذ حتى دون ذكر اسم النمط، ما لم يُعلن التعليق عن انتشار آخر: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. يمكن تعديل النوافذ والوسوم.
- **المعيار الثاني – أنماط MS:** خارج النوافذ، أو مع أحد تلك الوسوم، لا يُحتفظ بالبلاغ إلا إذا تضمن **MSK144 أو FSK441 أو FSK41 أو PSK2K أو JTMS أو JT6M** (أنماط رقمية لا تُستخدم إلا لـ MS) أو **\<MS\>**، بأحرف كبيرة أو صغيرة أو مختلطة. يمكن تعطيل الكلمات وإضافتها وحذفها؛ ولكل منها عدّاد.
- **النطاقات** 28، 50، 70، 144، 222، 432 MHz؛ **اختبار المرشِّح** على سطر ملصوق؛ **العدّادات**.

## محددات الموقع والتخزين

تؤخذ محددات الموقع المفقودة، أو المؤلفة من 4 أحرف فقط، من أرشيف **CALL3** (`data/call3.txt`، ملف JTDX، أكثر من مليون رمز نداء)، الذي تكون له الأولوية دائماً على محدد موقع من 4 أحرف. تُحفظ البلاغات المقبولة في `data/spot_ms`، ملف CSV واحد لكل يوم، وتغذّي خريطة [الحركة مباشرةً](Live-Traffic-ar).
