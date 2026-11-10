[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · **Magyar** · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [ไทย](Getting-Started-th) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Első lépések

Első indításkor a YA-MS egy példaútvonalat mutat (JN70CN → JO62QM, 144 MHz). Öt perc elég ahhoz, hogy beállítsa a saját állomására.

## 1. A vezérlők három sora

A fülek felett három sor vezérlő található, amelyek minden fülre érvényesek. A jobb felső **Vezérlők** gomb összecsukja és kinyitja őket (nagy betűméretnél hasznos); a választást a program megjegyzi.

**1. sor – állomások és sáv**

| Vezérlő | Mit csinál |
|---|---|
| **Saját lokátor** / **magasság m** | Az Ön Maidenhead-lokátora (4, 6 vagy 8 karakter; a négyzet középpontját használja) és az állomás tengerszint feletti magassága. |
| **DX állomás** / **magasság m** | Annak az állomásnak a lokátora és magassága, amellyel összeköttetést szeretne. |
| **Sáv MHz** | 28, 50, 70, 144, 222 vagy 432 MHz: az antennanyereséghez és -lebenyhez, a fluxusbecsléshez és az összeköttetési mérleghez használja. |
| **Számítás** | Újraszámítja az útvonalat (az E-réteg mintavételezése: néhány másodperc). |
| **Antennairány** | Az antenna azimutja: mindig **a DX felé** (az útvonal azimutja). |
| **Betűtípus** | Az összes szöveg mérete, 100–300 %. Lásd [Beállítások](Settings-and-Data-Folder-hu#betűtípus-és-vezérlők). |

**2. sor – E-réteg és antenna**

| Vezérlő | Mit csinál |
|---|---|
| **Nyommagasság km** + **radarból** | A meteornyomok magassága (alapértelmezés 90 km). Ha a *radarból* be van jelölve, a Collm radar által mért leggyakoribb magasságot (módusz) használja; lásd [Radarfluxus](Radar-Flux-hu). |
| **Lebeny elevációja °** | Az antennalebeny legalacsonyabb elevációja (0° = horizont). Csak az E-réteg azon pontjait használja, amelyeket mindkét állomás e fölötti elevációban lát. |
| **Yagi antenna: tartócső m** | A Yagi tartócsövének (boom) hossza. A program kijelzi a hosszt λ-ban, a nyereséget (DL6WU-görbe) és a −3 dB-es lebenyt vízszintesen és függőlegesen; lásd [Geometria és útvonalcsillapítás](Geometry-and-Path-Loss-hu#antennanyereség-és-lebeny). 2 λ alatt a becslés durva. |
| **Hot spot a felezőponttól, km** | A Hot A és Hot B távolsága a felezőponttól, 30–400 km (alapértelmezés 150 km, mint az AMS Bulletin 203 / W8WN / MSHV esetén). |

**3. sor – idő**

| Vezérlő | Mit csinál |
|---|---|
| **Idő** | UTC óra. |
| **Égbolt-kupola ideje (±36 h)** | Az [Égbolt-kupola](Sky-View-hu) és a [GRAVES radar](GRAVES-Radar-hu) fül idejét legfeljebb 36 órával előre vagy hátra viszi, 15 perces lépésekben. |
| **Valós idő** | Vissza a jelen időpontra. |
| **A 24 órás táblázat napja (UTC)** | A [Hatékonyság számítása](Efficiency-Calculation-hu) fülön és a GRAVES idővonalon megjelenített nap. |

## 2. Az Ön állomása és a DX

1. Írja be a **Saját lokátor** és a **magasság m** értékét.
2. Írja be a **DX állomás** lokátorát és magasságát – vagy kattintson a térképre az [Égbolt-kupola](Sky-View-hu) fülön: **bal kattintás = DX állomás lokátora**, **jobb kattintás = saját állomás lokátora**.
3. Válassza ki a **Sáv MHz** értékét, és nyomja meg a **Számítás** gombot.

Az alsó állapotsor megerősíti: *Útvonal kiszámítva: … km, … visszaverődési pont mintavételezve … s alatt*.

## 3. Az Ön antennája

Adja meg a Yagi **tartócsövének hosszát**. A program ebből levezeti a nyereséget és a lebenyt, és figyelmeztet, ha a Hot A vagy a Hot B már **a lebenyen belül** esik, amikor az antenna a DX felé néz (ekkor szürkével rajzolja őket: nem kell elfordítani az antennát).

## 4. Az eredmények olvasása

| Kérdés | Hol nézze meg |
|---|---|
| Melyik raj segíti most az útvonalamat, és melyik oldalról? | [Égbolt-kupola](Sky-View-hu): rajlista, ajánlott Hot pirossal, PREV zónák |
| Mi ma a legjobb óra? | [Hatékonyság számítása](Efficiency-Calculation-hu): áttekintő kártyák és óránkénti táblázat |
| Hány meteort számol a radar? | [Radarfluxus](Radar-Flux-hu) |
| Hány pingre számíthatok 144 MHz-en? | [Kísérleti előrejelzések](Experimental-Forecasts-hu) (kísérleti) |
| Képes az állomásom az útvonalat áthidalni? | [Geometria és útvonalcsillapítás](Geometry-and-Path-Loss-hu): útvonalcsillapítás és tartalék |
| Mikor lesz a következő csúcs? | [Rajok](Showers-hu) |
| Kipróbálhatom a GRAVES-szel? | [GRAVES radar](GRAVES-Radar-hu) |

## Gyakorlati szabályok (a forrásokból)

- **Irányítson merőlegesen a rajra**: a legjobb útvonal merőleges a radiáns azimutjára; legjobb irány = a radiáns azimutja ±90°, tűrés ±40–50° (SM6FHZ).
- **Side-scatter**: fordítsa az antennát 10–30°-kal afelé az oldal (A vagy B) felé, ahonnan a legtöbb visszaverődés érkezik (Cerrotta–Sartori cikk).
- A **túl magasan** (70° felett) vagy túl alacsonyan (20° alatt) álló radiáns kevés hasznos nyomot ad (DF5HC, DH9GCD).
- A sporadikus meteorok csúcsa **06 UTC** körül van (cikk; a Collm-fluxus is megerősíti).
- Hasznos távolságok 432 MHz-en: 800–2000 km, a legjobb kb. 1400 km (SM6FHZ); általában a legjobb távolság 1300–1500 km (DF5HC).

Következő: [Égbolt-kupola](Sky-View-hu).
