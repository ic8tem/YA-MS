[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · **Română** · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Eficiență - explicație

*Fila: Documente tehnice › Eficiență - explicație.*

[![Eficiență - explicație](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Un document tehnic, *„Come YA-MS calcola l'efficienza di uno sciame”* (Cum calculează YA-MS eficiența unui roi), afișat în program ca o pagină deschisă la culoare. Explică **pas cu pas** cum se obține eficiența și spune pentru fiecare pas **de unde provine**. Documentul este deocamdată **în italiană**; acest wiki îi prezintă conținutul în română în [Calculul eficienței](Efficiency-Calculation-ro#modelul) și [Geometrie și atenuare](Geometry-and-Path-Loss-ro).

## Etichete

Fiecare pas are o etichetă colorată:

| Etichetă | Culoare | Semnificație |
|---|---|---|
| **FONTE** (sursă) | albastru | pasul preia o sursă citată; numărul dintre paranteze trimite la lista de la final |
| **RILIEVO** (verificare) | verde | comparație între program și surse, cu rezultatul |
| **SCELTA** (alegere) | portocaliu | o alegere a programului, nepreluată dintr-o sursă: de verificat cu experiența din trafic |

## Capitole

| Capitol | Conținut |
|---|---|
| 1. Introducere | Scopul, etichetele, ce înseamnă eficiența (OH5IY, MCG_MS; YA-MS folosește traseul real) |
| 2. Unde au loc reflexiile: stratul E | Urme la 80–120 km; altitudinea urmelor = moda histogramei Collm (verificare: 89,5 km pe 5/11/2026) |
| 3. Geometria traseului | Pământul și punctul median; elevația antenei (formula din articol); zona comună și limitele ei; Hot A / Hot B; lobul antenei (DL6WU, Kraus, W4RNL) |
| 4. Radiantul roiului | Poziția radiantului (IMO 2026/2027), data maximului (IMO sau longitudinea solară), profilul de activitate |
| 5. Condiția de reflexie | Reflexia speculară (McKinley), toleranța gaussiană 0,05 rad, orientarea optimă (SM6FHZ), formula DH9GCD |
| 6. De la un punct la eficiență | Puncte de reflexie la fiecare 15 km, ponderea fiecărui punct, procentul; comparația cu QTFGUI (DJ5HG) |
| 7. Citirea rezultatelor | Latura A / B, indicele traseului, culorile radianților, zonele PREV, secțiunea văzută de antenă |
| 8. Frecvența de lucru și atenuarea | Regulile λ³ / λ², de la radar la banda de radioamatori, referințele pentru atenuare |
| 9. Limite cunoscute | Doar urme subdense, antene izotrope, valori de lucru |
| 10. Surse | 17 surse numerotate |

## Butoane

| Buton | Ce face |
|---|---|
| **Exportă în Word (.docx)...** | Salvează o copie a `data/efficienza_spiegazione.docx` unde alegi (nume sugerat *YA-MS - calcolo dell'efficienza.docx*) |
| **Deschide în Word** | Deschide același `.docx` cu programul implicit pentru documentele Word (Word, LibreOffice, …) |

## Fișiere

| Fișier | Conținut |
|---|---|
| `data/efficienza_spiegazione.txt` | Textul afișat în filă, câte un bloc pe rând (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Versiunea Word |
| `doc/YA-MS_manuale_calcoli.docx` | **Manualul de calcul**: toate ecuațiile (editorul de ecuații din Word), numerotate, cu sursele lor |

Cele două documente se regenerează din sursă cu `tools/build_spiegazione.py data` și `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
