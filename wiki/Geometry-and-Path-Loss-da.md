[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · **Dansk** · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh)

# Geometri og dæmpning

*Fane: Prognoseberegning › Geometri og dæmpning.*

[![Geometri og dæmpning](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

En tekstrapport om strækningen (kan markeres, så du kan kopiere den) og til højre grafen **Antenneelevation som funktion af afstanden til scatterpunktet**. Tal i parentes henviser til ligningerne i beregningsmanualen (`doc/YA-MS_manuale_calcoli.docx`).

## Inddata på denne fane

| Felt | Standard | Anvendelse |
|---|---|---|
| **Effekt W** | 400 | Sendereffekt til linkbudgettet |
| **Antenneforstærkning dBi (tx = rx)** | 14 | Samme antenne i begge ender |
| **Mindste signal dBm** | −130 | Mindste modtagelige signal (artiklen: 8-elements Yagi + forforstærker) |
| **Spordensitet q = 10^ … elektroner/m** | 14 | Det underdense spors lineære elektrontæthed |

Stationer, bånd, sporhøjde, lapelevation, bom og hot spot-afstand kommer fra [rækkerne af betjeningselementer](Getting-Started-da#1-de-tre-rækker-betjeningselementer).

## Rapportens afsnit

| Afsnit | Indhold |
|---|---|
| **STRÆKNINGENS GEOMETRI (kugleformet Jord, R = 6372,7955 km)** | Station og DX med højder; afstand, azimut og modsat azimut; midtpunkt (lokator og koordinater); sporhøjde (*← typetal målt af Collm-radaren*, når den er taget fra radaren); antenneelevation mod midtpunktet |
| **HOT A / HOT B (klassiske hot spots, til antenneretning)** | For hvert: lokator, azimut fra dig og forskydning fra den direkte strækning, azimut fra DX, afstand, elevation |
| **GRÆNSER FOR DEN FÆLLES ZONE** | Rækkevidde i sporhøjde med lapelevationen; Grænse A / Grænse B med azimut |
| Antenne | Bom i λ, forstærkning, vandret / lodret lap; om Hot A og Hot B ligger inden for eller uden for lappen |
| **STRÆKNINGSDÆMPNING (underdenst spor, McKinley 1961; antenneforstærkning ikke medregnet)** | Tabel for midtpunktet (forward), Hot A og Hot B ved 28, 50, 70, 144, 222 og 432 MHz |
| **LINKBUDGET VED … MHz (midtpunkt)** | Effekt og EIRP, strækningsdæmpning, signal ved antennen, mindste modtagelige, **margin**; samme margin med OH5IY's gennemsnitlige dæmpning |
| **EKSPERIMENTELLE REGLER MELLEM BÅNDENE (SM6FHZ, VUSHF 2025)** | Antal/intensitet og varighed i forhold til 144 MHz; IARU's maksimale ping |

## Lokator og strækning

Lokator (4, 6 eller 8 tegn; feltets centrum, IARU's Maidenhead-system) [14]. Afstand, azimut og midtpunkt med storcirkelformler på en kugle med radius **r = 6372,7955 km** (artiklen af Cerrotta–Sartori) [15–16]. Tidsafhængige beregninger refererer til **midtpunktet**, fordi det bedste tidspunkt kan afvige op til 1,5 time mellem de to ender (SM6FHZ).

## Antenneelevation

**Kilde:** formlen i artiklen af Cerrotta–Sartori (figur 7), med x = d/r, d afstanden langs jorden til refleksionspunktet, H sporhøjden og h stationens højde [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Kontrol:** den stemmer med eksakt sfærisk geometri inden for 0,03°. Programmet bruger arcustangens med to argumenter, som giver negative værdier bag horisonten og undgår det periodicitetsproblem, der nævnes i artiklen. En negativ elevation mod midtpunktet betyder *strækningen er længere end den geometriske rækkevidde for ét hop*.

## Rækkevidde til horisonten

Afstand langs jorden, hvor en stråle med elevation e når højden H (geometrisk invers af formlen ovenfor) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Kontrol:** H = 89,5 km, e = 0° → **1062 km**. I artiklens eksempel (JN44BB–IO53RT) placerer tegningen horisontskæringerne ca. 870 km fra stationerne, hvilket svarer til en lap hævet ca. 2° (865 km).

## Grænser for den fælles zone

**Kilde:** artiklen bestemmer skæringerne mellem de kurver, hvor hver stations horisont møder E-laget: skæringspunkterne mellem to cirkler med vinkelradius ρ = d_H/r centreret i A og B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Hvis 1 − |p0|² < 0, er strækningen længere end 2·d_H, og stationerne ser **ingen fælles zone i E-laget**.

**Kontrol:** dette er de **fjerneste kanter** af himlen set fra begge stationer, **ikke punkter at rette antennen mod**. På JN70CN–IN78UO (1710 km, azimut 308°) ligger de 1062 km fra stationen, 37° til venstre og højre for den direkte strækning, mens MSHV foreslår 10°. Derfor kaldes de *Grænse A* / *Grænse B* og tegnes svagt på kortet.

## Hot A og Hot B

**Kilde:** refleksionerne samles i to zoner ("hot spots") ca. **50–150 km på hver side af midtpunktet**. Det er grundlaget for tabellen over antenneforskydning i AMS Bulletin nr. 203, som W8WN har overtaget (forskydning på 10° for strækninger på 1500 og 1800 km); MSHV af LZ2HV bruger samme kriterium.

**Valg:** Hot A og Hot B er punkterne i afstanden s fra midtpunktet M, vinkelret på strækningen (s = 150 km, kan indstilles 30–400 km); A til venstre set fra din station mod DX, B til højre [21]. Forskydningen set fra stationen er ca. [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Kontrol:** JN70CN–IN78UO, D = 1710 km: 6,7° med s = 100 km, **10,0° med s = 150 km** (samme som MSHV og AMS/W8WN), 13,2° med s = 200 km.

## Dæmpning for underdense spor

**Kilde:** McKinleys ligning for underdense spor (β = 0, sin α = 1), antenneforstærkning ikke medregnet; q = lineær elektrontæthed, r_e = klassisk elektronradius = 2,818·10⁻¹⁵ m, R1, R2 afstande fra sporet, φ halvdelen af spredningsvinklen [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\cos^2\varphi}{\lambda^3 q^2 r_e^2}\right]\ \mathrm{dB}
```

**Kontrol:** med q = 10¹⁴ elektroner/m ved 144 MHz: **181–192 dB** mellem 600 og 2200 km, i overensstemmelse med artiklens referencer ved 144 MHz: **182 dB minimum** (GM8JBJ, efter Kaiser & Closs 1952) og **200 dB gennemsnit** (OH5IY).

## Linkbudget

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - 2{.}15 - L + G_{rx} - 2{.}15,\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Forstærkning indtastes i dBi og bruges i dBd (dBi − 2,15). Rapporten angiver også marginen med **OH5IY's gennemsnitlige dæmpning** (200 dB ved 144 MHz, skaleret med λ³ til det valgte bånd). Artiklens reference: der kræves ca. **70 dBm EIRP** (−130 dBm + 200 dB, fx ca. 400 W i 14 dBi).

## Antenneforstærkning og lap

**Forstærkning – kilde:** kurve af Günter Hoch **DL6WU** for lange Yagi'er som funktion af bomlængden L, gengivet af W8IO (gælder fra ca. 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Kontrol mod NEC-modellerne af L.B. Cebik W4RNL ved 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementer | Bom (λ) | W4RNL NEC (dBi) | Formel (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Forskellen overstiger aldrig **0,1 dB**: forstærkningen afhænger mere af bomlængden end af konstruktionen (VK3AUU-Yagi'er har kortere bom for samme antal elementer). Yagi Calculator af VK5DJ giver også estimater for varianterne VK3AUU, WA2PHW og DJ9BV, hvis formler ikke er publiceret.

**Lap – kilde:** Kraus' regel med cirkulær lap θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Kontrol:** W4RNL's NEC-modeller af DL6WU-Yagi'er giver en **vandret lap, der er 5–10 % smallere** end Kraus: 33,8° / 26,4° / 22,6° for 12, 19 og 26 elementer mod 37,3° / 28,0° / 23,9°. Enkle formler ser bort fra sidelapperne fremad (W4RNL, *Long-Boom Yagi Rules of Thumb*). På lange bomme er den lodrette lap lidt bredere end den vandrette (14 λ: 18,4° / 18,8°).

**Valg** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Eksempel: Yagi på 14 λ ved 432 MHz → 20,3 dBi, lap 18,1° vandret og 19,5° lodret; W4RNL's modeller giver 20,4 dBi og 18,4° / 18,8°. Det er tilnærmede regler udledt af nogle få DL6WU-antenner.

Antennen betragtes altid som rettet mod DX. Et hot spot ligger **inden for lappen**, hvis |Az(Hot) − Az(antenne)| ≤ θ_vandret/2: så tegnes det med gråt i [himmelkuplen](Sky-View-da), og der vises en advarsel. I effektivitetsberegningen er antennerne isotrope; den faktiske lap bruges kun til denne kontrol.

## Eksperimentelle regler mellem båndene

I forhold til 144 MHz: antal/intensitet × (144/f)³ (i dB), varighed × (144/f)² (SM6FHZ, VUSHF 2025). IARU Region 1's maksimale pingvarighed: 1000 ms ved 50 MHz, 500 ms ved 70 MHz, 100 ms ved 144 MHz, 13 ms ved 432 MHz (VHF Handbook, citeret i artiklen). Se også [Eksperimentelle prognoser](Experimental-Forecasts-da).
