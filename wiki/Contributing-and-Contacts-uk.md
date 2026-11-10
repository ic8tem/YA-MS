[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · **Українська** · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [ไทย](Contributing-and-Contacts-th) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# Участь у проєкті та контакти

YA-MS удосконалюється завдяки повідомленням тих, хто користується нею в ефірі. Кожне виправлення зараховується його джерелу.

## Контакти

| | |
|---|---|
| Автор | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Як повідомити про проблему

Відкрийте **issue на GitHub** або напишіть листа, вказавши:

- операційну систему і версію YA-MS (у заголовку вікна);
- обидва локатори, діапазон і час UTC;
- що ви очікували і що побачили (знімок екрана допоможе);
- для проблем із радарами — повідомлення, показане у вкладці [Потік за радаром](Radar-Flux-uk).

## Що особливо корисно

- **Звіти з ефіру.** Години й траси, на яких ефективність або прогноз виявилися правильними — або хибними. Модель експериментальна, і її потрібно порівнювати з реальними QSO та з MCG_MS / MS-Soft.
- **Порівняння з RMOB.** Значення коефіцієнта станції K і показника k, які ви отримали за допомогою [порівняння з RMOB](Experimental-Forecasts-uk#порівняння-з-rmob), із зазначенням діапазону і станції.
- **Дані з джерелом.** Кращий дрейф радіантів, профілі активності, нові дати максимумів IMO (`data/massimi_imo.csv`), дані антен: вкажіть джерело, і його буде процитовано.
- **Зміни графіків радарів.** Якщо формат графіка Collm зміниться, копія зображення (`data/radar/`) допоможе перекалібрувати зчитування.

## Переклади

Переклади інтерфейсу — це прості текстові файли **`data/lingue/<code>.txt`** (UTF-8), і **будь-хто може їх виправляти**:

```
<Italian text><TAB><translation>
```

- Один запис на рядок; рядки, що починаються з `#`, — коментарі.
- В обох стовпцях два символи `\n` означають перенесення рядка.
- Зберігайте заповнювачі `{0}`, `{1}`, … з їхнім форматом (напр. `{0:F1}`, `{3:+0;-0}`), у порядку, якого потребує ваша мова.
- Відсутні або порожні записи показуються італійською. Список усіх ключів — `data/lingue/chiavi.txt` (генерується `tools/estrai_chiavi.py`, не редагуйте його).

Відредагуйте файл у теці `data/lingue` вашої інсталяції й перезапустіть YA-MS (або перемкніть мову), щоб побачити результат. Оскільки ці файли **замінюються новішими під час кожного оновлення**, будь ласка, також **надішліть свої виправлення** — електронною поштою або як pull request на GitHub (`data/lingue/`), — щоб вони потрапили до наступного релізу.

Ця вікі існує 36 мовами (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, ไทย, 日本語, 한국어, 中文, 中文 (繁體)); виправлення сторінок вікі також вітаються.
