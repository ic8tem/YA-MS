[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · **Svenska** · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh)

# Experimentella prognoser

*Flik: Prognosberäkning › Experimentella prognoser.*

[![Experimentella prognoser](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Den här fliken omvandlar meteorräkningarna från **Collm-radarn (36,2 MHz)** till en uppskattning av **reflexer per timme på ett amatörband** (144 MHz som standard, valfri frekvens från 28 till 1300 MHz), gör en prognos för **de närmaste 24 timmarna** för din sträcka och låter dig **jämföra** uppskattningen med en **RMOB**-observatör – till exempel en som lyssnar på GRAVES på 143,050 MHz.

> Allt här är **experimentellt**: frekvensregeln är en empirisk regel, och stationsfaktorn beror på din station. Använd siffrorna för att jämföra timmar och dagar, och kontrollera dem i luften.

## Reglage

| Reglage | Standard | Vad det gör |
|---|---|---|
| **Målfrekvens MHz** | 144 | Prognosens frekvens (28–1300 MHz) |
| **λ^k-exponent** | 3 | Exponenten k i frekvensregeln (SM6FHZ: 3) |
| **Stationsfaktor K** | 1 | Tar hänsyn till den mottagande stationen (effekt, antenner); härleds genom jämförelse med en RMOB-observatör på samma band |
| **Läs in RMOB-fil från disk...** | | Läser en månatlig RMOB-textfil (se nedan) |
| **Härled exponenten från RMOB-filen** | | Anpassar k utifrån de timmar som Collm och RMOB har gemensamt |
| **RMOB-observatör** | tom | Observatörens namn så som det står i filnamnet (t.ex. `NAME_112026rmob.TXT` → `NAME`) |
| **Hämta RMOB nu** | | Hämtar den aktuella månadens fil för den observatören en gång |
| **automatisk hämtning var 5:e minut (aktivera endast med tillstånd från RMOB)** | **av** | Se [RMOB och automatiska program](#rmob-och-automatiska-program) |

Den orange raden under reglagen visar regeln med de aktuella siffrorna, t.ex. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, omräkningen av varaktigheten och IARU:s maximala pinglängd vid den frekvensen.

## Från radarn till amatörbandet

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Källa:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, maj 2025 – reflexernas antal och intensitet skalar med **λ³**, varaktigheten med **λ²** (432 MHz ligger 14–15 dB under 144 MHz och varar 1/9 så länge). **Kontroll:** λ³-beroendet är detsamma som i McKinleys ekvation för underdensa spår. Med k = 3 blir 1000 meteorer/timme i Collm omkring **16 reflexer/timme på 144 MHz**; RMOB-observatörer av GRAVES på 143,050 MHz räknar vanligen **20 till 140 ekon/timme** (RMOB-bulletinen, juni 2018): storleksordningen är förenlig, och skillnaden är stationsfaktorn K. (Handboken ekv. 44–45.)

## De närmaste 24 timmarna

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Persistens:** det omräknade värdet för samma timme dagen innan (eller två dagar innan om det saknas), korrigerat med förändringen i **sträckans svärmindex** I (Σ ZHR × effektivitet, se [Effektivitetsberäkning](Efficiency-Calculation-sv#modellen)). Konstanten 10 representerar den sporadiska bakgrunden och begränsar korrektionen när indexet är litet. *Programmets val (handboken ekv. 47).*

| Panel | Innehåll |
|---|---|
| **Uppmätt i Collm och omräknat till f MHz – igår och idag (UTC)** | Collm-radarns meteorer/timme; omräknade värden (orange, högra skalan); RMOB-räkningarna om de är inlästa (grönt, högra skalan) |
| **Experimentell prognos för de närmaste 24 timmarna vid f MHz för …** | Prognostiserade reflexer/timme (staplar) och sträckans svärmindex (högra skalan) |
| Tabell | UTC-tid · Collm samma timme · Omräknat · Sträckans svärmindex · Prognos /timme · **Bedömning** |

**Bedömning:** *bra* när prognosen är minst 1,3 × medelvärdet för 24 timmar, *medel* från 0,8 ×, *dålig* därunder. Samma prognos visas i kortet **EXPERIMENTELL PROGNOS** och i den orange raden i [Effektivitetsberäkning](Efficiency-Calculation-sv), och den är grunden för de förväntade ekona i fliken [GRAVES-radar](GRAVES-Radar-sv#förväntade-ekon-experimentellt).

## Jämförelse med RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) samlar radioobservatörers meteorräkningar per timme; många i Italien lyssnar på GRAVES på 143,050 MHz (planetariet i Venedig, Faenza, Rovereto med flera).

**Läsa RMOB-filer.** Två textformat godtas:

| Format | Utseende | Anmärkningar |
|---|---|---|
| Månadsfil (Colorgramme / Spectrum Lab) | en rad per dag, `day| n| n| …` med 24 timvärden | den vanliga `NAME_MMYYYYrmob.TXT` |
| Bulletintabell | rubrik ` UT |  1   2   3 …`, rader `0h|175 166 …` | om filen innehåller flera observatörer läses de en efter en: använd en fil med en enda observatör |

Månad och år tas från filnamnet (`…_MMYYYYrmob…`) eller från rubriken; annars används innevarande månad (och programmet säger det).

**Anpassa exponenten.** Med K = 1, utifrån medianen av kvoterna RMOB/Collm över de gemensamma timmarna (minst 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Programmets val (handboken ekv. 46).* Dialogrutan visar de gemensamma timmarna, medianen av kvoterna och k; **Ja** tillämpar k (och sätter K = 1), **Nej** behåller k = 3 – justera då K för hand till det värde som föreslås i samma dialogruta.

## RMOB och automatiska program

RMOB ber att **automatiska program inte hämtar dess filer**. Därför är **automatisk hämtning avstängd** från början och bör aktiveras **först efter att du har bett RMOB om tillstånd**. Utan det kan du alltid använda **Läs in RMOB-fil från disk...** eller trycka på **Hämta RMOB nu** när du behöver.

Hämtningsadressen är en mall i `config.ini` (nyckeln `rmob_url`, standard `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, där `{NOME}` är observatören och `{MMAAAA}` månad och år); hämtade filer sparas i `data/radar/`.
