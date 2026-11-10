[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-br) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · **Latviešu** · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Magyar](Radar-Flux-hu) · [Română](Radar-Flux-ro) · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [ไทย](Radar-Flux-th) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · [中文 (繁體)](Radar-Flux-zh-tw)

# Radara meteoru skaits

*Cilne: Tiešsaiste un reāllaika dati › Radara meteoru skaits.*

[![Radara meteoru skaits](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Šī cilne rāda, ko profesionālie meteoru radari skaita **tagad**: meteoru skaitu stundā un sliežu augstumus no **Collm** SKiYMET radara (Leipcigas Universitāte / IAP Kühlungsborn, Vācija, 36,2 MHz) un jaunāko **Sodankylä** radara (SGO, Somija) attēlu. Collm skaiti baro novērtējumu tavai joslai un [Eksperimentālas prognozes](Experimental-Forecasts-lv); izmērītais sliežu augstums baro visu ģeometriju.

## Vadība

| Vadīkla | Ko tā dara |
|---|---|
| **Lejupielādēt tagad** | Uzreiz pārbauda visus ārējos avotus. |
| **Visu avotu automātiska atjaunināšana ik pēc 5 minūtēm** | Noklusējumā ieslēgta. Ik pēc 5 minūtēm tiek pārbaudīti visi avoti un no jauna lejupielādēti **tikai tie, kas mainījušies** (*nemainīgs (pārbaudīts … UTC)* / *jauni dati … UTC*). |
| **λ kāpinātājs (SM6FHZ)** | Frekvences likuma kāpinātājs k, noklusējumā 3 (1–4). |

## Kas tiek rādīts

| Panelis | Saturs |
|---|---|
| **Meteori/stundā – vakar un šodien (UTC)** | Ciānas joslas = Collm skaiti (derīgie), sarkanas joslas = atmestie, bieza oranža līnija = *novērtējums pie … MHz* pēc labās skalas |
| **Sliežu augstumi (Collm)** | Meteori uz augstuma km starp 70 un 110 km, ar biežāko augstumu (modu), vidējo, mediānu un standartnovirzi |
| Collm attēls | Oriģinālais SKiYMET grafiks, kā lejupielādēts |
| Sodankylä attēls | Jaunākais Sodankylä radara meteoru skaita attēls (tikai parādīts; tā formāts netiek nolasīts) |

Rinda virs grafikiem norāda, kad Collm grafiks nolasīts un kāda vertikālā skala atrasta (*skala nolasīta no grafika: 0-… meteori/stundā*).

## Kā tiek nolasīts Collm grafiks

Collm grafikam (720 × 720 pikseļi, tīras krāsas) asu vietas ir fiksētas, bet radars **katru dienu pielāgo vertikālo skalu** izmērītajām vērtībām (piem. 0–1,2·10³ 5/11/2026 un 0–1,0·10³ 6/11/2026, ar pārvietotām iedaļām). Tāpēc YA-MS:

1. atrod ass garās iedaļas;
2. **nolasa augstākās iedaļas un nulles etiķetes**, salīdzinot katru rakstzīmi ar grafika punktu matricas fontu;
3. katrai stundai i (0–47, vakar un šodien) ņem centrālo kolonnu un pirmo ciānas pikseli no augšas, y:

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top un y0 ir augstākās iedaļas un nulles rindas, N_top – augstākajā etiķetē nolasītā vērtība (×1000). Izšķirtspēja: ap 7–8 meteoriem stundā uz pikseli. *Programmas izvēle (rokasgrāmatas 42. vien.).*

Ja etiķeti nevar nolasīt, programma izmanto 5/11/2026 kalibrāciju (**kalibrēta skala 0-1200 meteori/stundā**) un par to paziņo oranžā krāsā: *Nevar nolasīt meteoru skaita vertikālo skalu (augšējā etiķete: …): vērtības jāpārbauda.* Ja mainās pats grafika formāts (*Grafika formāts mainījies (…x…): nolasīt nav iespējams* vai *Meteoru skaita grafika asis nav atrastas gaidītajā vietā*), nolasīšana ir jāpārkalibrē: lūdzu, ziņo par to (sk. [Līdzdalība](Contributing-and-Contacts-lv)).

### Sliežu augstumi

No augstumu histogrammas (n_k meteori km k, vidējais augstums h_k):

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*Rokasgrāmatas 43. vien.* Ja atzīmēts **no radara** (vadības 2. rinda), **moda** kļūst par visu aprēķinu sliežu augstumu. Pārbaude: 5/11/2026 grafiks – moda 89,5 km, vidējais 88,6 km, standartnovirze 6,8 km, kas apstiprina Cerrotta–Sartori raksta ~90 km (SKiYMET vidējais).

Ja augstumu grafika skala mainās, programma brīdina: *augstumu statistika (moda, vidējais, mediāna) paliek derīga, absolūtie skaiti – ne.*

## Novērtējums tavai joslai

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

**SM6FHZ** eksperimentālie likumi (VUSHF 2025): atstarojumu skaits un intensitāte mainās ar λ³, ilgums ar λ²; λ³ atkarība ir tā pati, kas McKinley zema blīvuma vienādojumā. Tiek parādīts arī IARU 1. reģiona maksimālais pinga ilgums (1000 ms 50 MHz, 500 ms 70 MHz, 100 ms 144 MHz, 13 ms 432 MHz). Vērtības ir orientējošas, salīdzināšanai ar pieredzi ēterā. Stacijas koeficients K un salīdzinājums ar RMOB ir cilnē [Eksperimentālas prognozes](Experimental-Forecasts-lv).

## Bez tīkla

Ja neviens avots nav sasniedzams, **vienu reizi** parādās ziņojums: *Nav interneta savienojuma. Radaru un RMOB datus nevar atjaunināt: programma izmanto pēdējos saglabātos datus un pati mēģina vēlreiz ik pēc 5 minūtēm.* Statusa josla apakšā kļūst sarkana (*NAV INTERNETA SAVIENOJUMA …*), līdz savienojums atjaunojas (*Savienojums atjaunots.*).

## Arhīvi un avoti

| Fails (mapē `data/`) | Saturs |
|---|---|
| `flusso_collm.csv` | No Collm nolasītā meteoru skaita stundu arhīvs (jau esošās stundas tiek atjauninātas) |
| `quote_collm.csv` | Sliežu augstumu arhīvs |
| `radar/` | Pēdējie lejupielādētie attēli (un RMOB faili) |
| `fonti_radar.csv` | Radaru avotu adreses, `attivo=1/0` katra ieslēgšanai/izslēgšanai |

| Avots | Frekvence | Piezīmes |
|---|---|---|
| Collm meteoru radars, Leipcigas Universitāte (LIM) un IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | atjaunina katru stundu 10. minūtē UTC; meteoru skaits vakar + šodien, augstumu sadalījums |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | tikai attēls (radars tiek atjaunots, projekts DECC) |
| swan.ms (Collm kopija) | 36,2 MHz | noklusējumā izslēgts; izmantot tikai ar DL1DBC atļauju |

> Radaru dati pieder to institūcijām (Leipcigas Universitāte / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
