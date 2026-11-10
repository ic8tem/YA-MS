[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · **Magyar** · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [ไทย](Efficiency-Explanation-th) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Hatékonyság - magyarázat

*Fül: Műszaki dokumentumok › Hatékonyság - magyarázat.*

[![Hatékonyság - magyarázat](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Műszaki dokumentum, *„Come YA-MS calcola l'efficienza di uno sciame”* (Hogyan számítja a YA-MS egy raj hatékonyságát), amely a programon belül világos oldalként jelenik meg. **Lépésről lépésre** elmagyarázza, hogyan adódik a hatékonyság, és minden lépésnél megmondja, **honnan származik**. A dokumentum jelenleg **olasz nyelvű**; ez a wiki magyarul ismerteti a tartalmát a [Hatékonyság számítása](Efficiency-Calculation-hu#a-modell) és a [Geometria és útvonalcsillapítás](Geometry-and-Path-Loss-hu) oldalakon.

## Címkék

Minden lépés színes címkét visel:

| Címke | Szín | Jelentés |
|---|---|---|
| **FONTE** (forrás) | kék | a lépés egy idézett forrást vesz át; a zárójelben lévő szám a végén található listára utal |
| **RILIEVO** (ellenőrzés) | zöld | összehasonlítás a program és a források között, az eredménnyel |
| **SCELTA** (választás) | narancs | a program választása, nem forrásból átvett: forgalmi tapasztalattal ellenőrizendő |

## Fejezetek

| Fejezet | Tartalom |
|---|---|
| 1. Bevezetés | Cél, címkék, mit jelent a hatékonyság (OH5IY, MCG_MS; a YA-MS a valódi útvonalat használja) |
| 2. Hol jönnek létre a visszaverődések: az E-réteg | Nyomok 80–120 km-en; nyommagasság = a Collm-hisztogram módusza (ellenőrzés: 89,5 km 2026. 11. 5-én) |
| 3. Az útvonal geometriája | Föld és felezőpont; antennaeleváció (a cikk képlete); a közös zóna és határai; Hot A / Hot B; antennalebeny (DL6WU, Kraus, W4RNL) |
| 4. A raj radiánsa | A radiáns helyzete (IMO 2026/2027), a csúcs dátuma (IMO vagy napi hosszúság), aktivitási profil |
| 5. A visszaverődés feltétele | Tükrös visszaverődés (McKinley), 0,05 rad-os Gauss-tűrés, legjobb irány (SM6FHZ), DH9GCD-képlet |
| 6. Egy ponttól a hatékonyságig | Visszaverődési pontok 15 km-enként, az egyes pontok súlya, százalék; összehasonlítás a QTFGUI-val (DJ5HG) |
| 7. Az eredmények értelmezése | A / B oldal, útvonalindex, radiánsszínek, PREV zónák, az antenna felől nézett metszet |
| 8. Üzemi frekvencia és útvonalcsillapítás | λ³ / λ² szabályok, a radartól az amatőrsávig, útvonalcsillapítási hivatkozások |
| 9. Ismert korlátok | Csak alulsűrű nyomok, izotrop antennák, munkaértékek |
| 10. Források | 17 számozott forrás |

## Gombok

| Gomb | Mit csinál |
|---|---|
| **Exportálás Wordbe (.docx)...** | A `data/efficienza_spiegazione.docx` egy másolatát az Ön által választott helyre menti (javasolt név: *YA-MS - calcolo dell'efficienza.docx*) |
| **Megnyitás Wordben** | Ugyanezt a `.docx` fájlt a Word-dokumentumok alapértelmezett programjával nyitja meg (Word, LibreOffice, …) |

## Fájlok

| Fájl | Tartalom |
|---|---|
| `data/efficienza_spiegazione.txt` | A fülön megjelenő szöveg, soronként egy blokk (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | A Word-változat |
| `doc/YA-MS_manuale_calcoli.docx` | A **számítási kézikönyv**: az összes egyenlet (Word-egyenletszerkesztő), számozva, a forrásaikkal |

A két dokumentum a forrásból újragenerálható a `tools/build_spiegazione.py data` és a `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` paranccsal.
