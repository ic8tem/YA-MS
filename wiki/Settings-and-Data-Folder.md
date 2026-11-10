**English** · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Română](Settings-and-Data-Folder-ro) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh)

# Settings and data folder

## The tab bar

At the right end of the tab bar, from right to left:

| Control | What it does |
|---|---|
| **Language** (list) | Interface language; see [Language](#language) |
| **Theme** (list) | Colour scheme; see [Colour schemes](#colour-schemes) |
| **Controls ▴ / ▾** | Folds or unfolds the three rows of controls above the tabs; see [Font and Controls](#font-and-controls) |

Changing language or theme saves the settings and **rebuilds the window** in the same position and size, on the same tab: no restart is needed.

## Language

Six interface languages:

| Language | Code | File |
|---|---|---|
| Italiano | `it` | none: Italian is the base language (the keys) |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

At the first start YA-MS uses the **system language** if it is one of these, otherwise Italian. Numbers and dates follow the chosen language (e.g. decimal point in English, comma in Italian and German). Any text missing from a translation file is shown in Italian. On Linux, Japanese needs suitable fonts: see [Troubleshooting](Troubleshooting-FAQ#linux-japanese-text-shows-boxes).

The [Efficiency - explanation](Efficiency-Explanation) document and the calculation manual are in Italian.

## Colour schemes

The **Theme** list offers 12 schemes, the same as the author's EME program YAEC plus the original YA-MS palette:

| Scheme | Description |
|---|---|
| **Light** | default |
| **Night** | dark blue tones, for use at night |
| **Black** | black background, for the dark and for OLED screens |
| Pastel light blue · Pastel orange · Pastel aquamarine · Pastel green · Pastel pink · Pastel lilac · Pastel indigo · Pastel brown | eight light pastel schemes |
| **Meteor trail** | the original YA-MS style (up to version 1.2.0): night violet with light blue, violet, light green, yellow and orange |

The scheme applies to all tabs and is saved in `config.ini` (key `tema`).

## Font and Controls

- **Font** (end of the first row of controls): enlarges **all the text** from **100 to 300 %** in 10 % steps; lines, circles and maps keep their size. With large fonts the tabs wrap onto a second line and the cards grow.
- **Controls**: with large fonts or a small screen, fold the three rows of controls to leave room for maps and charts. The state is remembered.

## Data folder

All data and settings are in a single **`data`** folder **next to the program** – no AppData, no system folders:

| System | Program | Data |
|---|---|---|
| Windows (installer) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (portable) | wherever you extracted it | `data` next to `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (next to the app) |

At start-up the program creates the folder if needed and copies only the **missing** starting files: files you have changed are never overwritten. Translation files in `data/lingue` are program files and are replaced when the new version's files are more recent.

### Files you can edit

| File | Content |
|---|---|
| `sciami.csv` | Shower catalogue (IMO values and working values); see [Showers](Showers#editing-the-catalogue) |
| `massimi_imo.csv` | Peak dates and times published by the IMO (2026, 2027): **add new years** here |
| `ant_radiante.csv` | Position of the Antihelion Source (IMO table 6) |
| `fonti_radar.csv` | Radar addresses; `attivo=1` downloads, `0` ignores |
| `regole_sperimentali.csv` | Constants and rules used, each with its source (reference) |
| `lingue/<code>.txt` | Interface translations; see [Contributing](Contributing-and-Contacts#translations) |
| `config.ini` | Settings (see below) |

### Files created by the program

| File / folder | Content |
|---|---|
| `config.ini` | Settings |
| `flusso_collm.csv` | Hourly archive of the Collm flux |
| `quote_collm.csv` | Archive of the trail heights |
| `radar/` | Latest radar images and RMOB files |
| `mappa/` | Natural Earth coastlines and borders (downloaded on the first start) |
| `adif_quadrati.csv` | Squares from the last ADIF loaded |
| `efficienza_spiegazione.txt`, `.docx` | The [explanation document](Efficiency-Explanation) |

## config.ini

Plain text, one `key=value` per line (lines starting with `#` or `;` are comments). The program writes it when it closes, so **edit it with YA-MS closed**. The keys you may want to know:

| Key | Default | Meaning |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Your locator and height (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | DX station locator and height (m) |
| `banda_MHz` | 144 | Band (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Trail height (km); 1 = use the Collm mode |
| `elevazione_lobo_gradi` | 0 | Lobe elevation (°) |
| `boom_m` | 4.6 | Yagi boom length (m) |
| `hot_spot_km` | 150 | Hot A / Hot B distance from the midpoint (30–400 km) |
| `lingua` | system / `it` | Language code (`it`, `en`, `ru`, `ja`, `de`, `nl`) |
| `tema` | `chiaro` | Colour scheme: `chiaro` (Light), `scuro` (Night), `nero` (Black), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Meteor trail) |
| `carattere_pct` | 100 | Font size (100–300 %) |
| `comandi_visibili` | 1 | 1 = rows of controls shown, 0 = folded |
| `mostra_mappa`, `vista_alto` | 1, 1 | Map of Europe, top view in the Sky dome |
| `aggiornamento_automatico` | 1 | Automatic check of the sources every 5 minutes |
| `esponente_lambda` | 3 | λ exponent in the Radar flux tab |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Link budget inputs |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Experimental forecast: frequency, k, K |
| `rmob_osservatore` | empty | RMOB observer name |
| `rmob_automatico` | 0 | Automatic RMOB download (enable only with RMOB's permission) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | RMOB address template |
| `graves_sequenza` | 0 | GRAVES beam sequence: 0 = 0.8 s (2021), 1 = 3.2 s (2007) |

## Privacy

YA-MS collects no data and shows no advertising. It connects to the internet only to download public data: the Collm and Sodankylä radar images, the Natural Earth map (first start) and, if you ask for it, an RMOB file.
