[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · **Deutsch** · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

# Geometrie und Dämpfung

*Reiter: Vorhersageberechnung › Geometrie und Dämpfung.*

[![Geometrie und Dämpfung](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/de-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/de-2_2.png)

Ein Textbericht der Strecke (markierbar, du kannst ihn also kopieren) und rechts das Diagramm **Antennenelevation in Abhängigkeit von der Entfernung zum Streupunkt**. Zahlen in eckigen Klammern verweisen auf die Gleichungen des Berechnungshandbuchs (`doc/YA-MS_manuale_calcoli.docx`).

## Eingaben dieses Reiters

| Feld | Standard | Verwendung |
|---|---|---|
| **Leistung W** | 400 | Sendeleistung für die Streckenbilanz |
| **Antennengewinn dBi (TX = RX)** | 14 | Gleiche Antenne an beiden Enden |
| **Min. Signal dBm** | −130 | Empfangsschwelle (Artikel: 8-Element-Yagi + Vorverstärker) |
| **Spurdichte q = 10^ … Elektronen/m** | 14 | Elektronen-Liniendichte der unterdichten Spur |

Stationen, Band, Spurhöhe, Keulenelevation, Boom und Hot-Spot-Abstand kommen aus den [Bedienzeilen](Getting-Started-de#1-die-drei-bedienzeilen).

## Abschnitte des Berichts

| Abschnitt | Inhalt |
|---|---|
| **STRECKENGEOMETRIE (Kugelerde, R = 6372,7955 km)** | Station und Gegenstation mit Höhen; Entfernung, Azimut und Gegenazimut; Mittelpunkt (Locator und Koordinaten); Spurhöhe (*← vom Collm-Radar gemessener Modalwert*, wenn vom Radar übernommen); Antennenelevation zum Mittelpunkt |
| **HOT A / HOT B (klassische Hot-Spots für die Antennenausrichtung)** | Für jeden: Locator, Azimut von dir und Abweichung von der Direktrichtung, Azimut von der Gegenstation, Entfernung, Elevation |
| **GRENZEN DER GEMEINSAMEN ZONE** | Reichweite in Spurhöhe bei der Keulenelevation; Grenze A / Grenze B mit Azimuten |
| Antenne | Boom in λ, Gewinn, horizontale / vertikale Keule; ob Hot A und Hot B in oder außerhalb der Keule liegen |
| **STRECKENDÄMPFUNG (unterdichte Spur, McKinley 1961; ohne Antennengewinne)** | Tabelle für Mittelpunkt (Forward), Hot A und Hot B auf 28, 50, 70, 144, 222 und 432 MHz |
| **BILANZ BEI … MHz (Mittelpunkt)** | Leistung und EIRP, Streckendämpfung, Signal an der Antenne, Empfangsschwelle, **Reserve**; dieselbe Reserve mit der mittleren Dämpfung von OH5IY |
| **EXPERIMENTELLE REGELN ZWISCHEN DEN BÄNDERN (SM6FHZ, VUSHF 2025)** | Anzahl/Intensität und Dauer gegenüber 144 MHz; IARU-Maximalping |

## Locator und Strecke

Locator (4, 6 oder 8 Zeichen; Feldmitte, IARU-Maidenhead-System) [14]. Entfernung, Azimut und Mittelpunkt mit Großkreisformeln auf einer Kugel mit Radius **r = 6372,7955 km** (Artikel Cerrotta–Sartori) [15–16]. Zeitabhängige Berechnungen beziehen sich auf den **Mittelpunkt**, weil die beste Zeit an den beiden Enden um bis zu 1,5 Stunden abweichen kann (SM6FHZ).

## Antennenelevation

**Quelle:** Formel des Artikels Cerrotta–Sartori (Bild 7), mit x = d/r, d der Bodenentfernung zum Reflexionspunkt, H der Spurhöhe und h der Stationshöhe [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Prüfung:** Sie stimmt mit der exakten Kugelgeometrie auf 0,03° überein. Das Programm verwendet den Arkustangens mit zwei Argumenten, der jenseits des Horizonts negative Werte liefert und das im Artikel erwähnte Periodizitätsproblem vermeidet. Eine negative Elevation zum Mittelpunkt bedeutet *Strecke jenseits der geometrischen Reichweite eines Einzelsprungs*.

## Horizontreichweite

Bodenentfernung, in der ein Strahl mit der Elevation e die Höhe H erreicht (geometrische Umkehrung der obigen Formel) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Prüfung:** H = 89,5 km, e = 0° → **1062 km**. Im Beispiel des Artikels (JN44BB–IO53RT) setzt die Zeichnung die Horizontschnittpunkte etwa 870 km von den Stationen entfernt, was einer um etwa 2° angehobenen Keule entspricht (865 km).

## Grenzen der gemeinsamen Zone

**Quelle:** Der Artikel bestimmt die Schnittpunkte der Kurven, an denen der Horizont jeder Station die E-Schicht trifft: die Schnittpunkte zweier Kreise mit dem Winkelradius ρ = d_H/r um A und B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Ist 1 − |p0|² < 0, ist die Strecke länger als 2·d_H und die Stationen sehen **keine gemeinsame Zone der E-Schicht**.

**Prüfung:** Das sind die **entferntesten Ränder** des von beiden Stationen gesehenen Himmels, **nicht die Zielpunkte**. Auf JN70CN–IN78UO (1710 km, Azimut 308°) liegen sie 1062 km von der Station entfernt, 37° links und rechts der Direktrichtung, während MSHV 10° vorschlägt. Deshalb heißen sie *Grenze A* / *Grenze B* und werden auf der Karte blass gezeichnet.

## Hot A und Hot B

**Quelle:** Die Reflexionen sporadischer Meteore konzentrieren sich in zwei Zonen („Hot-Spots“) beiderseits des Mittelpunkts. J. Richardson (AMS) gibt in der von DJ5HG zitierten Tabelle (*Die Geometrie von Meteorscatterverbindungen*, 2004) die Antennenablage gegenüber der direkten Richtung an: **13° bei 1000 km, 11° bei 1250 km, 10° bei 1500 und 2000 km**. Das AMS Bulletin Nr. 203, aufgegriffen von W8WN, gibt 10° bei 1500 und 1800 km an.

**Entscheidung:** Hot A und Hot B sind die Punkte im Abstand s vom Mittelpunkt M, senkrecht zur Strecke. Mit angekreuztem *auto (AMS)* (Standard) ergibt sich s aus der Ablage von Richardsons Tabelle, linear interpoliert (13° unter 1000 km, 10° über 2000 km): s = (D/2)·tan(Ablage). Nicht angekreuzt wird s von Hand eingegeben, 30–400 km (MSHV verwendet 150 km); A links, von deiner Station zur Gegenstation gesehen, B rechts [21]. Die von der Station aus gesehene Abweichung beträgt etwa [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Prüfung:** mit der AMS-Tabelle 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, also wie die bisher und von MSHV verwendeten 150 km; auf kurzen Strecken rückt die Tabelle die Hot-Spots näher an den Mittelpunkt.

## Dämpfung unterdichter Spuren

**Quelle:** McKinleys Gleichung und ITU-R-Empfehlung P.843 für unterdichte Spuren (sin α = 1), ohne Antennengewinne; q = Elektronen-Liniendichte, r_e = klassischer Elektronenradius = 2,818·10⁻¹⁵ m, R1, R2 Entfernungen von der Spur, φ halber Streuwinkel, β Winkel zwischen der Spur und der Streckenebene, a₁ Anfangsradiusfaktor mit r₀ in m und h in km (P.843, Gl. 4 und 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Entscheidung:** Die Streckenbilanz und die Dämpfungstabelle verwenden β = 90° (Spur quer zur Streckenebene, der ungünstigste Fall: vorsichtiger Wert), und die Streckenbilanz zeigt auch den besten Fall, β = 0. r₀ wird in der mittleren Echohöhe für die Frequenz genommen, h = 124 − 17 log f (P.843, Gl. 15): 0,76 m in 95 km für 50 MHz, 0,40 m in 87 km für 144 MHz, 0,21 m in 79 km für 432 MHz. Über 1000 km beträgt a₁ 0,2 dB auf 50 MHz, 0,6 dB auf 144 MHz und 1,4 dB auf 432 MHz (2,9 dB bei 600 km); bei den festen 102 km von DJ5HG wären es auf 432 MHz etwa 70 dB, also überhaupt kein Echo.

**Prüfung:** Mit q = 10¹⁴ Elektronen/m, Spuren in 89,5 km und β = 0, auf 144 MHz: **182–192 dB** zwischen 600 und 2100 km (185 dB bei 1000 km), innerhalb des Bereichs von **172–190 dB**, den John Worsnop **G4BAO** in seiner Doktorarbeit berechnet hat, wie GM8JBJ berichtet. Mit β = 90° steigt die Dämpfung um 10 dB bei 600 km, 13 dB bei 1000 km und 16 dB bei 2100 km; der **Mittelwert von 200 dB** von OH5IY liegt zwischen beiden Fällen. Die 182 dB in der Tabelle von GM8JBJ sind keine Bestätigung: Die Tabelle nennt keine Frequenz, ihre 86,4 dB pro Teilstrecke sind die Freiraumdämpfung über 500 km bei 1 MHz (der Term 20 log f fehlt: 129,6 dB auf 144 MHz), und ihre Posten ergeben zusammen 163,8 dB, nicht 182; die Seite sagt weder „Minimum“ noch „144 MHz“.

## Streckenbilanz

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Die Gewinne werden in dBi eingegeben und verwendet: McKinleys Dämpfung bezieht sich auf isotrope Antennen, daher wird keine Dipolkorrektur von 2,15 dB abgezogen (EIRP = Leistung + Gewinn). Der Bericht nennt auch die Reserve mit der **mittleren Dämpfung von OH5IY** (200 dB bei 144 MHz, mit λ³ auf das gewählte Band umgerechnet). Referenz des Artikels: Benötigt werden etwa **70 dBm EIRP** (−130 dBm + 200 dB, z. B. etwa 400 W an 14 dBi).

## Antennengewinn und Keule

**Gewinn – Quelle:** Kurve von Günter Hoch **DL6WU** für lange Yagis in Abhängigkeit von der Boomlänge L, wiedergegeben von W8IO (gültig ab etwa 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Prüfung anhand der NEC-Modelle von L.B. Cebik W4RNL auf 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elemente | Boom (λ) | W4RNL NEC (dBi) | Formel (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Die Abweichung übersteigt nie **0,1 dB**: Der Gewinn hängt mehr von der Boomlänge als vom Design ab (VK3AUU-Yagis haben bei gleicher Elementzahl einen kürzeren Boom). Der Yagi Calculator von VK5DJ liefert auch Schätzungen für die Varianten VK3AUU, WA2PHW und DJ9BV, deren Formeln nicht veröffentlicht sind.

**Keule – Quelle:** Kraus-Regel, mit kreisförmiger Keule θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Prüfung:** Die NEC-Modelle von W4RNL für DL6WU-Yagis ergeben eine **um 5–10 % schmalere horizontale Keule** als Kraus: 33,8° / 26,4° / 22,6° für 12, 19 und 26 Elemente, gegenüber 37,3° / 28,0° / 23,9°. Einfache Formeln vernachlässigen die vorderen Nebenkeulen (W4RNL, *Long-Boom Yagi Rules of Thumb*). Bei langen Booms ist die vertikale Keule etwas breiter als die horizontale (14 λ: 18,4° / 18,8°).

**Entscheidung** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Beispiel: Yagi mit 14 λ auf 432 MHz → 20,3 dBi, Keule 18,1° horizontal und 19,5° vertikal; die Modelle von W4RNL ergeben 20,4 dBi und 18,4° / 18,8°. Das sind Näherungsregeln, abgeleitet aus einigen wenigen DL6WU-Antennen.

Die Antenne gilt immer als auf die Gegenstation gerichtet. Ein Hot-Spot liegt **in der Keule**, wenn |Az(Hot) − Az(Antenne)| ≤ θ_horizontal/2: Dann wird er in der [Himmelsansicht](Sky-View-de) grau gezeichnet und eine Warnung erscheint. In der Effektivitätsberechnung sind die Antennen isotrop; die tatsächliche Keule wird nur für diese Prüfung verwendet.

## Experimentelle Regeln zwischen den Bändern

Gegenüber 144 MHz: Anzahl/Intensität × (144/f)³ (in dB), Dauer × (144/f)² (SM6FHZ, VUSHF 2025). Maximale Pingdauer nach IARU Region 1: 1000 ms auf 50 MHz, 500 ms auf 70 MHz, 100 ms auf 144 MHz, 13 ms auf 432 MHz (VHF Handbook, im Artikel zitiert). Siehe auch [Experimentelle Vorhersage](Experimental-Forecasts-de).
