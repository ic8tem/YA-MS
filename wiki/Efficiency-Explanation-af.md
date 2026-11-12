[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · **Afrikaans** · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Verduideliking van die doeltreffendheidsberekening

*Oortjie: Tegniese dokumente › Verduideliking van die doeltreffendheidsberekening.*

[![Verduideliking van die doeltreffendheidsberekening](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

'n Tegniese dokument, *"Come YA-MS calcola l'efficienza di uno sciame"* (Hoe YA-MS die doeltreffendheid van 'n swerm bereken), wat binne die program as 'n ligte bladsy gewys word. Dit verduidelik **stap vir stap** hoe die doeltreffendheid verkry word, en sê vir elke stap **waar dit vandaan kom**. Die program wys dit **in die koppelvlaktaal** (al 36 tale), net soos die berekeningshandleiding; hierdie wiki gee die inhoud ook in [Berekening van doeltreffendheid](Efficiency-Calculation-af#die-model) en [Geometrie en padverlies](Geometry-and-Path-Loss-af).

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
| `data/spiegazione/efficienza_spiegazione_<code>.txt` / `.docx` | Dieselfde dokument in die ander 35 tale (bv. `_en`, `_de`, `_pt-br`) |
| `doc/YA-MS_manuale_calcoli.docx` | Die **berekeningshandleiding** (Italiaans): al die vergelykings (Word se vergelykingsredigeerder), genommer, met hul bronne |
| `doc/manuali/YA-MS_manuale_calcoli_<code>.docx` | Die berekeningshandleiding in die ander 35 tale |

Die twee dokumente word uit die bronkode hergenereer met `tools/build_spiegazione.py data [code]` en `node tools/build_manuale.js <file.docx> [code]`. Die vertalings is in `tools/traduzioni_doc/` (`tools/build_documenti.sh` hergenereer alle tale).
