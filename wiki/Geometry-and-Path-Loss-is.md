[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · **Íslenska** · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

# Rúmfræði og deyfing

*Flipi: Spáreikningur › Rúmfræði og deyfing.*

[![Rúmfræði og deyfing](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Textaskýrsla um leiðina (hægt að velja textann og afrita hann) og, hægra megin, grafið **Hæðarhorn loftnets sem fall af fjarlægð frá scatter point**. Tölur innan hornklofa vísa til jafnanna í reiknihandbókinni (`doc/YA-MS_manuale_calcoli.docx`).

## Inntak á þessum flipa

| Reitur | Sjálfgefið | Notkun |
|---|---|---|
| **Afl W** | 400 | Afl sendis fyrir aflreikninginn |
| **Loftnetsmögnun dBi (tx = rx)** | 14 | Sama loftnet í báðum endum |
| **Lágmarksmerki dBm** | −130 | Minnsta greinanlega merki (greinin: 8 staka Yagi + formagnari) |
| **Þéttleiki slóðar q = 10^ … rafeindir/m** | 14 | Línuleg rafeindaþéttni undirþéttu slóðarinnar |

Stöðvar, tíðnisvið, hæð slóða, hæðarhorn geisla, bóma og fjarlægð heitu blettanna koma úr [röðum stýringanna](Getting-Started-is#1-þrjár-raðir-stýringa).

## Hlutar skýrslunnar

| Hluti | Innihald |
|---|---|
| **RÚMFRÆÐI LEIÐARINNAR (kúlulaga jörð, R = 6372,7955 km)** | Stöð og DX með hæðum; fjarlægð, áttarhorn og bakáttarhorn; miðpunktur (locator og hnit); hæð slóða (*← tíðasta gildi mælt af Collm-ratsjánni* þegar hún er tekin frá ratsjánni); hæðarhorn loftnets að miðpunktinum |
| **HOT A / HOT B (hefðbundnir heitir blettir, til að beina loftneti)** | Fyrir hvorn: locator, áttarhorn frá þér og frávik frá beinu leiðinni, áttarhorn frá DX, fjarlægð, hæðarhorn |
| **MÖRK SAMEIGINLEGA SVÆÐISINS** | Drægni í hæð slóða með hæðarhorni geislans; Mörk A / Mörk B með áttarhornum |
| Loftnet | Bóma í λ, mögnun, láréttur / lóðréttur geisli; hvort Hot A og Hot B eru innan eða utan geislans |
| **LEIÐARDEYFING (undirþétt slóð, McKinley 1961; loftnetsmögnun ekki meðtalin)** | Tafla fyrir miðpunktinn (forward), Hot A og Hot B á 28, 50, 70, 144, 222 og 432 MHz |
| **AFLREIKNINGUR VIÐ … MHz (miðpunktur)** | Afl og EIRP, leiðardeyfing, merki við loftnetið, minnsta greinanlega merki, **borð fyrir báru**; sama borð fyrir báru með meðaldeyfingu OH5IY |
| **TILRAUNAREGLUR MILLI TÍÐNISVIÐA (SM6FHZ, VUSHF 2025)** | Fjöldi/styrkur og lengd miðað við 144 MHz; hámarkslengd pings samkvæmt IARU |

## Locator og leið

Locator (4, 6 eða 8 stafir; miðja reitsins, Maidenhead-kerfi IARU) [14]. Fjarlægð, áttarhorn og miðpunktur með stórhringsformúlum á kúlu með radíus **r = 6372,7955 km** (grein Cerrotta–Sartori) [15–16]. Tímaháðir útreikningar miðast við **miðpunktinn**, því besti tíminn getur munað allt að 1,5 klukkustundum milli endanna tveggja (SM6FHZ).

## Hæðarhorn loftnets

**Heimild:** formúlan úr grein Cerrotta–Sartori (mynd 7), með x = d/r, þar sem d er fjarlægð eftir yfirborði að endurvarpspunktinum, H hæð slóðarinnar og h hæð stöðvarinnar [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Prófun:** hún samsvarar nákvæmri kúlurúmfræði innan 0,03°. Forritið notar arkustangens með tveimur breytum, sem gefur neikvæð gildi handan sjóndeildarhrings og forðast lotuvandann sem nefndur er í greininni. Neikvætt hæðarhorn að miðpunktinum þýðir *leiðin er handan rúmfræðilegrar drægni eins stökks*.

## Drægni að sjóndeildarhring

Fjarlægð eftir yfirborði þar sem geisli með hæðarhorn e nær hæðinni H (rúmfræðileg andhverfa formúlunnar hér að ofan) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Prófun:** H = 89,5 km, e = 0° → **1062 km**. Í dæmi greinarinnar (JN44BB–IO53RT) setur teikningin skurðpunkta sjóndeildarhringsins um 870 km frá stöðvunum, sem samsvarar geisla sem lyft er um 2° (865 km).

## Mörk sameiginlega svæðisins

**Heimild:** greinin staðsetur skurðpunkta ferlanna þar sem sjóndeildarhringur hvorrar stöðvar mætir E-laginu: skurðpunkta tveggja hringja með hornradíus ρ = d_H/r með miðju í A og B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Ef 1 − |p0|² < 0 er leiðin lengri en 2·d_H og stöðvarnar sjá **ekkert sameiginlegt svæði í E-laginu**.

**Prófun:** þetta eru **ystu jaðrar** himinsins sem báðar stöðvar sjá, **ekki punktar til að miða á**. Á JN70CN–IN78UO (1710 km, áttarhorn 308°) lenda þeir 1062 km frá stöðinni, 37° til vinstri og hægri við beinu leiðina, á meðan MSHV leggur til 10°. Þess vegna heita þeir *Mörk A* / *Mörk B* og eru teiknaðir daufir á kortið.

## Hot A og Hot B

**Heimild:** endurvörp stopulla loftsteina safnast á tvö svæði („heita bletti“) sitt hvorum megin við miðpunktinn. J. Richardson (AMS) gefur í töflunni sem DJ5HG vitnar í (*Die Geometrie von Meteorscatterverbindungen*, 2004) frávik loftnetsins frá beinu stefnunni: **13° við 1000 km, 11° við 1250 km, 10° við 1500 og 2000 km**. AMS Bulletin No. 203, sem W8WN tók upp, gefur 10° við 1500 og 1800 km.

**Val:** Hot A og Hot B eru punktarnir í fjarlægðinni s frá miðpunktinum M, hornrétt á leiðina. Þegar hakað er við *auto (AMS)* (sjálfgefið) fæst s úr frávikinu í töflu Richardsons, línulega brúað (13° undir 1000 km, 10° yfir 2000 km): s = (D/2)·tan(frávik). Án haks er s slegið inn handvirkt, 30–400 km (MSHV notar 150 km); A vinstra megin séð frá þinni stöð að DX, B hægra megin [21]. Frávikið séð frá stöðinni er um það bil [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Prófun:** með AMS-töflunni, 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, það sama og þeir 150 km sem notaðir voru áður og MSHV notar; á stuttum leiðum færir taflan heitu blettina nær miðpunktinum.

## Leiðardeyfing undirþéttra slóða

**Heimild:** jafna McKinleys og ITU-R-tilmæli P.843 fyrir undirþéttar slóðir (sin α = 1), án loftnetsmögnunar; q = línuleg rafeindaþéttni, r_e = klassískur rafeindageisli = 2,818·10⁻¹⁵ m, R1, R2 fjarlægðir frá slóðinni, φ hálft dreifihornið, β hornið milli slóðarinnar og sléttu leiðarinnar, a₁ upphafsgeislastuðull með r₀ í m og h í km (P.843, jöfnur 4 og 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Val:** aflreikningurinn og deyfingartaflan nota β = 90° (slóð sem sker sléttu leiðarinnar, óhagstæðasta tilvikið: varfærið gildi) og aflreikningurinn sýnir einnig besta tilvikið, β = 0. r₀ er tekið í meðalhæð bergmála fyrir tíðnina, h = 124 − 17 log f (P.843, jafna 15): 0,76 m í 95 km fyrir 50 MHz, 0,40 m í 87 km fyrir 144 MHz, 0,21 m í 79 km fyrir 432 MHz. Yfir 1000 km er a₁ 0,2 dB á 50 MHz, 0,6 dB á 144 MHz og 1,4 dB á 432 MHz (2,9 dB við 600 km); í föstu 102 km hæð DJ5HG væri hann um 70 dB á 432 MHz, þ.e. ekkert bergmál.

**Prófun:** með q = 10¹⁴ rafeindir/m, slóðir í 89,5 km og β = 0, á 144 MHz: **182–192 dB** milli 600 og 2100 km (185 dB við 1000 km), innan bilsins **172–190 dB** sem John Worsnop **G4BAO** reiknaði í doktorsritgerð sinni, eins og GM8JBJ greinir frá. Með β = 90° eykst deyfingin um 10 dB við 600 km, 13 dB við 1000 km og 16 dB við 2100 km; **200 dB meðaltal** OH5IY liggur milli tilvikanna tveggja. 182 dB í töflu GM8JBJ eru ekki staðfesting: taflan gefur enga tíðni, 86,4 dB hennar á hvern legg eru deyfing í lausu rúmi yfir 500 km á 1 MHz (liðinn 20 log f vantar: 129,6 dB á 144 MHz) og liðir hennar leggjast saman í 163,8 dB, ekki 182; á síðunni stendur hvorki „lágmark“ né „144 MHz“.

## Aflreikningur

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Mögnun er slegin inn og notuð í dBi: deyfing McKinleys miðast við jafnátta loftnet, svo engin 2,15 dB tvípólsleiðrétting er dregin frá (EIRP = afl + mögnun). Skýrslan gefur einnig borð fyrir báru með **meðalleiðardeyfingu OH5IY** (200 dB á 144 MHz, kvörðuð með λ³ að völdu tíðnisviði). Viðmiðun greinarinnar: um **70 dBm EIRP** þarf (−130 dBm + 200 dB, t.d. um 400 W inn á 14 dBi).

## Loftnetsmögnun og geisli

**Mögnun – heimild:** ferill Günters Hoch **DL6WU** fyrir löng Yagi-loftnet sem fall af lengd bómunnar L, eftir frásögn W8IO (gildir frá um 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Prófun á móti NEC-líkönum L.B. Cebik W4RNL á 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Stök | Bóma (λ) | W4RNL NEC (dBi) | Formúla (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Munurinn fer aldrei yfir **0,1 dB**: mögnunin ræðst meira af lengd bómunnar en af hönnuninni (Yagi-loftnet VK3AUU hafa styttri bómu fyrir sama fjölda staka). Yagi Calculator eftir VK5DJ gefur einnig mat fyrir afbrigðin VK3AUU, WA2PHW og DJ9BV, en formúlur þeirra hafa ekki verið birtar.

**Geisli – heimild:** regla Kraus, með hringlaga geisla θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Prófun:** NEC-líkön W4RNL af DL6WU Yagi-loftnetum gefa **láréttan geisla 5–10 % mjórri** en Kraus: 33,8° / 26,4° / 22,6° fyrir 12, 19 og 26 stök, á móti 37,3° / 28,0° / 23,9°. Einfaldar formúlur hunsa fremri hliðargeislana (W4RNL, *Long-Boom Yagi Rules of Thumb*). Á löngum bómum er lóðrétti geislinn aðeins breiðari en sá lárétti (14 λ: 18,4° / 18,8°).

**Val** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Dæmi: 14 λ Yagi á 432 MHz → 20,3 dBi, geisli 18,1° láréttur og 19,5° lóðréttur; líkön W4RNL gefa 20,4 dBi og 18,4° / 18,8°. Þetta eru nálgunarreglur leiddar af fáeinum DL6WU-loftnetum.

Alltaf er gert ráð fyrir að loftnetinu sé beint að DX. Heitur blettur er **innan geislans** ef |Az(Hot) − Az(loftnet)| ≤ θ_láréttur/2: hann er þá teiknaður grár í [Himinhvelfingunni](Sky-View-is) og viðvörun birtist. Í útreikningi nýtninnar eru loftnetin stefnulaus; raunverulegi geislinn er aðeins notaður í þessa prófun.

## Tilraunareglur milli tíðnisviða

Miðað við 144 MHz: fjöldi/styrkur × (144/f)³ (í dB), lengd × (144/f)² (SM6FHZ, VUSHF 2025). Hámarkslengd pings samkvæmt IARU Region 1: 1000 ms á 50 MHz, 500 ms á 70 MHz, 100 ms á 144 MHz, 13 ms á 432 MHz (VHF Handbook, vitnað í greininni). Sjá einnig [Tilraunaspár](Experimental-Forecasts-is).
