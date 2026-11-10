[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · **Deutsch** · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Effektivitätsberechnung

*Reiter: Vorhersageberechnung › Effektivitätsberechnung.*

[![Effektivitätsberechnung](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/de-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/de-2_3.png)

Die **Effektivität** eines Meteorstroms gibt in Prozent an, wie sehr die Position seines Radianten Reflexionen auf **deiner** Strecke zulässt. Das Konzept stammt von Ilkka **OH5IY** (MS-Soft) und wird im Artikel Cerrotta–Sartori aufgegriffen: Das Maximum der Effektivität fällt nicht mit dem visuellen Maximum (ZHR) zusammen, weil es davon abhängt, wo der Radiant relativ zu den beiden Stationen steht. MCG_MS von DL5MCG wendet dieselbe Idee auf vier feste Richtungen an; YA-MS berechnet sie für die **tatsächliche Strecke** zwischen den beiden Locatoren.

Dieser Reiter zeigt sie Stunde für Stunde für den in *Tag für 24-h-Tabelle (UTC)* gewählten Tag (Werte zur halben Stunde).

## Übersichtskarten

| Karte | Inhalt |
|---|---|
| **BESTE TAGESZEIT** | Stunde mit dem höchsten Streckenindex, der Index und die überwiegende Seite (A/B mit ihrem %) |
| **GÜNSTIGSTER STROM** | Der Strom mit dem größten ZHR × Effektivität des Tages, seine Effektivität, Stunde und Seite sowie die **beste Ausrichtung** (Radiant-Azimut +90° / −90°) |
| **JETZT** | Index und überwiegende Seite zu dieser Stunde und der empfohlene Hot (nur wenn der gewählte Tag heute ist) |
| **EXPERIMENTELLE VORHERSAGE** | Erwartete Reflexionen/h jetzt, in 1 h und in 2 h auf der Vorhersagefrequenz (Collm, SM6FHZ-Regeln; siehe [Experimentelle Vorhersage](Experimental-Forecasts-de)) |

Unter den Karten erklärt ein Streifen die Buchstaben A und B (siehe unten).

## Diagramm

*Stündliche Effektivität für … am … (UTC, Werte zur halben Stunde).* Für bis zu fünf Ströme: Effektivität % als durchgezogene Linie und die DH9GCD-Formel als gepunktete Linie gleicher Farbe; der **Streckenindex** als blaue Balken auf der rechten Skala.

## Stundentabelle

Eine Zeile pro an diesem Tag aktivem Strom (nach ZHR sortiert), 24 Spalten für die Stunden (UTC):

| Zelle | Bedeutung |
|---|---|
| `63A` | Effektivität 63 %, die meisten Reflexionen von Seite **A** |
| `41B` | Effektivität 41 %, Seite **B** |
| `3` | Effektivität unter 5 %: Zahl ohne Seitenbuchstaben |
| leer | Effektivität unter 1 % |
| `…↑` | der Radiant steht zu dieser Stunde an deiner Station **höher als 70°** (zu hoch) |
| gelber Text | Effektivität ≥ 50 % |

- **A** = **links**, von deiner Station zur Gegenstation gesehen (Zone Hot A); **B** = **rechts** (Zone Hot B). Es lohnt sich, die Antenne **um 10–30° zu dieser Seite** zu drehen (Side-Scatter, Artikel Cerrotta–Sartori).
- **Hellblaue Zeilen** (*DH9GCD %*, unter jedem Strom): die DH9GCD-Formel zum Vergleich.
- **Zeile Σ**: *Streckenindex (ZHR×Eff.)*.
- **Orange Zeile** (*Vorhersage … MHz (Refl./h)*): die experimentelle Vorhersage für die Stunden, für die es sie gibt (heute und ein Teil von morgen).

## Das Modell

Alle Schritte stehen im [Berechnungshandbuch](Efficiency-Explanation-de) (`doc/YA-MS_manuale_calcoli.docx`, Kapitel 5). Kurz gefasst:

**1. Spiegelnde Reflexion.** Eine Spur leitet das Signal nur dann von A nach B, wenn sie ein Ellipsoid mit A und B in den Brennpunkten tangiert (McKinley 1961). Die Spuren eines Stroms verlaufen parallel zur Radiantenrichtung ŝ (Artikel; McKinley). Für jeden Punkt P der E-Schicht, mit Einheitsvektoren zu den Stationen:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Dasselbe Gesetz liegt QTFGUI von DJ5HG und seinem Text *"Die Geometrie von Meteorscatterverbindungen"* (2004) zugrunde: Die Spur streut auf einen Kegel mit der Spur als Achse, und nur ein Empfänger auf dem Kegel hört sie. Bei einer idealen Spur ist die Kegelwand sehr dünn (ein Strahler von Tausenden Wellenlängen Länge); das Programm akzeptiert die Bedingung mit einer gaußförmigen Toleranz σ = 0,05 rad (etwa 3°), die für das steht, was der ideale Kegel nicht sieht: die Streuung der Radianten der Ströme (0,3–1,4°, vom GMN gemessen), vom Wind gekrümmte Spuren und ihre endliche Länge – *Entscheidung des Programms*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Gewicht jedes Punktes.** Leistung einer unterdichten Spur (McKinley; ITU-R P.843, Gl. 3), φ = halber Streuwinkel (begrenzt auf 85°, *Entscheidung*), β = Winkel zwischen der Spur und der Ausbreitungsebene A-P-B, p̂ = Einheitsnormale dieser Ebene:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Option „β-Winkel zwischen Spur und Strecke (vollständiger McKinley)“** (standardmäßig ein, vorsichtige Einstellung). Ein: Spuren, die die Ausbreitungsebene kreuzen, sind 10–15 dB weniger wert als solche, die in ihr liegen, sodass keine Spur überschätzt wird. Aus: Jede Spur wird so gewichtet, als läge sie in der Ebene (β = 0, Gewicht mit cos²φ), wie bis Version 1.6. *Prüfung:* Auf einer 1000-km-Strecke liegt ohne β das beste Radiantenazimut je nach Radiantenelevation 15°–90° neben der Strecke (30° bei Radiant in 30°, quer zur Strecke bei Radiant in 60°), und der quer stehende Radiant ist bei 30° Elevation 67 % wert; mit β liegt der beste Radiant immer in Streckenrichtung, und der quer stehende fällt auf 15 %. Mit β geht die Regel der besten Richtung von SM6FHZ / DH9GCD verloren; β bleibt eine Option, standardmäßig eingeschaltet, weil sie die vorsichtigsten Werte liefert, und Ausschalten bringt die Regel zurück.

Die Zahl der Meteore, die einen Punkt erreichen, ist proportional zum Sinus der Radiantenhöhe dort (ŝ·û_P), dieselbe Korrektur, die die IMO für die ZHR verwendet.

**Option „Längere Spuren bei niedrigem Radianten (DJ5HG)“** (Kontrollkästchen über dem Diagramm, standardmäßig aus, mit Tooltip): DJ5HG merkt an, dass bei niedrigem Radianten weniger Meteore pro km² fallen, die Spuren aber länger sind (bis zu 100 km nutzbar) und die Reflexionsbedingung öfter erfüllen. Mit eingeschalteter Option wird das Gewicht zu min(sin El, 15/100): Die nutzbare Schichtdicke, 15 km, geteilt durch den Sinus der Elevation ergibt die Spurlänge, begrenzt auf 100 km. Oberhalb von etwa 9° heben sich die beiden Effekte auf. Ausgeschaltet bleibt die Berechnung vorsichtig.

**Berechnungseinstellung** (dieselbe Zeile, Optionsfelder): **Vorsichtig** (Standard, die vorsichtigsten Werte: Spurhöhe vom Radar, normale Spuren, β ein), **Wie DJ5HG** (102 km, längere Spuren, β) und **Benutzerdefiniert**, das automatisch gewählt wird, wenn du die Höhe, das Kästchen *vom Radar*, die Option der längeren Spuren oder β von Hand änderst.

**3. Summe und Prozentwert.** Punkte alle 15 km in Spurhöhe, nur dort, wo beide Stationen sie oberhalb der Keulenelevation sehen (*Entscheidung*). 100 % ist die günstigste Radiantenposition für diese Strecke:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F wird einmal pro Strecke auf einem Richtungsgitter berechnet (Azimut alle 5°, Elevation alle 2,5°) und interpoliert.

**Effektivität in dB (Referenz DJ5HG).** Der Prozentwert bezieht sich nur auf die beste Radiantenposition für diese Strecke. Um verschiedene Strecken zu vergleichen, gibt das Programm die Effektivität auch in dB bezogen auf die feste Referenz von DJ5HG an: 0 dB ist das Maximum einer 1000 km langen Nord-Süd-Strecke über den Äquator, mit dem Radianten auf dem Himmelsäquator zur Tagundnachtgleiche, berechnet mit derselben Höhe und denselben Gewichten. DJ5HG gibt seine Werte als besser als 6 dB an.

**4. Seite und Index.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Der Buchstabe in der Tabelle ist die Seite mit dem größeren Anteil. *Entscheidungen des Programms (Handbuch Gl. 32–33).*

## Vergleich mit DH9GCD

Die Primärquellen für die beste Richtung sind Eshleman & Mlodnosky und Meeks & James (Proc. IRE, 1957), Hines (1955) und dessen experimentelle Prüfung durch Forsyth, Hines & Vogan (1955): Nur Radianten auf dem Halbkreis des Himmels senkrecht zur Winkelhalbierenden des Streuwinkels sind nutzbar, die Zahl der Spuren wächst mit sin El, und nahe dem Mittelpunkt liegen die nutzbaren Spuren etwa H·tan El seitlich, auf der dem Radianten gegenüberliegenden Seite. DJ5HG macht einen Vorbehalt: Bei einem **niedrigen** Radianten genau entlang der Strecke liefert McKinleys Formel starke Signale (Hamburg–Narvik, Quadrantiden, etwa 19 UTC), daher gilt „Radiant in Streckenrichtung = fast null“ nur für einen hohen Radianten; das Programm bleibt vorsichtig und zeigt die Warnung *NIEDRIGER RADIANT ENTLANG DER STRECKE*.

Eine unabhängige Prüfung: die Formel der besten Richtung von **DH9GCD**, wiedergegeben von **DF5HC** (DARC-Vortrag, Januar 2018) – eine veröffentlichte Primärquelle gibt es nicht –, mit El und Az als Elevation und Azimut des Radianten von deiner Station aus und P als Azimut der Gegenstation:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Sie ist maximal, wenn der Radiant auf 45° und quer zur Strecke steht. DF5HC hält den Radianten unter 20° für zu niedrig und **über 70° für zu hoch**: Diese Stunden erhalten in der Tabelle ein ↑ und eine Warnung in der [Himmelsansicht](Sky-View-de#warnungen). Die Formel berücksichtigt weder Entfernung noch Höhen, ist aber ein guter Vergleichswert.

## Prüfungen

| Prüfung | Ergebnis |
|---|---|
| SM6FHZ-Regel (VUSHF 2025): beste Strecke rechtwinklig zum Radiant-Azimut, Ausrichtung = Radiant-Az. ±90°, Toleranz ±40–50° | Vom Modell reproduziert; mit dem Radianten in Streckenrichtung und hoch am Himmel ist die Effektivität fast null |
| QTFGUI von DJ5HG, Hamburg JO53IM – Barcelona, Quadrantiden, 4. Januar (Beispiel aus seinem Handbuch) | QTFGUI: 07:00 Ausrichtung 252°, −8 dB; 08:00 keine Reflexionszone; 09:00 Ausrichtung 168°, −4 dB. YA-MS (Höhe 102 km wie QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Alle drei Methoden sehen das Loch um 08:00, mit dem Radianten fast im Zenit |
| Kurven von DJ5HG (*Die Geometrie…*, Bild 8–9: von Hamburg und München aus, Quadrantiden, 4. Januar; aus dem Diagramm abgelesen, etwa ±0,5 dB und ±15 min) gegenüber dem automatischen Test `--prova-dj5hg` (ein Wert pro Stunde) | Zeitpunkte: Das Loch mit dem Radianten nahe dem Zenit fällt auf dieselben Stunden (Barcelona 07:30–08:30 gegenüber 07–09; Sofia 06:36–07:48 gegenüber 07–08; Narvik 07–08:30 gegenüber 07–09); Moskau ist in beiden 03–10 geschlossen, von Hamburg aus offen bis etwa 02:30 und von München aus bis etwa 00:30, wie DJ5HG schreibt. Ausrichtungen: 2–10° Unterschied. Pegel und Verlauf bei 102 km (mittlere Abweichung und RMS-Abweichung von den Kurven): ohne β, ohne längere Spuren −1,6 / 4,0 dB; längere Spuren +1,1 / 4,6 dB; β −5,4 / 6,2 dB, aber mit dem besten Verlauf (3,0 dB nach Abzug des Mittelwerts, gegenüber 3,6): Die tiefen Minima bei niedrigem Radianten erscheinen (Barcelona −15,6 dB um 17 gegenüber −16 dB um 19:36; Sofia −18,5 dB um 20 gegenüber −14 dB). β und längere Spuren (*Wie DJ5HG*) −2,2 / 4,7 dB; die vorsichtige Einstellung (Radarhöhe 89,5 km, β ein, keine längeren Spuren) −6,9 / 7,6 dB, Verlauf 3,3 dB. Ohne β zeigt YA-MS das Minimum bei niedrigem, fast in Streckenrichtung stehendem Radianten kaum (−8,6 und −10,4 dB): Das ist DJ5HGs eigener Vorbehalt, daher die Warnung |
| Abtastung alle 5 km statt 15 km | die Prozentwerte ändern sich um weniger als 0,3 Punkte |

> Die Dokumentation von MS-Soft 5.2 definiert die Effektivität von OH5IY als relativen Index nur für unterdichte Spuren, mit zwei Faktoren (Elevation des Radianten, am besten etwa 45°, und Winkel zur Strecke, am besten 90°) und einem für überdichte Spuren von Hand auf 20 % angehobenen Minimum; die Formel ist nicht veröffentlicht. MCG_MS berechnet sie für vier feste Richtungen und, mit dem DX-Locator, für die tatsächliche Strecke. Das Modell berücksichtigt nur unterdichte Spuren, mit isotropen Antennen; überdichte Bursts und der sporadische Untergrund sind nicht in der Effektivität enthalten (der sporadische Untergrund wird durch den Radarfluss dargestellt).
