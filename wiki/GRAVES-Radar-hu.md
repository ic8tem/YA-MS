[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Português (Brasil)](GRAVES-Radar-pt-br) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Polski](GRAVES-Radar-pl) · [Čeština](GRAVES-Radar-cs) · **Magyar** · [Română](GRAVES-Radar-ro) · [Ελληνικά](GRAVES-Radar-el) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [ไทย](GRAVES-Radar-th) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh) · [中文 (繁體)](GRAVES-Radar-zh-tw)

# GRAVES-radar

*Fül: Élő és valós idejű adatok › GRAVES-radar.*

[![GRAVES-radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Mi a GRAVES

A **GRAVES** egy francia radar, amely **CW-jelet sugároz 143,050 MHz-en** **Broye-lès-Pesmes**-ből (é. sz. 47,348°, k. h. 5,515°, lokátor: **JN27SI**, kb. 200 m tengerszint feletti magasság; Wikipédia). Azokban a zónákban lévő meteornyomok, amelyeket a GRAVES és Ön is lát, **előreszórással** visszaverik Önhöz a jelét: rövid *pingeket* hall a vivő közelében. Így számolják a **RMOB** megfigyelői a 143,050 MHz-en óráról órára a meteorokat, és ez egy ingyenes, mindig bekapcsolt tesztjel a 2 m-es meteorszórásos állomása számára.

A fül a **GRAVES → Ön** útvonalat önálló meteorszórásos útvonalként kezeli: a fő útvonallal azonos függvényekkel (azonos nyommagasság, nyalábeleváció és hot spot-távolság) kiszámítja a rajok hatékonyságát, az ajánlott Hot pontot és a PREV zónákat, majd ellenőrzi, hogy ez a zóna **a GRAVES nyalábján belül** van-e, és **mikor** világítja meg a nyaláb.

## Felső sáv

| Vezérlő | Mire szolgál |
|---|---|
| **Most** | Visszaállítja a számítást valós időre: mai dátum és nullán álló óracsúszka (a fül a *Számítás dátuma* és az *Órák* vezérlőt követi). |
| **GRAVES beállítása DX-ként** | A DX-állomás a GRAVES lesz (JN27SI, magasság 200 m), és a fő útvonal újraszámolódik: ezután az összes többi fül a GRAVES-útvonalat mutatja. |
| **Nyalábsorrend** | *0,8 s lépésenként · 4,8 s ciklus (PE1ITR 2021)* (alapértelmezés) vagy *3,2 s lépésenként · 19,2 s ciklus (PE1ITR 2007)*. |

## A négy kártya

| Kártya | Tartalom |
|---|---|
| **HASZNOS ZÓNA A GRAVES NYALÁBJÁBAN** | *Igen · X szektor* az ajánlott hot spot GRAVES-ből látott azimutjával és elevációjával, valamint a lépéssel (1–6); vagy *Nem: a szektorokon kívül* / *Nem: a GRAVES horizontja alatt* / *Nem: a nyaláb felett (kb. 25°)* |
| **A GRAVES → ÖN ÚTVONAL HATÉKONYSÁGA MOST** | Útvonalindex Σ ZHR × hatékonyság, legjobb raj, túlsúlyban lévő oldal (A/B), és *várható visszhangok ≈ …/óra* (kísérleti, lásd lent) |
| **ÚTVONAL** | Távolság a GRAVES-ig; antenna az ajánlott Hot felé (azimut és eleváció); a GRAVES közvetlen azimutja |
| **A NYALÁB KÖVETKEZŐ ÁTHALADÁSA A ZÓNA FELETT** | *most · még … s* vagy *… s múlva*, a lépés (pl. *B4*), a következő három időpont (másodperc a percen belül) és az elkapott nyomok aránya |

Ha abban a pillanatban egyetlen raj sem hasznos, a program a **nyalábhoz legjobban illő** hot spotot mutatja (a szektorokon belül, a déli irányhoz legközelebb), és ezt jelzi is.

## Az égbolt a GRAVES-ből nézve

PE1ITR és a Bolidozor-wiki szerint **négy fázisvezérelt antennarendszer** fedi le a déli égboltot **90°-tól 270°-ig** terjedő azimutban, négy **45°-os szektorban**:

| Szektor | Azimut a GRAVES-től |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Minden szektor **6 darab 7,5°-os lépésre** oszlik, a legkisebb azimuttól kezdve 1-től 6-ig számozva; ezek egymás után világítanak, **mind a négy szektorban egyidejűleg**. A nyaláb **elevációban kb. 25° széles**: a nyommagasságban a két szaggatott kör közötti színes gyűrűt fedi le (*nyalábhorizont*). Az ábrán: narancs/rózsaszín pontok = a GRAVES → Ön útvonal PREV zónái, zöld vonal = az Ön állomásának iránya, piros vonal = az Ön állomásától az ajánlott hot spotig; az éppen világító lépés kiemelve látható.

## Idővonal-rekonstrukció

*IDŐVONAL-REKONSTRUKCIÓ · dátum UTC* (ugyanaz a nap, mint a 24 órás táblázatban): minden órára a GRAVES → Ön útvonal hatékonysága, a legkedvezőbb raj és a hasznos ablak (*óó:00 → óó:00 UTC · n h*), a maximummal (*max Σ … óó:30-kor*) és egy piros *most* jelzővel. Alatta **a következő másodpercek részletei**: a szektor hat lépése, a hasznos zónát megvilágító lépés, és *lehetséges visszhang (+0,3 s nyom)*.

### A nyaláb időzítése

A sorrend az **UTC**-hez van kötve (PE1ITR): az éppen világító lépést a 00:00 UTC óta eltelt másodpercekből számolja, a ciklus szerinti maradékkal (a 86 400 s a 4,8 s-nak és a 19,2 s-nak is többszöröse). A vezérlőállomás néha néhány lépéssel eltolja a sorrendet, ezért a részletezés **előrejelzés, amelyet hallgatással kell megerősíteni**. A sárga **PC-óra szinkronizálva** címke erre emlékeztet: szinkronizálja számítógépét egy NTP-szerverrel (legfeljebb néhány tized másodperc hiba).

### Észlelési tényező

Egy nyom csak akkor hallható, ha a nyaláb megvilágítja, amíg tart:

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

A 0,3 s egy alulsűrű nyom tipikus időtartama 143 MHz-en – rögzített érték, *a program döntése* (az SM6FHZ-féle λ²-szabály a sávok között skálázza az időtartamokat, de kiindulási értéket nem ad).

### Várható visszhangok (kísérleti)

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

A [Kísérleti előrejelzések](Experimental-Forecasts-hu) előrejelzését (amely már tartalmazza a K állomástényezőt) az SM6FHZ-szabállyal (azonos k kitevővel) a saját f_fc frekvenciájáról 143,050 MHz-re skálázza, a két útvonal rajindexeinek arányával korrigálja (a 10-es állandó a sporadikus hátteret képviseli, mint az előrejelzésben), és megszorozza az észlelési tényezővel. Csak tájékoztató jellegű: vesse össze az RMOB-megfigyelőkkel.

## Hogyan hallhatók a GRAVES pingjei

| Lépés | Teendő |
|---|---|
| Vevő | **USB 143,049 MHz-en** (kb. 1 kHz-es hang) vagy 143,050 MHz, **lassú vagy kikapcsolt AGC**, **legalább 2,4 kHz-es** hangfrekvenciás sávszélesség |
| Antenna | A GRAVES → Ön útvonal **ajánlott hot spotja** felé (*ÚTVONAL* kártya), **alacsony elevációval** |
| Waterfall | A pingek **rövid vonalak a vivő közelében**; a hosszú (túlsűrű) nyomok szélesebbek és Doppler-eltolódást mutatnak |
| Számlálás | Az RMOB a GRAVES-t használja az óránkénti meteorszámláláshoz: **vesse össze pingjeit a 143,050 MHz-es megfigyelőkkel** ([Kísérleti előrejelzések](Experimental-Forecasts-hu#összehasonlítás-az-rmob-bal)) |

## Források

1. Rob Hardenberg **PE1ITR**, *„The 143.050 MHz Graves Radar, a VHF Beacon”* (DUBUS 4/2007) és *„Graves Radar Update April 2021”* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozor**-wiki, „Graves” – antennarendszerek, szektorok és a nyaláb időzítése
3. **Wikipédia**, „GRAVES (system)” – adó Broye-lès-Pesmes-ben (é. sz. 47,348°, k. h. 5,515°)
4. **RMOB** – megfigyelők 143,050 MHz-en ([rmob.org](https://www.rmob.org))
5. **YAEC** (IC8TEM) – GRAVES Radar fül (ennek a fülnek a mintája)
