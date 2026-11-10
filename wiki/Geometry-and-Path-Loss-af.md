[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · **Afrikaans** · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh)

# Geometrie en padverlies

*Oortjie: Voorspellingsberekening › Geometrie en padverlies.*

[![Geometrie en padverlies](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

'n Teksverslag van die pad (kiesbaar, sodat jy dit kan kopieer) en, regs, die grafiek **Antenna-elevasie teenoor afstand vanaf die scatter point**. Getalle tussen hakies verwys na die vergelykings van die berekeningshandleiding (`doc/YA-MS_manuale_calcoli.docx`).

## Invoere van hierdie oortjie

| Veld | Verstek | Gebruik |
|---|---|---|
| **Drywing W** | 400 | Senderdrywing vir die skakelbegroting |
| **Antennawins dBi (tx = rx)** | 14 | Dieselfde antenna aan albei kante |
| **Minimum sein dBm** | −130 | Minimum waarneembare sein (artikel: 8-element-Yagi + voorversterker) |
| **Spoordigtheid q = 10^ … elektrone/m** | 14 | Lineêre elektrondigtheid van die onderdigte spoor |

Die stasies, band, spoorhoogte, lob-elevasie, boom en hot spot-afstand kom van die [rye kontroles](Getting-Started-af#1-die-drie-rye-kontroles).

## Afdelings van die verslag

| Afdeling | Inhoud |
|---|---|
| **PADGEOMETRIE (sferiese Aarde, R = 6372,7955 km)** | Stasie en DX met hoogtes; afstand, azimut en teenazimut; middelpunt (lokator en koördinate); spoorhoogte (*<- modus gemeet deur die Collm-radar* wanneer van die radar geneem); antenna-elevasie na die middelpunt |
| **HOT A / HOT B (klassieke hot spots, vir antennarigting)** | Vir elkeen: lokator, azimut vanaf jou en verskuiwing van die direkte pad, azimut vanaf die DX, afstand, elevasie |
| **GRENSE VAN DIE GEMEENSKAPLIKE SONE** | Bereik op spoorhoogte met die lob-elevasie; Grens A / Grens B met azimute |
| Antenna | Boom in λ, wins, horisontale / vertikale lob; of Hot A en Hot B binne of buite die lob is |
| **PADVERLIES (onderdigte spoor, McKinley 1961; antennawins uitgesluit)** | Tabel vir die middelpunt (forward), Hot A en Hot B op 28, 50, 70, 144, 222 en 432 MHz |
| **SKAKELBEGROTING BY … MHz (middelpunt)** | Drywing en EIRP, padverlies, sein by die antenna, minimum waarneembaar, **marge**; dieselfde marge met OH5IY se gemiddelde verlies |
| **EKSPERIMENTELE REËLS TUSSEN BANDE (SM6FHZ, VUSHF 2025)** | Aantal/intensiteit en duur vergeleke met 144 MHz; IARU-maksimum ping |

## Lokator en pad

Lokator (4, 6 of 8 karakters; middel van die vierkant, IARU Maidenhead-stelsel) [14]. Afstand, azimut en middelpunt met grootsirkelformules op 'n sfeer met radius **r = 6372,7955 km** (Cerrotta–Sartori-artikel) [15–16]. Tydafhanklike berekeninge verwys na die **middelpunt**, omdat die beste tyd tot 1,5 uur tussen die twee kante kan verskil (SM6FHZ).

## Antenna-elevasie

**Bron:** formule uit die Cerrotta–Sartori-artikel (figuur 7), met x = d/r, d die grondafstand tot die refleksiepunt, H die spoorhoogte en h die stasiehoogte [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Kontrole:** dit stem binne 0,03° met eksakte sferiese geometrie ooreen. Die program gebruik die arktangens met twee argumente, wat negatiewe waardes anderkant die horison gee en die periodisiteitsprobleem vermy wat in die artikel genoem word. 'n Negatiewe elevasie na die middelpunt beteken *pad anderkant die geometriese bereik van 'n enkele sprong*.

## Horisonbereik

Grondafstand waarop 'n straal met elevasie e die hoogte H bereik (geometriese inverse van die formule hierbo) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Kontrole:** H = 89,5 km, e = 0° → **1062 km**. In die artikel se voorbeeld (JN44BB–IO53RT) plaas die tekening die horisonkruisings ongeveer 870 km van die stasies, wat ooreenstem met 'n lob wat ongeveer 2° gelig is (865 km).

## Grense van die gemeenskaplike sone

**Bron:** die artikel plaas die kruisings van die kurwes waar elke stasie se horison die E-laag ontmoet: die snypunte van twee sirkels met hoekradius ρ = d_H/r gesentreer op A en B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

As 1 − |p0|² < 0 is die pad langer as 2·d_H en sien die stasies **geen gemeenskaplike E-laagsone nie**.

**Kontrole:** dit is die **verste rande** van die hemel wat albei stasies sien, **nie punte om op te mik nie**. Op JN70CN–IN78UO (1710 km, azimut 308°) val hulle 1062 km van die stasie, 37° links en regs van die direkte pad, terwyl MSHV 10° voorstel. Daarom word hulle *Grens A* / *Grens B* genoem en dof op die kaart geteken.

## Hot A en Hot B

**Bron:** refleksies van sporadiese meteore konsentreer in twee sones ("hot spots") aan weerskante van die middelpunt. J. Richardson (AMS) gee in die tabel wat DJ5HG aanhaal (*Die Geometrie von Meteorscatterverbindungen*, 2004) die antennaverskuiwing vanaf die direkte rigting: **13° by 1000 km, 11° by 1250 km, 10° by 1500 en 2000 km**. AMS Bulletin No. 203, oorgeneem deur W8WN, gee 10° by 1500 en 1800 km.

**Keuse:** Hot A en Hot B is die punte op afstand s van die middelpunt M, loodreg op die pad. Met *auto (AMS)* gemerk (verstek) kom s uit die verskuiwing van Richardson se tabel, lineêr geïnterpoleer (13° onder 1000 km, 10° bo 2000 km): s = (D/2)·tan(verskuiwing). Ongemerk word s met die hand ingevoer, 30–400 km (MSHV gebruik 150 km); A links as jy van jou stasie na die DX kyk, B regs [21]. Die verskuiwing soos vanaf die stasie gesien is ongeveer [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Kontrole:** met die AMS-tabel, 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, dieselfde as die 150 km wat voorheen en deur MSHV gebruik is; op kort paaie bring die tabel die hot spots nader aan die middelpunt.

## Onderdigte padverlies

**Bron:** McKinley se vergelyking en ITU-R-aanbeveling P.843 vir onderdigte spore (sin α = 1), antennawins uitgesluit; q = lineêre elektrondigtheid, r_e = klassieke elektronradius = 2,818·10⁻¹⁵ m, R1, R2 afstande vanaf die spoor, φ die helfte van die verstrooiingshoek, β hoek tussen die spoor en die padvlak, a₁ beginradiusfaktor met r₀ in m en h in km (P.843, vgl. 4 en 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Keuse:** die skakelbegroting en die verliestabel gebruik β = 90° (spoor wat die padvlak kruis, die ongunstigste geval: versigtige waarde) en die skakelbegroting toon ook die beste geval, β = 0. r₀ word geneem by die gemiddelde eggohoogte vir die frekwensie, h = 124 − 17 log f (P.843, vgl. 15): 0,76 m by 95 km vir 50 MHz, 0,40 m by 87 km vir 144 MHz, 0,21 m by 79 km vir 432 MHz. Oor 1000 km is a₁ 0,2 dB op 50 MHz, 0,6 dB op 144 MHz en 1,4 dB op 432 MHz (2,9 dB by 600 km); by DJ5HG se vaste 102 km sou dit sowat 70 dB op 432 MHz wees, m.a.w. glad geen eggo nie.

**Kontrole:** met q = 10¹⁴ elektrone/m, spore op 89,5 km en β = 0, op 144 MHz: **182–192 dB** tussen 600 en 2100 km (185 dB by 1000 km), binne die reeks van **172–190 dB** wat John Worsnop **G4BAO** in sy PhD-proefskrif bereken het, soos deur GM8JBJ gerapporteer. Met β = 90° neem die verlies toe met 10 dB by 600 km, 13 dB by 1000 km en 16 dB by 2100 km; die **gemiddelde van 200 dB** van OH5IY lê tussen die twee gevalle. Die 182 dB in GM8JBJ se tabel is nie 'n bevestiging nie: die tabel gee geen frekwensie nie, sy 86,4 dB per been is die vrye-ruimte-verlies oor 500 km op 1 MHz (die term 20 log f ontbreek: 129,6 dB op 144 MHz) en sy items tel op tot 163,8 dB, nie 182 nie; die bladsy sê nóg "minimum" nóg "144 MHz".

## Skakelbegroting

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Winse word in dBi ingevoer en gebruik: McKinley se verlies verwys na isotropiese antennes, dus word geen dipoolkorreksie van 2,15 dB afgetrek nie (EIRP = drywing + wins). Die verslag gee ook die marge met **OH5IY se gemiddelde padverlies** (200 dB op 144 MHz, met λ³ na die gekose band geskaal). Verwysing uit die artikel: ongeveer **70 dBm EIRP** is nodig (−130 dBm + 200 dB, bv. ongeveer 400 W in 14 dBi).

## Wins en lob van die antenna

**Wins – bron:** kurwe van Günter Hoch **DL6WU** vir lang Yagi's as funksie van die boomlengte L, gerapporteer deur W8IO (geldig vanaf ongeveer 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Kontrole teen die NEC-modelle van L.B. Cebik W4RNL op 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elemente | Boom (λ) | W4RNL NEC (dBi) | Formule (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Die verskil oorskry nooit **0,1 dB** nie: die wins hang meer van die boomlengte af as van die ontwerp (VK3AUU-Yagi's het 'n korter boom vir dieselfde aantal elemente). Die Yagi Calculator van VK5DJ gee ook skattings vir die VK3AUU-, WA2PHW- en DJ9BV-variante, waarvan die formules nie gepubliseer is nie.

**Lob – bron:** Kraus-reël, met 'n sirkelvormige lob θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Kontrole:** W4RNL se NEC-modelle van DL6WU-Yagi's gee 'n **horisontale lob 5–10 % nouer** as Kraus: 33,8° / 26,4° / 22,6° vir 12, 19 en 26 elemente, teenoor 37,3° / 28,0° / 23,9°. Eenvoudige formules ignoreer die voorwaartse sylobbe (W4RNL, *Long-Boom Yagi Rules of Thumb*). Op lang booms is die vertikale lob effens wyer as die horisontale (14 λ: 18,4° / 18,8°).

**Keuse** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Voorbeeld: 14 λ-Yagi op 432 MHz → 20,3 dBi, lob 18,1° horisontaal en 19,5° vertikaal; W4RNL se modelle gee 20,4 dBi en 18,4° / 18,8°. Dit is benaderde reëls, afgelei van 'n paar DL6WU-antennas.

Die antenna word altyd beskou as na die DX gerig. 'n Hot spot is **binne die lob** as |Az(Hot) − Az(antenna)| ≤ θ_horizontal/2: dit word dan in grys op die [hemelkoepel](Sky-View-af) geteken en 'n waarskuwing verskyn. In die doeltreffendheidsberekening is die antennas isotropies; die werklike lob word slegs vir hierdie kontrole gebruik.

## Eksperimentele reëls tussen bande

Vergeleke met 144 MHz: aantal/intensiteit × (144/f)³ (in dB), duur × (144/f)² (SM6FHZ, VUSHF 2025). IARU Streek 1 se maksimum pingduur: 1000 ms op 50 MHz, 500 ms op 70 MHz, 100 ms op 144 MHz, 13 ms op 432 MHz (VHF Handbook, in die artikel aangehaal). Sien ook [Eksperimentele voorspellings](Experimental-Forecasts-af).
