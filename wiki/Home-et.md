[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · **Eesti** · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [ไทย](Home-th) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – meteor scatteri prognoosid ja meteoorivoolude efektiivsus otse

*koostanud Costantino Cerrotta IC8TEM*

**YA-MS** on tasuta programm raadioamatööridele, kes töötavad **meteor scatteriga (MS) sagedustel 50, 70, 144, 222 ja 432 MHz**. Sinu lokaatori ja korrespondendi lokaatori vahelise tegeliku trassi jaoks arvutab see tund-tunnilt, kui palju iga aktiivne meteoorivool trassi aitab (selle **efektiivsus**), kummalt poolt trassi peegeldused tulevad (**Hot A / Hot B**), kuhu antenn suunata, ning eksperimentaalse prognoosi peegelduste arvu kohta tunnis, mis tuletatakse **otse töötava meteoorradari** (Collm, Saksamaa) andmetest. See töötab **Windowsis, Linuxis ja macOS-is** (.NET 8 + Avalonia), 36 kasutajaliidese keeles.

Peamine allikas on **C. Cerrotta IC8TEM-i ja G. Sartori IV3GTH** artikkel *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (versioon 7). Iga programmis kasutatud valem ja andmeüksus viitab oma allikale; vt [Allikad](Sources-et).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Taevavõlv"></a><br><sub>Taevavõlv</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Efektiivsuse arvutus"></a><br><sub>Efektiivsuse arvutus</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVESi radar"></a><br><sub>GRAVESi radar</sub></td>
</tr></table>

## Kellele see on mõeldud

- Operaatoritele, kes tahavad teada, **millal** meteor scatteri trass on avatud ja **kuhu** antenn suunata, mitte üksnes üldist "meteoorivoolu maksimum on täna öösel".
- Jaamadele, kes töötavad **pikkadel trassidel 144 ja 432 MHz-l**, kus radiandi asend otsustab, kas meteoorivool on kasulik või kasutu.
- Kõigile, kes tahavad **numbreid kontrollida**: arvutusjuhend ja programmisisene selgitus esitavad iga sammu koos päritoluga – avaldatud allikas, programmiga tehtud kontroll või programmi valik.

## Sakid

Alates versioonist 1.6 on põhisakkidel **alamsakid** (heledam rida põhirea all). Käivitamisel näitab 5-sekundiline avakuva Perseiide ESO VLT kohal (foto ESO/S. Guisard, CC BY 4.0).

| Sakk | Alamsakk | Mida see näitab |
|---|---|---|
| **Otse ja reaalajas andmed** | [Liiklus otse](Live-Traffic-et) | Asimuutne kaart kogu kogutud MS-liiklusest, iga side kohta kõige tõenäolisemate jälgede pilv, sagedusalade värvid, uued spotid vilguvad |
| | [Radari voog](Radar-Flux-et) | Collmi SKiYMET-radarilt loetud meteooride tunniloendused ja jälgede kõrgused, Sodankylä pilt, hinnang sinu sagedusalale |
| | [GRAVESi radar](GRAVES-Radar-et) | Forward scatteri trass GRAVES → sina: kasulik ala kiires, sektor ja samm, kiire järgmine möödumine, kuidas kuulata |
| | [Andmete kogumine](Data-Collection-et) | Kolm telneti klastrivoogu (DX cluster, RBN, DM4X/PSKReporter) ja MS-spotide filter |
| **Prognoosarvutus** | [Prognoosarvutus](Sky-View-et) | Trassi pealtvaate kaart koos Hot A / Hot B, antenni peaharu, PREV alade ja meteoorivoolu nihkumisega; meteoorivoolude loetelu; väike taevavõlv radiantide ja õigete antennisuundadega; antennist nähtav lõige |
| | [Geomeetria ja sumbumine](Geometry-and-Path-Loss-et) | Kaugus, keskpunkt, elevatsioon, Hot A / Hot B, ühisala piirid, sumbumine 28–432 MHz, lingi eelarve, antenn |
| | [Efektiivsuse arvutus](Efficiency-Calculation-et) | Ülevaatekaardid, iga meteoorivoolu tunnipõhine efektiivsus koos poolega A/B, trassi indeks, DH9GCD võrdlus, graafik |
| | [Eksperimentaalsed prognoosid](Experimental-Forecasts-et) | Collmi voog teisendatuna 144 MHz-le (või mis tahes sagedusele) λ^k ja jaama teguriga K, 24 tunni prognoos, RMOB-i võrdlus |
| **Tehnilised dokumendid** | [Allikad](Sources-et) | Kõik allikad; peamine on Cerrotta–Sartori artikkel |
| | [Euroopa radarite kaart](European-Radar-Map-et) | Kus Collm, Sodankylä, GRAVES ja CMOR sinu jaama suhtes asuvad |
| | [Efektiivsus - selgitus](Efficiency-Explanation-et) | Samm-sammuline dokument efektiivsuse arvutamise kohta, eksporditav Wordi |
| [Meteoorivoolud otse](Live-Showers-et) | – | Global Meteor Networki mõõdetud ZHR ja CMOR-i radiantide kaardid |
| [Meteoorivoolud](Showers-et) | – | IMO kataloog järgmise maksimumiga (IMO kuupäev ja kellaaeg või arvutatud) |
| [Ruutude kaart](Grid-Square-Map-et) | – | ADIF-failist loetud töötatud ja kinnitatud Maidenheadi ruudud, iga sagedusala oma sakil |

Sakkide kohal on kolm juhtnuppude rida (sinu lokaator, korrespondent, sagedusala, antenn, jälgede kõrgus, aeg); vt [Alustamine](Getting-Started-et). Nupp **Juhtnupud** peidab need ning keel ja värviskeem valitakse paremal üleval; vt [Seaded ja andmekaust](Settings-and-Data-Folder-et).

## Lühidalt

- **Tegelik trass, mitte fikseeritud suunad**: efektiivsus arvutatakse kahe lokaatori vahelise suurringjoone trassi jaoks (vanemad programmid kasutasid nelja fikseeritud suunda).
- **Peegelpeegelduse mudel** (McKinley) E-kihi punktides iga 15 km järel, jälgede kõrgus loetakse otse Collmi radarilt.
- **Hot A / Hot B** 150 km kaugusel mõlemal pool keskpunkti (reguleeritav 30–400 km), soovitatud punane, juba antenni peaharus olevad hallid.
- **Radar otse**: Collmi kontrollitakse iga 5 minuti järel, uuesti laaditakse ainult muutunud allikad; ilma võrguta töötab programm edasi viimati salvestatud andmetega.
- **Eksperimentaalne** prognoos sagedustel 50/144/432 MHz SM6FHZ-i λ³ reegliga, võrreldav RMOB-i vaatlejatega.
- Kõik ühes programmi kõrval olevas kaustas **`data`**: ei AppData-t ega süsteemikaustu.

> Efektiivsus on eksperimentaalne mudel (peegelpeegeldus + alatihedad jäljed). Võrdle seda MCG_MS-i, MS-Softi ja oma eetrikogemusega.

## Kust alustada

1. [Paigaldamine](Installation-et)
2. [Alustamine](Getting-Started-et)
3. [Tõrkeotsing ja KKK](Troubleshooting-FAQ-et), kui midagi ei tööta.

Allalaadimised: **[Releases](https://github.com/ic8tem/YA-MS/releases)** GitHubis.
