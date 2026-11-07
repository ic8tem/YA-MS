# YA-MS

**YA-MS** - previsione e calcolo in diretta dell'efficienza degli sciami meteorici per il meteor scatter (50-432 MHz).
A cura di Costantino Cerrotta IC8TEM. Windows, Linux, Raspberry Pi e Mac (.NET 8 + Avalonia).

Linguette (1.6):
- **Live e dati real-time**: Traffico in diretta (spot MS raccolti su mappa azimutale, con la nuvola della zona di scie piu' probabile), Flusso radar (SKiYMET Collm e Sodankyla, stima sperimentale a 50/144/432 MHz, confronto RMOB), Radar GRAVES, Raccolta dati (DX cluster, RBN, DM4X/PSKReporter).
- **Calcolo previsionale**: Calcolo previsionale (volta celeste e pianta della tratta: radianti, Hot A / Hot B, lobo, zone PREV, direzioni d'antenna), Geometria e attenuazione (McKinley, bilancio di tratta), Calcolo dell'efficienza ora per ora (con la formula di DH9GCD), Attuazione sperimentale previsioni.
- **Documenti tecnici**: Fonti, Mappa dei radar europei, Efficienza - spiegazione.
- Sciami in diretta (GMN, CMOR), Sciami, Mappa quadrati da ADIF.

Fonte principale: C. Cerrotta IC8TEM, G. Sartori IV3GTH, "METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese".

## Installazione
Scaricare l'installatore dalla pagina **Releases** (vedi `LEGGIMI.txt`):
Windows `...-windows-x64-setup.exe` (C:\YA-MS; a 32 bit `...-windows-x86-setup.exe`), Linux `...-linux-x64.tar.gz` + `./installa.sh` (~/YA-MS),
Raspberry Pi `...-raspberry-pi-64bit.tar.gz` / `...-raspberry-pi-32bit.tar.gz` + `./installa.sh` (~/YA-MS),
Mac `...-mac-apple-silicon.dmg` / `...-mac-intel.dmg` (~/YA-MS).

## Compilazione
Gli installatori li produce GitHub Actions (`.github/workflows/build.yml`) a ogni aggiornamento del ramo `release` (versione dal file `VERSION`), che crea anche la Release `vX.Y.Z`.
In locale: `dotnet publish YA-MS.csproj -c Release -r win-x64|win-x86|linux-x64|linux-arm64|linux-arm|osx-arm64 --self-contained true`.
I documenti si rigenerano con `tools/build_spiegazione.py data` e `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

I dati dei radar appartengono ai rispettivi enti (Universita' di Lipsia / IAP Kuehlungsborn, Sodankyla Geophysical Observatory).
