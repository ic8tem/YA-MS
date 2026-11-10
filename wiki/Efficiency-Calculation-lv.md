[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · **Latviešu** · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh)

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

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Tas pats likums ir DJ5HG QTFGUI un viņa teksta *"Die Geometrie von Meteorscatterverbindungen"* (2004) pamatā: sliede izkliedē uz konusa, kura ass ir pati sliede, un to dzird tikai uztvērējs, kas atrodas uz konusa. Ideālai sliedei konusa siena ir ļoti plāna (izstarotājs tūkstošiem viļņa garumu garumā); programma pieņem nosacījumu ar Gausa pielaidi σ = 0,05 rad (ap 3°), kas aizstāj to, ko ideālais konuss neredz: plūsmu radiantu izkliedi (0,3–1,4° pēc GMN mērījumiem), vēja saliektas sliedes un to galīgo garumu – *programmas izvēle*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Katra punkta svars.** Zema blīvuma sliedes jauda (McKinley), φ = puse no izkliedes leņķa (ierobežota līdz 85°, *izvēle*):

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad w_P = \frac{1}{R_1 R_2 (R_1+R_2)\cos^2\varphi}
```

Meteoru skaits, kas sasniedz punktu, ir proporcionāls radianta elevācijas sinusam tajā (ŝ·û_P) – tā pati korekcija, ko IMO izmanto ZHR.

**Opcija “Garākas sliedes ar zemu radiantu (DJ5HG)”** (izvēles rūtiņa virs diagrammas, noklusējumā izslēgta, ar rīka padomu): DJ5HG norāda, ka ar zemu radiantu uz km² nokrīt mazāk meteoru, bet sliedes ir garākas (līdz 100 km lietderīgā garuma) un biežāk izpilda atstarošanās likumu. Ar ieslēgtu opciju svars kļūst min(sin El, 15/100): lietderīgais slāņa biezums, 15 km, dalīts ar elevācijas sinusu, dod sliedes garumu, ierobežotu līdz 100 km. Virs aptuveni 9° abi efekti viens otru kompensē. Izslēgtai opcijai aprēķins paliek piesardzīgs.

**3. Summa un procenti.** Punkti ik pēc 15 km sliežu augstumā, tikai tur, kur abas stacijas tos redz virs ziedlapiņas elevācijas (*izvēle*). 100 % ir šai trasei izdevīgākais radianta stāvoklis:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F katrai trasei tiek aprēķināts vienreiz virzienu režģī (azimuts ik pēc 5°, elevācija ik pēc 2,5°) un interpolēts.

**Efektivitāte dB (DJ5HG atskaite).** Procenti ir relatīvi tikai pret labāko radianta stāvokli šai trasei. Lai salīdzinātu dažādas trases, programma dod arī efektivitāti dB attiecībā pret fiksēto DJ5HG atskaiti: 0 dB ir maksimums 1000 km garai ziemeļu–dienvidu trasei pāri ekvatoram, ar radiantu uz debess ekvatora ekvinokcijā, aprēķināts ar to pašu augstumu un tiem pašiem svariem. DJ5HG norāda savas vērtības kā precīzākas par 6 dB.

**4. Puse un indekss.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Burts tabulā ir puse ar lielāko daļu. *Programmas izvēles (rokasgrāmatas 32.–33. vien.).*

## DH9GCD salīdzinājums

Labākā virziena primārie avoti ir Eshleman & Mlodnosky un Meeks & James (Proc. IRE, 1957), Hines (1955) un tā eksperimentālā pārbaude, ko veica Forsyth, Hines & Vogan (1955): noderīgi ir tikai radianti uz debess pusloka, kas ir perpendikulārs izkliedes leņķa bisektrisei, sliežu skaits pieaug ar sin El, un tuvu viduspunktam noderīgās sliedes krīt apmēram H·tan El sāņus, radiantam pretējā pusē. DJ5HG izdara atrunu: ar **zemu** radiantu tieši gar trasi McKinley formula dod spēcīgus signālus (Hamburga–Narvika, kvadrantīdas, ap 19 UTC), tāpēc “radiants gar trasi = gandrīz nulle” attiecas tikai uz augstu radiantu; programma paliek piesardzīga un rāda brīdinājumu *ZEMS RADIANTS GAR TRASI*.

Neatkarīga pārbaude: **DH9GCD** labākā virziena formula, ko citē **DF5HC** (DARC konference, 2018. gada janvāris) – tai nav publicēta primārā avota –, kur El un Az ir radianta elevācija un azimuts, skatoties no tavas stacijas, un P – korespondenta azimuts:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Tā ir maksimāla, ja radiants ir 45° augstumā un šķērsām trasei. DF5HC uzskata radiantu par pārāk zemu zem 20° un **pārāk augstu virs 70°**: šīs stundas tabulā saņem ↑ un [debess velvē](Sky-View-lv#brīdinājumi) brīdinājumu. Formula neņem vērā attālumu un augstumus, taču ir laba atsauce.

## Pārbaudes

| Pārbaude | Rezultāts |
|---|---|
| SM6FHZ likums (VUSHF 2025): labākā trase ortogonāla radianta azimutam, virziens = radianta az ±90°, pielaide ±40–50° | Modelis to atveido; ja radiants ir trases virzienā un augstu debesīs, efektivitāte ir gandrīz nulle |
| DJ5HG QTFGUI, Hamburga JO53IM – Barselona, Kvadrantīdas, 4. janvāris (piemērs no tā rokasgrāmatas) | QTFGUI: 07:00 virziens 252°, −8 dB; 08:00 nav atstarošanas zonas; 09:00 virziens 168°, −4 dB. YA-MS (augstums 102 km kā QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Visas trīs metodes redz 08:00 "caurumu", kad radiants ir gandrīz zenītā |
| DJ5HG līknes (*Die Geometrie…*, Bild 8–9: no Hamburgas un Minhenes, kvadrantīdas, 4. janvāris; nolasītas no grafika, ap ±0,5 dB un ±15 min) salīdzinājumā ar automātisko testu `--prova-dj5hg` (viena vērtība stundā) | Laiki: robs, kad radiants ir tuvu zenītam, iekrīt tajās pašās stundās (Barselona 07:30–08:30 pret 07–09; Sofija 06:36–07:48 pret 07–08; Narvika 07–08:30 pret 07–09); Maskava abos ir slēgta 03–10, atvērta no Hamburgas līdz aptuveni 02:30 un no Minhenes līdz aptuveni 00:30, kā raksta DJ5HG. Virzieni: 2–10° starpība. Līmeņi: ar augstumu 102 km un ieslēgtu garāko sliežu opciju gandrīz visas vērtības ir 2–3 dB robežās no līknēm; ar izslēgtu opciju 3–7 dB zemāk, bet pēcpusdienas minimumi ir tuvāk (Maskava −9 dB plkst. 15, −11,5 dB plkst. 18 pret −9 un −12,5). Galvenā atšķirība: DJ5HG rāda dziļu minimumu, kad radiants ir viszemāk un gandrīz gar trasi (Barselona −16 dB plkst. 19:36, Sofija −14 dB plkst. 20); YA-MS to gandrīz nerāda (−8,6 un −10,4 dB ar izslēgtu opciju, −1 un −3 dB ar ieslēgtu). Tā ir paša DJ5HG atruna par zemu radiantu gar trasi: tāpēc ir brīdinājums, un opcija noklusējumā ir izslēgta |
| Izlase ik pēc 5 km, nevis 15 km | procenti mainās mazāk nekā par 0,3 punktiem |

> MS-Soft 5.2 dokumentācija definē OH5IY efektivitāti kā relatīvu indeksu tikai zema blīvuma sliedēm, ar diviem faktoriem (radianta elevācija, labākā ap 45°, un leņķis ar trasi, labākais 90°) un minimumu, kas augsta blīvuma sliedēm ar roku pacelts līdz 20 %; formula nav publicēta. MCG_MS to aprēķina četriem fiksētiem virzieniem un, ja dots DX lokators, reālajai trasei. Modelis ņem vērā tikai zema blīvuma sliedes ar izotropām antenām; augsta blīvuma uzliesmojumi un sporādiskais fons efektivitātē nav iekļauti (sporādisko fonu attēlo radara meteoru skaits).
