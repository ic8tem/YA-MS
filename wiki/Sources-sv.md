[English](Sources) · [Italiano](Sources-it) · [Deutsch](Sources-de) · [Nederlands](Sources-nl) · [Français](Sources-fr) · [Español](Sources-es) · [Português](Sources-pt) · [Português (Brasil)](Sources-pt-BR) · [Dansk](Sources-da) · [Norsk](Sources-nb) · **Svenska** · [Íslenska](Sources-is) · [Eesti](Sources-et) · [Lietuvių](Sources-lt) · [Latviešu](Sources-lv) · [Polski](Sources-pl) · [Čeština](Sources-cs) · [Magyar](Sources-hu) · [Română](Sources-ro) · [Ελληνικά](Sources-el) · [Русский](Sources-ru) · [Українська](Sources-uk) · [Türkçe](Sources-tr) · [Afrikaans](Sources-af) · [العربية](Sources-ar) · [עברית](Sources-he) · [اردو](Sources-ur) · [हिन्दी](Sources-hi) · [বাংলা](Sources-bn) · [ไทย](Sources-th) · [Bahasa Indonesia](Sources-id) · [Tagalog](Sources-tl) · [日本語](Sources-ja) · [한국어](Sources-ko) · [中文](Sources-zh) · [中文 (繁體)](Sources-zh-TW)

# Källor

*Flik: Tekniska dokument › Källor.*

[![Källor](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)

Fliken **Källor** listar alla verk som YA-MS bygger på, grupperade enligt nedan (texten är markerbar, så att du kan kopiera referenserna). Samma källor, numrerade, avslutar beräkningshandboken (`doc/YA-MS_manuale_calcoli.docx`) och dokumentet [Effektivitet - förklaring](Efficiency-Explanation-sv).

## HUVUDKÄLLA

| Källa | Används för |
|---|---|
| Costantino Cerrotta **IC8TEM**, Gianluigi "Gigi" Sartori **IV3GTH** – *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (artikel på italienska, version 7) | Spår i E-skiktet på omkring 90 km (SKiYMET-radar), jordradie 6372,7955 km, elevationsformeln, Hot A / Hot B, side-scatter 10–30°, sträckdämpning, minsta signal −130 dBm, IARU:s pinglängder, sporadiskt maximum kl. 06 UTC |

## EFFEKTIVITET: BERÄKNING OCH TEORI

| Källa | Används för |
|---|---|
| Ilkka Yrjölä **OH5IY** – MS-Soft, www.kolumbus.fi/oh5iy (historisk webbplats) | Begreppet svärmeffektivitet; genomsnittlig sträckdämpning 200 dB |
| Wilhelm Rauh **DL5MCG** – MCG_MS, MS Efficiency Calculator v1.61, qsl.net/dl5mcg | Effektivitet i fyra fasta riktningar (jämförelse) |
| Ingolf **SM6FHZ** – *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, maj 2025 | Reglerna λ³ och λ², mittpunkten, bästa riktning (radiantens az ±90°) |
| D.W.R. **McKinley** – *Meteor Science and Engineering*, McGraw-Hill, 1961 | Spegelreflexion, ekvationen för underdensa spår |
| John **GM8JBJ** – Meteor scatter path loss, hamradio.engineering (från Kaiser & Closs 1952) | Sträckdämpning på 172–190 dB beräknad av John Worsnop **G4BAO** (doktorsavhandling), omkring 6 dB mindre för spår i linje med sträckan; sidans egen tabell med 182 dB används inte (se [Geometri och dämpning](Geometry-and-Path-Loss-sv)) |
| Shelby **W8WN** – qsl.net/w8wn/hscw (förskjutningstabellen i AMS Bulletin 203) | Optimal elevation och förskjutning, hot spots på 50–150 km |
| **LZ2HV** – MSHV | Hot A / Hot B (jämförelse; i handboken) |
| Klaus von der Heide **DJ5HG** – QTFGUI och handboken "QTFGUI Help" (2007) | Lagen för cone scattering; testfallet Hamburg – Barcelona under Quadrantiderna, använt för att verifiera modellen |
| Jens **DF5HC** – *"Meteorscatter auf UKW"*, DARC-konferensen, januari 2018 | Formeln för bästa riktning av **DH9GCD**; cone scattering och valet HOT-A / HOT-B av DJ5HG; användbar radiant 20–70°; bästa avstånd 1300–1500 km; sporadiska meteorer enligt KB0VUK |
| Günter Hoch **DL6WU** – förstärkning som funktion av bomlängd för långa yagis, återgiven av W8IO (w8io.com) | G(dBi) = 7.773 log(L/λ) + 11.43 |
| J.D. **Kraus** – *Antennas*, McGraw-Hill | G = 41253 / (θE·θH) |
| L.B. Cebik **W4RNL** – *Long-Boom Yagi Rules of Thumb: A Comparison with Modeling Data*; *Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2* (VK3AUU-yagis av David Tanner) | NEC-simuleringar använda för att verifiera förstärkningskurvan och korrigera den horisontella loben (0,93 × Kraus) |
| John Drew **VK5DJ** – Yagi Calculator | Förstärkningsuppskattningar för varianterna VK3AUU, WA2PHW och DJ9BV |
| J. **Meeus** – *Astronomical Algorithms*, 2nd ed., Willmann-Bell, 1998 | Juliansk dag, stjärntid, solens longitud, azimut/elevation (i handboken) |

## SVÄRMDATA

| Källa | Används för |
|---|---|
| International Meteor Organization – Meteor Shower Calendar 2026 (och 2027), www.imo.net, tabell 5, 6 och 7 | Radianter, λ max, v, r, ZHR, Antihelion Source, datum och tider för maximum |
| Rossano **IZ5TEK** – www.aripisa.it/images/pdf/scattertek.pdf | Svärmdata |

## RADARDATA I REALTID

| Källa | Används för |
|---|---|
| Collm meteor radar, Leipzigs universitet (LIM) och IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | Meteorflöde per timme och spårhöjder ([Radarflöde](Radar-Flux-sv)) |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | Bild med meteorräkning |
| DL1DBC – Swan Meteor Skyview, swan.ms | Referens för himlavalvets grafik |
| SM6FHZ – RadiantCalc | Polärdiagram med bästa riktning |
| Natural Earth – kustlinjer och gränser i skala 1:50 miljoner, public domain, www.naturalearthdata.com | Europakarta |
| RMOB, Radio Meteor Observatories On Line (Pierre Terrier) – www.rmob.org; månadsbulletiner rmob.org/rmobtext | Observatörer av GRAVES på 143,050 MHz (planetariet i Venedig, Faenza, Rovereto med flera) för jämförelse |

## GRAVES-RADAR

| Källa | Används för |
|---|---|
| Rob Hardenberg **PE1ITR** – *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) och *"Graves Radar Update April 2021"* – pe1itr.com/graves | Sektorer, steg, stegtider 0,8 s / 3,2 s |
| Bolidozor-wikin, "Graves" | Antenner, sektorer och lobens tidsschema |
| Wikipedia, "GRAVES (system)" | Sändaren i Broye-lès-Pesmes (47.348° N 5.515° E) |

Se [GRAVES-radar](GRAVES-Radar-sv).

## ÖVRIGA REFERENSER I ARTIKELN

G3WZT, DH8BQA, geekshed.co.uk, handboken till WSJT-X, WB2FKO (pingar), IU6GIR (aktivitet på 143,050 MHz), IARU Region 1 VHF Handbook.

## Konstanter med källa

`data/regole_sperimentali.csv` listar de konstanter och regler som programmet använder, var och en med sin källa (typisk spårhöjd, höjdintervall, jordradie, reglerna λ³ / λ², IARU:s pinglängder, sträckdämpningar, minsta signal, vägledande EIRP, sporadiskt maximum, användbara avstånd på 432 MHz, bästa riktning, högsta användbara radiantelevation på 432 MHz, side-scatter).

> Radardata tillhör sina institutioner. Tillstånd måste begäras innan de hämtas automatiskt i ett program som distribueras.
