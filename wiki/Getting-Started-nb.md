[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · **Norsk** · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Komme i gang

Ved første oppstart viser YA-MS en eksempelstrekning (JN70CN → JO62QM på 144 MHz). Fem minutter er nok til å stille det inn for din stasjon.

## 1. De tre radene med kontroller

Over fanene er det tre rader med kontroller som gjelder for alle fanene. Knappen **Kontroller** øverst til høyre felder dem sammen og ut (nyttig med store skrifter); valget huskes.

**Rad 1 – stasjoner og bånd**

| Kontroll | Hva den gjør |
|---|---|
| **Min lokator** / **høyde m** | Din Maidenhead-lokator (4, 6 eller 8 tegn; midten av ruten brukes) og stasjonens høyde over havet. |
| **Motstasjon** / **høyde m** | Lokator og høyde for stasjonen du vil kjøre. |
| **Bånd MHz** | 28, 50, 70, 144, 222 eller 432 MHz: brukes for antennens forsterkning og lobe, fluksestimatet og linkbudsjettet. |
| **Beregn** | Beregner strekningen på nytt (sampling av E-laget: noen sekunder). |
| **Antenne az** | Antennens asimut: alltid **mot DX** (strekningens asimut). |
| **Skrift** | Størrelsen på all tekst, 85–140 %. Se [Innstillinger](Settings-and-Data-Folder-nb#skrift-og-kontroller). |

**Rad 2 – E-laget og antenne**

| Kontroll | Hva den gjør |
|---|---|
| **Sporhøyde km** + **fra radar** | Høyden på meteorsporene (standard 90 km). Med *fra radar* avkrysset brukes den hyppigste høyden (typetallet) målt av Collm-radaren; se [Radarfluks](Radar-Flux-nb). |
| **Lobeelevasjon °** | Elevasjon for maksimum av antennens vertikale lobe: en retningsantenne festet på 0° har likevel loben noen grader over horisonten på grunn av bakkerefleksjonen (vanligvis 3-8°). Med boksen **antennediagram** på (standard) vektes punktene i E-laget med det vertikale diagrammet til begge antennene; av brukes bare punkter som begge stasjonene ser over denne elevasjonen. |
| **Yagi-antenne: bom m** | Bomlengden på Yagien din. Programmet viser lengden i λ, forsterkningen (DL6WU-kurven) og −3 dB-loben, horisontalt og vertikalt; se [Geometri og demping](Geometry-and-Path-Loss-nb#antenneforsterkning-og-lobe). Under 2 λ er estimatet grovt. |
| **Hot spot fra midtpunkt km** + **auto (AMS)** | Avstanden fra Hot A og Hot B til midtpunktet. Med *auto (AMS)* avkrysset (standard) følger den tabellen over antenneforskyvning av J. Richardson (AMS) som DJ5HG siterer: 13° ved 1000 km, 11° ved 1250 km, 10° ved 1500 og 2000 km (ca. 115, 121, 132 og 176 km fra midtpunktet). Fjern avkrysningen for å legge inn 30–400 km for hånd (MSHV bruker 150 km). |

**Rad 3 – tid**

| Kontroll | Hva den gjør |
|---|---|
| **Tid** | UTC-klokke. |
| **Beregningsdato (UTC)** | Dagen for beregningen i [Prognoseberegning](Sky-View-nb) og [Radar GRAVES](GRAVES-Radar-nb) (i dag som standard), på gjeldende klokkeslett. Også: dagen som vises i [Effektivitetsberegning](Efficiency-Calculation-nb) og i GRAVES-tidslinjen. |
| **Timer (−12 til +36 t)** | Flytter tidspunktet for beregningen fra 12 timer før til 36 timer etter dette klokkeslettet, i steg på 15 minutter. Ved siden av: *Beregning for: nå* eller *Beregning for: dd/mm tt:mm UTC*. |
| **Sanntid** | Tilbake til nå. |

## 2. Din stasjon og DX

1. Skriv inn **Min lokator** og **høyde m**.
2. Skriv inn lokator og høyde for **Motstasjon** – eller klikk på kartet i [himmelhvelvingen](Sky-View-nb): **venstreklikk = motstasjonens lokator**, **høyreklikk = min stasjons lokator**.
3. Velg **Bånd MHz** og trykk **Beregn**.

Statuslinjen nederst bekrefter: *Strekning beregnet: … km, … refleksjonspunkter samplet på … s*.

## 3. Antennen din

Skriv inn **bomlengden** på Yagien. Programmet utleder forsterkning og lobe og varsler deg hvis Hot A eller Hot B allerede ligger **innenfor loben** når antennen peker mot DX (da tegnes de i grått: ingen grunn til å dreie antennen).

## 4. Les resultatene

| Spørsmål | Hvor du ser |
|---|---|
| Hvilken sverm hjelper strekningen min nå, og fra hvilken side? | [Himmelhvelving](Sky-View-nb): svermliste, anbefalt Hot i rødt, PREV-soner |
| Hva er dagens beste time? | [Effektivitetsberegning](Efficiency-Calculation-nb): oversiktspaneler og timetabell |
| Hvor mange meteorer teller radaren? | [Radarfluks](Radar-Flux-nb) |
| Hvor mange pinger kan jeg vente på 144 MHz? | [Eksperimentelle prognoser](Experimental-Forecasts-nb) (eksperimentelt) |
| Klarer stasjonen min strekningen? | [Geometri og demping](Geometry-and-Path-Loss-nb): strekningsdemping og margin |
| Når er neste maksimum? | [Svermer](Showers-nb) |
| Kan jeg teste med GRAVES? | [Radar GRAVES](GRAVES-Radar-nb) |

## Praktiske regler (fra kildene)

- **Pek vinkelrett på svermen**: den beste strekningen står vinkelrett på radiantens asimut; beste retning = radiantens asimut ±90°, toleranse ±40–50° (SM6FHZ).
- **Side-scatter**: drei antennen 10–30° mot den siden (A eller B) der de fleste refleksjonene kommer fra (artikkelen av Cerrotta–Sartori).
- **Radianten for høyt** (over 70°) eller for lavt (under 20°) gir få nyttige spor (DF5HC, DH9GCD).
- Sporadiske meteorer topper rundt **06 UTC** (artikkelen; bekreftet av Collm-fluksen).
- Nyttige avstander på 432 MHz: 800–2000 km, best rundt 1400 km (SM6FHZ); beste avstand generelt 1300–1500 km (DF5HC).

Neste: [Himmelhvelving](Sky-View-nb).
