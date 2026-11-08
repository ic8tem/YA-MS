**English** · [Русский](Efficiency-Explanation-ru) · [Deutsch](Efficiency-Explanation-de) · [日本語](Efficiency-Explanation-ja)

# Effektivitet - förklaring

*Flik: Tekniska dokument › Effektivitet - förklaring.*

[![Effektivitet - förklaring](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Ett tekniskt dokument, *"Come YA-MS calcola l'efficienza di uno sciame"* (Hur YA-MS beräknar en svärms effektivitet), som visas i programmet som en ljus sida. Det förklarar **steg för steg** hur effektiviteten tas fram och anger för varje steg **var det kommer ifrån**. Dokumentet finns för närvarande **på italienska**; den här wikin återger dess innehåll på svenska i [Effektivitetsberäkning](Efficiency-Calculation-sv#modellen) och [Geometri och dämpning](Geometry-and-Path-Loss-sv).

## Etiketter

Varje steg har en färgad etikett:

| Etikett | Färg | Betydelse |
|---|---|---|
| **FONTE** (källa) | blå | steget bygger på en citerad källa; siffran inom parentes hänvisar till listan i slutet |
| **RILIEVO** (kontroll) | grön | jämförelse mellan programmet och källorna, med resultatet |
| **SCELTA** (val) | orange | ett val gjort av programmet, inte hämtat från en källa: ska kontrolleras mot erfarenheten i luften |

## Kapitel

| Kapitel | Innehåll |
|---|---|
| 1. Inledning | Syfte, etiketter, vad effektivitet betyder (OH5IY, MCG_MS; YA-MS använder den verkliga sträckan) |
| 2. Var reflexerna sker: E-skiktet | Spår på 80–120 km; spårhöjd = typvärdet i Collm-histogrammet (kontroll: 89,5 km den 5/11/2026) |
| 3. Sträckans geometri | Jorden och mittpunkten; antennelevation (artikelns formel); den gemensamma zonen och dess gränser; Hot A / Hot B; antennlob (DL6WU, Kraus, W4RNL) |
| 4. Svärmens radiant | Radiantens läge (IMO 2026/2027), datum för maximum (IMO eller solens longitud), aktivitetsprofil |
| 5. Reflexionsvillkoret | Spegelreflexion (McKinley), gaussisk tolerans 0,05 rad, bästa riktning (SM6FHZ), DH9GCD-formeln |
| 6. Från en punkt till effektiviteten | Reflexionspunkter var 15:e km, varje punkts vikt, procent; jämförelse med QTFGUI (DJ5HG) |
| 7. Läsa resultaten | Sida A / B, sträckindex, radianternas färger, PREV-zoner, tvärsnitt sett från antennen |
| 8. Arbetsfrekvens och sträckdämpning | Reglerna λ³ / λ², från radar till amatörband, referenser för sträckdämpning |
| 9. Kända begränsningar | Endast underdensa spår, isotropa antenner, arbetsvärden |
| 10. Källor | 17 numrerade källor |

## Knappar

| Knapp | Vad den gör |
|---|---|
| **Exportera till Word (.docx)...** | Sparar en kopia av `data/efficienza_spiegazione.docx` där du väljer (föreslaget namn *YA-MS - calcolo dell'efficienza.docx*) |
| **Öppna i Word** | Öppnar samma `.docx` med standardprogrammet för Word-dokument (Word, LibreOffice, …) |

## Filer

| Fil | Innehåll |
|---|---|
| `data/efficienza_spiegazione.txt` | Texten som visas i fliken, ett block per rad (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Word-versionen |
| `doc/YA-MS_manuale_calcoli.docx` | **Beräkningshandboken**: alla ekvationer (Words ekvationsredigerare), numrerade, med sina källor |

De två dokumenten genereras på nytt från källkoden med `tools/build_spiegazione.py data` och `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
