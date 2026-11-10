[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-br) · [Dansk](Radar-Flux-da) · **Norsk** · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Magyar](Radar-Flux-hu) · [Română](Radar-Flux-ro) · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [ไทย](Radar-Flux-th) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · [中文 (繁體)](Radar-Flux-zh-tw)

# Radarfluks

*Fane: Direkte og sanntidsdata › Radarfluks.*

[![Radarfluks](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Denne fanen viser hva profesjonelle meteorradarer teller **akkurat nå**: meteortellinger per time og sporhøyder fra SKiYMET-radaren i **Collm** (Universitetet i Leipzig / IAP Kühlungsborn, Tyskland, 36,2 MHz), og det siste bildet fra radaren i **Sodankylä** (SGO, Finland). Collm-tellingene brukes i estimatet for ditt bånd og i [Eksperimentelle prognoser](Experimental-Forecasts-nb); den målte sporhøyden brukes i hele geometrien.

## Kontroller

| Kontroll | Hva den gjør |
|---|---|
| **Last ned nå** | Sjekker alle eksterne kilder på én gang. |
| **Automatisk oppdatering av alle kilder hvert 5. minutt** | På som standard. Hvert 5. minutt sjekkes alle kildene, og **bare de som er endret**, lastes ned på nytt (*uendret (sjekket kl. … UTC)* / *nye data kl. … UTC*). |
| **λ-eksponent (SM6FHZ)** | Eksponenten k i frekvensregelen, standard 3 (1–4). |

## Hva som vises

| Panel | Innhold |
|---|---|
| **Meteorer/time – i går og i dag (UTC)** | Cyan søyler = Collm-tellinger (gyldige), røde søyler = forkastet, tykk oransje linje = *estimat på … MHz* på høyre skala |
| **Sporhøyder (Collm)** | Meteorer per km høyde mellom 70 og 110 km, med hyppigste høyde (typetall), middel, median og standardavvik |
| Collm-bilde | Det originale SKiYMET-diagrammet, slik det er lastet ned |
| Sodankylä-bilde | Det siste bildet med meteortellinger fra radaren i Sodankylä (vises bare; formatet leses ikke) |

Linjen over diagrammene forteller når Collm-diagrammet ble lest, og hvilken vertikal skala som ble funnet (*skala lest fra diagrammet: 0-… meteorer/time*).

## Slik leses Collm-diagrammet

Collm-diagrammet (720 × 720 piksler, rene farger) har faste akseposisjoner, men radaren **tilpasser den vertikale skalaen hver dag** til de målte verdiene (f.eks. 0–1,2·10³ den 5.11.2026 og 0–1,0·10³ den 6.11.2026, med flyttede skalastreker). YA-MS gjør derfor følgende:

1. finner de lange skalastrekene på aksen;
2. **leser etikettene** ved den øverste skalastreken og ved null ved å sammenligne hvert tegn med diagrammets punktmatriseskrift;
3. for hver time i (0–47, i går og i dag) tas midtkolonnen og den første cyan pikselen ovenfra, y:

```math
x_i = 101 + (i+0{.}5)\,\frac{676-101}{48},\qquad N = (y_0-y)\,\frac{N_{top}}{y_0-y_{top}}
```

y_top og y0 er radene for den øverste skalastreken og for null, N_top verdien lest på den øverste etiketten (×1000). Oppløsning: ca. 7–8 meteorer/time per piksel. *Programmets valg (håndbokens likn. 42).*

Hvis en etikett ikke kan leses, faller programmet tilbake på kalibreringen fra 5.11.2026 (**kalibrert skala 0-1200 meteorer/time**) og sier fra i oransje: *Kan ikke lese den vertikale fluksskalaen (øverste etikett: …): verdiene må kontrolleres.* Hvis selve diagramformatet endres (*Diagramformatet er endret (…x…): kan ikke leses* eller *Fluksaksene ble ikke funnet på forventet sted*), må avlesningen kalibreres på nytt: meld fra om det (se [Bidra](Contributing-and-Contacts-nb)).

### Sporhøyder

Fra høydehistogrammet (n_k meteorer i km k, middelhøyde h_k):

```math
\hat{h} = h_{k^*},\ k^* = \arg\max_k n_k,\qquad \bar{h} = \frac{\sum_k n_k h_k}{\sum_k n_k},\qquad s = \sqrt{\frac{\sum_k n_k (h_k-\bar{h})^2}{\sum_k n_k}}
```

*Håndbokens likn. 43.* Med **fra radar** avkrysset (rad 2 av kontrollene) blir **typetallet** sporhøyden for alle beregninger. Kontroll: diagrammet fra 5.11.2026 – typetall 89,5 km, middel 88,6 km, standardavvik 6,8 km, som bekrefter de ca. 90 km i artikkelen av Cerrotta–Sartori (SKiYMET-middel).

Hvis skalaen i høydediagrammet endres, varsler programmet: *høydestatistikken (typetall, middel, median) er fortsatt gyldig, de absolutte tellingene ikke.*

## Estimat for ditt bånd

```math
N(f) = N_{Collm}(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k},\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

Eksperimentelle regler fra **SM6FHZ** (VUSHF 2025): antall og intensitet av refleksjoner skalerer med λ³, varigheten med λ² (hos McKinley er λ³ effekten fra ett spor; antall spor skalerer omtrent som λ^1,5, og ved foroverspredning øker varighetene i tillegg med sec²φ: se [Eksperimentelle prognoser](Experimental-Forecasts-nb)). IARU Region 1s maksimale pingvarighet vises også (1000 ms på 50 MHz, 500 ms på 70 MHz, 100 ms på 144 MHz, 13 ms på 432 MHz). Verdiene er veiledende og bør sammenlignes med erfaring på båndet. Stasjonsfaktoren K og sammenligningen med RMOB står i [Eksperimentelle prognoser](Experimental-Forecasts-nb).

## Uten nett

Hvis ingen kilde kan nås, vises en melding **én gang**: *Ingen internettforbindelse. Radar- og RMOB-data kan ikke oppdateres: programmet bruker de sist lagrede dataene og prøver på nytt av seg selv hvert 5. minutt.* Statuslinjen nederst blir rød (*INGEN INTERNETTFORBINDELSE …*) til forbindelsen er tilbake (*Forbindelsen er gjenopprettet.*).

## Arkiver og kilder

| Fil (i `data/`) | Innhold |
|---|---|
| `flusso_collm.csv` | Timearkiv med fluksen lest fra Collm (timer som allerede finnes, oppdateres) |
| `quote_collm.csv` | Arkiv med sporhøydene |
| `radar/` | Sist nedlastede bilder (og RMOB-filer) |
| `fonti_radar.csv` | Adressene til radarkildene, `attivo=1/0` slår hver av eller på |

| Kilde | Frekvens | Merknader |
|---|---|---|
| Collm meteorradar, Universitetet i Leipzig (LIM) og IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | oppdateres hver time i minutt 10 UTC; fluks i går + i dag, høydefordeling |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | bare bilde (radaren oppgraderes, DECC-prosjektet) |
| swan.ms (kopi av Collm) | 36,2 MHz | avslått som standard; brukes bare med tillatelse fra DL1DBC |

> Radardataene tilhører de respektive institusjonene (Universitetet i Leipzig / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
