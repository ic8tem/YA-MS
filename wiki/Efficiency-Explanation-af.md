**English** · [Русский](Efficiency-Explanation-ru) · [Deutsch](Efficiency-Explanation-de) · [日本語](Efficiency-Explanation-ja)

# Doeltreffendheid - verduideliking

*Oortjie: Tegniese dokumente › Doeltreffendheid - verduideliking.*

[![Doeltreffendheid - verduideliking](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

'n Tegniese dokument, *"Come YA-MS calcola l'efficienza di uno sciame"* (Hoe YA-MS die doeltreffendheid van 'n swerm bereken), wat binne die program as 'n ligte bladsy gewys word. Dit verduidelik **stap vir stap** hoe die doeltreffendheid verkry word, en sê vir elke stap **waar dit vandaan kom**. Die dokument is tans **in Italiaans**; hierdie wiki gee die inhoud in Afrikaans in [Berekening van doeltreffendheid](Efficiency-Calculation-af#die-model) en [Geometrie en padverlies](Geometry-and-Path-Loss-af).

## Etikette

Elke stap dra 'n gekleurde etiket:

| Etiket | Kleur | Betekenis |
|---|---|---|
| **FONTE** (bron) | blou | die stap neem 'n aangehaalde bron oor; die getal tussen hakies verwys na die lys aan die einde |
| **RILIEVO** (kontrole) | groen | vergelyking tussen die program en die bronne, met die resultaat |
| **SCELTA** (keuse) | oranje | 'n keuse van die program, nie uit 'n bron geneem nie: moet met ervaring op die lug nagegaan word |

## Hoofstukke

| Hoofstuk | Inhoud |
|---|---|
| 1. Inleiding | Doel, etikette, wat doeltreffendheid beteken (OH5IY, MCG_MS; YA-MS gebruik die werklike pad) |
| 2. Waar refleksies plaasvind: die E-laag | Spore op 80–120 km; spoorhoogte = modus van die Collm-histogram (kontrole: 89,5 km op 5/11/2026) |
| 3. Padgeometrie | Aarde en middelpunt; antenna-elevasie (formule uit die artikel); gemeenskaplike sone en sy grense; Hot A / Hot B; antennalob (DL6WU, Kraus, W4RNL) |
| 4. Die radiant van die swerm | Radiantposisie (IMO 2026/2027), datum van die maksimum (IMO of sonlengte), aktiwiteitsprofiel |
| 5. Refleksievoorwaarde | Spekulêre refleksie (McKinley), Gaussiese toleransie 0,05 rad, beste rigting (SM6FHZ), DH9GCD-formule |
| 6. Van een punt na die doeltreffendheid | Refleksiepunte elke 15 km, gewig van elke punt, persentasie; vergelyking met QTFGUI (DJ5HG) |
| 7. Die resultate lees | Kant A / B, padindeks, radiantkleure, PREV-sones, deursnee soos vanaf die antenna gesien |
| 8. Werkfrekwensie en padverlies | λ³- / λ²-reëls, van radar na amateurband, verwysings vir padverlies |
| 9. Bekende beperkings | Slegs onderdigte spore, isotropiese antennas, werkwaardes |
| 10. Bronne | 17 genommerde bronne |

## Knoppies

| Knoppie | Wat dit doen |
|---|---|
| **Voer na Word uit (.docx)...** | Stoor 'n kopie van `data/efficienza_spiegazione.docx` waar jy kies (voorgestelde naam *YA-MS - calcolo dell'efficienza.docx*) |
| **Open in Word** | Open dieselfde `.docx` met die verstekprogram vir Word-dokumente (Word, LibreOffice, …) |

## Lêers

| Lêer | Inhoud |
|---|---|
| `data/efficienza_spiegazione.txt` | Die teks wat in die oortjie gewys word, een blok per reël (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Die Word-weergawe |
| `doc/YA-MS_manuale_calcoli.docx` | Die **berekeningshandleiding**: al die vergelykings (Word se vergelykingsredigeerder), genommer, met hul bronne |

Die twee dokumente word uit die bronkode hergenereer met `tools/build_spiegazione.py data` en `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
