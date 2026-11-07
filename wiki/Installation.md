**English** · [Русский](Installation-ru) · [Deutsch](Installation-de) · [日本語](Installation-ja)

# Installation

All packages are on the **[Releases](https://github.com/ic8tem/YA-MS/releases)** page (in the file names below `x.y.z` is the version, e.g. `1.2.0`). Nothing needs compiling and nothing else needs installing: each package contains the .NET 8 runtime.

| System | File | Installs into |
|---|---|---|
| Windows (64-bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (installer) | `C:\YA-MS` |
| Windows (64-bit), portable | `YA-MS-x.y.z-windows-x64-portatile.zip` | any folder where you can write |
| Linux (64-bit) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**The program and its `data` folder always stay together** in the YA-MS folder: all data and settings are there (no AppData, no system folders). See [Settings and data folder](Settings-and-Data-Folder).

## Windows

### Installer
1. Download `YA-MS-x.y.z-windows-x64-setup.exe` and run it.
2. If **SmartScreen** shows "Windows protected your PC": *More info* → *Run anyway* (the program is not signed with a commercial certificate).
3. YA-MS is installed into **`C:\YA-MS`**, **without administrator rights**, with a Start menu icon and, if you tick it, a desktop icon.

### Portable
Extract `YA-MS-x.y.z-windows-x64-portatile.zip` wherever you like (a folder where you can write, not *Program Files*) and run `YA-MS.exe`. You can copy the whole folder to a USB stick or another computer.

## Linux

1. Extract `YA-MS-x.y.z-linux-x64.tar.gz`.
2. From the extracted folder run:
   ```sh
   ./installa.sh
   ```
3. The script copies YA-MS into **`~/YA-MS`** (no root needed) and adds **YA-MS** to the applications menu (category *HamRadio*). You can also start it with `~/YA-MS/YA-MS`.

For Japanese text you may need the Noto CJK fonts: see [Troubleshooting](Troubleshooting-FAQ#linux-japanese-text-shows-boxes).

## macOS

1. Choose the right file: `-mac-apple-silicon.dmg` for M1/M2/M3/M4 processors, `-mac-intel.dmg` for Intel Macs.
2. Open the `.dmg`, **right-click "Installa YA-MS.command" → Open** and confirm.
3. The script copies `YA-MS.app` into **`~/YA-MS`** and opens it.

The program is not signed by Apple, so the first time macOS asks for confirmation; see [Troubleshooting](Troubleshooting-FAQ#macos-cannot-be-opened-because-it-is-from-an-unidentified-developer).

## First start

- The **map of Europe** (Natural Earth coastlines and borders) is downloaded automatically into `data/mappa` the first time: an internet connection is needed once.
- The **radar data** (Collm, Sodankylä) are downloaded at once and then checked every 5 minutes.
- The interface starts in your system language if it is one of the six available, otherwise in Italian; change it at the top right (see [Settings](Settings-and-Data-Folder#language)).

## Updating

Install the new version **over the old one** (same installer, same folder). Settings (`config.ini`), the flux archives and the map stay in `data`. Translation files in `data/lingue` are replaced when the new ones are more recent.

## Building from source (developers only)

The installers are produced by GitHub Actions (`.github/workflows/build.yml`) at every update of the `release` branch (version taken from the `VERSION` file), which also creates the release `vX.Y.Z`. Locally:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, osx-arm64
```

The documents are regenerated with `tools/build_spiegazione.py data` and `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Next: [Getting started](Getting-Started).
