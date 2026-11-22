[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · **Nederlands** · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

# Geometrie en demping

*Tabblad: Voorspellingsberekening › Geometrie en demping.*

[![Geometrie en demping](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/nl-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/nl-2_2.png)

Een tekstverslag van het traject (selecteerbaar, zodat je het kunt kopiëren) en rechts de grafiek **Antenne-elevatie als functie van de afstand tot het scatterpunt**. Getallen tussen haken verwijzen naar de vergelijkingen in de rekenhandleiding (`doc/YA-MS_manuale_calcoli.docx`).

## Invoer van dit tabblad

| Veld | Standaard | Gebruik |
|---|---|---|
| **Vermogen W** | 400 | Zendvermogen voor het linkbudget |
| **Antennewinst dBi (tx = rx)** | 14 | Dezelfde antenne aan beide kanten |
| **Minimaal signaal dBm** | −130 | Minimaal detecteerbaar signaal (artikel: 8-elements Yagi + voorversterker) |
| **Spoordichtheid q = 10^ … elektronen/m** | 14 | Lineaire elektronendichtheid van het onderdichte spoor |

De stations, band, spoorhoogte, bundelelevatie, boom en hotspot-afstand komen uit de [rijen bedieningselementen](Getting-Started-nl#1-de-drie-rijen-bedieningselementen).

## Onderdelen van het verslag

| Onderdeel | Inhoud |
|---|---|
| **TRAJECTGEOMETRIE (bolvormige aarde, R = 6372,7955 km)** | Station en tegenstation met hoogtes; afstand, azimut en tegenazimut; middelpunt (locator en coördinaten); spoorhoogte (*<- modus gemeten door de Collm-radar* als die van de radar komt); antenne-elevatie naar het middelpunt |
| **HOT A / HOT B (klassieke hotspots, voor het richten van de antenne)** | Voor elk: locator, azimut vanaf jou en afwijking van het directe traject, azimut vanaf het tegenstation, afstand, elevatie |
| **GRENZEN VAN DE GEMEENSCHAPPELIJKE ZONE** | Bereik op spoorhoogte met de bundelelevatie; Grens A / Grens B met azimuts |
| Antenne | Boom in λ, winst, horizontale / verticale bundel; of Hot A en Hot B binnen of buiten de bundel liggen |
| **TRAJECTDEMPING (onderdicht spoor, McKinley 1961; zonder antennewinst)** | Tabel voor het middelpunt (forward), Hot A en Hot B op 28, 50, 70, 144, 222 en 432 MHz |
| **LINKBUDGET OP … MHz (middelpunt)** | Vermogen en EIRP, trajectdemping, signaal op de antenne, minimaal detecteerbaar, **marge**; dezelfde marge met de gemiddelde demping van OH5IY |
| **EXPERIMENTELE REGELS TUSSEN DE BANDEN (SM6FHZ, VUSHF 2025)** | Aantal/intensiteit en duur vergeleken met 144 MHz; maximale IARU-ping |

## Locator en traject

Locator (4, 6 of 8 tekens; midden van het vak, IARU-Maidenheadsysteem) [14]. Afstand, azimut en middelpunt met grootcirkelformules op een bol met straal **r = 6372,7955 km** (artikel van Cerrotta–Sartori) [15–16]. Tijdsafhankelijke berekeningen verwijzen naar het **middelpunt**, omdat het beste tijdstip tussen de twee uiteinden tot 1,5 uur kan verschillen (SM6FHZ).

## Antenne-elevatie

**Bron:** formule uit het artikel van Cerrotta–Sartori (figuur 7), met x = d/r, d de grondafstand tot het reflectiepunt, H de spoorhoogte en h de stationshoogte [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Controle:** komt binnen 0,03° overeen met de exacte bolgeometrie. Het programma gebruikt de arctangens met twee argumenten, die voorbij de horizon negatieve waarden geeft en het periodiciteitsprobleem uit het artikel vermijdt. Een negatieve elevatie naar het middelpunt betekent *traject voorbij het geometrisch bereik van één sprong*.

## Bereik tot de horizon

Grondafstand waarop een straal met elevatie e de hoogte H bereikt (geometrische inverse van de formule hierboven) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Controle:** H = 89,5 km, e = 0° → **1062 km**. In het voorbeeld uit het artikel (JN44BB–IO53RT) legt de tekening de horizonsnijpunten op ongeveer 870 km van de stations, wat overeenkomt met een bundel die ongeveer 2° is opgeheven (865 km).

## Troposferische refractie (GFS)

Troposferische refractie (vakje "Troposferische refractie (GFS)", uit bij het starten). Met het vakje aan haalt het programma bij Open-Meteo het profiel van het GFS-model boven de twee stations op (druk, temperatuur en vochtigheid aan de grond en op de niveaus van 1000 tot 500 hPa, op het dichtstbijzijnde uur binnen 6 uur), bepaalt de hoogten van de niveaus met de hypsometrische vergelijking (virtuele temperatuur) en de refractiviteit met de formule van Aanbeveling ITU-R P.453:

```math
N = \frac{77{.}6}{T}\left(P + \frac{4810\,e}{T}\right)
```

met P en e (dampdruk, uit de formule van Magnus) in hPa en T in kelvin. Boven het hoogste niveau neemt N exponentieel af met een schaalhoogte van 7,35 km. Als het GFS niet antwoordt, wordt de referentieatmosfeer van P.453 gebruikt, N = 315·exp(−h/7,35), en het verslag vermeldt dat.

De straal wordt door dunne bolschillen gevolgd met de wet van Snellius in bolvorm (n·r·cos e constant) tot de spoorhoogte; daaruit volgen het bereik op hoogte H en de correctie van de elevatie:

```math
\Delta\varphi = \frac{k\,\Delta r}{r_m\,\bar u},\quad u = \sqrt{n^2r^2-k^2},\quad k = n_0 r_0\cos e
```

Voorbeeld met de referentieatmosfeer en sporen op 89,5 km: bij 0° gaat het bereik van 1061,5 naar ongeveer 1133 km (+72 km) en lijkt het punt 0,62° hoger; bij 4° groeit het bereik met 14 km en is de correctie 0,20°; boven 10° is het effect verwaarloosbaar. De correctie geldt voor de elevatie naar het middelpunt, de straal van de gemeenschappelijke zone, de hot spots en de punten van de efficiëntiekaart; punten onder de gebroken horizon vallen weg. Het verslag geeft haar op de regel "Refractie".

De equivalente aardstraal k = 4/3 geldt voor stralen die in de eerste kilometers van de troposfeer blijven, waar N met ongeveer 40 eenheden per km afneemt. De straal naar een spoor op 90 km doorkruist de hele troposfeer en gaat boven 10-15 km, waar N bijna nul is, vrijwel recht verder: met k = 4/3 over de hele klim zou het bereik bij 0° ongeveer 1230 km zijn, bijna 100 km meer dan de gevolgde straal. Daarom volgt het programma de straal in het GFS-profiel, zoals LIVETROPOVHF van de auteur doet voor troposferische propagatie, in plaats van k = 4/3 te gebruiken.

→ [Open-Meteo (GFS)](https://open-meteo.com/) · [ITU-R P.453](https://www.itu.int/rec/R-REC-P.453)

## Grenzen van de gemeenschappelijke zone

**Bron:** het artikel bepaalt de snijpunten van de curven waar de horizon van elk station de E-laag raakt: de snijpunten van twee cirkels met hoekstraal ρ = d_H/r rond A en B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Als 1 − |p0|² < 0 is het traject langer dan 2·d_H en zien de stations **geen gemeenschappelijke zone in de E-laag**.

**Controle:** dit zijn de **verste randen** van de hemel die beide stations zien, **geen punten om op te richten**. Op JN70CN–IN78UO (1710 km, azimut 308°) liggen ze op 1062 km van het station, 37° links en rechts van het directe traject, terwijl MSHV 10° voorstelt. Daarom heten ze *Grens A* / *Grens B* en worden ze vaag op de kaart getekend.

## Hot A en Hot B

**Bron:** reflecties van sporadische meteoren concentreren zich in twee zones ("hotspots") aan weerszijden van het middelpunt. J. Richardson (AMS) geeft in de door DJ5HG aangehaalde tabel (*Die Geometrie von Meteorscatterverbindungen*, 2004) de antenne-afwijking ten opzichte van de directe richting: **13° bij 1000 km, 11° bij 1250 km, 10° bij 1500 en 2000 km**. AMS Bulletin nr. 203, overgenomen door W8WN, geeft 10° bij 1500 en 1800 km.

**Keuze:** Hot A en Hot B zijn de punten op afstand s van het middelpunt M, loodrecht op het traject. Met *auto (AMS)* aangevinkt (standaard) volgt s uit de afwijking van de tabel van Richardson, lineair geïnterpoleerd (13° onder 1000 km, 10° boven 2000 km): s = (D/2)·tan(afwijking). Niet aangevinkt wordt s met de hand ingevoerd, 30–400 km (MSHV gebruikt 150 km); A links, kijkend van jouw station naar de DX, B rechts [21]. De afwijking gezien vanaf het station is ongeveer [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Controle:** met de AMS-tabel 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, gelijk aan de eerder en door MSHV gebruikte 150 km; op korte trajecten brengt de tabel de hotspots dichter bij het middelpunt.

## Demping bij onderdichte sporen

**Bron:** de vergelijking van McKinley en ITU-R-aanbeveling P.843 voor onderdichte sporen (sin α = 1), zonder antennewinst; q = lineaire elektronendichtheid, r_e = klassieke elektronstraal = 2,818·10⁻¹⁵ m, R1, R2 afstanden tot het spoor, φ de halve verstrooiingshoek, β hoek tussen het spoor en het trajectvlak, a₁ beginstraalfactor met r₀ in m en h in km (P.843, vgl. 4 en 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Keuze:** het linkbudget en de dempingstabel gebruiken β = 90° (spoor dat het trajectvlak kruist, het minst gunstige geval: voorzichtige waarde) en het linkbudget toont ook het beste geval, β = 0. r₀ wordt genomen op de gemiddelde echohoogte voor de frequentie, h = 124 − 17 log f (P.843, vgl. 15): 0,76 m op 95 km voor 50 MHz, 0,40 m op 87 km voor 144 MHz, 0,21 m op 79 km voor 432 MHz. Over 1000 km is a₁ 0,2 dB op 50 MHz, 0,6 dB op 144 MHz en 1,4 dB op 432 MHz (2,9 dB op 600 km); bij de vaste 102 km van DJ5HG zou het op 432 MHz ongeveer 70 dB zijn, dus helemaal geen echo.

**Controle:** met q = 10¹⁴ elektronen/m, sporen op 89,5 km en β = 0, op 144 MHz: **182–192 dB** tussen 600 en 2100 km (185 dB op 1000 km), binnen het bereik van **172–190 dB** dat John Worsnop **G4BAO** in zijn proefschrift berekende, zoals GM8JBJ vermeldt. Met β = 90° neemt de demping toe met 10 dB op 600 km, 13 dB op 1000 km en 16 dB op 2100 km; het **gemiddelde van 200 dB** van OH5IY ligt tussen beide gevallen. De 182 dB in de tabel van GM8JBJ zijn geen bevestiging: de tabel noemt geen frequentie, de 86,4 dB per deeltraject zijn de vrije-ruimtedemping over 500 km op 1 MHz (de term 20 log f ontbreekt: 129,6 dB op 144 MHz) en de posten tellen op tot 163,8 dB, niet 182; de pagina zegt noch "minimum" noch "144 MHz".

## Linkbudget

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Winsten worden in dBi ingevoerd en gebruikt: de demping volgens McKinley geldt voor isotrope antennes, dus wordt er geen dipoolcorrectie van 2,15 dB afgetrokken (EIRP = vermogen + winst). Het verslag geeft ook de marge met de **gemiddelde trajectdemping van OH5IY** (200 dB op 144 MHz, met λ³ omgerekend naar de gekozen band). Referentie uit het artikel: er is ongeveer **70 dBm EIRP** nodig (−130 dBm + 200 dB, bijv. ongeveer 400 W in 14 dBi).

## Antennewinst en bundel

**VE7BQH** – Winst van een Yagi als functie van de boomlengte L: gemiddelde rechte van de tabellen van VE7BQH per band (ongeveer 60 Yagi's per band, NEC-winsten). Tussen haakjes het bereik van de steekproef en de standaardafwijking:

```math
\begin{aligned}50\,\mathrm{MHz}:\ & G = 7{.}36\,\log_{10}(L/\lambda) + 11{.}67\ \mathrm{dBi} \\ 144\,\mathrm{MHz}:\ & G = 8{.}27\,\log_{10}(L/\lambda) + 11{.}31\ \mathrm{dBi} \\ 432\,\mathrm{MHz}:\ & G = 8{.}68\,\log_{10}(L/\lambda) + 11{.}03\ \mathrm{dBi}\end{aligned}
```

(50 MHz: 0,3–5 λ, 0,25 dB · 144 MHz: 0,75–8,9 λ, 0,15 dB · 432 MHz: 1,8–16 λ, 0,17 dB)

De rechte van de dichtstbijzijnde band wordt gebruikt: onder 100 MHz die van 50 MHz, tussen 100 en 300 MHz die van 144 MHz, boven 300 MHz die van 432 MHz (voor 1296 MHz is dat een extrapolatie). Buiten het bereik van de steekproef waarschuwt het hoofdvenster dat de schatting onnauwkeurig is.

Historische curve van DL6WU (VHF Communications 3/1982, fig. 1): metingen op 432 en 1296 MHz uit 1981, 2,35 dB per octaaf boom, opgegeven nauwkeurigheid 0,5 dB; G ≈ 9,2 + 7,81 log10(L/λ) dBd. W8IO geeft haar als 7,773 log10(L/λ) + 11,43 dBi (minder dan 0,1 dB verschil). Het programma schrijft haar ter vergelijking in het rapport:

```math
G = 7{.}81\,\log_{10}(L/\lambda) + 11{.}35\ \mathrm{dBi}
```

**Controle tegen de NEC-modellen van L.B. Cebik W4RNL op 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementen | Boom (λ) | W4RNL NEC (dBi) | Formule (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Het verschil is nooit groter dan **0,1 dB**: de winst hangt meer af van de boomlengte dan van het ontwerp (VK3AUU-Yagi's hebben bij hetzelfde aantal elementen een kortere boom). De Yagi Calculator van VK5DJ geeft ook schattingen voor de varianten VK3AUU, WA2PHW en DJ9BV, waarvan de formules niet zijn gepubliceerd.

VE7BQH-gemiddelde min DL6WU-curve: op 50 MHz binnen 0,25 dB van 2 tot 16 λ; op 144 MHz van −0,04 dB bij 1 λ tot +0,42 dB bij 10 λ; op 432 MHz van −0,06 dB bij 2 λ tot +0,55 dB bij 10 λ. Bij de door W4RNL op 432 MHz gesimuleerde DL6WU- en VK3AUU-Yagi's ligt het VE7BQH-gemiddelde 0,15–0,55 dB boven NEC: op lange booms presteren de computergeoptimaliseerde Yagi's van de tabellen beter dan de oorspronkelijke ontwerpen.

**Bundel – bron:** regel van Kraus, met een cirkelvormige bundel θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Controle:** de NEC-modellen van W4RNL voor DL6WU-Yagi's geven een **horizontale bundel die 5–10 % smaller is** dan volgens Kraus: 33,8° / 26,4° / 22,6° voor 12, 19 en 26 elementen, tegenover 37,3° / 28,0° / 23,9°. Eenvoudige formules negeren de voorwaartse zijlobben (W4RNL, *Long-Boom Yagi Rules of Thumb*). Bij lange booms is de verticale bundel iets breder dan de horizontale (14 λ: 18,4° / 18,8°).

**Keuze** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Voorbeeld: Yagi van 14 λ op 432 MHz → 20,3 dBi, bundel 18,1° horizontaal en 19,5° verticaal; de modellen van W4RNL geven 20,4 dBi en 18,4° / 18,8°. Het zijn benaderende regels, afgeleid van een paar DL6WU-antennes.

Met het VE7BQH-gemiddelde geeft dezelfde Yagi van 14 λ 21,0 dBi en een bundel van 16,9° horizontaal en 18,1° verticaal; de 20,3 dBi hierboven komen uit de DL6WU-curve. De bundelcorrecties (0,93 · θK en θK) blijven de uit de DL6WU-Yagi's afgeleide.

De antenne wordt altijd als op de DX gericht beschouwd. Een hot spot ligt **in de lob** als |Az(Hot) − Az(antenne)| ≤ θ_horizontal/2: hij wordt dan grijs getekend in de [Hemelkoepel](Sky-View-nl) en er verschijnt een waarschuwing. De verticale lob telt ook mee in de rendementsberekening: met het vakje *antennediagram* aan worden de reflectiepunten gewogen met de verticale winst van beide antennes (breedte θ_vertical, maximum bij de lobelevatie, grondfactor tot nul aan de horizon).

## Experimentele regels tussen de banden

Vergeleken met 144 MHz: aantal/intensiteit × (144/f)³ (in dB), duur × (144/f)² (SM6FHZ, VUSHF 2025). Maximale pingduur volgens IARU Regio 1: 1000 ms op 50 MHz, 500 ms op 70 MHz, 100 ms op 144 MHz, 13 ms op 432 MHz (VHF Handbook, geciteerd in het artikel). Zie ook [Experimentele voorspelling](Experimental-Forecasts-nl).
