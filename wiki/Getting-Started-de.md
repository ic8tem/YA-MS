[English](Getting-Started) · [Italiano](Getting-Started-it) · **Deutsch** · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh)

# Erste Schritte

Beim ersten Start zeigt YA-MS eine Beispielstrecke (JN70CN → JO62QM auf 144 MHz). Fünf Minuten reichen, um es für deine Station einzurichten.

## 1. Die drei Bedienzeilen

Über den Reitern liegen drei Bedienzeilen, die für alle Reiter gelten. Die Schaltfläche **Bedienung** oben rechts klappt sie ein und aus (nützlich bei großer Schrift); die Wahl wird gespeichert.

**Zeile 1 – Stationen und Band**

| Bedienelement | Was es tut |
|---|---|
| **Mein Locator** / **Höhe m** | Dein Maidenhead-Locator (4, 6 oder 8 Zeichen; verwendet wird die Feldmitte) und die Höhe der Station über dem Meeresspiegel. |
| **Gegenstation** / **Höhe m** | Locator und Höhe der Station, die du arbeiten willst. |
| **Band MHz** | 28, 50, 70, 144, 222 oder 432 MHz: verwendet für Antennengewinn und Keule, die Flussschätzung und die Streckenbilanz. |
| **Berechnen** | Berechnet die Strecke neu (Abtastung der E-Schicht: wenige Sekunden). |
| **Antennen-Az.** | Azimut deiner Antenne: immer **Richtung DX** (Azimut der Strecke). |
| **Schrift** | Größe des gesamten Textes, 100–300 %. Siehe [Einstellungen](Settings-and-Data-Folder-de#schrift-und-bedienung). |

**Zeile 2 – E-Schicht und Antenne**

| Bedienelement | Was es tut |
|---|---|
| **Spurhöhe km** + **vom Radar** | Höhe der Meteorspuren (Standard 90 km). Mit angekreuztem *vom Radar* wird die häufigste vom Collm-Radar gemessene Höhe (Modalwert) verwendet; siehe [Radarfluss](Radar-Flux-de). |
| **Keulenelev. °** | Niedrigste Elevation deiner Antennenkeule (0° = Horizont). Verwendet werden nur Punkte der E-Schicht, die beide Stationen oberhalb dieser Elevation sehen. |
| **Yagi: Boomlänge m** | Boomlänge deiner Yagi. Das Programm zeigt die Länge in λ, den Gewinn (DL6WU-Kurve) und den Öffnungswinkel (−3 dB) horizontal und vertikal; siehe [Geometrie und Dämpfung](Geometry-and-Path-Loss-de#antennengewinn-und-keule). Unter 2 λ ist die Schätzung ungenau. |
| **Hot-Spot ab Mittelpunkt km** | Abstand von Hot A und Hot B vom Mittelpunkt, 30–400 km (Standard 150 km, wie AMS Bulletin 203 / W8WN / MSHV). |

**Zeile 3 – Zeit**

| Bedienelement | Was es tut |
|---|---|
| **Zeit** | UTC-Uhr. |
| **Zeit der Himmelsansicht (±36 h)** | Verschiebt die [Himmelsansicht](Sky-View-de) und den Reiter [Radar GRAVES](GRAVES-Radar-de) um bis zu 36 Stunden zurück oder vor, in Schritten von 15 Minuten. |
| **Echtzeit** | Zurück zu jetzt. |
| **Tag für 24-h-Tabelle (UTC)** | Der Tag, der in [Effektivitätsberechnung](Efficiency-Calculation-de) und in der GRAVES-Zeitleiste gezeigt wird. |

## 2. Deine Station und die Gegenstation

1. Gib **Mein Locator** und **Höhe m** ein.
2. Gib Locator und Höhe der **Gegenstation** ein – oder klicke in der [Himmelsansicht](Sky-View-de) auf die Karte: **Linksklick = Gegenstation**, **Rechtsklick = meine Station** (setzt jeweils den Locator).
3. Wähle **Band MHz** und drücke **Berechnen**.

Die Statusleiste unten bestätigt: *Strecke berechnet: … km, … Reflexionspunkte in … s abgetastet*.

## 3. Deine Antenne

Gib die **Boomlänge** deiner Yagi ein. Das Programm leitet Gewinn und Keule ab und warnt dich, wenn Hot A oder Hot B schon **in der Keule** liegen, während die Antenne auf die Gegenstation zeigt (dann werden sie grau gezeichnet: Die Antenne muss nicht gedreht werden).

## 4. Die Ergebnisse lesen

| Frage | Wo nachsehen |
|---|---|
| Welcher Strom hilft meiner Strecke jetzt, und von welcher Seite? | [Himmelsansicht](Sky-View-de): Liste der Ströme, empfohlener Hot in Rot, PREV-Zonen |
| Welche ist heute die beste Stunde? | [Effektivitätsberechnung](Efficiency-Calculation-de): Übersichtskarten und Stundentabelle |
| Wie viele Meteore zählt das Radar? | [Radarfluss](Radar-Flux-de) |
| Wie viele Pings kann ich auf 144 MHz erwarten? | [Experimentelle Vorhersage](Experimental-Forecasts-de) (experimentell) |
| Kann meine Station die Strecke schaffen? | [Geometrie und Dämpfung](Geometry-and-Path-Loss-de): Streckendämpfung und Reserve |
| Wann ist das nächste Maximum? | [Ströme](Showers-de) |
| Kann ich mit GRAVES testen? | [Radar GRAVES](GRAVES-Radar-de) |

## Praktische Regeln (aus den Quellen)

- **Senkrecht zum Strom ausrichten**: Die beste Strecke liegt rechtwinklig zum Radiant-Azimut; beste Ausrichtung = Radiant-Azimut ±90°, Toleranz ±40–50° (SM6FHZ).
- **Side-Scatter**: Drehe die Antenne um 10–30° zu der Seite (A oder B), von der die meisten Reflexionen kommen (Artikel Cerrotta–Sartori).
- Ein **zu hoher** (über 70°) oder zu niedriger (unter 20°) **Radiant** liefert wenige nutzbare Spuren (DF5HC, DH9GCD).
- Sporadische Meteore haben ihr Maximum gegen **06 UTC** (Artikel; vom Collm-Fluss bestätigt).
- Nutzbare Entfernungen auf 432 MHz: 800–2000 km, am besten etwa 1400 km (SM6FHZ); beste Entfernung allgemein 1300–1500 km (DF5HC).

Weiter: [Himmelsansicht](Sky-View-de).
