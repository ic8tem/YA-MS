[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · **Íslenska** · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [ไทย](Geometry-and-Path-Loss-th) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

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

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Prófun:** hún samsvarar nákvæmri kúlurúmfræði innan 0,03°. Forritið notar arkustangens með tveimur breytum, sem gefur neikvæð gildi handan sjóndeildarhrings og forðast lotuvandann sem nefndur er í greininni. Neikvætt hæðarhorn að miðpunktinum þýðir *leiðin er handan rúmfræðilegrar drægni eins stökks*.

## Drægni að sjóndeildarhring

Fjarlægð eftir yfirborði þar sem geisli með hæðarhorn e nær hæðinni H (rúmfræðileg andhverfa formúlunnar hér að ofan) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Prófun:** H = 89,5 km, e = 0° → **1062 km**. Í dæmi greinarinnar (JN44BB–IO53RT) setur teikningin skurðpunkta sjóndeildarhringsins um 870 km frá stöðvunum, sem samsvarar geisla sem lyft er um 2° (865 km).

## Mörk sameiginlega svæðisins

**Heimild:** greinin staðsetur skurðpunkta ferlanna þar sem sjóndeildarhringur hvorrar stöðvar mætir E-laginu: skurðpunkta tveggja hringja með hornradíus ρ = d_H/r með miðju í A og B [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Ef 1 − |p0|² < 0 er leiðin lengri en 2·d_H og stöðvarnar sjá **ekkert sameiginlegt svæði í E-laginu**.

**Prófun:** þetta eru **ystu jaðrar** himinsins sem báðar stöðvar sjá, **ekki punktar til að miða á**. Á JN70CN–IN78UO (1710 km, áttarhorn 308°) lenda þeir 1062 km frá stöðinni, 37° til vinstri og hægri við beinu leiðina, á meðan MSHV leggur til 10°. Þess vegna heita þeir *Mörk A* / *Mörk B* og eru teiknaðir daufir á kortið.

## Hot A og Hot B

**Heimild:** endurvörpin safnast á tvö svæði („heita bletti“) um **50–150 km sitt hvorum megin við miðpunktinn**. Þetta er grunnurinn að töflunni um frávik loftnets í AMS Bulletin No. 203, sem W8WN tók upp (frávik 10° fyrir 1500 og 1800 km leiðir); MSHV eftir LZ2HV notar sama viðmið.

**Val:** Hot A og Hot B eru punktarnir í fjarlægðinni s frá miðpunktinum M, hornrétt á leiðina (s = 150 km, stillanlegt 30–400 km); A vinstra megin séð frá þinni stöð að DX, B hægra megin [21]. Frávikið séð frá stöðinni er um það bil [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Prófun:** JN70CN–IN78UO, D = 1710 km: 6,7° með s = 100 km, **10,0° með s = 150 km** (sama og MSHV og AMS/W8WN), 13,2° með s = 200 km.

## Leiðardeyfing undirþéttra slóða

**Heimild:** jafna McKinleys fyrir undirþéttar slóðir (β = 0, sin α = 1), án loftnetsmögnunar; q = línuleg rafeindaþéttni, r_e = klassískur rafeindageisli = 2,818·10⁻¹⁵ m, R1, R2 fjarlægðir frá slóðinni, φ hálft dreifihornið [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Prófun:** með q = 10¹⁴ rafeindir/m á 144 MHz: **181–192 dB** milli 600 og 2200 km, í samræmi við viðmiðanir greinarinnar á 144 MHz: **182 dB lágmark** (GM8JBJ, eftir Kaiser & Closs 1952) og **200 dB að meðaltali** (OH5IY).

## Aflreikningur

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. Mögnun er slegin inn í dBi og notuð í dBd (dBi − 2,15). Skýrslan gefur einnig borð fyrir báru með **meðalleiðardeyfingu OH5IY** (200 dB á 144 MHz, kvörðuð með λ³ að völdu tíðnisviði). Viðmiðun greinarinnar: um **70 dBm EIRP** þarf (−130 dBm + 200 dB, t.d. um 400 W inn á 14 dBi).

## Loftnetsmögnun og geisli

**Mögnun – heimild:** ferill Günters Hoch **DL6WU** fyrir löng Yagi-loftnet sem fall af lengd bómunnar L, eftir frásögn W8IO (gildir frá um 2 λ) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Prófun á móti NEC-líkönum L.B. Cebik W4RNL á 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Stök | Bóma (λ) | W4RNL NEC (dBi) | Formúla (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Munurinn fer aldrei yfir **0,1 dB**: mögnunin ræðst meira af lengd bómunnar en af hönnuninni (Yagi-loftnet VK3AUU hafa styttri bómu fyrir sama fjölda staka). Yagi Calculator eftir VK5DJ gefur einnig mat fyrir afbrigðin VK3AUU, WA2PHW og DJ9BV, en formúlur þeirra hafa ekki verið birtar.

**Geisli – heimild:** regla Kraus, með hringlaga geisla θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Prófun:** NEC-líkön W4RNL af DL6WU Yagi-loftnetum gefa **láréttan geisla 5–10 % mjórri** en Kraus: 33,8° / 26,4° / 22,6° fyrir 12, 19 og 26 stök, á móti 37,3° / 28,0° / 23,9°. Einfaldar formúlur hunsa fremri hliðargeislana (W4RNL, *Long-Boom Yagi Rules of Thumb*). Á löngum bómum er lóðrétti geislinn aðeins breiðari en sá lárétti (14 λ: 18,4° / 18,8°).

**Val** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Dæmi: 14 λ Yagi á 432 MHz → 20,3 dBi, geisli 18,1° láréttur og 19,5° lóðréttur; líkön W4RNL gefa 20,4 dBi og 18,4° / 18,8°. Þetta eru nálgunarreglur leiddar af fáeinum DL6WU-loftnetum.

Alltaf er gert ráð fyrir að loftnetinu sé beint að DX. Heitur blettur er **innan geislans** ef |Az(Hot) − Az(loftnet)| ≤ θ_láréttur/2: hann er þá teiknaður grár í [Himinhvelfingunni](Sky-View-is) og viðvörun birtist. Í útreikningi nýtninnar eru loftnetin stefnulaus; raunverulegi geislinn er aðeins notaður í þessa prófun.

## Tilraunareglur milli tíðnisviða

Miðað við 144 MHz: fjöldi/styrkur × (144/f)³ (í dB), lengd × (144/f)² (SM6FHZ, VUSHF 2025). Hámarkslengd pings samkvæmt IARU Region 1: 1000 ms á 50 MHz, 500 ms á 70 MHz, 100 ms á 144 MHz, 13 ms á 432 MHz (VHF Handbook, vitnað í greininni). Sjá einnig [Tilraunaspár](Experimental-Forecasts-is).
