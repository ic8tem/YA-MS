[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · **Українська** · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Збір даних

*Вкладка: Наживо та дані в реальному часі › Збір даних.*

[![Збір даних](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Чотири джерела

Вкладка збирає **споти meteor scatter** із трьох telnet-потоків і з потоку PSKReporter MQTT, кожне джерело у власній підвкладці:

| Підвкладка | Типово | Примітки |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Кластер на ваш вибір. На ON0DXK діапазони VHF відфільтровано: увімкніть їх командою `set/filter dxbm/pass 6` (потім 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Скімери рідко декодують режими MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Кластер DM4X зі спотами **PSKReporter**: сюди надходять декодування MSK144 з WSJT-X і MSHV. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Споти PSKReporter у реальному часі через **MQTT** (сервіс M0LTE): без входу, кожен спот уже містить локатори передавальної та приймальної станції. Теми за замовчуванням: MSK144 на 6 m, 4 m, 2 m, 1,25 m, 70 cm і FSK441 на 2 m (`pskr/filter/v2/band/mode/#`); кнопка *Теми за замовчуванням* відновлює їх. |
| **Зібрані MS-споти** | – | Таблиця прийнятих спотів, найновіші першими. |

Кожен потік має хост, порт, команди, що надсилаються після входу, *Перепідключити*, *Підключатися під час запуску*, консоль і рядок для надсилання команд. Вгорі введіть свій **позивний для входу**. Джерело MQTT має хост, порт, теми (по одній у рядку або через `;`), *Перепідключити* і *Підключатися під час запуску* (типово вимкнено) та консоль з отриманими спотами; його споти проходять через той самий фільтр. Смужка показує стан чотирьох джерел (зелена точка = підключено). Сесії лишаються відкритими, коли ви змінюєте мову або колірну схему.

## Фільтр (40 % вікна)

- **Необов'язковий локальний фільтр:** рядки кластера нижче **27990,0 kHz** відкидаються одразу (не показуються, не зберігаються).
- CW-споти одразу відкидаються (CW або WPM у коментарі, або 28000-28070 кГц): вони не з'являються в консолі й не зберігаються, якщо не позначені <MS>. Прапорець можна вимкнути.
- **1-й критерій – типові частоти MS:** 50190–50300, 70100–70400, 144290–144399 kHz. Спот у цих вікнах приймається навіть без назви режиму, якщо тільки коментар не вказує на інше поширення: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Вікна і теги можна редагувати.
- **2-й критерій – режими MS:** поза вікнами або з одним із цих тегів спот зберігається, лише якщо містить **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (цифрові режими, що використовуються тільки для MS) або **\<MS\>**, великими, малими чи змішаними літерами. Слова можна вимикати, додавати й видаляти; кожне має свій лічильник.
- **Діапазони** 28, 50, 70, 144, 222, 432 MHz; **перевірка фільтра** на вставленому рядку; **лічильники**.

## Локатори та зберігання

Відсутні локатори або локатори лише з 4 символів беруться з бази **CALL3** (`data/call3.txt`, файл JTDX, понад мільйон позивних), яка завжди має перевагу над 4-символьним локатором. Прийняті споти зберігаються в `data/spot_ms`, один файл CSV на добу, і живлять мапу [Трафік наживо](Live-Traffic-uk).
