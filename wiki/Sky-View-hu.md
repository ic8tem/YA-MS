[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Português (Brasil)](Sky-View-pt-BR) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Polski](Sky-View-pl) · [Čeština](Sky-View-cs) · **Magyar** · [Română](Sky-View-ro) · [Ελληνικά](Sky-View-el) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [ไทย](Sky-View-th) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh) · [中文 (繁體)](Sky-View-zh-TW)

# Égbolt-kupola

*Fül: Előrejelzés-számítás › Előrejelzés-számítás.*

[![Égbolt-kupola](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Ez az alfül (a korábbi változatok égbolt-kupolája) egyetlen képernyőn mutatja meg, **hol** vannak most a hasznos nyomok, és **merre** kell fordítani az antennát. Bal oldalon az útvonal **felülnézete**; jobb oldalon a rajlista, egy kis égbolt-kupola a radiánsokkal, a számítás szövege és az antennából látott **metszet**. Minden a *Számítás dátuma (UTC)* mezővel és az *Órák (−12 és +36 h között)* csúszkával kiválasztott pillanatra vonatkozik (alapértelmezés a valós idő, 15 perces lépések).

A **felülnézet feletti sáv** összefoglalja az adott pillanat számítását: dátum és idő (*most* vagy órák a jelenhez képest), az **útvonalindex Σ ZHR×η**, a **leghasznosabb raj** a ZHR-jével és hatékonyságával (dB-ben is, a DJ5HG-referenciához viszonyítva, lásd: [Hatékonyság-számítás](Efficiency-Calculation-hu)), a horizont feletti rajok száma és az **ajánlott Hot** az azimutjával.

A kis égbolt-kupolán egy, a zeniten átmenő **narancs vonal** mindig a **helyes antennairányokat** mutatja, merőlegesen a kiválasztott (vagy a legkedvezőbb) raj vándorlására: radiáns azimutja ±90°, mindkét végén *antenna NNN°* felirattal, a ±45°-os tűréssel vékony vonalakként. A peremen rövid narancs jelek mutatják a többi hasznos raj merőleges irányait.

## Felülnézet (bal oldalon)

Európa felülről nézett térképe (**K jobbra**), körülötte fokbeosztással. A térkép alatti felirat megadja a sugarát (*Térkép: perem = … km az állomástól*).

| Elem | Ábrázolás |
|---|---|
| Útvonal / DX | Zöld vonal az Ön állomásától a DX-állomásig (mindig a lokátorok közötti valós főkörív menti útvonal) |
| **Hot A / Hot B** | A felezőpont két oldalán, az útvonalra merőlegesen elhelyezkedő pontok, az AMS-eltérítési táblázat szerinti (vagy kézzel megadott) távolságban. **Piros = ajánlott**, **rózsaszín = az antennanyalábon kívül**, **szürke = a nyalábon belül** (figyelmeztetéssel) |
| Antennanyaláb | A −3 dB-es vízszintes nyaláb az antenna azimutja körül (az antenna mindig a DX felé néz), *nyaláb …°* felirattal |
| A közös zóna határai | Halvány *hat. A* / *hat. B* pontok és a két kör, ahol az egyes állomások horizontja eléri az E-réteget (lásd: [Geometria](Geometry-and-Path-Loss-hu#a-közös-zóna-határai)) |
| A raj vándorlása | **Sárga vonal**: az az irány, amerre a kiválasztott (vagy a legkedvezőbb) raj végigsöpör az égbolton, azaz a radiáns azimutja |
| Legjobb irányok | **Narancs pontok**: a vándorlásra merőleges két irány (radiáns azimutja ±90°, SM6FHZ) |
| **PREV zónák** | Világos ellipszisek: ahová a legvalószínűbb nyomok **most** esnek, az útvonal mindkét oldalán egy-egy |

A feliratok nem fedik egymást: Hot A és PREV A az útvonal bal oldalára, B a jobb oldalára kerül. A **Jelmagyarázat** egy összecsukható oszlop a térkép jobb oldalán.

**Egér a térképen:** **bal kattintás = DX-állomás lokátora**, **jobb kattintás = saját állomás lokátora**. Az útvonal azonnal újraszámolódik.

Beállítások a rajlista felett: **Hot A / Hot B irányok**, **Európa-térkép** (Natural Earth, első indításkor töltődik le a `data/mappa` mappába), **Felülnézet (K jobbra)**.

### Ajánlott Hot

A megjelenített időpontra a program összeadja a horizont feletti összes rajra a ZHR × hatékonyság súlyt, felosztva az A oldal (f_A arány) és a B oldal között. A nagyobb súlyú oldal adja az ajánlott Hot pontot, pirossal rajzolva:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*A program döntése (kézikönyv, 23. egyenlet).* Az ötlet forrása: DJ5HG, DF5HC közlése nyomán (DARC-konferencia, 2018) – a radiáns helyzetétől függően a két pont, a HOT-A vagy a HOT-B közül az egyik kedvezőbb. Az, hogy az antennát 10–30°-kal e felé az oldal felé kell fordítani (oldalszórás), a Cerrotta–Sartori-cikkből származik.

### PREV zónák

Az E-réteg minden P pontjára összeadja az összes aktív raj hatékonysághoz való hozzájárulását (ugyanazzal a tükrös feltétellel, mint a [hatékonyságnál](Efficiency-Calculation-hu#a-modell)), ZHR-rel súlyozva. A maximum legalább 3 %-át elérő pontok alkotják a PREV zónákat; mindegyiket ellipszisként rajzolja, középpontja a pontok súlyozott átlaga, tengelyei szórásuk kétszerese.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*A program döntése (kézikönyv, 34. egyenlet).* Ez a gyakorlati szabály: ha a raj északról délre söpör, a hasznos nyomok keletre és nyugatra esnek.

## Rajlista (jobbra fent)

| Oszlop | Jelentés |
|---|---|
| Raj, Kód | Név és IMO-kód |
| ZHR most | Aktivitás ebben a pillanatban (IMO-csúcs ZHR az aktivitási profillal) |
| Azimut, Elev. | A radiáns helyzete az Ön állomásáról nézve |
| Hatékonyság % | A raj hatékonysága erre az útvonalra |
| Oldal | A vagy B, az az oldal, ahonnan a legtöbb reflexió érkezik |
| Legjobb irány | Radiáns azimutja ±90° |
| Kelte, Nyugta | A radiáns kelte és nyugta (UTC); ha érvényes: *cirkumpoláris* vagy *mindig a horizont alatt* |

Kattintson egy sorra a raj kiválasztásához: a sárga vándorlási vonal és a narancs pontok követik.

## Kis égbolt-kupola (jobbra középen)

A radiánsok az Ön állomásáról látott égbolt-kupolán, **IMO-kódjukkal** és **napi pályájukkal ciánkékben** (UTC-órák). **Kattintson egy radiánsra** a kiválasztásához. Színek:

| Szín | Jelentés |
|---|---|
| Sárga | hatékonyság ≥ 50 % és ZHR ≥ 2 |
| Narancs | hatékonyság ≥ 20 % |
| Sötétvörös | hatékonyság < 20 % |
| Szürke | szinte inaktív |

Mellette a számítás szövege: az útvonal hossza és azimutja, a felezőpont és elevációja, Hot A / Hot B azimutja és eltolása, az ajánlott Hot (*… most ajánlott: az. …° (a várható reflexiók …%-a)*), a közös zóna határai, és az emlékeztető: *legjobb irány a rajhoz: MERŐLEGES a beérkezési irányra (radiáns azimutja ±90°, tűrés ±40–50°, SM6FHZ)*.

## Metszet (jobbra lent)

*METSZET – a legvalószínűbb nyomok az antennából nézve a DX-állomás felé.* Vízszintesen az **azimut a DX-állomáshoz képest** (← A balra, B → jobbra), függőlegesen az **eleváció**. Minden rajhoz a 14 legerősebb reflexiós pontot veszi; minden nyom egy, a radiáns felé irányuló szakasz a nyommagasság felett 10 km-től alatta 10 km-ig (oldalanként legfeljebb 60 km), annál vastagabb, minél valószínűbb. Szintén megjelenik: az antennanyaláb (−3 dB-es kör a nyalábeleváció körül), a DX-állomás és Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*A program döntése (kézikönyv, 35. egyenlet).*

## Figyelmeztetések

| Figyelmeztetés | Mikor |
|---|---|
| **FIGYELEM: Hot A (és/vagy Hot B) az antennanyalábon belül esik …** | A hot spot az antenna azimutjától ±θ/2-n belül van (θ = vízszintes −3 dB-es nyaláb): ezzel az iránnyal már le van fedve. A térképen szürkén jelenik meg. Az ajánlott Hot piros marad. |
| **TÚL MAGAS RADIÁNS (70° felett)** | Egy hasznos radiáns az Ön állomásáról nézve 70° felett van: a nyomok szinte függőlegesen esnek, és keveset vernek vissza az útvonal felé (DF5HC, DH9GCD). Ugyanezek az órák ↑ jellel szerepelnek az [óránkénti táblázatban](Efficiency-Calculation-hu#óránkénti-táblázat). |
| **ALACSONY RADIÁNS AZ ÚTVONAL MENTÉN** | Egy aktív radiáns 20° alatt van, és az útvonal irányától 30°-on belül. A számított hatékonyság alacsony marad (óvatos becslés), de DJ5HG ritka, erős reflexiókra számít az útvonallal egy irányba eső, súroló nyomokból (Hamburg–Narvik, Quadrantidák, kb. 19 UTC): érdemes hallgatni. |
| **AZ ÚTVONAL A NYOMHORIZONTON TÚL VAN** | A nyommagasságban az útvonal felezőpontja mindkét állomás horizontja alatt van (kb. 2120 km 90 km-es nyomoknál). A figyelmeztetés megadja a szükséges minimális nyommagasságot (kb. 96 km 2200 km-hez, 105 km 2300 km-hez): az összeköttetés csak a legmagasabb nyomokkal lehetséges, a hatékonyságok és a csillapítások a modell határán vannak |
| *Nincs közös E-réteg-zóna* | Az útvonal hosszabb, mint a nyommagasságbeli hatótáv kétszerese: a két állomás nem lát közös részt az E-rétegből (egyetlen ugrás lehetetlen). |
| *Nincs ajánlott Hot* | Ebben az időpontban szinte egyetlen raj sem aktív. |

Az égbolt-kupola grafikájának mintája: a DL1DBC-féle Swan Meteor Skyview (swan.ms); poláris diagram a legjobb iránnyal: SM6FHZ RadiantCalc programja.
