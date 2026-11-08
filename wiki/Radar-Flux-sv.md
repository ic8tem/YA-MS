**English** · [Русский](Radar-Flux-ru) · [Deutsch](Radar-Flux-de) · [日本語](Radar-Flux-ja)

# Radarflöde

*Flik: Live och realtidsdata › Radarflöde.*

[![Radarflöde](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Den här fliken visar vad professionella meteorradarer räknar **just nu**: antalet meteorer per timme och spårhöjderna från SKiYMET-radarn i **Collm** (Leipzigs universitet / IAP Kühlungsborn, Tyskland, 36,2 MHz), samt den senaste bilden från radarn i **Sodankylä** (SGO, Finland). Räkningarna från Collm matar uppskattningen för ditt band och [Experimentella prognoser](Experimental-Forecasts-sv); den uppmätta spårhöjden matar hela geometrin.

## Reglage

| Reglage | Vad det gör |
|---|---|
| **Hämta nu** | Kontrollerar alla externa källor på en gång. |
| **Automatisk uppdatering av alla källor var 5:e minut** | På som standard. Var 5:e minut kontrolleras alla källor och **endast de som har ändrats** hämtas på nytt (*oförändrat (kontrollerat kl. … UTC)* / *nya data kl. … UTC*). |
| **λ-exponent (SM6FHZ)** | Exponenten k i frekvensregeln, standard 3 (1–4). |

## Vad som visas

| Panel | Innehåll |
|---|---|
| **Meteorer/timme – igår och idag (UTC)** | Cyan staplar = räkningar från Collm (giltiga), röda staplar = kasserade, tjock orange linje = *uppskattning vid … MHz* mot den högra skalan |
| **Spårhöjder (Collm)** | Meteorer per km höjd mellan 70 och 110 km, med vanligaste höjd (typvärde), medelvärde, median och standardavvikelse |
| Bild från Collm | Originaldiagrammet från SKiYMET, som det hämtades |
| Bild från Sodankylä | Den senaste bilden med meteorräkningar från radarn i Sodankylä (visas endast; dess format läses inte) |

Raden ovanför diagrammen anger när Collm-diagrammet lästes och vilken vertikal skala som hittades (*skala avläst från diagrammet: 0-… meteorer/timme*).

## Hur Collm-diagrammet läses

Collm-diagrammet (720 × 720 pixlar, rena färger) har fasta axelpositioner, men radarn **anpassar den vertikala skalan varje dag** efter de uppmätta värdena (t.ex. 0–1,2·10³ den 5/11/2026 och 0–1,0·10³ den 6/11/2026, med flyttade skalstreck). YA-MS gör därför så här:

1. hittar axelns långa skalstreck;
2. **läser etiketterna** vid det översta skalstrecket och vid nollan genom att jämföra varje tecken med diagrammets punktmatristypsnitt;
3. för varje timme i (0–47, igår och idag) tas mittkolumnen och den första cyan pixeln uppifrån, y:

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top och y0 är raderna för det översta skalstrecket och för nollan, N_top värdet som lästs på den översta etiketten (×1000). Upplösning: omkring 7–8 meteorer/timme per pixel. *Programmets val (handboken ekv. 42).*

Om en etikett inte kan läsas faller programmet tillbaka på kalibreringen från 5/11/2026 (**kalibrerad skala 0-1200 meteorer/timme**) och säger det i orange: *Kan inte läsa flödets vertikala skala (översta etiketten: …): värdena bör kontrolleras.* Om själva diagramformatet ändras (*Diagrammets format har ändrats (…x…): kan inte läsas* eller *Flödesaxlarna hittades inte på förväntad plats*) måste avläsningen kalibreras om: rapportera det gärna (se [Bidra](Contributing-and-Contacts-sv)).

### Spårhöjder

Ur höjdhistogrammet (n_k meteorer vid km k, medelhöjd h_k):

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*Handboken ekv. 43.* Med **från radar** ikryssat (rad 2 bland reglagen) blir **typvärdet** spårhöjden i alla beräkningar. Kontroll: diagrammet från 5/11/2026 – typvärde 89,5 km, medelvärde 88,6 km, standardavvikelse 6,8 km, vilket bekräftar de ~90 km som anges i artikeln av Cerrotta–Sartori (medelvärde enligt SKiYMET).

Om höjddiagrammets skala ändras varnar programmet: *höjdstatistiken (typvärde, medel, median) gäller fortfarande, de absoluta antalen inte.*

## Uppskattning för ditt band

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

Experimentella regler av **SM6FHZ** (VUSHF 2025): reflexernas antal och intensitet skalar med λ³, varaktigheten med λ²; λ³-beroendet är detsamma som i McKinleys ekvation för underdensa spår. IARU Region 1:s maximala pinglängd visas också (1000 ms på 50 MHz, 500 ms på 70 MHz, 100 ms på 144 MHz, 13 ms på 432 MHz). Värdena är vägledande och ska jämföras med erfarenheten i luften. Stationsfaktorn K och jämförelsen med RMOB finns i [Experimentella prognoser](Experimental-Forecasts-sv).

## Utan nätverk

Om ingen källa kan nås visas ett meddelande **en gång**: *Ingen internetanslutning. Radar- och RMOB-data kan inte uppdateras: programmet använder senast sparade data och försöker igen automatiskt var 5:e minut.* Statusraden längst ned blir röd (*INGEN INTERNETANSLUTNING …*) tills anslutningen kommer tillbaka (*Anslutningen återställd.*).

## Arkiv och källor

| Fil (i `data/`) | Innehåll |
|---|---|
| `flusso_collm.csv` | Timarkiv över flödet avläst från Collm (timmar som redan finns uppdateras) |
| `quote_collm.csv` | Arkiv över spårhöjderna |
| `radar/` | Senast hämtade bilder (och RMOB-filer) |
| `fonti_radar.csv` | Radarkällornas adresser, `attivo=1/0` för att aktivera/avaktivera var och en |

| Källa | Frekvens | Anmärkningar |
|---|---|---|
| Collm meteor radar, Leipzigs universitet (LIM) och IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | uppdateras varje timme vid minut 10 UTC; flöde igår + idag, höjdfördelning |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | endast bild (radarn håller på att uppgraderas, projektet DECC) |
| swan.ms (kopia av Collm) | 36,2 MHz | avaktiverad som standard; används endast med tillstånd från DL1DBC |

> Radardata tillhör sina institutioner (Leipzigs universitet / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
