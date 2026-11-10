[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · **Svenska** · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh)

# Kom igång

Vid första starten visar YA-MS en exempelsträcka (JN70CN → JO62QM på 144 MHz). Fem minuter räcker för att ställa in det för din station.

## 1. De tre raderna med reglage

Ovanför flikarna finns tre rader med reglage som gäller för alla flikar. Knappen **Reglage** uppe till höger fäller ihop och fäller ut dem (praktiskt med stora typsnitt); valet sparas.

**Rad 1 – stationer och band**

| Reglage | Vad det gör |
|---|---|
| **Min lokator** / **höjd m** | Din Maidenhead-lokator (4, 6 eller 8 tecken; rutans mittpunkt används) och stationens höjd över havet. |
| **Motstation** / **höjd m** | Lokator och höjd för den station du vill köra. |
| **Band MHz** | 28, 50, 70, 144, 222 eller 432 MHz: används för antennens förstärkning och lob, flödesuppskattningen och länkbudgeten. |
| **Beräkna** | Beräknar sträckan på nytt (sampling av E-skiktet: några sekunder). |
| **Antenn az** | Din antenns azimut: alltid **mot DX** (sträckans azimut). |
| **Typsnitt** | Storlek på all text, 100–300 %. Se [Inställningar](Settings-and-Data-Folder-sv#typsnitt-och-reglage). |

**Rad 2 – E-skiktet och antennen**

| Reglage | Vad det gör |
|---|---|
| **Spårhöjd km** + **från radar** | Meteorspårens höjd (standard 90 km). Med *från radar* ikryssat används den vanligaste höjden (typvärdet) som Collm-radarn har mätt; se [Radarflöde](Radar-Flux-sv). |
| **Lobelevation °** | Lägsta elevation för din antennlob (0° = horisonten). Endast punkter i E-skiktet som båda stationerna ser ovanför denna elevation används. |
| **Yagiantenn: bom m** | Bomlängden på din yagi. Programmet visar längden i λ, förstärkningen (DL6WU-kurvan) och −3 dB-loben, horisontellt och vertikalt; se [Geometri och dämpning](Geometry-and-Path-Loss-sv#antennförstärkning-och-lob). Under 2 λ är uppskattningen grov. |
| **Hot spot från mittpunkt km** | Avståndet från mittpunkten till Hot A och Hot B, 30–400 km (standard 150 km, som i AMS Bulletin 203 / W8WN / MSHV). |

**Rad 3 – tid**

| Reglage | Vad det gör |
|---|---|
| **Tid** | UTC-klocka. |
| **Himlavalvets tid (±36 h)** | Flyttar [Himlavalvet](Sky-View-sv) och fliken [GRAVES-radar](GRAVES-Radar-sv) upp till 36 timmar bakåt eller framåt, i steg om 15 minuter. |
| **Realtid** | Tillbaka till nu. |
| **Dag för 24 h-tabellen (UTC)** | Den dag som visas i [Effektivitetsberäkning](Efficiency-Calculation-sv) och i GRAVES-tidslinjen. |

## 2. Din station och motstationen

1. Skriv in **Min lokator** och **höjd m**.
2. Skriv in **Motstation**ens lokator och höjd – eller klicka på kartan i [Himlavalvet](Sky-View-sv): **vänsterklick = motstationens lokator**, **högerklick = min stations lokator**.
3. Välj **Band MHz** och tryck på **Beräkna**.

Statusraden längst ned bekräftar: *Sträcka beräknad: … km, … reflexionspunkter samplade på … s*.

## 3. Din antenn

Ange **bomlängden** på din yagi. Programmet härleder förstärkning och lob och varnar dig om Hot A eller Hot B redan ligger **inom loben** när antennen är riktad mot DX (de ritas då i grått: du behöver inte vrida antennen).

## 4. Läs resultaten

| Fråga | Var du tittar |
|---|---|
| Vilken svärm hjälper min sträcka nu, och från vilken sida? | [Himlavalv](Sky-View-sv): svärmlista, rekommenderad Hot i rött, PREV-zoner |
| Vilken är dagens bästa timme? | [Effektivitetsberäkning](Efficiency-Calculation-sv): översiktskort och timtabell |
| Hur många meteorer räknar radarn? | [Radarflöde](Radar-Flux-sv) |
| Hur många pingar kan jag vänta mig på 144 MHz? | [Experimentella prognoser](Experimental-Forecasts-sv) (experimentellt) |
| Klarar min station sträckan? | [Geometri och dämpning](Geometry-and-Path-Loss-sv): sträckdämpning och marginal |
| När är nästa maximum? | [Svärmar](Showers-sv) |
| Kan jag testa med GRAVES? | [GRAVES-radar](GRAVES-Radar-sv) |

## Praktiska regler (från källorna)

- **Rikta vinkelrätt mot svärmen**: den bästa sträckan är ortogonal mot radiantens azimut; bästa riktning = radiantens azimut ±90°, tolerans ±40–50° (SM6FHZ).
- **Side-scatter**: vrid antennen 10–30° åt den sida (A eller B) varifrån flest reflexer kommer (artikeln av Cerrotta–Sartori).
- **En radiant som står för högt** (över 70°) eller för lågt (under 20°) ger få användbara spår (DF5HC, DH9GCD).
- Sporadiska meteorer har maximum kring **06 UTC** (artikeln; bekräftat av flödet från Collm).
- Användbara avstånd på 432 MHz: 800–2000 km, bäst omkring 1400 km (SM6FHZ); bästa avstånd i allmänhet 1300–1500 km (DF5HC).

Nästa: [Himlavalv](Sky-View-sv).
