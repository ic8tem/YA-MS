[English](Sources) · [Italiano](Sources-it) · [Deutsch](Sources-de) · [Nederlands](Sources-nl) · [Français](Sources-fr) · [Español](Sources-es) · [Português](Sources-pt) · [Português (Brasil)](Sources-pt-BR) · [Dansk](Sources-da) · **Norsk** · [Svenska](Sources-sv) · [Íslenska](Sources-is) · [Eesti](Sources-et) · [Lietuvių](Sources-lt) · [Latviešu](Sources-lv) · [Polski](Sources-pl) · [Čeština](Sources-cs) · [Magyar](Sources-hu) · [Română](Sources-ro) · [Ελληνικά](Sources-el) · [Русский](Sources-ru) · [Українська](Sources-uk) · [Türkçe](Sources-tr) · [Afrikaans](Sources-af) · [العربية](Sources-ar) · [עברית](Sources-he) · [اردو](Sources-ur) · [हिन्दी](Sources-hi) · [বাংলা](Sources-bn) · [ไทย](Sources-th) · [Bahasa Indonesia](Sources-id) · [Tagalog](Sources-tl) · [日本語](Sources-ja) · [한국어](Sources-ko) · [中文](Sources-zh) · [中文 (繁體)](Sources-zh-TW)

# Kilder

*Fane: Tekniske dokumenter › Kilder.*

[![Kilder](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)

Fanen **Kilder** lister alle verkene YA-MS bygger på, gruppert som nedenfor (teksten kan merkes, så du kan kopiere referansene). De samme kildene, nummerert, avslutter beregningshåndboken (`doc/YA-MS_manuale_calcoli.docx`) og dokumentet [Effektivitet - forklaring](Efficiency-Explanation-nb).

## HOVEDKILDE

| Kilde | Brukt til |
|---|---|
| Costantino Cerrotta **IC8TEM**, Gianluigi "Gigi" Sartori **IV3GTH** – *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (artikkel på italiensk, versjon 7) | Spor i E-laget i ca. 90 km høyde (SKiYMET-radar), jordradius 6372,7955 km, elevasjonsformel, Hot A / Hot B, side-scatter 10–30°, strekningsdemping, minste signal −130 dBm, IARU-pingvarigheter, sporadisk maksimum kl. 06 UTC |

## EFFEKTIVITET: BEREGNING OG TEORI

| Kilde | Brukt til |
|---|---|
| Ilkka Yrjölä **OH5IY** – MS-Soft, www.kolumbus.fi/oh5iy (historisk nettsted) | Begrepet svermeffektivitet; gjennomsnittlig strekningsdemping 200 dB |
| Wilhelm Rauh **DL5MCG** – MCG_MS, MS Efficiency Calculator v1.61, qsl.net/dl5mcg | Effektivitet på fire faste retninger (sammenligning) |
| Ingolf **SM6FHZ** – *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, mai 2025 | λ³- og λ²-reglene, midtpunkt, beste retning (radiantens az ±90°) |
| D.W.R. **McKinley** – *Meteor Science and Engineering*, McGraw-Hill, 1961 | Speilrefleksjon, likningen for underdense spor |
| John **GM8JBJ** – Meteor scatter path loss, hamradio.engineering (etter Kaiser & Closs 1952) | Strekningsdemping på 172–190 dB beregnet av John Worsnop **G4BAO** (doktoravhandling), omkring 6 dB mindre for spor på linje med strekningen; sidens egen tabell med 182 dB brukes ikke (se [Geometri og demping](Geometry-and-Path-Loss-nb)) |
| Shelby **W8WN** – qsl.net/w8wn/hscw (forskyvningstabellen i AMS Bulletin 203) | Optimal elevasjon og forskyvning, hot spots 50–150 km |
| **LZ2HV** – MSHV | Hot A / Hot B (sammenligning; i håndboken) |
| Klaus von der Heide **DJ5HG** – QTFGUI og håndboken "QTFGUI Help" (2007) | Loven om kjegleformet spredning; testtilfellet Hamburg – Barcelona under Kvadrantidene, brukt til å verifisere modellen |
| Jens **DF5HC** – *"Meteorscatter auf UKW"*, DARC-konferanse, januar 2018 | Formel for beste retning fra **DH9GCD**; kjegleformet spredning og valg av HOT-A / HOT-B fra DJ5HG; nyttig radiant 20–70°; beste avstand 1300–1500 km; sporadiske meteorer fra KB0VUK |
| Günter Hoch **DL6WU** – forsterkning mot bomlengde for lange Yagier, gjengitt av W8IO (w8io.com) | G(dBi) = 7,773 log(L/λ) + 11,43 |
| J.D. **Kraus** – *Antennas*, McGraw-Hill | G = 41253 / (θE·θH) |
| L.B. Cebik **W4RNL** – *Long-Boom Yagi Rules of Thumb: A Comparison with Modeling Data*; *Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2* (VK3AUU-Yagier av David Tanner) | NEC-simuleringer brukt til å verifisere forsterkningskurven og korrigere den horisontale loben (0,93 × Kraus) |
| John Drew **VK5DJ** – Yagi Calculator | Forsterkningsestimater for variantene VK3AUU, WA2PHW og DJ9BV |
| J. **Meeus** – *Astronomical Algorithms*, 2. utg., Willmann-Bell, 1998 | Juliansk dag, stjernetid, solens lengde, asimut/elevasjon (i håndboken) |

## SVERMDATA

| Kilde | Brukt til |
|---|---|
| International Meteor Organization – Meteor Shower Calendar 2026 (og 2027), www.imo.net, tabell 5, 6 og 7 | Radianter, λ max, v, r, ZHR, Antihelion-kilden, datoer og tidspunkter for maksima |
| Rossano **IZ5TEK** – www.aripisa.it/images/pdf/scattertek.pdf | Svermdata |

## RADARDATA DIREKTE

| Kilde | Brukt til |
|---|---|
| Collm meteorradar, Universitetet i Leipzig (LIM) og IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | Meteorfluks per time og sporhøyder ([Radarfluks](Radar-Flux-nb)) |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | Bilde med meteortellinger |
| DL1DBC – Swan Meteor Skyview, swan.ms | Forbilde for grafikken til himmelhvelvingen |
| SM6FHZ – RadiantCalc | Polardiagram med beste retning |
| Natural Earth – kystlinjer og grenser 1:50 millioner, fritt brukbart (public domain), www.naturalearthdata.com | Europakart |
| RMOB, Radio Meteor Observatories On Line (Pierre Terrier) – www.rmob.org; månedlige bulletiner rmob.org/rmobtext | GRAVES-observatører på 143,050 MHz (Planetariet i Venezia, Faenza, Rovereto og andre) til sammenligning |

## GRAVES-RADAR

| Kilde | Brukt til |
|---|---|
| Rob Hardenberg **PE1ITR** – *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) og *"Graves Radar Update April 2021"* – pe1itr.com/graves | Sektorer, steg, stegtiming 0,8 s / 3,2 s |
| Bolidozor wiki, "Graves" | Antennegrupper, sektorer og stråletiming |
| Wikipedia, "GRAVES (system)" | Sender i Broye-lès-Pesmes (47,348° N 5,515° E) |

Se [Radar GRAVES](GRAVES-Radar-nb).

## ANDRE REFERANSER FRA ARTIKKELEN

G3WZT, DH8BQA, geekshed.co.uk, WSJT-X-manualen, WB2FKO (pinger), IU6GIR (aktivitet på 143,050 MHz), IARU Region 1 VHF Handbook.

## Konstanter med kilde

`data/regole_sperimentali.csv` lister konstantene og reglene programmet bruker, hver med sin kilde (typisk sporhøyde, høydeområde, jordradius, λ³- / λ²-reglene, IARU-pingvarigheter, strekningsdemping, minste signal, veiledende EIRP, sporadisk maksimum, nyttige avstander på 432 MHz, beste retning, maksimal nyttig radiantelevasjon på 432 MHz, side-scatter).

> Radardataene tilhører de respektive institusjonene. Det må bes om tillatelse før de hentes automatisk i et distribuert program.
