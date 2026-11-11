[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · **Svenska** · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Installation

Alla paket finns på sidan **[Releases](https://github.com/ic8tem/YA-MS/releases)** (i filnamnen nedan är `x.y.z` versionen, t.ex. `1.2.0`). Inget behöver kompileras och inget annat behöver installeras: varje paket innehåller .NET 8-körmiljön.

| System | Fil | Installeras i |
|---|---|---|
| Windows (64 bitar) | `YA-MS-x.y.z-windows-x64-setup.exe` (installationsprogram) | `C:\YA-MS` |
| Windows (64 bitar), portabel | `YA-MS-x.y.z-windows-x64-portatile.zip` | valfri mapp där du har skrivrättighet |
| Windows (32 bitar, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` eller `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 bitar): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (kopieras dit vid första starten) |
| Linux (64 bitar), alla distributioner | `YA-MS-x.y.z-linux-x64.tar.gz` (portabel eller med `./installa.sh`) | `~/YA-MS` eller valfri mapp |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bitar) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bitar) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debianpaket | `ya-ms_x.y.z_arm64.deb` (64 bitar) eller `ya-ms_x.y.z_armhf.deb` (32 bitar) | `~/YA-MS` (kopieras dit vid första starten) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, endast programmet | `YA-MS-x.y.z-mac-apple-silicon-app.zip` eller `...-mac-intel-app.zip` | mappen där du packar upp `YA-MS.app` |

**Programmet och dess mapp `data` hålls alltid ihop** i mappen YA-MS: där finns alla data och inställningar (ingen AppData, inga systemmappar). Se [Inställningar och datamapp](Settings-and-Data-Folder-sv).

## Windows

### Installationsprogram
1. Ladda ned `YA-MS-x.y.z-windows-x64-setup.exe` och kör den.
2. Om **SmartScreen** visar "Windows skyddade datorn": *Mer information* → *Kör ändå* (programmet är inte signerat med ett kommersiellt certifikat).
3. YA-MS installeras i **`C:\YA-MS`**, **utan administratörsrättigheter**, med en ikon i Start-menyn och, om du kryssar i det, en ikon på skrivbordet.

### Portabel
Packa upp `YA-MS-x.y.z-windows-x64-portatile.zip` var du vill (i en mapp där du har skrivrättighet, inte *Program Files*) och kör `YA-MS.exe`. Du kan kopiera hela mappen till ett USB-minne eller en annan dator.

## Linux

1. Packa upp `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Kör i den uppackade mappen:
   ```sh
   ./installa.sh
   ```
3. Skriptet kopierar YA-MS till **`~/YA-MS`** (root behövs inte) och lägger till **YA-MS** i programmenyn (kategori *HamRadio*). Du kan också starta det med `~/YA-MS/YA-MS`.

### Debianpaket (.deb)
På Debian, Ubuntu, Mint och Raspberry Pi OS kan du i stället installera `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` på Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Paketet lägger programmet i `/opt/ya-ms` och lägger till **YA-MS** i menyn. Vid första starten (och efter varje ny version) kopierar det sig självt till **`~/YA-MS`** och körs därifrån, så att mappen `data` ligger kvar bredvid programmet och dina inställningar behålls.

### Portabel
`.tar.gz`-filen fungerar också utan installation: packa upp den var som helst där du har skrivrättighet och kör `./YA-MS` från den mappen.

För japansk text kan du behöva typsnitten Noto CJK: se [Felsökning](Troubleshooting-FAQ-sv#linux-japansk-text-visas-som-rutor).

## Raspberry Pi

Samma procedur som för Linux: packa upp `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (eller `-32bit` på Raspberry Pi OS 32 bitar) och kör `./installa.sh` i den uppackade mappen.

- För att se vilket system du har, skriv `uname -m` i en terminal: `aarch64` → 64-bitarspaketet, `armv7l` → 32-bitarspaketet.
- Stöds: Raspberry Pi 2 (endast 32 bitar), 3, 4, 5, 400 och 500, med skrivbordsversionen av Raspberry Pi OS. **Stöds inte:** Pi Zero / Zero W och Pi 1 (ARMv6-processor, .NET körs inte där); Pi Zero 2 W fungerar med 64-bitarspaketet men 512 MB RAM är snålt.
- En Pi 4 eller 5 med minst 2 GB RAM rekommenderas; första starten tar några sekunder längre än på en PC.

## macOS

1. Välj rätt fil: `-mac-apple-silicon.dmg` för processorerna M1/M2/M3/M4, `-mac-intel.dmg` för Mac med Intel.
2. Öppna `.dmg`-filen, **högerklicka på "Installa YA-MS.command" → Öppna** och bekräfta.
3. Skriptet kopierar `YA-MS.app` till **`~/YA-MS`** och öppnar det.

Alternativt innehåller `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` bara `YA-MS.app`: packa upp den i en valfri mapp (där du har skrivrättighet); mappen `data` skapas bredvid `YA-MS.app`. Första gången: högerklicka → **Öppna**.

Programmet är inte signerat av Apple, så första gången ber macOS om bekräftelse; se [Felsökning](Troubleshooting-FAQ-sv#macos-kan-inte-öppnas-eftersom-den-kommer-från-en-oidentifierad-utvecklare).

## Första starten

- **Europakartan** (kustlinjer och gränser från Natural Earth) hämtas automatiskt till `data/mappa` första gången: en internetanslutning behövs en gång.
- **Radardata** (Collm, Sodankylä) hämtas direkt och kontrolleras sedan var 5:e minut.
- Gränssnittet startar på systemets språk om det är ett av de 36 tillgängliga, annars på italienska; byt språk uppe till höger (se [Inställningar](Settings-and-Data-Folder-sv#språk)).

## Uppdatering

Installera den nya versionen **ovanpå den gamla** (samma installationsprogram, samma mapp). Inställningar (`config.ini`), flödesarkiv och karta finns kvar i `data`. Översättningsfilerna i `data/lingue` ersätts när de nya är nyare.

**Från 1.8.0 uppdaterar YA-MS sig självt.** Vid start kontrollerar det en gång om dagen på GitHub om det finns en ny version och erbjuder den; knappen **Uppdateringar** i nedre fältet kontrollerar för hand. *Uppdatera nu* laddar ner det portabla paketet för ditt system, ersätter programfilerna, behåller mappen `data` (programfiler som ändras kopieras först till `data/backup/v<gammal version>`) och startar om; programmappen måste vara skrivbar. Saknas programfiler vid start (i `data` eller `doc`) listar ett fönster dem och erbjuder att ladda ner dem igen från GitHub. För att sluta söka efter nya versioner, sätt `controlla_aggiornamenti=0` i `config.ini`.

## Bygga från källkod (endast för utvecklare)

Installationsprogrammen skapas av GitHub Actions (`.github/workflows/build.yml`) vid varje uppdatering av grenen `release` (versionen tas från filen `VERSION`), som också skapar releasen `vX.Y.Z`. Lokalt:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # eller linux-x64, linux-arm64, linux-arm, osx-arm64
```

Dokumenten (alla språk) genereras på nytt med `tools/build_documenti.sh`.

Nästa: [Kom igång](Getting-Started-sv).
