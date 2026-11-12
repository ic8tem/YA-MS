# YA-MS

**Italiano** · [English](README.en.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português](README.pt.md)

[![Ko-fi](https://img.shields.io/badge/Ko--fi-ic8tem-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/ic8tem)

**YA-MS** calcola, in diretta e in previsione, l'efficienza degli sciami meteorici per i collegamenti radioamatoriali in **meteor scatter** (50–432 MHz): dove guardano i radianti, quali hot spot usare, quando la tratta rende di più e quanto segnale arriva.
A cura di Costantino Cerrotta IC8TEM. Gratuito, per Windows, Linux, Raspberry Pi e Mac. Interfaccia, wiki e manuali in 36 lingue.

![Calcolo previsionale: volta celeste, pianta della tratta e hot spot](docs/screenshots/readme/it-1.png)

## Cosa fa
- **Calcolo previsionale**: volta celeste con i radianti, pianta della tratta con Hot A / Hot B, lobo d'antenna, zone PREV e direzioni migliori; fascia riassuntiva con l'efficienza del momento scelto (data e ore da −12 a +36 h).
- **Calcolo dell'efficienza** ora per ora per ogni sciame, con il confronto con la formula di DH9GCD e le impostazioni pronte *Prudente* (di partenza) e *Come DJ5HG*.
- **Geometria e attenuazione**: perdita di tratta (McKinley, ITU-R P.843) e bilancio con i valori prudenti.
- **Dati in diretta**: flusso dei radar meteorici SKiYMET (Collm, Sodankylä) con la stima a 50/144/432 MHz, radar GRAVES, raccolta degli spot MS da DX cluster, Reverse Beacon Network e PSKReporter (anche MQTT), traffico in diretta su mappa.
- **Documenti tecnici**: fonti con i confronti, manuale dei calcoli e spiegazione dell'efficienza con tutte le equazioni.

![Calcolo dell'efficienza ora per ora](docs/screenshots/readme/it-2.png)

![Flusso dei radar meteorici](docs/screenshots/readme/it-3.png)

## Installazione
Dalla pagina **[Releases](https://github.com/ic8tem/YA-MS/releases/latest)**:
- **Windows**: `...-windows-x64-setup.exe` (a 32 bit `...-windows-x86-setup.exe`, su ARM/Snapdragon `...-windows-arm64-setup.exe`) o lo zip portatile;
- **Linux**: `ya-ms_..._amd64.deb` oppure `...-linux-x64.tar.gz`;
- **Fedora, openSUSE**: `ya-ms-....x86_64.rpm` o `.aarch64.rpm` / `.armv7hl.rpm` (`sudo dnf install` / `sudo zypper install`);
- **Arch, Manjaro, Arch Linux ARM**: `ya-ms-...-x86_64.pkg.tar.zst` / `-aarch64.pkg.tar.zst` (`sudo pacman -U`);
- **Slackware64, Slackware ARM64**: `ya-ms-...-x86_64-1_ic8tem.txz` / `-aarch64-1_ic8tem.txz` (`installpkg`);
- **AppImage**: `YA-MS-...-x86_64.AppImage` / `-aarch64.AppImage`;
- **Alpine Linux** (musl): `YA-MS-...-alpine-x64.tar.gz` / `-alpine-arm64.tar.gz`;
- **Raspberry Pi**: `ya-ms_..._arm64.deb` / `_armhf.deb` oppure i tar.gz a 64 e 32 bit;
- **Linux ARM** (es. Slackware ARM64, schede armv7l): `...-linux-arm64.tar.gz` o `...-linux-armv7l.tar.gz`;
- **Mac**: `...-mac-apple-silicon.dmg` o `...-mac-intel.dmg` (oppure l'app.zip).

I dati restano nella cartella `data` accanto al programma. Istruzioni complete nel **[wiki](https://github.com/ic8tem/YA-MS/wiki/Home-it)** e nel file `LEGGIMI.txt`.

Dalla 1.8.0 YA-MS controlla da solo su GitHub se c'è una versione nuova e si aggiorna con un clic (pulsante **Aggiornamenti** in basso), tenendo la cartella `data`; se mancano file del programma propone di riscaricarli.

## Fonte principale
C. Cerrotta IC8TEM, G. Sartori IV3GTH, «METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese». Le altre fonti sono elencate nel programma e nel wiki.

## Compilazione
Gli installatori li produce GitHub Actions (`.github/workflows/build.yml`) a ogni aggiornamento del ramo `release` (versione dal file `VERSION`). In locale: `dotnet publish YA-MS.csproj -c Release -r <rid> --self-contained true`. I documenti in tutte le lingue si rigenerano con `tools/build_documenti.sh`.

I dati dei radar appartengono ai rispettivi enti (Università di Lipsia / IAP Kühlungsborn, Sodankylä Geophysical Observatory).

## Sostieni il progetto
YA-MS è gratuito. Se ti è utile puoi offrirmi un caffè su **[Ko-fi](https://ko-fi.com/ic8tem)**.
