[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · **Русский** · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Установка

Все пакеты находятся на странице **[Releases](https://github.com/ic8tem/YA-MS/releases)** (в именах файлов ниже `x.y.z` – номер версии, например `1.2.0`). Ничего не нужно компилировать и ничего не нужно доустанавливать: каждый пакет содержит среду выполнения .NET 8.

| Система | Файл | Куда устанавливается |
|---|---|---|
| Windows (64 бита) | `YA-MS-x.y.z-windows-x64-setup.exe` (установщик) | `C:\YA-MS` |
| Windows (64 бита), портативная | `YA-MS-x.y.z-windows-x64-portatile.zip` | любая папка, в которую разрешена запись |
| Windows (32 бита, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` или `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Windows на ARM (64 бит, ПК со Snapdragon) | `YA-MS-x.y.z-windows-arm64-setup.exe` или `...-windows-arm64-portatile.zip` | `C:\YA-MS` |
| Linux (64 бита): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (копируется туда при первом запуске) |
| Linux (64 бита), любой дистрибутив | `YA-MS-x.y.z-linux-x64.tar.gz` (портативно или через `./installa.sh`) | `~/YA-MS` или любая папка |
| Linux (64 бит): Fedora, openSUSE | `ya-ms-x.y.z.x86_64.rpm` (x86_64), `ya-ms-x.y.z.aarch64.rpm` (ARM64), `ya-ms-x.y.z.armv7hl.rpm` (ARM 32) | `~/YA-MS` (копируется туда при первом запуске) |
| Arch, Manjaro, EndeavourOS, Arch Linux ARM | `ya-ms-x.y.z-1-x86_64.pkg.tar.zst`, `ya-ms-x.y.z-1-aarch64.pkg.tar.zst` | `~/YA-MS` (копируется туда при первом запуске) |
| Slackware64, Slackware ARM64 | `ya-ms-x.y.z-x86_64-1_ic8tem.txz`, `ya-ms-x.y.z-aarch64-1_ic8tem.txz` | `~/YA-MS` (копируется туда при первом запуске) |
| AppImage (x86_64, aarch64) | `YA-MS-x.y.z-x86_64.AppImage`, `YA-MS-x.y.z-aarch64.AppImage` | `~/YA-MS` (копируется туда при первом запуске) |
| Alpine Linux (musl) | `YA-MS-x.y.z-alpine-x64.tar.gz`, `YA-MS-x.y.z-alpine-arm64.tar.gz` | `~/YA-MS` или любая папка |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 бита) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 бита) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, пакет Debian | `ya-ms_x.y.z_arm64.deb` (64 бита) или `ya-ms_x.y.z_armhf.deb` (32 бита) | `~/YA-MS` (копируется туда при первом запуске) |
| Linux ARM 64 бит, любой дистрибутив (например, Slackware ARM64) | `YA-MS-x.y.z-linux-arm64.tar.gz` (портативно или через `./installa.sh`) | `~/YA-MS` или любая папка |
| Linux armv7l (ARM 32 бит), любой дистрибутив | `YA-MS-x.y.z-linux-armv7l.tar.gz` (портативно или через `./installa.sh`) | `~/YA-MS` или любая папка |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, только приложение | `YA-MS-x.y.z-mac-apple-silicon-app.zip` или `...-mac-intel-app.zip` | папка, в которую вы распаковали `YA-MS.app` |

**Программа и её папка `data` всегда находятся вместе** в папке YA-MS: там все данные и настройки (никакого AppData и системных папок). См. [Настройки и папка данных](Settings-and-Data-Folder-ru).

## Windows

### Установщик
1. Скачайте `YA-MS-x.y.z-windows-x64-setup.exe` и запустите его.
2. Если **SmartScreen** выводит «Система Windows защитила ваш компьютер»: *Подробнее* → *Выполнить в любом случае* (программа не подписана коммерческим сертификатом).
3. YA-MS устанавливается в **`C:\YA-MS`**, **без прав администратора**, со значком в меню «Пуск» и, если отметить, на рабочем столе.

### Портативная версия
Распакуйте `YA-MS-x.y.z-windows-x64-portatile.zip` куда угодно (в папку, в которую разрешена запись, не в *Program Files*) и запустите `YA-MS.exe`. Всю папку можно скопировать на USB-накопитель или на другой компьютер.

## Linux

1. Распакуйте `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Из распакованной папки выполните:
   ```sh
   ./installa.sh
   ```
3. Скрипт копирует YA-MS в **`~/YA-MS`** (права root не нужны) и добавляет **YA-MS** в меню приложений (категория *HamRadio*). Запускать можно также командой `~/YA-MS/YA-MS`.

### Пакет Debian (.deb)
В Debian, Ubuntu, Mint и Raspberry Pi OS можно вместо этого установить `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` на Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Пакет помещает программу в `/opt/ya-ms` и добавляет **YA-MS** в меню. При первом запуске (и после каждой новой версии) программа копирует себя в **`~/YA-MS`** и запускается оттуда, поэтому папка `data` остаётся рядом с программой, а ваши настройки сохраняются.

### Портативная версия
Архив `.tar.gz` работает и без установки: распакуйте его в любую папку, в которую разрешена запись, и запустите `./YA-MS` из этой папки.

Для японского текста могут понадобиться шрифты Noto CJK: см. [Неполадки](Troubleshooting-FAQ-ru#linux-японский-текст-отображается-квадратиками).

## Raspberry Pi

Так же, как в Linux: распакуйте `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (или `-32bit` для 32-битной Raspberry Pi OS) и запустите `./installa.sh` из распакованной папки.

- Чтобы узнать разрядность системы, введите в терминале `uname -m`: `aarch64` → 64-битный пакет, `armv7l` → 32-битный.
- Поддерживаются Raspberry Pi 2 (только 32 бита), 3, 4, 5, 400 и 500 с настольной версией Raspberry Pi OS. **Не поддерживаются:** Pi Zero / Zero W и Pi 1 (процессор ARMv6, .NET на нём не работает); Pi Zero 2 W работает с 64-битным пакетом, но 512 МБ памяти мало.
- Рекомендуется Pi 4 или 5 с памятью от 2 ГБ; первый запуск занимает на несколько секунд больше, чем на ПК.

## macOS

1. Выберите нужный файл: `-mac-apple-silicon.dmg` для процессоров M1/M2/M3/M4, `-mac-intel.dmg` для Mac с Intel.
2. Откройте `.dmg`, **правый щелчок по «Installa YA-MS.command» → Открыть** и подтвердите.
3. Скрипт копирует `YA-MS.app` в **`~/YA-MS`** и запускает его.

Кроме того, `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` содержит только `YA-MS.app`: распакуйте его в папку по вашему выбору (в которую разрешена запись); папка `data` создаётся рядом с `YA-MS.app`. При первом запуске – правый щелчок → **Открыть**.

Программа не подписана Apple, поэтому при первом запуске macOS запрашивает подтверждение; см. [Неполадки](Troubleshooting-FAQ-ru#macos-не-удаётся-открыть-так-как-разработчик-не-установлен).

## Первый запуск

- **Карта Европы** (береговые линии и границы Natural Earth) при первом запуске загружается автоматически в `data/mappa`: подключение к интернету нужно один раз.
- **Данные радаров** (Collm, Sodankylä) загружаются сразу, а затем проверяются каждые 5 минут.
- Интерфейс запускается на языке системы, если это один из 36 доступных, иначе на итальянском; язык меняется справа вверху (см. [Настройки](Settings-and-Data-Folder-ru#язык)).

## Обновление

Установите новую версию **поверх старой** (тот же установщик, та же папка). Настройки (`config.ini`), архивы потока и карта остаются в `data`. Файлы переводов в `data/lingue` заменяются, если новые более свежие.

**Начиная с 1.8.0 YA-MS обновляется сама.** При запуске, раз в день, она проверяет на GitHub, есть ли новая версия, и предлагает её; кнопка **Обновления** в нижней строке проверяет вручную. *Обновить сейчас* скачивает переносной пакет для вашей системы, заменяет файлы программы, сохраняет папку `data` (изменившиеся файлы программы сначала копируются в `data/backup/v<старая версия>`) и перезапускается; в папку программы должна быть возможна запись. Если при запуске отсутствуют файлы программы (в `data` или `doc`), окно перечисляет их и предлагает скачать их заново с GitHub. Чтобы не искать новые версии, укажите `controlla_aggiornamenti=0` в `config.ini`.

## Сборка из исходного кода (только для разработчиков)

Установщики собираются GitHub Actions (`.github/workflows/build.yml`) при каждом обновлении ветки `release` (версия берётся из файла `VERSION`), при этом создаётся и релиз `vX.Y.Z`. Локально:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

Документы (на всех языках) пересоздаются командой `tools/build_documenti.sh`.

Далее: [Начало работы](Getting-Started-ru).
