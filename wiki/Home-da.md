[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · **Dansk** · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – meteor scatter-prognoser og sværmeffektivitet i realtid

*af Costantino Cerrotta IC8TEM*

**YA-MS** er et gratis program til radioamatører, der kører **meteor scatter (MS) på 50, 70, 144, 222 og 432 MHz**. For den faktiske strækning mellem din lokator og modstationens beregner det time for time, hvor meget hver aktiv meteorsværm hjælper strækningen (dens **effektivitet**), fra hvilken side af strækningen refleksionerne kommer (**Hot A / Hot B**), hvor antennen skal pege hen, og en eksperimentel prognose for refleksioner pr. time udledt af en **meteorradar i realtid** (Collm, Tyskland). Det kører på **Windows, Linux, Raspberry Pi og macOS** (.NET 8 + Avalonia) med 36 sprog i brugerfladen.

Hovedkilden er artiklen af **C. Cerrotta IC8TEM og G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (version 7). Hver formel og hvert datum i programmet angiver sin kilde; se [Kilder](Sources-da).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Himmelkuppel"></a><br><sub>Himmelkuppel</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Effektivitetsberegning"></a><br><sub>Effektivitetsberegning</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES-radar"></a><br><sub>GRAVES-radar</sub></td>
</tr></table>

## Hvem er det til

- Operatører, der vil vide, **hvornår** en meteor scatter-strækning er åben, og **hvorhen** antennen skal pege – ud over det generelle "sværmen topper i nat".
- Stationer, der kører **lange strækninger på 144 og 432 MHz**, hvor radiantens position afgør, om en sværm er nyttig eller ubrugelig.
- Alle, der vil **kontrollere tallene**: beregningsmanualen og forklaringen i programmet viser hvert trin med dets oprindelse: en publiceret kilde, en kontrol udført på programmet eller et valg truffet af programmet.

## Fanerne

Fra version 1.6 har hovedfanerne **underfaner** (en lysere række under hovedrækken). Ved opstart viser en velkomstskærm i 5 sekunder Perseiderne over ESO's VLT (foto ESO/S. Guisard, CC BY 4.0).

| Fane | Underfane | Hvad den viser |
|---|---|---|
| **Live og realtidsdata** | [Live-trafik](Live-Traffic-da) | Azimutalt kort over al indsamlet MS-trafik med en sky af de mest sandsynlige spor for hver forbindelse, båndfarver og blinkende nye spots |
| | [Radarflux](Radar-Flux-da) | Meteortællinger pr. time og sporhøjder aflæst fra Collms SKiYMET-radar, billede fra Sodankylä, vurdering for dit bånd |
| | [GRAVES-radar](GRAVES-Radar-da) | Forward scatter-strækningen GRAVES → dig: nyttig zone i strålen, sektor og trin, næste strålepassage, sådan lytter du |
| | [Dataindsamling](Data-Collection-da) | Tre telnet-cluster-strømme (DX cluster, RBN, DM4X/PSKReporter) og filteret for MS-spots |
| **Prognoseberegning** | [Prognoseberegning](Sky-View-da) | Kort over strækningen set ovenfra med Hot A / Hot B, antennelap, PREV-zoner og sværmens vandring; sværmliste; lille himmelkuppel med radianter og de rigtige antenneretninger; snit set fra antennen |
| | [Geometri og dæmpning](Geometry-and-Path-Loss-da) | Afstand, midtpunkt, elevation, Hot A / Hot B, grænser for den fælles zone, strækningsdæmpning 28–432 MHz, linkbudget, antenne |
| | [Effektivitetsberegning](Efficiency-Calculation-da) | Overbliksbokse, effektivitet pr. time for hver sværm med side A/B, strækningsindeks, sammenligning med DH9GCD, graf |
| | [Eksperimentelle prognoser](Experimental-Forecasts-da) | Collm-flux skaleret til 144 MHz (eller en vilkårlig frekvens) med λ^k og stationsfaktor K, prognose for 24 timer, sammenligning med RMOB |
| [Live-sværme](Live-Showers-da) | – | Målt ZHR fra Global Meteor Network og CMOR's radiantkort |
| [Sværme](Showers-da) | – | IMO-katalog med næste maksimum (IMO's dato og tid eller beregnet) |
| [Kort over felter](Grid-Square-Map-da) | – | Kørte og bekræftede Maidenhead-felter fra en ADIF-fil, én fane pr. bånd |
| **Tekniske dokumenter** | [Kilder](Sources-da) | Alle kilder; hovedkilden er artiklen af Cerrotta–Sartori |
| | [Kort over europæiske radarer](European-Radar-Map-da) | Hvor Collm, Sodankylä, GRAVES og CMOR ligger i forhold til din station |
| | [Forklaring af effektivitetsberegningen](Efficiency-Explanation-da) | Dokument, der trin for trin forklarer, hvordan effektiviteten beregnes; kan eksporteres til Word |

Over fanerne er der tre rækker betjeningselementer (din lokator, modstation, bånd, antenne, sporhøjde, tid); se [Kom godt i gang](Getting-Started-da). Knappen **Betjening** folder dem sammen, og sprog og farveskema vælges øverst til højre; se [Indstillinger og datamappe](Settings-and-Data-Folder-da).

## Kort fortalt

- **Faktisk strækning, ikke faste retninger**: effektiviteten beregnes for storcirkelstrækningen mellem de to lokatorer (ældre programmer brugte fire faste retninger).
- **Model med spejlende refleksion** (McKinley) i punkter i E-laget for hver 15 km, med sporhøjden aflæst i realtid fra Collm-radaren.
- **Hot A / Hot B** 150 km på hver side af midtpunktet (kan indstilles 30–400 km), det anbefalede med rødt, dem der allerede ligger inden for din antennelap med gråt.
- **Radar i realtid**: Collm kontrolleres hvert 5. minut, og kun ændrede kilder hentes igen; uden forbindelse arbejder programmet videre med de senest gemte data.
- **Eksperimentel** prognose på 50/144/432 MHz med SM6FHZ's λ³-regel, som kan sammenlignes med RMOB-observatører.
- Alt ligger i én **`data`**-mappe ved siden af programmet: ingen AppData, ingen systemmapper.

> Effektiviteten er en eksperimentel model (spejlende refleksion + underdense spor). Sammenlign den med MCG_MS, MS-Soft og din egen erfaring på båndet.

## Hvor skal man begynde

1. [Installation](Installation-da)
2. [Kom godt i gang](Getting-Started-da)
3. [Fejlfinding og FAQ](Troubleshooting-FAQ-da), hvis noget ikke virker.

Download: **[Releases](https://github.com/ic8tem/YA-MS/releases)** på GitHub.
