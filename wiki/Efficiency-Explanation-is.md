**English** · [Русский](Efficiency-Explanation-ru) · [Deutsch](Efficiency-Explanation-de) · [日本語](Efficiency-Explanation-ja)

# Nýtni - skýringar

*Flipi: Tæknileg skjöl › Nýtni - skýringar.*

[![Nýtni - skýringar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Tæknilegt skjal, *"Come YA-MS calcola l'efficienza di uno sciame"* (Hvernig YA-MS reiknar nýtni drífu), sem birt er í forritinu sem ljós síða. Það skýrir **skref fyrir skref** hvernig nýtnin fæst og segir fyrir hvert skref **hvaðan það kemur**. Skjalið er sem stendur **á ítölsku**; þessi wiki gefur efni þess á íslensku í [Útreikningi nýtni](Efficiency-Calculation-is#líkanið) og [Rúmfræði og deyfingu](Geometry-and-Path-Loss-is).

## Merkingar

Hvert skref ber litaða merkingu:

| Merking | Litur | Merking hennar |
|---|---|---|
| **FONTE** (heimild) | blár | skrefið byggir á tilvitnaðri heimild; talan innan sviga vísar til listans í lokin |
| **RILIEVO** (prófun) | grænn | samanburður forritsins og heimildanna, með niðurstöðunni |
| **SCELTA** (val) | appelsínugulur | val forritsins, ekki tekið úr heimild: þarf að sannreyna með reynslu í loftinu |

## Kaflar

| Kafli | Innihald |
|---|---|
| 1. Inngangur | Tilgangur, merkingar, hvað nýtni þýðir (OH5IY, MCG_MS; YA-MS notar raunverulegu leiðina) |
| 2. Hvar endurvörpin verða: E-lagið | Slóðir í 80–120 km; hæð slóða = tíðasta gildi Collm-stuðlaritsins (prófun: 89,5 km þann 5/11/2026) |
| 3. Rúmfræði leiðarinnar | Jörðin og miðpunkturinn; hæðarhorn loftnets (formúla greinarinnar); sameiginlega svæðið og mörk þess; Hot A / Hot B; loftnetsgeisli (DL6WU, Kraus, W4RNL) |
| 4. Geislapunktur drífunnar | Staða geislapunktsins (IMO 2026/2027), dagsetning hámarks (IMO eða sólarlengd), virknisnið |
| 5. Endurvarpsskilyrðið | Speglunarendurvarp (McKinley), Gauss-vikmörk 0,05 rad, besta stefna (SM6FHZ), formúla DH9GCD |
| 6. Frá einum punkti að nýtninni | Endurvarpspunktar á 15 km fresti, vægi hvers punkts, prósenta; samanburður við QTFGUI (DJ5HG) |
| 7. Lestur niðurstaðnanna | Hlið A / B, leiðarstuðull, litir geislapunkta, PREV-svæði, snið séð frá loftnetinu |
| 8. Vinnutíðni og leiðardeyfing | Reglurnar λ³ / λ², frá ratsjá að amatörtíðnisviði, viðmiðanir um leiðardeyfingu |
| 9. Þekktar takmarkanir | Aðeins undirþéttar slóðir, stefnulaus loftnet, vinnugildi |
| 10. Heimildir | 17 tölusettar heimildir |

## Hnappar

| Hnappur | Hvað hann gerir |
|---|---|
| **Flytja út í Word (.docx)...** | Vistar afrit af `data/efficienza_spiegazione.docx` þar sem þú velur (tillaga að heiti *YA-MS - calcolo dell'efficienza.docx*) |
| **Opna í Word** | Opnar sömu `.docx`-skrá með sjálfgefnu forriti fyrir Word-skjöl (Word, LibreOffice, …) |

## Skrár

| Skrá | Innihald |
|---|---|
| `data/efficienza_spiegazione.txt` | Textinn sem sýndur er á flipanum, ein eining á hverri línu (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Word-útgáfan |
| `doc/YA-MS_manuale_calcoli.docx` | **Reiknihandbókin**: allar jöfnur (jöfnuritill Word), tölusettar, með heimildum sínum |

Skjölin tvö eru endurgerð úr frumkóðanum með `tools/build_spiegazione.py data` og `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
