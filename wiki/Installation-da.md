[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · **Dansk** · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [ไทย](Installation-th) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Installation

Alle pakker ligger på siden **[Releases](https://github.com/ic8tem/YA-MS/releases)** (i filnavnene nedenfor er `x.y.z` versionen, fx `1.2.0`). Intet skal kompileres, og intet andet skal installeres: hver pakke indeholder .NET 8-runtime.

| System | Fil | Installeres i |
|---|---|---|
| Windows (64 bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (installationsprogram) | `C:\YA-MS` |
| Windows (64 bit), portabel | `YA-MS-x.y.z-windows-x64-portatile.zip` | en vilkårlig mappe, hvor du har skriveadgang |
| Windows (32 bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` eller `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 bit) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**Programmet og dets `data`-mappe hører altid sammen** i YA-MS-mappen: alle data og indstillinger ligger der (ingen AppData, ingen systemmapper). Se [Indstillinger og datamappe](Settings-and-Data-Folder-da).

## Windows

### Installationsprogram
1. Hent `YA-MS-x.y.z-windows-x64-setup.exe`, og kør den.
2. Hvis **SmartScreen** viser "Windows beskyttede din pc": *Flere oplysninger* → *Kør alligevel* (programmet er ikke signeret med et kommercielt certifikat).
3. YA-MS installeres i **`C:\YA-MS`**, **uden administratorrettigheder**, med et ikon i menuen Start og, hvis du sætter flueben, et ikon på skrivebordet.

### Portabel
Pak `YA-MS-x.y.z-windows-x64-portatile.zip` ud, hvor du vil (en mappe med skriveadgang, ikke *Program Files*), og kør `YA-MS.exe`. Du kan kopiere hele mappen til en USB-nøgle eller en anden computer.

## Linux

1. Pak `YA-MS-x.y.z-linux-x64.tar.gz` ud.
2. Kør fra den udpakkede mappe:
   ```sh
   ./installa.sh
   ```
3. Scriptet kopierer YA-MS til **`~/YA-MS`** (root er ikke nødvendig) og føjer **YA-MS** til programmenuen (kategori *HamRadio*). Du kan også starte det med `~/YA-MS/YA-MS`.

Til japansk tekst kan du få brug for Noto CJK-skrifttyperne: se [Fejlfinding](Troubleshooting-FAQ-da#linux-japansk-tekst-vises-som-firkanter).

## Raspberry Pi

Samme fremgangsmåde som for Linux: pak `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` ud (eller `-32bit` på Raspberry Pi OS 32 bit), og kør `./installa.sh` fra den udpakkede mappe.

- Skriv `uname -m` i en terminal for at se, hvilket system du har: `aarch64` → 64 bit-pakken, `armv7l` → 32 bit-pakken.
- Understøttet: Raspberry Pi 2 (kun 32 bit), 3, 4, 5, 400 og 500 med desktopudgaven af Raspberry Pi OS. **Ikke understøttet:** Pi Zero / Zero W og Pi 1 (ARMv6-processor, .NET kører ikke der); Pi Zero 2 W virker med 64 bit-pakken, men 512 MB RAM er i underkanten.
- En Pi 4 eller 5 med mindst 2 GB RAM anbefales; første opstart tager nogle sekunder længere end på en pc.

## macOS

1. Vælg den rigtige fil: `-mac-apple-silicon.dmg` til M1/M2/M3/M4-processorer, `-mac-intel.dmg` til Intel-Mac'er.
2. Åbn `.dmg`-filen, **højreklik på "Installa YA-MS.command" → Åbn**, og bekræft.
3. Scriptet kopierer `YA-MS.app` til **`~/YA-MS`** og åbner det.

Programmet er ikke signeret af Apple, så første gang beder macOS om bekræftelse; se [Fejlfinding](Troubleshooting-FAQ-da#macos-kan-ikke-åbnes-fordi-det-er-fra-en-ukendt-udvikler).

## Første opstart

- **Europakortet** (kystlinjer og grænser fra Natural Earth) hentes automatisk til `data/mappa` første gang: der kræves internetforbindelse én gang.
- **Radardata** (Collm, Sodankylä) hentes med det samme og kontrolleres derefter hvert 5. minut.
- Brugerfladen starter på systemets sprog, hvis det er et af de 36 tilgængelige, ellers på italiensk; skift det øverst til højre (se [Indstillinger](Settings-and-Data-Folder-da#sprog)).

## Opdatering

Installér den nye version **oven i den gamle** (samme installationsprogram, samme mappe). Indstillingerne (`config.ini`), fluxarkiverne og kortet bliver i `data`. Oversættelsesfilerne i `data/lingue` udskiftes, når de nye er nyere.

## Byg fra kildekoden (kun for udviklere)

Installationspakkerne laves af GitHub Actions (`.github/workflows/build.yml`) ved hver opdatering af grenen `release` (versionen tages fra filen `VERSION`), som også opretter udgivelsen `vX.Y.Z`. Lokalt:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # eller linux-x64, linux-arm64, linux-arm, osx-arm64
```

Dokumenterne genereres med `tools/build_spiegazione.py data` og `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Næste: [Kom godt i gang](Getting-Started-da).
