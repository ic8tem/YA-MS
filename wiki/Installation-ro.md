[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · **Română** · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [ไทย](Installation-th) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Instalare

Toate pachetele se află pe pagina **[Releases](https://github.com/ic8tem/YA-MS/releases)** (în numele fișierelor de mai jos `x.y.z` este versiunea, de ex. `1.2.0`). Nu trebuie compilat nimic și nu trebuie instalat nimic altceva: fiecare pachet conține runtime-ul .NET 8.

| Sistem | Fișier | Se instalează în |
|---|---|---|
| Windows (64 de biți) | `YA-MS-x.y.z-windows-x64-setup.exe` (program de instalare) | `C:\YA-MS` |
| Windows (64 de biți), portabil | `YA-MS-x.y.z-windows-x64-portatile.zip` | orice dosar în care poți scrie |
| Windows (32 de biți, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` sau `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 de biți) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 de biți) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 de biți) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**Programul și dosarul său `data` stau întotdeauna împreună** în dosarul YA-MS: acolo sunt toate datele și setările (fără AppData, fără dosare de sistem). Vezi [Setări și dosarul de date](Settings-and-Data-Folder-ro).

## Windows

### Program de instalare
1. Descarcă `YA-MS-x.y.z-windows-x64-setup.exe` și rulează-l.
2. Dacă **SmartScreen** afișează „Windows a protejat PC-ul”: *Mai multe informații* → *Rulează oricum* (programul nu este semnat cu un certificat comercial).
3. YA-MS se instalează în **`C:\YA-MS`**, **fără drepturi de administrator**, cu o pictogramă în meniul Start și, dacă bifezi opțiunea, o pictogramă pe desktop.

### Portabil
Extrage `YA-MS-x.y.z-windows-x64-portatile.zip` unde dorești (într-un dosar în care poți scrie, nu în *Program Files*) și rulează `YA-MS.exe`. Poți copia întregul dosar pe un stick USB sau pe alt calculator.

## Linux

1. Extrage `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Din dosarul extras rulează:
   ```sh
   ./installa.sh
   ```
3. Scriptul copiază YA-MS în **`~/YA-MS`** (nu este nevoie de root) și adaugă **YA-MS** în meniul aplicațiilor (categoria *HamRadio*). Îl poți porni și cu `~/YA-MS/YA-MS`.

Pentru textul japonez s-ar putea să ai nevoie de fonturile Noto CJK: vezi [Depanare](Troubleshooting-FAQ-ro#linux-textul-japonez-apare-ca-pătrățele).

## Raspberry Pi

Aceeași procedură ca la Linux: extrage `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (sau `-32bit` pe Raspberry Pi OS pe 32 de biți) și rulează `./installa.sh` din dosarul extras.

- Ca să vezi ce sistem ai, scrie `uname -m` într-un terminal: `aarch64` → pachetul pe 64 de biți, `armv7l` → pachetul pe 32 de biți.
- Suportate: Raspberry Pi 2 (doar 32 de biți), 3, 4, 5, 400 și 500, cu versiunea desktop a Raspberry Pi OS. **Nesuportate:** Pi Zero / Zero W și Pi 1 (procesor ARMv6, .NET nu rulează pe ele); Pi Zero 2 W funcționează cu pachetul pe 64 de biți, dar 512 MB de RAM sunt la limită.
- Se recomandă un Pi 4 sau 5 cu cel puțin 2 GB de RAM; prima pornire durează câteva secunde mai mult decât pe un PC.

## macOS

1. Alege fișierul potrivit: `-mac-apple-silicon.dmg` pentru procesoarele M1/M2/M3/M4, `-mac-intel.dmg` pentru Mac-urile Intel.
2. Deschide `.dmg`-ul, **clic dreapta pe „Installa YA-MS.command” → Deschide** și confirmă.
3. Scriptul copiază `YA-MS.app` în **`~/YA-MS`** și îl deschide.

Programul nu este semnat de Apple, așa că prima dată macOS cere confirmare; vezi [Depanare](Troubleshooting-FAQ-ro#macos-nu-poate-fi-deschis-deoarece-provine-de-la-un-dezvoltator-neidentificat).

## Prima pornire

- **Harta Europei** (coastele și granițele Natural Earth) se descarcă automat în `data/mappa` prima dată: este nevoie de o conexiune la internet o singură dată.
- **Datele radar** (Collm, Sodankylä) se descarcă imediat și apoi se verifică la fiecare 5 minute.
- Interfața pornește în limba sistemului tău dacă este una dintre cele 36 disponibile, altfel în italiană; o schimbi în dreapta sus (vezi [Setări](Settings-and-Data-Folder-ro#limba)).

## Actualizare

Instalează noua versiune **peste cea veche** (același program de instalare, același dosar). Setările (`config.ini`), arhivele fluxului și harta rămân în `data`. Fișierele de traducere din `data/lingue` se înlocuiesc atunci când cele noi sunt mai recente.

## Compilare din sursă (doar pentru dezvoltatori)

Programele de instalare sunt produse de GitHub Actions (`.github/workflows/build.yml`) la fiecare actualizare a ramurii `release` (versiunea este luată din fișierul `VERSION`), care creează și release-ul `vX.Y.Z`. Local:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # sau linux-x64, linux-arm64, linux-arm, osx-arm64
```

Documentele se regenerează cu `tools/build_spiegazione.py data` și `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Urmează: [Primii pași](Getting-Started-ro).
