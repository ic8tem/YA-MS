[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · **Română** · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Instalare

Toate pachetele se află pe pagina **[Releases](https://github.com/ic8tem/YA-MS/releases)** (în numele fișierelor de mai jos, `x.y.z` este versiunea, de ex. `1.2.0`). Nu trebuie compilat nimic și nu trebuie instalat nimic altceva: fiecare pachet conține runtime-ul .NET 8.

| Sistem | Fișier | Se instalează în |
|---|---|---|
| Windows (64 de biți) | `YA-MS-x.y.z-windows-x64-setup.exe` (program de instalare) | `C:\YA-MS` |
| Windows (64 de biți), portabil | `YA-MS-x.y.z-windows-x64-portatile.zip` | orice dosar în care puteți scrie |
| Windows (32 de biți, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` sau `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Windows pe ARM (64 de biți, PC-uri cu Snapdragon) | `YA-MS-x.y.z-windows-arm64-setup.exe` sau `...-windows-arm64-portatile.zip` | `C:\YA-MS` |
| Linux (64 de biți): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (copiat acolo la prima pornire) |
| Linux (64 de biți), orice distribuție | `YA-MS-x.y.z-linux-x64.tar.gz` (portabil sau cu `./installa.sh`) | `~/YA-MS` sau orice dosar |
| Linux (64 de biți): Fedora, openSUSE | `ya-ms-x.y.z.x86_64.rpm` (x86_64), `ya-ms-x.y.z.aarch64.rpm` (ARM64), `ya-ms-x.y.z.armv7hl.rpm` (ARM 32) | `~/YA-MS` (copiat acolo la prima pornire) |
| Arch, Manjaro, EndeavourOS, Arch Linux ARM | `ya-ms-x.y.z-1-x86_64.pkg.tar.zst`, `ya-ms-x.y.z-1-aarch64.pkg.tar.zst` | `~/YA-MS` (copiat acolo la prima pornire) |
| Slackware64, Slackware ARM64 | `ya-ms-x.y.z-x86_64-1_ic8tem.txz`, `ya-ms-x.y.z-aarch64-1_ic8tem.txz` | `~/YA-MS` (copiat acolo la prima pornire) |
| AppImage (x86_64, aarch64) | `YA-MS-x.y.z-x86_64.AppImage`, `YA-MS-x.y.z-aarch64.AppImage` | `~/YA-MS` (copiat acolo la prima pornire) |
| Alpine Linux (musl) | `YA-MS-x.y.z-alpine-x64.tar.gz`, `YA-MS-x.y.z-alpine-arm64.tar.gz` | `~/YA-MS` sau orice dosar |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 de biți) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 de biți) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, pachet Debian | `ya-ms_x.y.z_arm64.deb` (64 de biți) sau `ya-ms_x.y.z_armhf.deb` (32 de biți) | `~/YA-MS` (copiat acolo la prima pornire) |
| Linux ARM pe 64 de biți, orice distribuție (de ex. Slackware ARM64) | `YA-MS-x.y.z-linux-arm64.tar.gz` (portabil sau cu `./installa.sh`) | `~/YA-MS` sau orice dosar |
| Linux armv7l (ARM pe 32 de biți), orice distribuție | `YA-MS-x.y.z-linux-armv7l.tar.gz` (portabil sau cu `./installa.sh`) | `~/YA-MS` sau orice dosar |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, doar aplicația | `YA-MS-x.y.z-mac-apple-silicon-app.zip` sau `...-mac-intel-app.zip` | dosarul în care extrageți `YA-MS.app` |

**Programul și dosarul său `data` stau întotdeauna împreună** în dosarul YA-MS: toate datele și setările se află acolo (fără AppData, fără dosare de sistem). Vedeți [Setări și dosarul de date](Settings-and-Data-Folder-ro).

## Windows

### Program de instalare
1. Descărcați `YA-MS-x.y.z-windows-x64-setup.exe` și rulați-l.
2. Dacă **SmartScreen** afișează „Windows v-a protejat PC-ul”: *Mai multe informații* → *Rulați oricum* (programul nu este semnat cu un certificat comercial).
3. YA-MS se instalează în **`C:\YA-MS`**, **fără drepturi de administrator**, cu o pictogramă în meniul Start și, dacă bifați opțiunea, o pictogramă pe desktop.

### Portabil
Extrageți `YA-MS-x.y.z-windows-x64-portatile.zip` unde doriți (într-un dosar în care puteți scrie, nu în *Program Files*) și rulați `YA-MS.exe`. Puteți copia întregul dosar pe un stick USB sau pe alt calculator.

## Linux

1. Extrageți `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Din dosarul extras rulați:
   ```sh
   ./installa.sh
   ```
3. Scriptul copiază YA-MS în **`~/YA-MS`** (nu este nevoie de root) și adaugă **YA-MS** în meniul de aplicații (categoria *HamRadio*). Îl puteți porni și cu `~/YA-MS/YA-MS`.

### Pachet Debian (.deb)
Pe Debian, Ubuntu, Mint și Raspberry Pi OS puteți instala în schimb `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` pe Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Pachetul pune programul în `/opt/ya-ms` și adaugă **YA-MS** în meniu. La prima pornire (și după fiecare versiune nouă) se copiază în **`~/YA-MS`** și rulează de acolo, astfel încât dosarul `data` rămâne lângă program și setările dumneavoastră se păstrează.

### Portabil
Și `.tar.gz` funcționează fără instalare: extrageți-l oriunde puteți scrie și rulați `./YA-MS` din acel dosar.

Pentru textul japonez s-ar putea să aveți nevoie de fonturile Noto CJK: vedeți [Rezolvarea problemelor](Troubleshooting-FAQ-ro#linux-textul-japonez-apare-ca-pătrățele).

## Raspberry Pi

Aceeași procedură ca pe Linux: extrageți `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (sau `-32bit` pe Raspberry Pi OS pe 32 de biți) și rulați `./installa.sh` din dosarul extras.

- Pentru a vedea ce sistem aveți, tastați `uname -m` într-un terminal: `aarch64` → pachetul pe 64 de biți, `armv7l` → pachetul pe 32 de biți.
- Suportate: Raspberry Pi 2 (doar 32 de biți), 3, 4, 5, 400 și 500, cu versiunea desktop a Raspberry Pi OS. **Nesuportate:** Pi Zero / Zero W și Pi 1 (procesor ARMv6, .NET nu rulează pe ele); Pi Zero 2 W funcționează cu pachetul pe 64 de biți, dar 512 MB de RAM sunt la limită.
- Se recomandă un Pi 4 sau 5 cu cel puțin 2 GB de RAM; prima pornire durează câteva secunde mai mult decât pe un PC.

## macOS

1. Alegeți fișierul potrivit: `-mac-apple-silicon.dmg` pentru procesoarele M1/M2/M3/M4, `-mac-intel.dmg` pentru Mac-urile Intel.
2. Deschideți `.dmg`, **clic dreapta pe „Installa YA-MS.command” → Deschide** și confirmați.
3. Scriptul copiază `YA-MS.app` în **`~/YA-MS`** și îl deschide.

Alternativ, `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` conține doar `YA-MS.app`: extrageți-l într-un dosar ales de dumneavoastră (în care puteți scrie); dosarul `data` se creează lângă `YA-MS.app`. Prima dată, clic dreapta → **Deschide**.

Programul nu este semnat de Apple, așa că prima dată macOS cere o confirmare; vedeți [Rezolvarea problemelor](Troubleshooting-FAQ-ro#macos-nu-poate-fi-deschis-deoarece-provine-de-la-un-dezvoltator-neidentificat).

## Prima pornire

- **Harta Europei** (liniile de coastă și granițele Natural Earth) se descarcă automat în `data/mappa` prima dată: este nevoie de o conexiune la internet o singură dată.
- **Datele radar** (Collm, Sodankylä) se descarcă imediat și apoi se verifică la fiecare 5 minute.
- Interfața pornește în limba sistemului dumneavoastră dacă este una dintre cele 36 disponibile, altfel în italiană; o puteți schimba în dreapta sus (vedeți [Setări](Settings-and-Data-Folder-ro#limba)).

## Actualizare

Instalați noua versiune **peste cea veche** (același program de instalare, același dosar). Setările (`config.ini`), arhivele de flux și harta rămân în `data`. Fișierele de traducere din `data/lingue` sunt înlocuite când cele noi sunt mai recente.

**De la 1.8.0, YA-MS se actualizează singur.** La pornire, o dată pe zi, verifică pe GitHub dacă există o versiune nouă și o propune; butonul **Actualizări** din bara de jos face verificarea manual. *Actualizează acum* descarcă pachetul portabil pentru sistemul tău, înlocuiește fișierele programului, păstrează dosarul `data` (fișierele programului care se schimbă sunt mai întâi copiate în `data/backup/v<versiunea veche>`) și repornește; trebuie să se poată scrie în dosarul programului. Dacă la pornire lipsesc fișiere ale programului (în `data` sau `doc`), o fereastră le enumeră și propune să le descarce din nou de pe GitHub. Ca să nu mai cauți versiuni noi, pune `controlla_aggiornamenti=0` în `config.ini`.

Începând cu versiunea 1.8.6 actualizările sunt automate și silențioase: la pornire și apoi la fiecare 6 ore YA-MS verifică GitHub și, dacă există o versiune nouă, o descarcă, o instalează și repornește singur fără să întrebe nimic (doar bara de stare o spune). Și fișierele lipsă se descarcă din nou fără să întrebe. Fereastra descrisă mai jos apare doar apăsând "Actualizări" sau dacă scrii aggiornamenti_automatici=0 în fișierul data/config.ini.

## Compilare din surse (doar pentru dezvoltatori)

Programele de instalare sunt produse de GitHub Actions (`.github/workflows/build.yml`) la fiecare actualizare a ramurii `release` (versiunea este luată din fișierul `VERSION`), care creează și release-ul `vX.Y.Z`. Local:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

Documentele (toate limbile) se regenerează cu `tools/build_documenti.sh`.

Mai departe: [Primii pași](Getting-Started-ro).
