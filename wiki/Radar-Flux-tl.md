**English** · [Русский](Radar-Flux-ru) · [Deutsch](Radar-Flux-de) · [日本語](Radar-Flux-ja)

# Flux ng radar

*Tab: Live at real-time na datos › Flux ng radar.*

[![Flux ng radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Ipinapakita ng tab na ito kung ano ang binibilang **ngayon** ng mga propesyonal na meteor radar: ang bilang ng meteor bawat oras at ang taas ng mga bakas mula sa SKiYMET radar ng **Collm** (Univ. ng Leipzig / IAP Kühlungsborn, Germany, 36.2 MHz), at ang pinakabagong larawan ng radar ng **Sodankylä** (SGO, Finland). Ang bilang ng Collm ang pinagbabatayan ng tantiya para sa iyong banda at ng [Eksperimental na pagtataya](Experimental-Forecasts-tl); ang sinukat na taas ng bakas ang pinagbabatayan ng buong heometriya.

## Mga kontrol

| Kontrol | Ano ang ginagawa |
|---|---|
| **I-download ngayon** | Sinusuri nang sabay-sabay ang lahat ng panlabas na sanggunian. |
| **Awtomatikong pag-update ng lahat ng sanggunian bawat 5 minuto** | Naka-on bilang default. Bawat 5 minuto, sinusuri ang lahat ng sanggunian at **ang mga nagbago lamang** ang muling dina-download (*walang pagbabago (sinuri noong … UTC)* / *bagong datos noong … UTC*). |
| **Exponent ng λ (SM6FHZ)** | Exponent k ng tuntunin ng frequency, default 3 (1–4). |

## Ano ang ipinapakita

| Panel | Nilalaman |
|---|---|
| **Meteor/oras – kahapon at ngayon (UTC)** | Mga cyan na bar = bilang ng Collm (balido), mga pulang bar = itinapon, makapal na kahel na linya = *tantiya sa … MHz* sa iskala sa kanan |
| **Taas ng mga bakas (Collm)** | Meteor bawat km ng taas sa pagitan ng 70 at 110 km, na may pinakamadalas na taas (moda), mean, median at standard deviation |
| Larawan ng Collm | Ang orihinal na graph ng SKiYMET, gaya ng pagkaka-download |
| Larawan ng Sodankylä | Ang pinakabagong larawan ng bilang ng meteor ng radar ng Sodankylä (ipinapakita lamang; hindi binabasa ang format nito) |

Sinasabi ng linya sa itaas ng mga graph kung kailan binasa ang graph ng Collm at kung aling patayong iskala ang natagpuan (*iskalang nabasa mula sa graph: 0-… meteor/oras*).

## Paano binabasa ang graph ng Collm

May nakapirming posisyon ng mga axis ang graph ng Collm (720 × 720 pixel, puro ang kulay), pero **inaangkop ng radar ang patayong iskala araw-araw** sa mga sinukat na halaga (hal. 0–1.2·10³ noong 5/11/2026 at 0–1.0·10³ noong 6/11/2026, na lumipat ang mga tick mark). Kaya ang YA-MS ay:

1. hinahanap ang mahahabang tick mark ng axis;
2. **binabasa ang mga label** ng pinakamataas na tick at ng zero sa pamamagitan ng paghahambing ng bawat character sa dot-matrix na font ng graph;
3. para sa bawat oras i (0–47, kahapon at ngayon), kinukuha ang gitnang column at ang unang cyan na pixel mula sa itaas, y:

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

Ang y_top at y0 ay ang mga hanay ng pinakamataas na tick at ng zero, ang N_top ay ang halagang nabasa sa pinakamataas na label (×1000). Resolusyon: mga 7–8 meteor/oras bawat pixel. *Pagpili ng programa (manwal eq. 42).*

Kung hindi mabasa ang isang label, bumabalik ang programa sa kalibrasyon ng 5/11/2026 (**kalibradong iskala 0-1200 meteor/oras**) at sinasabi ito sa kulay kahel: *Hindi mabasa ang patayong iskala ng flux (label sa itaas: …): kailangang suriin ang mga halaga.* Kung nagbago mismo ang format ng graph (*Nagbago ang format ng graph (…x…): hindi mabasa* o *Hindi nakita ang mga axis ng flux sa inaasahang posisyon*), kailangang i-recalibrate ang pagbasa: pakiulat ito (tingnan ang [Pag-ambag](Contributing-and-Contacts-tl)).

### Taas ng mga bakas

Mula sa histogram ng taas (n_k na meteor sa km k, mean na taas h_k):

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*Manwal eq. 43.* Kapag may tsek ang **mula sa radar** (hanay 2 ng mga kontrol), ang **moda** ang nagiging taas ng bakas sa lahat ng kalkulasyon. Pagsusuri: graph ng 5/11/2026 – moda 89.5 km, mean 88.6 km, standard deviation 6.8 km, na kumukumpirma sa ~90 km ng artikulong Cerrotta–Sartori (mean ng SKiYMET).

Kung magbago ang iskala ng graph ng taas, nagbababala ang programa: *balido pa rin ang estadistika ng taas (moda, mean, median), ang absolutong bilang ay hindi na.*

## Tantiya para sa iyong banda

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

Mga eksperimental na tuntunin ni **SM6FHZ** (VUSHF 2025): ang bilang at lakas ng mga repleksiyon ay sumusunod sa λ³, ang tagal ay sa λ²; ang pagdepende sa λ³ ay kapareho ng nasa underdense na ekwasyon ni McKinley. Ipinapakita rin ang pinakamahabang tagal ng ping ayon sa IARU Region 1 (1000 ms sa 50 MHz, 500 ms sa 70 MHz, 100 ms sa 144 MHz, 13 ms sa 432 MHz). Pahiwatig lamang ang mga halaga, na dapat ihambing sa karanasan sa ere. Nasa [Eksperimental na pagtataya](Experimental-Forecasts-tl) ang station factor K at ang paghahambing sa RMOB.

## Offline

Kung walang maabot na sanggunian, lumalabas ang isang mensahe **nang isang beses**: *Walang koneksiyon sa internet. Hindi ma-update ang datos ng mga radar at ng RMOB: ginagamit ng programa ang huling na-save na datos at kusang sumusubok muli bawat 5 minuto.* Nagiging pula ang status bar sa ibaba (*WALANG KONEKSIYON SA INTERNET …*) hanggang bumalik ang koneksiyon (*Naibalik ang koneksiyon.*).

## Mga archive at sanggunian

| File (sa `data/`) | Nilalaman |
|---|---|
| `flusso_collm.csv` | Archive bawat oras ng flux na binasa mula sa Collm (ina-update ang mga oras na naroon na) |
| `quote_collm.csv` | Archive ng taas ng mga bakas |
| `radar/` | Pinakabagong na-download na mga larawan (at mga RMOB file) |
| `fonti_radar.csv` | Mga address ng sanggunian ng radar, `attivo=1/0` para i-enable/i-disable ang bawat isa |

| Sanggunian | Frequency | Mga tala |
|---|---|---|
| Collm meteor radar, Leipzig University (LIM) at IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36.2 MHz | ina-update bawat oras sa minutong 10 UTC; flux kahapon + ngayon, distribusyon ng taas |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36.9 MHz | larawan lamang (ina-update ang radar, proyektong DECC) |
| swan.ms (kopya ng Collm) | 36.2 MHz | naka-disable bilang default; gamitin lamang nang may pahintulot ni DL1DBC |

> Pag-aari ng kani-kanilang institusyon ang datos ng radar (Leipzig University / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
