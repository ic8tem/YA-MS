[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · **Polski** · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Instalacja

Wszystkie pakiety znajdują się na stronie **[Releases](https://github.com/ic8tem/YA-MS/releases)** (w poniższych nazwach plików `x.y.z` to wersja, np. `1.2.0`). Niczego nie trzeba kompilować ani doinstalowywać: każdy pakiet zawiera środowisko uruchomieniowe .NET 8.

| System | Plik | Instaluje się do |
|---|---|---|
| Windows (64-bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (instalator) | `C:\YA-MS` |
| Windows (64-bit), wersja przenośna | `YA-MS-x.y.z-windows-x64-portatile.zip` | dowolnego folderu z prawem zapisu |
| Windows (32-bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` lub `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Windows na ARM (64-bit, komputery ze Snapdragonem) | `YA-MS-x.y.z-windows-arm64-setup.exe` lub `...-windows-arm64-portatile.zip` | `C:\YA-MS` |
| Linux (64-bit): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (kopiowany tam przy pierwszym uruchomieniu) |
| Linux (64-bit), dowolna dystrybucja | `YA-MS-x.y.z-linux-x64.tar.gz` (przenośnie lub przez `./installa.sh`) | `~/YA-MS` lub dowolnego folderu |
| Linux (64-bit): Fedora, openSUSE | `ya-ms-x.y.z.x86_64.rpm` (x86_64), `ya-ms-x.y.z.aarch64.rpm` (ARM64) | `~/YA-MS` (kopiowany tam przy pierwszym uruchomieniu) |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, pakiet Debiana | `ya-ms_x.y.z_arm64.deb` (64-bit) lub `ya-ms_x.y.z_armhf.deb` (32-bit) | `~/YA-MS` (kopiowany tam przy pierwszym uruchomieniu) |
| Linux ARM 64-bit, dowolna dystrybucja (np. Slackware ARM64) | `YA-MS-x.y.z-linux-arm64.tar.gz` (przenośnie lub przez `./installa.sh`) | `~/YA-MS` lub dowolnego folderu |
| Linux armv7l (ARM 32-bit), dowolna dystrybucja | `YA-MS-x.y.z-linux-armv7l.tar.gz` (przenośnie lub przez `./installa.sh`) | `~/YA-MS` lub dowolnego folderu |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, tylko aplikacja | `YA-MS-x.y.z-mac-apple-silicon-app.zip` lub `...-mac-intel-app.zip` | folderu, do którego rozpakujesz `YA-MS.app` |

32-bitowy Linux na PC (i686), FreeBSD i OpenBSD nie mają pakietu: .NET 8, na którym opiera się YA-MS, nie działa w tych systemach.

**Program i jego folder `data` zawsze pozostają razem** w folderze YA-MS: tam są wszystkie dane i ustawienia (bez AppData, bez folderów systemowych). Zob. [Ustawienia i folder danych](Settings-and-Data-Folder-pl).

## Windows

### Instalator
1. Pobierz `YA-MS-x.y.z-windows-x64-setup.exe` i uruchom go.
2. Jeśli **SmartScreen** wyświetli komunikat „System Windows ochronił ten komputer”: *Więcej informacji* → *Uruchom mimo to* (program nie jest podpisany komercyjnym certyfikatem).
3. YA-MS instaluje się do **`C:\YA-MS`**, **bez uprawnień administratora**, z ikoną w menu Start oraz, jeśli to zaznaczysz, z ikoną na pulpicie.

### Wersja przenośna
Rozpakuj `YA-MS-x.y.z-windows-x64-portatile.zip` w dowolnym miejscu (w folderze z prawem zapisu, nie w *Program Files*) i uruchom `YA-MS.exe`. Cały folder możesz skopiować na pendrive lub na inny komputer.

## Linux

1. Rozpakuj `YA-MS-x.y.z-linux-x64.tar.gz`.
2. W rozpakowanym folderze uruchom:
   ```sh
   ./installa.sh
   ```
3. Skrypt kopiuje YA-MS do **`~/YA-MS`** (bez uprawnień roota) i dodaje **YA-MS** do menu aplikacji (kategoria *HamRadio*). Możesz go też uruchomić poleceniem `~/YA-MS/YA-MS`.

### Pakiet Debiana (.deb)
W systemach Debian, Ubuntu, Mint i Raspberry Pi OS możesz zamiast tego zainstalować `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` na Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Pakiet umieszcza program w `/opt/ya-ms` i dodaje **YA-MS** do menu. Przy pierwszym uruchomieniu (i po każdej nowej wersji) kopiuje się do **`~/YA-MS`** i stamtąd działa, dzięki czemu folder `data` pozostaje obok programu, a twoje ustawienia są zachowane.

### Wersja przenośna
Plik `.tar.gz` działa też bez instalacji: rozpakuj go w dowolnym miejscu z prawem zapisu i uruchom `./YA-MS` z tego folderu.

Do wyświetlania tekstu japońskiego mogą być potrzebne czcionki Noto CJK: zob. [Rozwiązywanie problemów](Troubleshooting-FAQ-pl#linux-tekst-japoński-wyświetla-się-jako-prostokąty).

## Raspberry Pi

Ta sama procedura co w Linuksie: rozpakuj `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (lub `-32bit` w 32-bitowym Raspberry Pi OS) i uruchom `./installa.sh` z rozpakowanego folderu.

- Aby sprawdzić, jaki masz system, wpisz w terminalu `uname -m`: `aarch64` → pakiet 64-bitowy, `armv7l` → pakiet 32-bitowy.
- Obsługiwane: Raspberry Pi 2 (tylko 32-bit), 3, 4, 5, 400 i 500, z wersją desktopową Raspberry Pi OS. **Nieobsługiwane:** Pi Zero / Zero W i Pi 1 (procesor ARMv6, .NET na nim nie działa); Pi Zero 2 W działa z pakietem 64-bitowym, ale 512 MB RAM to niewiele.
- Zalecany jest Pi 4 lub 5 z co najmniej 2 GB RAM; pierwsze uruchomienie trwa kilka sekund dłużej niż na PC.

## macOS

1. Wybierz właściwy plik: `-mac-apple-silicon.dmg` dla procesorów M1/M2/M3/M4, `-mac-intel.dmg` dla Maców z procesorem Intel.
2. Otwórz plik `.dmg`, **kliknij prawym przyciskiem „Installa YA-MS.command” → Otwórz** i potwierdź.
3. Skrypt kopiuje `YA-MS.app` do **`~/YA-MS`** i go otwiera.

Alternatywnie `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` zawiera tylko `YA-MS.app`: rozpakuj go do wybranego folderu (z prawem zapisu); folder `data` zostanie utworzony obok `YA-MS.app`. Za pierwszym razem: prawy przycisk → **Otwórz**.

Program nie jest podpisany przez Apple, więc za pierwszym razem macOS prosi o potwierdzenie; zob. [Rozwiązywanie problemów](Troubleshooting-FAQ-pl#macos-nie-można-otworzyć-bo-pochodzi-od-niezidentyfikowanego-dewelopera).

## Pierwsze uruchomienie

- **Mapa Europy** (linie brzegowe i granice Natural Earth) jest za pierwszym razem pobierana automatycznie do `data/mappa`: połączenie z internetem jest potrzebne jednorazowo.
- **Dane radarowe** (Collm, Sodankylä) są pobierane od razu, a następnie sprawdzane co 5 minut.
- Interfejs uruchamia się w języku systemu, jeśli jest on jednym z 36 dostępnych, w przeciwnym razie po włosku; zmienisz go w prawym górnym rogu (zob. [Ustawienia](Settings-and-Data-Folder-pl#język)).

## Aktualizacja

Zainstaluj nową wersję **na starszą** (ten sam instalator, ten sam folder). Ustawienia (`config.ini`), archiwa strumienia i mapa pozostają w `data`. Pliki tłumaczeń w `data/lingue` są zastępowane, gdy nowe są nowsze.

**Od wersji 1.8.0 YA-MS aktualizuje się sam.** Przy uruchomieniu, raz dziennie, sprawdza na GitHubie, czy jest nowa wersja, i ją proponuje; przycisk **Aktualizacje** na dolnym pasku sprawdza ręcznie. *Aktualizuj teraz* pobiera pakiet przenośny dla twojego systemu, zastępuje pliki programu, zachowuje folder `data` (zmieniające się pliki programu są najpierw kopiowane do `data/backup/v<stara wersja>`) i uruchamia się ponownie; folder programu musi być zapisywalny. Jeśli przy uruchomieniu brakuje plików programu (w `data` lub `doc`), okno je wymienia i proponuje ponowne pobranie z GitHuba. Aby nie szukać nowych wersji, ustaw `controlla_aggiornamenti=0` w `config.ini`.

## Kompilacja ze źródeł (tylko dla programistów)

Instalatory są tworzone przez GitHub Actions (`.github/workflows/build.yml`) przy każdej aktualizacji gałęzi `release` (wersja pobierana z pliku `VERSION`), co tworzy również wydanie `vX.Y.Z`. Lokalnie:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

Dokumenty (we wszystkich językach) są generowane ponownie poleceniem `tools/build_documenti.sh`.

Dalej: [Pierwsze kroki](Getting-Started-pl).
