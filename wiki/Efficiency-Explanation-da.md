[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-BR) · **Dansk** · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-TW)

# Effektivitet - forklaring

*Fane: Tekniske dokumenter › Effektivitet - forklaring.*

[![Effektivitet - forklaring](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Et teknisk dokument, *"Come YA-MS calcola l'efficienza di uno sciame"* (Sådan beregner YA-MS en sværms effektivitet), vist i programmet som en lys side. Det forklarer **trin for trin**, hvordan effektiviteten fremkommer, og angiver for hvert trin, **hvor det stammer fra**. Dokumentet findes i øjeblikket **på italiensk**; denne wiki gengiver indholdet på dansk i [Effektivitetsberegning](Efficiency-Calculation-da#modellen) og [Geometri og dæmpning](Geometry-and-Path-Loss-da).

## Mærkater

Hvert trin har en farvet mærkat:

| Mærkat | Farve | Betydning |
|---|---|---|
| **FONTE** (kilde) | blå | trinnet bygger på en citeret kilde; tallet i parentes henviser til listen til sidst |
| **RILIEVO** (kontrol) | grøn | sammenligning mellem programmet og kilderne med resultatet |
| **SCELTA** (valg) | orange | et valg truffet af programmet, ikke taget fra en kilde: skal kontrolleres med erfaringen på båndet |

## Kapitler

| Kapitel | Indhold |
|---|---|
| 1. Indledning | Formål, mærkater, hvad effektivitet betyder (OH5IY, MCG_MS; YA-MS bruger den faktiske strækning) |
| 2. Hvor refleksionerne sker: E-laget | Spor i 80–120 km højde; sporhøjde = typetallet i Collm-histogrammet (kontrol: 89,5 km den 5.11.2026) |
| 3. Strækningens geometri | Jorden og midtpunktet; antenneelevation (artiklens formel); den fælles zone og dens grænser; Hot A / Hot B; antennelap (DL6WU, Kraus, W4RNL) |
| 4. Sværmens radiant | Radiantens position (IMO 2026/2027), dato for maksimum (IMO eller solens længde), aktivitetsprofil |
| 5. Refleksionsbetingelsen | Spejlende refleksion (McKinley), gaussisk tolerance 0,05 rad, bedste retning (SM6FHZ), DH9GCD-formlen |
| 6. Fra ét punkt til effektiviteten | Refleksionspunkter for hver 15 km, hvert punkts vægt, procent; sammenligning med QTFGUI (DJ5HG) |
| 7. Aflæsning af resultaterne | Side A / B, strækningsindeks, radianternes farver, PREV-zoner, snit set fra antennen |
| 8. Arbejdsfrekvens og strækningsdæmpning | λ³- / λ²-reglerne, fra radar til amatørbånd, referencer for strækningsdæmpning |
| 9. Kendte begrænsninger | Kun underdense spor, isotrope antenner, arbejdsværdier |
| 10. Kilder | 17 nummererede kilder |

## Knapper

| Knap | Hvad den gør |
|---|---|
| **Eksportér til Word (.docx)...** | Gemmer en kopi af `data/efficienza_spiegazione.docx`, hvor du vælger (foreslået navn *YA-MS - calcolo dell'efficienza.docx*) |
| **Åbn i Word** | Åbner samme `.docx` med standardprogrammet for Word-dokumenter (Word, LibreOffice, …) |

## Filer

| Fil | Indhold |
|---|---|
| `data/efficienza_spiegazione.txt` | Teksten, der vises i fanen, én blok pr. linje (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Word-udgaven |
| `doc/YA-MS_manuale_calcoli.docx` | **Beregningsmanualen**: alle ligninger (Words ligningseditor), nummereret, med kilder |

De to dokumenter genereres fra kildekoden med `tools/build_spiegazione.py data` og `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
