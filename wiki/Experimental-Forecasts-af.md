[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · **Afrikaans** · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [ไทย](Experimental-Forecasts-th) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Eksperimentele voorspellings

*Oortjie: Voorspellingsberekening › Eksperimentele voorspellings.*

[![Eksperimentele voorspellings](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Hierdie oortjie omskep die meteoortellings van die **Collm-radar (36,2 MHz)** in 'n skatting van die **refleksies per uur op 'n amateurband** (verstek 144 MHz, enige frekwensie van 28 tot 1300 MHz), voorspel die **volgende 24 uur** vir jou pad en laat jou toe om die skatting met 'n **RMOB**-waarnemer te **vergelyk** – byvoorbeeld een wat na GRAVES op 143,050 MHz luister.

> Alles hier is **eksperimenteel**: die frekwensiereël is 'n empiriese reël, en die stasiefaktor hang van jou stasie af. Gebruik die syfers om ure en dae te vergelyk, en kontroleer hulle op die lug.

## Kontroles

| Kontrole | Verstek | Wat dit doen |
|---|---|---|
| **Teikenfrekwensie MHz** | 144 | Frekwensie van die voorspelling (28–1300 MHz) |
| **λ^k-eksponent** | 3 | Eksponent k van die frekwensiereël (SM6FHZ: 3) |
| **Stasiefaktor K** | 1 | Verreken die ontvangstasie (drywing, antennas); bepaal deur vergelyking met 'n RMOB-waarnemer op dieselfde band |
| **Laai RMOB-lêer van skyf...** | | Lees 'n maandelikse RMOB-tekslêer (sien hieronder) |
| **Bepaal die eksponent uit die RMOB-lêer** | | Pas k aan op die gemeenskaplike ure van Collm en RMOB |
| **RMOB-waarnemer** | leeg | Naam van die waarnemer soos dit in die lêernaam verskyn (bv. `NAME_112026rmob.TXT` → `NAME`) |
| **Laai RMOB nou af** | | Laai die huidige maand se lêer van daardie waarnemer een keer af |
| **outomatiese aflaai elke 5 minute (aktiveer slegs met RMOB se toestemming)** | **af** | Sien [RMOB en outomatiese programme](#rmob-en-outomatiese-programme) |

Die oranje reël onder die kontroles wys die reël met die huidige getalle, bv. *N(144 MHz) = N(Collm 36,2 MHz) x (36,2/144)^3,00 x K = N x 0,01589 x 1,00*, die skalering van die duur en die IARU-maksimum ping op daardie frekwensie.

## Van die radar na die amateurband

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Bron:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45ste Nordic VUSHF, Mei 2025 – aantal en intensiteit van refleksies skaal met **λ³**, duur met **λ²** (432 MHz is 14–15 dB onder 144 MHz en duur 1/9). **Kontrole:** die λ³-afhanklikheid is dieselfde as in McKinley se onderdigte vergelyking. Met k = 3 word 1000 meteore/uur by Collm ongeveer **16 refleksies/uur op 144 MHz**; RMOB-waarnemers van GRAVES op 143,050 MHz tel gewoonlik **20 tot 140 eggo's/uur** (RMOB-bulletin, Junie 2018): die grootte-orde is versoenbaar, en die verskil is die stasiefaktor K. (Handleiding vgl. 44–45.)

## Volgende 24 uur

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Persistensie:** die geskaalde waarde van dieselfde uur van die vorige dag (of twee dae vroeër as dit ontbreek), gekorrigeer deur die verandering van die **padswermindeks** I (Σ ZHR × doeltreffendheid, sien [Berekening van doeltreffendheid](Efficiency-Calculation-af#die-model)). Die konstante 10 stel die sporadiese agtergrond voor en beperk die korreksie wanneer die indeks klein is. *Keuse van die program (handleiding vgl. 47).*

| Paneel | Inhoud |
|---|---|
| **Gemeet by Collm en geskaal na f MHz – gister en vandag (UTC)** | Collm-radarmeteore/uur; geskaalde waardes (oranje, regterskaal); die RMOB-tellings as dit gelaai is (groen, regterskaal) |
| **Eksperimentele voorspelling vir die volgende 24 uur by f MHz vir …** | Voorspelde refleksies/uur (stawe) en die padswermindeks (regterskaal) |
| Tabel | UTC-tyd · Collm selfde uur · Geskaal · Padswermindeks · Voorspelling /uur · **Beoordeling** |

**Beoordeling:** *goed* wanneer die voorspelling minstens 1,3 × die 24-uur-gemiddelde is, *redelik* vanaf 0,8 ×, *swak* daaronder. Dieselfde voorspelling verskyn in die kaart **EKSPERIMENTELE VOORSPELLING** en in die oranje ry van die [Berekening van doeltreffendheid](Efficiency-Calculation-af), en dit is die basis van die verwagte eggo's in die oortjie [GRAVES-radar](GRAVES-Radar-af#verwagte-eggos-eksperimenteel).

## RMOB-vergelyking

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) versamel die uurlikse meteoortellings van radiowaarnemers; baie in Italië luister na GRAVES op 143,050 MHz (Planetarium van Venesië, Faenza, Rovereto en ander).

**RMOB-lêers lees.** Twee teksformate word aanvaar:

| Formaat | Voorkoms | Opmerkings |
|---|---|---|
| Maandelikse lêer (Colorgramme / Spectrum Lab) | een ry per dag, `day| n| n| …` met 24 uurwaardes | die gewone `NAME_MMYYYYrmob.TXT` |
| Bulletintabel | kopreël ` UT |  1   2   3 …`, rye `0h|175 166 …` | as die lêer verskeie waarnemers bevat, word hulle een na die ander gelees: gebruik 'n lêer met 'n enkele waarnemer |

Maand en jaar kom uit die lêernaam (`…_MMYYYYrmob…`) of uit die kopreël; anders word die huidige maand gebruik (en die program sê so).

**Die eksponent aanpas.** Met K = 1, uit die mediaan van die RMOB/Collm-verhoudings oor die gemeenskaplike ure (minstens 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Keuse van die program (handleiding vgl. 46).* Die dialoog wys die gemeenskaplike ure, die mediaanverhouding en k; **Ja** pas k toe (en stel K = 1), **Nee** behou k = 3 – stel dan K met die hand op die waarde wat in dieselfde dialoog voorgestel word.

## RMOB en outomatiese programme

RMOB vra dat **outomatiese programme nie sy lêers aflaai nie**. Daarom is die **outomatiese aflaai aan die begin af** en moet dit **slegs aangeskakel word nadat jy RMOB om toestemming gevra het**. Daarsonder kan jy altyd **Laai RMOB-lêer van skyf...** gebruik of **Laai RMOB nou af** druk wanneer jy dit nodig het.

Die aflaai-adres is 'n sjabloon in `config.ini` (sleutel `rmob_url`, verstek `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, waar `{NOME}` die waarnemer is en `{MMAAAA}` maand en jaar); afgelaaide lêers word in `data/radar/` bewaar.
