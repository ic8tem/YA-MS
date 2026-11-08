[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · **Eesti** · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh)

# Geomeetria ja sumbumine

*Sakk: Prognoosarvutus › Geomeetria ja sumbumine.*

[![Geomeetria ja sumbumine](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Trassi tekstiaruanne (valitav, nii et saad seda kopeerida) ja paremal graafik **Antenni elevatsioon sõltuvalt kaugusest hajumispunktini**. Nurksulgudes numbrid viitavad arvutusjuhendi (`doc/YA-MS_manuale_calcoli.docx`) võrranditele.

## Selle saki sisendid

| Väli | Vaikimisi | Kasutus |
|---|---|---|
| **Võimsus W** | 400 | Saatja võimsus lingi eelarve jaoks |
| **Antenni võimendus dBi (tx = rx)** | 14 | Sama antenn mõlemas otsas |
| **Minimaalne signaal dBm** | −130 | Minimaalne tuvastatav signaal (artikkel: 8-elemendiline Yagi + eelvõimendi) |
| **Jälje tihedus q = 10^ … elektroni/m** | 14 | Alatiheda jälje elektronide joontihedus |

Jaamad, sagedusala, jälgede kõrgus, peaharu elevatsioon, poom ja hot spoti kaugus tulevad [juhtnuppude ridadest](Getting-Started-et#1-kolm-juhtnuppude-rida).

## Aruande osad

| Osa | Sisu |
|---|---|
| **TRASSI GEOMEETRIA (sfääriline Maa, R = 6372,7955 km)** | Jaam ja korrespondent koos kõrgustega; kaugus, asimuut ja tagasisuuna asimuut; keskpunkt (lokaator ja koordinaadid); jälgede kõrgus (*<- Collmi radari mõõdetud mood*, kui võetud radarilt); antenni elevatsioon keskpunkti suunas |
| **HOT A / HOT B (klassikalised hot spotid antenni suunamiseks)** | Kummagi kohta: lokaator, asimuut sinult ja nihe otsesuunast, asimuut korrespondendilt, kaugus, elevatsioon |
| **ÜHISALA PIIRID** | Ulatus jälgede kõrgusel peaharu elevatsiooniga; Piir A / Piir B koos asimuutidega |
| Antenn | Poom λ-des, võimendus, horisontaalne / vertikaalne peaharu; kas Hot A ja Hot B on peaharu sees või väljas |
| **TRASSI SUMBUMINE (alatihe jälg, McKinley 1961; antennivõimendused välja arvatud)** | Tabel keskpunkti (forward), Hot A ja Hot B jaoks sagedustel 28, 50, 70, 144, 222 ja 432 MHz |
| **LINGI EELARVE SAGEDUSEL … MHz (keskpunkt)** | Võimsus ja EIRP, sumbumine, signaal antennil, minimaalne tuvastatav, **varu**; sama varu OH5IY keskmise sumbumisega |
| **EKSPERIMENTAALSED REEGLID SAGEDUSALADE VAHEL (SM6FHZ, VUSHF 2025)** | Arv/intensiivsus ja kestus võrreldes 144 MHz-ga; IARU maksimaalne ping |

## Lokaator ja trass

Lokaator (4, 6 või 8 märki; ruudu keskpunkt, IARU Maidenheadi süsteem) [14]. Kaugus, asimuut ja keskpunkt suurringjoone valemitega sfääril raadiusega **r = 6372,7955 km** (Cerrotta–Sartori artikkel) [15–16]. Ajast sõltuvad arvutused viitavad **keskpunktile**, sest parim aeg võib kahe otsa vahel erineda kuni 1,5 tundi (SM6FHZ).

## Antenni elevatsioon

**Allikas:** Cerrotta–Sartori artikli valem (joonis 7), kus x = d/r, d on maapealne kaugus peegelduspunktini, H jälgede kõrgus ja h jaama kõrgus [17]:

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Kontroll:** tulemus ühtib täpse sfäärilise geomeetriaga 0,03° piires. Programm kasutab kaheargumendilist arkustangensit, mis annab horisondi taga negatiivsed väärtused ja väldib artiklis mainitud perioodilisuse probleemi. Negatiivne elevatsioon keskpunkti suunas tähendab *trass on ühe hüppe geomeetrilisest ulatusest kaugemal*.

## Horisondi ulatus

Maapealne kaugus, mille juures elevatsiooniga e kiir jõuab kõrgusele H (ülaltoodud valemi geomeetriline pöördvalem) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Kontroll:** H = 89,5 km, e = 0° → **1062 km**. Artikli näites (JN44BB–IO53RT) asetab joonis horisondi lõikepunktid jaamadest umbes 870 km kaugusele, mis vastab umbes 2° võrra tõstetud peaharule (865 km).

## Ühisala piirid

**Allikas:** artikkel määrab kõverate lõikepunktid, kus kummagi jaama horisont kohtub E-kihiga: kahe A ja B keskmega ringi, nurkraadiusega ρ = d_H/r, lõikepunktid [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Kui 1 − |p0|² < 0, on trass pikem kui 2·d_H ja jaamad **ei näe E-kihi ühisala**.

**Kontroll:** need on mõlema jaama nähtava taeva **kaugeimad servad**, **mitte suunamispunktid**. Trassil JN70CN–IN78UO (1710 km, asimuut 308°) asuvad need jaamast 1062 km kaugusel, 37° otsesuunast vasakul ja paremal, samas kui MSHV soovitab 10°. Seepärast nimetatakse neid *Piir A* / *Piir B* ja joonistatakse kaardile kahvatult.

## Hot A ja Hot B

**Allikas:** peegeldused koonduvad kahte alasse ("hot spotid") umbes **50–150 km kaugusel mõlemal pool keskpunkti**. See on AMS Bulletin No. 203 antennisuuna nihete tabeli alus, mille võttis üle W8WN (10° nihe 1500 ja 1800 km trassidel); LZ2HV MSHV kasutab sama kriteeriumi.

**Valik:** Hot A ja Hot B on punktid kaugusel s keskpunktist M, trassiga risti (s = 150 km, reguleeritav 30–400 km); A vasakul, vaadates oma jaamast korrespondendi poole, B paremal [21]. Jaamast nähtav nihe on ligikaudu [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Kontroll:** JN70CN–IN78UO, D = 1710 km: 6,7° kui s = 100 km, **10,0° kui s = 150 km** (sama mis MSHV ja AMS/W8WN), 13,2° kui s = 200 km.

## Alatiheda jälje sumbumine

**Allikas:** McKinley võrrand alatihedate jälgede jaoks (β = 0, sin α = 1), antennivõimendused välja arvatud; q = elektronide joontihedus, r_e = elektroni klassikaline raadius = 2,818·10⁻¹⁵ m, R1, R2 kaugused jäljest, φ pool hajumisnurgast [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Kontroll:** q = 10¹⁴ elektroni/m korral sagedusel 144 MHz: **181–192 dB** vahemikus 600 kuni 2200 km, kooskõlas artikli viidetega 144 MHz kohta: **182 dB minimaalne** (GM8JBJ, Kaiser & Closs 1952 järgi) ja **200 dB keskmine** (OH5IY).

## Lingi eelarve

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. Võimendused sisestatakse dBi-des ja kasutatakse dBd-des (dBi − 2,15). Aruanne annab ka varu **OH5IY keskmise sumbumisega** (200 dB sagedusel 144 MHz, skaleeritud λ³ järgi valitud sagedusalale). Artikli viide: vaja on umbes **70 dBm EIRP-d** (−130 dBm + 200 dB, nt umbes 400 W 14 dBi antenni).

## Antenni võimendus ja peaharu

**Võimendus – allikas:** Günter Hoch **DL6WU** kõver pikkade Yagide jaoks poomi pikkuse L funktsioonina, vahendanud W8IO (kehtib alates umbes 2 λ) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Kontroll L.B. Cebik W4RNL-i NEC-mudelitega sagedusel 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elemendid | Poom (λ) | W4RNL NEC (dBi) | Valem (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Erinevus ei ületa kunagi **0,1 dB**: võimendus sõltub rohkem poomi pikkusest kui konstruktsioonist (VK3AUU Yagidel on sama elementide arvu juures lühem poom). VK5DJ Yagi Calculator annab hinnanguid ka VK3AUU, WA2PHW ja DJ9BV variantide jaoks, mille valemeid pole avaldatud.

**Peaharu – allikas:** Krausi reegel ümmarguse peaharuga θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Kontroll:** W4RNL-i NEC-mudelid DL6WU Yagide kohta annavad Krausist **5–10 % kitsama horisontaalse peaharu**: 33,8° / 26,4° / 22,6° 12, 19 ja 26 elemendi korral, võrreldes 37,3° / 28,0° / 23,9°. Lihtsad valemid ignoreerivad eesmisi kõrvalharusid (W4RNL, *Long-Boom Yagi Rules of Thumb*). Pikkade poomide korral on vertikaalne peaharu horisontaalsest veidi laiem (14 λ: 18,4° / 18,8°).

**Valik** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Näide: 14 λ Yagi sagedusel 432 MHz → 20,3 dBi, peaharu 18,1° horisontaalselt ja 19,5° vertikaalselt; W4RNL-i mudelid annavad 20,4 dBi ja 18,4° / 18,8°. Need on ligikaudsed reeglid, mis on tuletatud mõnest DL6WU antennist.

Antenni loetakse alati DX-ile suunatuks. Hot spot on **peaharu sees**, kui |Az(Hot) − Az(antenn)| ≤ θ_horisontaalne/2: siis joonistatakse see [Taevavõlvis](Sky-View-et) halliga ja ilmub hoiatus. Efektiivsuse arvutuses on antennid isotroopsed; tegelikku peaharu kasutatakse ainult selle kontrolli jaoks.

## Eksperimentaalsed reeglid sagedusalade vahel

Võrreldes 144 MHz-ga: arv/intensiivsus × (144/f)³ (dB-des), kestus × (144/f)² (SM6FHZ, VUSHF 2025). IARU 1. regiooni maksimaalne pingi kestus: 1000 ms 50 MHz-l, 500 ms 70 MHz-l, 100 ms 144 MHz-l, 13 ms 432 MHz-l (VHF Handbook, tsiteeritud artiklis). Vt ka [Eksperimentaalsed prognoosid](Experimental-Forecasts-et).
