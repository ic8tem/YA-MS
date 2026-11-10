**English** · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh)

# Installation

All packages are on the **[Releases](https://github.com/ic8tem/YA-MS/releases)** page (in the file names below `x.y.z` is the version, e.g. `1.2.0`). Nothing needs compiling and nothing else needs installing: each package contains the .NET 8 runtime.

| System | File | Installs into |
|---|---|---|
| Windows (64-bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (installer) | `C:\YA-MS` |
| Windows (64-bit), portable | `YA-MS-x.y.z-windows-x64-portatile.zip` | any folder where you can write |
| Windows (32-bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` or `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-bit): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (copied there at the first start) |
| Linux (64-bit), any distribution | `YA-MS-x.y.z-linux-x64.tar.gz` (portable or with `./installa.sh`) | `~/YA-MS` or any folder |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian package | `ya-ms_x.y.z_arm64.deb` (64-bit) or `ya-ms_x.y.z_armhf.deb` (32-bit) | `~/YA-MS` (copied there at the first start) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, application only | `YA-MS-x.y.z-mac-apple-silicon-app.zip` or `...-mac-intel-app.zip` | the folder where you extract `YA-MS.app` |

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

### Debian package (.deb)
On Debian, Ubuntu, Mint and Raspberry Pi OS you can instead install `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` on the Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
The package puts the program in `/opt/ya-ms` and adds **YA-MS** to the menu. At the first start (and after each new version) it copies itself into **`~/YA-MS`** and runs from there, so the `data` folder stays next to the program and your settings are kept.

### Portable
The `.tar.gz` also works without installing: extract it anywhere you can write and run `./YA-MS` from that folder.

For Japanese text you may need the Noto CJK fonts: see [Troubleshooting](Troubleshooting-FAQ#linux-japanese-text-shows-boxes).

## Raspberry Pi

Same procedure as Linux: extract `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (or `-32bit` on Raspberry Pi OS 32-bit) and run `./installa.sh` from the extracted folder.

- To see which system you have, type `uname -m` in a terminal: `aarch64` → 64-bit package, `armv7l` → 32-bit package.
- Supported: Raspberry Pi 2 (32-bit only), 3, 4, 5, 400 and 500, with the desktop version of Raspberry Pi OS. **Not supported:** Pi Zero / Zero W and Pi 1 (ARMv6 processor, .NET does not run there); Pi Zero 2 W works with the 64-bit package but 512 MB of RAM is tight.
- A Pi 4 or 5 with at least 2 GB of RAM is recommended; the first start takes a few seconds longer than on a PC.

## macOS

1. Choose the right file: `-mac-apple-silicon.dmg` for M1/M2/M3/M4 processors, `-mac-intel.dmg` for Intel Macs.
2. Open the `.dmg`, **right-click "Installa YA-MS.command" → Open** and confirm.
3. The script copies `YA-MS.app` into **`~/YA-MS`** and opens it.

Alternatively, `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` contains only `YA-MS.app`: extract it into a folder of your choice (where you can write); the `data` folder is created next to `YA-MS.app`. The first time, right-click → **Open**.

The program is not signed by Apple, so the first time macOS asks for confirmation; see [Troubleshooting](Troubleshooting-FAQ#macos-cannot-be-opened-because-it-is-from-an-unidentified-developer).

## First start

- The **map of Europe** (Natural Earth coastlines and borders) is downloaded automatically into `data/mappa` the first time: an internet connection is needed once.
- The **radar data** (Collm, Sodankylä) are downloaded at once and then checked every 5 minutes.
- The interface starts in your system language if it is one of the 28 available, otherwise in Italian; change it at the top right (see [Settings](Settings-and-Data-Folder#language)).

## Updating

Install the new version **over the old one** (same installer, same folder). Settings (`config.ini`), the flux archives and the map stay in `data`. Translation files in `data/lingue` are replaced when the new ones are more recent.

## Building from source (developers only)

The installers are produced by GitHub Actions (`.github/workflows/build.yml`) at every update of the `release` branch (version taken from the `VERSION` file), which also creates the release `vX.Y.Z`. Locally:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

The documents are regenerated with `tools/build_spiegazione.py data` and `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Next: [Getting started](Getting-Started).
