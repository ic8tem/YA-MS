[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Português (Brasil)](Sky-View-pt-br) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Polski](Sky-View-pl) · [Čeština](Sky-View-cs) · **Magyar** · [Română](Sky-View-ro) · [Ελληνικά](Sky-View-el) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [ไทย](Sky-View-th) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh) · [中文 (繁體)](Sky-View-zh-tw)

# Égbolt-kupola

*Fül: Előrejelzés számítása › Előrejelzés számítása.*

[![Égbolt-kupola](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Ez az alfül (a korábbi változatok égbolt-kupolája) egyetlen képernyőn mutatja meg, **hol** vannak most a hasznos nyomok, és **merre kell irányítani** az antennát. Balra az útvonal **felülnézete**; jobbra a rajlista, egy kis égbolt-kupola a radiánsokkal, a számítás szövege és az antenna felől nézett **metszet**. Minden az *Égbolt-kupola ideje* csúszka időpontjára vonatkozik (alapértelmezésben valós idő; ±36 h, 15 perces lépésekben).

A kis égbolt-kupolán a zeniten átmenő **narancs vonal** mindig a **helyes antennairányokat** adja, merőlegesen a kiválasztott (vagy a legkedvezőbb) raj elmozdulására: a radiáns azimutja ±90°, mindkét végén *antenna NNN°* felirattal, a ±45°-os tűréssel vékony vonalakként. A peremen lévő rövid narancs jelek a többi hasznos raj merőleges irányait adják.

## Felülnézet (balra)

Európa térképe felülről nézve (**K jobbra**), körülötte fokbeosztással. A térkép alatti felirat megadja a sugarát (*Térkép: széle = … km az állomástól*).

| Elem | Rajz |
|---|---|
| Útvonal / DX | Zöld vonal az Ön állomásától a DX állomásig (mindig a lokátorok közötti valódi főkör-útvonal) |
| **Hot A / Hot B** | A felezőponttól mindkét oldalon 150 km-re (állítható) lévő pontok, merőlegesen az útvonalra. **Piros = ajánlott**, **rózsaszín = az antennalebenyen kívül**, **szürke = a lebenyen belül** (figyelmeztetéssel) |
| Antennalebeny | A −3 dB-es vízszintes lebeny az antenna azimutja körül (az antenna mindig a DX felé néz), *lebeny …°* felirattal |
| A közös zóna határai | Halvány *A hat.* / *B hat.* pontok és a két kör, ahol az egyes állomások horizontja eléri az E-réteget (lásd [Geometria](Geometry-and-Path-Loss-hu#a-közös-zóna-határai)) |
| A raj elmozdulása | **Sárga vonal**: az az irány, amelyben a kiválasztott (vagy a legkedvezőbb) raj végigsöpör az égen, vagyis a radiáns azimutja |
| Legjobb irányok | **Narancs pontok**: az elmozdulásra merőleges két irány (a radiáns azimutja ±90°, SM6FHZ) |
| **PREV zónák** | Világos ellipszisek: ahová **most** a legvalószínűbb nyomok esnek, az útvonal mindkét oldalán egy-egy |

A feliratok nem fedik egymást: a Hot A és a PREV A az útvonaltól balra, a B jobbra van kiírva. A **Jelmagyarázat** a térkép jobb oldalán lévő összecsukható oszlop.

**Egér a térképen:** **bal kattintás = DX állomás lokátora**, **jobb kattintás = saját állomás lokátora**. Az útvonal azonnal újraszámolódik.

Beállítások a rajlista felett: **Hot A / Hot B irányok**, **Európa-térkép** (Natural Earth, első indításkor letöltve a `data/mappa` mappába), **Felülnézet (K jobbra)**.

### Ajánlott Hot

A megjelenített időpontra a program összegzi a horizont feletti összes rajra a ZHR × hatékonyság súlyt, megosztva az A oldal (f_A hányad) és a B oldal között. A nagyobb súlyú oldal adja az ajánlott Hot pontot, amelyet pirossal rajzol:

```
W_A = Σ (ZHR·η/100)·f_A        W_B = Σ (ZHR·η/100)·(1 − f_A)        recommended = side with larger W
```

*A program választása (kézikönyv, 23. egyenlet).* Az ötlet forrása: DJ5HG, DF5HC beszámolója szerint (DARC-konferencia, 2018) – a radiáns helyzetétől függően a két pont, a HOT-A vagy a HOT-B közül az egyik kedvezőbb. Az, hogy 10–30°-kal érdemes az adott oldal felé fordulni (side-scatter), a Cerrotta–Sartori cikkből származik.

### PREV zónák

Az E-réteg minden P pontjára a program összeadja az összes aktív raj hatékonysághoz való hozzájárulását (ugyanazzal a tükrözési feltétellel, mint a [hatékonyságnál](Efficiency-Calculation-hu#a-modell)), a ZHR-rel súlyozva. A maximum legalább 3 %-át elérő pontok alkotják a PREV zónákat; mindegyiket ellipszisként rajzolja, amelynek középpontja a pontok súlyozott átlaga, tengelyei pedig a szórásuk kétszeresei.

```
W_P = Σ ZHR · c_P(ŝ)      c_P = 100 · w_P·S_P·max(0, ŝ·û_P) / max F      PREV: W_P ≥ 0.03 · max W
```

*A program választása (kézikönyv, 34. egyenlet).* Ez a gyakorlati szabály: ha a raj északról délre söpör, a hasznos nyomok keletre és nyugatra esnek.

## Rajlista (jobbra fent)

| Oszlop | Jelentés |
|---|---|
| Raj, Kód | Név és IMO-kód |
| ZHR most | Aktivitás ebben a pillanatban (az IMO csúcs-ZHR az aktivitási profillal) |
| Azimut, Elev. | A radiáns helyzete az Ön állomásáról nézve |
| Hatékony. % | A raj hatékonysága erre az útvonalra |
| Oldal | A vagy B, az az oldal, ahonnan a legtöbb visszaverődés érkezik |
| Legjobb irány | A radiáns azimutja ±90° |
| Kelés, Nyugvás | A radiáns kelése és nyugvása (UTC); ahol érvényes, *cirkumpoláris* vagy *mindig alatta* |

Egy sorra kattintva kiválasztja a rajt: a sárga elmozdulási vonal és a narancs pontok azt követik.

## Kis égbolt-kupola (jobbra középen)

A radiánsok az Ön állomásáról nézett égbolt-kupolán, **IMO-kódjukkal** és **napi pályájukkal ciánkékben** (UTC órák). **Kattintson egy radiánsra** a kiválasztásához. Színek:

| Szín | Jelentés |
|---|---|
| Sárga | hatékonyság ≥ 50 % és ZHR ≥ 2 |
| Narancs | hatékonyság ≥ 20 % |
| Sötétvörös | hatékonyság < 20 % |
| Szürke | szinte inaktív |

Mellette a számítás szövege: az útvonal hossza és azimutja, a felezőpont és elevációja, a Hot A / Hot B azimutjai és eltérései, az ajánlott Hot (*Most ajánlott: …, az. …° (a várható visszaverődések …%-a)*), a közös zóna határai, valamint az emlékeztető: *legjobb irányzás a rajhoz: MERŐLEGESEN a beérkezés irányára (radiáns azimutja ±90°, tűrés ±40–50°, SM6FHZ)*.

## Metszet (jobbra lent)

*METSZET – a legvalószínűbb nyomok az antennától a DX állomás felé nézve.* Vízszintesen az **azimut a DX állomáshoz képest** (← A bal, B → jobb), függőlegesen az **eleváció**. Minden rajból a 14 legerősebb visszaverődési pontot veszi; minden nyom egy a radiáns felé irányított szakasz, a nyommagasság felett 10 km-től alatta 10 km-ig (oldalanként legfeljebb 60 km), annál vastagabb, minél valószínűbb. Ugyancsak megjelenik: az antennalebeny (−3 dB-es kör a lebeny elevációja körül), a DX állomás és a Hot A / Hot B.

```
Q = P ± t½·ŝ        t½ = min(60 km, 10 km / max(0.17, |ŝ·û_P|))
```

*A program választása (kézikönyv, 35. egyenlet).*

## Figyelmeztetések

| Figyelmeztetés | Mikor |
|---|---|
| **FIGYELEM: a Hot A (és/vagy a Hot B) az antennalebenyen belül esik …** | A hot spot az antenna azimutjától ±θ/2-n belül van (θ = a −3 dB-es vízszintes lebeny): ezzel az iránnyal már le van fedve. A térképen szürkén látszik. Az ajánlott Hot piros marad. |
| **TÚL MAGAS RADIÁNS (70° felett)** | Egy hasznos radiáns az Ön állomásáról nézve 70° felett van: a nyomok szinte függőlegesen esnek, és kevéssé vernek vissza az útvonal felé (DF5HC, DH9GCD). Ugyanezek az órák ↑ jellel vannak megjelölve az [óránkénti táblázatban](Efficiency-Calculation-hu#óránkénti-táblázat). |
| *Nincs közös E-réteg-zóna* | Az útvonal hosszabb, mint a nyommagasságban mért hatótávolság kétszerese: a két állomás nem lát közös E-réteg-részt (egyetlen ugrás lehetetlen). |
| *Nincs ajánlott Hot* | Ebben az időpontban szinte nincs aktív raj. |

Hivatkozás az égbolt-kupola grafikájához: DL1DBC Swan Meteor Skyview programja (swan.ms); poláris diagram a legjobb iránnyal: SM6FHZ RadiantCalc programja.
