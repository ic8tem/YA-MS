**English** · [Italiano](Sources-it) · [Deutsch](Sources-de) · [Nederlands](Sources-nl) · [Français](Sources-fr) · [Español](Sources-es) · [Português](Sources-pt) · [Português (Brasil)](Sources-pt-BR) · [Dansk](Sources-da) · [Norsk](Sources-nb) · [Svenska](Sources-sv) · [Íslenska](Sources-is) · [Eesti](Sources-et) · [Lietuvių](Sources-lt) · [Latviešu](Sources-lv) · [Polski](Sources-pl) · [Čeština](Sources-cs) · [Magyar](Sources-hu) · [Română](Sources-ro) · [Ελληνικά](Sources-el) · [Русский](Sources-ru) · [Українська](Sources-uk) · [Türkçe](Sources-tr) · [Afrikaans](Sources-af) · [العربية](Sources-ar) · [עברית](Sources-he) · [اردو](Sources-ur) · [हिन्दी](Sources-hi) · [বাংলা](Sources-bn) · [ไทย](Sources-th) · [Bahasa Indonesia](Sources-id) · [Tagalog](Sources-tl) · [日本語](Sources-ja) · [한국어](Sources-ko) · [中文](Sources-zh) · [中文 (繁體)](Sources-zh-TW)

# Sources

*Tab: Technical documents › Sources.*

[![Sources](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)

The **Sources** tab lists every work YA-MS is built on, grouped as below (the text is selectable, so you can copy the references). The same sources, numbered, close the calculation manual (`doc/YA-MS_manuale_calcoli.docx`) and the [Efficiency - explanation](Efficiency-Explanation) document.

## MAIN SOURCE

| Source | Used for |
|---|---|
| Costantino Cerrotta **IC8TEM**, Gianluigi "Gigi" Sartori **IV3GTH** – *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (article in Italian, version 7) | Trails in the E layer at about 90 km (SKiYMET radar), Earth radius 6372.7955 km, elevation formula, Hot A / Hot B, side-scatter 10–30°, path loss, minimum signal −130 dBm, IARU ping durations, sporadic peak at 06 UTC |

## EFFICIENCY: CALCULATION AND THEORY

| Source | Used for |
|---|---|
| Ilkka Yrjölä **OH5IY** – MS-Soft, www.kolumbus.fi/oh5iy (historical site) | Concept of shower efficiency; 200 dB average path loss |
| Wilhelm Rauh **DL5MCG** – MCG_MS, MS Efficiency Calculator v1.61, qsl.net/dl5mcg | Efficiency on four fixed directions (comparison) |
| Ingolf **SM6FHZ** – *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, May 2025 | λ³ and λ² rules, midpoint, best direction (radiant az ±90°) |
| D.W.R. **McKinley** – *Meteor Science and Engineering*, McGraw-Hill, 1961 | Specular reflection, underdense trail equation |
| John **GM8JBJ** – Meteor scatter path loss, hamradio.engineering (from Kaiser & Closs 1952) | 172–190 dB path loss computed by John Worsnop **G4BAO** (PhD thesis), about 6 dB less for trails aligned with the path; the page's own 182 dB table is not used (see [Geometry and path loss](Geometry-and-Path-Loss)) |
| Shelby **W8WN** – qsl.net/w8wn/hscw (AMS Bulletin 203 offset table) | Optimum elevation and offset, hot spots 50–150 km |
| **LZ2HV** – MSHV | Hot A / Hot B (comparison; in the manual) |
| Klaus von der Heide **DJ5HG** – QTFGUI and the "QTFGUI Help" manual (2007) | Cone scattering law; Hamburg – Barcelona Quadrantids test case used to verify the model |
| Jens **DF5HC** – *"Meteorscatter auf UKW"*, DARC conference, January 2018 | Best-direction formula by **DH9GCD**; cone scattering and HOT-A / HOT-B choice by DJ5HG; useful radiant 20–70°; best distance 1300–1500 km; sporadic meteors by KB0VUK |
| Günter Hoch **DL6WU** – gain vs boom length of long Yagis, reported by W8IO (w8io.com) | G(dBi) = 7.773 log(L/λ) + 11.43 |
| J.D. **Kraus** – *Antennas*, McGraw-Hill | G = 41253 / (θE·θH) |
| L.B. Cebik **W4RNL** – *Long-Boom Yagi Rules of Thumb: A Comparison with Modeling Data*; *Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2* (VK3AUU Yagis by David Tanner) | NEC simulations used to verify the gain curve and correct the horizontal lobe (0.93 × Kraus) |
| John Drew **VK5DJ** – Yagi Calculator | Gain estimates for the VK3AUU, WA2PHW and DJ9BV variants |
| J. **Meeus** – *Astronomical Algorithms*, 2nd ed., Willmann-Bell, 1998 | Julian day, sidereal time, solar longitude, azimuth/elevation (in the manual) |

## SHOWER DATA

| Source | Used for |
|---|---|
| International Meteor Organization – Meteor Shower Calendar 2026 (and 2027), www.imo.net, tables 5, 6 and 7 | Radiants, λ max, v, r, ZHR, Antihelion Source, peak dates and times |
| Rossano **IZ5TEK** – www.aripisa.it/images/pdf/scattertek.pdf | Shower data |

## LIVE RADAR DATA

| Source | Used for |
|---|---|
| Collm meteor radar, Leipzig University (LIM) and IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | Hourly meteor flux and trail heights ([Radar flux](Radar-Flux)) |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | Meteor count image |
| DL1DBC – Swan Meteor Skyview, swan.ms | Reference for the sky dome graphics |
| SM6FHZ – RadiantCalc | Polar plot with the best direction |
| Natural Earth – 1:50 million coastlines and borders, public domain, www.naturalearthdata.com | Map of Europe |
| RMOB, Radio Meteor Observatories On Line (Pierre Terrier) – www.rmob.org; monthly bulletins rmob.org/rmobtext | GRAVES 143.050 MHz observers (Venice Planetarium, Faenza, Rovereto and others) for comparison |

## GRAVES RADAR

| Source | Used for |
|---|---|
| Rob Hardenberg **PE1ITR** – *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) and *"Graves Radar Update April 2021"* – pe1itr.com/graves | Sectors, steps, 0.8 s / 3.2 s step timing |
| Bolidozor wiki, "Graves" | Arrays, sectors and beam timing |
| Wikipedia, "GRAVES (system)" | Transmitter at Broye-lès-Pesmes (47.348° N 5.515° E) |

See [GRAVES radar](GRAVES-Radar).

## OTHER REFERENCES FROM THE ARTICLE

G3WZT, DH8BQA, geekshed.co.uk, WSJT-X manual, WB2FKO (pings), IU6GIR (143.050 MHz activity), IARU Region 1 VHF Handbook.

## Constants with their source

`data/regole_sperimentali.csv` lists the constants and rules used by the program, each with its source (typical trail height, height range, Earth radius, λ³ / λ² rules, IARU ping durations, path losses, minimum signal, indicative EIRP, sporadic peak, useful distances at 432 MHz, best direction, maximum useful radiant elevation at 432 MHz, side-scatter).

> Radar data belong to their institutions. Permission must be asked before fetching them automatically in a distributed program.
