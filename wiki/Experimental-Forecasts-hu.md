[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · **Magyar** · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [ไทย](Experimental-Forecasts-th) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Kísérleti előrejelzések

*Fül: Előrejelzés-számítás › Kísérleti előrejelzések.*

[![Kísérleti előrejelzések](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Ez a fül a **collmi radar (36,2 MHz)** meteorszámait egy **amatőrsávon várható óránkénti reflexiószámmá** alakítja (alapértelmezésben 144 MHz, de bármely frekvencia 28 és 1300 MHz között), előre jelzi az Ön útvonalára a **következő 24 órát**, és lehetővé teszi, hogy a becslést **összevesse** egy **RMOB**-megfigyelővel – például olyannal, aki a GRAVES-t hallgatja 143,050 MHz-en.

> Itt minden **kísérleti**: a frekvenciaszabály tapasztalati szabály, az állomástényező pedig az Ön állomásától függ. A számokat órák és napok összehasonlítására használja, és ellenőrizze őket forgalmazás közben.

## Vezérlők

| Vezérlő | Alapértelmezés | Mire szolgál |
|---|---|---|
| **Célfrekvencia MHz** | 144 | Az előrejelzés frekvenciája (28–1300 MHz) |
| **λ^k kitevő** | 3 | A frekvenciaszabály k kitevője (SM6FHZ: 3) |
| **K állomástényező** | 1 | A vevőállomást veszi figyelembe (teljesítmény, antennák); egy azonos sávon dolgozó RMOB-megfigyelővel való összevetésből adódik |
| **RMOB-fájl betöltése lemezről...** | | Beolvas egy havi RMOB-szövegfájlt (lásd lent) |
| **A kitevő meghatározása az RMOB-fájlból** | | A Collm és az RMOB közös óráiból illeszti k-t |
| **RMOB-megfigyelő** | üres | A megfigyelő neve, ahogy a fájlnévben szerepel (pl. `NAME_112026rmob.TXT` → `NAME`) |
| **RMOB letöltése most** | | Egyszer letölti az adott megfigyelő aktuális havi fájlját |
| **automatikus letöltés 5 percenként (csak az RMOB engedélyével kapcsolja be)** | **ki** | Lásd: [RMOB és automatikus programok](#rmob-és-automatikus-programok) |

A vezérlők alatti narancs sor az aktuális számokkal mutatja a szabályt, pl. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, az időtartam skálázását és az IARU szerinti legnagyobb pinget az adott frekvencián.

## A radartól az amatőrsávig

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}\sec^2\varphi
```

**Forrás:** SM6FHZ, *„432 MHz Meteorscatter, Challenges and Techniques”*, 45. Nordic VUSHF, 2025. május – a reflexiók száma és erőssége **λ³**-nel, időtartamuk **λ²**-tel skálázódik (a 432 MHz 14–15 dB-lel a 144 MHz alatt van, és 1/9-ig tart). **Ellenőrzés:** McKinley egyenletében a λ³ egyetlen alulsűrű nyom teljesítménye, nem a nyomok száma; 2-es tömegindexnél a rögzített küszöb feletti nyomok száma nagyjából λ^1.5 szerint skálázódik (IZ5TEK; OH5IY). A program k = 3-mal számol, SM6FHZ tapasztalati szabálya szerint, és ezt jelzi is; az Ön állomásához illő k az RMOB-összehasonlításból adódik. Előreszórásban az időtartam sec²φ-vel is nő (McKinley; OH5IY): Collm visszaszórásban mér (φ = 0), ezért az előrejelzés sec²φ-vel szoroz az útvonal felezőpontjában (×4 60°-nál, ×8,5 70°-nál, ×33 80°-nál). k = 3 mellett 1000 meteor/óra Collmban kb. **16 reflexió/órának felel meg 144 MHz-en**; a GRAVES-t 143,050 MHz-en figyelő RMOB-megfigyelők általában **20–140 visszhangot/órát** számolnak (RMOB-közlöny, 2018. június): a nagyságrend összeegyeztethető, a különbség pedig a K állomástényező. (Kézikönyv, 44–45. egyenlet.)

## A következő 24 óra

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**Perzisztencia:** az előző nap (ha hiányzik, két nappal korábbi) ugyanazon órájának skálázott értéke, az **útvonal rajindexének** (I) változásával korrigálva (Σ ZHR × hatékonyság, lásd: [Hatékonyság-számítás](Efficiency-Calculation-hu#a-modell)). A 10-es állandó a sporadikus hátteret képviseli, és kis indexnél korlátozza a korrekciót. *A program döntése (kézikönyv, 47. egyenlet).*

| Panel | Tartalom |
|---|---|
| **Collmban mérve és f MHz-re skálázva – tegnap és ma (UTC)** | A collmi radar meteor/óra értékei; skálázott értékek (narancs, jobb oldali skála); az RMOB-számok, ha be vannak töltve (zöld, jobb oldali skála) |
| **Kísérleti előrejelzés a következő 24 órára f MHz-en, … számára** | Előre jelzett reflexió/óra (oszlopok) és az útvonal rajindexe (jobb oldali skála) |
| Táblázat | UTC-idő · Collm ugyanabban az órában · Skálázott · Útvonal rajindexe · Előrejelzés /óra · **Értékelés** |

**Értékelés:** *jó*, ha az előrejelzés legalább a 24 órás átlag 1,3-szorosa, *közepes* 0,8-szorostól, *gyenge* ez alatt. Ugyanez az előrejelzés jelenik meg a **KÍSÉRLETI ELŐREJELZÉS** kártyán és a [Hatékonyság-számítás](Efficiency-Calculation-hu) narancs sorában, és ez az alapja a várható visszhangoknak a [GRAVES-radar](GRAVES-Radar-hu#várható-visszhangok-kísérleti) fülön.

## Összehasonlítás az RMOB-bal

Az [RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) a rádiós megfigyelők óránkénti meteorszámait gyűjti; Olaszországban sokan a GRAVES-t hallgatják 143,050 MHz-en (Velencei Planetárium, Faenza, Rovereto és mások).

**RMOB-fájlok beolvasása.** Két szöveges formátumot fogad el:

| Formátum | Megjelenés | Megjegyzés |
|---|---|---|
| Havi fájl (Colorgramme / Spectrum Lab) | naponként egy sor, `day| n| n| …` 24 óránkénti értékkel | a szokásos `NAME_MMYYYYrmob.TXT` |
| Közlönytáblázat | fejléc: ` UT |  1   2   3 …`, sorok: `0h|175 166 …` | ha a fájl több megfigyelőt tartalmaz, egymás után olvassa be őket: használjon egyetlen megfigyelőt tartalmazó fájlt |

A hónapot és az évet a fájlnévből (`…_MMYYYYrmob…`) vagy a fejlécből veszi; ha egyik sem áll rendelkezésre, az aktuális hónapot használja (és ezt jelzi).

**A kitevő illesztése.** K = 1 mellett, az RMOB/Collm arányok mediánjából a közös órákra (legalább 3):

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*A program döntése (kézikönyv, 46. egyenlet).* A párbeszédablak mutatja a közös órákat, a medián arányt és k-t; az **Igen** alkalmazza k-t (és K = 1-et állít be), a **Nem** megtartja a k = 3-at – ekkor állítsa be kézzel K-t az ugyanabban a párbeszédablakban javasolt értékre.

## RMOB és automatikus programok

Az RMOB azt kéri, hogy **automatikus programok ne töltsék le a fájljait**. Ezért az **automatikus letöltés** induláskor **ki van kapcsolva**, és **csak az RMOB engedélyének kikérése után** szabad bekapcsolni. Enélkül bármikor használhatja az **RMOB-fájl betöltése lemezről...** gombot, vagy szükség esetén megnyomhatja az **RMOB letöltése most** gombot.

A letöltési cím egy sablon a `config.ini` fájlban (`rmob_url` kulcs, alapértelmezés: `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, ahol `{NOME}` a megfigyelő, `{MMAAAA}` pedig a hónap és az év); a letöltött fájlok a `data/radar/` mappában maradnak.
