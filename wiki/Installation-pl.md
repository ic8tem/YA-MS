[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · **Polski** · [Čeština](Installation-cs) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh)

# Instalacja

Wszystkie pakiety są na stronie **[Releases](https://github.com/ic8tem/YA-MS/releases)** (w nazwach plików poniżej `x.y.z` oznacza wersję, np. `1.2.0`). Niczego nie trzeba kompilować ani doinstalowywać: każdy pakiet zawiera środowisko uruchomieniowe .NET 8.

| System | Plik | Instaluje się do |
|---|---|---|
| Windows (64-bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (instalator) | `C:\YA-MS` |
| Windows (64-bit), wersja przenośna | `YA-MS-x.y.z-windows-x64-portatile.zip` | dowolny folder z prawem zapisu |
| Windows (32-bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` lub `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-bit) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**Program i jego folder `data` zawsze pozostają razem** w folderze YA-MS: są tam wszystkie dane i ustawienia (żadnego AppData, żadnych folderów systemowych). Zob. [Ustawienia i folder danych](Settings-and-Data-Folder-pl).

## Windows

### Instalator
1. Pobierz `YA-MS-x.y.z-windows-x64-setup.exe` i uruchom go.
2. Jeśli **SmartScreen** wyświetli „System Windows ochronił ten komputer”: *Więcej informacji* → *Uruchom mimo to* (program nie jest podpisany komercyjnym certyfikatem).
3. YA-MS instaluje się do **`C:\YA-MS`**, **bez uprawnień administratora**, z ikoną w menu Start oraz, jeśli to zaznaczysz, ikoną na pulpicie.

### Wersja przenośna
Rozpakuj `YA-MS-x.y.z-windows-x64-portatile.zip` w dowolnym miejscu (w folderze z prawem zapisu, nie w *Program Files*) i uruchom `YA-MS.exe`. Cały folder możesz skopiować na pendrive lub na inny komputer.

## Linux

1. Rozpakuj `YA-MS-x.y.z-linux-x64.tar.gz`.
2. W rozpakowanym folderze uruchom:
   ```sh
   ./installa.sh
   ```
3. Skrypt kopiuje YA-MS do **`~/YA-MS`** (bez potrzeby uprawnień roota) i dodaje **YA-MS** do menu aplikacji (kategoria *HamRadio*). Program można też uruchomić poleceniem `~/YA-MS/YA-MS`.

Do wyświetlania tekstu japońskiego mogą być potrzebne czcionki Noto CJK: zob. [Rozwiązywanie problemów](Troubleshooting-FAQ-pl#linux-tekst-japoński-wyświetla-się-jako-kwadraciki).

## Raspberry Pi

Ta sama procedura co w Linuksie: rozpakuj `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (lub `-32bit` w 32-bitowym Raspberry Pi OS) i uruchom `./installa.sh` z rozpakowanego folderu.

- Aby sprawdzić, jaki masz system, wpisz w terminalu `uname -m`: `aarch64` → pakiet 64-bitowy, `armv7l` → pakiet 32-bitowy.
- Obsługiwane: Raspberry Pi 2 (tylko 32-bit), 3, 4, 5, 400 i 500, z wersją desktopową Raspberry Pi OS. **Nieobsługiwane:** Pi Zero / Zero W i Pi 1 (procesor ARMv6, .NET na nim nie działa); Pi Zero 2 W działa z pakietem 64-bitowym, ale 512 MB RAM to niewiele.
- Zalecany jest Pi 4 lub 5 z co najmniej 2 GB RAM; pierwsze uruchomienie trwa kilka sekund dłużej niż na PC.

## macOS

1. Wybierz właściwy plik: `-mac-apple-silicon.dmg` dla procesorów M1/M2/M3/M4, `-mac-intel.dmg` dla Maców z procesorem Intel.
2. Otwórz plik `.dmg`, **kliknij prawym przyciskiem „Installa YA-MS.command” → Otwórz** i potwierdź.
3. Skrypt kopiuje `YA-MS.app` do **`~/YA-MS`** i go otwiera.

Program nie jest podpisany przez Apple, więc za pierwszym razem macOS prosi o potwierdzenie; zob. [Rozwiązywanie problemów](Troubleshooting-FAQ-pl#macos-nie-można-otworzyć-bo-pochodzi-od-niezidentyfikowanego-dewelopera).

## Pierwsze uruchomienie

- **Mapa Europy** (linie brzegowe i granice z Natural Earth) jest pobierana automatycznie do `data/mappa` za pierwszym razem: połączenie z internetem jest potrzebne jednorazowo.
- **Dane radarowe** (Collm, Sodankylä) są pobierane od razu, a potem sprawdzane co 5 minut.
- Interfejs uruchamia się w języku systemu, jeśli jest on jednym z 36 dostępnych, w przeciwnym razie po włosku; zmienisz go w prawym górnym rogu (zob. [Ustawienia](Settings-and-Data-Folder-pl#język)).

## Aktualizacja

Zainstaluj nową wersję **na starej** (ten sam instalator, ten sam folder). Ustawienia (`config.ini`), archiwa strumienia i mapa pozostają w `data`. Pliki tłumaczeń w `data/lingue` są zastępowane, gdy nowe są nowsze.

## Kompilacja ze źródeł (tylko dla programistów)

Instalatory są tworzone przez GitHub Actions (`.github/workflows/build.yml`) przy każdej aktualizacji gałęzi `release` (wersja pobierana z pliku `VERSION`), co tworzy również wydanie `vX.Y.Z`. Lokalnie:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # lub linux-x64, linux-arm64, linux-arm, osx-arm64
```

Dokumenty generuje się ponownie poleceniami `tools/build_spiegazione.py data` i `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Dalej: [Pierwsze kroki](Getting-Started-pl).
