[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Русский](Grid-Square-Map-ru) · **Українська** · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# Мапа квадратів

*Вкладка: Мапа квадратів.*

[![Мапа квадратів](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Квадрати Maidenhead (4 символи), які ви **зробили** й **підтвердили**, зчитані з файлу ADIF вашого журналу, на мапі Європи – **окрема підвкладка для кожного діапазону: 50, 70, 144, 222 і 432 MHz**.

## Керування

| Елемент | Що робить |
|---|---|
| **Завантажити файл ADIF...** | Зчитує файл `.adi` / `.adif`. Новий ADIF **замінює** попередні дані. |
| **Очистити пам'ять** | Видаляє всі квадрати, завантажені з ADIF (просить підтвердження). |
| Миша | **Коліщатко = масштаб, перетягування = зсув, курсор над квадратом = QSO** (до шести позивних з датою, *(підтверджено)*, якщо підтверджено) |

Після завантаження рядок стану показує *прочитано … QSO, … квадратів-QSO в діапазонах 50-432 MHz, відкинуто … QSO (інші діапазони або без квадрата)*. Мапа кожного діапазону має підпис *зроблено квадратів …, підтверджено …*.

| Колір | Значення |
|---|---|
| Помаранчевий | зроблено |
| Зелений | підтверджено (QSL або LoTW) |

## Як зчитується ADIF

- Використовувані поля: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (специфікація ADIF).
- Діапазон — з `BAND` або за частотою: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Квадрат **підтверджено**, якщо хоча б одне QSO в ньому має `QSL_RCVD = Y` або `LOTW_QSL_RCVD = Y`.
- Квадрати зберігаються в `data/adif_quadrati.csv`, доки ви не завантажите інший файл або не натиснете **Очистити пам'ять**.

YA-MS **не** підключається до LoTW: експортуйте ADIF зі своєї програми ведення журналу (або з LoTW) і завантажте його тут.
