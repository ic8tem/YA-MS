[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Dansk](Experimental-Forecasts-da) · **Norsk** · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh)

# Eksperimentelle prognoser

*Fane: Prognoseberegning › Eksperimentelle prognoser.*

[![Eksperimentelle prognoser](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Denne fanen gjør om meteortellingene fra **Collm-radaren (36,2 MHz)** til et estimat av **refleksjoner per time på et amatørbånd** (144 MHz som standard, vilkårlig frekvens fra 28 til 1300 MHz), lager en prognose for de **neste 24 timene** for strekningen din og lar deg **sammenligne** estimatet med en **RMOB**-observatør – for eksempel en som lytter på GRAVES på 143,050 MHz.

> Alt her er **eksperimentelt**: frekvensregelen er en empirisk regel, og stasjonsfaktoren avhenger av stasjonen din. Bruk tallene til å sammenligne timer og dager, og sjekk dem på båndet.

## Kontroller

| Kontroll | Standard | Hva den gjør |
|---|---|---|
| **Målfrekvens MHz** | 144 | Prognosens frekvens (28–1300 MHz) |
| **λ^k-eksponent** | 3 | Eksponenten k i frekvensregelen (SM6FHZ: 3) |
| **Stasjonsfaktor K** | 1 | Tar hensyn til mottakerstasjonen (effekt, antenner); finnes ved sammenligning med en RMOB-observatør på samme bånd |
| **Last inn RMOB-fil fra disk...** | | Leser en månedlig RMOB-tekstfil (se nedenfor) |
| **Finn eksponenten fra RMOB-filen** | | Tilpasser k ut fra de felles timene for Collm og RMOB |
| **RMOB-observatør** | tom | Observatørens navn slik det står i filnavnet (f.eks. `NAME_112026rmob.TXT` → `NAME`) |
| **Last ned RMOB nå** | | Laster ned denne observatørens fil for inneværende måned én gang |
| **automatisk nedlasting hvert 5. minutt (aktiver bare med tillatelse fra RMOB)** | **av** | Se [RMOB og automatiske programmer](#rmob-og-automatiske-programmer) |

Den oransje linjen under kontrollene viser regelen med de aktuelle tallene, f.eks. *N(144 MHz) = N(Collm 36,2 MHz) x (36,2/144)^3,00 x K = N x 0,01589 x 1,00*, skaleringen av varigheten og IARU maksimal ping på den frekvensen.

## Fra radaren til amatørbåndet

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Kilde:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, mai 2025 – antall og intensitet av refleksjoner skalerer med **λ³**, varigheten med **λ²** (432 MHz ligger 14–15 dB under 144 MHz og varer 1/9). **Kontroll:** λ³-avhengigheten er den samme som i McKinleys likning for underdense spor. Med k = 3 blir 1000 meteorer/time i Collm til ca. **16 refleksjoner/time på 144 MHz**; RMOB-observatører som lytter på GRAVES på 143,050 MHz, teller vanligvis **20 til 140 ekkoer/time** (RMOB-bulletin, juni 2018): størrelsesordenen er forenlig, og forskjellen er stasjonsfaktoren K. (Håndbokens likn. 44–45.)

## De neste 24 timene

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Persistens:** den omregnede verdien for samme time dagen før (eller to dager før hvis den mangler), korrigert for endringen i **svermindeksen for strekningen** I (Σ ZHR × effektivitet, se [Effektivitetsberegning](Efficiency-Calculation-nb#modellen)). Konstanten 10 representerer den sporadiske bakgrunnen og begrenser korreksjonen når indeksen er liten. *Programmets valg (håndbokens likn. 47).*

| Panel | Innhold |
|---|---|
| **Målt i Collm og omregnet til f MHz – i går og i dag (UTC)** | Collm-radarens meteorer/time; omregnede verdier (oransje, høyre skala); RMOB-tellingene hvis de er lastet inn (grønn, høyre skala) |
| **Eksperimentell prognose for de neste 24 timene på f MHz for …** | Prognose for refleksjoner/time (søyler) og svermindeksen for strekningen (høyre skala) |
| Tabell | UTC-tid · Collm samme time · Omregnet · Svermindeks for strekningen · Prognose /time · **Vurdering** |

**Vurdering:** *god* når prognosen er minst 1,3 × gjennomsnittet over 24 timer, *middels* fra 0,8 ×, *svak* under det. Samme prognose vises i panelet **EKSPERIMENTELL PROGNOSE** og i den oransje raden i [Effektivitetsberegning](Efficiency-Calculation-nb), og den er grunnlaget for de forventede ekkoene i fanen [Radar GRAVES](GRAVES-Radar-nb#forventede-ekkoer-eksperimentelt).

## Sammenligning med RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) samler radioobservatørers timetellinger av meteorer; mange i Italia lytter på GRAVES på 143,050 MHz (Planetariet i Venezia, Faenza, Rovereto og andre).

**Lese RMOB-filer.** To tekstformater godtas:

| Format | Utseende | Merknader |
|---|---|---|
| Månedsfil (Colorgramme / Spectrum Lab) | én rad per dag, `day| n| n| …` med 24 timeverdier | den vanlige `NAME_MMYYYYrmob.TXT` |
| Bulletintabell | overskrift ` UT |  1   2   3 …`, rader `0h|175 166 …` | inneholder filen flere observatører, leses de etter hverandre: bruk en fil med bare én observatør |

Måned og år hentes fra filnavnet (`…_MMYYYYrmob…`) eller fra overskriften; ellers brukes inneværende måned (og programmet sier fra).

**Tilpasse eksponenten.** Med K = 1, ut fra medianen av forholdene RMOB/Collm over de felles timene (minst 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Programmets valg (håndbokens likn. 46).* Dialogen viser de felles timene, medianforholdet og k; **Ja** bruker k (og setter K = 1), **Nei** beholder k = 3 – juster da K for hånd til verdien som foreslås i samme dialog.

## RMOB og automatiske programmer

RMOB ber om at **automatiske programmer ikke henter filene deres**. Derfor er **automatisk nedlasting avslått** fra start og bør bare slås på **etter at du har bedt RMOB om tillatelse**. Uten den kan du alltid bruke **Last inn RMOB-fil fra disk...** eller trykke **Last ned RMOB nå** når du trenger det.

Nedlastingsadressen er en mal i `config.ini` (nøkkelen `rmob_url`, standard `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, der `{NOME}` er observatøren og `{MMAAAA}` måned og år); nedlastede filer lagres i `data/radar/`.
