[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Português (Brasil)](GRAVES-Radar-pt-BR) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · **Svenska** · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Polski](GRAVES-Radar-pl) · [Čeština](GRAVES-Radar-cs) · [Magyar](GRAVES-Radar-hu) · [Română](GRAVES-Radar-ro) · [Ελληνικά](GRAVES-Radar-el) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [ไทย](GRAVES-Radar-th) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh) · [中文 (繁體)](GRAVES-Radar-zh-TW)

# GRAVES-radar

*Flik: Live och realtidsdata › GRAVES-radar.*

[![GRAVES-radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Vad GRAVES är

**GRAVES** är en fransk radar som sänder **CW på 143,050 MHz** från **Broye-lès-Pesmes** (47.348° N 5.515° E, lokator **JN27SI**, omkring 200 m ö.h.; Wikipedia). Meteorspår i den zon som både GRAVES och du kan se reflekterar dess signal till dig genom **forward scatter**: du hör korta *pingar* nära bärvågen. Det är så **RMOB**-observatörerna på 143,050 MHz räknar meteorer timme för timme, och det är en gratis testsignal som alltid är på för din meteorscatterstation på 2 m.

Fliken behandlar **GRAVES → dig** som en egen meteorscattersträcka: med samma funktioner som för huvudsträckan (samma spårhöjd, lobelevation och hot spot-avstånd) beräknar den svärmarnas effektivitet, rekommenderad Hot och PREV-zoner, och kontrollerar sedan om zonen ligger **inom GRAVES-loben** och **när** loben belyser den.

## Översta raden

| Reglage | Vad det gör |
|---|---|
| **Nu** | För beräkningen tillbaka till realtid: dagens datum och timreglaget på noll (fliken följer *Beräkningsdatum* och *Timmar*). |
| **Sätt GRAVES som DX** | Motstationen blir GRAVES (JN27SI, höjd 200 m) och huvudsträckan beräknas om: alla andra flikar visar då GRAVES-sträckan. |
| **Lobsekvens** | *0,8 s per steg · cykel 4,8 s (PE1ITR 2021)* (standard) eller *3,2 s per steg · cykel 19,2 s (PE1ITR 2007)*. |

## De fyra korten

| Kort | Innehåll |
|---|---|
| **ANVÄNDBAR ZON I GRAVES-LOBEN** | *Ja · sektor X* med azimut och elevation för den rekommenderade hot spoten sett från GRAVES och steget (1–6); eller *Nej: utanför sektorerna* / *Nej: under GRAVES horisont* / *Nej: över loben (cirka 25°)* |
| **EFFEKTIVITET FÖR STRÄCKAN GRAVES → DIG NU** | Sträckindex Σ ZHR × effektivitet, bästa svärm, dominerande sida A/B och *förväntade ekon ≈ …/timme* (experimentellt, se nedan) |
| **STRÄCKA** | Avstånd till GRAVES; antenn mot rekommenderad Hot (azimut och elevation); direkt azimut till GRAVES |
| **NÄSTA LOBPASSAGE ÖVER ZONEN** | *nu · … s kvar* eller *om … s*, steget (t.ex. *B4*), de tre nästa tidpunkterna (sekunder inom minuten) och andelen spår som fångas |

Om ingen svärm är användbar i det ögonblicket visar programmet den hot spot som är **bäst anpassad till loben** (inom sektorerna, närmast söder) och säger det.

## Himlen sedd från GRAVES

Enligt PE1ITR och Bolidozor-wikin täcker **fyra fasstyrda antenner** den södra himlen från **90° till 270°** azimut i fyra **sektorer om 45°**:

| Sektor | Azimut från GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Varje sektor är indelad i **6 steg om 7,5°**, numrerade 1 till 6 från lägsta azimut, som belyses ett efter ett, **samtidigt i alla fyra sektorerna**. Loben är omkring **25° bred i elevation**: på spårhöjden täcker den den färgade ringen mellan de två streckade cirklarna (*lobens horisont*). På ritningen: orange/rosa punkter = PREV-zoner för sträckan GRAVES → dig, grön linje = riktningen mot din station, röd linje = från din station till den rekommenderade hot spoten; steget som belyses just nu är markerat.

## Kronologisk rekonstruktion

*KRONOLOGISK REKONSTRUKTION · datum UTC* (samma dag som 24 h-tabellen): för varje timme effektiviteten för sträckan GRAVES → dig, den mest gynnsamma svärmen och det användbara fönstret (*hh:00 → hh:00 UTC · n h*), med maximum (*max Σ … kl. hh:30*) och en röd markering för *nu*. Nedanför finns **detaljvyn för de närmaste sekunderna**: sektorns sex steg, steget som belyser den användbara zonen, och *möjligt eko (+0,3 s spår)*.

### Lobens tidsschema

Sekvensen är knuten till **UTC** (PE1ITR): steget som belyses nu beräknas från antalet sekunder sedan 00:00 UTC modulo cykeln (86 400 s är en multipel av både 4,8 s och 19,2 s). Kommandostationen förskjuter ibland sekvensen några steg, så detaljvyn är en **förutsägelse som ska bekräftas genom att lyssna**. Den gula etiketten **datorns klocka synkroniserad** påminner dig: synkronisera din dator mot en NTP-server (fel på högst några tiondels sekund).

### Detektionsfaktor

Ett spår hörs bara om loben belyser det medan det varar:

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0,3 s är en typisk varaktighet för ett underdenst spår på 143 MHz – ett fast värde, *programmets val* (SM6FHZ:s λ²-regel skalar varaktigheter mellan banden men ger inget startvärde).

### Förväntade ekon (experimentellt)

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

Prognosen från [Experimentella prognoser](Experimental-Forecasts-sv) (som redan innehåller stationsfaktorn K) räknas om från sin frekvens f_fc till 143,050 MHz med SM6FHZ:s regel (samma exponent k), korrigeras med kvoten mellan de två sträckornas svärmindex (konstanten 10 representerar den sporadiska bakgrunden, som i prognosen) och multipliceras med detektionsfaktorn. Endast vägledande: jämför med RMOB-observatörerna.

## Hur du hör GRAVES-pingarna

| Steg | Vad du gör |
|---|---|
| Mottagare | **USB på 143,049 MHz** (ton omkring 1 kHz) eller 143,050 MHz, **långsam eller avstängd AGC**, audiobandbredd **minst 2,4 kHz** |
| Antenn | Mot den **rekommenderade hot spoten** för sträckan GRAVES → dig (kortet *STRÄCKA*), med **låg elevation** |
| Vattenfall | Pingarna är **korta streck nära bärvågen**; långa (overdensa) spår är bredare och visar doppler |
| Räkning | RMOB använder GRAVES för meteorräkning per timme: **jämför dina pingar med observatörerna på 143,050 MHz** ([Experimentella prognoser](Experimental-Forecasts-sv#jämförelse-med-rmob)) |

## Källor

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) och *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozor**-wikin, "Graves" – antenner, sektorer och lobens tidsschema
3. **Wikipedia**, "GRAVES (system)" – sändaren i Broye-lès-Pesmes (47.348° N 5.515° E)
4. **RMOB** – observatörer på 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** av IC8TEM – fliken GRAVES Radar (den förlaga som den här fliken bygger på)
