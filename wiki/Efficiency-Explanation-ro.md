[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · **Română** · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Explicația calculului eficienței

*Filă: Documente tehnice › Explicația calculului eficienței.*

[![Explicația calculului eficienței](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Un document tehnic, *"Come YA-MS calcola l'efficienza di uno sciame"* (Cum calculează YA-MS eficiența unui roi), afișat în program ca o pagină luminoasă. Explică **pas cu pas** cum se obține eficiența și spune pentru fiecare pas **de unde provine**. Programul îl afișează **în limba interfeței** (toate cele 36 de limbi), la fel ca manualul de calcul; acest wiki îi prezintă conținutul și în [Calculul eficienței](Efficiency-Calculation-ro#modelul) și [Geometrie și atenuare pe traseu](Geometry-and-Path-Loss-ro).

## Etichete

Fiecare pas poartă o etichetă colorată:

| Etichetă | Culoare | Semnificație |
|---|---|---|
| **FONTE** (sursă) | albastru | pasul preia o sursă citată; numărul dintre paranteze se referă la lista de la final |
| **RILIEVO** (verificare) | verde | comparație între program și surse, cu rezultatul |
| **SCELTA** (alegere) | portocaliu | o alegere a programului, nepreluată dintr-o sursă: de verificat cu experiența din eter |

## Capitole

| Capitol | Conținut |
|---|---|
| 1. Introducere | Scopul, etichetele, ce înseamnă eficiența (OH5IY, MCG_MS; YA-MS folosește traseul real) |
| 2. Unde au loc reflexiile: stratul E | Urme la 80–120 km; înălțimea urmei = moda histogramei Collm (verificare: 89,5 km pe 5/11/2026) |
| 3. Geometria traseului | Pământul și punctul median; elevația antenei (formula articolului); zona comună și limitele sale; Hot A / Hot B; lobul antenei (DL6WU, Kraus, W4RNL) |
| 4. Radiantul roiului | Poziția radiantului (IMO 2026/2027), data maximului (IMO sau longitudinea solară), profilul de activitate |
| 5. Condiția de reflexie | Reflexia speculară (McKinley), toleranța gaussiană 0,05 rad, direcția optimă (SM6FHZ), formula DH9GCD |
| 6. De la un punct la eficiență | Puncte de reflexie la fiecare 15 km, ponderea fiecărui punct, procentul; comparația cu QTFGUI (DJ5HG) |
| 7. Citirea rezultatelor | Latura A / B, indicele traseului, culorile radianților, zonele PREV, secțiunea văzută de la antenă |
| 8. Frecvența de lucru și atenuarea pe traseu | Regulile λ³ / λ², de la radar la banda de radioamatori, referințe pentru atenuarea pe traseu |
| 9. Limite cunoscute | Doar urme subdense, antene izotrope (în azimut; diagramă verticală opțională), valori de lucru |
| 10. Surse | 17 surse numerotate |

## Butoane

| Buton | Ce face |
|---|---|
| **Exportă în Word (.docx)...** | Salvează o copie a `data/efficienza_spiegazione.docx` unde alegeți (nume sugerat *YA-MS - calcolo dell'efficienza.docx*) |
| **Deschide în Word** | Deschide același `.docx` cu programul implicit pentru documente Word (Word, LibreOffice, …) |

## Fișiere

| Fișier | Conținut |
|---|---|
| `data/efficienza_spiegazione.txt` | Textul afișat în filă, câte un bloc pe linie (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Versiunea Word |
| `data/spiegazione/efficienza_spiegazione_<code>.txt` / `.docx` | Același document în celelalte 35 de limbi (de ex. `_en`, `_de`, `_pt-br`) |
| `doc/YA-MS_manuale_calcoli.docx` | **Manualul de calcul** (în italiană): toate ecuațiile (editorul de ecuații Word), numerotate, cu sursele lor |
| `doc/manuali/YA-MS_manuale_calcoli_<code>.docx` | Manualul de calcul în celelalte 35 de limbi |

Cele două documente sunt regenerate din sursă cu `tools/build_spiegazione.py data [code]` și `node tools/build_manuale.js <file.docx> [code]`; traducerile se află în `tools/traduzioni_doc/` (`tools/build_documenti.sh` reconstruiește toate limbile).
