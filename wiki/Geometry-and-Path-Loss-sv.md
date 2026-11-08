[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · **Svenska** · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh)

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

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Kontroll:** den stämmer med exakt sfärisk geometri inom 0,03°. Programmet använder arcustangens med två argument, som ger negativa värden bortom horisonten och undviker periodicitetsproblemet som nämns i artikeln. En negativ elevation mot mittpunkten betyder *sträckan ligger utanför den geometriska räckvidden för ett enkelhopp*.

## Horisonträckvidd

Markavståndet där en stråle med elevationen e når höjden H (geometrisk invers av formeln ovan) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Kontroll:** H = 89,5 km, e = 0° → **1062 km**. I artikelns exempel (JN44BB–IO53RT) placerar ritningen horisontkorsningarna omkring 870 km från stationerna, vilket motsvarar en lob som är upplyft omkring 2° (865 km).

## Gränser för den gemensamma zonen

**Källa:** artikeln anger skärningspunkterna mellan de kurvor där varje stations horisont möter E-skiktet: skärningarna mellan två cirklar med vinkelradien ρ = d_H/r centrerade på A och B [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Om 1 − |p0|² < 0 är sträckan längre än 2·d_H och stationerna ser **ingen gemensam zon i E-skiktet**.

**Kontroll:** detta är de **yttersta kanterna** av den himmel som båda stationerna ser, **inte punkter att rikta mot**. På JN70CN–IN78UO (1710 km, azimut 308°) hamnar de 1062 km från stationen, 37° till vänster och höger om den direkta sträckan, medan MSHV föreslår 10°. Därför kallas de *Gräns A* / *Gräns B* och ritas svagt på kartan.

## Hot A och Hot B

**Källa:** reflexerna koncentreras till två zoner ("hot spots") omkring **50–150 km på var sida om mittpunkten**. Detta är grunden för tabellen över antennförskjutning i AMS Bulletin No. 203, som W8WN tagit upp (förskjutning 10° för sträckor på 1500 och 1800 km); MSHV av LZ2HV använder samma kriterium.

**Val:** Hot A och Hot B är punkterna på avståndet s från mittpunkten M, vinkelrätt mot sträckan (s = 150 km, justerbart 30–400 km); A till vänster sett från din station mot DX, B till höger [21]. Förskjutningen sett från stationen är ungefär [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Kontroll:** JN70CN–IN78UO, D = 1710 km: 6,7° med s = 100 km, **10,0° med s = 150 km** (samma som MSHV och AMS/W8WN), 13,2° med s = 200 km.

## Underdens sträckdämpning

**Källa:** McKinleys ekvation för underdensa spår (β = 0, sin α = 1), utan antennförstärkning; q = linjär elektrontäthet, r_e = klassiska elektronradien = 2,818·10⁻¹⁵ m, R1, R2 avstånden från spåret, φ halva spridningsvinkeln [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Kontroll:** med q = 10¹⁴ elektroner/m på 144 MHz: **181–192 dB** mellan 600 och 2200 km, i linje med artikelns referenser på 144 MHz: **182 dB minimum** (GM8JBJ, från Kaiser & Closs 1952) och **200 dB i genomsnitt** (OH5IY).

## Länkbudget

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. Förstärkningen anges i dBi och används i dBd (dBi − 2,15). Rapporten ger också marginalen med **OH5IY:s genomsnittliga sträckdämpning** (200 dB på 144 MHz, omräknad med λ³ till det valda bandet). Artikelns referens: omkring **70 dBm EIRP** behövs (−130 dBm + 200 dB, t.ex. omkring 400 W i 14 dBi).

## Antennförstärkning och lob

**Förstärkning – källa:** kurvan av Günter Hoch **DL6WU** för långa yagiantenner som funktion av bomlängden L, återgiven av W8IO (giltig från omkring 2 λ) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Kontroll mot NEC-modellerna av L.B. Cebik W4RNL på 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Element | Bom (λ) | W4RNL NEC (dBi) | Formel (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Skillnaden överstiger aldrig **0,1 dB**: förstärkningen beror mer på bomlängden än på konstruktionen (VK3AUU-yagis har kortare bom för samma antal element). Yagi Calculator av VK5DJ ger också uppskattningar för varianterna VK3AUU, WA2PHW och DJ9BV, vars formler inte är publicerade.

**Lob – källa:** Kraus regel, med cirkulär lob θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Kontroll:** W4RNL:s NEC-modeller av DL6WU-yagis ger en **horisontell lob som är 5–10 % smalare** än Kraus: 33,8° / 26,4° / 22,6° för 12, 19 och 26 element, mot 37,3° / 28,0° / 23,9°. Enkla formler bortser från de främre sidloberna (W4RNL, *Long-Boom Yagi Rules of Thumb*). På långa bommar är den vertikala loben något bredare än den horisontella (14 λ: 18,4° / 18,8°).

**Val** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Exempel: yagi på 14 λ på 432 MHz → 20,3 dBi, lob 18,1° horisontellt och 19,5° vertikalt; W4RNL:s modeller ger 20,4 dBi och 18,4° / 18,8°. Detta är ungefärliga regler härledda från ett fåtal DL6WU-antenner.

Antennen anses alltid vara riktad mot DX. En hot spot ligger **inom loben** om |Az(Hot) − Az(antenn)| ≤ θ_horisontell/2: den ritas då i grått i [Himlavalvet](Sky-View-sv) och en varning visas. I effektivitetsberäkningen är antennerna isotropa; den verkliga loben används bara för denna kontroll.

## Experimentella regler mellan banden

Jämfört med 144 MHz: antal/intensitet × (144/f)³ (i dB), varaktighet × (144/f)² (SM6FHZ, VUSHF 2025). IARU Region 1:s maximala pinglängd: 1000 ms på 50 MHz, 500 ms på 70 MHz, 100 ms på 144 MHz, 13 ms på 432 MHz (VHF Handbook, citerad i artikeln). Se även [Experimentella prognoser](Experimental-Forecasts-sv).
