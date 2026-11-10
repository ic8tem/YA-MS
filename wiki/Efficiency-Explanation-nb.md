[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · **Norsk** · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Effektivitet - forklaring

*Fane: Tekniske dokumenter › Effektivitet - forklaring.*

[![Effektivitet - forklaring](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Et teknisk dokument, *"Come YA-MS calcola l'efficienza di uno sciame"* (Slik beregner YA-MS effektiviteten til en sverm), vist i programmet som en lys side. Det forklarer **trinn for trinn** hvordan effektiviteten kommer fram, og sier for hvert trinn **hvor det kommer fra**. Dokumentet finnes foreløpig **på italiensk**; denne wikien gjengir innholdet på norsk i [Effektivitetsberegning](Efficiency-Calculation-nb#modellen) og [Geometri og demping](Geometry-and-Path-Loss-nb).

## Merkelapper

Hvert trinn har en farget merkelapp:

| Merkelapp | Farge | Betydning |
|---|---|---|
| **FONTE** (kilde) | blå | trinnet bygger på en sitert kilde; tallet i parentes viser til listen til slutt |
| **RILIEVO** (kontroll) | grønn | sammenligning mellom programmet og kildene, med resultatet |
| **SCELTA** (valg) | oransje | et valg gjort av programmet, ikke hentet fra en kilde: må kontrolleres med erfaring på båndet |

## Kapitler

| Kapittel | Innhold |
|---|---|
| 1. Innledning | Formål, merkelapper, hva effektivitet betyr (OH5IY, MCG_MS; YA-MS bruker den faktiske strekningen) |
| 2. Hvor refleksjonene skjer: E-laget | Spor i 80–120 km høyde; sporhøyde = typetallet i Collm-histogrammet (kontroll: 89,5 km den 5.11.2026) |
| 3. Strekningsgeometri | Jorda og midtpunktet; antenneelevasjon (artikkelens formel); fellessonen og grensene; Hot A / Hot B; antennelobe (DL6WU, Kraus, W4RNL) |
| 4. Svermens radiant | Radiantens posisjon (IMO 2026/2027), dato for maksimum (IMO eller solens lengde), aktivitetsprofil |
| 5. Refleksjonsbetingelsen | Speilrefleksjon (McKinley), gaussisk toleranse 0,05 rad, beste retning (SM6FHZ), DH9GCD-formelen |
| 6. Fra ett punkt til effektiviteten | Refleksjonspunkter for hver 15 km, vekten til hvert punkt, prosent; sammenligning med QTFGUI (DJ5HG) |
| 7. Tolkning av resultatene | Side A / B, strekningsindeks, radiantfarger, PREV-soner, snitt sett fra antennen |
| 8. Arbeidsfrekvens og strekningsdemping | λ³- / λ²-reglene, fra radar til amatørbånd, referanser for strekningsdemping |
| 9. Kjente begrensninger | Bare underdense spor, isotrope antenner, arbeidsverdier |
| 10. Kilder | 17 nummererte kilder |

## Knapper

| Knapp | Hva den gjør |
|---|---|
| **Eksporter til Word (.docx)...** | Lagrer en kopi av `data/efficienza_spiegazione.docx` der du velger (foreslått navn *YA-MS - calcolo dell'efficienza.docx*) |
| **Åpne i Word** | Åpner samme `.docx` med standardprogrammet for Word-dokumenter (Word, LibreOffice, …) |

## Filer

| Fil | Innhold |
|---|---|
| `data/efficienza_spiegazione.txt` | Teksten som vises i fanen, én blokk per linje (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Word-versjonen |
| `doc/YA-MS_manuale_calcoli.docx` | **Beregningshåndboken**: alle likninger (Words formelredigering), nummerert, med kilder |

De to dokumentene genereres på nytt fra kildekoden med `tools/build_spiegazione.py data` og `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
