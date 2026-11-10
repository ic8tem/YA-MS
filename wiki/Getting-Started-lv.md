[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · **Latviešu** · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [ไทย](Getting-Started-th) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Darba sākšana

Pirmajā palaišanā YA-MS rāda trases piemēru (JN70CN → JO62QM 144 MHz joslā). Ar piecām minūtēm pietiek, lai to iestatītu savai stacijai.

## 1. Trīs vadības rindas

Virs cilnēm ir trīs vadības rindas, kas attiecas uz visām cilnēm. Poga **Vadība** augšā pa labi tās sakļauj un izvērš (noderīgi ar lieliem fontiem); izvēle tiek atcerēta.

**1. rinda – stacijas un josla**

| Vadīkla | Ko tā dara |
|---|---|
| **Mans lokators** / **augstums m** | Tavs Maidenhead lokators (4, 6 vai 8 rakstzīmes; tiek izmantots kvadrāta centrs) un stacijas augstums virs jūras līmeņa. |
| **Korespondents** / **augstums m** | Tās stacijas lokators un augstums, ar kuru vēlies strādāt. |
| **Josla MHz** | 28, 50, 70, 144, 222 vai 432 MHz: izmanto antenas pastiprinājumam un ziedlapiņai, meteoru skaita novērtējumam un sakaru budžetam. |
| **Aprēķināt** | Aprēķina trasi no jauna (E slāņa izlase: dažas sekundes). |
| **Antenas az** | Tavas antenas azimuts: vienmēr **uz DX** (trases azimuts). |
| **Fonts** | Visa teksta izmērs, 100–300 %. Sk. [Iestatījumi](Settings-and-Data-Folder-lv#fonts-un-vadība). |

**2. rinda – E slānis un antena**

| Vadīkla | Ko tā dara |
|---|---|
| **Sliežu augstums km** + **no radara** | Meteoru sliežu augstums (noklusējumā 90 km). Ja atzīmēts *no radara*, tiek izmantots biežākais augstums (moda), ko izmērījis Collm radars; sk. [Radara meteoru skaits](Radar-Flux-lv). |
| **Ziedlapiņas elevācija °** | Tavas antenas ziedlapiņas zemākā elevācija (0° = horizonts). Tiek izmantoti tikai tie E slāņa punkti, ko abas stacijas redz virs šīs elevācijas. |
| **Yagi antena: traverse m** | Tavas Yagi antenas traverses garums. Programma rāda garumu λ, pastiprinājumu (DL6WU līkne) un −3 dB ziedlapiņu horizontāli un vertikāli; sk. [Ģeometrija un vājinājums](Geometry-and-Path-Loss-lv#antenas-pastiprinājums-un-ziedlapiņa). Zem 2 λ novērtējums ir neprecīzs. |
| **Hot spot no viduspunkta km** | Hot A un Hot B attālums no viduspunkta, 30–400 km (noklusējumā 150 km, kā AMS Bulletin 203 / W8WN / MSHV). |

**3. rinda – laiks**

| Vadīkla | Ko tā dara |
|---|---|
| **Laiks** | UTC pulkstenis. |
| **Debess velves laiks (±36 h)** | Pārvieto [debess velvi](Sky-View-lv) un cilni [GRAVES radars](GRAVES-Radar-lv) līdz 36 stundām atpakaļ vai uz priekšu ar 15 minūšu soli. |
| **Reālais laiks** | Atpakaļ uz tagadni. |
| **Diena 24 h tabulai (UTC)** | Diena, kas tiek rādīta cilnē [Efektivitātes aprēķins](Efficiency-Calculation-lv) un GRAVES hronoloģijā. |

## 2. Tava stacija un DX

1. Ieraksti **Mans lokators** un **augstums m**.
2. Ieraksti **korespondenta** lokatoru un augstumu – vai klikšķini uz kartes [debess velvē](Sky-View-lv): **kreisais klikšķis = korespondenta lokators**, **labais klikšķis = manas stacijas lokators**.
3. Izvēlies **Josla MHz** un nospied **Aprēķināt**.

Statusa josla apakšā apstiprina: *Trase aprēķināta: … km, … atstarošanas punktu izlase … s laikā*.

## 3. Tava antena

Ievadi savas Yagi antenas **traverses garumu**. Programma no tā iegūst pastiprinājumu un ziedlapiņu un brīdina, ja Hot A vai Hot B jau ir **ziedlapiņas iekšpusē**, kad antena vērsta uz DX (tad tie ir zīmēti pelēkā krāsā: antena nav jāgroza).

## 4. Rezultātu lasīšana

| Jautājums | Kur skatīties |
|---|---|
| Kura plūsma tagad palīdz manai trasei un no kuras puses? | [Debess velve](Sky-View-lv): plūsmu saraksts, ieteicamais Hot sarkanā krāsā, PREV zonas |
| Kura ir labākā stunda šodien? | [Efektivitātes aprēķins](Efficiency-Calculation-lv): pārskata kartītes un stundu tabula |
| Cik meteorus skaita radars? | [Radara meteoru skaits](Radar-Flux-lv) |
| Cik pingu var gaidīt 144 MHz? | [Eksperimentālas prognozes](Experimental-Forecasts-lv) (eksperimentāli) |
| Vai mana stacija var noslēgt trasi? | [Ģeometrija un vājinājums](Geometry-and-Path-Loss-lv): trases vājinājums un rezerve |
| Kad ir nākamais maksimums? | [Plūsmas](Showers-lv) |
| Vai varu izmēģināt ar GRAVES? | [GRAVES radars](GRAVES-Radar-lv) |

## Praktiski likumi (no avotiem)

- **Tēmē perpendikulāri plūsmai**: labākā trase ir ortogonāla radianta azimutam; labākais virziens = radianta azimuts ±90°, pielaide ±40–50° (SM6FHZ).
- **Side-scatter**: pagriez antenu par 10–30° uz to pusi (A vai B), no kuras nāk vairums atstarojumu (Cerrotta–Sartori raksts).
- **Pārāk augsts radiants** (virs 70°) vai pārāk zems (zem 20°) dod maz lietderīgu sliežu (DF5HC, DH9GCD).
- Sporādisko meteoru maksimums ir ap **06 UTC** (raksts; to apstiprina Collm meteoru skaits).
- Lietderīgie attālumi 432 MHz: 800–2000 km, labākais ap 1400 km (SM6FHZ); labākais attālums kopumā 1300–1500 km (DF5HC).

Tālāk: [Debess velve](Sky-View-lv).
