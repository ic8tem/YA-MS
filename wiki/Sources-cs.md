LANGBAR

# Zdroje

*Karta: Technické dokumenty › Zdroje.*

[![Zdroje](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)

Karta **Zdroje** uvádí všechna díla, na kterých je YA-MS postaven, seskupená jako níže (text lze označit, takže můžete odkazy kopírovat). Tytéž zdroje, číslované, uzavírají výpočetní příručku (`doc/YA-MS_manuale_calcoli.docx`) a dokument [Účinnost - vysvětlení](Efficiency-Explanation-cs).

## HLAVNÍ ZDROJ

| Zdroj | Použito pro |
|---|---|
| Costantino Cerrotta **IC8TEM**, Gianluigi „Gigi“ Sartori **IV3GTH** – *„METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese“* (článek v italštině, verze 7) | Stopy ve vrstvě E ve výšce asi 90 km (radar SKiYMET), poloměr Země 6372,7955 km, vzorec elevace, Hot A / Hot B, side-scatter 10–30°, útlum trasy 182–200 dB, minimální signál −130 dBm, délky pingů podle IARU, maximum sporadických meteorů v 06 UTC |

## ÚČINNOST: VÝPOČET A TEORIE

| Zdroj | Použito pro |
|---|---|
| Ilkka Yrjölä **OH5IY** – MS-Soft, www.kolumbus.fi/oh5iy (historický web) | Pojem účinnosti roje; průměrný útlum trasy 200 dB |
| Wilhelm Rauh **DL5MCG** – MCG_MS, MS Efficiency Calculator v1.61, qsl.net/dl5mcg | Účinnost ve čtyřech pevných směrech (srovnání) |
| Ingolf **SM6FHZ** – *„432 MHz Meteorscatter, Challenges and Techniques“*, 45. Nordic VUSHF, květen 2025 | Pravidla λ³ a λ², střed trasy, nejlepší směr (az. radiantu ±90°) |
| D. W. R. **McKinley** – *Meteor Science and Engineering*, McGraw-Hill, 1961 | Zrcadlový odraz, rovnice podhusté stopy |
| John **GM8JBJ** – Meteor scatter path loss, hamradio.engineering (podle Kaiser & Closs 1952) | Minimální útlum trasy 182 dB |
| Shelby **W8WN** – qsl.net/w8wn/hscw (tabulka odsazení z AMS Bulletin 203) | Optimální elevace a odsazení, hot spoty 50–150 km |
| **LZ2HV** – MSHV | Hot A / Hot B (srovnání; v příručce) |
| Klaus von der Heide **DJ5HG** – QTFGUI a příručka „QTFGUI Help“ (2007) | Zákon kuželového rozptylu; testovací případ Hamburk – Barcelona s Kvadrantidami použitý k ověření modelu |
| Jens **DF5HC** – *„Meteorscatter auf UKW“*, konference DARC, leden 2018 | Vzorec nejlepšího směru od **DH9GCD**; kuželový rozptyl a volba HOT-A / HOT-B podle DJ5HG; užitečný radiant 20–70°; nejlepší vzdálenost 1300–1500 km; sporadické meteory podle KB0VUK |
| Günter Hoch **DL6WU** – zisk v závislosti na délce ráhna dlouhých antén Yagi, podle W8IO (w8io.com) | G(dBi) = 7,773 log(L/λ) + 11,43 |
| J. D. **Kraus** – *Antennas*, McGraw-Hill | G = 41253 / (θE·θH) |
| L. B. Cebik **W4RNL** – *Long-Boom Yagi Rules of Thumb: A Comparison with Modeling Data*; *Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2* (antény Yagi VK3AUU od Davida Tannera) | Simulace NEC použité k ověření křivky zisku a ke korekci vodorovného laloku (0,93 × Kraus) |
| John Drew **VK5DJ** – Yagi Calculator | Odhady zisku pro varianty VK3AUU, WA2PHW a DJ9BV |
| J. **Meeus** – *Astronomical Algorithms*, 2. vyd., Willmann-Bell, 1998 | Juliánské datum, hvězdný čas, sluneční délka, azimut/elevace (v příručce) |

## ÚDAJE O ROJÍCH

| Zdroj | Použito pro |
|---|---|
| International Meteor Organization – Meteor Shower Calendar 2026 (a 2027), www.imo.net, tabulky 5, 6 a 7 | Radianty, λ max, v, r, ZHR, Antihelionový zdroj, data a časy maxim |
| Philip **G0ISW** – www.qsl.net/g0isw/g0iswms.htm | Maximální rádiové hodinové frekvence |
| Rossano **IZ5TEK** – www.aripisa.it/images/pdf/scattertek.pdf | Údaje o rojích |

## ŽIVÁ DATA RADARŮ

| Zdroj | Použito pro |
|---|---|
| Meteorický radar Collm, Univerzita Lipsko (LIM) a IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | Hodinový tok meteorů a výšky stop ([Tok z radaru](Radar-Flux-cs)) |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | Snímek počtů meteorů |
| DL1DBC – Swan Meteor Skyview, swan.ms | Předloha grafiky nebeské klenby |
| SM6FHZ – RadiantCalc | Polární graf s nejlepším směrem |
| Natural Earth – pobřeží a hranice 1 : 50 milionům, volné dílo, www.naturalearthdata.com | Mapa Evropy |
| RMOB, Radio Meteor Observatories On Line (Pierre Terrier) – www.rmob.org; měsíční bulletiny rmob.org/rmobtext | Pozorovatelé GRAVES na 143,050 MHz (planetárium v Benátkách, Faenza, Rovereto a další) pro srovnání |

## RADAR GRAVES

| Zdroj | Použito pro |
|---|---|
| Rob Hardenberg **PE1ITR** – *„The 143.050 MHz Graves Radar, a VHF Beacon“* (DUBUS 4/2007) a *„Graves Radar Update April 2021“* – pe1itr.com/graves | Sektory, kroky, časování kroků 0,8 s / 3,2 s |
| Wiki Bolidozor, „Graves“ | Soustavy, sektory a časování svazku |
| Wikipedie, „GRAVES (system)“ | Vysílač v Broye-lès-Pesmes (47,348° s. š. 5,515° v. d.) |

Viz [Radar GRAVES](GRAVES-Radar-cs).

## DALŠÍ ODKAZY Z ČLÁNKU

G3WZT, DH8BQA, geekshed.co.uk, příručka WSJT-X, WB2FKO (pingy), IU6GIR (aktivita na 143,050 MHz), IARU Region 1 VHF Handbook.

## Konstanty s jejich zdrojem

`data/regole_sperimentali.csv` uvádí konstanty a pravidla, která program používá, každé se svým zdrojem (typická výška stopy, rozsah výšek, poloměr Země, pravidla λ³ / λ², délky pingů podle IARU, útlumy trasy, minimální signál, orientační EIRP, maximum sporadických meteorů, užitečné vzdálenosti na 432 MHz, nejlepší směr, maximální užitečná elevace radiantu na 432 MHz, side-scatter).

> Data radarů patří příslušným institucím. Před jejich automatickým stahováním v distribuovaném programu je třeba požádat o svolení.
