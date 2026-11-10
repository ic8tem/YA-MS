[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · **Lietuvių** · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [ไทย](Home-th) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – meteor scatter prognozės ir srautų efektyvumas realiuoju laiku

*parengė Costantino Cerrotta IC8TEM*

**YA-MS** – nemokama programa radijo mėgėjams, dirbantiems **meteor scatter (MS) ryšiais 50, 70, 144, 222 ir 432 MHz juostose**. Realiai trasai tarp jūsų ir korespondento lokatorių ji kas valandą apskaičiuoja, kiek kiekvienas aktyvus meteorų srautas padeda trasai (jo **efektyvumą**), iš kurios trasos pusės ateina atspindžiai (**Hot A / Hot B**), kur nukreipti anteną, ir eksperimentinę atspindžių per valandą prognozę, gautą iš **realiuoju laiku veikiančio meteorų radaro** (Collm, Vokietija). Programa veikia **Windows, Linux ir macOS** sistemose (.NET 8 + Avalonia), 36 sąsajos kalbomis.

Pagrindinis šaltinis – **C. Cerrotta IC8TEM ir G. Sartori IV3GTH** straipsnis *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (7 versija). Kiekviena programos formulė ir kiekvienas duomuo nurodo savo šaltinį; žr. [Šaltiniai](Sources-lt).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Dangaus skliautas"></a><br><sub>Dangaus skliautas</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Efektyvumo skaičiavimas"></a><br><sub>Efektyvumo skaičiavimas</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES radaras"></a><br><sub>GRAVES radaras</sub></td>
</tr></table>

## Kam ji skirta

- Operatoriams, norintiems žinoti, **kada** meteor scatter trasa atvira ir **kur** nukreipti anteną, o ne tik bendrą „srauto maksimumas šiąnakt“.
- Stotims, dirbančioms **ilgomis trasomis 144 ir 432 MHz juostose**, kur radianto padėtis lemia, ar srautas naudingas, ar ne.
- Visiems, kurie nori **patikrinti skaičius**: skaičiavimų vadovas ir paaiškinimas programoje pateikia kiekvieną žingsnį su jo kilme – paskelbtu šaltiniu, programoje atlikta patikra arba programos sprendimu.

## Kortelės

Nuo 1.6 versijos pagrindinės kortelės turi **vidines korteles** (šviesesnė eilutė po pagrindine). Paleidžiant 5 sekundes rodomas pradžios ekranas su Perseidais virš ESO VLT (nuotrauka ESO/S. Guisard, CC BY 4.0).

| Kortelė | Vidinė kortelė | Ką rodo |
|---|---|---|
| **Tiesiogiai ir realiojo laiko duomenys** | [Eismas realiuoju laiku](Live-Traffic-lt) | Azimutinis viso surinkto MS eismo žemėlapis, kiekvienam ryšiui – labiausiai tikėtinų pėdsakų debesis, juostų spalvos, nauji spotai mirksi |
| | [Radaro srautas](Radar-Flux-lt) | Iš Collm SKiYMET radaro nuskaityti valandiniai meteorų skaičiai ir pėdsakų aukščiai, Sodankylä vaizdas, įvertis jūsų juostai |
| | [GRAVES radaras](GRAVES-Radar-lt) | Forward scatter trasa GRAVES → jūs: naudingoji zona pluošte, sektorius ir žingsnis, kitas pluošto praėjimas, kaip klausytis |
| | [Duomenų rinkimas](Data-Collection-lt) | Trys telnet klasterių srautai (DX cluster, RBN, DM4X/PSKReporter) ir MS spotų filtras |
| **Prognozės skaičiavimas** | [Prognozės skaičiavimas](Sky-View-lt) | Trasos plano žemėlapis su Hot A / Hot B, antenos lapeliu, PREV zonomis ir srauto slinkimu; srautų sąrašas; mažas dangaus skliautas su radiantais ir tinkamomis antenos kryptimis; pjūvis, matomas iš antenos |
| | [Geometrija ir slopinimas](Geometry-and-Path-Loss-lt) | Atstumas, vidurio taškas, elevacija, Hot A / Hot B, bendrosios zonos ribos, slopinimas 28–432 MHz, ryšio biudžetas, antena |
| | [Efektyvumo skaičiavimas](Efficiency-Calculation-lt) | Apžvalgos skydeliai, kiekvieno srauto valandinis efektyvumas su puse A/B, trasos indeksas, DH9GCD palyginimas, grafikas |
| | [Eksperimentinės prognozės](Experimental-Forecasts-lt) | Collm srautas, perskaičiuotas į 144 MHz (ar bet kurį dažnį) su λ^k ir stoties koeficientu K, 24 valandų prognozė, palyginimas su RMOB |
| **Techniniai dokumentai** | [Šaltiniai](Sources-lt) | Visi šaltiniai; pagrindinis – Cerrotta–Sartori straipsnis |
| | [Europos radarų žemėlapis](European-Radar-Map-lt) | Kur yra Collm, Sodankylä, GRAVES ir CMOR jūsų stoties atžvilgiu |
| | [Efektyvumas - paaiškinimas](Efficiency-Explanation-lt) | Dokumentas žingsnis po žingsnio apie tai, kaip skaičiuojamas efektyvumas, eksportuojamas į Word |
| [Srautai realiuoju laiku](Live-Showers-lt) | – | Global Meteor Network išmatuoti ZHR ir CMOR radiantų žemėlapiai |
| [Srautai](Showers-lt) | – | IMO katalogas su kitu maksimumu (IMO data ir laikas arba apskaičiuotas) |
| [Kvadratų žemėlapis](Grid-Square-Map-lt) | – | Iš ADIF failo nuskaityti dirbti ir patvirtinti Maidenhead kvadratai, kiekviena juosta atskiroje kortelėje |

Virš kortelių yra trys valdymo eilutės (jūsų lokatorius, korespondentas, juosta, antena, pėdsakų aukštis, laikas); žr. [Pradžia](Getting-Started-lt). Mygtukas **Valdymas** jas suskleidžia, o kalba ir spalvų schema pasirenkamos viršuje dešinėje; žr. [Nustatymai ir duomenų aplankas](Settings-and-Data-Folder-lt).

## Trumpai

- **Reali trasa, ne fiksuotos kryptys**: efektyvumas skaičiuojamas didžiojo apskritimo trasai tarp dviejų lokatorių (senesnės programos naudojo keturias fiksuotas kryptis).
- **Veidrodinio atspindžio modelis** (McKinley) E sluoksnio taškuose kas 15 km, pėdsakų aukštis realiuoju laiku nuskaitomas iš Collm radaro.
- **Hot A / Hot B** 150 km abipus vidurio taško (reguliuojama 30–400 km), rekomenduojamas – raudonas, jau antenos lapelyje esantys – pilki.
- **Radaras realiuoju laiku**: Collm tikrinamas kas 5 minutes, iš naujo atsisiunčiami tik pasikeitę šaltiniai; be tinklo programa toliau veikia su paskutiniais išsaugotais duomenimis.
- **Eksperimentinė** prognozė 50/144/432 MHz juostose pagal SM6FHZ λ³ taisyklę, palyginama su RMOB stebėtojais.
- Viskas viename **`data`** aplanke šalia programos: jokio AppData, jokių sisteminių aplankų.

> Efektyvumas yra eksperimentinis modelis (veidrodinis atspindys + retieji pėdsakai). Palyginkite jį su MCG_MS, MS-Soft ir savo patirtimi eteryje.

## Nuo ko pradėti

1. [Diegimas](Installation-lt)
2. [Pradžia](Getting-Started-lt)
3. [Trikčių šalinimas ir DUK](Troubleshooting-FAQ-lt), jei kas nors neveikia.

Atsisiuntimai: **[Releases](https://github.com/ic8tem/YA-MS/releases)** GitHub svetainėje.
