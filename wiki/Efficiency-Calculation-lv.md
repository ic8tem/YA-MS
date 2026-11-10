[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · **Latviešu** · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Efektivitātes aprēķins

*Cilne: Prognozes aprēķins › Efektivitātes aprēķins.*

[![Efektivitātes aprēķins](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

Plūsmas **efektivitāte** procentos norāda, cik lielā mērā tās radianta stāvoklis ļauj atstarojumus **tavā** trasē. Jēdziena autors ir Ilkka **OH5IY** (MS-Soft), un to pārņem Cerrotta–Sartori raksts: efektivitātes maksimums nesakrīt ar vizuālo maksimumu (ZHR), jo tas atkarīgs no tā, kur radiants atrodas attiecībā pret abām stacijām. DL5MCG MCG_MS to pašu ideju piemēro četriem fiksētiem virzieniem; YA-MS to aprēķina **reālajai trasei** starp abiem lokatoriem.

Šī cilne to rāda pa stundām dienai, kas izvēlēta laukā *Diena 24 h tabulai (UTC)* (vērtības katras stundas vidū).

## Pārskata kartītes

| Kartīte | Saturs |
|---|---|
| **LABĀKAIS DIENAS LAIKS** | Stunda ar augstāko trases indeksu, indekss un dominējošā puse (A/B ar tās %) |
| **VISIZDEVĪGĀKĀ PLŪSMA** | Dienas plūsma ar lielāko ZHR × efektivitāte, tās efektivitāte, stunda un puse, un **labākais virziens** (radianta azimuts +90° / −90°) |
| **TAGAD** | Indekss un dominējošā puse šajā stundā un ieteicamais Hot (tikai tad, ja izvēlētā diena ir šodiena) |
| **EKSPERIMENTĀLA PROGNOZE** | Gaidāmie atstarojumi stundā tagad, pēc 1 h un pēc 2 h prognozes frekvencē (Collm, SM6FHZ likumi; sk. [Eksperimentālas prognozes](Experimental-Forecasts-lv)) |

Zem kartītēm josla paskaidro burtus A un B (sk. zemāk).

## Grafiks

*Efektivitāte pa stundām: …, … (UTC, vērtības stundas vidū).* Līdz piecām plūsmām: efektivitāte % kā nepārtraukta līnija un DH9GCD formula kā tās pašas krāsas punktota līnija; **trases indekss** kā zilas joslas pēc labās skalas.

## Stundu tabula

Viena rinda katrai tajā dienā aktīvajai plūsmai (sakārtotas pēc ZHR), 24 kolonnas stundām (UTC):

| Šūna | Nozīme |
|---|---|
| `63A` | efektivitāte 63 %, vairums atstarojumu no puses **A** |
| `41B` | efektivitāte 41 %, puse **B** |
| `3` | efektivitāte zem 5 %: skaitlis bez puses burta |
| tukša | efektivitāte zem 1 % |
| `…↑` | radiants tajā stundā ir **virs 70°**, skatoties no tavas stacijas (pārāk augstu) |
| dzeltens teksts | efektivitāte ≥ 50 % |

- **A** = **pa kreisi**, skatoties no tavas stacijas uz korespondentu (Hot A zona); **B** = **pa labi** (Hot B zona). Vērts pagriezt antenu **par 10–30° uz šo pusi** (side-scatter, Cerrotta–Sartori raksts).
- **Gaiši zilās rindas** (*DH9GCD %*, zem katras plūsmas): DH9GCD formula salīdzinājumam.
- **Σ rinda**: *Trases indekss (ZHR×efekt.)*.
- **Oranžā rinda** (*Prognoze … MHz (atstar./stundā)*): eksperimentālā prognoze tām stundām, kurām tā ir (šodien un daļa rītdienas).

## Modelis

Visi soļi ir [aprēķinu rokasgrāmatā](Efficiency-Explanation-lv) (`doc/YA-MS_manuale_calcoli.docx`, 5. nodaļa). Īsumā:

**1. Spoguļatstarošana.** Sliede pārraida signālu no A uz B tikai tad, ja tā pieskaras elipsoīdam ar A un B fokusos (McKinley 1961). Plūsmas sliedes ir paralēlas radianta virzienam ŝ (raksts; McKinley). Katram E slāņa punktam P ar vienības vektoriem uz stacijām:

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

Tas pats likums ir DJ5HG QTFGUI pamatā (konusa izkliede). Nosacījums tiek pieņemts ar Gausa pielaidi σ = 0,05 rad (ap 3°) – *programmas izvēle*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Katra punkta svars.** Zema blīvuma sliedes jauda (McKinley), φ = puse no izkliedes leņķa (ierobežota līdz 85°, *izvēle*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Meteoru skaits, kas sasniedz punktu, ir proporcionāls radianta elevācijas sinusam tajā (ŝ·û_P) – tā pati korekcija, ko IMO izmanto ZHR.

**3. Summa un procenti.** Punkti ik pēc 15 km sliežu augstumā, tikai tur, kur abas stacijas tos redz virs ziedlapiņas elevācijas (*izvēle*). 100 % ir šai trasei izdevīgākais radianta stāvoklis:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F katrai trasei tiek aprēķināts vienreiz virzienu režģī (azimuts ik pēc 5°, elevācija ik pēc 2,5°) un interpolēts.

**4. Puse un indekss.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

Burts tabulā ir puse ar lielāko daļu. *Programmas izvēles (rokasgrāmatas 32.–33. vien.).*

## DH9GCD salīdzinājums

Neatkarīga pārbaude: **DH9GCD** labākā virziena formula, ko citē **DF5HC** (DARC konference, 2018. gada janvāris), kur El un Az ir radianta elevācija un azimuts, skatoties no tavas stacijas, un P – korespondenta azimuts:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Tā ir maksimāla, ja radiants ir 45° augstumā un šķērsām trasei. DF5HC uzskata radiantu par pārāk zemu zem 20° un **pārāk augstu virs 70°**: šīs stundas tabulā saņem ↑ un [debess velvē](Sky-View-lv#brīdinājumi) brīdinājumu. Formula neņem vērā attālumu un augstumus, taču ir laba atsauce.

## Pārbaudes

| Pārbaude | Rezultāts |
|---|---|
| SM6FHZ likums (VUSHF 2025): labākā trase ortogonāla radianta azimutam, virziens = radianta az ±90°, pielaide ±40–50° | Modelis to atveido; ja radiants ir trases virzienā un augstu debesīs, efektivitāte ir gandrīz nulle |
| DJ5HG QTFGUI, Hamburga JO53IM – Barselona, Kvadrantīdas, 4. janvāris (piemērs no tā rokasgrāmatas) | QTFGUI: 07:00 virziens 252°, −8 dB; 08:00 nav atstarošanas zonas; 09:00 virziens 168°, −4 dB. YA-MS (augstums 102 km kā QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Visas trīs metodes redz 08:00 "caurumu", kad radiants ir gandrīz zenītā |
| Izlase ik pēc 5 km, nevis 15 km | procenti mainās mazāk nekā par 0,3 punktiem |

> OH5IY un MCG_MS izmantotā skala nav zināma sīkāk (MS-Soft rokasgrāmatas nav pieejamas): salīdzini procentus ar šīm programmām, pirms uzskati tos par līdzvērtīgiem. Modelis ņem vērā tikai zema blīvuma sliedes ar izotropām antenām; augsta blīvuma uzliesmojumi un sporādiskais fons efektivitātē nav iekļauti (sporādisko fonu attēlo radara meteoru skaits).
