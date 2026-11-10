[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-BR) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · **Afrikaans** · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-TW)

# YA-MS – meteor scatter-voorspellings en regstreekse swermdoeltreffendheid

*deur Costantino Cerrotta IC8TEM*

**YA-MS** is 'n gratis program vir radioamateurs wat **meteor scatter (MS) op 50, 70, 144, 222 en 432 MHz** werk. Vir die werklike pad tussen jou lokator en dié van die DX-stasie bereken dit uur vir uur hoeveel elke aktiewe meteoorswerm die pad help (sy **doeltreffendheid**), van watter kant van die pad die refleksies kom (**Hot A / Hot B**), waarheen die antenna gerig moet word, en 'n eksperimentele voorspelling van die refleksies per uur, afgelei van 'n **regstreekse meteoorradar** (Collm, Duitsland). Dit loop op **Windows, Linux, Raspberry Pi en macOS** (.NET 8 + Avalonia), met 'n koppelvlak in 36 tale.

Die hoofbron is die artikel deur **C. Cerrotta IC8TEM en G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (weergawe 7). Elke formule en elke gegewe in die program noem sy bron; sien [Bronne](Sources-af).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Hemelkoepel"></a><br><sub>Hemelkoepel</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Berekening van doeltreffendheid"></a><br><sub>Berekening van doeltreffendheid</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES-radar"></a><br><sub>GRAVES-radar</sub></td>
</tr></table>

## Vir wie dit is

- Operateurs wat wil weet **wanneer** 'n meteor scatter-pad oop is en **waarheen** om te rig, verder as die algemene "die swerm piek vanaand".
- Stasies wat **lang paaie op 144 en 432 MHz** werk, waar die posisie van die radiant bepaal of 'n swerm nuttig of nutteloos is.
- Enigiemand wat **die syfers wil nagaan**: die berekeningshandleiding en die verduideliking in die program gee elke stap met sy oorsprong: 'n gepubliseerde bron, 'n kontrole op die program, of 'n keuse van die program.

## Die oortjies

Sedert weergawe 1.6 het die hoofoortjies **sub-oortjies** ('n ligter ry onder die hoofry). By opstart wys 'n welkomskerm vir 5 sekondes die Perseïede oor ESO se VLT (foto ESO/S. Guisard, CC BY 4.0).

| Oortjie | Sub-oortjie | Wat dit wys |
|---|---|---|
| **Regstreeks en intydse data** | [Regstreekse verkeer](Live-Traffic-af) | Azimutale kaart van al die ingesamelde MS-verkeer, met 'n wolk van die mees waarskynlike spore vir elke kontak, bandkleure, nuwe spots wat flikker |
| | [Radarvloed](Radar-Flux-af) | Uurlikse meteoortellings en spoorhoogtes gelees van die Collm SKiYMET-radar, Sodankylä-beeld, skatting op jou band |
| | [GRAVES-radar](GRAVES-Radar-af) | Die forward scatter-pad GRAVES → jy: bruikbare sone in die bundel, sektor en stap, volgende bundeldeurgang, hoe om te luister |
| | [Data-insameling](Data-Collection-af) | Drie telnet-clusterstrome (DX cluster, RBN, DM4X/PSKReporter) en die MS-spotfilter |
| **Voorspellingsberekening** | [Voorspellingsberekening](Sky-View-af) | Bo-aansig van die pad met Hot A / Hot B, antennalob, PREV-sones en swermdrywing; swermlys; klein hemelkoepel met die radiante en die regte antennarigtings; deursnee soos vanaf die antenna gesien |
| | [Geometrie en padverlies](Geometry-and-Path-Loss-af) | Afstand, middelpunt, elevasie, Hot A / Hot B, grense van die gemeenskaplike sone, padverlies 28–432 MHz, skakelbegroting, antenna |
| | [Berekening van doeltreffendheid](Efficiency-Calculation-af) | Oorsigkaarte, uurlikse doeltreffendheid van elke swerm met kant A/B, padindeks, DH9GCD-vergelyking, grafiek |
| | [Eksperimentele voorspellings](Experimental-Forecasts-af) | Collm-vloed geskaal na 144 MHz (of enige frekwensie) met λ^k en stasiefaktor K, 24-uur-voorspelling, RMOB-vergelyking |
| **Tegniese dokumente** | [Bronne](Sources-af) | Al die bronne; die belangrikste is die Cerrotta–Sartori-artikel |
| | [Kaart van Europese radars](European-Radar-Map-af) | Waar Collm, Sodankylä, GRAVES en CMOR relatief tot jou stasie is |
| | [Doeltreffendheid - verduideliking](Efficiency-Explanation-af) | Stap-vir-stap-dokument oor hoe die doeltreffendheid bereken word, uitvoerbaar na Word |
| [Regstreekse swerms](Live-Showers-af) | – | Gemete ZHR van die Global Meteor Network en CMOR-radiantkaarte |
| [Swerms](Showers-af) | – | IMO-katalogus met die volgende maksimum (IMO-datum en -tyd of bereken) |
| [Vierkantkaart](Grid-Square-Map-af) | – | Gewerkte en bevestigde Maidenhead-vierkante uit 'n ADIF-lêer, een oortjie per band |

Bo die oortjies is daar drie rye kontroles (jou lokator, DX-stasie, band, antenna, spoorhoogte, tyd); sien [Aan die gang](Getting-Started-af). Die knoppie **Kontroles** vou hulle weg, en die taal en kleurskema word regs bo gekies; sien [Instellings en datagids](Settings-and-Data-Folder-af).

## Kortliks

- **Werklike pad, nie vaste rigtings nie**: die doeltreffendheid word bereken vir die grootsirkelpad tussen die twee lokators (ouer programme het vier vaste rigtings gebruik).
- **Spekulêre refleksiemodel** (McKinley) op punte van die E-laag elke 15 km, met die spoorhoogte regstreeks van die Collm-radar gelees.
- **Hot A / Hot B** 150 km aan weerskante van die middelpunt (verstelbaar 30–400 km), die aanbevole een in rooi, dié wat reeds binne jou antennalob val in grys.
- **Regstreekse radar**: Collm word elke 5 minute nagegaan, slegs veranderde bronne word weer afgelaai; vanlyn werk die program voort met die laaste gestoorde data.
- **Eksperimentele** voorspelling op 50/144/432 MHz met die λ³-reël van SM6FHZ, vergelykbaar met RMOB-waarnemers.
- Alles in een **`data`**-gids langs die program: geen AppData, geen stelselgidse nie.

> Die doeltreffendheid is 'n eksperimentele model (spekulêre refleksie + onderdigte spore). Vergelyk dit met MCG_MS, MS-Soft en jou eie ervaring op die lug.

## Waar om te begin

1. [Installering](Installation-af)
2. [Aan die gang](Getting-Started-af)
3. [Probleemoplossing en gereelde vrae](Troubleshooting-FAQ-af) as iets nie werk nie.

Aflaaie: **[Releases](https://github.com/ic8tem/YA-MS/releases)** op GitHub.
