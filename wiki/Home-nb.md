[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-BR) · [Dansk](Home-da) · **Norsk** · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-TW)

# YA-MS – meteor scatter-prognoser og svermeffektivitet i sanntid

*av Costantino Cerrotta IC8TEM*

**YA-MS** er et gratis program for radioamatører som kjører **meteor scatter (MS) på 50, 70, 144, 222 og 432 MHz**. For den faktiske strekningen mellom din lokator og motstasjonens beregner det time for time hvor mye hver aktiv meteorsverm hjelper strekningen (dens **effektivitet**), fra hvilken side av strekningen refleksjonene kommer (**Hot A / Hot B**), hvor antennen skal peke, og en eksperimentell prognose for refleksjoner per time utledet fra en **meteorradar i sanntid** (Collm, Tyskland). Det kjører på **Windows, Linux, Raspberry Pi og macOS** (.NET 8 + Avalonia), med 36 språk i grensesnittet.

Hovedkilden er artikkelen av **C. Cerrotta IC8TEM og G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (versjon 7). Hver formel og hvert datum i programmet oppgir sin kilde; se [Kilder](Sources-nb).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Himmelhvelving"></a><br><sub>Himmelhvelving</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Effektivitetsberegning"></a><br><sub>Effektivitetsberegning</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="Radar GRAVES"></a><br><sub>Radar GRAVES</sub></td>
</tr></table>

## Hvem er det for

- Operatører som vil vite **når** en meteor scatter-strekning er åpen og **hvor** antennen skal peke, utover det generelle «svermen topper i natt».
- Stasjoner som kjører **lange strekninger på 144 og 432 MHz**, der radiantens posisjon avgjør om en sverm er nyttig eller ubrukelig.
- Alle som vil **sjekke tallene**: beregningshåndboken og forklaringen i programmet viser hvert trinn med opphav: en publisert kilde, en kontroll utført på programmet eller et valg gjort av programmet.

## Fanene

Fra versjon 1.6 har hovedfanene **underfaner** (en lysere rad under hovedraden). Ved oppstart viser en velkomstskjerm i 5 sekunder Perseidene over ESOs VLT (foto ESO/S. Guisard, CC BY 4.0).

| Fane | Underfane | Hva den viser |
|---|---|---|
| **Direkte og sanntidsdata** | [Trafikk direkte](Live-Traffic-nb) | Asimutalt kart over all innsamlet MS-trafikk, med en sky av de mest sannsynlige sporene for hver forbindelse, båndfarger og blinkende nye spot |
| | [Radarfluks](Radar-Flux-nb) | Meteortellinger per time og sporhøyder lest fra SKiYMET-radaren i Collm, bilde fra Sodankylä, estimat for ditt bånd |
| | [Radar GRAVES](GRAVES-Radar-nb) | Forward scatter-strekningen GRAVES → deg: nyttig sone i strålen, sektor og steg, neste strålepassering, slik lytter du |
| | [Datainnsamling](Data-Collection-nb) | Tre telnet-clusterstrømmer (DX cluster, RBN, DM4X/PSKReporter) og filteret for MS-spot |
| **Prognoseberegning** | [Prognoseberegning](Sky-View-nb) | Grunnriss av strekningen med Hot A / Hot B, antennelobe, PREV-soner og svermens forflytning; svermliste; liten himmelhvelving med radianter og riktige antenneretninger; snitt sett fra antennen |
| | [Geometri og demping](Geometry-and-Path-Loss-nb) | Avstand, midtpunkt, elevasjon, Hot A / Hot B, grenser for fellessonen, strekningsdemping 28–432 MHz, linkbudsjett, antenne |
| | [Effektivitetsberegning](Efficiency-Calculation-nb) | Oversiktspaneler, effektivitet time for time for hver sverm med side A/B, strekningsindeks, sammenligning med DH9GCD, diagram |
| | [Eksperimentelle prognoser](Experimental-Forecasts-nb) | Collm-fluks omregnet til 144 MHz (eller vilkårlig frekvens) med λ^k og stasjonsfaktor K, prognose for 24 timer, sammenligning med RMOB |
| **Tekniske dokumenter** | [Kilder](Sources-nb) | Alle kilder; hovedkilden er artikkelen av Cerrotta–Sartori |
| | [Kart over europeiske radarer](European-Radar-Map-nb) | Hvor Collm, Sodankylä, GRAVES og CMOR ligger i forhold til din stasjon |
| | [Effektivitet - forklaring](Efficiency-Explanation-nb) | Dokument som trinn for trinn forklarer hvordan effektiviteten beregnes, kan eksporteres til Word |
| [Svermer direkte](Live-Showers-nb) | – | Målt ZHR fra Global Meteor Network og radiantkart fra CMOR |
| [Svermer](Showers-nb) | – | IMO-katalog med neste maksimum (IMOs dato og tid eller beregnet) |
| [Rutekart](Grid-Square-Map-nb) | – | Kjørte og bekreftede Maidenhead-ruter fra en ADIF-fil, én fane per bånd |

Over fanene er det tre rader med kontroller (din lokator, motstasjon, bånd, antenne, sporhøyde, tid); se [Komme i gang](Getting-Started-nb). Knappen **Kontroller** felder dem sammen, og språk og fargeskjema velges øverst til høyre; se [Innstillinger og datamappe](Settings-and-Data-Folder-nb).

## Kort fortalt

- **Faktisk strekning, ikke faste retninger**: effektiviteten beregnes for storsirkelstrekningen mellom de to lokatorene (eldre programmer brukte fire faste retninger).
- **Modell med speilrefleksjon** (McKinley) i punkter i E-laget for hver 15 km, med sporhøyden lest i sanntid fra Collm-radaren.
- **Hot A / Hot B** 150 km på hver side av midtpunktet (justerbart 30–400 km), det anbefalte i rødt, de som allerede ligger innenfor antenneloben i grått.
- **Radar i sanntid**: Collm sjekkes hvert 5. minutt, og bare endrede kilder lastes ned på nytt; uten nett arbeider programmet videre med de sist lagrede dataene.
- **Eksperimentell** prognose på 50/144/432 MHz med λ³-regelen til SM6FHZ, sammenlignbar med RMOB-observatører.
- Alt ligger i én **`data`**-mappe ved siden av programmet: ingen AppData, ingen systemmapper.

> Effektiviteten er en eksperimentell modell (speilrefleksjon + underdense spor). Sammenlign den med MCG_MS, MS-Soft og din egen erfaring på båndet.

## Hvor du begynner

1. [Installasjon](Installation-nb)
2. [Komme i gang](Getting-Started-nb)
3. [Feilsøking og FAQ](Troubleshooting-FAQ-nb) hvis noe ikke virker.

Nedlasting: **[Releases](https://github.com/ic8tem/YA-MS/releases)** på GitHub.
