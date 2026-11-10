[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · **Русский** · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [ไทย](Efficiency-Explanation-th) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Эффективность - пояснение

*Вкладка: Технические документы › Эффективность - пояснение.*

[![Эффективность - пояснение](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/ru-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/ru-3_3.png)

Технический документ *«Come YA-MS calcola l'efficienza di uno sciame»* (Как YA-MS рассчитывает эффективность потока), показываемый в программе в виде светлой страницы. Он **шаг за шагом** объясняет, как получается эффективность, и для каждого шага указывает, **откуда он взят**. Сейчас документ существует **на итальянском языке**; эта вики излагает его содержание по-русски на страницах [Расчёт эффективности](Efficiency-Calculation-ru#модель) и [Геометрия и затухание](Geometry-and-Path-Loss-ru).

## Метки

Каждый шаг снабжён цветной меткой:

| Метка | Цвет | Значение |
|---|---|---|
| **FONTE** (источник) | синий | шаг основан на цитируемом источнике; число в скобках ссылается на список в конце |
| **RILIEVO** (проверка) | зелёный | сравнение программы с источниками и его результат |
| **SCELTA** (выбор) | оранжевый | выбор программы, не взятый из источника: требует проверки опытом работы в эфире |

## Главы

| Глава | Содержание |
|---|---|
| 1. Введение | Цель, метки, что означает эффективность (OH5IY, MCG_MS; YA-MS использует реальную трассу) |
| 2. Где происходят отражения: слой E | Следы на высоте 80–120 km; высота следов = мода гистограммы Collm (проверка: 89,5 km 5/11/2026) |
| 3. Геометрия трассы | Земля и средняя точка; угол места антенны (формула статьи); общая зона и её границы; Hot A / Hot B; ДН антенны (DL6WU, Kraus, W4RNL) |
| 4. Радиант потока | Положение радианта (IMO 2026/2027), дата максимума (IMO или по солнечной долготе), профиль активности |
| 5. Условие отражения | Зеркальное отражение (McKinley), гауссов допуск 0,05 rad, лучшее направление (SM6FHZ), формула DH9GCD |
| 6. От точки к эффективности | Точки отражения через каждые 15 km, вес каждой точки, проценты; сравнение с QTFGUI (DJ5HG) |
| 7. Чтение результатов | Сторона A / B, индекс трассы, цвета радиантов, зоны PREV, разрез, видимый от антенны |
| 8. Рабочая частота и затухание | Правила λ³ / λ², от радара к любительскому диапазону, данные о затухании на трассе |
| 9. Известные ограничения | Только ненасыщенные следы, изотропные антенны, рабочие значения |
| 10. Источники | 17 пронумерованных источников |

## Кнопки

| Кнопка | Что делает |
|---|---|
| **Экспорт в Word (.docx)...** | Сохраняет копию `data/efficienza_spiegazione.docx` в выбранное место (предлагаемое имя *YA-MS - calcolo dell'efficienza.docx*) |
| **Открыть в Word** | Открывает тот же `.docx` программой, назначенной по умолчанию для документов Word (Word, LibreOffice, …) |

## Файлы

| Файл | Содержание |
|---|---|
| `data/efficienza_spiegazione.txt` | Текст, показываемый на вкладке, по одному блоку на строку (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Версия для Word |
| `doc/YA-MS_manuale_calcoli.docx` | **Руководство по расчётам**: все уравнения (редактор формул Word), пронумерованные, с источниками |

Оба документа пересоздаются из исходного кода командами `tools/build_spiegazione.py data` и `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
