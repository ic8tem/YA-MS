# YA-MS

**YA-MS** - previsione e calcolo in diretta dell'efficienza degli sciami meteorici per il meteor scatter (50-432 MHz).
A cura di Costantino Cerrotta IC8TEM. Windows, Linux, Raspberry Pi e Mac (.NET 8 + Avalonia).

- Volta celeste e pianta della tratta: radianti, Hot A / Hot B, lobo dell'antenna, zone PREV delle scie piu' probabili, sezione vista dall'antenna.
- Calcolo dell'efficienza ora per ora, con il confronto della formula di DH9GCD.
- Flusso dal radar SKiYMET di Collm e stima sperimentale a 50/144/432 MHz (regole SM6FHZ); confronto con RMOB.
- Geometria, attenuazione (McKinley) e bilancio di tratta; mappa dei quadrati da ADIF.

Fonte principale: C. Cerrotta IC8TEM, G. Sartori IV3GTH, "METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese".

## Installazione
Scaricare l'installatore dalla pagina **Releases** (vedi `LEGGIMI.txt`):
Windows `...-windows-x64-setup.exe` (C:\YA-MS), Linux `...-linux-x64.tar.gz` + `./installa.sh` (~/YA-MS),
Raspberry Pi `...-raspberry-pi-64bit.tar.gz` / `...-raspberry-pi-32bit.tar.gz` + `./installa.sh` (~/YA-MS),
Mac `...-mac-apple-silicon.dmg` / `...-mac-intel.dmg` (~/YA-MS).

## Compilazione
Gli installatori li produce GitHub Actions (`.github/workflows/build.yml`) a ogni aggiornamento del ramo `release` (versione dal file `VERSION`), che crea anche la Release `vX.Y.Z`.
In locale: `dotnet publish YA-MS.csproj -c Release -r win-x64|linux-x64|linux-arm64|linux-arm|osx-arm64 --self-contained true`.
I documenti si rigenerano con `tools/build_spiegazione.py data` e `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

I dati dei radar appartengono ai rispettivi enti (Universita' di Lipsia / IAP Kuehlungsborn, Sodankyla Geophysical Observatory).
