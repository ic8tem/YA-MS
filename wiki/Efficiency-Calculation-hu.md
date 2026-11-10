[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · **Magyar** · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [ไทย](Efficiency-Calculation-th) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Hatékonyság számítása

*Fül: Előrejelzés számítása › Hatékonyság számítása.*

[![Hatékonyság számítása](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

Egy raj **hatékonysága** százalékban megadja, hogy radiánsának helyzete mennyire teszi lehetővé a visszaverődéseket az **Ön** útvonalán. A fogalom Ilkka **OH5IY**-tól (MS-Soft) származik, és a Cerrotta–Sartori cikk is átveszi: a hatékonysági csúcs nem esik egybe a vizuális csúccsal (ZHR), mert attól függ, hol van a radiáns a két állomáshoz képest. A DL5MCG-féle MCG_MS ugyanezt az elvet négy rögzített irányra alkalmazza; a YA-MS a két lokátor közötti **valódi útvonalra** számítja.

Ez a fül óráról órára mutatja a *A 24 órás táblázat napja (UTC)* mezőben kiválasztott napra (értékek minden óra felénél).

## Áttekintő kártyák

| Kártya | Tartalom |
|---|---|
| **A NAP LEGJOBB IDŐSZAKA** | A legnagyobb útvonalindexű óra, az index és a túlnyomó oldal (A/B a %-ával) |
| **LEGKEDVEZŐBB RAJ** | A nap legnagyobb ZHR × hatékonyságú raja, hatékonysága, órája és oldala, valamint a **legjobb irány** (a radiáns azimutja +90° / −90°) |
| **MOST** | Index és túlnyomó oldal ebben az órában, valamint az ajánlott Hot (csak ha a kiválasztott nap a mai) |
| **KÍSÉRLETI ELŐREJELZÉS** | Várható visszaverődés/óra most, 1 óra és 2 óra múlva az előrejelzési frekvencián (Collm, SM6FHZ-szabályok; lásd [Kísérleti előrejelzések](Experimental-Forecasts-hu)) |

A kártyák alatt egy sáv magyarázza az A és B betűket (lásd alább).

## Grafikon

*Óránkénti hatékonyság: …, … (UTC, értékek fél órakor).* Legfeljebb öt rajra: a hatékonyság %-ban folytonos vonallal, a DH9GCD-képlet ugyanolyan színű pontozott vonallal; az **útvonalindex** kék oszlopokkal a jobb oldali skálán.

## Óránkénti táblázat

Az adott napon aktív minden rajhoz egy sor (ZHR szerint rendezve), 24 oszlop az órákhoz (UTC):

| Cella | Jelentés |
|---|---|
| `63A` | 63 % hatékonyság, a legtöbb visszaverődés az **A** oldalról |
| `41B` | 41 % hatékonyság, **B** oldal |
| `3` | 5 % alatti hatékonyság: szám oldalbetű nélkül |
| üres | 1 % alatti hatékonyság |
| `…↑` | a radiáns abban az órában az Ön állomásáról nézve **70° felett** van (túl magasan) |
| sárga szöveg | hatékonyság ≥ 50 % |

- **A** = **balra** az Ön állomásától a DX állomás felé nézve (Hot A zóna); **B** = **jobbra** (Hot B zóna). Érdemes az antennát **10–30°-kal az adott oldal felé** fordítani (side-scatter, Cerrotta–Sartori cikk).
- **Világoskék sorok** (*DH9GCD %*, minden raj alatt): a DH9GCD-képlet, összehasonlításként.
- **Σ sor**: *Útvonalindex (ZHR×hat.)*.
- **Narancs sor** (*Előrejelzés … MHz (visszav./óra)*): a kísérleti előrejelzés azokra az órákra, amelyekre létezik (ma és holnap egy része).

## A modell

Minden lépés megtalálható a [számítási kézikönyvben](Efficiency-Explanation-hu) (`doc/YA-MS_manuale_calcoli.docx`, 5. fejezet). Röviden:

**1. Tükrös visszaverődés.** Egy nyom csak akkor juttatja el a jelet A-ból B-be, ha érinti azt az ellipszoidot, amelynek fókuszai A és B (McKinley 1961). Egy raj nyomai párhuzamosak a radiáns ŝ irányával (cikk; McKinley). Az E-réteg minden P pontjára, az állomások felé mutató egységvektorokkal:

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

Ugyanez a törvény áll a DJ5HG-féle QTFGUI (kúpos szórás) mögött is. A feltételt a program σ = 0,05 rad (kb. 3°) Gauss-tűréssel fogadja el – *a program választása*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Az egyes pontok súlya.** Egy alulsűrű nyom teljesítménye (McKinley), φ = a szórási szög fele (85°-ra korlátozva, *választás*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Az egy pontba érkező meteorok száma arányos a radiáns ottani elevációjának szinuszával (ŝ·û_P); ugyanezt a korrekciót használja az IMO a ZHR-nél.

**3. Összeg és százalék.** Pontok 15 km-enként a nyommagasságban, csak ott, ahol mindkét állomás a lebenyeleváció felett látja őket (*választás*). A 100 % az adott útvonalra legkedvezőbb radiánshelyzet:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

Az F-et útvonalanként egyszer számítja ki egy irányrácson (azimut 5°-onként, eleváció 2,5°-onként), majd interpolál.

**4. Oldal és index.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

A táblázatban szereplő betű a nagyobb hányadú oldal. *A program választásai (kézikönyv, 32–33. egyenlet).*

## DH9GCD-összehasonlítás

Független ellenőrzés: **DH9GCD** legjobbirány-képlete, **DF5HC** közlése szerint (DARC-konferencia, 2018. január), ahol El és Az a radiáns Ön állomásáról nézett elevációja és azimutja, P pedig a DX állomás azimutja:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Akkor maximális, ha a radiáns 45°-on áll és az útvonalra merőleges irányban van. DF5HC szerint a radiáns 20° alatt túl alacsony, **70° felett túl magas**: ezek az órák ↑ jelet kapnak a táblázatban, és figyelmeztetés jelenik meg az [Égbolt-kupola](Sky-View-hu#figyelmeztetések) fülön. A képlet figyelmen kívül hagyja a távolságot és a magasságokat, de jó viszonyítási alap.

## Ellenőrzések

| Ellenőrzés | Eredmény |
|---|---|
| SM6FHZ szabálya (VUSHF 2025): a legjobb útvonal merőleges a radiáns azimutjára, irány = radiáns az ±90°, tűrés ±40–50° | A modell reprodukálja; ha a radiáns az útvonallal egy vonalban és magasan áll, a hatékonyság szinte nulla |
| DJ5HG QTFGUI programja, Hamburg JO53IM – Barcelona, Kvadrantidák, január 4. (a kézikönyvének példája) | QTFGUI: 07:00 irány 252°, −8 dB; 08:00 nincs visszaverődési zóna; 09:00 irány 168°, −4 dB. YA-MS (102 km-es magassággal, mint a QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Mindhárom módszer látja a 08:00-s lyukat, amikor a radiáns szinte a zenitben van |
| Mintavételezés 5 km-enként 15 km helyett | a százalékok kevesebb mint 0,3 ponttal változnak |

> Az OH5IY és az MCG_MS által használt skála részletei nem ismertek (az MS-Soft kézikönyvei nem érhetők el): mielőtt egyenértékűnek tekintené őket, vesse össze a százalékokat ezekkel a programokkal. A modell csak alulsűrű nyomokat vesz figyelembe, izotrop antennákkal; a túlsűrű kitörések és a sporadikus háttér nincs benne a hatékonyságban (a sporadikus hátteret a radarfluxus képviseli).
