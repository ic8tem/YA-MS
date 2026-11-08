**English** · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh)

# Troubleshooting and FAQ

## Installation and start-up

### Windows SmartScreen says "Windows protected your PC"
The program is not signed with a commercial certificate. Click *More info* → *Run anyway*. Download it only from the [Releases](https://github.com/ic8tem/YA-MS/releases) page.

### macOS: cannot be opened because it is from an unidentified developer
YA-MS is not signed by Apple, so **Gatekeeper** blocks it the first time. In the `.dmg`, **right-click "Installa YA-MS.command" → Open** and confirm. The script removes the "downloaded from the internet" quarantine flag from `~/YA-MS/YA-MS.app` and opens it. If macOS still refuses, open *System Settings → Privacy & Security* and press *Open Anyway*.

### macOS: which .dmg?
`-mac-apple-silicon.dmg` for M1/M2/M3/M4 processors, `-mac-intel.dmg` for Intel Macs (Apple menu → *About This Mac* tells you which).

### Linux: YA-MS is not in the applications menu
Run `./installa.sh` from the extracted folder (not from `~/YA-MS`). Some desktops need a log-out/log-in to show new entries. You can always start it with `~/YA-MS/YA-MS`.

### The map of Europe is missing
*Map of Europe not available (network needed on first start).* The Natural Earth map is downloaded into `data/mappa` on the first start. Connect to the internet and restart YA-MS.

## Display

### Linux: Japanese text shows boxes
Your system lacks CJK fonts. Install the **Noto CJK** fonts and restart YA-MS:

| Distribution | Command |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Text is too small, or the charts have no room
Use the **Font** slider (100–300 %) and fold the rows with **Controls**. See [Settings](Settings-and-Data-Folder#font-and-controls).

### The screen is too bright at night
Choose **Night** or **Black** in the **Theme** list.

## Internet and radar data

### "No internet connection" message
YA-MS shows it **once** when no source can be reached; the status bar turns red. The program keeps working with the **last saved data** and retries by itself every 5 minutes; *Connection restored.* appears when the network is back. Nothing to do.

### Orange warning in Radar flux: "Cannot read the vertical flux scale …"
The Collm radar changes its vertical scale every day and YA-MS reads it from the chart labels. If a label cannot be read, the program uses the calibrated scale 0–1200 meteors/hour and warns that **values need checking**. Usually the next hourly chart is read correctly. If you see *Chart format changed* or *Flux axes not found in the expected position* for many hours, the radar has changed its chart format: please [report it](Contributing-and-Contacts).

### "The height chart scale has changed"
Height statistics (mode, mean, median) remain valid; only the absolute counts of the height histogram do not.

### "Radar flux: no data"
Press **Download now** in [Radar flux](Radar-Flux), and check that `data/fonti_radar.csv` has `attivo=1` for Collm.

### RMOB: why is the automatic download off?
RMOB asks **automatic programs not to fetch its files**. Enable *automatic download every 5 minutes* only after RMOB has given you permission. Meanwhile use **Download RMOB now** or **Load RMOB file from disk...**. See [Experimental forecasts](Experimental-Forecasts#rmob-and-automatic-programs).

### RMOB: "File format not recognised" or few hours read
Use the observer's monthly text file (`NAME_MMYYYYrmob.TXT`) or a bulletin table with a single observer. The exponent fit needs at least 3 hours in common with the Collm data (yesterday and today).

## Calculations

### "Invalid station locator" / "Invalid DX station locator"
Locators must have 4, 6 or 8 characters (e.g. `JN70`, `JN70CN`, `JN70CN12`).

### "No common E-layer zone"
The path is longer than twice the range at trail height (about 2 × 1062 km with the lobe at 0° and trails at 89.5 km): a single meteor-scatter hop cannot cover it. Raising the **Lobe elevation** shortens the range further.

### Hot A / Hot B are grey
They are already **inside your antenna lobe** when pointing at the DX: no need to turn. See [Sky dome](Sky-View#warnings).

### The efficiency differs from MCG_MS or MS-Soft
YA-MS uses the real path and its own model; the scale of OH5IY and MCG_MS is not documented in detail. Compare hours and trends rather than absolute percentages, and see the [model](Efficiency-Calculation#the-model).

### The GRAVES beam pass seems shifted
The beam sequence is computed from the PC clock: synchronise it with an NTP server. The GRAVES command station also shifts the sequence by a few steps at times; the detail is a prediction to be confirmed by listening.

## Other questions

**Is YA-MS free?** Yes, it is a free program for radio amateurs.

**Does it control my rotator or radio?** No. YA-MS is a forecasting and planning tool; use your digital-mode program (e.g. MSHV, WSJT-X) for the QSO.

**Does it work above 432 MHz?** The band list stops at 432 MHz (28, 50, 70, 144, 222, 432). The experimental forecast accepts any frequency from 28 to 1300 MHz, but the SM6FHZ rules it uses come from experience on 144 and 432 MHz.

**Something went wrong.** Write to the author with your operating system, the YA-MS version and what you did: see [Contributing and contacts](Contributing-and-Contacts).
