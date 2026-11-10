[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-br) · **Dansk** · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh)

# Radarflux

*Fane: Live og realtidsdata › Radarflux.*

[![Radarflux](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Denne fane viser, hvad professionelle meteorradarer tæller **lige nu**: meteortællinger pr. time og sporhøjder fra **Collms** SKiYMET-radar (Leipzig Universitet / IAP Kühlungsborn, Tyskland, 36,2 MHz) og det seneste billede fra radaren i **Sodankylä** (SGO, Finland). Collm-tællingerne indgår i vurderingen for dit bånd og i [Eksperimentelle prognoser](Experimental-Forecasts-da); den målte sporhøjde indgår i hele geometrien.

## Betjening

| Element | Hvad det gør |
|---|---|
| **Hent nu** | Kontrollerer alle eksterne kilder på én gang. |
| **Automatisk opdatering af alle kilder hvert 5. minut** | Slået til som standard. Hvert 5. minut kontrolleres alle kilder, og **kun dem, der er ændret**, hentes igen (*uændret (kontrolleret kl. … UTC)* / *nye data kl. … UTC*). |
| **λ-eksponent (SM6FHZ)** | Eksponenten k i frekvensreglen, standard 3 (1–4). |

## Hvad der vises

| Panel | Indhold |
|---|---|
| **Meteorer/time – i går og i dag (UTC)** | Cyan søjler = Collm-tællinger (gyldige), røde søjler = kasserede, tyk orange linje = *vurdering ved … MHz* på højre skala |
| **Sporhøjder (Collm)** | Meteorer pr. km højde mellem 70 og 110 km med hyppigste højde (typetal), middelværdi, median og standardafvigelse |
| Collm-billede | Den originale SKiYMET-graf, som den er hentet |
| Sodankylä-billede | Det seneste billede med meteortællinger fra radaren i Sodankylä (vises kun; formatet aflæses ikke) |

Linjen over graferne fortæller, hvornår Collm-grafen blev aflæst, og hvilken lodret skala der blev fundet (*skala aflæst fra grafen: 0-… meteorer/time*).

## Sådan aflæses Collm-grafen

Collm-grafen (720 × 720 pixel, rene farver) har faste aksepositioner, men radaren **tilpasser den lodrette skala hver dag** til de målte værdier (fx 0–1,2·10³ den 5.11.2026 og 0–1,0·10³ den 6.11.2026, med flyttede skalastreger). YA-MS gør derfor følgende:

1. finder aksens lange skalastreger;
2. **aflæser etiketterne** ved den øverste skalastreg og ved nul ved at sammenligne hvert tegn med grafens punktmatrix-skrift;
3. for hver time i (0–47, i går og i dag) tages den midterste kolonne og den første cyan pixel fra toppen, y:

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top og y0 er rækkerne for den øverste skalastreg og for nul, N_top værdien aflæst på den øverste etiket (×1000). Opløsning: ca. 7–8 meteorer/time pr. pixel. *Programmets valg (manualens lign. 42).*

Hvis en etiket ikke kan aflæses, falder programmet tilbage på kalibreringen fra 5.11.2026 (**kalibreret skala 0-1200 meteorer/time**) og siger det med orange: *Kan ikke aflæse fluxens lodrette skala (øverste etiket: …): værdierne skal kontrolleres.* Hvis selve grafens format ændres (*Grafens format er ændret (…x…): kan ikke aflæses* eller *Fluxakserne blev ikke fundet på den forventede plads*), skal aflæsningen kalibreres igen: meld det venligst (se [Bidrag](Contributing-and-Contacts-da)).

### Sporhøjder

Ud fra højdehistogrammet (n_k meteorer i km k, middelhøjde h_k):

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*Manualens lign. 43.* Med flueben i **fra radar** (række 2 af betjeningselementerne) bliver **typetallet** sporhøjden for alle beregninger. Kontrol: grafen fra 5.11.2026 – typetal 89,5 km, middelværdi 88,6 km, standardafvigelse 6,8 km, hvilket bekræfter de ca. 90 km i artiklen af Cerrotta–Sartori (SKiYMET-middelværdi).

Hvis skalaen på højdegrafen ændres, advarer programmet: *højdestatistikken (typetal, middelværdi, median) er stadig gyldig, de absolutte tællinger er ikke.*

## Vurdering for dit bånd

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

Eksperimentelle regler af **SM6FHZ** (VUSHF 2025): antal og intensitet af refleksioner skalerer med λ³, varigheden med λ²; λ³-afhængigheden er den samme som i McKinleys ligning for underdense spor. IARU Region 1's maksimale pingvarighed vises også (1000 ms ved 50 MHz, 500 ms ved 70 MHz, 100 ms ved 144 MHz, 13 ms ved 432 MHz). Værdierne er vejledende og bør sammenlignes med erfaringen på båndet. Stationsfaktoren K og sammenligningen med RMOB findes i [Eksperimentelle prognoser](Experimental-Forecasts-da).

## Uden forbindelse

Hvis ingen kilde kan nås, vises en meddelelse **én gang**: *Ingen internetforbindelse. Radar- og RMOB-data kan ikke opdateres: programmet bruger de senest gemte data og prøver selv igen hvert 5. minut.* Statuslinjen nederst bliver rød (*INGEN INTERNETFORBINDELSE …*), indtil forbindelsen vender tilbage (*Forbindelsen er genoprettet.*).

## Arkiver og kilder

| Fil (i `data/`) | Indhold |
|---|---|
| `flusso_collm.csv` | Timearkiv med fluxen aflæst fra Collm (timer, der allerede findes, opdateres) |
| `quote_collm.csv` | Arkiv med sporhøjderne |
| `radar/` | Senest hentede billeder (og RMOB-filer) |
| `fonti_radar.csv` | Adresserne på radarkilderne, `attivo=1/0` slår hver enkelt til/fra |

| Kilde | Frekvens | Bemærkninger |
|---|---|---|
| Collm-meteorradaren, Leipzig Universitet (LIM) og IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | opdateres hver time i minut 10 UTC; flux i går + i dag, højdefordeling |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | kun billede (radaren er ved at blive opdateret, DECC-projektet) |
| swan.ms (kopi af Collm) | 36,2 MHz | slået fra som standard; brug kun med tilladelse fra DL1DBC |

> Radardata tilhører de respektive institutioner (Leipzig Universitet / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
