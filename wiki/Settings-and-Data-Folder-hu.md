[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · **Magyar** · [Română](Settings-and-Data-Folder-ro) · [Ελληνικά](Settings-and-Data-Folder-el) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [ไทย](Settings-and-Data-Folder-th) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh) · [中文 (繁體)](Settings-and-Data-Folder-zh-tw)

# Beállítások és adatmappa

## A fülsor

A fülsor jobb végén, jobbról balra:

| Vezérlő | Mire szolgál |
|---|---|
| **Nyelv** (lista) | A felület nyelve; lásd: [Nyelv](#nyelv) |
| **Téma** (lista) | Színséma; lásd: [Színsémák](#színsémák) |
| **Vezérlők ▴ / ▾** | Összecsukja vagy kinyitja a fülek feletti három vezérlősort; lásd: [Betűméret és vezérlők](#betűméret-és-vezérlők) |

A nyelv vagy a téma módosítása elmenti a beállításokat, és **újraépíti az ablakot** ugyanabban a helyzetben és méretben, ugyanazon a fülön: nincs szükség újraindításra.

## Nyelv

36 felületi nyelv, ugyanazok, mint a YAEC és az E-LAYER ANALYZER esetében (a YAEC-kel közös kifejezések ugyanúgy vannak fordítva):

| Nyelv | Kód | Fájl |
|---|---|---|
| Italiano | `it` | nincs: az olasz az alapnyelv (a kulcsok) |
| English | `en` | `data/lingue/en.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Français | `fr` | `data/lingue/fr.txt` |
| Español | `es` | `data/lingue/es.txt` |
| Português (Portugal) | `pt` | `data/lingue/pt.txt` |
| Português (Brasil) | `pt-br` | `data/lingue/pt-br.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |
| Svenska | `sv` | `data/lingue/sv.txt` |
| Norsk (bokmål) | `nb` | `data/lingue/nb.txt` |
| Dansk | `da` | `data/lingue/da.txt` |
| Íslenska | `is` | `data/lingue/is.txt` |
| Eesti | `et` | `data/lingue/et.txt` |
| Latviešu | `lv` | `data/lingue/lv.txt` |
| Lietuvių | `lt` | `data/lingue/lt.txt` |
| Polski | `pl` | `data/lingue/pl.txt` |
| Čeština | `cs` | `data/lingue/cs.txt` |
| Magyar | `hu` | `data/lingue/hu.txt` |
| Română | `ro` | `data/lingue/ro.txt` |
| Ελληνικά | `el` | `data/lingue/el.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| Українська | `uk` | `data/lingue/uk.txt` |
| Türkçe | `tr` | `data/lingue/tr.txt` |
| Afrikaans | `af` | `data/lingue/af.txt` |
| العربية | `ar` | `data/lingue/ar.txt` |
| עברית | `he` | `data/lingue/he.txt` |
| اردو | `ur` | `data/lingue/ur.txt` |
| हिन्दी | `hi` | `data/lingue/hi.txt` |
| বাংলা | `bn` | `data/lingue/bn.txt` |
| ไทย | `th` | `data/lingue/th.txt` |
| Bahasa Indonesia | `id` | `data/lingue/id.txt` |
| Tagalog | `tl` | `data/lingue/tl.txt` |
| 中文 (简体) | `zh` | `data/lingue/zh.txt` |
| 中文 (繁體) | `zh-tw` | `data/lingue/zh-tw.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| 한국어 | `ko` | `data/lingue/ko.txt` |

Első indításkor a YA-MS a **rendszer nyelvét** használja, ha az ezek egyike, egyébként az olaszt. A számok és dátumok a választott nyelvet követik (pl. tizedespont angolul, tizedesvessző olaszul és németül). A fordítási fájlból hiányzó szövegek olaszul jelennek meg. Linuxon a kínai, japán, koreai, arab, héber, urdu, hindi és bengáli nyelvhez megfelelő betűtípusok kellenek (pl. a Noto családok): lásd: [Hibaelhárítás](Troubleshooting-FAQ-hu#linux-a-japán-szöveg-helyén-négyzetek-jelennek-meg).

A [Hatékonyság – magyarázat](Efficiency-Explanation-hu) dokumentum a felület nyelvét követi; a számítási kézikönyv a `doc/` mappában (olaszul) és a `doc/manuali/` mappában (a többi 35 nyelven) található.

## Színsémák

A **Téma** lista 12 sémát kínál: ugyanazokat, mint a szerző YAEC nevű EME-programja, kiegészítve az eredeti YA-MS-palettával:

| Séma | Leírás |
|---|---|
| **Világos** | alapértelmezés |
| **Éjszakai** | sötétkék árnyalatok, éjszakai használatra |
| **Fekete** | fekete háttér, sötétben és OLED-kijelzőkhöz |
| Pasztell világoskék · Pasztell narancs · Pasztell akvamarin · Pasztell zöld · Pasztell rózsaszín · Pasztell lila · Pasztell indigó · Pasztell barna | nyolc világos pasztellséma |
| **Meteornyom** | az eredeti YA-MS-stílus (az 1.2.0-s változatig): éjszakai ibolya világoskékkel, ibolyával, világoszölddel, sárgával és naranccsal |

A séma minden fülre érvényes, és a `config.ini` fájlba mentődik (`tema` kulcs).

## Betűméret és vezérlők

- **Betűméret** (a vezérlők első sorának végén): **az összes szöveget** **100 és 300 %** között nagyítja, 10 %-os lépésekben; a vonalak, körök és térképek megtartják a méretüket. Nagy betűméretnél a fülek második sorba törnek, a kártyák pedig megnőnek.
- **Vezérlők**: nagy betűméretnél vagy kis képernyőn csukja össze a három vezérlősort, hogy több hely maradjon a térképeknek és grafikonoknak. Az állapotot a program megjegyzi.

## Adatmappa

Minden adat és beállítás egyetlen **`data`** mappában van **a program mellett** – nincs AppData, nincsenek rendszermappák:

| Rendszer | Program | Adatok |
|---|---|---|
| Windows (telepítő) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (hordozható) | ahová kibontotta | `data` a `YA-MS.exe` mellett |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (az alkalmazás mellett) |

Indításkor a program szükség esetén létrehozza a mappát, és csak a **hiányzó** kiinduló fájlokat másolja be: az Ön által módosított fájlokat soha nem írja felül. A `data/lingue` mappában lévő fordítási fájlok a program részei, és lecserélődnek, ha az új változat fájljai frissebbek.

### Szerkeszthető fájlok

| Fájl | Tartalom |
|---|---|
| `sciami.csv` | Rajkatalógus (IMO-értékek és üzemi értékek); lásd: [Meteorrajok](Showers-hu#a-katalógus-szerkesztése) |
| `massimi_imo.csv` | Az IMO által közzétett csúcsdátumok és -időpontok (2026, 2027): ide **vegye fel az új éveket** |
| `ant_radiante.csv` | Az Antihelion-forrás helyzete (IMO 6. táblázat) |
| `fonti_radar.csv` | Radarcímek; `attivo=1` letölti, `0` figyelmen kívül hagyja |
| `regole_sperimentali.csv` | A használt állandók és szabályok, mindegyik a forrásával (referencia) |
| `lingue/<code>.txt` | A felület fordításai; lásd: [Közreműködés](Contributing-and-Contacts-hu#fordítások) |
| `config.ini` | Beállítások (lásd lent) |

### A program által létrehozott fájlok

| Fájl / mappa | Tartalom |
|---|---|
| `config.ini` | Beállítások |
| `flusso_collm.csv` | A collmi fluxus óránkénti archívuma |
| `quote_collm.csv` | A nyommagasságok archívuma |
| `radar/` | A legutóbbi radarképek és RMOB-fájlok |
| `mappa/` | Natural Earth partvonalak és határok (első indításkor töltődnek le) |
| `adif_quadrati.csv` | A legutóbb betöltött ADIF négyzetei |
| `efficienza_spiegazione.txt`, `.docx` | A [magyarázó dokumentum](Efficiency-Explanation-hu) |

## config.ini

Egyszerű szövegfájl, soronként egy `key=value` pár (a `#` vagy `;` karakterrel kezdődő sorok megjegyzések). A program bezáráskor írja, ezért **a YA-MS bezárt állapotában szerkessze**. A hasznos kulcsok:

| Kulcs | Alapértelmezés | Jelentés |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Saját lokátor és magasság (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | A DX-állomás lokátora és magassága (m) |
| `banda_MHz` | 144 | Sáv (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Nyommagasság (km); 1 = a collmi módusz használata |
| `elevazione_lobo_gradi` | 0 | Nyalábeleváció (°) |
| `boom_m` | 4.6 | A Yagi boomhossza (m) |
| `hot_spot_km` | 150 | Hot A / Hot B távolsága a felezőponttól (30–400 km) |
| `lingua` | rendszer / `it` | Nyelvkód (a fenti 36 kód egyike, pl. `it`, `en`, `de`) |
| `tema` | `chiaro` | Színséma: `chiaro` (Világos), `scuro` (Éjszakai), `nero` (Fekete), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Meteornyom) |
| `carattere_pct` | 100 | Betűméret (100–300 %) |
| `comandi_visibili` | 1 | 1 = a vezérlősorok láthatók, 0 = összecsukva |
| `mostra_mappa`, `vista_alto` | 1, 1 | Európa-térkép, felülnézet az égbolt-kupolán |
| `aggiornamento_automatico` | 1 | A források automatikus ellenőrzése 5 percenként |
| `esponente_lambda` | 3 | λ-kitevő a Radarfluxus fülön |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Az összeköttetési mérleg bemenetei |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Kísérleti előrejelzés: frekvencia, k, K |
| `rmob_osservatore` | üres | Az RMOB-megfigyelő neve |
| `rmob_automatico` | 0 | Automatikus RMOB-letöltés (csak az RMOB engedélyével kapcsolja be) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Az RMOB-cím sablonja |
| `graves_sequenza` | 0 | A GRAVES nyalábsorrendje: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Adatvédelem

A YA-MS nem gyűjt adatokat és nem jelenít meg reklámot. Csak nyilvános adatok letöltéséhez csatlakozik az internethez: a collmi és sodankyläi radarképekhez, a Natural Earth térképhez (első indításkor) és – ha Ön kéri – egy RMOB-fájlhoz.
