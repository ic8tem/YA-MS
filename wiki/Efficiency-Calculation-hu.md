**English** · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh)

# Hatékonyság-számítás

*Fül: Előrejelzés-számítás › Hatékonyság-számítás.*

[![Hatékonyság-számítás](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

Egy raj **hatékonysága** százalékban fejezi ki, mennyire teszi lehetővé a radiáns helyzete a reflexiókat az **Ön** útvonalán. A fogalom Ilkka **OH5IY**-tól (MS-Soft) származik, és a Cerrotta–Sartori-cikk is átveszi: a hatékonyság csúcsa nem esik egybe a vizuális csúccsal (ZHR), mert attól függ, hol van a radiáns a két állomáshoz képest. A DL5MCG-féle MCG_MS ugyanezt az elvet négy rögzített irányra alkalmazza; a YA-MS a két lokátor közötti **valós útvonalra** számítja.

Ez a fül óránként mutatja a hatékonyságot az *A 24 órás táblázat napja (UTC)* mezőben választott napra (az értékek minden óra felénél érvényesek).

## Áttekintő kártyák

| Kártya | Tartalom |
|---|---|
| **A NAP LEGJOBB IDŐPONTJA** | A legnagyobb útvonalindexű óra, az index és a túlsúlyban lévő oldal (A/B a %-ával) |
| **LEGKEDVEZŐBB RAJ** | A nap legnagyobb ZHR × hatékonyság értékű raja, hatékonysága, órája és oldala, valamint a **legjobb irány** (radiáns azimutja +90° / −90°) |
| **MOST** | Index és túlsúlyban lévő oldal ebben az órában, valamint az ajánlott Hot (csak ha a választott nap a mai) |
| **KÍSÉRLETI ELŐREJELZÉS** | Várható reflexió/óra most, 1 óra és 2 óra múlva az előrejelzési frekvencián (Collm, SM6FHZ-szabályok; lásd: [Kísérleti előrejelzések](Experimental-Forecasts-hu)) |

A kártyák alatti sáv elmagyarázza az A és B betűket (lásd lent).

## Grafikon

*Óránkénti hatékonyság … számára, … napon (UTC, az értékek az óra felénél).* Legfeljebb öt rajra: a hatékonyság %-ban folytonos vonallal, a DH9GCD-képlet azonos színű pontozott vonallal; az **útvonalindex** kék oszlopokkal a jobb oldali skálán.

## Óránkénti táblázat

Az adott napon aktív rajonként egy sor (ZHR szerint rendezve), 24 oszlop az órákhoz (UTC):

| Cella | Jelentés |
|---|---|
| `63A` | hatékonyság 63 %, a legtöbb reflexió az **A** oldalról |
| `41B` | hatékonyság 41 %, **B** oldal |
| `3` | 5 % alatti hatékonyság: szám oldalbetű nélkül |
| üres | 1 % alatti hatékonyság |
| `…↑` | a radiáns abban az órában az Ön állomásáról nézve **70° felett** van (túl magasan) |
| sárga szöveg | hatékonyság ≥ 50 % |

- **A** = **balra** az Ön állomásától a DX-állomás felé nézve (Hot A zóna); **B** = **jobbra** (Hot B zóna). Érdemes az antennát **10–30°-kal e felé az oldal felé** fordítani (oldalszórás, Cerrotta–Sartori-cikk).
- **Világoskék sorok** (*DH9GCD %*, minden raj alatt): a DH9GCD-képlet, összehasonlításként.
- **Σ sor**: *Útvonalindex (ZHR×hat.)*.
- **Narancs sor** (*Előrejelzés … MHz (refl./óra)*): a kísérleti előrejelzés azokra az órákra, amelyekre létezik (ma és holnap egy része).

## A modell

Minden lépés megtalálható a [számítási kézikönyvben](Efficiency-Explanation-hu) (`doc/YA-MS_manuale_calcoli.docx`, 5. fejezet). Röviden:

**1. Tükrös reflexió.** Egy nyom csak akkor juttatja el a jelet A-ból B-be, ha érinti azt az ellipszoidot, amelynek fókuszai A és B (McKinley 1961). Egy raj nyomai párhuzamosak a radiáns ŝ irányával (cikk; McKinley). Az E-réteg minden P pontjára, az állomások felé mutató egységvektorokkal:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Ugyanez a törvény áll DJ5HG QTFGUI programja és *„Die Geometrie von Meteorscatterverbindungen”* (2004) című írása mögött: a nyom egy olyan kúp mentén szór, amelynek tengelye maga a nyom, és csak a kúpon lévő vevő hallja. Ideális nyomnál a kúp fala nagyon vékony (több ezer hullámhossz hosszú sugárzó); a program a feltételt σ = 0,05 rad (kb. 3°) Gauss-tűréssel fogadja el, amely azt képviseli, amit az ideális kúp nem lát: a rajradiánsok szóródását (a GMN mérései szerint 0,3–1,4°), a szél által meghajlított nyomokat és véges hosszukat – *a program döntése*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Az egyes pontok súlya.** Egy alulsűrű nyom teljesítménye (McKinley; ITU-R P.843, 3. egyenlet), φ = a szórási szög fele (85°-ra korlátozva, *döntés*), β = a nyom és az A-P-B terjedési sík által bezárt szög, p̂ = e sík egységnormálisa:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**„β szög a nyom és az útvonal között (teljes McKinley)” opció** (alapértelmezésben bekapcsolva, óvatos beállítás). Bekapcsolva: a terjedési síkot keresztező nyomok 10–15 dB-lel kevesebbet érnek, mint a síkban fekvők, így egyetlen nyom sincs túlbecsülve. Kikapcsolva: minden nyomot úgy súlyoz, mintha a síkban feküdne (β = 0, cos²φ súllyal), ahogy az 1.6-os változatig. *Ellenőrzés:* egy 1000 km-es útvonalon β nélkül a legjobb radiánsazimut az útvonaltól 15°–90°-ra van a radiáns elevációjától függően (30°, ha a radiáns 30°-on van, merőleges, ha 60°-on), és a merőleges radiáns 30°-os elevációnál 67 %-ot ér; β-val a legjobb radiáns mindig az útvonal mentén van, a merőleges pedig 15 %-ra esik. β-val elvész az SM6FHZ / DH9GCD-féle legjobbirány-szabály; β opció marad, alapértelmezésben bekapcsolva, mert ez adja a legóvatosabb értékeket, kikapcsolása pedig visszahozza a szabályt.

Egy pontot elérő meteorok száma arányos az ott mért radiánseleváció szinuszával (ŝ·û_P), ez ugyanaz a korrekció, amelyet az IMO a ZHR-nél használ.

**„Hosszabb nyomok alacsony radiánsnál (DJ5HG)” opció** (jelölőnégyzet a grafikon felett, alapértelmezésben kikapcsolva, súgóbuborékkal): DJ5HG megjegyzi, hogy alacsony radiánsnál kevesebb meteor esik egy km²-re, de a nyomok hosszabbak (akár 100 km hasznos hossz), és gyakrabban teljesítik a reflexiós törvényt. Bekapcsolt opciónál a súly min(sin El, 15/100) lesz: a hasznos rétegvastagság (15 km) osztva az eleváció szinuszával adja a nyomhosszt, 100 km-re korlátozva. Kb. 9° felett a két hatás kioltja egymást. Kikapcsolva a számítás óvatos marad.

**Számítási beállítások** (ugyanabban a sorban, választógombok): **Óvatos** (alapértelmezés, a legóvatosabb értékek: nyommagasság a radarból, normál nyomok, β bekapcsolva), **DJ5HG szerint** (102 km, hosszabb nyomok, β) és **Egyéni**, amely automatikusan kiválasztódik, ha kézzel módosítja a magasságot, a *radarból* négyzetet, a hosszabb nyomok opciót vagy β-t.

**3. Összeg és százalék.** Pontok 15 km-enként a nyommagasságban, csak ott, ahol mindkét állomás a nyalábeleváció felett látja őket (*döntés*). A 100 % az adott útvonalra legkedvezőbb radiánshelyzet:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F-et útvonalanként egyszer számítja ki egy iránybeli rácson (azimut 5°-onként, eleváció 2,5°-onként), majd interpolál.

**Hatékonyság dB-ben (DJ5HG-referencia).** A százalék csak az adott útvonal legjobb radiánshelyzetéhez viszonyított. Különböző útvonalak összehasonlításához a program a hatékonyságot dB-ben is megadja DJ5HG rögzített referenciájához képest: 0 dB egy 1000 km-es, az egyenlítőt keresztező észak–déli útvonal maximuma, a radiánssal az égi egyenlítőn napéjegyenlőségkor, ugyanazzal a magassággal és súlyokkal számítva. DJ5HG értékeit 6 dB-nél pontosabbnak adja meg.

**4. Oldal és index.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

A táblázatban szereplő betű a nagyobb arányú oldal. *A program döntései (kézikönyv, 32–33. egyenlet).*

## Összehasonlítás a DH9GCD-képlettel

A legjobb irány elsődleges forrásai Eshleman & Mlodnosky és Meeks & James (Proc. IRE, 1957), Hines (1955), valamint ennek kísérleti ellenőrzése Forsyth, Hines & Vogan által (1955): csak a szórási szög felezőjére merőleges égbolt-félkörön lévő radiánsok hasznosak, a nyomok száma sin El-lel nő, és a felezőpont közelében a hasznos nyomok kb. H·tan El távolságra esnek oldalra, a radiánssal ellentétes oldalon. DJ5HG fenntartással él: **alacsony** radiánsnál, pontosan az útvonal mentén McKinley képlete erős jeleket ad (Hamburg–Narvik, Quadrantidák, kb. 19 UTC), így a „radiáns az útvonal irányában = szinte nulla” csak magas radiánsra érvényes; a program óvatos marad, és megjeleníti az *ALACSONY RADIÁNS AZ ÚTVONAL MENTÉN* figyelmeztetést.

Független ellenőrzés: **DH9GCD** legjobbirány-képlete, **DF5HC** közlése szerint (DARC-konferencia, 2018. január) – nincs publikált elsődleges forrása –, ahol El és Az a radiáns Ön állomásáról látott elevációja és azimutja, P pedig a DX-állomás azimutja:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Akkor maximális, ha a radiáns 45°-on van és merőleges az útvonalra. DF5HC 20° alatt túl alacsonynak, **70° felett túl magasnak** tartja a radiánst: ezek az órák ↑ jelet kapnak a táblázatban és figyelmeztetést az [Égbolt-kupolán](Sky-View-hu#figyelmeztetések). A képlet nem veszi figyelembe a távolságot és a magasságokat, de jó viszonyítási alap.

## Ellenőrzések

| Ellenőrzés | Eredmény |
|---|---|
| SM6FHZ-szabály (VUSHF 2025): a legjobb útvonal merőleges a radiáns azimutjára, irány = radiáns az. ±90°, tűrés ±40–50° | A modell reprodukálja; ha a radiáns az útvonal irányában és magasan az égen van, a hatékonyság szinte nulla |
| DJ5HG QTFGUI programja, Hamburg JO53IM – Barcelona, Quadrantidák, január 4. (a kézikönyvében szereplő példa) | QTFGUI: 07:00 irány 252°, −8 dB; 08:00 nincs reflexiós zóna; 09:00 irány 168°, −4 dB. YA-MS (magasság 102 km, mint a QTFGUI-nál): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Mindhárom módszer látja a 08:00-s lyukat, amikor a radiáns szinte a zenitben van |
| DJ5HG görbéi (*Die Geometrie…*, 8–9. ábra: Hamburgból és Münchenből, Quadrantidák, január 4.; a grafikonról leolvasva, kb. ±0,5 dB és ±15 perc) a `--prova-dj5hg` automatikus teszttel összevetve (óránként egy érték) | Időzítés: a zenitközeli radiánshoz tartozó lyuk ugyanazokra az órákra esik (Barcelona 07:30–08:30 vs. 07–09; Szófia 06:36–07:48 vs. 07–08; Narvik 07–08:30 vs. 07–09); Moszkva mindkettőnél zárva van 03–10 között, Hamburgból kb. 02:30-ig, Münchenből kb. 00:30-ig nyitva, ahogy DJ5HG írja. Irányok: 2–10° eltérés. Szintek és alak 102 km-en (átlagos és RMS-eltérés a görbéktől): β és hosszabb nyomok nélkül −1,6 / 4,0 dB; hosszabb nyomokkal +1,1 / 4,6 dB; β-val −5,4 / 6,2 dB, de a legjobb alakkal (3,0 dB az átlag levonása után, szemben a 3,6-del): megjelennek az alacsony radiánshoz tartozó mély minimumok (Barcelona −15,6 dB 17-kor vs. −16 dB 19:36-kor; Szófia −18,5 dB 20-kor vs. −14 dB). β és hosszabb nyomok (*DJ5HG szerint*) −2,2 / 4,7 dB; az óvatos beállítás (radarmagasság 89,5 km, β bekapcsolva, hosszabb nyomok nélkül) −6,9 / 7,6 dB, alak 3,3 dB. β nélkül a YA-MS alig mutatja a minimumot alacsony, az útvonallal szinte egy irányba eső radiánsnál (−8,6 és −10,4 dB): ez éppen DJ5HG saját fenntartása, innen a figyelmeztetés |
| Mintavételezés 5 km-enként 15 km helyett | a százalékok kevesebb mint 0,3 ponttal változnak |

> Az MS-Soft 5.2 dokumentációja OH5IY hatékonyságát csak alulsűrű nyomokra vonatkozó relatív indexként definiálja, két tényezővel (radiánseleváció, legjobb kb. 45°, és az útvonallal bezárt szög, legjobb 90°), túlsűrű nyomokra pedig kézzel 20 %-ra emelt minimummal; a képlet nem publikus. Az MCG_MS négy rögzített irányra, a DX-lokátorral pedig a valós útvonalra számítja. A modell csak alulsűrű nyomokat vesz figyelembe, izotróp antennákkal; a túlsűrű kitörések és a sporadikus háttér nem szerepelnek a hatékonyságban (a sporadikus hátteret a radarfluxus képviseli).
