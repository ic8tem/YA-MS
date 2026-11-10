**English** · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-BR) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Ελληνικά](Grid-Square-Map-el) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [ไทย](Grid-Square-Map-th) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh) · [中文 (繁體)](Grid-Square-Map-zh-TW)

# Grid square map

*Tab: Grid square map.*

[![Grid square map](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

The Maidenhead squares (4 characters) you have **worked** and **confirmed**, read from the ADIF file of your log, on a map of Europe – **one sub-tab per band: 50, 70, 144, 222 and 432 MHz**.

## Controls

| Control | What it does |
|---|---|
| **Load ADIF file...** | Reads an `.adi` / `.adif` file. A new ADIF **replaces** the previous data. |
| **Clear memory** | Deletes all the squares loaded from ADIF (asks for confirmation). |
| Mouse | **Wheel = zoom, drag = pan, mouse over a square = QSOs** (up to six callsigns with date, *(confirmed)* when confirmed) |

After loading, the status shows *… QSOs read, … QSO squares in the 50-432 MHz bands, … QSOs discarded (other bands or no square)*. Each band map has the caption *… squares worked, … confirmed*.

| Colour | Meaning |
|---|---|
| Orange | worked |
| Green | confirmed (QSL or LoTW) |

## How the ADIF is read

- Fields used: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF specification).
- Band from `BAND`, or from the frequency: 50–54 MHz = 6 m, 69.9–71.5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1.25 m, 420–450 MHz = 70 cm.
- A square is **confirmed** if at least one QSO in it has `QSL_RCVD = Y` or `LOTW_QSL_RCVD = Y`.
- The squares are kept in `data/adif_quadrati.csv` until you load another file or press **Clear memory**.

YA-MS does **not** connect to LoTW: export the ADIF from your logging program (or from LoTW) and load it here.
