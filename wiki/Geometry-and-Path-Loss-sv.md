[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-BR) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · **Svenska** · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-TW)

# Geometri och dämpning

*Flik: Prognosberäkning › Geometri och dämpning.*

[![Geometri och dämpning](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

En textrapport om sträckan (markerbar, så att du kan kopiera den) och till höger diagrammet **Antennelevation som funktion av avståndet till scatterpunkten**. Siffror inom hakparentes hänvisar till ekvationerna i beräkningshandboken (`doc/YA-MS_manuale_calcoli.docx`).

## Indata på den här fliken

| Fält | Standard | Användning |
|---|---|---|
| **Effekt W** | 400 | Sändareffekt för länkbudgeten |
| **Antennförstärkning dBi (tx = rx)** | 14 | Samma antenn i båda ändarna |
| **Minsta signal dBm** | −130 | Minsta detekterbara signal (artikeln: 8-elements yagi + förförstärkare) |
| **Spårtäthet q = 10^ … elektroner/m** | 14 | Linjär elektrontäthet i det underdensa spåret |

Stationer, band, spårhöjd, lobelevation, bom och hot spot-avstånd kommer från [raderna med reglage](Getting-Started-sv#1-de-tre-raderna-med-reglage).

## Rapportens avsnitt

| Avsnitt | Innehåll |
|---|---|
| **STRÄCKANS GEOMETRI (sfärisk jord, R = 6372,7955 km)** | Station och DX med höjder; avstånd, azimut och omvänd azimut; mittpunkt (lokator och koordinater); spårhöjd (*← typvärde uppmätt av Collm-radarn* när den tas från radarn); antennelevation mot mittpunkten |
| **HOT A / HOT B (klassiska hot spots, för antennriktning)** | För var och en: lokator, azimut från dig och förskjutning från den direkta sträckan, azimut från DX, avstånd, elevation |
| **GRÄNSER FÖR DEN GEMENSAMMA ZONEN** | Räckvidd på spårhöjden med lobelevationen; Gräns A / Gräns B med azimut |
| Antenn | Bom i λ, förstärkning, horisontell / vertikal lob; om Hot A och Hot B ligger inom eller utanför loben |
| **STRÄCKDÄMPNING (underdenst spår, McKinley 1961; antennförstärkning ej medräknad)** | Tabell för mittpunkten (forward), Hot A och Hot B på 28, 50, 70, 144, 222 och 432 MHz |
| **LÄNKBUDGET VID … MHz (mittpunkt)** | Effekt och EIRP, sträckdämpning, signal vid antennen, minsta detekterbara, **marginal**; samma marginal med OH5IY:s genomsnittliga dämpning |
| **EXPERIMENTELLA REGLER MELLAN BANDEN (SM6FHZ, VUSHF 2025)** | Antal/intensitet och varaktighet jämfört med 144 MHz; IARU:s maximala pinglängd |

## Lokator och sträcka

Lokator (4, 6 eller 8 tecken; rutans mittpunkt, IARU:s Maidenhead-system) [14]. Avstånd, azimut och mittpunkt med storcirkelformler på en sfär med radien **r = 6372,7955 km** (artikeln av Cerrotta–Sartori) [15–16]. Tidsberoende beräkningar avser **mittpunkten**, eftersom den bästa tiden kan skilja upp till 1,5 timmar mellan de två ändarna (SM6FHZ).

## Antennelevation

**Källa:** formeln i artikeln av Cerrotta–Sartori (figur 7), med x = d/r, där d är markavståndet till reflexionspunkten, H spårhöjden och h stationens höjd [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Kontroll:** den stämmer med exakt sfärisk geometri inom 0,03°. Programmet använder arcustangens med två argument, som ger negativa värden bortom horisonten och undviker periodicitetsproblemet som nämns i artikeln. En negativ elevation mot mittpunkten betyder *sträckan ligger utanför den geometriska räckvidden för ett enkelhopp*.

## Horisonträckvidd

Markavståndet där en stråle med elevationen e når höjden H (geometrisk invers av formeln ovan) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Kontroll:** H = 89,5 km, e = 0° → **1062 km**. I artikelns exempel (JN44BB–IO53RT) placerar ritningen horisontkorsningarna omkring 870 km från stationerna, vilket motsvarar en lob som är upplyft omkring 2° (865 km).

## Gränser för den gemensamma zonen

**Källa:** artikeln anger skärningspunkterna mellan de kurvor där varje stations horisont möter E-skiktet: skärningarna mellan två cirklar med vinkelradien ρ = d_H/r centrerade på A och B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Om 1 − |p0|² < 0 är sträckan längre än 2·d_H och stationerna ser **ingen gemensam zon i E-skiktet**.

**Kontroll:** detta är de **yttersta kanterna** av den himmel som båda stationerna ser, **inte punkter att rikta mot**. På JN70CN–IN78UO (1710 km, azimut 308°) hamnar de 1062 km från stationen, 37° till vänster och höger om den direkta sträckan, medan MSHV föreslår 10°. Därför kallas de *Gräns A* / *Gräns B* och ritas svagt på kartan.

## Hot A och Hot B

**Källa:** reflexerna från sporadiska meteorer koncentreras till två zoner ("hot spots") på var sida om mittpunkten. J. Richardson (AMS) anger i tabellen som DJ5HG citerar (*Die Geometrie von Meteorscatterverbindungen*, 2004) antennförskjutningen från den direkta riktningen: **13° vid 1000 km, 11° vid 1250 km, 10° vid 1500 och 2000 km**. AMS Bulletin No. 203, som W8WN tagit upp, anger 10° vid 1500 och 1800 km.

**Val:** Hot A och Hot B är punkterna på avståndet s från mittpunkten M, vinkelrätt mot sträckan. Med *auto (AMS)* ikryssat (standard) fås s ur förskjutningen i Richardsons tabell, linjärt interpolerad (13° under 1000 km, 10° över 2000 km): s = (D/2)·tan(förskjutning). Utan kryss anges s för hand, 30–400 km (MSHV använder 150 km); A till vänster sett från din station mot DX, B till höger [21]. Förskjutningen sett från stationen är ungefär [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Kontroll:** med AMS-tabellen 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, samma som de 150 km som användes tidigare och av MSHV; på korta sträckor flyttar tabellen hot spots närmare mittpunkten.

## Underdens sträckdämpning

**Källa:** McKinleys ekvation och ITU-R-rekommendation P.843 för underdensa spår (sin α = 1), utan antennförstärkning; q = linjär elektrontäthet, r_e = klassiska elektronradien = 2,818·10⁻¹⁵ m, R1, R2 avstånden från spåret, φ halva spridningsvinkeln, β vinkeln mellan spåret och sträckans plan, a₁ faktor för initialradien med r₀ i m och h i km (P.843, ekv. 4 och 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Val:** länkbudgeten och dämpningstabellen använder β = 90° (spår som korsar sträckans plan, det minst gynnsamma fallet: försiktigt värde) och länkbudgeten visar även det bästa fallet, β = 0. r₀ tas vid medelhöjden för ekon vid frekvensen, h = 124 − 17 log f (P.843, ekv. 15): 0,76 m vid 95 km för 50 MHz, 0,40 m vid 87 km för 144 MHz, 0,21 m vid 79 km för 432 MHz. Över 1000 km är a₁ 0,2 dB på 50 MHz, 0,6 dB på 144 MHz och 1,4 dB på 432 MHz (2,9 dB vid 600 km); vid DJ5HG:s fasta 102 km skulle den vara omkring 70 dB på 432 MHz, alltså inget eko alls.

**Kontroll:** med q = 10¹⁴ elektroner/m, spår på 89,5 km och β = 0, på 144 MHz: **182–192 dB** mellan 600 och 2100 km (185 dB vid 1000 km), inom intervallet **172–190 dB** som John Worsnop **G4BAO** beräknade i sin doktorsavhandling, enligt GM8JBJ. Med β = 90° ökar dämpningen med 10 dB vid 600 km, 13 dB vid 1000 km och 16 dB vid 2100 km; OH5IY:s **medelvärde på 200 dB** ligger mellan de två fallen. De 182 dB i GM8JBJ:s tabell är ingen bekräftelse: tabellen anger ingen frekvens, dess 86,4 dB per delsträcka är fritt-rum-dämpningen över 500 km vid 1 MHz (termen 20 log f saknas: 129,6 dB på 144 MHz) och dess poster summerar till 163,8 dB, inte 182; sidan säger varken "minimum" eller "144 MHz".

## Länkbudget

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Förstärkningen anges och används i dBi: McKinleys dämpning avser isotropa antenner, så ingen dipolkorrektion på 2,15 dB dras av (EIRP = effekt + förstärkning). Rapporten ger också marginalen med **OH5IY:s genomsnittliga sträckdämpning** (200 dB på 144 MHz, omräknad med λ³ till det valda bandet). Artikelns referens: omkring **70 dBm EIRP** behövs (−130 dBm + 200 dB, t.ex. omkring 400 W i 14 dBi).

## Antennförstärkning och lob

**Förstärkning – källa:** kurvan av Günter Hoch **DL6WU** för långa yagiantenner som funktion av bomlängden L, återgiven av W8IO (giltig från omkring 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Kontroll mot NEC-modellerna av L.B. Cebik W4RNL på 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Element | Bom (λ) | W4RNL NEC (dBi) | Formel (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Skillnaden överstiger aldrig **0,1 dB**: förstärkningen beror mer på bomlängden än på konstruktionen (VK3AUU-yagis har kortare bom för samma antal element). Yagi Calculator av VK5DJ ger också uppskattningar för varianterna VK3AUU, WA2PHW och DJ9BV, vars formler inte är publicerade.

**Lob – källa:** Kraus regel, med cirkulär lob θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Kontroll:** W4RNL:s NEC-modeller av DL6WU-yagis ger en **horisontell lob som är 5–10 % smalare** än Kraus: 33,8° / 26,4° / 22,6° för 12, 19 och 26 element, mot 37,3° / 28,0° / 23,9°. Enkla formler bortser från de främre sidloberna (W4RNL, *Long-Boom Yagi Rules of Thumb*). På långa bommar är den vertikala loben något bredare än den horisontella (14 λ: 18,4° / 18,8°).

**Val** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Exempel: yagi på 14 λ på 432 MHz → 20,3 dBi, lob 18,1° horisontellt och 19,5° vertikalt; W4RNL:s modeller ger 20,4 dBi och 18,4° / 18,8°. Detta är ungefärliga regler härledda från ett fåtal DL6WU-antenner.

Antennen anses alltid vara riktad mot DX. En hot spot ligger **inom loben** om |Az(Hot) − Az(antenn)| ≤ θ_horisontell/2: den ritas då i grått i [Himlavalvet](Sky-View-sv) och en varning visas. I effektivitetsberäkningen är antennerna isotropa; den verkliga loben används bara för denna kontroll.

## Experimentella regler mellan banden

Jämfört med 144 MHz: antal/intensitet × (144/f)³ (i dB), varaktighet × (144/f)² (SM6FHZ, VUSHF 2025). IARU Region 1:s maximala pinglängd: 1000 ms på 50 MHz, 500 ms på 70 MHz, 100 ms på 144 MHz, 13 ms på 432 MHz (VHF Handbook, citerad i artikeln). Se även [Experimentella prognoser](Experimental-Forecasts-sv).
