[English](Getting-Started) · [Italiano](Getting-Started-it) · **Deutsch** · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Erste Schritte

Beim ersten Start zeigt YA-MS eine Beispielstrecke (JN70CN → JO62QM auf 144 MHz). Fünf Minuten reichen, um es für deine Station einzurichten.

## 1. Die zwei Bedienzeilen

Über den Reitern liegen zwei Bedienzeilen, die für alle Reiter gelten. Die Schaltfläche **Bedienung** oben rechts klappt sie ein und aus (nützlich bei großer Schrift); die Wahl wird gespeichert. Deine Station (Locator, Höhe, Band und Berechnen) steht oben rechts im Live-Verkehr.

**Meine Station – Verkehr live**

| Bedienelement | Was es tut |
|---|---|
| **Mein Locator** / **Höhe m** | Dein Maidenhead-Locator (4, 6 oder 8 Zeichen; verwendet wird die Feldmitte) und die Höhe der Station über dem Meeresspiegel. |
| **Gegenstation** / **Höhe m** | Neben der Karte, rechts, ist das Feld der Gegenstation: Rufzeichen eingeben und Enter drücken, der Locator kommt aus der CALL3-Datenbank (wie in YAEC und LIVETROPOVHF); darunter stehen Locator und Höhe. Das Rufzeichen kann auch ins Locator-Feld geschrieben werden. |
| **Band MHz** | 28, 50, 70, 144, 222 oder 432 MHz: verwendet für Antennengewinn und Keule, die Flussschätzung und die Streckenbilanz. |
| **Berechnen** | Berechnet die Strecke neu (Abtastung der E-Schicht: wenige Sekunden). |
| **Antennen-Az.** | Oben im Feld der Gegenstation, neben der Karte: Azimut deiner Antenne, immer **Richtung DX** (Azimut der Strecke). Darunter, in derselben Spalte, steht die Kartenlegende. |

**Zeile 1 – E-Schicht und Antenne**

| Bedienelement | Was es tut |
|---|---|
| **Spurhöhe km** + **vom Radar** | Höhe der Meteorspuren (Standard 90 km). Mit angekreuztem *vom Radar* wird die häufigste vom Collm-Radar gemessene Höhe (Modalwert) verwendet; siehe [Radarfluss](Radar-Flux-de). |
| **Keulenelev. °** | Erhebung des Maximums der vertikalen Antennenkeule: Eine auf 0° fixierte Richtantenne hat wegen der Bodenreflexion trotzdem ihre Keule einige Grad über dem Horizont (meist 3-8°). Mit eingeschaltetem Kästchen **Antennendiagramm** (Voreinstellung) werden die Punkte der E-Schicht mit dem vertikalen Diagramm beider Antennen gewichtet; ausgeschaltet zählen nur die Punkte, die beide Stationen über dieser Erhebung sehen. |
| **Yagi: Boomlänge m** | Boomlänge deiner Yagi. Das Programm zeigt die Länge in λ, den Gewinn (DL6WU-Kurve) und den Öffnungswinkel (−3 dB) horizontal und vertikal; siehe [Geometrie und Dämpfung](Geometry-and-Path-Loss-de#antennengewinn-und-keule). Unter 2 λ ist die Schätzung ungenau. |
| **Hot-Spot ab Mittelpunkt km** + **auto (AMS)** | Abstand von Hot A und Hot B vom Mittelpunkt. Mit angekreuztem *auto (AMS)* (Standard) folgt er der von DJ5HG zitierten Tabelle der Antennenablage von J. Richardson (AMS): 13° bei 1000 km, 11° bei 1250 km, 10° bei 1500 und 2000 km (etwa 115, 121, 132 und 176 km vom Mittelpunkt). Kreuz es nicht an, um 30–400 km von Hand einzugeben (MSHV verwendet 150 km). |

**Zeile 2 – Zeit**

| Bedienelement | Was es tut |
|---|---|
| **Zeit** | UTC-Uhr. |
| **Berechnungsdatum (UTC)** | Der Tag der Berechnung für [Vorhersageberechnung](Sky-View-de) und [Radar GRAVES](GRAVES-Radar-de) (standardmäßig heute), zur aktuellen Tageszeit. Auch: der Tag, der in [Effektivitätsberechnung](Efficiency-Calculation-de) und in der GRAVES-Zeitleiste gezeigt wird. |
| **Stunden (−12 bis +36 h)** | Verschiebt den Zeitpunkt der Berechnung von 12 Stunden vor bis 36 Stunden nach dieser Uhrzeit, in Schritten von 15 Minuten. Daneben: *Berechnung für: jetzt* oder *Berechnung für: TT/MM hh:mm UTC*. |
| **Echtzeit** | Zurück zu jetzt. |

Die Zeitleiste («Stunden (−12 bis +36 h)» und «Echtzeit») steht oben in der Registerkarte Vorhersageberechnung, weil sie nur für diese Berechnung gilt.

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
