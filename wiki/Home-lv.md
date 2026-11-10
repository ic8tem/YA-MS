[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · **Latviešu** · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [ไทย](Home-th) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – meteor scatter prognozes un plūsmu efektivitāte tiešsaistē

*sagatavoja Costantino Cerrotta IC8TEM*

**YA-MS** ir bezmaksas programma radioamatieriem, kas strādā **meteor scatter (MS) 50, 70, 144, 222 un 432 MHz joslās**. Reālajai trasei starp tavu un korespondenta lokatoru tā stundu pa stundai aprēķina, cik lielā mērā katra aktīvā meteoru plūsma palīdz trasei (tās **efektivitāti**), no kuras trases puses nāk atstarojumi (**Hot A / Hot B**), kur tēmēt antenu, un eksperimentālu atstarojumu skaita stundā prognozi, kas iegūta no **meteoru radara tiešsaistē** (Collm, Vācija). Tā darbojas **Windows, Linux un macOS** (.NET 8 + Avalonia) 36 saskarnes valodās.

Galvenais avots ir **C. Cerrotta IC8TEM un G. Sartori IV3GTH** raksts *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (7. versija). Katrai programmas formulai un datu vienībai ir norādīts avots; sk. [Avoti](Sources-lv).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Debess velve"></a><br><sub>Debess velve</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Efektivitātes aprēķins"></a><br><sub>Efektivitātes aprēķins</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES radars"></a><br><sub>GRAVES radars</sub></td>
</tr></table>

## Kam tā paredzēta

- Operatoriem, kas grib zināt, **kad** meteor scatter trase ir atvērta un **kurp** tēmēt, nevis tikai vispārīgo "plūsmas maksimums ir šonakt".
- Stacijām, kas strādā **garās trasēs 144 un 432 MHz**, kur radianta stāvoklis izšķir, vai plūsma ir noderīga vai nederīga.
- Ikvienam, kas grib **pārbaudīt skaitļus**: aprēķinu rokasgrāmata un skaidrojums programmā sniedz katru soli ar tā izcelsmi – publicētu avotu, programmā veiktu pārbaudi vai programmas izvēli.

## Cilnes

Kopš 1.6. versijas galvenajām cilnēm ir **apakšcilnes** (gaišāka rinda zem galvenās). Startējot 5 sekundes redzams ievadekrāns ar Perseīdām virs ESO VLT (foto ESO/S. Guisard, CC BY 4.0).

| Cilne | Apakšcilne | Ko tā rāda |
|---|---|---|
| **Tiešsaiste un reāllaika dati** | [Satiksme tiešsaistē](Live-Traffic-lv) | Azimutāla karte ar visu savākto MS satiksmi, katram sakaram varbūtīgāko sliežu mākonis, joslu krāsas, jaunie spoti mirgo |
| | [Radara meteoru skaits](Radar-Flux-lv) | Meteoru skaits stundā un sliežu augstumi no Collm SKiYMET radara, Sodankylä attēls, novērtējums tavai joslai |
| | [GRAVES radars](GRAVES-Radar-lv) | Forward scatter trase GRAVES → tu: lietderīgā zona kūlī, sektors un solis, nākamā kūļa pāreja, kā klausīties |
| | [Datu vākšana](Data-Collection-lv) | Trīs telnet klasteru plūsmas (DX cluster, RBN, DM4X/PSKReporter) un MS spotu filtrs |
| **Prognozes aprēķins** | [Prognozes aprēķins](Sky-View-lv) | Trases plāna karte ar Hot A / Hot B, antenas ziedlapiņu, PREV zonām un plūsmas pārvietošanos; plūsmu saraksts; maza debess velve ar radiantiem un pareizajiem antenas virzieniem; griezums, kā to redz antena |
| | [Ģeometrija un vājinājums](Geometry-and-Path-Loss-lv) | Attālums, viduspunkts, elevācija, Hot A / Hot B, kopējās zonas robežas, trases vājinājums 28–432 MHz, sakaru budžets, antena |
| | [Efektivitātes aprēķins](Efficiency-Calculation-lv) | Pārskata kartītes, katras plūsmas efektivitāte pa stundām ar pusi A/B, trases indekss, DH9GCD salīdzinājums, grafiks |
| | [Eksperimentālas prognozes](Experimental-Forecasts-lv) | Collm meteoru skaits, pārrēķināts uz 144 MHz (vai jebkuru frekvenci) ar λ^k un stacijas koeficientu K, 24 stundu prognoze, salīdzinājums ar RMOB |
| **Tehniskie dokumenti** | [Avoti](Sources-lv) | Visi avoti; galvenais ir Cerrotta–Sartori raksts |
| | [Eiropas radaru karte](European-Radar-Map-lv) | Kur atrodas Collm, Sodankylä, GRAVES un CMOR attiecībā pret tavu staciju |
| | [Efektivitāte - skaidrojums](Efficiency-Explanation-lv) | Dokuments soli pa solim par to, kā tiek aprēķināta efektivitāte, eksportējams uz Word |
| [Plūsmas tiešsaistē](Live-Showers-lv) | – | Global Meteor Network izmērītie ZHR un CMOR radiantu kartes |
| [Plūsmas](Showers-lv) | – | IMO katalogs ar nākamo maksimumu (IMO datums un laiks vai aprēķināts) |
| [Kvadrātu karte](Grid-Square-Map-lv) | – | Strādātie un apstiprinātie Maidenhead kvadrāti no ADIF faila, viena cilne katrai joslai |

Virs cilnēm ir trīs vadības rindas (tavs lokators, korespondents, josla, antena, sliežu augstums, laiks); sk. [Darba sākšana](Getting-Started-lv). Poga **Vadība** tās sakļauj, bet valodu un krāsu shēmu izvēlas augšā pa labi; sk. [Iestatījumi un datu mape](Settings-and-Data-Folder-lv).

## Īsumā

- **Reāla trase, nevis fiksēti virzieni**: efektivitāte tiek aprēķināta lielā loka trasei starp abiem lokatoriem (vecākas programmas izmantoja četrus fiksētus virzienus).
- **Spoguļatstarošanas modelis** (McKinley) E slāņa punktos ik pēc 15 km, ar sliežu augstumu, kas tiešsaistē nolasīts no Collm radara.
- **Hot A / Hot B** 150 km abpus viduspunktam (regulējams 30–400 km), ieteicamais sarkanā krāsā, tie, kas jau ir antenas ziedlapiņā, pelēkā.
- **Radars tiešsaistē**: Collm tiek pārbaudīts ik pēc 5 minūtēm, no jauna lejupielādē tikai mainījušos avotus; bez tīkla programma turpina strādāt ar pēdējiem saglabātajiem datiem.
- **Eksperimentāla** prognoze 50/144/432 MHz ar SM6FHZ λ³ likumu, salīdzināma ar RMOB novērotājiem.
- Viss vienā **`data`** mapē blakus programmai: ne AppData, ne sistēmas mapes.

> Efektivitāte ir eksperimentāls modelis (spoguļatstarošana + zema blīvuma sliedes). Salīdzini to ar MCG_MS, MS-Soft un savu pieredzi ēterā.

## Ar ko sākt

1. [Instalēšana](Installation-lv)
2. [Darba sākšana](Getting-Started-lv)
3. [Problēmu risināšana un BUJ](Troubleshooting-FAQ-lv), ja kaut kas nedarbojas.

Lejupielāde: **[Releases](https://github.com/ic8tem/YA-MS/releases)** vietnē GitHub.
