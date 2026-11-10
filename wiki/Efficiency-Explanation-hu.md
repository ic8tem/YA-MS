**English** · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh)

# Hatékonyság – magyarázat

*Fül: Műszaki dokumentumok › Hatékonyság – magyarázat.*

[![Hatékonyság – magyarázat](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Műszaki dokumentum *„Come YA-MS calcola l'efficienza di uno sciame”* (Hogyan számítja ki a YA-MS egy meteorraj hatékonyságát) címmel, amely a programon belül világos oldalként jelenik meg. **Lépésről lépésre** elmagyarázza, hogyan adódik a hatékonyság, és minden lépésnél megmondja, **honnan származik**. A program **a felület nyelvén** jeleníti meg (mind a 36 nyelven), akárcsak a számítási kézikönyvet; tartalmát ez a wiki is közli a [Hatékonyság-számítás](Efficiency-Calculation-hu#a-modell) és a [Geometria és útcsillapítás](Geometry-and-Path-Loss-hu) oldalon.

## Címkék

Minden lépés színes címkét visel:

| Címke | Szín | Jelentés |
|---|---|---|
| **FONTE** (forrás) | kék | a lépés egy idézett forrást vesz át; a zárójelben lévő szám a végén lévő listára utal |
| **RILIEVO** (ellenőrzés) | zöld | összevetés a program és a források között, az eredménnyel |
| **SCELTA** (döntés) | narancs | a program döntése, nem forrásból származik: forgalmazási tapasztalattal ellenőrizendő |

## Fejezetek

| Fejezet | Tartalom |
|---|---|
| 1. Bevezetés | Cél, címkék, mit jelent a hatékonyság (OH5IY, MCG_MS; a YA-MS a valós útvonalat használja) |
| 2. Hol jönnek létre a reflexiók: az E-réteg | Nyomok 80–120 km-en; nyommagasság = a collmi hisztogram módusza (ellenőrzés: 89,5 km 2026. 11. 5-én) |
| 3. Az útvonal geometriája | A Föld és a felezőpont; antennaeleváció (a cikk képlete); a közös zóna és határai; Hot A / Hot B; antennanyaláb (DL6WU, Kraus, W4RNL) |
| 4. A raj radiánsa | A radiáns helyzete (IMO 2026/2027), a csúcs dátuma (IMO vagy napközépponti hosszúság), aktivitási profil |
| 5. A reflexió feltétele | Tükrös reflexió (McKinley), 0,05 rad Gauss-tűrés, legjobb irány (SM6FHZ), DH9GCD-képlet |
| 6. Egy ponttól a hatékonyságig | Reflexiós pontok 15 km-enként, az egyes pontok súlya, százalék; összevetés a QTFGUI-val (DJ5HG) |
| 7. Az eredmények értelmezése | A / B oldal, útvonalindex, radiánsszínek, PREV zónák, az antennából látott metszet |
| 8. Üzemi frekvencia és útcsillapítás | λ³ / λ² szabályok, a radartól az amatőrsávig, útcsillapítási hivatkozások |
| 9. Ismert korlátok | Csak alulsűrű nyomok, izotróp antennák, üzemi értékek |
| 10. Források | 17 számozott forrás |

## Gombok

| Gomb | Mire szolgál |
|---|---|
| **Exportálás Wordbe (.docx)...** | A `data/efficienza_spiegazione.docx` egy másolatát az Ön által választott helyre menti (javasolt név: *YA-MS - calcolo dell'efficienza.docx*) |
| **Megnyitás Wordben** | Ugyanazt a `.docx` fájlt nyitja meg a Word-dokumentumokhoz rendelt alapértelmezett programmal (Word, LibreOffice, …) |

## Fájlok

| Fájl | Tartalom |
|---|---|
| `data/efficienza_spiegazione.txt` | A fülön megjelenő szöveg, soronként egy blokk (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | A Word-változat |
| `data/spiegazione/efficienza_spiegazione_<code>.txt` / `.docx` | Ugyanez a dokumentum a többi 35 nyelven (pl. `_en`, `_de`, `_pt-BR`) |
| `doc/YA-MS_manuale_calcoli.docx` | A **számítási kézikönyv** (olaszul): az összes egyenlet (Word-egyenletszerkesztővel), számozva, forrásaikkal |
| `doc/manuali/YA-MS_manuale_calcoli_<code>.docx` | A számítási kézikönyv a többi 35 nyelven |

A két dokumentum a forrásból a `tools/build_spiegazione.py data [code]` és a `node tools/build_manuale.js <file.docx> [code]` paranccsal generálható újra; a fordítások a `tools/traduzioni_doc/` mappában vannak (a `tools/build_documenti.sh` az összes nyelvet újraépíti).
