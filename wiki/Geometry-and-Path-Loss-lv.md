[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · **Latviešu** · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

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

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Pārbaude:** tā sakrīt ar precīzo sfērisko ģeometriju 0,03° robežās. Programma izmanto divargumentu arktangensu, kas aiz horizonta dod negatīvas vērtības un novērš rakstā minēto periodiskuma problēmu. Negatīva elevācija uz viduspunktu nozīmē *trase ir ārpus viena lēciena ģeometriskās sniedzamības*.

## Horizonta sniedzamība

Attālums pa zemi, kurā stars ar elevāciju e sasniedz augstumu H (iepriekšējās formulas ģeometriskā inversija) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Pārbaude:** H = 89,5 km, e = 0° → **1062 km**. Raksta piemērā (JN44BB–IO53RT) zīmējumā horizonta krustpunkti ir ap 870 km no stacijām, kas atbilst ziedlapiņai, kas pacelta par apmēram 2° (865 km).

## Troposfēras refrakcija (GFS)

Troposfēras refrakcija (rūtiņa "Troposfēras refrakcija (GFS)", palaižot izslēgta). Ar ieslēgtu rūtiņu programma no Open-Meteo lejupielādē GFS modeļa profilu virs abām stacijām (spiedienu, temperatūru un mitrumu pie zemes un līmeņos no 1000 līdz 500 hPa, tuvākajai stundai 6 stundu robežās), līmeņu augstumus aprēķina ar hipsometrisko vienādojumu (virtuālā temperatūra), bet refraktivitāti – ar Ieteikuma ITU-R P.453 formulu:

```math
N = \frac{77{.}6}{T}\left(P + \frac{4810\,e}{T}\right)
```

kur P un e (tvaika spiediens, pēc Magnusa formulas) ir hPa, bet T – kelvinos. Virs augšējā līmeņa N samazinās eksponenciāli ar mēroga augstumu 7,35 km. Ja GFS neatbild, izmanto P.453 atsauces atmosfēru N = 315·exp(−h/7,35), un pārskats to norāda.

Staru izseko caur plāniem sfēriskiem slāņiem pēc Snella likuma sfēriskā formā (n·r·cos e konstants) līdz pēdu augstumam; no tā iegūst sniedzamību augstumā H un pacēluma leņķa labojumu:

```math
\Delta\varphi = \frac{k\,\Delta r}{r_m\,\bar u},\quad u = \sqrt{n^2r^2-k^2},\quad k = n_0 r_0\cos e
```

Piemērs ar atsauces atmosfēru un pēdām 89,5 km augstumā: pie 0° sniedzamība pieaug no 1061,5 līdz aptuveni 1133 km (+72 km), un punkts šķiet par 0,62° augstāk; pie 4° sniedzamība pieaug par 14 km, labojums ir 0,20°; virs 10° ietekme ir niecīga. Labojumu piemēro pacēluma leņķim uz viduspunktu, kopīgās zonas rādiusam, karstajiem punktiem un efektivitātes kartes punktiem; punktus zem lauztā horizonta atmet. Pārskats to sniedz rindā "Refrakcija".

Ekvivalentais Zemes rādiuss k = 4/3 attiecas uz stariem, kas paliek troposfēras pirmajos kilometros, kur N samazinās par aptuveni 40 vienībām uz km. Stars uz pēdu 90 km augstumā šķērso visu troposfēru un virs 10-15 km, kur N ir gandrīz nulle, turpinās gandrīz taisni: ar k = 4/3 visā kāpumā sniedzamība pie 0° būtu aptuveni 1230 km, gandrīz par 100 km vairāk nekā izsekotajam staram. Tāpēc programma izseko staru GFS profilā, kā to dara autora LIVETROPOVHF troposfēras izplatībai, nevis izmanto k = 4/3.

→ [Open-Meteo (GFS)](https://open-meteo.com/) · [ITU-R P.453](https://www.itu.int/rec/R-REC-P.453)

## Kopējās zonas robežas

**Avots:** raksts nosaka līkņu krustpunktus, kur katras stacijas horizonts satiekas ar E slāni: divu apļu ar leņķisko rādiusu ρ = d_H/r un centriem A un B krustpunkti [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Ja 1 − |p0|² < 0, trase ir garāka par 2·d_H, un stacijas neredz **nevienu kopēju E slāņa zonu**.

**Pārbaude:** tās ir abu staciju redzamo debesu **tālākās malas**, **nevis punkti, uz kuriem tēmēt**. Trasē JN70CN–IN78UO (1710 km, azimuts 308°) tās ir 1062 km no stacijas, 37° pa kreisi un pa labi no tiešās trases, kamēr MSHV iesaka 10°. Tāpēc tās sauc par *Robeža A* / *Robeža B* un kartē zīmē blāvi.

## Hot A un Hot B

**Avots:** sporādisko meteoru atstarojumi koncentrējas divās zonās ("hot spot") abpus viduspunktam. J. Richardson (AMS) tabulā, ko citē DJ5HG (*Die Geometrie von Meteorscatterverbindungen*, 2004), dod antenas nobīdi no tiešā virziena: **13° pie 1000 km, 11° pie 1250 km, 10° pie 1500 un 2000 km**. AMS Bulletin Nr. 203, ko pārņēmis W8WN, dod 10° pie 1500 un 1800 km.

**Izvēle:** Hot A un Hot B ir punkti attālumā s no viduspunkta M, perpendikulāri trasei. Ja atzīmēts *auto (AMS)* (noklusējums), s iegūst no Richardson tabulas nobīdes, lineāri interpolējot (13° zem 1000 km, 10° virs 2000 km): s = (D/2)·tan(nobīde). Ja nav atzīmēts, s ievada ar roku, 30–400 km (MSHV izmanto 150 km); A pa kreisi, skatoties no tavas stacijas uz DX, B pa labi [21]. Nobīde, kā to redz stacija, ir aptuveni [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Pārbaude:** ar AMS tabulu 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, tāpat kā iepriekš un MSHV izmantotie 150 km; īsās trasēs tabula pietuvina hot spot viduspunktam.

## Zema blīvuma trases vājinājums

**Avots:** McKinley vienādojums un ITU-R ieteikums P.843 zema blīvuma sliedēm (sin α = 1), bez antenu pastiprinājuma; q = elektronu lineārais blīvums, r_e = klasiskais elektrona rādiuss = 2,818·10⁻¹⁵ m, R1, R2 – attālumi no sliedes, φ – puse no izkliedes leņķa, β – leņķis starp sliedi un trases plakni, a₁ – sākotnējā rādiusa koeficients, r₀ metros un h kilometros (P.843, 4. un 7. vien.) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Izvēle:** sakaru budžetā un vājinājumu tabulā izmanto β = 90° (sliede šķērso trases plakni, nelabvēlīgākais gadījums: piesardzīga vērtība), un budžetā parāda arī labāko gadījumu, β = 0. r₀ ņem frekvences vidējā atbalss augstumā, h = 124 − 17 log f (P.843, 15. vien.): 0,76 m pie 95 km 50 MHz frekvencei, 0,40 m pie 87 km 144 MHz, 0,21 m pie 79 km 432 MHz. 1000 km trasē a₁ ir 0,2 dB pie 50 MHz, 0,6 dB pie 144 MHz un 1,4 dB pie 432 MHz (2,9 dB pie 600 km); pie DJ5HG fiksētajiem 102 km tas būtu ap 70 dB pie 432 MHz, t. i., nekādas atbalss.

**Pārbaude:** ar q = 10¹⁴ elektroni/m, sliedēm 89,5 km augstumā un β = 0, pie 144 MHz: **182–192 dB** starp 600 un 2100 km (185 dB pie 1000 km), **172–190 dB** diapazonā, ko savā doktora disertācijā aprēķinājis John Worsnop **G4BAO**, kā norāda GM8JBJ. Ar β = 90° vājinājums pieaug par 10 dB pie 600 km, 13 dB pie 1000 km un 16 dB pie 2100 km; OH5IY **200 dB vidēji** atrodas starp abiem gadījumiem. 182 dB GM8JBJ tabulā nav apstiprinājums: tabulā nav norādīta frekvence, tās 86,4 dB katram posmam ir brīvās telpas vājinājums 500 km attālumā pie 1 MHz (trūkst locekļa 20 log f: 129,6 dB pie 144 MHz), un tās pozīciju summa ir 163,8 dB, nevis 182; lapā nav rakstīts ne “minimums”, ne “144 MHz”.

## Sakaru budžets

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Pastiprinājumus ievada un izmanto dBi: McKinley vājinājums attiecas uz izotropām antenām, tāpēc 2,15 dB dipola korekcija netiek atņemta (EIRP = jauda + pastiprinājums). Atskaitē dota arī rezerve ar **OH5IY vidējo trases vājinājumu** (200 dB pie 144 MHz, pārrēķināts ar λ³ uz izvēlēto joslu). Raksta atsauce: vajadzīgi ap **70 dBm EIRP** (−130 dBm + 200 dB, piem. ap 400 W uz 14 dBi).

## Antenas pastiprinājums un ziedlapiņa

**VE7BQH** – Yagi pastiprinājums atkarībā no traverses garuma L: VE7BQH tabulu vidējā taisne katrai joslai (ap 60 Yagi antenu joslā, NEC pastiprinājumi). Iekavās izlases diapazons un standartnovirze:

```math
\begin{aligned}50\,\mathrm{MHz}:\ & G = 7{.}36\,\log_{10}(L/\lambda) + 11{.}67\ \mathrm{dBi} \\ 144\,\mathrm{MHz}:\ & G = 8{.}27\,\log_{10}(L/\lambda) + 11{.}31\ \mathrm{dBi} \\ 432\,\mathrm{MHz}:\ & G = 8{.}68\,\log_{10}(L/\lambda) + 11{.}03\ \mathrm{dBi}\end{aligned}
```

(50 MHz: 0,3–5 λ, 0,25 dB · 144 MHz: 0,75–8,9 λ, 0,15 dB · 432 MHz: 1,8–16 λ, 0,17 dB)

Izmanto tuvākās joslas taisni: zem 100 MHz – 50 MHz, no 100 līdz 300 MHz – 144 MHz, virs 300 MHz – 432 MHz (1296 MHz tā ir ekstrapolācija). Ārpus izlases diapazona galvenais logs brīdina, ka novērtējums ir neprecīzs.

DL6WU vēsturiskā līkne (VHF Communications 3/1982, 1. att.): 1981. gada mērījumi pie 432 un 1296 MHz, 2,35 dB uz traverses oktāvu, norādītā precizitāte 0,5 dB; G ≈ 9,2 + 7,81 log10(L/λ) dBd. W8IO to dod kā 7,773 log10(L/λ) + 11,43 dBi (atšķirība mazāka par 0,1 dB). Programma to salīdzinājumam ieraksta atskaitē:

```math
G = 7{.}81\,\log_{10}(L/\lambda) + 11{.}35\ \mathrm{dBi}
```

**Pārbaude pret L.B. Cebik W4RNL NEC modeļiem pie 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementi | Traverse (λ) | W4RNL NEC (dBi) | Formula (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Starpība nekad nepārsniedz **0,1 dB**: pastiprinājums vairāk atkarīgs no traverses garuma nekā no konstrukcijas (VK3AUU Yagi antenām tam pašam elementu skaitam ir īsāka traverse). VK5DJ Yagi Calculator dod novērtējumus arī VK3AUU, WA2PHW un DJ9BV variantiem, kuru formulas nav publicētas.

VE7BQH vidējais mīnus DL6WU līkne: pie 50 MHz 0,25 dB robežās no 2 līdz 16 λ; pie 144 MHz no −0,04 dB (1 λ) līdz +0,42 dB (10 λ); pie 432 MHz no −0,06 dB (2 λ) līdz +0,55 dB (10 λ). W4RNL pie 432 MHz modelētajām DL6WU un VK3AUU antenām VE7BQH vidējais ir 0,15–0,55 dB virs NEC: uz gariem traversēm tabulu datorā optimizētās antenas dod vairāk nekā sākotnējās konstrukcijas.

**Ziedlapiņa – avots:** Kraus likums ar apaļu ziedlapiņu θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Pārbaude:** W4RNL NEC modeļi DL6WU Yagi antenām dod **horizontālo ziedlapiņu par 5–10 % šaurāku** nekā Kraus: 33,8° / 26,4° / 22,6° 12, 19 un 26 elementiem pret 37,3° / 28,0° / 23,9°. Vienkāršās formulas neņem vērā priekšējās sānu ziedlapiņas (W4RNL, *Long-Boom Yagi Rules of Thumb*). Garām traversēm vertikālā ziedlapiņa ir nedaudz platāka par horizontālo (14 λ: 18,4° / 18,8°).

**Izvēle** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Piemērs: 14 λ Yagi pie 432 MHz → 20,3 dBi, ziedlapiņa 18,1° horizontāli un 19,5° vertikāli; W4RNL modeļi dod 20,4 dBi un 18,4° / 18,8°. Tie ir aptuveni likumi, kas iegūti no dažām DL6WU antenām.

Ar VE7BQH vidējo tā pati 14 λ Yagi dod 21,0 dBi un ziedlapiņu 16,9° horizontāli un 18,1° vertikāli; augstāk minētie 20,3 dBi ir no DL6WU līknes. Ziedlapiņas korekcijas (0,93 · θK un θK) paliek tās, kas iegūtas no DL6WU antenām.

Antena vienmēr tiek uzskatīta par pavērstu uz DX. Hot spot ir **daivas iekšpusē**, ja |Az(Hot) − Az(antena)| ≤ θ_horizontal/2: tad to zīmē pelēku [debess velvē](Sky-View-lv) un parādās brīdinājums. Vertikālā daiva iekļaujas arī efektivitātes aprēķinā: ja rūtiņa *antenas diagramma* ir ieslēgta, atstarošanas punktus sver ar abu antenu vertikālo pastiprinājumu (platums θ_vertical, maksimums daivas elevācijā, zemes koeficients līdz nullei pie horizonta).

## Eksperimentālie likumi starp joslām

Salīdzinājumā ar 144 MHz: skaits/intensitāte × (144/f)³ (dB), ilgums × (144/f)² (SM6FHZ, VUSHF 2025). IARU 1. reģiona maksimālais pinga ilgums: 1000 ms 50 MHz, 500 ms 70 MHz, 100 ms 144 MHz, 13 ms 432 MHz (VHF Handbook, citēts rakstā). Sk. arī [Eksperimentālas prognozes](Experimental-Forecasts-lv).
