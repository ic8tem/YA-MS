**English** · [Русский](GRAVES-Radar-ru) · [Deutsch](GRAVES-Radar-de) · [日本語](GRAVES-Radar-ja)

# Radar GRAVES

*Fane: Direkte og sanntidsdata › Radar GRAVES.*

[![Radar GRAVES](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Hva GRAVES er

**GRAVES** er en fransk radar som sender **CW på 143,050 MHz** fra **Broye-lès-Pesmes** (47,348° N 5,515° E, lokator **JN27SI**, ca. 200 m o.h.; Wikipedia). Meteorspor i sonen som både GRAVES og du kan se, reflekterer signalet til deg ved **forward scatter**: du hører korte *pinger* nær bærebølgen. Det er slik **RMOB**-observatørene på 143,050 MHz teller meteorer time for time, og det er et gratis testsignal som alltid er på lufta, for meteor scatter-stasjonen din på 2 m.

Fanen behandler **GRAVES → deg** som en egen meteor scatter-strekning: med de samme funksjonene som hovedstrekningen (samme sporhøyde, lobeelevasjon og hot spot-avstand) beregner den svermeffektivitet, anbefalt Hot og PREV-soner, og sjekker deretter om sonen ligger **innenfor GRAVES-strålen**, og **når** strålen belyser den.

## Øverste linje

| Kontroll | Hva den gjør |
|---|---|
| **Nå** | Setter tiden for himmelhvelvingen tilbake til sanntid (fanen følger glidebryteren *Tid for himmelhvelvingen*). |
| **Sett GRAVES som DX** | Motstasjonen blir GRAVES (JN27SI, høyde 200 m), og hovedstrekningen beregnes på nytt: alle de andre fanene viser da GRAVES-strekningen. |
| **Strålesekvens** | *0,8 s per steg · syklus 4,8 s (PE1ITR 2021)* (standard) eller *3,2 s per steg · syklus 19,2 s (PE1ITR 2007)*. |

## De fire panelene

| Panel | Innhold |
|---|---|
| **NYTTIG SONE I GRAVES-STRÅLEN** | *Ja · sektor X* med asimut og elevasjon for anbefalt hot spot sett fra GRAVES og steget (1–6); eller *Nei: utenfor sektorene* / *Nei: under GRAVES' horisont* / *Nei: over strålen (ca. 25°)* |
| **EFFEKTIVITET PÅ STREKNINGEN GRAVES → DEG NÅ** | Strekningsindeks Σ ZHR × effektivitet, beste sverm, dominerende side A/B, og *forventede ekkoer ≈ …/time* (eksperimentelt, se nedenfor) |
| **STREKNING** | Avstand til GRAVES; antenne mot anbefalt Hot (asimut og elevasjon); direkte asimut til GRAVES |
| **NESTE STRÅLEPASSERING OVER SONEN** | *nå · … s igjen* eller *om … s*, steget (f.eks. *B4*), de tre neste tidspunktene (sekunder innenfor minuttet) og andelen spor som fanges |

Hvis ingen sverm er nyttig i øyeblikket, viser programmet hot spot-et **best egnet for strålen** (innenfor sektorene, nærmest sør) og sier fra om det.

## Himmelen sett fra GRAVES

Ifølge PE1ITR og Bolidozor-wikien dekker **fire fasestyrte antennegrupper** den sørlige himmelen fra **90° til 270°** asimut i fire **sektorer på 45°**:

| Sektor | Asimut fra GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Hver sektor er delt i **6 steg på 7,5°**, nummerert 1 til 6 fra laveste asimut, som belyses etter hverandre, **samtidig i alle fire sektorene**. Strålen er ca. **25° bred i elevasjon**: i sporhøyden dekker den den fargede ringen mellom de to stiplede sirklene (*strålens horisont*). På tegningen: oransje/rosa punkter = PREV-soner for strekningen GRAVES → deg, grønn linje = retningen til stasjonen din, rød linje = fra stasjonen din til anbefalt hot spot; steget som belyses nå, er uthevet.

## Kronologisk rekonstruksjon

*KRONOLOGISK REKONSTRUKSJON · dato UTC* (samme dag som 24 t-tabellen): for hver time effektiviteten på strekningen GRAVES → deg, den gunstigste svermen og det nyttige vinduet (*hh:00 → hh:00 UTC · n t*), med maksimum (*maks Σ … kl. hh:30*) og en rød *nå*-markør. Nedenfor **detaljene for de neste sekundene**: sektorens seks steg, steget som belyser den nyttige sonen, og *mulig ekko (+0,3 s spor)*.

### Stråletiming

Sekvensen er knyttet til **UTC** (PE1ITR): steget som belyses nå, beregnes ut fra sekundene siden 00:00 UTC modulo syklusen (86 400 s er et multiplum av både 4,8 s og 19,2 s). Kommandostasjonen forskyver iblant sekvensen noen steg, så detaljene er en **prognose som må bekreftes ved lytting**. Den gule merkelappen **PC-klokken er synkronisert** minner deg på det: synkroniser PC-en med en NTP-server (feil på høyst noen tideler av et sekund).

### Deteksjonsfaktor

Et spor høres bare hvis strålen belyser det mens det varer:

```
probability ≈ min(1, (step + trail) / cycle)
2021 sequence:  (0.8 + 0.3) / 4.8  ≈ 23 %
2007 sequence:  (3.2 + 0.3) / 19.2 ≈ 18 %
```

0,3 s er en typisk varighet for et underdenst spor på 143 MHz – en fast verdi, *programmets valg* (λ²-regelen til SM6FHZ skalerer varigheter mellom bånd, men gir ingen startverdi).

### Forventede ekkoer (eksperimentelt)

```
echoes/hour ≈ forecast(main path, f_fc) · (f_fc / 143.05)^k · (I_GRAVES + 10) / (I_main + 10) · probability
```

Prognosen fra [Eksperimentelle prognoser](Experimental-Forecasts-nb) (som allerede inneholder stasjonsfaktoren K) omregnes fra sin frekvens f_fc til 143,050 MHz med SM6FHZ-regelen (samme eksponent k), korrigeres med forholdet mellom svermindeksene for de to strekningene (konstanten 10 representerer den sporadiske bakgrunnen, som i prognosen) og multipliseres med deteksjonsfaktoren. Bare veiledende: sammenlign med RMOB-observatørene.

## Slik hører du GRAVES-pingene

| Trinn | Hva du gjør |
|---|---|
| Mottaker | **USB på 143,049 MHz** (tone på ca. 1 kHz) eller 143,050 MHz, **langsom eller avslått AGC**, lydbåndbredde på **minst 2,4 kHz** |
| Antenne | Mot **anbefalt hot spot** for strekningen GRAVES → deg (panelet *STREKNING*), med **lav elevasjon** |
| Fossefall | Pinger er **korte streker nær bærebølgen**; lange (overdense) spor er bredere og viser doppler |
| Telling | RMOB bruker GRAVES til timetelling av meteorer: **sammenlign pingene dine med observatørene på 143,050 MHz** ([Eksperimentelle prognoser](Experimental-Forecasts-nb#sammenligning-med-rmob)) |

## Kilder

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) og *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozor** wiki, "Graves" – antennegrupper, sektorer og stråletiming
3. **Wikipedia**, "GRAVES (system)" – sender i Broye-lès-Pesmes (47,348° N 5,515° E)
4. **RMOB** – observatører på 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** av IC8TEM – fanen Radar GRAVES (skissen denne fanen er avledet fra)
