[English](Installation) · **Italiano** · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh)

# Installazione

Tutti i pacchetti sono nella pagina **[Releases](https://github.com/ic8tem/YA-MS/releases)** (nei nomi dei file qui sotto `x.y.z` è la versione, per esempio `1.2.0`). Non c'è niente da compilare e niente altro da installare: ogni pacchetto contiene il runtime .NET 8.

| Sistema | File | Si installa in |
|---|---|---|
| Windows (64 bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (installatore) | `C:\YA-MS` |
| Windows (64 bit), portatile | `YA-MS-x.y.z-windows-x64-portatile.zip` | qualsiasi cartella in cui puoi scrivere |
| Windows (32 bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` oppure `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 bit): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (copiato lì al primo avvio) |
| Linux (64 bit), qualsiasi distribuzione | `YA-MS-x.y.z-linux-x64.tar.gz` (portatile o con `./installa.sh`) | `~/YA-MS` o qualsiasi cartella |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, pacchetto Debian | `ya-ms_x.y.z_arm64.deb` (64 bit) oppure `ya-ms_x.y.z_armhf.deb` (32 bit) | `~/YA-MS` (copiato lì al primo avvio) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, solo applicazione | `YA-MS-x.y.z-mac-apple-silicon-app.zip` oppure `...-mac-intel-app.zip` | la cartella in cui estrai `YA-MS.app` |

**Il programma e la sua cartella `data` stanno sempre insieme** nella cartella YA-MS: lì ci sono tutti i dati e le impostazioni (niente AppData, niente cartelle di sistema). Vedi [Impostazioni e cartella dei dati](Settings-and-Data-Folder-it).

## Windows

### Installatore
1. Scarica `YA-MS-x.y.z-windows-x64-setup.exe` ed eseguilo.
2. Se **SmartScreen** mostra "Windows ha protetto il PC": *Ulteriori informazioni* → *Esegui comunque* (il programma non è firmato con un certificato commerciale).
3. YA-MS viene installato in **`C:\YA-MS`**, **senza diritti di amministratore**, con un'icona nel menu Start e, se la spunti, un'icona sul desktop.

### Portatile
Estrai `YA-MS-x.y.z-windows-x64-portatile.zip` dove preferisci (in una cartella in cui puoi scrivere, non in *Programmi*) ed esegui `YA-MS.exe`. Puoi copiare l'intera cartella su una chiavetta USB o su un altro computer.

## Linux

1. Estrai `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Dalla cartella estratta esegui:
   ```sh
   ./installa.sh
   ```
3. Lo script copia YA-MS in **`~/YA-MS`** (non servono i permessi di root) e aggiunge **YA-MS** al menu delle applicazioni (categoria *HamRadio*). Puoi anche avviarlo con `~/YA-MS/YA-MS`.

### Pacchetto Debian (.deb)
Su Debian, Ubuntu, Mint e Raspberry Pi OS puoi invece installare `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` sul Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Il pacchetto mette il programma in `/opt/ya-ms` e aggiunge **YA-MS** al menu. Al primo avvio (e dopo ogni nuova versione) si copia in **`~/YA-MS`** e parte da lì, così la cartella `data` resta accanto al programma e le tue impostazioni vengono conservate.

### Portatile
Il `.tar.gz` funziona anche senza installazione: estrailo in una cartella qualsiasi in cui puoi scrivere ed esegui `./YA-MS` da quella cartella.

Per il testo giapponese possono servire i font Noto CJK: vedi [Problemi e domande frequenti](Troubleshooting-FAQ-it#linux-il-testo-giapponese-appare-come-quadratini).

## Raspberry Pi

Stessa procedura di Linux: estrai `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (oppure `-32bit` su Raspberry Pi OS a 32 bit) ed esegui `./installa.sh` dalla cartella estratta.

- Per sapere quale sistema hai, scrivi `uname -m` in un terminale: `aarch64` → pacchetto a 64 bit, `armv7l` → pacchetto a 32 bit.
- Supportati: Raspberry Pi 2 (solo 32 bit), 3, 4, 5, 400 e 500, con la versione desktop di Raspberry Pi OS. **Non supportati:** Pi Zero / Zero W e Pi 1 (processore ARMv6, .NET non ci gira); il Pi Zero 2 W funziona con il pacchetto a 64 bit, ma 512 MB di RAM sono pochi.
- Si consiglia un Pi 4 o 5 con almeno 2 GB di RAM; il primo avvio richiede qualche secondo in più che su un PC.

## macOS

1. Scegli il file giusto: `-mac-apple-silicon.dmg` per i processori M1/M2/M3/M4, `-mac-intel.dmg` per i Mac Intel.
2. Apri il `.dmg`, fai **clic destro su "Installa YA-MS.command" → Apri** e conferma.
3. Lo script copia `YA-MS.app` in **`~/YA-MS`** e lo apre.

In alternativa, `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` contiene solo `YA-MS.app`: estrailo in una cartella a tua scelta (in cui puoi scrivere); la cartella `data` viene creata accanto a `YA-MS.app`. La prima volta fai clic destro → **Apri**.

Il programma non è firmato da Apple, quindi la prima volta macOS chiede una conferma; vedi [Problemi e domande frequenti](Troubleshooting-FAQ-it#macos-non-è-possibile-aprire-perché-proviene-da-uno-sviluppatore-non-identificato).

## Primo avvio

- La **mappa d'Europa** (coste e confini di Natural Earth) viene scaricata automaticamente in `data/mappa` la prima volta: serve una connessione internet una sola volta.
- I **dati radar** (Collm, Sodankylä) vengono scaricati subito e poi controllati ogni 5 minuti.
- L'interfaccia parte nella lingua del sistema se è una delle 28 disponibili, altrimenti in italiano; la cambi in alto a destra (vedi [Impostazioni](Settings-and-Data-Folder-it#lingua)).

## Aggiornamento

Installa la nuova versione **sopra la vecchia** (stesso installatore, stessa cartella). Le impostazioni (`config.ini`), gli archivi del flusso e la mappa restano in `data`. I file di traduzione in `data/lingue` vengono sostituiti quando i nuovi sono più recenti.

## Compilare dai sorgenti (solo per sviluppatori)

Gli installatori sono prodotti da GitHub Actions (`.github/workflows/build.yml`) a ogni aggiornamento del ramo `release` (versione presa dal file `VERSION`), che crea anche la release `vX.Y.Z`. In locale:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # oppure linux-x64, linux-arm64, linux-arm, osx-arm64
```

I documenti si rigenerano con `tools/build_spiegazione.py data` e `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Avanti: [Primi passi](Getting-Started-it).
