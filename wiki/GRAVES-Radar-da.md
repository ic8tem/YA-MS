[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · **Dansk** · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh)

# GRAVES-radar

*Fane: Live og realtidsdata › GRAVES-radar.*

[![GRAVES-radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Hvad GRAVES er

**GRAVES** er en fransk radar, der sender **CW på 143,050 MHz** fra **Broye-lès-Pesmes** (47,348° N 5,515° Ø, lokator **JN27SI**, ca. 200 m o.h.; Wikipedia). Meteorspor i den zone, som både GRAVES og du kan se, reflekterer signalet til dig ved **forward scatter**: du hører korte *pings* tæt på bærebølgen. Det er sådan, **RMOB**-observatørerne på 143,050 MHz tæller meteorer time for time, og det er et gratis testsignal, der altid er i luften, til din meteor scatter-station på 2 m.

Fanen behandler **GRAVES → dig** som en selvstændig meteor scatter-strækning: med de samme funktioner som hovedstrækningen (samme sporhøjde, lapelevation og hot spot-afstand) beregner den sværmeffektivitet, anbefalet Hot og PREV-zoner og kontrollerer derefter, om zonen ligger **inden for GRAVES-strålen**, og **hvornår** strålen belyser den.

## Øverste linje

| Element | Hvad det gør |
|---|---|
| **Nu** | Sætter beregningstidspunktet tilbage til realtid (fanen følger skyderen *Beregningstidspunkt*). |
| **Sæt GRAVES som DX** | Modstationen bliver GRAVES (JN27SI, højde 200 m), og hovedstrækningen genberegnes: alle andre faner viser derefter GRAVES-strækningen. |
| **Strålesekvens** | *0,8 s pr. trin · cyklus 4,8 s (PE1ITR 2021)* (standard) eller *3,2 s pr. trin · cyklus 19,2 s (PE1ITR 2007)*. |

## De fire bokse

| Boks | Indhold |
|---|---|
| **NYTTIG ZONE I GRAVES-STRÅLEN** | *Ja · sektor X* med azimut og elevation for det anbefalede hot spot set fra GRAVES og trinnet (1–6); eller *Nej: uden for sektorerne* / *Nej: under GRAVES' horisont* / *Nej: over strålen (ca. 25°)* |
| **EFFEKTIVITET FOR STRÆKNINGEN GRAVES → DIG NU** | Strækningsindeks Σ ZHR × effektivitet, bedste sværm, fremherskende side A/B og *forventede ekkoer ≈ …/time* (eksperimentelt, se nedenfor) |
| **STRÆKNING** | Afstand til GRAVES; antenne mod det anbefalede Hot (azimut og elevation); azimut til GRAVES i direkte linje |
| **NÆSTE STRÅLEPASSAGE OVER ZONEN** | *nu · … s tilbage* eller *om … s*, trinnet (fx *B4*), de næste tre tidspunkter (sekunder inden for minuttet) og andelen af spor, der fanges |

Hvis ingen sværm er nyttig i øjeblikket, viser programmet det hot spot, der **passer bedst til strålen** (inden for sektorerne, tættest på syd), og siger det.

## Himlen set fra GRAVES

Ifølge PE1ITR og Bolidozor-wikien dækker **fire fasestyrede antennegrupper** den sydlige himmel fra **90° til 270°** azimut i fire **sektorer på 45°**:

| Sektor | Azimut fra GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Hver sektor er delt i **6 trin på 7,5°**, nummereret 1 til 6 fra den laveste azimut, som belyses efter hinanden, **samtidig i alle fire sektorer**. Strålen er ca. **25° bred i elevation**: i sporhøjde dækker den den farvede ring mellem de to stiplede cirkler (*strålens horisont*). På tegningen: orange/lyserøde prikker = PREV-zoner for strækningen GRAVES → dig, grøn linje = retning til din station, rød linje = fra din station til det anbefalede hot spot; det trin, der belyses nu, er fremhævet.

## Kronologisk rekonstruktion

*KRONOLOGISK REKONSTRUKTION · dato UTC* (samme dag som 24 t-tabellen): for hver time effektiviteten for strækningen GRAVES → dig, den mest gunstige sværm og det nyttige vindue (*hh:00 → hh:00 UTC · n t*), med maksimum (*maks. Σ … kl. hh:30*) og en rød *nu*-markør. Nedenunder **detaljerne for de næste sekunder**: sektorens seks trin, det trin, der belyser den nyttige zone, og *muligt ekko (+0,3 s spor)*.

### Strålens timing

Sekvensen er knyttet til **UTC** (PE1ITR): det trin, der belyses nu, beregnes ud fra sekunderne siden 00:00 UTC modulo cyklussen (86 400 s er et multiplum af både 4,8 s og 19,2 s). Kommandostationen forskyder sommetider sekvensen nogle trin, så detaljen er en **prognose, der skal bekræftes ved at lytte**. Den gule mærkat **pc-uret er synkroniseret** minder dig om det: synkronisér din pc med en NTP-server (fejl på højst nogle tiendedele sekund).

### Detektionsfaktor

Et spor høres kun, hvis strålen belyser det, mens det varer:

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0,3 s er en typisk varighed for et underdenst spor ved 143 MHz – en fast værdi, *programmets valg* (SM6FHZ's λ²-regel skalerer varigheder mellem bånd, men giver ingen startværdi).

### Forventede ekkoer (eksperimentelt)

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

Prognosen fra [Eksperimentelle prognoser](Experimental-Forecasts-da) (som allerede indeholder stationsfaktoren K) skaleres fra sin frekvens f_fc til 143,050 MHz med SM6FHZ-reglen (samme eksponent k), korrigeres med forholdet mellem de to strækningers sværmindekser (konstanten 10 repræsenterer den sporadiske baggrund, som i prognosen) og ganges med detektionsfaktoren. Kun vejledende: sammenlign med RMOB-observatørerne.

## Sådan hører du GRAVES-pings

| Trin | Hvad skal man gøre |
|---|---|
| Modtager | **USB på 143,049 MHz** (tone ved ca. 1 kHz) eller 143,050 MHz, **langsom eller slukket AGC**, audiobåndbredde på **mindst 2,4 kHz** |
| Antenne | Mod det **anbefalede hot spot** for strækningen GRAVES → dig (boksen *STRÆKNING*), med **lav elevation** |
| Vandfald | Pings er **korte streger tæt på bærebølgen**; lange (overdense) spor er bredere og viser Doppler |
| Tælling | RMOB bruger GRAVES til meteortællinger pr. time: **sammenlign dine pings med observatørerne på 143,050 MHz** ([Eksperimentelle prognoser](Experimental-Forecasts-da#sammenligning-med-rmob)) |

## Kilder

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) og *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozor** wiki, "Graves" – antennegrupper, sektorer og strålens timing
3. **Wikipedia**, "GRAVES (system)" – sender i Broye-lès-Pesmes (47,348° N 5,515° Ø)
4. **RMOB** – observatører på 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** af IC8TEM – fanen Radar GRAVES (skitsen, som denne fane er afledt af)
