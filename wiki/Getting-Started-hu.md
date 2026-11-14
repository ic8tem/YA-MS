[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · **Magyar** · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Első lépések

Első indításkor a YA-MS egy példaútvonalat mutat (JN70CN → JO62QM, 144 MHz). Öt perc elég ahhoz, hogy beállítsa a saját állomására.

## 1. A két vezérlősor

A fülek felett két sor vezérlőelem található, amelyek minden fülre érvényesek. A jobb felső sarokban lévő **Vezérlők** gomb összecsukja és kinyitja őket (nagy betűméretnél hasznos); a program megjegyzi a választást. Az állomásod (lokátor, magasság, sáv és Számítás) az Élő forgalom jobb felső részén van.

**Saját állomásom – Élő forgalom**

| Vezérlő | Mire szolgál |
|---|---|
| **Saját lokátor** / **magasság m** | Az Ön Maidenhead-lokátora (4, 6 vagy 8 karakter; a négyzet középpontját használja) és az állomás tengerszint feletti magassága. |
| **DX-állomás** / **magasság m** | A térkép mellett jobbra van az ellenállomás kerete: írd be a hívójelet és nyomj Entert, a lokátor a CALL3 adatbázisból jön (mint a YAEC-ben és a LIVETROPOVHF-ben); alatta van a lokátor és a magasság. A hívójel a lokátor mezőbe is írható. |
| **Sáv MHz** | 28, 50, 70, 144, 222 vagy 432 MHz: ebből számolja az antennanyereséget és a nyalábot, a fluxusbecslést és az összeköttetési mérleget. |
| **Számítás** | Újraszámítja az útvonalat (az E-réteg mintavételezése: néhány másodperc). |
| **Antenna az.** | Az ellenállomás dobozának tetején, a térkép mellett: az antennád azimutja, mindig **a DX felé** (az útvonal azimutja). Alatta, ugyanabban az oszlopban, a térkép jelmagyarázata. |

**2. sor – E-réteg és antenna**

| Vezérlő | Mire szolgál |
|---|---|
| **Nyommagasság km** + **radarból** | A meteornyomok magassága (alapértelmezés 90 km). Ha a *radarból* be van jelölve, a collmi radar által mért leggyakoribb magasságot (módusz) használja; lásd: [Radarfluxus](Radar-Flux-hu). |
| **Nyalábeleváció °** | Az antenna függőleges nyalábja maximumának emelkedési szöge: a 0°-ra rögzített irányantenna nyalába a talajról való visszaverődés miatt mégis néhány fokkal a horizont felett van (általában 3-8°). Bekapcsolt **antenna iránykarakterisztika** jelölőnégyzettel (alapértelmezés) az E-réteg pontjait a két antenna függőleges iránykarakterisztikája súlyozza; kikapcsolva csak azokat a pontokat használja, amelyeket mindkét állomás e szög felett lát. |
| **Yagi antenna: boom m** | A Yagi boomhossza. A program kiírja a hosszt λ-ban, a nyereséget (DL6WU-görbe) és a −3 dB-es nyalábszélességet vízszintesen és függőlegesen; lásd: [Geometria és útcsillapítás](Geometry-and-Path-Loss-hu#antennanyereség-és-nyaláb). 2 λ alatt a becslés durva. |
| **Hot spot a felezőponttól km** + **auto (AMS)** | Hot A és Hot B távolsága a felezőponttól. Az *auto (AMS)* bejelölésekor (alapértelmezés) J. Richardson (AMS) antennaeltérítési táblázatát követi, ahogy azt DJ5HG idézi: 13° 1000 km-nél, 11° 1250 km-nél, 10° 1500 és 2000 km-nél (kb. 115, 121, 132 és 176 km a felezőponttól). Ha kikapcsolja, kézzel adhat meg 30–400 km-t (az MSHV 150 km-t használ). |

**3. sor – idő**

| Vezérlő | Mire szolgál |
|---|---|
| **Idő** | UTC-óra. |
| **Számítás dátuma (UTC)** | A számítás napja az [Előrejelzés-számítás](Sky-View-hu) és a [GRAVES-radar](GRAVES-Radar-hu) számára (alapértelmezés a mai nap), az aktuális napszakban. Egyben: a [Hatékonyság-számítás](Efficiency-Calculation-hu) fülön és a GRAVES-idővonalon megjelenített nap. |
| **Órák (−12 és +36 h között)** | A számítás időpontját az adott időponthoz képest 12 órával korábbra és 36 órával későbbre tolja, 15 perces lépésekben. Mellette: *Számítás erre: most* vagy *Számítás erre: nn/hh óó:pp UTC*. |
| **Valós idő** | Vissza a jelenhez. |

Az idővonal («Órák (−12-től +36 h-ig)» és «Valós idő») a Előrejelző számítás fül tetején van, mert csak arra a számításra vonatkozik.

## 2. Az Ön állomása és a DX

1. Írja be a **Saját lokátor** és a **magasság m** értékét.
2. Írja be a **DX-állomás** lokátorát és magasságát – vagy kattintson a térképre az [Égbolt-kupola](Sky-View-hu) nézetben: **bal kattintás = DX-állomás lokátora**, **jobb kattintás = saját állomás lokátora**.
3. Válassza ki a **Sáv MHz** értéket, és nyomja meg a **Számítás** gombot.

Az alsó állapotsor megerősíti: *Útvonal kiszámítva: … km, … reflexiós pont mintavételezve … s alatt*.

## 3. Az Ön antennája

Adja meg a Yagi **boomhosszát**. A program ebből levezeti a nyereséget és a nyalábot, és figyelmeztet, ha Hot A vagy Hot B már **a nyalábon belül** esik, amikor az antenna a DX felé néz (ekkor szürkén rajzolja őket: nem kell elfordítani az antennát).

## 4. Az eredmények értelmezése

| Kérdés | Hol nézze meg |
|---|---|
| Melyik raj segíti most az útvonalamat, és melyik oldalról? | [Égbolt-kupola](Sky-View-hu): rajlista, ajánlott Hot pirossal, PREV zónák |
| Melyik ma a legjobb óra? | [Hatékonyság-számítás](Efficiency-Calculation-hu): áttekintő kártyák és óránkénti táblázat |
| Hány meteort számol a radar? | [Radarfluxus](Radar-Flux-hu) |
| Hány pingre számíthatok 144 MHz-en? | [Kísérleti előrejelzések](Experimental-Forecasts-hu) (kísérleti) |
| Képes az állomásom áthidalni az útvonalat? | [Geometria és útcsillapítás](Geometry-and-Path-Loss-hu): útcsillapítás és tartalék |
| Mikor lesz a következő csúcs? | [Meteorrajok](Showers-hu) |
| Tesztelhetek a GRAVES-szel? | [GRAVES-radar](GRAVES-Radar-hu) |

## Gyakorlati szabályok (a forrásokból)

- **A rajra merőlegesen célozzon**: a legjobb útvonal merőleges a radiáns azimutjára; legjobb irány = radiáns azimutja ±90°, tűrés ±40–50° (SM6FHZ).
- **Oldalszórás**: fordítsa az antennát 10–30°-kal afelé az oldal (A vagy B) felé, ahonnan a legtöbb reflexió érkezik (Cerrotta–Sartori-cikk).
- **Túl magas** (70° feletti) vagy túl alacsony (20° alatti) **radiáns** kevés hasznos nyomot ad (DF5HC, DH9GCD).
- A sporadikus meteorok **06 UTC** körül tetőznek (a cikk szerint; a collmi fluxus is megerősíti).
- Hasznos távolságok 432 MHz-en: 800–2000 km, a legjobb kb. 1400 km (SM6FHZ); a legjobb távolság általában 1300–1500 km (DF5HC).

Következő: [Égbolt-kupola](Sky-View-hu).
