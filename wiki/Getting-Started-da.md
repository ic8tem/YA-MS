[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · **Dansk** · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Kom godt i gang

Ved første opstart viser YA-MS en eksempelstrækning (JN70CN → JO62QM på 144 MHz). Fem minutter er nok til at indstille det til din station.

## 1. De tre rækker betjeningselementer

Over fanerne er der tre rækker betjeningselementer, som gælder for alle faner. Knappen **Betjening** øverst til højre folder dem sammen og ud (nyttigt med store skrifttyper); valget huskes.

**Række 1 – stationer og bånd**

| Element | Hvad det gør |
|---|---|
| **Min lokator** / **højde m** | Din Maidenhead-lokator (4, 6 eller 8 tegn; feltets centrum bruges) og stationens højde over havet. |
| **Modstation** / **højde m** | Lokator og højde for den station, du vil køre. |
| **Bånd MHz** | 28, 50, 70, 144, 222 eller 432 MHz: bruges til antennens forstærkning og lap, fluxvurderingen og linkbudgettet. |
| **Beregn** | Genberegner strækningen (sampling af E-laget: nogle sekunder). |
| **Antenne az** | Din antennes azimut: altid **mod DX** (strækningens azimut). |
| **Skrifttype** | Størrelsen på al tekst, 85–140 %. Se [Indstillinger](Settings-and-Data-Folder-da#skrifttype-og-betjening). |

**Række 2 – E-laget og antenne**

| Element | Hvad det gør |
|---|---|
| **Sporhøjde km** + **fra radar** | Meteorsporenes højde (standard 90 km). Med flueben i *fra radar* bruges den hyppigste højde (typetallet) målt af Collm-radaren; se [Radarflux](Radar-Flux-da). |
| **Lapelevation °** | Elevation for maksimum af antennens lodrette lobe: en retningsantenne fastgjort på 0° har alligevel loben nogle grader over horisonten på grund af jordrefleksionen (normalt 3-8°). Med feltet **antennediagram** slået til (standard) vægtes punkterne i E-laget med begge antenners lodrette diagram; slået fra bruges kun punkter, som begge stationer ser over denne elevation. |
| **Yagi-antenne: bom m** | Bomlængden på din Yagi. Programmet viser længden i λ, forstærkningen (DL6WU-kurven) og −3 dB-lappen, vandret og lodret; se [Geometri og dæmpning](Geometry-and-Path-Loss-da#antenneforstærkning-og-lap). Under 2 λ er vurderingen grov. |
| **Hot spot fra midtpunkt km** + **auto (AMS)** | Afstanden fra Hot A og Hot B til midtpunktet. Med flueben i *auto (AMS)* (standard) følger den tabellen over antenneforskydning af J. Richardson (AMS), som DJ5HG citerer: 13° ved 1000 km, 11° ved 1250 km, 10° ved 1500 og 2000 km (ca. 115, 121, 132 og 176 km fra midtpunktet). Fjern fluebenet for at indtaste 30–400 km manuelt (MSHV bruger 150 km). |

**Række 3 – tid**

| Element | Hvad det gør |
|---|---|
| **Tid** | UTC-ur. |
| **Beregningsdato (UTC)** | Dagen for beregningen i [Prognoseberegning](Sky-View-da) og [GRAVES-radar](GRAVES-Radar-da) (i dag som standard), på det aktuelle klokkeslæt. Også: den dag, der vises i [Effektivitetsberegning](Efficiency-Calculation-da) og i GRAVES-kronologien. |
| **Timer (−12 til +36 t)** | Flytter beregningens tidspunkt fra 12 timer før til 36 timer efter dette klokkeslæt i trin på 15 minutter. Ved siden af: *Beregning for: nu* eller *Beregning for: dd/mm tt:mm UTC*. |
| **Realtid** | Tilbage til nu. |

## 2. Din station og DX

1. Skriv **Min lokator** og **højde m**.
2. Skriv lokator og højde for **Modstation** – eller klik på kortet i [himmelkuplen](Sky-View-da): **venstreklik = modstationens lokator**, **højreklik = min stations lokator**.
3. Vælg **Bånd MHz**, og tryk på **Beregn**.

Statuslinjen nederst bekræfter: *Strækning beregnet: … km, … refleksionspunkter samplet på … s*.

## 3. Din antenne

Indtast din Yagis **bomlængde**. Programmet udleder forstærkning og lap og advarer dig, hvis Hot A eller Hot B allerede ligger **inden for lappen**, når antennen peger mod DX (så tegnes de med gråt: ingen grund til at dreje antennen).

## 4. Aflæs resultaterne

| Spørgsmål | Hvor skal man se |
|---|---|
| Hvilken sværm hjælper min strækning nu, og fra hvilken side? | [Himmelkuppel](Sky-View-da): sværmliste, anbefalet Hot med rødt, PREV-zoner |
| Hvad er dagens bedste time? | [Effektivitetsberegning](Efficiency-Calculation-da): overbliksbokse og timetabel |
| Hvor mange meteorer tæller radaren? | [Radarflux](Radar-Flux-da) |
| Hvor mange pings kan jeg forvente på 144 MHz? | [Eksperimentelle prognoser](Experimental-Forecasts-da) (eksperimentelt) |
| Kan min station klare strækningen? | [Geometri og dæmpning](Geometry-and-Path-Loss-da): strækningsdæmpning og margin |
| Hvornår er næste maksimum? | [Sværme](Showers-da) |
| Kan jeg teste med GRAVES? | [GRAVES-radar](GRAVES-Radar-da) |

## Praktiske regler (fra kilderne)

- **Peg vinkelret på sværmen**: den bedste strækning er vinkelret på radiantens azimut; bedste retning = radiantens azimut ±90°, tolerance ±40–50° (SM6FHZ).
- **Side-scatter**: drej antennen 10–30° mod den side (A eller B), hvorfra de fleste refleksioner kommer (artiklen af Cerrotta–Sartori).
- **Radiant for højt** (over 70°) eller for lavt (under 20°) giver få brugbare spor (DF5HC, DH9GCD).
- Sporadiske meteorer topper omkring **06 UTC** (artiklen; bekræftet af Collm-fluxen).
- Nyttige afstande på 432 MHz: 800–2000 km, bedst ca. 1400 km (SM6FHZ); bedste afstand generelt 1300–1500 km (DF5HC).

Næste: [Himmelkuppel](Sky-View-da).
