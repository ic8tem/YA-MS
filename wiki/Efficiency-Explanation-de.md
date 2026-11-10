[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · **Deutsch** · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh)

# Effektivität - Erklärung

*Reiter: Technische Dokumente › Effektivität - Erklärung.*

[![Effektivität - Erklärung](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/de-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/de-3_3.png)

Ein technisches Dokument, *"Come YA-MS calcola l'efficienza di uno sciame"* (Wie YA-MS die Effektivität eines Meteorstroms berechnet), das im Programm als helle Seite angezeigt wird. Es erklärt **Schritt für Schritt**, wie die Effektivität ermittelt wird, und gibt bei jedem Schritt an, **woher er stammt**. Das Dokument ist derzeit **auf Italienisch**; dieses Wiki gibt seinen Inhalt auf Deutsch in [Effektivitätsberechnung](Efficiency-Calculation-de#das-modell) und [Geometrie und Dämpfung](Geometry-and-Path-Loss-de) wieder.

## Kennzeichnungen

Jeder Schritt trägt eine farbige Kennzeichnung:

| Kennzeichnung | Farbe | Bedeutung |
|---|---|---|
| **FONTE** (Quelle) | blau | der Schritt greift eine zitierte Quelle auf; die Zahl in Klammern verweist auf die Liste am Ende |
| **RILIEVO** (Prüfung) | grün | Vergleich zwischen Programm und Quellen, mit dem Ergebnis |
| **SCELTA** (Entscheidung) | orange | eine Entscheidung des Programms, die nicht aus einer Quelle stammt: mit der Erfahrung auf dem Band zu prüfen |

## Kapitel

| Kapitel | Inhalt |
|---|---|
| 1. Einleitung | Zweck, Kennzeichnungen, was Effektivität bedeutet (OH5IY, MCG_MS; YA-MS verwendet die tatsächliche Strecke) |
| 2. Wo Reflexionen entstehen: die E-Schicht | Spuren in 80–120 km; Spurhöhe = Modalwert des Collm-Histogramms (Prüfung: 89,5 km am 5.11.2026) |
| 3. Geometrie der Strecke | Erde und Mittelpunkt; Antennenelevation (Formel des Artikels); gemeinsame Zone und ihre Grenzen; Hot A / Hot B; Antennenkeule (DL6WU, Kraus, W4RNL) |
| 4. Der Radiant des Stroms | Position des Radianten (IMO 2026/2027), Datum des Maximums (IMO oder Sonnenlänge), Aktivitätsprofil |
| 5. Reflexionsbedingung | Spiegelnde Reflexion (McKinley), gaußförmige Toleranz 0,05 rad, beste Ausrichtung (SM6FHZ), DH9GCD-Formel |
| 6. Vom einzelnen Punkt zur Effektivität | Reflexionspunkte alle 15 km, Gewicht jedes Punktes, Prozentwert; Vergleich mit QTFGUI (DJ5HG) |
| 7. Ergebnisse lesen | Seite A / B, Streckenindex, Farben der Radianten, PREV-Zonen, Schnitt von der Antenne aus gesehen |
| 8. Arbeitsfrequenz und Streckendämpfung | λ³- / λ²-Regel, vom Radar zum Amateurfunkband, Referenzwerte der Streckendämpfung |
| 9. Bekannte Grenzen | Nur unterdichte Spuren, isotrope Antennen, Arbeitswerte |
| 10. Quellen | 17 nummerierte Quellen |

## Schaltflächen

| Schaltfläche | Was sie tut |
|---|---|
| **Nach Word exportieren (.docx)...** | Speichert eine Kopie von `data/efficienza_spiegazione.docx` an einem Ort deiner Wahl (vorgeschlagener Name *YA-MS - calcolo dell'efficienza.docx*) |
| **In Word öffnen** | Öffnet dieselbe `.docx` mit dem Standardprogramm für Word-Dokumente (Word, LibreOffice, …) |

## Dateien

| Datei | Inhalt |
|---|---|
| `data/efficienza_spiegazione.txt` | Der im Reiter angezeigte Text, ein Block pro Zeile (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Die Word-Fassung |
| `doc/YA-MS_manuale_calcoli.docx` | Das **Berechnungshandbuch**: alle Gleichungen (Word-Formeleditor), nummeriert, mit ihren Quellen |

Die beiden Dokumente werden aus dem Quellcode mit `tools/build_spiegazione.py data` und `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` neu erzeugt.
