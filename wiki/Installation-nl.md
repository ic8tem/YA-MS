[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · **Nederlands** · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh)

# Installatie

Alle pakketten staan op de pagina **[Releases](https://github.com/ic8tem/YA-MS/releases)** (in de bestandsnamen hieronder is `x.y.z` de versie, bijv. `1.2.0`). Er hoeft niets gecompileerd en niets anders geïnstalleerd te worden: elk pakket bevat de .NET 8-runtime.

| Systeem | Bestand | Installeert in |
|---|---|---|
| Windows (64-bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (installatieprogramma) | `C:\YA-MS` |
| Windows (64-bit), portable | `YA-MS-x.y.z-windows-x64-portatile.zip` | elke map waarin je kunt schrijven |
| Windows (32-bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` of `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-bit): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (daarheen gekopieerd bij de eerste start) |
| Linux (64-bit), elke distributie | `YA-MS-x.y.z-linux-x64.tar.gz` (portable of met `./installa.sh`) | `~/YA-MS` of elke map |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian-pakket | `ya-ms_x.y.z_arm64.deb` (64-bit) of `ya-ms_x.y.z_armhf.deb` (32-bit) | `~/YA-MS` (daarheen gekopieerd bij de eerste start) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, alleen de applicatie | `YA-MS-x.y.z-mac-apple-silicon-app.zip` of `...-mac-intel-app.zip` | de map waarin je `YA-MS.app` uitpakt |

**Het programma en zijn map `data` blijven altijd samen** in de map YA-MS: daar staan alle gegevens en instellingen (geen AppData, geen systeemmappen). Zie [Instellingen en gegevensmap](Settings-and-Data-Folder-nl).

## Windows

### Installatieprogramma
1. Download `YA-MS-x.y.z-windows-x64-setup.exe` en voer het uit.
2. Als **SmartScreen** "Windows heeft uw pc beschermd" toont: *Meer informatie* → *Toch uitvoeren* (het programma is niet ondertekend met een commercieel certificaat).
3. YA-MS wordt geïnstalleerd in **`C:\YA-MS`**, **zonder beheerdersrechten**, met een pictogram in het menu Start en, als je dat aanvinkt, een pictogram op het bureaublad.

### Portable
Pak `YA-MS-x.y.z-windows-x64-portatile.zip` uit waar je wilt (in een map waarin je kunt schrijven, niet in *Program Files*) en start `YA-MS.exe`. Je kunt de hele map naar een USB-stick of een andere computer kopiëren.

## Linux

1. Pak `YA-MS-x.y.z-linux-x64.tar.gz` uit.
2. Voer in de uitgepakte map uit:
   ```sh
   ./installa.sh
   ```
3. Het script kopieert YA-MS naar **`~/YA-MS`** (geen root nodig) en voegt **YA-MS** toe aan het toepassingenmenu (categorie *HamRadio*). Je kunt het ook starten met `~/YA-MS/YA-MS`.

### Debian-pakket (.deb)
Op Debian, Ubuntu, Mint en Raspberry Pi OS kun je in plaats daarvan `ya-ms_x.y.z_amd64.deb` installeren (`_arm64.deb` / `_armhf.deb` op de Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Het pakket zet het programma in `/opt/ya-ms` en voegt **YA-MS** toe aan het menu. Bij de eerste start (en na elke nieuwe versie) kopieert het zichzelf naar **`~/YA-MS`** en draait het van daaruit, zodat de map `data` naast het programma blijft en je instellingen behouden blijven.

### Portable
De `.tar.gz` werkt ook zonder installatie: pak hem uit op een plek waar je kunt schrijven en start `./YA-MS` vanuit die map.

Voor Japanse tekst heb je mogelijk de Noto CJK-lettertypen nodig: zie [Problemen en FAQ](Troubleshooting-FAQ-nl#linux-japanse-tekst-verschijnt-als-vierkantjes).

## Raspberry Pi

Dezelfde procedure als bij Linux: pak `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` uit (of `-32bit` op Raspberry Pi OS 32-bit) en voer `./installa.sh` uit in de uitgepakte map.

- Om te zien welk systeem je hebt, typ je `uname -m` in een terminal: `aarch64` → 64-bit pakket, `armv7l` → 32-bit pakket.
- Ondersteund: Raspberry Pi 2 (alleen 32-bit), 3, 4, 5, 400 en 500, met de desktopversie van Raspberry Pi OS. **Niet ondersteund:** Pi Zero / Zero W en Pi 1 (ARMv6-processor, .NET draait daar niet); de Pi Zero 2 W werkt met het 64-bit pakket, maar 512 MB RAM is krap.
- Een Pi 4 of 5 met minstens 2 GB RAM wordt aanbevolen; de eerste start duurt een paar seconden langer dan op een pc.

## macOS

1. Kies het juiste bestand: `-mac-apple-silicon.dmg` voor M1/M2/M3/M4-processors, `-mac-intel.dmg` voor Intel-Macs.
2. Open de `.dmg`, **klik met de rechtermuisknop op "Installa YA-MS.command" → Open** en bevestig.
3. Het script kopieert `YA-MS.app` naar **`~/YA-MS`** en opent het.

Je kunt ook `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` gebruiken, dat alleen `YA-MS.app` bevat: pak het uit in een map naar keuze (waarin je kunt schrijven); de map `data` wordt naast `YA-MS.app` aangemaakt. De eerste keer: rechtsklik → **Open**.

Het programma is niet door Apple ondertekend, dus de eerste keer vraagt macOS om bevestiging; zie [Problemen en FAQ](Troubleshooting-FAQ-nl#macos-kan-niet-worden-geopend-omdat-het-van-een-onbekende-ontwikkelaar-is).

## Eerste start

- De **kaart van Europa** (kustlijnen en grenzen van Natural Earth) wordt de eerste keer automatisch gedownload naar `data/mappa`: eenmalig is een internetverbinding nodig.
- De **radargegevens** (Collm, Sodankylä) worden meteen gedownload en daarna elke 5 minuten gecontroleerd.
- De interface start in de taal van je systeem als dat een van de zes beschikbare is, anders in het Italiaans; je wijzigt dat rechtsboven (zie [Instellingen](Settings-and-Data-Folder-nl#taal)).

## Bijwerken

Installeer de nieuwe versie **over de oude heen** (hetzelfde installatieprogramma, dezelfde map). De instellingen (`config.ini`), de fluxarchieven en de kaart blijven in `data`. De vertaalbestanden in `data/lingue` worden vervangen als de nieuwe recenter zijn.

## Compileren vanuit de broncode (alleen voor ontwikkelaars)

De installatiepakketten worden gemaakt door GitHub Actions (`.github/workflows/build.yml`) bij elke update van de branch `release` (versie uit het bestand `VERSION`), die ook de release `vX.Y.Z` aanmaakt. Lokaal:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # of linux-x64, linux-arm64, linux-arm, osx-arm64
```

De documenten worden opnieuw gegenereerd met `tools/build_spiegazione.py data` en `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Volgende: [Aan de slag](Getting-Started-nl).
