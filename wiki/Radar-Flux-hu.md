[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-br) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · **Magyar** · [Română](Radar-Flux-ro) · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [ไทย](Radar-Flux-th) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · [中文 (繁體)](Radar-Flux-zh-tw)

# Radarfluxus

*Fül: Élő és valós idejű adatok › Radarfluxus.*

[![Radarfluxus](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Ez a fül azt mutatja, amit a professzionális meteorradarok **éppen most** számolnak: a **Collm** SKiYMET radar (Lipcsei Egyetem / IAP Kühlungsborn, Németország, 36,2 MHz) óránkénti meteorszámait és nyommagasságait, valamint a **Sodankylä** radar (SGO, Finnország) legutóbbi képét. A Collm-számok táplálják az Ön sávjára vonatkozó becslést és a [Kísérleti előrejelzéseket](Experimental-Forecasts-hu); a mért nyommagasság a teljes geometriát.

## Vezérlők

| Vezérlő | Mit csinál |
|---|---|
| **Letöltés most** | Egyszerre ellenőrzi az összes külső forrást. |
| **Minden forrás automatikus frissítése 5 percenként** | Alapértelmezésben bekapcsolva. Ötpercenként minden forrás ellenőrzésre kerül, és **csak a megváltozottak** töltődnek le újra (*változatlan (ellenőrizve … UTC-kor)* / *új adatok … UTC-kor*). |
| **λ-kitevő (SM6FHZ)** | A frekvenciaszabály k kitevője, alapértelmezés 3 (1–4). |

## Mi látható

| Panel | Tartalom |
|---|---|
| **Meteor/óra – tegnap és ma (UTC)** | Cián oszlopok = Collm-számok (érvényes), piros oszlopok = elvetett, vastag narancs vonal = *becslés … MHz-en* a jobb oldali skálán |
| **Nyommagasságok (Collm)** | Meteorok magassági kilométerenként 70 és 110 km között, a leggyakoribb magassággal (módusz), átlaggal, mediánnal és szórással |
| Collm-kép | Az eredeti SKiYMET-diagram, ahogy letöltődött |
| Sodankylä-kép | A Sodankylä radar legutóbbi meteorszám-képe (csak megjelenítve; a formátumát a program nem olvassa) |

A diagramok feletti sor megmondja, mikor olvasta be a program a Collm-diagramot, és milyen függőleges skálát talált (*a diagramról olvasott skála: 0-… meteor/óra*).

## Hogyan olvassa a program a Collm-diagramot

A Collm-diagram (720 × 720 képpont, tiszta színek) tengelyei rögzített helyen vannak, de a radar **naponta a mért értékekhez igazítja a függőleges skálát** (pl. 0–1,2·10³ 2026. 11. 5-én és 0–1,0·10³ 2026. 11. 6-án, elmozdult osztásjelekkel). A YA-MS ezért:

1. megkeresi a tengely hosszú osztásjeleit;
2. **beolvassa a legfelső osztásjel és a nulla feliratát**, minden karaktert összevetve a diagram pontmátrixos betűkészletével;
3. minden i órára (0–47, tegnap és ma) veszi a középső oszlopot és felülről az első cián képpontot, y:

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top és y0 a legfelső osztásjel és a nulla sora, N_top a legfelső feliraton olvasott érték (×1000). Felbontás: kb. 7–8 meteor/óra képpontonként. *A program választása (kézikönyv, 42. egyenlet).*

Ha egy felirat nem olvasható, a program visszatér a 2026. 11. 5-i kalibrációhoz (**kalibrált skála 0-1200 meteor/óra**), és ezt narancs színnel jelzi: *A függőleges fluxusskála nem olvasható (felső felirat: …): az értékeket ellenőrizni kell.* Ha magának a diagramnak a formátuma változik meg (*A diagram formátuma megváltozott (…x…): nem olvasható* vagy *A fluxustengelyek nem a várt helyen vannak*), a beolvasást újra kell kalibrálni: kérjük, jelezze (lásd [Közreműködés](Contributing-and-Contacts-hu)).

### Nyommagasságok

A magassági hisztogramból (n_k meteor a k-adik km-ben, átlagos magasság h_k):

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*Kézikönyv, 43. egyenlet.* Ha a **radarból** be van jelölve (a vezérlők 2. sora), a **módusz** lesz az összes számítás nyommagassága. Ellenőrzés: a 2026. 11. 5-i diagram – módusz 89,5 km, átlag 88,6 km, szórás 6,8 km, ami megerősíti a Cerrotta–Sartori cikk ~90 km-ét (SKiYMET-átlag).

Ha a magassági diagram skálája megváltozik, a program figyelmeztet: *a magassági statisztikák (leggyakoribb érték, átlag, medián) érvényesek maradnak, az abszolút számok nem.*

## Becslés az Ön sávjára

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

**SM6FHZ** kísérleti szabályai (VUSHF 2025): a visszaverődések száma és intenzitása λ³-nel, időtartamuk λ²-tel skálázódik; a λ³-függés ugyanaz, mint McKinley alulsűrű egyenletében. A program az IARU 1. Régió szerinti legnagyobb pingidőtartamot is kijelzi (1000 ms 50 MHz-en, 500 ms 70 MHz-en, 100 ms 144 MHz-en, 13 ms 432 MHz-en). Az értékek tájékoztató jellegűek, a forgalmi tapasztalattal összevetendők. A K állomástényező és az RMOB-összehasonlítás a [Kísérleti előrejelzések](Experimental-Forecasts-hu) oldalon található.

## Kapcsolat nélkül

Ha egyetlen forrás sem érhető el, **egyszer** megjelenik egy üzenet: *Nincs internetkapcsolat. A radar- és RMOB-adatok nem frissíthetők: a program az utoljára mentett adatokat használja, és 5 percenként magától újrapróbálkozik.* Az alsó állapotsor pirosra vált (*NINCS INTERNETKAPCSOLAT …*), amíg a kapcsolat helyre nem áll (*A kapcsolat helyreállt.*).

## Archívumok és források

| Fájl (a `data/` mappában) | Tartalom |
|---|---|
| `flusso_collm.csv` | A Collmból olvasott fluxus óránkénti archívuma (a már meglévő órák frissülnek) |
| `quote_collm.csv` | A nyommagasságok archívuma |
| `radar/` | A legutóbb letöltött képek (és RMOB-fájlok) |
| `fonti_radar.csv` | A radarforrások címei, `attivo=1/0` az egyes források be-/kikapcsolásához |

| Forrás | Frekvencia | Megjegyzés |
|---|---|---|
| Collm meteorradar, Lipcsei Egyetem (LIM) és IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | óránként, a 10. percben frissül (UTC); fluxus tegnap + ma, magassági eloszlás |
| Sodankylä Geofizikai Obszervatórium – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | csak kép (a radar korszerűsítés alatt, DECC-projekt) |
| swan.ms (a Collm másolata) | 36,2 MHz | alapértelmezésben kikapcsolva; csak DL1DBC engedélyével használja |

> A radaradatok az illető intézmények tulajdonát képezik (Lipcsei Egyetem / IAP Kühlungsborn, Sodankylä Geofizikai Obszervatórium).
