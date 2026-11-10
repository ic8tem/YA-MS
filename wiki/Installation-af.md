[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · **Afrikaans** · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [ไทย](Installation-th) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Installering

Al die pakkette is op die **[Releases](https://github.com/ic8tem/YA-MS/releases)**-bladsy (in die lêername hieronder is `x.y.z` die weergawe, bv. `1.2.0`). Niks hoef gekompileer te word nie en niks anders hoef geïnstalleer te word nie: elke pakket bevat die .NET 8-looptyd.

| Stelsel | Lêer | Installeer in |
|---|---|---|
| Windows (64-bis) | `YA-MS-x.y.z-windows-x64-setup.exe` (installeerder) | `C:\YA-MS` |
| Windows (64-bis), draagbaar | `YA-MS-x.y.z-windows-x64-portatile.zip` | enige gids waarin jy kan skryf |
| Windows (32-bis, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` of `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-bis) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-bis) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-bis) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**Die program en sy `data`-gids bly altyd saam** in die YA-MS-gids: alle data en instellings is daar (geen AppData, geen stelselgidse nie). Sien [Instellings en datagids](Settings-and-Data-Folder-af).

## Windows

### Installeerder
1. Laai `YA-MS-x.y.z-windows-x64-setup.exe` af en voer dit uit.
2. As **SmartScreen** "Windows protected your PC" wys: *More info* → *Run anyway* (die program is nie met 'n kommersiële sertifikaat onderteken nie).
3. YA-MS word in **`C:\YA-MS`** geïnstalleer, **sonder administrateursregte**, met 'n ikoon in die Start-kieslys en, as jy dit merk, 'n ikoon op die lessenaar.

### Draagbaar
Pak `YA-MS-x.y.z-windows-x64-portatile.zip` uit waar jy wil ('n gids waarin jy kan skryf, nie *Program Files* nie) en voer `YA-MS.exe` uit. Jy kan die hele gids na 'n USB-stokkie of 'n ander rekenaar kopieer.

## Linux

1. Pak `YA-MS-x.y.z-linux-x64.tar.gz` uit.
2. Voer vanuit die uitgepakte gids uit:
   ```sh
   ./installa.sh
   ```
3. Die skrip kopieer YA-MS na **`~/YA-MS`** (geen root nodig nie) en voeg **YA-MS** by die toepassingskieslys (kategorie *HamRadio*). Jy kan dit ook met `~/YA-MS/YA-MS` begin.

Vir Japannese teks het jy dalk die Noto CJK-lettertipes nodig: sien [Probleemoplossing](Troubleshooting-FAQ-af#linux-japannese-teks-verskyn-as-blokkies).

## Raspberry Pi

Dieselfde prosedure as Linux: pak `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` uit (of `-32bit` op Raspberry Pi OS 32-bis) en voer `./installa.sh` vanuit die uitgepakte gids uit.

- Om te sien watter stelsel jy het, tik `uname -m` in 'n terminaal: `aarch64` → 64-bis-pakket, `armv7l` → 32-bis-pakket.
- Ondersteun: Raspberry Pi 2 (slegs 32-bis), 3, 4, 5, 400 en 500, met die lessenaarweergawe van Raspberry Pi OS. **Nie ondersteun nie:** Pi Zero / Zero W en Pi 1 (ARMv6-verwerker, .NET loop nie daarop nie); Pi Zero 2 W werk met die 64-bis-pakket, maar 512 MB RAM is krap.
- 'n Pi 4 of 5 met minstens 2 GB RAM word aanbeveel; die eerste opstart neem 'n paar sekondes langer as op 'n rekenaar.

## macOS

1. Kies die regte lêer: `-mac-apple-silicon.dmg` vir M1/M2/M3/M4-verwerkers, `-mac-intel.dmg` vir Intel-Macs.
2. Open die `.dmg`, **regsklik op "Installa YA-MS.command" → Open** en bevestig.
3. Die skrip kopieer `YA-MS.app` na **`~/YA-MS`** en open dit.

Die program is nie deur Apple onderteken nie, so die eerste keer vra macOS vir bevestiging; sien [Probleemoplossing](Troubleshooting-FAQ-af#macos-kan-nie-oopgemaak-word-nie-omdat-dit-van-n-onbekende-ontwikkelaar-is).

## Eerste opstart

- Die **kaart van Europa** (Natural Earth-kuslyne en -grense) word die eerste keer outomaties in `data/mappa` afgelaai: 'n internetverbinding is een keer nodig.
- Die **radardata** (Collm, Sodankylä) word dadelik afgelaai en daarna elke 5 minute nagegaan.
- Die koppelvlak begin in jou stelseltaal as dit een van die ses beskikbare tale is, anders in Italiaans; verander dit regs bo (sien [Instellings](Settings-and-Data-Folder-af#taal)).

## Bywerking

Installeer die nuwe weergawe **oor die ou een** (dieselfde installeerder, dieselfde gids). Die instellings (`config.ini`), die vloedargiewe en die kaart bly in `data`. Vertaallêers in `data/lingue` word vervang wanneer die nuwes meer onlangs is.

## Bou vanaf die bronkode (slegs vir ontwikkelaars)

Die installeerders word deur GitHub Actions (`.github/workflows/build.yml`) gebou by elke bywerking van die `release`-tak (weergawe uit die `VERSION`-lêer geneem), wat ook die release `vX.Y.Z` skep. Plaaslik:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # of linux-x64, linux-arm64, linux-arm, osx-arm64
```

Die dokumente word hergenereer met `tools/build_spiegazione.py data` en `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Volgende: [Aan die gang](Getting-Started-af).
