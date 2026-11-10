[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · **العربية** · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# الكفاءة - شرح

*علامة التبويب: وثائق تقنية › الكفاءة - شرح.*

[![الكفاءة - شرح](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

وثيقة تقنية بعنوان *"Come YA-MS calcola l'efficienza di uno sciame"* (كيف يحسب YA-MS كفاءة الزخة)، تُعرض داخل البرنامج كصفحة فاتحة. تشرح **خطوةً بخطوة** كيف تُستخرج الكفاءة، وتذكر لكل خطوة **من أين تأتي**. يعرضها البرنامج **بلغة الواجهة** (بجميع اللغات الـ36)، وكذلك دليل الحسابات؛ وتعرض هذه الويكي محتواها أيضاً في [حساب الكفاءة](Efficiency-Calculation-ar#النموذج) و[الهندسة والتوهين](Geometry-and-Path-Loss-ar).

## التسميات

تحمل كل خطوة تسمية ملونة:

| التسمية | اللون | المعنى |
|---|---|---|
| **FONTE** (مصدر) | أزرق | تعتمد الخطوة على مصدر مذكور؛ يشير الرقم بين معقوفين إلى القائمة في النهاية |
| **RILIEVO** (تحقق) | أخضر | مقارنة بين البرنامج والمصادر، مع النتيجة |
| **SCELTA** (اختيار) | برتقالي | اختيار خاص بالبرنامج، غير مأخوذ من مصدر: يجب التحقق منه بالخبرة على الهواء |

## الفصول

| الفصل | المحتوى |
|---|---|
| 1. مقدمة | الغرض، التسميات، معنى الكفاءة (OH5IY، ‏MCG_MS؛ يستخدم YA-MS المسار الحقيقي) |
| 2. أين تحدث الانعكاسات: الطبقة E | الآثار على 80–120 km؛ ارتفاع الآثار = منوال المدرج التكراري لـ Collm (تحقق: 89.5 km في 5/11/2026) |
| 3. هندسة المسار | الأرض ونقطة المنتصف؛ زاوية ارتفاع الهوائي (صيغة المقال)؛ المنطقة المشتركة وحدودها؛ Hot A / Hot B؛ فص الهوائي (DL6WU، ‏Kraus، ‏W4RNL) |
| 4. نقطة إشعاع الزخة | موضع نقطة الإشعاع (IMO 2026/2027)، تاريخ الذروة (IMO أو خط الطول الشمسي)، منحنى النشاط |
| 5. شرط الانعكاس | الانعكاس المرآوي (McKinley)، تفاوت غاوسي 0.05 rad، أفضل توجيه (SM6FHZ)، صيغة DH9GCD |
| 6. من نقطة واحدة إلى الكفاءة | نقاط الانعكاس كل 15 km، وزن كل نقطة، النسبة المئوية؛ المقارنة مع QTFGUI (DJ5HG) |
| 7. قراءة النتائج | الجانب A / B، مؤشر المسار، ألوان نقاط الإشعاع، مناطق PREV، المقطع كما يُرى من الهوائي |
| 8. تردد العمل وتوهين المسار | قاعدتا λ³ / λ²، من الرادار إلى نطاق الهواة، مراجع توهين المسار |
| 9. الحدود المعروفة | الآثار منخفضة الكثافة فقط، هوائيات متناحية، قيم العمل |
| 10. المصادر | 17 مصدراً مرقَّماً |

## الأزرار

| الزر | وظيفته |
|---|---|
| **تصدير إلى Word (.docx)...** | يحفظ نسخة من `data/efficienza_spiegazione.docx` حيث تختار (الاسم المقترح *YA-MS - calcolo dell'efficienza.docx*) |
| **فتح في Word** | يفتح ملف `.docx` نفسه بالبرنامج الافتراضي لمستندات Word (Word، ‏LibreOffice، …) |

## الملفات

| الملف | المحتوى |
|---|---|
| `data/efficienza_spiegazione.txt` | النص المعروض في علامة التبويب، كتلة واحدة لكل سطر (`TITLE`، `SUB`، `H1`، `H2`، `P`، `TAG|FONTE|…`، `TAG|RILIEVO|…`، `TAG|SCELTA|…`، `EQ`، `LI`، `SRC`) |
| `data/efficienza_spiegazione.docx` | نسخة Word |
| `data/spiegazione/efficienza_spiegazione_<code>.txt` / `.docx` | الوثيقة نفسها باللغات الـ35 الأخرى (مثلاً `_en`, `_de`, `_pt-br`) |
| `doc/YA-MS_manuale_calcoli.docx` | **دليل الحسابات** (بالإيطالية): جميع المعادلات (محرر معادلات Word)، مرقَّمة، مع مصادرها |
| `doc/manuali/YA-MS_manuale_calcoli_<code>.docx` | دليل الحسابات باللغات الـ35 الأخرى |

تُعاد توليد الوثيقتين من المصدر بالأمرين `tools/build_spiegazione.py data [code]` و`node tools/build_manuale.js <file.docx> [code]`. الترجمات موجودة في `tools/traduzioni_doc/` (ويعيد `tools/build_documenti.sh` توليد جميع اللغات).
