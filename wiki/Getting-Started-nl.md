[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · **Nederlands** · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh)

# Aan de slag

Bij de eerste start toont YA-MS een voorbeeldtraject (JN70CN → JO62QM op 144 MHz). Vijf minuten zijn genoeg om het voor jouw station in te stellen.

## 1. De drie rijen bedieningselementen

Boven de tabbladen staan drie rijen bedieningselementen die voor alle tabbladen gelden. Met de knop **Bediening** rechtsboven klap je ze in en uit (handig bij grote lettertypen); de keuze wordt onthouden.

**Rij 1 – stations en band**

| Element | Wat het doet |
|---|---|
| **Mijn locator** / **hoogte m** | Jouw Maidenhead-locator (4, 6 of 8 tekens; het midden van het vak wordt gebruikt) en de hoogte van het station boven zeeniveau. |
| **Tegenstation** / **hoogte m** | Locator en hoogte van het station dat je wilt werken. |
| **Band MHz** | 28, 50, 70, 144, 222 of 432 MHz: gebruikt voor de antennewinst en -bundel, de fluxschatting en het linkbudget. |
| **Bereken** | Berekent het traject opnieuw (bemonstering van de E-laag: enkele seconden). |
| **Antenne az** | Azimut van je antenne: altijd **richting DX** (azimut van het traject). |
| **Lettertype** | Grootte van alle tekst, 100–300 %. Zie [Instellingen](Settings-and-Data-Folder-nl#lettertype-en-bediening). |

**Rij 2 – E-laag en antenne**

| Element | Wat het doet |
|---|---|
| **Spoorhoogte km** + **van de radar** | Hoogte van de meteorensporen (standaard 90 km). Met *van de radar* aangevinkt wordt de meest voorkomende hoogte (modus) gebruikt die de radar in Collm meet; zie [Radarflux](Radar-Flux-nl). |
| **Elevatie bundel °** | Laagste elevatie van je antennebundel (0° = horizon). Alleen punten van de E-laag die beide stations boven deze elevatie zien, worden gebruikt. |
| **Yagi-antenne: boom m** | Boomlengte van je Yagi. Het programma toont de lengte in λ, de winst (DL6WU-curve) en de −3 dB-bundel, horizontaal en verticaal; zie [Geometrie en demping](Geometry-and-Path-Loss-nl#antennewinst-en-bundel). Onder 2 λ is de schatting onnauwkeurig. |
| **Hotspot vanaf middelpunt km** + **auto (AMS)** | Afstand van Hot A en Hot B tot het middelpunt. Met *auto (AMS)* aangevinkt (standaard) volgt die de tabel met antenne-afwijkingen van J. Richardson (AMS), aangehaald door DJ5HG: 13° bij 1000 km, 11° bij 1250 km, 10° bij 1500 en 2000 km (ongeveer 115, 121, 132 en 176 km van het middelpunt). Vink het uit om 30–400 km met de hand in te voeren (MSHV gebruikt 150 km). |

**Rij 3 – tijd**

| Element | Wat het doet |
|---|---|
| **Uur** | UTC-klok. |
| **Berekeningsdatum (UTC)** | De dag van de berekening voor [Voorspellingsberekening](Sky-View-nl) en [Radar GRAVES](GRAVES-Radar-nl) (standaard vandaag), op het huidige tijdstip van de dag. |
| **Uren (−12 tot +36 u)** | Verschuift het moment van de berekening van 12 uur vóór tot 36 uur na dat tijdstip, in stappen van 15 minuten. Ernaast: *Berekening voor: nu* of *Berekening voor: dd/mm hh:mm UTC*. |
| **Realtime** | Terug naar nu. |
| **Dag voor de 24-uurstabel (UTC)** | De dag die wordt getoond in [Efficiëntieberekening](Efficiency-Calculation-nl) en in de tijdlijn van GRAVES. |

## 2. Jouw station en de DX

1. Vul **Mijn locator** en **hoogte m** in.
2. Vul locator en hoogte van het **Tegenstation** in – of klik op de kaart in de [Hemelkoepel](Sky-View-nl): **linksklik = locator van het tegenstation**, **rechtsklik = locator van mijn station**.
3. Kies de **Band MHz** en druk op **Bereken**.

De statusbalk onderaan bevestigt: *Traject berekend: … km, … reflectiepunten bemonsterd in … s*.

## 3. Jouw antenne

Vul de **boomlengte** van je Yagi in. Het programma leidt daaruit winst en bundel af en waarschuwt je als Hot A of Hot B al **binnen de bundel** vallen wanneer de antenne op de DX is gericht (dan worden ze grijs getekend: je hoeft de antenne niet te draaien).

## 4. De resultaten lezen

| Vraag | Waar kijken |
|---|---|
| Welke zwerm helpt mijn traject nu, en van welke kant? | [Hemelkoepel](Sky-View-nl): lijst van zwermen, aanbevolen hot in het rood, PREV-zones |
| Wat is vandaag het beste uur? | [Efficiëntieberekening](Efficiency-Calculation-nl): overzichtskaarten en uurtabel |
| Hoeveel meteoren telt de radar? | [Radarflux](Radar-Flux-nl) |
| Hoeveel pings kan ik op 144 MHz verwachten? | [Experimentele voorspelling](Experimental-Forecasts-nl) (experimenteel) |
| Kan mijn station het traject overbruggen? | [Geometrie en demping](Geometry-and-Path-Loss-nl): trajectdemping en marge |
| Wanneer is het volgende maximum? | [Zwermen](Showers-nl) |
| Kan ik testen met GRAVES? | [Radar GRAVES](GRAVES-Radar-nl) |

## Praktische regels (uit de bronnen)

- **Richt loodrecht op de zwerm**: het beste traject staat haaks op het azimut van de radiant; beste richting = azimut van de radiant ±90°, tolerantie ±40–50° (SM6FHZ).
- **Side-scatter**: draai de antenne 10–30° naar de kant (A of B) waarvan de meeste reflecties komen (artikel van Cerrotta–Sartori).
- **Een te hoge radiant** (boven 70°) of te lage (onder 20°) geeft weinig bruikbare sporen (DF5HC, DH9GCD).
- Sporadische meteoren hebben hun maximum rond **06 UTC** (artikel; bevestigd door de flux van Collm).
- Bruikbare afstanden op 432 MHz: 800–2000 km, het best rond 1400 km (SM6FHZ); beste afstand in het algemeen 1300–1500 km (DF5HC).

Volgende: [Hemelkoepel](Sky-View-nl).
