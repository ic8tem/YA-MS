[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · **Українська** · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Ефективність - пояснення

*Вкладка: Технічні документи › Ефективність - пояснення.*

[![Ефективність - пояснення](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Технічний документ *"Come YA-MS calcola l'efficienza di uno sciame"* (Як YA-MS обчислює ефективність потоку), показаний у програмі як світла сторінка. Він **крок за кроком** пояснює, як отримується ефективність, і для кожного кроку вказує, **звідки він походить**. Наразі документ **італійською мовою**; ця вікі подає його зміст українською на сторінках [Розрахунок ефективності](Efficiency-Calculation-uk#модель) і [Геометрія і загасання](Geometry-and-Path-Loss-uk).

## Позначки

Кожен крок має кольорову позначку:

| Позначка | Колір | Значення |
|---|---|---|
| **FONTE** (джерело) | синій | крок узято з цитованого джерела; число в дужках відсилає до списку наприкінці |
| **RILIEVO** (перевірка) | зелений | порівняння програми з джерелами, з результатом |
| **SCELTA** (рішення) | помаранчевий | рішення програми, не взяте з джерела: його слід перевірити досвідом в ефірі |

## Розділи

| Розділ | Вміст |
|---|---|
| 1. Вступ | Мета, позначки, що означає ефективність (OH5IY, MCG_MS; YA-MS використовує реальну трасу) |
| 2. Де відбуваються відбиття: шар E | Сліди на висоті 80–120 km; висота слідів = мода гістограми Collm (перевірка: 89,5 km 5/11/2026) |
| 3. Геометрія траси | Земля і середня точка; кут місця антени (формула статті); спільна зона та її межі; Hot A / Hot B; пелюстка антени (DL6WU, Kraus, W4RNL) |
| 4. Радіант потоку | Положення радіанта (IMO 2026/2027), дата максимуму (IMO або сонячна довгота), профіль активності |
| 5. Умова відбиття | Дзеркальне відбиття (McKinley), гаусів допуск 0,05 rad, найкращий напрямок (SM6FHZ), формула DH9GCD |
| 6. Від однієї точки до ефективності | Точки відбиття через кожні 15 km, вага кожної точки, відсоток; порівняння з QTFGUI (DJ5HG) |
| 7. Читання результатів | Бік A / B, індекс траси, кольори радіантів, зони PREV, розріз, як його бачить антена |
| 8. Робоча частота і загасання на трасі | Правила λ³ / λ², від радара до аматорського діапазону, посилання щодо загасання |
| 9. Відомі обмеження | Лише недощільні сліди, ізотропні антени, робочі значення |
| 10. Джерела | 17 пронумерованих джерел |

## Кнопки

| Кнопка | Що робить |
|---|---|
| **Експорт у Word (.docx)...** | Зберігає копію `data/efficienza_spiegazione.docx` у вибране вами місце (запропонована назва *YA-MS - calcolo dell'efficienza.docx*) |
| **Відкрити у Word** | Відкриває той самий `.docx` програмою, призначеною типово для документів Word (Word, LibreOffice, …) |

## Файли

| Файл | Вміст |
|---|---|
| `data/efficienza_spiegazione.txt` | Текст, показаний у вкладці, один блок на рядок (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Версія для Word |
| `doc/YA-MS_manuale_calcoli.docx` | **Посібник із розрахунків**: усі рівняння (редактор рівнянь Word), пронумеровані, з їхніми джерелами |

Обидва документи генеруються заново з вихідного коду командами `tools/build_spiegazione.py data` і `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
