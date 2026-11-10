[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-BR) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · **Українська** · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-TW)

# Встановлення

Усі пакети розміщено на сторінці **[Releases](https://github.com/ic8tem/YA-MS/releases)** (у назвах файлів нижче `x.y.z` — це версія, напр. `1.2.0`). Нічого не потрібно компілювати й нічого більше встановлювати: кожен пакет містить середовище виконання .NET 8.

| Система | Файл | Куди встановлюється |
|---|---|---|
| Windows (64 біт) | `YA-MS-x.y.z-windows-x64-setup.exe` (інсталятор) | `C:\YA-MS` |
| Windows (64 біт), портативна | `YA-MS-x.y.z-windows-x64-portatile.zip` | будь-яка тека, у яку ви можете записувати |
| Windows (32 біт, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` або `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 біт): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (копіюється туди під час першого запуску) |
| Linux (64 біт), будь-який дистрибутив | `YA-MS-x.y.z-linux-x64.tar.gz` (портативно або через `./installa.sh`) | `~/YA-MS` або будь-яка тека |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 біт) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 біт) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, пакет Debian | `ya-ms_x.y.z_arm64.deb` (64 біт) або `ya-ms_x.y.z_armhf.deb` (32 біт) | `~/YA-MS` (копіюється туди під час першого запуску) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, лише застосунок | `YA-MS-x.y.z-mac-apple-silicon-app.zip` або `...-mac-intel-app.zip` | тека, у яку ви розпакували `YA-MS.app` |

**Програма і її тека `data` завжди лишаються разом** у теці YA-MS: там усі дані й налаштування (без AppData і системних тек). Див. [Налаштування і тека даних](Settings-and-Data-Folder-uk).

## Windows

### Інсталятор
1. Завантажте `YA-MS-x.y.z-windows-x64-setup.exe` і запустіть його.
2. Якщо **SmartScreen** показує «Windows захистила ваш ПК»: *Докладніше* → *Усе одно запустити* (програму не підписано комерційним сертифікатом).
3. YA-MS встановлюється в **`C:\YA-MS`** **без прав адміністратора**, з ярликом у меню «Пуск» і, якщо поставити позначку, на робочому столі.

### Портативна версія
Розпакуйте `YA-MS-x.y.z-windows-x64-portatile.zip` куди завгодно (у теку, де ви можете записувати, не в *Program Files*) і запустіть `YA-MS.exe`. Усю теку можна скопіювати на USB-флешку або інший комп'ютер.

## Linux

1. Розпакуйте `YA-MS-x.y.z-linux-x64.tar.gz`.
2. З розпакованої теки виконайте:
   ```sh
   ./installa.sh
   ```
3. Скрипт копіює YA-MS у **`~/YA-MS`** (права root не потрібні) і додає **YA-MS** до меню застосунків (категорія *HamRadio*). Запустити програму можна також командою `~/YA-MS/YA-MS`.

### Пакет Debian (.deb)
У Debian, Ubuntu, Mint і Raspberry Pi OS можна натомість встановити `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` на Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Пакет розміщує програму в `/opt/ya-ms` і додає **YA-MS** до меню. Під час першого запуску (і після кожної нової версії) програма копіює себе в **`~/YA-MS`** і запускається звідти, тож тека `data` лишається поруч із програмою, а ваші налаштування зберігаються.

### Портативна версія
Архів `.tar.gz` працює й без встановлення: розпакуйте його в будь-яку теку, де ви можете записувати, і запустіть `./YA-MS` з цієї теки.

Для японського тексту можуть знадобитися шрифти Noto CJK: див. [Усунення несправностей](Troubleshooting-FAQ-uk#linux-японський-текст-відображається-квадратиками).

## Raspberry Pi

Та сама процедура, що й для Linux: розпакуйте `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (або `-32bit` для 32-бітної Raspberry Pi OS) і запустіть `./installa.sh` з розпакованої теки.

- Щоб дізнатися, яка у вас система, введіть у терміналі `uname -m`: `aarch64` → 64-бітний пакет, `armv7l` → 32-бітний пакет.
- Підтримуються: Raspberry Pi 2 (лише 32 біт), 3, 4, 5, 400 і 500 з настільною версією Raspberry Pi OS. **Не підтримуються:** Pi Zero / Zero W і Pi 1 (процесор ARMv6, .NET на ньому не працює); Pi Zero 2 W працює з 64-бітним пакетом, але 512 MB RAM — це впритул.
- Рекомендовано Pi 4 або 5 щонайменше з 2 GB RAM; перший запуск триває на кілька секунд довше, ніж на ПК.

## macOS

1. Виберіть правильний файл: `-mac-apple-silicon.dmg` для процесорів M1/M2/M3/M4, `-mac-intel.dmg` для Mac з Intel.
2. Відкрийте `.dmg`, **клацніть правою кнопкою «Installa YA-MS.command» → Open** і підтвердьте.
3. Скрипт копіює `YA-MS.app` у **`~/YA-MS`** і відкриває його.

Інший варіант: `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` містить лише `YA-MS.app`: розпакуйте його в теку на ваш вибір (де ви можете записувати); тека `data` створюється поруч із `YA-MS.app`. Першого разу — клацніть правою кнопкою → **Open**.

Програму не підписано Apple, тому першого разу macOS просить підтвердження; див. [Усунення несправностей](Troubleshooting-FAQ-uk#macos-неможливо-відкрити-бо-розробника-не-ідентифіковано).

## Перший запуск

- **Мапа Європи** (берегові лінії та кордони Natural Earth) першого разу завантажується автоматично в `data/mappa`: інтернет-з'єднання потрібне один раз.
- **Дані радарів** (Collm, Соданкюля) завантажуються одразу, а потім перевіряються кожні 5 хвилин.
- Інтерфейс запускається мовою вашої системи, якщо вона є серед 36 доступних, інакше — італійською; змінити мову можна вгорі праворуч (див. [Налаштування](Settings-and-Data-Folder-uk#мова)).

## Оновлення

Встановіть нову версію **поверх старої** (той самий інсталятор, та сама тека). Налаштування (`config.ini`), архіви потоку і мапа лишаються в `data`. Файли перекладів у `data/lingue` замінюються, якщо нові свіжіші.

## Збирання з вихідного коду (лише для розробників)

Інсталятори створює GitHub Actions (`.github/workflows/build.yml`) під час кожного оновлення гілки `release` (версія береться з файлу `VERSION`); він також створює реліз `vX.Y.Z`. Локально:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # або linux-x64, linux-arm64, linux-arm, osx-arm64
```

Документи (усіма мовами) генеруються заново командою `tools/build_documenti.sh`.

Далі: [Початок роботи](Getting-Started-uk).
