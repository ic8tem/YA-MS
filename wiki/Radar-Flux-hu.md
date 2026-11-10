[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-BR) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · **Magyar** · [Română](Radar-Flux-ro) · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [ไทย](Radar-Flux-th) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · [中文 (繁體)](Radar-Flux-zh-TW)

# Radarfluxus

*Fül: Élő és valós idejű adatok › Radarfluxus.*

[![Radarfluxus](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Ez a fül azt mutatja, amit a professzionális meteorradarok **éppen most** számolnak: az óránkénti meteorszámokat és a nyommagasságokat a **collmi** SKiYMET radarból (Lipcsei Egyetem / IAP Kühlungsborn, Németország, 36,2 MHz), valamint a **sodankyläi** radar (SGO, Finnország) legfrissebb képét. A collmi számok táplálják az Ön sávjára vonatkozó becslést és a [Kísérleti előrejelzések](Experimental-Forecasts-hu) fület; a mért nyommagasság a teljes geometriát.

## Vezérlők

| Vezérlő | Mire szolgál |
|---|---|
| **Letöltés most** | Az összes külső forrást egyszerre ellenőrzi. |
| **Az összes forrás automatikus frissítése 5 percenként** | Alapértelmezésben bekapcsolva. 5 percenként minden forrást ellenőriz, és **csak a megváltozottakat** tölti le újra (*változatlan (ellenőrizve … UTC-kor)* / *új adatok … UTC-kor*). |
| **λ-kitevő (SM6FHZ)** | A frekvenciaszabály k kitevője, alapértelmezés 3 (1–4). |

## Mi látható

| Panel | Tartalom |
|---|---|
| **Meteor/óra – tegnap és ma (UTC)** | Ciánkék oszlopok = collmi számok (érvényes), piros oszlopok = elvetett, vastag narancs vonal = *becslés … MHz-re* a jobb oldali skálán |
| **Nyommagasságok (Collm)** | Meteorok magasság-kilométerenként 70 és 110 km között, a leggyakoribb magassággal (módusz), átlaggal, mediánnal és szórással |
| Collmi kép | Az eredeti SKiYMET-grafikon, ahogy letöltődött |
| Sodankyläi kép | A sodankyläi radar legfrissebb meteorszám-képe (csak megjelenítés; a formátumát nem olvassa be) |

A grafikonok feletti sor kiírja, mikor olvasta be a collmi grafikont, és milyen függőleges skálát talált (*a grafikonról leolvasott skála: 0-… meteor/óra*).

## Hogyan olvassa be a collmi grafikont

A collmi grafikon (720 × 720 pixel, tiszta színek) tengelyei rögzített helyen vannak, de a radar **minden nap a mért értékekhez igazítja a függőleges skálát** (pl. 0–1,2·10³ 2026. 11. 5-én és 0–1,0·10³ 2026. 11. 6-án, elmozdult osztásjelekkel). A YA-MS ezért:

1. megkeresi a tengely hosszú osztásjeleit;
2. **leolvassa a feliratokat** a legfelső osztásnál és a nullánál úgy, hogy minden karaktert összevet a grafikon pontmátrixos betűkészletével;
3. minden i órára (0–47, tegnap és ma) veszi a középső oszlopot és felülről az első ciánkék pixelt, y:

```math
x_i = 101 + (i+0{.}5)\,\frac{676-101}{48},\qquad N = (y_0-y)\,\frac{N_{top}}{y_0-y_{top}}
```

y_top és y0 a legfelső osztás és a nulla sora, N_top a legfelső feliraton leolvasott érték (×1000). Felbontás: kb. 7–8 meteor/óra pixelenként. *A program döntése (kézikönyv, 42. egyenlet).*

Ha egy felirat nem olvasható, a program visszaáll a 2026. 11. 5-i kalibrációra (**kalibrált skála 0-1200 meteor/óra**), és ezt narancssárgával jelzi: *Nem olvasható a fluxus függőleges skálája (felső felirat: …): az értékeket ellenőrizni kell.* Ha maga a grafikon formátuma változik meg (*A grafikon formátuma megváltozott (…x…): nem olvasható* vagy *A fluxus tengelyei nem a várt helyen találhatók*), a beolvasást újra kell kalibrálni: kérjük, jelezze (lásd: [Közreműködés](Contributing-and-Contacts-hu)).

### Nyommagasságok

A magasság-hisztogramból (n_k meteor a k-adik km-ben, h_k átlagmagasság):

```math
\hat{h} = h_{k^*},\ k^* = \arg\max_k n_k,\qquad \bar{h} = \frac{\sum_k n_k h_k}{\sum_k n_k},\qquad s = \sqrt{\frac{\sum_k n_k (h_k-\bar{h})^2}{\sum_k n_k}}
```

*Kézikönyv, 43. egyenlet.* Ha a **radarból** be van jelölve (a vezérlők 2. sora), a **módusz** lesz minden számítás nyommagassága. Ellenőrzés: a 2026. 11. 5-i grafikon – módusz 89,5 km, átlag 88,6 km, szórás 6,8 km, ami megerősíti a Cerrotta–Sartori-cikk ~90 km-es értékét (SKiYMET-átlag).

Ha a magassággrafikon skálája megváltozik, a program figyelmeztet: *a magassági statisztikák (módusz, átlag, medián) érvényesek maradnak, az abszolút számok nem.*

## Becslés az Ön sávjára

```math
N(f) = N_{Collm}(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k},\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

**SM6FHZ** kísérleti szabályai (VUSHF 2025): a reflexiók száma és erőssége λ³-nel, időtartamuk λ²-tel skálázódik (McKinleynél λ³ egyetlen nyom teljesítménye; a nyomok száma nagyjából λ^1.5 szerint skálázódik, előreszórásban pedig az időtartamok sec²φ-vel is nőnek: lásd: [Kísérleti előrejelzések](Experimental-Forecasts-hu)). Megjelenik az IARU Region 1 szerinti legnagyobb pingidőtartam is (1000 ms 50 MHz-en, 500 ms 70 MHz-en, 100 ms 144 MHz-en, 13 ms 432 MHz-en). Az értékek tájékoztató jellegűek, a forgalmazási tapasztalattal összevetendők. A K állomástényező és az RMOB-összehasonlítás a [Kísérleti előrejelzések](Experimental-Forecasts-hu) oldalon található.

## Internetkapcsolat nélkül

Ha egyik forrás sem érhető el, **egyszer** megjelenik egy üzenet: *Nincs internetkapcsolat. A radar- és RMOB-adatok nem frissíthetők: a program az utoljára mentett adatokat használja, és 5 percenként magától újrapróbálkozik.* Az alsó állapotsor pirosra vált (*NINCS INTERNETKAPCSOLAT …*), amíg a kapcsolat helyre nem áll (*A kapcsolat helyreállt.*).

## Archívumok és források

| Fájl (a `data/` mappában) | Tartalom |
|---|---|
| `flusso_collm.csv` | A Collmból beolvasott fluxus óránkénti archívuma (a már meglévő órák frissülnek) |
| `quote_collm.csv` | A nyommagasságok archívuma |
| `radar/` | A legutóbb letöltött képek (és RMOB-fájlok) |
| `fonti_radar.csv` | A radarforrások címei, `attivo=1/0` az egyes források be- és kikapcsolásához |

| Forrás | Frekvencia | Megjegyzés |
|---|---|---|
| Collmi meteorradar, Lipcsei Egyetem (LIM) és IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | óránként frissül, minden óra 10. percében UTC; fluxus tegnap + ma, magasságeloszlás |
| Sodankylä Geofizikai Obszervatórium – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | csak kép (a radar korszerűsítés alatt, DECC-projekt) |
| swan.ms (a Collm másolata) | 36,2 MHz | alapértelmezésben kikapcsolva; csak DL1DBC engedélyével használja |

> A radaradatok az illető intézmények tulajdonát képezik (Lipcsei Egyetem / IAP Kühlungsborn, Sodankylä Geofizikai Obszervatórium).
