[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · **Íslenska** · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh)

# Ratsjárflæði

*Flipi: Beint og rauntímagögn › Ratsjárflæði.*

[![Ratsjárflæði](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Þessi flipi sýnir hvað loftsteinaratsjár fagmanna eru að telja **núna**: fjölda loftsteina á klukkustund og hæð slóða frá SKiYMET-ratsjánni í **Collm** (Háskólinn í Leipzig / IAP Kühlungsborn, Þýskalandi, 36,2 MHz), og nýjustu myndina frá ratsjánni í **Sodankylä** (SGO, Finnlandi). Talningarnar frá Collm fæða matið fyrir þitt tíðnisvið og [Tilraunaspár](Experimental-Forecasts-is); mæld hæð slóða fæðir alla rúmfræðina.

## Stýringar

| Stýring | Hvað hún gerir |
|---|---|
| **Sækja núna** | Athugar allar ytri lindir í einu. |
| **Sjálfvirk uppfærsla allra gagnalinda á 5 mínútna fresti** | Kveikt sjálfgefið. Á 5 mínútna fresti eru allar lindir athugaðar og **aðeins þær sem hafa breyst** sóttar aftur (*óbreytt (athugað kl. … UTC)* / *ný gögn kl. … UTC*). |
| **Veldisvísir λ (SM6FHZ)** | Veldisvísirinn k í tíðnireglunni, sjálfgefið 3 (1–4). |

## Hvað er sýnt

| Spjald | Innihald |
|---|---|
| **Loftsteinar/klst. – í gær og í dag (UTC)** | Blágrænar súlur = talningar frá Collm (gildar), rauðar súlur = hent, þykk appelsínugul lína = *mat við … MHz* á hægri kvarðanum |
| **Hæðir slóða (Collm)** | Loftsteinar á hvern km hæðar milli 70 og 110 km, með algengustu hæð (tíðasta gildi), meðaltali, miðgildi og staðalfráviki |
| Mynd frá Collm | Upprunalega SKiYMET-grafið, eins og það var sótt |
| Mynd frá Sodankylä | Nýjasta mynd ratsjárinnar í Sodankylä með loftsteinatalningum (aðeins sýnd; snið hennar er ekki lesið) |

Línan fyrir ofan gröfin segir hvenær Collm-grafið var lesið og hvaða lóðrétti kvarði fannst (*kvarði lesinn af grafi: 0-… loftsteinar/klst.*).

## Hvernig Collm-grafið er lesið

Collm-grafið (720 × 720 dílar, hreinir litir) hefur fasta staðsetningu ása, en ratsjáin **aðlagar lóðrétta kvarðann á hverjum degi** að mældu gildunum (t.d. 0–1,2·10³ þann 5/11/2026 og 0–1,0·10³ þann 6/11/2026, með færðum kvarðastrikum). YA-MS gerir því eftirfarandi:

1. finnur löngu kvarðastrik ássins;
2. **les merkimiðana** við efsta kvarðastrikið og við núllið með því að bera hvert tákn saman við punktafylkisletur grafsins;
3. fyrir hverja klukkustund i (0–47, í gær og í dag) tekur það miðdálkinn og fyrsta blágræna dílinn ofan frá, y:

```math
x_i = 101 + (i+0{.}5)\,\frac{676-101}{48},\qquad N = (y_0-y)\,\frac{N_{top}}{y_0-y_{top}}
```

y_top og y0 eru línur efsta kvarðastriksins og núllsins, N_top gildið sem lesið er á efsta merkimiðanum (×1000). Upplausn: um 7–8 loftsteinar/klst. á hvern díl. *Val forritsins (handbók, jafna 42).*

Ef ekki tekst að lesa merkimiða grípur forritið til kvörðunarinnar frá 5/11/2026 (**kvarðaður skali 0-1200 loftsteinar/klst.**) og segir frá því í appelsínugulu: *Get ekki lesið lóðréttan kvarða flæðisins (efsti merkimiði: …): gildin þarf að athuga.* Ef snið grafsins sjálfs breytist (*Snið grafsins hefur breyst (…x…): ekki hægt að lesa það* eða *Ásar flæðisins fundust ekki á væntanlegum stað*) þarf að kvarða lesturinn upp á nýtt: vinsamlegast tilkynntu það (sjá [Framlög](Contributing-and-Contacts-is)).

### Hæðir slóða

Úr hæðarstuðlaritinu (n_k loftsteinar við km k, meðalhæð h_k):

```math
\hat{h} = h_{k^*},\ k^* = \arg\max_k n_k,\qquad \bar{h} = \frac{\sum_k n_k h_k}{\sum_k n_k},\qquad s = \sqrt{\frac{\sum_k n_k (h_k-\bar{h})^2}{\sum_k n_k}}
```

*Handbók, jafna 43.* Þegar hakað er við **frá ratsjá** (röð 2 í stýringunum) verður **tíðasta gildið** hæð slóða í öllum útreikningum. Prófun: graf frá 5/11/2026 – tíðasta gildi 89,5 km, meðaltal 88,6 km, staðalfrávik 6,8 km, sem staðfestir ~90 km í grein Cerrotta–Sartori (meðaltal SKiYMET).

Ef kvarði hæðargrafsins breytist varar forritið við: *tölfræði hæða (tíðasta gildi, meðaltal, miðgildi) er enn gild, en heildartalningar ekki.*

## Mat fyrir þitt tíðnisvið

```math
N(f) = N_{Collm}(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k},\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

Tilraunareglur **SM6FHZ** (VUSHF 2025): fjöldi og styrkur endurvarpa breytist með λ³, lengd með λ² (hjá McKinley er λ³ afl einnar slóðar; fjöldi slóða breytist um það bil með λ^1,5, og í framdreifingu vex lengdin einnig með sec²φ: sjá [Tilraunaspár](Experimental-Forecasts-is)). Hámarkslengd pings samkvæmt IARU Region 1 er einnig sýnd (1000 ms á 50 MHz, 500 ms á 70 MHz, 100 ms á 144 MHz, 13 ms á 432 MHz). Gildin eru til viðmiðunar og ber að bera saman við reynslu í loftinu. Stöðvarstuðullinn K og samanburðurinn við RMOB eru í [Tilraunaspám](Experimental-Forecasts-is).

## Án nettengingar

Ef engin lind næst birtast skilaboð **einu sinni**: *Engin nettenging. Ekki er hægt að uppfæra gögn ratsjánna og RMOB: forritið notar síðustu vistuðu gögn og reynir sjálft aftur á 5 mínútna fresti.* Stöðustikan neðst verður rauð (*ENGIN NETTENGING …*) þar til tengingin kemst aftur á (*Tenging komin aftur.*).

## Skjalasöfn og lindir

| Skrá (í `data/`) | Innihald |
|---|---|
| `flusso_collm.csv` | Safn flæðisins sem lesið er frá Collm, eftir klukkustundum (klukkustundir sem þegar eru til eru uppfærðar) |
| `quote_collm.csv` | Safn yfir hæð slóða |
| `radar/` | Síðast sóttar myndir (og RMOB-skrár) |
| `fonti_radar.csv` | Slóðir ratsjárlindanna, `attivo=1/0` til að virkja/óvirkja hverja þeirra |

| Lind | Tíðni | Athugasemdir |
|---|---|---|
| Collm meteor radar, Háskólinn í Leipzig (LIM) og IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | uppfært á hverri klukkustund á mínútu 10 UTC; flæði í gær + í dag, hæðardreifing |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | aðeins mynd (verið er að uppfæra ratsjána, verkefnið DECC) |
| swan.ms (afrit af Collm) | 36,2 MHz | óvirkt sjálfgefið; notaðu aðeins með leyfi DL1DBC |

> Ratsjárgögnin tilheyra viðkomandi stofnunum (Háskólinn í Leipzig / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
