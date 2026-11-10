**English** · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [ไทย](Efficiency-Explanation-th) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Efficiency - explanation

*Tab: Technical documents › Efficiency - explanation.*

[![Efficiency - explanation](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

A technical document, *"Come YA-MS calcola l'efficienza di uno sciame"* (How YA-MS computes the efficiency of a shower), shown inside the program as a light page. It explains **step by step** how the efficiency is obtained, and says for each step **where it comes from**. The document is currently **in Italian**; this wiki gives its content in English in [Efficiency calculation](Efficiency-Calculation#the-model) and [Geometry and path loss](Geometry-and-Path-Loss).

## Labels

Every step carries a coloured label:

| Label | Colour | Meaning |
|---|---|---|
| **FONTE** (source) | blue | the step takes up a cited source; the number in brackets refers to the list at the end |
| **RILIEVO** (check) | green | comparison between the program and the sources, with the result |
| **SCELTA** (choice) | orange | a choice of the program, not taken from a source: to be checked with experience on the air |

## Chapters

| Chapter | Content |
|---|---|
| 1. Introduction | Purpose, labels, what efficiency means (OH5IY, MCG_MS; YA-MS uses the real path) |
| 2. Where reflections happen: the E layer | Trails at 80–120 km; trail height = mode of the Collm histogram (check: 89.5 km on 5/11/2026) |
| 3. Path geometry | Earth and midpoint; antenna elevation (article formula); common zone and its limits; Hot A / Hot B; antenna lobe (DL6WU, Kraus, W4RNL) |
| 4. The shower radiant | Radiant position (IMO 2026/2027), peak date (IMO or solar longitude), activity profile |
| 5. Reflection condition | Specular reflection (McKinley), Gaussian tolerance 0.05 rad, best heading (SM6FHZ), DH9GCD formula |
| 6. From one point to the efficiency | Reflection points every 15 km, weight of each point, percentage; comparison with QTFGUI (DJ5HG) |
| 7. Reading the results | Side A / B, path index, radiant colours, PREV zones, section seen from the antenna |
| 8. Working frequency and path loss | λ³ / λ² rules, from radar to amateur band, path loss references |
| 9. Known limits | Underdense trails only, isotropic antennas, working values |
| 10. Sources | 17 numbered sources |

## Buttons

| Button | What it does |
|---|---|
| **Export to Word (.docx)...** | Saves a copy of `data/efficienza_spiegazione.docx` where you choose (suggested name *YA-MS - calcolo dell'efficienza.docx*) |
| **Open in Word** | Opens the same `.docx` with the default program for Word documents (Word, LibreOffice, …) |

## Files

| File | Content |
|---|---|
| `data/efficienza_spiegazione.txt` | The text shown in the tab, one block per line (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | The Word version |
| `doc/YA-MS_manuale_calcoli.docx` | The **calculation manual**: all equations (Word equation editor), numbered, with their sources |

The two documents are regenerated from the source with `tools/build_spiegazione.py data` and `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
