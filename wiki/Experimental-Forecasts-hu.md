[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · **Magyar** · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Kísérleti előrejelzések

*Fül: Előrejelzés számítása › Kísérleti előrejelzések.*

[![Kísérleti előrejelzések](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Ez a fül a **Collm radar (36,2 MHz)** meteorszámait **óránkénti visszaverődésszám-becsléssé alakítja egy amatőrsávra** (alapértelmezésben 144 MHz, de bármely frekvencia 28 és 1300 MHz között), előrejelzést ad a **következő 24 órára** az Ön útvonalára, és lehetővé teszi a becslés **összehasonlítását** egy **RMOB**-megfigyelővel – például olyannal, aki a GRAVES-t hallgatja 143,050 MHz-en.

> Itt minden **kísérleti**: a frekvenciaszabály empirikus szabály, az állomástényező pedig az Ön állomásától függ. A számokat órák és napok összehasonlítására használja, és ellenőrizze őket forgalom közben.

## Vezérlők

| Vezérlő | Alapértelmezés | Mit csinál |
|---|---|---|
| **Célfrekvencia MHz** | 144 | Az előrejelzés frekvenciája (28–1300 MHz) |
| **λ^k kitevő** | 3 | A frekvenciaszabály k kitevője (SM6FHZ: 3) |
| **K állomástényező** | 1 | A vevőállomást veszi figyelembe (teljesítmény, antennák); egy ugyanazon a sávon dolgozó RMOB-megfigyelővel való összehasonlításból vezethető le |
| **RMOB-fájl betöltése lemezről...** | | Beolvas egy havi RMOB szövegfájlt (lásd alább) |
| **A kitevő levezetése az RMOB-fájlból** | | A Collm és az RMOB közös óráiból illeszti a k értékét |
| **RMOB-megfigyelő** | üres | A megfigyelő neve úgy, ahogy a fájlnévben szerepel (pl. `NAME_112026rmob.TXT` → `NAME`) |
| **RMOB letöltése most** | | Egyszer letölti az adott megfigyelő aktuális havi fájlját |
| **automatikus letöltés 5 percenként (csak az RMOB engedélyével kapcsolja be)** | **ki** | Lásd [Az RMOB és az automatikus programok](#az-rmob-és-az-automatikus-programok) |

A vezérlők alatti narancs sor a szabályt az aktuális számokkal mutatja, pl. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, valamint az időtartam skálázását és az adott frekvencián érvényes IARU legnagyobb pingidőtartamot.

## A radartól az amatőrsávig

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Forrás:** SM6FHZ, *„432 MHz Meteorscatter, Challenges and Techniques”*, 45. Nordic VUSHF, 2025. május – a visszaverődések száma és intenzitása **λ³**-nel, időtartamuk **λ²**-tel skálázódik (a 432 MHz 14–15 dB-lel a 144 MHz alatt van, és 1/9-ed ideig tart). **Ellenőrzés:** a λ³-függés ugyanaz, mint McKinley alulsűrű egyenletében. k = 3 mellett a Collmban mért 1000 meteor/óra kb. **16 visszaverődés/órának felel meg 144 MHz-en**; a GRAVES-t 143,050 MHz-en hallgató RMOB-megfigyelők általában **20–140 visszhangot számolnak óránként** (RMOB-közlöny, 2018. június): a nagyságrend összeegyeztethető, a különbség a K állomástényező. (Kézikönyv, 44–45. egyenlet.)

## A következő 24 óra

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Perzisztencia:** az előző nap (vagy ha hiányzik, két nappal korábbi nap) ugyanazon órájának skálázott értéke, az **útvonal rajindexének** (I, Σ ZHR × hatékonyság, lásd [Hatékonyság számítása](Efficiency-Calculation-hu#a-modell)) változásával korrigálva. A 10-es állandó a sporadikus hátteret képviseli, és korlátozza a korrekciót, ha az index kicsi. *A program választása (kézikönyv, 47. egyenlet).*

| Panel | Tartalom |
|---|---|
| **Collm-ban mérve és f MHz-re skálázva – tegnap és ma (UTC)** | A Collm radar meteor/óra értékei; skálázott értékek (narancs, jobb skála); az RMOB-számok, ha be vannak töltve (zöld, jobb skála) |
| **Kísérleti előrejelzés a következő 24 órára f MHz-en, … számára** | Előrejelzett visszaverődés/óra (oszlopok) és az útvonal rajindexe (jobb skála) |
| Táblázat | UTC idő · Collm, ugyanabban az órában · Skálázott · Az útvonal rajindexe · Előrejelzés /óra · **Értékelés** |

**Értékelés:** *jó*, ha az előrejelzés legalább a 24 órás átlag 1,3-szerese, *közepes* 0,8-szorostól, *gyenge* ez alatt. Ugyanez az előrejelzés jelenik meg a **KÍSÉRLETI ELŐREJELZÉS** kártyán és a [Hatékonyság számítása](Efficiency-Calculation-hu) fül narancs sorában, és ez az alapja a várható visszhangoknak a [GRAVES radar](GRAVES-Radar-hu#várható-visszhangok-kísérleti) fülön.

## RMOB-összehasonlítás

Az [RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) a rádiós megfigyelők óránkénti meteorszámait gyűjti; Olaszországban sokan a GRAVES-t hallgatják 143,050 MHz-en (Velencei Planetárium, Faenza, Rovereto és mások).

**RMOB-fájlok beolvasása.** Két szövegformátumot fogad el:

| Formátum | Kinézet | Megjegyzés |
|---|---|---|
| Havi fájl (Colorgramme / Spectrum Lab) | naponta egy sor, `day| n| n| …` 24 óránkénti értékkel | a szokásos `NAME_MMYYYYrmob.TXT` |
| Közlöny-táblázat | fejléc ` UT |  1   2   3 …`, sorok `0h|175 166 …` | ha a fájl több megfigyelőt tartalmaz, egymás után olvassa be őket: használjon egyetlen megfigyelőt tartalmazó fájlt |

A hónapot és az évet a fájlnévből (`…_MMYYYYrmob…`) vagy a fejlécből veszi; ha ez nem lehetséges, az aktuális hónapot használja (és ezt jelzi is).

**A kitevő illesztése.** K = 1 mellett, az RMOB/Collm arányok mediánjából a közös órákon (legalább 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*A program választása (kézikönyv, 46. egyenlet).* A párbeszédablak megmutatja a közös órákat, az arány mediánját és a k értékét; az **Igen** alkalmazza a k-t (és K = 1-et állít be), a **Nem** megtartja a k = 3-at – ekkor kézzel állítsa be a K-t az ugyanebben a párbeszédablakban javasolt értékre.

## Az RMOB és az automatikus programok

Az RMOB azt kéri, hogy **automatikus programok ne töltsék le a fájljait**. Ezért az **automatikus letöltés** induláskor **ki van kapcsolva**, és **csak az RMOB engedélyének kikérése után** szabad bekapcsolni. Enélkül bármikor használhatja az **RMOB-fájl betöltése lemezről...** lehetőséget, vagy megnyomhatja az **RMOB letöltése most** gombot, amikor szüksége van rá.

A letöltési cím egy sablon a `config.ini` fájlban (`rmob_url` kulcs, alapértelmezés `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, ahol `{NOME}` a megfigyelő, `{MMAAAA}` a hónap és az év); a letöltött fájlok a `data/radar/` mappában maradnak.
