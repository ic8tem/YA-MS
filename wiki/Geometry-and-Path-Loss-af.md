[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · **Afrikaans** · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

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
| **PADGEOMETRIE (WGS84-ellipsoïed)** | Stasie en DX met hoogtes; afstand, azimut en teenazimut; middelpunt (lokator en koördinate); spoorhoogte (*<- modus gemeet deur die Collm-radar* wanneer van die radar geneem); antenna-elevasie na die middelpunt |
| **HOT A / HOT B (klassieke hot spots, vir antennarigting)** | Vir elkeen: lokator, azimut vanaf jou en verskuiwing van die direkte pad, azimut vanaf die DX, afstand, elevasie |
| **GRENSE VAN DIE GEMEENSKAPLIKE SONE** | Bereik op spoorhoogte met die lob-elevasie; Grens A / Grens B met azimute |
| Antenna | Boom in λ, wins, horisontale / vertikale lob; of Hot A en Hot B binne of buite die lob is |
| **PADVERLIES (onderdigte spoor, McKinley 1961; antennawins uitgesluit)** | Tabel vir die middelpunt (forward), Hot A en Hot B op 28, 50, 70, 144, 222 en 432 MHz |
| **SKAKELBEGROTING BY … MHz (middelpunt)** | Drywing en EIRP, padverlies, sein by die antenna, minimum waarneembaar, **marge**; dieselfde marge met OH5IY se gemiddelde verlies |
| **EKSPERIMENTELE REËLS TUSSEN BANDE (SM6FHZ, VUSHF 2025)** | Aantal/intensiteit en duur vergeleke met 144 MHz; IARU-maksimum ping |

## Lokator en pad

Lokator (4, 6 of 8 karakters; middel van die vierkant, IARU Maidenhead-stelsel) [14]. Afstand, azimut en middelpunt op die geodeet van die **WGS84**-ellipsoïed met Karney se metode (vanaf weergawe 1.8.24; voorheen 'n sfeer met radius r = 6372,7955 km uit die artikel Cerrotta–Sartori [15–16]). Tydafhanklike berekeninge verwys na die **middelpunt**, omdat die beste tyd tot 1,5 uur tussen die twee kante kan verskil (SM6FHZ).

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

## Troposferiese refraksie (GFS)

Troposferiese refraksie (blokkie "Troposferiese refraksie (GFS)", af by begin). Met die blokkie aan laai die program van Open-Meteo die profiel van die GFS-model bo die twee stasies af (druk, temperatuur en humiditeit by die grond en op die vlakke van 1000 tot 500 hPa, op die naaste uur binne 6 uur), bepaal die hoogtes van die vlakke met die hipsometriese vergelyking (virtuele temperatuur) en die refraktiwiteit met die formule van Aanbeveling ITU-R P.453:

```math
N = \frac{77{.}6}{T}\left(P + \frac{4810\,e}{T}\right)
```

met P en e (dampdruk, uit die Magnus-formule) in hPa en T in kelvin. Bo die boonste vlak neem N eksponensieel af met 'n skaalhoogte van 7,35 km. As die GFS nie antwoord nie, word die P.453-verwysingsatmosfeer gebruik, N = 315·exp(−h/7,35), en die verslag sê so.

Die straal word deur dun sferiese skille gevolg met die wet van Snell in sferiese vorm (n·r·cos e konstant) tot by die spoorhoogte; dit gee die bereik op hoogte H en die korreksie van die elevasie:

```math
\Delta\varphi = \frac{k\,\Delta r}{r_m\,\bar u},\quad u = \sqrt{n^2r^2-k^2},\quad k = n_0 r_0\cos e
```

Voorbeeld met die verwysingsatmosfeer en spore op 89,5 km: by 0° gaan die bereik van 1061,5 na sowat 1133 km (+72 km) en die punt lyk 0,62° hoër; by 4° groei die bereik met 14 km en die korreksie is 0,20°; bo 10° is die effek weglaatbaar. Die korreksie geld vir die elevasie na die middelpunt, die radius van die gemeenskaplike sone, die hot spots en die punte van die doeltreffendheidskaart; punte onder die gebreekte horison word weggelaat. Die verslag gee dit in die reël "Refraksie".

Die ekwivalente aardradius k = 4/3 geld vir strale wat in die eerste kilometers van die troposfeer bly, waar N met sowat 40 eenhede per km daal. Die straal na 'n spoor op 90 km kruis die hele troposfeer en gaan bo 10-15 km, waar N amper nul is, byna reguit voort: met k = 4/3 oor die hele klim sou die bereik by 0° sowat 1230 km wees, amper 100 km meer as die gevolgde straal. Daarom volg die program die straal in die GFS-profiel, soos die outeur se LIVETROPOVHF vir troposferiese voortplanting doen, in plaas daarvan om k = 4/3 te gebruik.

→ [Open-Meteo (GFS)](https://open-meteo.com/) · [ITU-R P.453](https://www.itu.int/rec/R-REC-P.453)

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

**VE7BQH** – Wins van 'n Yagi as funksie van die boomlengte L: gemiddelde reguitlyn van die VE7BQH-tabelle per band (sowat 60 Yagi's per band, NEC-winste). Tussen hakies die omvang van die steekproef en die standaardafwyking:

```math
\begin{aligned}50\,\mathrm{MHz}:\ & G = 7{.}36\,\log_{10}(L/\lambda) + 11{.}67\ \mathrm{dBi} \\ 144\,\mathrm{MHz}:\ & G = 8{.}27\,\log_{10}(L/\lambda) + 11{.}31\ \mathrm{dBi} \\ 432\,\mathrm{MHz}:\ & G = 8{.}68\,\log_{10}(L/\lambda) + 11{.}03\ \mathrm{dBi}\end{aligned}
```

(50 MHz: 0,3–5 λ, 0,25 dB · 144 MHz: 0,75–8,9 λ, 0,15 dB · 432 MHz: 1,8–16 λ, 0,17 dB)

Die reguitlyn van die naaste band word gebruik: onder 100 MHz dié van 50 MHz, tussen 100 en 300 MHz dié van 144 MHz, bo 300 MHz dié van 432 MHz (vir 1296 MHz is dit 'n ekstrapolasie). Buite die omvang van die steekproef waarsku die hoofvenster dat die skatting onakkuraat is.

Historiese kurwe van DL6WU (VHF Communications 3/1982, fig. 1): metings by 432 en 1296 MHz uit 1981, 2,35 dB per oktaaf boom, verklaarde akkuraatheid 0,5 dB; G ≈ 9,2 + 7,81 log10(L/λ) dBd. W8IO gee dit as 7,773 log10(L/λ) + 11,43 dBi (minder as 0,1 dB verskil). Die program skryf dit ter vergelyking in die verslag:

```math
G = 7{.}81\,\log_{10}(L/\lambda) + 11{.}35\ \mathrm{dBi}
```

**Kontrole teen die NEC-modelle van L.B. Cebik W4RNL op 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elemente | Boom (λ) | W4RNL NEC (dBi) | Formule (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Die verskil oorskry nooit **0,1 dB** nie: die wins hang meer van die boomlengte af as van die ontwerp (VK3AUU-Yagi's het 'n korter boom vir dieselfde aantal elemente). Die Yagi Calculator van VK5DJ gee ook skattings vir die VK3AUU-, WA2PHW- en DJ9BV-variante, waarvan die formules nie gepubliseer is nie.

VE7BQH-gemiddelde minus DL6WU-kurwe: by 50 MHz binne 0,25 dB van 2 tot 16 λ; by 144 MHz van −0,04 dB by 1 λ tot +0,42 dB by 10 λ; by 432 MHz van −0,06 dB by 2 λ tot +0,55 dB by 10 λ. Op die DL6WU- en VK3AUU-Yagi's wat W4RNL by 432 MHz gesimuleer het, lê die VE7BQH-gemiddelde 0,15–0,55 dB bo NEC: op lang booms presteer die rekenaar-geoptimeerde Yagi's van die tabelle beter as die oorspronklike ontwerpe.

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

Met die VE7BQH-gemiddelde gee dieselfde Yagi van 14 λ 21,0 dBi en 'n lob van 16,9° horisontaal en 18,1° vertikaal; die 20,3 dBi hierbo kom van die DL6WU-kurwe. Die lobkorreksies (0,93 · θK en θK) bly dié wat van die DL6WU-Yagi's afgelei is.

Die antenna word altyd beskou as gerig op die DX. 'n Hot spot is **binne die lob** as |Az(Hot) − Az(antenna)| ≤ θ_horizontal/2: dit word dan grys geteken in die [hemelkoepel](Sky-View-af) en 'n waarskuwing verskyn. Die vertikale lob tel ook in die doeltreffendheidsberekening: met die blokkie *antennapatroon* aan word die weerkaatsingspunte geweeg met die vertikale wins van albei antennas (breedte θ_vertical, maksimum by die lobhoogte, grondfaktor tot nul by die horison).

## Eksperimentele reëls tussen bande

Vergeleke met 144 MHz: aantal/intensiteit × (144/f)³ (in dB), duur × (144/f)² (SM6FHZ, VUSHF 2025). IARU Streek 1 se maksimum pingduur: 1000 ms op 50 MHz, 500 ms op 70 MHz, 100 ms op 144 MHz, 13 ms op 432 MHz (VHF Handbook, in die artikel aangehaal). Sien ook [Eksperimentele voorspellings](Experimental-Forecasts-af).
