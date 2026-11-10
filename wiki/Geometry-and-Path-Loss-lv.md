[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · **Latviešu** · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh)

# Ģeometrija un vājinājums

*Cilne: Prognozes aprēķins › Ģeometrija un vājinājums.*

[![Ģeometrija un vājinājums](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Trases teksta atskaite (iezīmējama, tāpēc to var nokopēt) un labajā pusē grafiks **Antenas elevācija atkarībā no attāluma līdz scatter point**. Skaitļi kvadrātiekavās attiecas uz aprēķinu rokasgrāmatas vienādojumiem (`doc/YA-MS_manuale_calcoli.docx`).

## Šīs cilnes ievaddati

| Lauks | Noklusējums | Lietojums |
|---|---|---|
| **Jauda W** | 400 | Raidītāja jauda sakaru budžetam |
| **Antenas pastiprinājums dBi (tx = rx)** | 14 | Tā pati antena abos galos |
| **Minimālais signāls dBm** | −130 | Minimālais uztveramais signāls (raksts: 8 elementu Yagi + priekšpastiprinātājs) |
| **Sliedes blīvums q = 10^ … elektroni/m** | 14 | Zema blīvuma sliedes elektronu lineārais blīvums |

Stacijas, josla, sliežu augstums, ziedlapiņas elevācija, traverse un hot spot attālums nāk no [vadības rindām](Getting-Started-lv#1-trīs-vadības-rindas).

## Atskaites sadaļas

| Sadaļa | Saturs |
|---|---|
| **TRASES ĢEOMETRIJA (sfēriska Zeme, R = 6372,7955 km)** | Stacija un DX ar augstumiem; attālums, azimuts un pretējais azimuts; viduspunkts (lokators un koordinātas); sliežu augstums (*<- Collm radara izmērītā moda*, ja ņemts no radara); antenas elevācija uz viduspunktu |
| **HOT A / HOT B (klasiskie hot spot, antenas tēmēšanai)** | Katram: lokators, azimuts no tevis un nobīde no tiešās trases, azimuts no DX, attālums, elevācija |
| **KOPĒJĀS ZONAS ROBEŽAS** | Sniedzamība sliežu augstumā ar ziedlapiņas elevāciju; Robeža A / Robeža B ar azimutiem |
| Antena | Traverse λ, pastiprinājums, horizontālā / vertikālā ziedlapiņa; vai Hot A un Hot B ir ziedlapiņā vai ārpus tās |
| **TRASES VĀJINĀJUMS (zema blīvuma sliede, McKinley 1961; bez antenu pastiprinājuma)** | Tabula viduspunktam (forward), Hot A un Hot B pie 28, 50, 70, 144, 222 un 432 MHz |
| **SAKARU BUDŽETS PIE … MHz (viduspunkts)** | Jauda un EIRP, trases vājinājums, signāls pie antenas, minimālais uztveramais, **rezerve**; tā pati rezerve ar OH5IY vidējo vājinājumu |
| **EKSPERIMENTĀLIE LIKUMI STARP JOSLĀM (SM6FHZ, VUSHF 2025)** | Skaits/intensitāte un ilgums salīdzinājumā ar 144 MHz; IARU maksimālais pings |

## Lokators un trase

Lokators (4, 6 vai 8 rakstzīmes; kvadrāta centrs, IARU Maidenhead sistēma) [14]. Attālums, azimuts un viduspunkts ar lielā loka formulām uz sfēras ar rādiusu **r = 6372,7955 km** (Cerrotta–Sartori raksts) [15–16]. No laika atkarīgie aprēķini attiecas uz **viduspunktu**, jo labākais laiks abos galos var atšķirties līdz pat 1,5 stundām (SM6FHZ).

## Antenas elevācija

**Avots:** Cerrotta–Sartori raksta formula (7. attēls), kur x = d/r, d – attālums pa zemi līdz atstarošanas punktam, H – sliežu augstums un h – stacijas augstums [17]:

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Pārbaude:** tā sakrīt ar precīzo sfērisko ģeometriju 0,03° robežās. Programma izmanto divargumentu arktangensu, kas aiz horizonta dod negatīvas vērtības un novērš rakstā minēto periodiskuma problēmu. Negatīva elevācija uz viduspunktu nozīmē *trase ir ārpus viena lēciena ģeometriskās sniedzamības*.

## Horizonta sniedzamība

Attālums pa zemi, kurā stars ar elevāciju e sasniedz augstumu H (iepriekšējās formulas ģeometriskā inversija) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Pārbaude:** H = 89,5 km, e = 0° → **1062 km**. Raksta piemērā (JN44BB–IO53RT) zīmējumā horizonta krustpunkti ir ap 870 km no stacijām, kas atbilst ziedlapiņai, kas pacelta par apmēram 2° (865 km).

## Kopējās zonas robežas

**Avots:** raksts nosaka līkņu krustpunktus, kur katras stacijas horizonts satiekas ar E slāni: divu apļu ar leņķisko rādiusu ρ = d_H/r un centriem A un B krustpunkti [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Ja 1 − |p0|² < 0, trase ir garāka par 2·d_H, un stacijas neredz **nevienu kopēju E slāņa zonu**.

**Pārbaude:** tās ir abu staciju redzamo debesu **tālākās malas**, **nevis punkti, uz kuriem tēmēt**. Trasē JN70CN–IN78UO (1710 km, azimuts 308°) tās ir 1062 km no stacijas, 37° pa kreisi un pa labi no tiešās trases, kamēr MSHV iesaka 10°. Tāpēc tās sauc par *Robeža A* / *Robeža B* un kartē zīmē blāvi.

## Hot A un Hot B

**Avots:** atstarojumi koncentrējas divās zonās ("hot spot") ap **50–150 km abpus viduspunktam**. Tas ir AMS Bulletin Nr. 203 antenas nobīžu tabulas pamatā, ko pārņēmis W8WN (10° nobīde 1500 un 1800 km trasēm); LZ2HV MSHV izmanto to pašu kritēriju.

**Izvēle:** Hot A un Hot B ir punkti attālumā s no viduspunkta M, perpendikulāri trasei (s = 150 km, regulējams 30–400 km); A pa kreisi, skatoties no tavas stacijas uz DX, B pa labi [21]. Nobīde, kā to redz stacija, ir aptuveni [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Pārbaude:** JN70CN–IN78UO, D = 1710 km: 6,7° ar s = 100 km, **10,0° ar s = 150 km** (tāpat kā MSHV un AMS/W8WN), 13,2° ar s = 200 km.

## Zema blīvuma trases vājinājums

**Avots:** McKinley vienādojums zema blīvuma sliedēm (β = 0, sin α = 1), bez antenu pastiprinājuma; q = elektronu lineārais blīvums, r_e = klasiskais elektrona rādiuss = 2,818·10⁻¹⁵ m, R1, R2 – attālumi no sliedes, φ – puse no izkliedes leņķa [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Pārbaude:** ar q = 10¹⁴ elektroni/m pie 144 MHz: **181–192 dB** starp 600 un 2200 km, saskaņā ar raksta atsaucēm 144 MHz: **182 dB minimums** (GM8JBJ, no Kaiser & Closs 1952) un **200 dB vidēji** (OH5IY).

## Sakaru budžets

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. Pastiprinājumus ievada dBi un izmanto dBd (dBi − 2,15). Atskaitē dota arī rezerve ar **OH5IY vidējo trases vājinājumu** (200 dB pie 144 MHz, pārrēķināts ar λ³ uz izvēlēto joslu). Raksta atsauce: vajadzīgi ap **70 dBm EIRP** (−130 dBm + 200 dB, piem. ap 400 W uz 14 dBi).

## Antenas pastiprinājums un ziedlapiņa

**Pastiprinājums – avots:** Günter Hoch **DL6WU** līkne garām Yagi antenām atkarībā no traverses garuma L, ko citē W8IO (derīga no apmēram 2 λ) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Pārbaude pret L.B. Cebik W4RNL NEC modeļiem pie 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementi | Traverse (λ) | W4RNL NEC (dBi) | Formula (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Starpība nekad nepārsniedz **0,1 dB**: pastiprinājums vairāk atkarīgs no traverses garuma nekā no konstrukcijas (VK3AUU Yagi antenām tam pašam elementu skaitam ir īsāka traverse). VK5DJ Yagi Calculator dod novērtējumus arī VK3AUU, WA2PHW un DJ9BV variantiem, kuru formulas nav publicētas.

**Ziedlapiņa – avots:** Kraus likums ar apaļu ziedlapiņu θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Pārbaude:** W4RNL NEC modeļi DL6WU Yagi antenām dod **horizontālo ziedlapiņu par 5–10 % šaurāku** nekā Kraus: 33,8° / 26,4° / 22,6° 12, 19 un 26 elementiem pret 37,3° / 28,0° / 23,9°. Vienkāršās formulas neņem vērā priekšējās sānu ziedlapiņas (W4RNL, *Long-Boom Yagi Rules of Thumb*). Garām traversēm vertikālā ziedlapiņa ir nedaudz platāka par horizontālo (14 λ: 18,4° / 18,8°).

**Izvēle** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Piemērs: 14 λ Yagi pie 432 MHz → 20,3 dBi, ziedlapiņa 18,1° horizontāli un 19,5° vertikāli; W4RNL modeļi dod 20,4 dBi un 18,4° / 18,8°. Tie ir aptuveni likumi, kas iegūti no dažām DL6WU antenām.

Antena vienmēr tiek uzskatīta par vērstu uz DX. Hot spot ir **ziedlapiņā**, ja |Az(Hot) − Az(antena)| ≤ θ_horizontal/2: tad [debess velvē](Sky-View-lv) tas tiek zīmēts pelēks un parādās brīdinājums. Efektivitātes aprēķinā antenas ir izotropas; reālā ziedlapiņa tiek izmantota tikai šai pārbaudei.

## Eksperimentālie likumi starp joslām

Salīdzinājumā ar 144 MHz: skaits/intensitāte × (144/f)³ (dB), ilgums × (144/f)² (SM6FHZ, VUSHF 2025). IARU 1. reģiona maksimālais pinga ilgums: 1000 ms 50 MHz, 500 ms 70 MHz, 100 ms 144 MHz, 13 ms 432 MHz (VHF Handbook, citēts rakstā). Sk. arī [Eksperimentālas prognozes](Experimental-Forecasts-lv).
