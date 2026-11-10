[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · **Nederlands** · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [ไทย](Efficiency-Calculation-th) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Efficiëntieberekening

*Tabblad: Voorspellingsberekening › Efficiëntieberekening.*

[![Efficiëntieberekening](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/nl-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/nl-2_3.png)

De **efficiëntie** van een zwerm geeft in procenten aan in hoeverre de positie van de radiant reflecties op **jouw** traject mogelijk maakt. Het begrip is van Ilkka **OH5IY** (MS-Soft) en wordt overgenomen in het artikel van Cerrotta–Sartori: het maximum van de efficiëntie valt niet samen met het visuele maximum (ZHR), omdat het afhangt van waar de radiant staat ten opzichte van de twee stations. MCG_MS van DL5MCG past hetzelfde idee toe op vier vaste richtingen; YA-MS berekent het voor het **werkelijke traject** tussen de twee locators.

Dit tabblad toont haar uur voor uur voor de dag die is gekozen in *Dag voor de 24-uurstabel (UTC)* (waarden op het halve uur).

## Overzichtskaarten

| Kaart | Inhoud |
|---|---|
| **BESTE UUR VAN DE DAG** | Uur met de hoogste trajectindex, de index en de overheersende zijde (A/B met haar %) |
| **GUNSTIGSTE ZWERM** | De zwerm met de hoogste ZHR × efficiëntie van de dag, zijn efficiëntie, uur en zijde, en de **beste richting** (azimut van de radiant +90° / −90°) |
| **NU** | Index en overheersende zijde op dit uur, en de aanbevolen hot (alleen als de gekozen dag vandaag is) |
| **EXPERIMENTELE VOORSPELLING** | Verwachte reflecties/uur nu, over 1 h en over 2 h op de voorspellingsfrequentie (Collm, SM6FHZ-regels; zie [Experimentele voorspelling](Experimental-Forecasts-nl)) |

Onder de kaarten legt een balk de letters A en B uit (zie hieronder).

## Grafiek

*Efficiëntie per uur voor … op … (UTC, waarden op het halve uur).* Voor maximaal vijf zwermen: efficiëntie % als doorgetrokken lijn en de DH9GCD-formule als stippellijn in dezelfde kleur; de **trajectindex** als blauwe balken op de rechterschaal.

## Uurtabel

Eén regel per zwerm die die dag actief is (gesorteerd op ZHR), 24 kolommen voor de uren (UTC):

| Cel | Betekenis |
|---|---|
| `63A` | efficiëntie 63 %, de meeste reflecties van zijde **A** |
| `41B` | efficiëntie 41 %, zijde **B** |
| `3` | efficiëntie onder 5 %: getal zonder letter voor de zijde |
| leeg | efficiëntie onder 1 % |
| `…↑` | de radiant staat op dat uur **hoger dan 70°** vanaf jouw station (te hoog) |
| gele tekst | efficiëntie ≥ 50 % |

- **A** = **links**, kijkend van jouw station naar het tegenstation (zone Hot A); **B** = **rechts** (zone Hot B). Het loont om de antenne **10–30° naar die kant** te draaien (side-scatter, artikel van Cerrotta–Sartori).
- **Lichtblauwe regels** (*DH9GCD %*, onder elke zwerm): de DH9GCD-formule, ter vergelijking.
- **Σ-regel**: *Trajectindex (ZHR×eff.)*.
- **Oranje regel** (*Voorspelling … MHz (refl./uur)*): de experimentele voorspelling, voor de uren waarvoor die bestaat (vandaag en een deel van morgen).

## Het model

Alle stappen staan in de [rekenhandleiding](Efficiency-Explanation-nl) (`doc/YA-MS_manuale_calcoli.docx`, hoofdstuk 5). In het kort:

**1. Spiegelende reflectie.** Een spoor stuurt het signaal alleen van A naar B als het raakt aan een ellipsoïde met A en B in de brandpunten (McKinley 1961). De sporen van een zwerm lopen evenwijdig aan de richting van de radiant ŝ (artikel; McKinley). Voor elk punt P van de E-laag, met eenheidsvectoren naar de stations:

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

Dezelfde wet ligt ten grondslag aan QTFGUI van DJ5HG (cone scattering). De voorwaarde wordt geaccepteerd met een Gaussische tolerantie σ = 0,05 rad (ongeveer 3°) – *keuze van het programma*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Gewicht van elk punt.** Vermogen van een onderdicht spoor (McKinley), φ = de halve verstrooiingshoek (begrensd op 85°, *keuze*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Het aantal meteoren dat een punt bereikt, is evenredig met de sinus van de elevatie van de radiant in dat punt (ŝ·û_P), dezelfde correctie die de IMO voor de ZHR gebruikt.

**3. Som en percentage.** Punten om de 15 km op spoorhoogte, alleen waar beide stations ze boven de bundelelevatie zien (*keuze*). 100 % is de gunstigste positie van de radiant voor dat traject:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F wordt eenmaal per traject berekend op een raster van richtingen (azimut om de 5°, elevatie om de 2,5°) en geïnterpoleerd.

**4. Zijde en index.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

De letter in de tabel is de zijde met de grootste fractie. *Keuzes van het programma (vgl. 32–33 van de handleiding).*

## Vergelijking met DH9GCD

Een onafhankelijke controle: de formule voor de beste richting van **DH9GCD**, aangehaald door **DF5HC** (DARC-congres, januari 2018), met El en Az de elevatie en het azimut van de radiant gezien vanaf jouw station en P het azimut van het tegenstation:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Ze is maximaal met de radiant op 45° en dwars op het traject. DF5HC vindt de radiant te laag onder 20° en **te hoog boven 70°**: die uren krijgen ↑ in de tabel en een waarschuwing in de [Hemelkoepel](Sky-View-nl#waarschuwingen). De formule negeert afstand en hoogtes, maar is een goede referentie.

## Controles

| Controle | Resultaat |
|---|---|
| Regel van SM6FHZ (VUSHF 2025): beste traject loodrecht op het azimut van de radiant, richting = az. radiant ±90°, tolerantie ±40–50° | Door het model gereproduceerd; met de radiant in lijn met het traject en hoog aan de hemel is de efficiëntie bijna nul |
| QTFGUI van DJ5HG, Hamburg JO53IM – Barcelona, Quadrantiden, 4 januari (voorbeeld uit zijn handleiding) | QTFGUI: 07:00 richting 252°, −8 dB; 08:00 geen reflectiezone; 09:00 richting 168°, −4 dB. YA-MS (hoogte 102 km zoals QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Alle drie de methoden zien het gat om 08:00, met de radiant bijna in het zenit |
| Bemonstering om de 5 km in plaats van 15 km | de percentages veranderen minder dan 0,3 punt |

> De schaal die OH5IY en MCG_MS gebruiken, is niet in detail bekend (de handleidingen van MS-Soft zijn niet beschikbaar): vergelijk de percentages met die programma's voordat je ze als gelijkwaardig beschouwt. Het model houdt alleen rekening met onderdichte sporen, met isotrope antennes; overdichte bursts en de sporadische achtergrond zitten niet in de efficiëntie (de sporadische achtergrond wordt vertegenwoordigd door de radarflux).
