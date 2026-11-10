[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Português (Brasil)](Sky-View-pt-br) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · **Latviešu** · [Polski](Sky-View-pl) · [Čeština](Sky-View-cs) · [Magyar](Sky-View-hu) · [Română](Sky-View-ro) · [Ελληνικά](Sky-View-el) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [ไทย](Sky-View-th) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh) · [中文 (繁體)](Sky-View-zh-tw)

# Debess velve

*Cilne: Prognozes aprēķins › Prognozes aprēķins.*

[![Debess velve](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Šī apakšcilne (agrāko versiju debess velve) vienā ekrānā parāda, **kur** tagad ir lietderīgās sliedes un **kurp** tēmēt. Kreisajā pusē ir trases **skats no augšas**; labajā – plūsmu saraksts, maza debess velve ar radiantiem, aprēķina teksts un **griezums**, kā to redz tava antena. Viss attiecas uz brīdi, kas izvēlēts ar *Aprēķina datums (UTC)* un slīdni *Stundas (no −12 līdz +36 h)* (noklusējumā reālais laiks, ar 15 minūšu soli).

**Josla virs skata no augšas** apkopo aprēķinu šim brīdim: datums un laiks (*tagad* vai stundas no šī brīža), **trases indekss Σ ZHR×η**, **noderīgākā plūsma** ar tās ZHR un efektivitāti (arī dB attiecībā pret DJ5HG atskaiti, sk. [Efektivitātes aprēķins](Efficiency-Calculation-lv)), plūsmu skaits virs horizonta un **ieteicamais Hot** ar tā azimutu.

Mazajā debess velvē **oranža līnija** caur zenītu vienmēr rāda **pareizos antenas virzienus**, ortogonālus izvēlētās (vai visizdevīgākās) plūsmas pārvietojumam: radianta azimuts ±90°, abos galos ar uzrakstu *antena NNN°*, un ±45° pielaide plānās līnijās. Īsas oranžas iedaļas uz malas rāda pārējo lietderīgo plūsmu ortogonālos virzienus.

## Skats no augšas (pa kreisi)

Eiropas karte, skatoties no augšas (**A pa labi**), ar grādu skalu apkārt. Paraksts zem kartes norāda tās rādiusu (*Karte: mala = … km no stacijas*).

| Elements | Zīmējums |
|---|---|
| Trase / DX | Zaļa līnija no tavas stacijas līdz korespondentam (vienmēr reālā lielā loka trase starp lokatoriem) |
| **Hot A / Hot B** | Punkti abpus viduspunktam, perpendikulāri trasei, attālumā pēc AMS nobīžu tabulas (vai ievadītā ar roku). **Sarkans = ieteicamais**, **rozā = ārpus antenas ziedlapiņas**, **pelēks = ziedlapiņā** (ar brīdinājumu) |
| Antenas ziedlapiņa | −3 dB horizontālā ziedlapiņa ap antenas azimutu (antena vienmēr vērsta uz DX), ar uzrakstu *ziedlapiņa …°* |
| Kopējās zonas robežas | Blāvi punkti *rob. A* / *rob. B* un divi apļi, kur katras stacijas horizonts satiekas ar E slāni (sk. [Ģeometrija](Geometry-and-Path-Loss-lv#kopējās-zonas-robežas)) |
| Plūsmas pārvietošanās | **Dzeltena līnija**: virziens, kurā izvēlētā (vai visizdevīgākā) plūsma pārvietojas pa debesīm, t.i., radianta azimuts |
| Labākie virzieni | **Oranži punkti**: abi virzieni, kas perpendikulāri pārvietojumam (radianta azimuts ±90°, SM6FHZ) |
| **PREV zonas** | Gaišas elipses: kur **tagad** krīt varbūtīgākās sliedes, viena katrā trases pusē |

Uzraksti nepārklājas: Hot A un PREV A ir rakstīti trases kreisajā pusē, B – labajā. **Leģenda** ir sakļaujama kolonna kartes labajā pusē.

**Pele uz kartes:** **kreisais klikšķis = korespondenta lokators**, **labais klikšķis = manas stacijas lokators**. Trase tiek uzreiz pārrēķināta.

Opcijas virs plūsmu saraksta: **Hot A / Hot B virzieni**, **Eiropas karte** (Natural Earth, pirmajā palaišanā lejupielādēta mapē `data/mappa`), **Skats no augšas (A pa labi)**.

### Ieteicamais Hot

Parādītajam laikam programma saskaita visām plūsmām virs horizonta svaru ZHR × efektivitāte, sadalītu starp pusi A (daļa f_A) un pusi B. Puse ar lielāko svaru nosaka ieteicamo Hot, ko zīmē sarkanā krāsā:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Programmas izvēle (rokasgrāmatas 23. vien.).* Idejas avots: DJ5HG, ko citē DF5HC (DARC konference 2018) – atkarībā no radianta stāvokļa viens no abiem punktiem, HOT-A vai HOT-B, ir izdevīgāks. Pagrieziens par 10–30° uz šo pusi (side-scatter) nāk no Cerrotta–Sartori raksta.

### PREV zonas

Katram E slāņa punktam P tiek saskaitīti visu aktīvo plūsmu devumi efektivitātē (tas pats spoguļatstarošanas nosacījums kā [efektivitātei](Efficiency-Calculation-lv#modelis)), svērti ar ZHR. Punkti ar vismaz 3 % no maksimuma veido PREV zonas; katra tiek zīmēta kā elipse ar centru = punktu svērtais vidējais un asīm = divkārša to izkliede.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Programmas izvēle (rokasgrāmatas 34. vien.).* Tas ir praktiskais likums: ja plūsma pārvietojas no ziemeļiem uz dienvidiem, lietderīgās sliedes krīt austrumos un rietumos.

## Plūsmu saraksts (augšā pa labi)

| Kolonna | Nozīme |
|---|---|
| Plūsma, Kods | Nosaukums un IMO kods |
| ZHR tagad | Aktivitāte šajā brīdī (IMO maksimālais ZHR ar aktivitātes profilu) |
| Azimuts, Elev. | Radianta stāvoklis, kā to redz tava stacija |
| Efekt. % | Plūsmas efektivitāte šai trasei |
| Puse | A vai B – puse, no kuras nāk vairums atstarojumu |
| Labākais virz. | Radianta azimuts ±90° |
| Lec, Riet | Radianta lēkts un riets (UTC); attiecīgā gadījumā *cirkumpolārs* vai *vienmēr zem* |

Klikšķis uz rindas izvēlas plūsmu: dzeltenā pārvietošanās līnija un oranžie punkti seko tai.

## Mazā debess velve (vidū pa labi)

Radianti uz debess velves, kā to redz tava stacija, ar to **IMO kodu** un **dienas ceļu ciānā krāsā** (UTC stundas). **Klikšķis uz radianta** to izvēlas. Krāsas:

| Krāsa | Nozīme |
|---|---|
| Dzeltena | efektivitāte ≥ 50 % un ZHR ≥ 2 |
| Oranža | efektivitāte ≥ 20 % |
| Tumši sarkana | efektivitāte < 20 % |
| Pelēka | gandrīz neaktīva |

Blakus ir aprēķina teksts: trases garums un azimuts, viduspunkts un tā elevācija, Hot A / Hot B azimuti un nobīdes, ieteicamais Hot (*… ieteicams tagad: az. …° (…% no gaidāmajiem atstarojumiem)*), kopējās zonas robežas un atgādinājums: *labākā tēmēšana plūsmai: PERPENDIKULĀRI pienākšanas virzienam (radianta azimuts ±90°, pielaide ±40–50°, SM6FHZ)*.

## Griezums (apakšā pa labi)

*GRIEZUMS – varbūtīgākās sliedes, kā tās redz antena, kas vērsta uz korespondentu.* Horizontāli – **azimuts attiecībā pret korespondentu** (← A pa kreisi, B → pa labi), vertikāli – **elevācija**. Katrai plūsmai tiek ņemti 14 spēcīgākie atstarošanas punkti; katra sliede ir nogrieznis, orientēts uz radiantu, no 10 km virs līdz 10 km zem sliežu augstuma (ne vairāk par 60 km katrā pusē), jo varbūtīgāka, jo biezāka. Zīmēta arī antenas ziedlapiņa (−3 dB aplis ap ziedlapiņas elevāciju), korespondents un Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Programmas izvēle (rokasgrāmatas 35. vien.).*

## Brīdinājumi

| Brīdinājums | Kad |
|---|---|
| **UZMANĪBU: Hot A (un/vai Hot B) ir antenas ziedlapiņā …** | Hot spot ir ±θ/2 robežās no antenas azimuta (θ = horizontālā −3 dB ziedlapiņa): ar šo virzienu tas jau ir pārklāts. Kartē tas ir pelēks. Ieteicamais Hot paliek sarkans. |
| **RADIANTS PĀRĀK AUGSTU (virs 70°)** | Kāds lietderīgs radiants ir virs 70°, skatoties no tavas stacijas: sliedes krīt gandrīz vertikāli un uz trasi atstaro maz (DF5HC, DH9GCD). Tās pašas stundas [stundu tabulā](Efficiency-Calculation-lv#stundu-tabula) ir atzīmētas ar ↑. |
| **ZEMS RADIANTS GAR TRASI** | Aktīvs radiants ir zem 20° un 30° robežās no trases virziena. Aprēķinātā efektivitāte paliek zema (piesardzīga), bet DJ5HG sagaida retus, spēcīgus atstarojumus no slīdošām sliedēm gar trasi (Hamburga–Narvika, kvadrantīdas, ap 19 UTC): vērts paklausīties. |
| **TRASE AIZ SLIEŽU HORIZONTA** | Sliežu augstumā trases viduspunkts ir zem abu staciju horizonta (ap 2120 km, ja sliedes ir 90 km augstumā). Brīdinājums norāda nepieciešamo minimālo sliežu augstumu (ap 96 km 2200 km trasei, 105 km 2300 km trasei): savienojums iespējams tikai ar augstākajām sliedēm, un efektivitātes un vājinājumi ir uz modeļa iespēju robežas. |
| *Nav kopējas E slāņa zonas* | Trase ir garāka par divkāršu sniedzamību sliežu augstumā: abas stacijas neredz kopīgu E slāņa daļu (viens lēciens nav iespējams). |
| *Nav ieteicamā Hot* | Šajā laikā gandrīz nav aktīvu plūsmu. |

Atsauce debess velves grafikai: DL1DBC Swan Meteor Skyview (swan.ms); polārais grafiks ar labāko virzienu: SM6FHZ RadiantCalc.
