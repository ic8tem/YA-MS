[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · **Dansk** · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

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

**Kilde:** refleksionerne fra sporadiske meteorer samles i to zoner ("hot spots") på hver side af midtpunktet. J. Richardson (AMS) angiver i tabellen, som DJ5HG citerer (*Die Geometrie von Meteorscatterverbindungen*, 2004), antenneforskydningen fra den direkte retning: **13° ved 1000 km, 11° ved 1250 km, 10° ved 1500 og 2000 km**. AMS Bulletin nr. 203, som W8WN har overtaget, angiver 10° ved 1500 og 1800 km.

**Valg:** Hot A og Hot B er punkterne i afstanden s fra midtpunktet M, vinkelret på strækningen. Med flueben i *auto (AMS)* (standard) fås s af forskydningen i Richardsons tabel, lineært interpoleret (13° under 1000 km, 10° over 2000 km): s = (D/2)·tan(forskydning). Uden flueben indtastes s manuelt, 30–400 km (MSHV bruger 150 km); A til venstre set fra din station mod DX, B til højre [21]. Forskydningen set fra stationen er ca. [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Kontrol:** med AMS-tabellen 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, det samme som de 150 km, der blev brugt før og bruges af MSHV; på korte strækninger flytter tabellen hot spots tættere på midtpunktet.

## Dæmpning for underdense spor

**Kilde:** McKinleys ligning og ITU-R-anbefaling P.843 for underdense spor (sin α = 1), antenneforstærkning ikke medregnet; q = lineær elektrontæthed, r_e = klassisk elektronradius = 2,818·10⁻¹⁵ m, R1, R2 afstande fra sporet, φ halvdelen af spredningsvinklen, β vinklen mellem sporet og strækningens plan, a₁ faktor for startradius med r₀ i m og h i km (P.843, lign. 4 og 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Valg:** linkbudgettet og dæmpningstabellen bruger β = 90° (spor, der krydser strækningens plan, det mindst gunstige tilfælde: forsigtig værdi), og linkbudgettet viser også det bedste tilfælde, β = 0. r₀ tages ved den gennemsnitlige ekkohøjde for frekvensen, h = 124 − 17 log f (P.843, lign. 15): 0,76 m ved 95 km for 50 MHz, 0,40 m ved 87 km for 144 MHz, 0,21 m ved 79 km for 432 MHz. Over 1000 km er a₁ 0,2 dB ved 50 MHz, 0,6 dB ved 144 MHz og 1,4 dB ved 432 MHz (2,9 dB ved 600 km); ved DJ5HG's faste 102 km ville den være omkring 70 dB ved 432 MHz, dvs. slet intet ekko.

**Kontrol:** med q = 10¹⁴ elektroner/m, spor i 89,5 km og β = 0, ved 144 MHz: **182–192 dB** mellem 600 og 2100 km (185 dB ved 1000 km), inden for intervallet **172–190 dB**, som John Worsnop **G4BAO** har beregnet i sin ph.d.-afhandling, som gengivet af GM8JBJ. Med β = 90° vokser dæmpningen med 10 dB ved 600 km, 13 dB ved 1000 km og 16 dB ved 2100 km; OH5IY's **gennemsnit på 200 dB** ligger mellem de to tilfælde. De 182 dB i GM8JBJ's tabel er ikke en bekræftelse: tabellen angiver ingen frekvens, dens 86,4 dB pr. delstrækning er fritrumsdæmpningen over 500 km ved 1 MHz (leddet 20 log f mangler: 129,6 dB ved 144 MHz), og dens poster summerer til 163,8 dB, ikke 182; siden siger hverken "minimum" eller "144 MHz".

## Linkbudget

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Forstærkning indtastes og bruges i dBi: McKinleys dæmpning gælder for isotrope antenner, så der trækkes ingen dipolkorrektion på 2,15 dB fra (EIRP = effekt + forstærkning). Rapporten angiver også marginen med **OH5IY's gennemsnitlige dæmpning** (200 dB ved 144 MHz, skaleret med λ³ til det valgte bånd). Artiklens reference: der kræves ca. **70 dBm EIRP** (−130 dBm + 200 dB, fx ca. 400 W i 14 dBi).

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
