[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Dansk](Installation-da) · **Norsk** · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh)

# Installasjon

Alle pakkene ligger på siden **[Releases](https://github.com/ic8tem/YA-MS/releases)** (i filnavnene nedenfor er `x.y.z` versjonen, f.eks. `1.2.0`). Ingenting skal kompileres, og ingenting annet skal installeres: hver pakke inneholder .NET 8-runtime.

| System | Fil | Installeres i |
|---|---|---|
| Windows (64-bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (installasjonsprogram) | `C:\YA-MS` |
| Windows (64-bit), portabel | `YA-MS-x.y.z-windows-x64-portatile.zip` | en hvilken som helst mappe der du har skrivetilgang |
| Windows (32-bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` eller `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-bit): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (kopieres dit ved første oppstart) |
| Linux (64-bit), alle distribusjoner | `YA-MS-x.y.z-linux-x64.tar.gz` (portabel eller med `./installa.sh`) | `~/YA-MS` eller en hvilken som helst mappe |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian-pakke | `ya-ms_x.y.z_arm64.deb` (64-bit) eller `ya-ms_x.y.z_armhf.deb` (32-bit) | `~/YA-MS` (kopieres dit ved første oppstart) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, bare programmet | `YA-MS-x.y.z-mac-apple-silicon-app.zip` eller `...-mac-intel-app.zip` | mappen der du pakker ut `YA-MS.app` |

**Programmet og `data`-mappen hører alltid sammen** i YA-MS-mappen: alle data og innstillinger ligger der (ingen AppData, ingen systemmapper). Se [Innstillinger og datamappe](Settings-and-Data-Folder-nb).

## Windows

### Installasjonsprogram
1. Last ned `YA-MS-x.y.z-windows-x64-setup.exe` og kjør den.
2. Hvis **SmartScreen** viser «Windows beskyttet PC-en»: *Mer informasjon* → *Kjør likevel* (programmet er ikke signert med et kommersielt sertifikat).
3. YA-MS installeres i **`C:\YA-MS`**, **uten administratorrettigheter**, med et ikon i Start-menyen og, hvis du krysser av, et ikon på skrivebordet.

### Portabel
Pakk ut `YA-MS-x.y.z-windows-x64-portatile.zip` der du vil (en mappe med skrivetilgang, ikke *Program Files*) og kjør `YA-MS.exe`. Du kan kopiere hele mappen til en minnepinne eller en annen datamaskin.

## Linux

1. Pakk ut `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Kjør fra den utpakkede mappen:
   ```sh
   ./installa.sh
   ```
3. Skriptet kopierer YA-MS til **`~/YA-MS`** (root trengs ikke) og legger **YA-MS** til i programmenyen (kategori *HamRadio*). Du kan også starte det med `~/YA-MS/YA-MS`.

### Debian-pakke (.deb)
På Debian, Ubuntu, Mint og Raspberry Pi OS kan du i stedet installere `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` på Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Pakken legger programmet i `/opt/ya-ms` og legger **YA-MS** til i menyen. Ved første oppstart (og etter hver nye versjon) kopierer det seg selv til **`~/YA-MS`** og kjører derfra, slik at mappen `data` blir liggende ved siden av programmet og innstillingene dine beholdes.

### Portabel
`.tar.gz`-filen fungerer også uten installasjon: pakk den ut et sted der du har skrivetilgang, og kjør `./YA-MS` fra den mappen.

For japansk tekst kan du trenge Noto CJK-skriftene: se [Feilsøking](Troubleshooting-FAQ-nb#linux-japansk-tekst-vises-som-firkanter).

## Raspberry Pi

Samme framgangsmåte som for Linux: pakk ut `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (eller `-32bit` på Raspberry Pi OS 32-bit) og kjør `./installa.sh` fra den utpakkede mappen.

- For å se hvilket system du har, skriv `uname -m` i en terminal: `aarch64` → 64-bitspakken, `armv7l` → 32-bitspakken.
- Støttet: Raspberry Pi 2 (bare 32-bit), 3, 4, 5, 400 og 500, med skrivebordsutgaven av Raspberry Pi OS. **Ikke støttet:** Pi Zero / Zero W og Pi 1 (ARMv6-prosessor, .NET kjører ikke der); Pi Zero 2 W fungerer med 64-bitspakken, men 512 MB RAM er i knappeste laget.
- En Pi 4 eller 5 med minst 2 GB RAM anbefales; første oppstart tar noen sekunder lenger enn på en PC.

## macOS

1. Velg riktig fil: `-mac-apple-silicon.dmg` for M1/M2/M3/M4-prosessorer, `-mac-intel.dmg` for Intel-Macer.
2. Åpne `.dmg`-filen, **høyreklikk på «Installa YA-MS.command» → Åpne** og bekreft.
3. Skriptet kopierer `YA-MS.app` til **`~/YA-MS`** og åpner det.

Alternativt inneholder `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` bare `YA-MS.app`: pakk den ut i en mappe du velger selv (med skrivetilgang); mappen `data` opprettes ved siden av `YA-MS.app`. Første gang: høyreklikk → **Åpne**.

Programmet er ikke signert av Apple, så første gang ber macOS om bekreftelse; se [Feilsøking](Troubleshooting-FAQ-nb#macos-kan-ikke-åpnes-fordi-det-er-fra-en-ukjent-utvikler).

## Første oppstart

- **Europakartet** (kystlinjer og grenser fra Natural Earth) lastes ned automatisk til `data/mappa` første gang: internettforbindelse trengs én gang.
- **Radardataene** (Collm, Sodankylä) lastes ned med en gang og sjekkes deretter hvert 5. minutt.
- Grensesnittet starter på systemspråket hvis det er ett av de seks tilgjengelige, ellers på italiensk; bytt det øverst til høyre (se [Innstillinger](Settings-and-Data-Folder-nb#språk)).

## Oppdatering

Installer den nye versjonen **oppå den gamle** (samme installasjonsprogram, samme mappe). Innstillingene (`config.ini`), fluksarkivene og kartet blir liggende i `data`. Oversettelsesfilene i `data/lingue` erstattes når de nye er nyere.

## Bygge fra kildekoden (bare for utviklere)

Installasjonspakkene lages av GitHub Actions (`.github/workflows/build.yml`) ved hver oppdatering av grenen `release` (versjonen hentes fra filen `VERSION`), som også oppretter utgivelsen `vX.Y.Z`. Lokalt:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # eller linux-x64, linux-arm64, linux-arm, osx-arm64
```

Dokumentene genereres på nytt med `tools/build_spiegazione.py data` og `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Neste: [Komme i gang](Getting-Started-nb).
