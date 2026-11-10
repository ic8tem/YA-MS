[English](Sources) · [Italiano](Sources-it) · [Deutsch](Sources-de) · [Nederlands](Sources-nl) · [Français](Sources-fr) · [Español](Sources-es) · [Português](Sources-pt) · [Português (Brasil)](Sources-pt-BR) · [Dansk](Sources-da) · [Norsk](Sources-nb) · [Svenska](Sources-sv) · [Íslenska](Sources-is) · [Eesti](Sources-et) · [Lietuvių](Sources-lt) · [Latviešu](Sources-lv) · [Polski](Sources-pl) · **Čeština** · [Magyar](Sources-hu) · [Română](Sources-ro) · [Ελληνικά](Sources-el) · [Русский](Sources-ru) · [Українська](Sources-uk) · [Türkçe](Sources-tr) · [Afrikaans](Sources-af) · [العربية](Sources-ar) · [עברית](Sources-he) · [اردو](Sources-ur) · [हिन्दी](Sources-hi) · [বাংলা](Sources-bn) · [ไทย](Sources-th) · [Bahasa Indonesia](Sources-id) · [Tagalog](Sources-tl) · [日本語](Sources-ja) · [한국어](Sources-ko) · [中文](Sources-zh) · [中文 (繁體)](Sources-zh-TW)

# Zdroje

*Karta: Technické dokumenty › Zdroje.*

[![Zdroje](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)

Karta **Zdroje** uvádí všechna díla, na nichž YA-MS stojí, seskupená jako níže (text lze označit, takže si odkazy můžete zkopírovat). Tytéž zdroje, očíslované, uzavírají manuál výpočtů (`doc/YA-MS_manuale_calcoli.docx`) a dokument [Účinnost - vysvětlení](Efficiency-Explanation-cs).

## HLAVNÍ ZDROJ

| Zdroj | Použito pro |
|---|---|
| Costantino Cerrotta **IC8TEM**, Gianluigi „Gigi“ Sartori **IV3GTH** – *„METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese“* (článek v italštině, verze 7) | Stopy ve vrstvě E ve výšce asi 90 km (radar SKiYMET), poloměr Země 6372,7955 km, vzorec pro elevaci, Hot A / Hot B, side-scatter 10–30°, útlum trasy, minimální signál −130 dBm, délky pingů podle IARU, maximum sporadických meteorů v 06 UTC |

## ÚČINNOST: VÝPOČET A TEORIE

| Zdroj | Použito pro |
|---|---|
| Ilkka Yrjölä **OH5IY** – MS-Soft, www.kolumbus.fi/oh5iy (historický web) | Koncept účinnosti roje; průměrný útlum trasy 200 dB |
| Wilhelm Rauh **DL5MCG** – MCG_MS, MS Efficiency Calculator v1.61, qsl.net/dl5mcg | Účinnost ve čtyřech pevných směrech (srovnání) |
| Ingolf **SM6FHZ** – *„432 MHz Meteorscatter, Challenges and Techniques“*, 45th Nordic VUSHF, květen 2025 | Pravidla λ³ a λ², střed trasy, nejlepší směr (az radiantu ±90°) |
| D.W.R. **McKinley** – *Meteor Science and Engineering*, McGraw-Hill, 1961 | Zrcadlový odraz, rovnice podhusté stopy |
| John **GM8JBJ** – Meteor scatter path loss, hamradio.engineering (podle Kaiser & Closs 1952) | Útlum trasy 172–190 dB vypočtený Johnem Worsnopem **G4BAO** (disertační práce), asi o 6 dB méně u stop rovnoběžných s trasou; vlastní tabulka stránky se 182 dB se nepoužívá (viz [Geometrie a útlum](Geometry-and-Path-Loss-cs)) |
| Shelby **W8WN** – qsl.net/w8wn/hscw (tabulka odklonů z AMS Bulletin 203) | Optimální elevace a odklon, hot spoty 50–150 km |
| **LZ2HV** – MSHV | Hot A / Hot B (srovnání; v manuálu) |
| Klaus von der Heide **DJ5HG** – QTFGUI a manuál „QTFGUI Help“ (2007) | Kuželový zákon rozptylu; testovací případ Hamburk – Barcelona s Kvadrantidami použitý k ověření modelu |
| Jens **DF5HC** – *„Meteorscatter auf UKW“*, konference DARC, leden 2018 | Vzorec nejlepšího směru od **DH9GCD**; kuželový rozptyl a volba HOT-A / HOT-B od DJ5HG; užitečný radiant 20–70°; nejlepší vzdálenost 1300–1500 km; sporadické meteory od KB0VUK |
| Günter Hoch **DL6WU** – zisk v závislosti na délce ráhna dlouhých Yagi, uvádí W8IO (w8io.com) | G(dBi) = 7,773 log(L/λ) + 11,43 |
| J.D. **Kraus** – *Antennas*, McGraw-Hill | G = 41253 / (θE·θH) |
| L.B. Cebik **W4RNL** – *Long-Boom Yagi Rules of Thumb: A Comparison with Modeling Data*; *Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2* (Yagi VK3AUU od Davida Tannera) | Simulace NEC použité k ověření křivky zisku a korekci vodorovného laloku (0,93 × Kraus) |
| John Drew **VK5DJ** – Yagi Calculator | Odhady zisku pro varianty VK3AUU, WA2PHW a DJ9BV |
| J. **Meeus** – *Astronomical Algorithms*, 2. vyd., Willmann-Bell, 1998 | Juliánské datum, hvězdný čas, sluneční délka, azimut/elevace (v manuálu) |

## DATA ROJŮ

| Zdroj | Použito pro |
|---|---|
| International Meteor Organization – Meteor Shower Calendar 2026 (a 2027), www.imo.net, tabulky 5, 6 a 7 | Radianty, λ max, v, r, ZHR, Antihelion Source, data a časy maxim |
| Rossano **IZ5TEK** – www.aripisa.it/images/pdf/scattertek.pdf | Data rojů |

## ŽIVÁ RADAROVÁ DATA

| Zdroj | Použito pro |
|---|---|
| Meteorický radar Collm, Lipská univerzita (LIM) a IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | Hodinový tok meteorů a výšky stop ([Tok z radaru](Radar-Flux-cs)) |
| Geofyzikální observatoř Sodankylä – sgo.fi/Data/RealTime/meteorRadar.php | Obrázek s počty meteorů |
| DL1DBC – Swan Meteor Skyview, swan.ms | Vzor pro grafiku nebeské klenby |
| SM6FHZ – RadiantCalc | Polární diagram s nejlepším směrem |
| Natural Earth – pobřeží a hranice v měřítku 1 : 50 milionů, volné dílo, www.naturalearthdata.com | Mapa Evropy |
| RMOB, Radio Meteor Observatories On Line (Pierre Terrier) – www.rmob.org; měsíční bulletiny rmob.org/rmobtext | Pozorovatelé GRAVES na 143,050 MHz (planetárium v Benátkách, Faenza, Rovereto a další) pro srovnání |

## RADAR GRAVES

| Zdroj | Použito pro |
|---|---|
| Rob Hardenberg **PE1ITR** – *„The 143.050 MHz Graves Radar, a VHF Beacon“* (DUBUS 4/2007) a *„Graves Radar Update April 2021“* – pe1itr.com/graves | Sektory, kroky, časování kroku 0,8 s / 3,2 s |
| Wiki Bolidozor, „Graves“ | Anténní pole, sektory a časování svazku |
| Wikipedie, „GRAVES (system)“ | Vysílač v Broye-lès-Pesmes (47,348° s. š., 5,515° v. d.) |

Viz [Radar GRAVES](GRAVES-Radar-cs).

## DALŠÍ ODKAZY Z ČLÁNKU

G3WZT, DH8BQA, geekshed.co.uk, manuál WSJT-X, WB2FKO (pingy), IU6GIR (aktivita na 143,050 MHz), IARU Region 1 VHF Handbook.

## Konstanty se zdrojem

`data/regole_sperimentali.csv` uvádí konstanty a pravidla, která program používá, každé se svým zdrojem (typická výška stop, rozsah výšek, poloměr Země, pravidla λ³ / λ², délky pingů podle IARU, útlumy trasy, minimální signál, orientační EIRP, maximum sporadických meteorů, užitečné vzdálenosti na 432 MHz, nejlepší směr, maximální užitečná elevace radiantu na 432 MHz, side-scatter).

> Radarová data patří svým institucím. Před jejich automatickým stahováním v distribuovaném programu je třeba požádat o svolení.
