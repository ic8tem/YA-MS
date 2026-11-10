[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-BR) · [Dansk](Home-da) · [Norsk](Home-nb) · **Svenska** · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-TW)

# YA-MS – meteorscatterprognoser och svärmarnas effektivitet live

*av Costantino Cerrotta IC8TEM*

**YA-MS** är ett gratisprogram för radioamatörer som kör **meteorscatter (MS) på 50, 70, 144, 222 och 432 MHz**. För den verkliga sträckan mellan din lokator och motstationens beräknar det timme för timme hur mycket varje aktiv meteorsvärm hjälper sträckan (dess **effektivitet**), från vilken sida av sträckan reflexerna kommer (**Hot A / Hot B**), vart antennen ska riktas, samt en experimentell prognos för antalet reflexer per timme, härledd från en **meteorradar i realtid** (Collm, Tyskland). Det körs på **Windows, Linux, Raspberry Pi och macOS** (.NET 8 + Avalonia), med 6 gränssnittsspråk.

Huvudkällan är artikeln av **C. Cerrotta IC8TEM och G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (version 7). Varje formel och varje uppgift i programmet anger sin källa; se [Källor](Sources-sv).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Himlavalv"></a><br><sub>Himlavalv</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Effektivitetsberäkning"></a><br><sub>Effektivitetsberäkning</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES-radar"></a><br><sub>GRAVES-radar</sub></td>
</tr></table>

## Vem programmet är till för

- Operatörer som vill veta **när** en meteorscattersträcka är öppen och **vart** de ska rikta antennen, bortom det allmänna "svärmen har maximum i natt".
- Stationer som kör **långa sträckor på 144 och 432 MHz**, där radiantens läge avgör om en svärm är användbar eller värdelös.
- Alla som vill **kontrollera siffrorna**: beräkningshandboken och förklaringen i programmet visar varje steg med dess ursprung: en publicerad källa, en kontroll gjord på programmet eller ett val gjort av programmet.

## Flikarna

Sedan version 1.6 har huvudflikarna **underflikar** (en ljusare rad under huvudraden). Vid start visas i 5 sekunder en startbild med Perseiderna över ESO:s VLT (foto ESO/S. Guisard, CC BY 4.0).

| Flik | Underflik | Vad den visar |
|---|---|---|
| **Live och realtidsdata** | [Trafik live](Live-Traffic-sv) | Azimutalkarta över all insamlad MS-trafik, med ett moln av de mest sannolika spåren för varje förbindelse, bandfärger och blinkande nya spots |
| | [Radarflöde](Radar-Flux-sv) | Meteorer per timme och spårhöjder avlästa från SKiYMET-radarn i Collm, bild från Sodankylä, uppskattning för ditt band |
| | [GRAVES-radar](GRAVES-Radar-sv) | Forward scatter-sträckan GRAVES → dig: användbar zon i loben, sektor och steg, nästa lobpassage, hur man lyssnar |
| | [Datainsamling](Data-Collection-sv) | Tre telnet-klusterflöden (DX cluster, RBN, DM4X/PSKReporter) och filtret för MS-spots |
| **Prognosberäkning** | [Prognosberäkning](Sky-View-sv) | Plankarta över sträckan med Hot A / Hot B, antennlob, PREV-zoner och svärmens drift; svärmlista; litet himlavalv med radianterna och rätt antennriktningar; tvärsnitt sett från antennen |
| | [Geometri och dämpning](Geometry-and-Path-Loss-sv) | Avstånd, mittpunkt, elevation, Hot A / Hot B, gränser för den gemensamma zonen, sträckdämpning 28–432 MHz, länkbudget, antenn |
| | [Effektivitetsberäkning](Efficiency-Calculation-sv) | Översiktskort, varje svärms effektivitet timme för timme med sida A/B, sträckindex, jämförelse med DH9GCD, diagram |
| | [Experimentella prognoser](Experimental-Forecasts-sv) | Flödet från Collm omräknat till 144 MHz (eller valfri frekvens) med λ^k och stationsfaktor K, prognos för 24 timmar, jämförelse med RMOB |
| **Tekniska dokument** | [Källor](Sources-sv) | Alla källor; den viktigaste är artikeln av Cerrotta–Sartori |
| | [Karta över europeiska radarer](European-Radar-Map-sv) | Var Collm, Sodankylä, GRAVES och CMOR ligger i förhållande till din station |
| | [Effektivitet - förklaring](Efficiency-Explanation-sv) | Dokument som steg för steg visar hur effektiviteten beräknas, kan exporteras till Word |
| [Svärmar live](Live-Showers-sv) | – | Uppmätt ZHR från Global Meteor Network och radiantkartor från CMOR |
| [Svärmar](Showers-sv) | – | IMO-katalogen med nästa maximum (IMO:s datum och tid eller beräknat) |
| [Rutkarta](Grid-Square-Map-sv) | – | Körda och bekräftade Maidenhead-rutor från en ADIF-fil, en flik per band |

Ovanför flikarna finns tre rader med reglage (din lokator, motstation, band, antenn, spårhöjd, tid); se [Kom igång](Getting-Started-sv). Knappen **Reglage** fäller ihop dem, och språk och färgschema väljs uppe till höger; se [Inställningar och datamapp](Settings-and-Data-Folder-sv).

## I korthet

- **Verklig sträcka, inte fasta riktningar**: effektiviteten beräknas för storcirkelsträckan mellan de två lokatorerna (äldre program använde fyra fasta riktningar).
- **Modell med spegelreflexion** (McKinley) i punkter i E-skiktet var 15:e km, med spårhöjden avläst live från Collm-radarn.
- **Hot A / Hot B** 150 km på var sida om mittpunkten (justerbart 30–400 km); den rekommenderade i rött, de som redan ligger inom din antennlob i grått.
- **Radar live**: Collm kontrolleras var 5:e minut och endast ändrade källor hämtas på nytt; utan nätverk fortsätter programmet att arbeta med senast sparade data.
- **Experimentell** prognos på 50/144/432 MHz med SM6FHZ:s λ³-regel, jämförbar med RMOB-observatörer.
- Allt i en enda mapp **`data`** bredvid programmet: ingen AppData, inga systemmappar.

> Effektiviteten är en experimentell modell (spegelreflexion + underdensa spår). Jämför den med MCG_MS, MS-Soft och din egen erfarenhet i luften.

## Var du ska börja

1. [Installation](Installation-sv)
2. [Kom igång](Getting-Started-sv)
3. [Felsökning och FAQ](Troubleshooting-FAQ-sv) om något inte fungerar.

Nedladdning: **[Releases](https://github.com/ic8tem/YA-MS/releases)** på GitHub.
