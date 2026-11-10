[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-BR) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · **Русский** · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [ไทย](Contributing-and-Contacts-th) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-TW)

# Участие и контакты

YA-MS совершенствуется благодаря сообщениям тех, кто пользуется ею в эфире. Каждое исправление сопровождается ссылкой на его источник.

## Контакты

| | |
|---|---|
| Автор | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Как сообщить о проблеме

Откройте **issue на GitHub** или напишите письмо, указав:

- операционную систему и версию YA-MS (в заголовке окна);
- оба локатора, диапазон и время UTC;
- что вы ожидали и что увидели (снимок экрана поможет);
- для проблем с радарами – сообщение, показанное на вкладке [Поток по радару](Radar-Flux-ru).

## Что особенно полезно

- **Отчёты о работе в эфире.** Часы и трассы, для которых эффективность или прогноз оказались верными – или неверными. Модель экспериментальная и нуждается в сравнении с реальными QSO и с MCG_MS / MS-Soft.
- **Сравнения с RMOB.** Значения коэффициента станции K и показателя k, найденные вами с помощью [сравнения с RMOB](Experimental-Forecasts-ru#сравнение-с-rmob), с указанием диапазона и станции.
- **Данные с источником.** Более точные смещения радиантов, профили активности, новые даты максимумов IMO (`data/massimi_imo.csv`), данные антенн: укажите источник, и он будет процитирован.
- **Изменения графиков радаров.** Если формат графика Collm изменится, копия изображения (`data/radar/`) поможет перекалибровать считывание.

## Переводы

Переводы интерфейса – это обычные текстовые файлы **`data/lingue/<code>.txt`** (UTF-8), и **исправить их может каждый**:

```
<Italian text><TAB><translation>
```

- Одна запись на строку; строки, начинающиеся с `#`, – комментарии.
- В обоих столбцах два символа `\n` означают перевод строки.
- Сохраняйте подстановки `{0}`, `{1}`, … с их форматом (например, `{0:F1}`, `{3:+0;-0}`), в том порядке, который нужен вашему языку.
- Отсутствующие или пустые записи показываются на итальянском. Список всех ключей – `data/lingue/chiavi.txt` (создаётся `tools/estrai_chiavi.py`, не редактируйте его).

Отредактируйте файл в папке `data/lingue` вашей установки и перезапустите YA-MS (или переключите язык), чтобы увидеть результат. Поскольку эти файлы **заменяются более новыми при каждом обновлении**, пожалуйста, также **присылайте свои исправления** – по e-mail или в виде pull request на GitHub (`data/lingue/`), – чтобы они вошли в следующий выпуск.

Эта вики существует на 36 языках (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, ไทย, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文, 中文 (繁體)); исправления страниц вики также приветствуются.
