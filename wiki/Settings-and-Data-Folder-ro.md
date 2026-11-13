[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · **Română** · [Ελληνικά](Settings-and-Data-Folder-el) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [ไทย](Settings-and-Data-Folder-th) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh) · [中文 (繁體)](Settings-and-Data-Folder-zh-tw)

# Setări și dosarul de date

## Bara de file

La capătul din dreapta al barei de file, de la dreapta la stânga:

| Comandă | Ce face |
|---|---|
| **Limba** (listă) | Limba interfeței; vedeți [Limba](#limba) |
| **Temă** (listă) | Schema de culori; vedeți [Scheme de culori](#scheme-de-culori) |
| **Comenzi ▴ / ▾** | Pliază sau desfășoară cele trei rânduri de comenzi de deasupra filelor; vedeți [Font și comenzi](#font-și-comenzi) |

Schimbarea limbii sau a temei salvează setările și **reconstruiește fereastra** în aceeași poziție și la aceeași dimensiune, pe aceeași filă: nu este nevoie de repornire.

## Limba

36 de limbi ale interfeței, aceleași ca în YAEC și E-LAYER ANALYZER (termenii comuni cu YAEC sunt traduși la fel):

| Limbă | Cod | Fișier |
|---|---|---|
| Italiano | `it` | niciunul: italiana este limba de bază (cheile) |
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

La prima pornire, YA-MS folosește **limba sistemului** dacă este una dintre acestea, altfel italiana. Numerele și datele urmează limba aleasă (de ex. punct zecimal în engleză, virgulă în italiană, germană și română). Orice text care lipsește dintr-un fișier de traducere este afișat în italiană. Pe Linux, chineza, japoneza, coreeana, araba, ebraica, urdu, hindi și bengali au nevoie de fonturi potrivite (de ex. familiile Noto): vedeți [Rezolvarea problemelor](Troubleshooting-FAQ-ro#linux-textul-japonez-apare-ca-pătrățele).

Documentul [Explicația calculului eficienței](Efficiency-Explanation-ro) urmează limba interfeței; manualul de calcul se află în `doc/` (italiană) și `doc/manuali/` (celelalte 35 de limbi).

## Scheme de culori

Lista **Temă** oferă 12 scheme, aceleași ca în programul EME al autorului, YAEC, plus paleta originală YA-MS:

| Schemă | Descriere |
|---|---|
| **Luminos** | implicit |
| **Noapte** | tonuri de albastru închis, pentru utilizare noaptea |
| **Negru** | fundal negru, pentru întuneric și pentru ecrane OLED |
| Pastel bleu · Pastel portocaliu · Pastel acvamarin · Pastel verde · Pastel roz · Pastel lila · Pastel indigo · Pastel maro | opt scheme pastelate deschise |
| **Urmă de meteor** | stilul original YA-MS (până la versiunea 1.2.0): violet de noapte cu bleu, violet, verde deschis, galben și portocaliu |

Schema se aplică tuturor filelor și este salvată în `config.ini` (cheia `tema`).

## Font și comenzi

- **Font** (la capătul primului rând de comenzi): mărește **întregul text** de la **85 la 140 %** în pași de 5 %; liniile, cercurile și hărțile își păstrează dimensiunea. Cu fonturi mari, filele trec pe un al doilea rând, iar cardurile cresc.
- **Comenzi**: cu fonturi mari sau un ecran mic, pliați cele trei rânduri de comenzi pentru a lăsa loc hărților și graficelor. Starea este memorată.

## Dosarul de date

Toate datele și setările se află într-un singur dosar **`data`** **lângă program** – fără AppData, fără dosare de sistem:

| Sistem | Program | Date |
|---|---|---|
| Windows (program de instalare) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (portabil) | unde l-ați extras | `data` lângă `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (lângă aplicație) |

La pornire, programul creează dosarul dacă este necesar și copiază doar fișierele inițiale **care lipsesc**: fișierele pe care le-ați modificat nu sunt niciodată suprascrise. Fișierele de traducere din `data/lingue` sunt fișiere ale programului și sunt înlocuite când fișierele noii versiuni sunt mai recente.

### Fișiere pe care le puteți edita

| Fișier | Conținut |
|---|---|
| `sciami.csv` | Catalogul roiurilor (valori IMO și valori de lucru); vedeți [Roiuri](Showers-ro#editarea-catalogului) |
| `massimi_imo.csv` | Datele și orele maximelor publicate de IMO (2026, 2027): **adăugați anii noi** aici |
| `ant_radiante.csv` | Poziția Sursei Antihelion (tabelul IMO 6) |
| `fonti_radar.csv` | Adresele radarelor; `attivo=1` descarcă, `0` ignoră |
| `regole_sperimentali.csv` | Constantele și regulile folosite, fiecare cu sursa sa (referință) |
| `lingue/<code>.txt` | Traducerile interfeței; vedeți [Contribuții](Contributing-and-Contacts-ro#traduceri) |
| `config.ini` | Setări (vedeți mai jos) |

### Fișiere create de program

| Fișier / dosar | Conținut |
|---|---|
| `config.ini` | Setări |
| `flusso_collm.csv` | Arhiva orară a fluxului de la Collm |
| `quote_collm.csv` | Arhiva înălțimilor urmelor |
| `radar/` | Cele mai recente imagini radar și fișierele RMOB |
| `mappa/` | Liniile de coastă și granițele Natural Earth (descărcate la prima pornire) |
| `adif_quadrati.csv` | Pătratele din ultimul ADIF încărcat |
| `efficienza_spiegazione.txt`, `.docx` | [Documentul de explicație](Efficiency-Explanation-ro) |
| `backup/` | Copii ale fișierelor programului înlocuite de o actualizare (câte un dosar pentru fiecare versiune) |
| `aggiornamento/` | Pachet descărcat în timpul unei actualizări (șters la pornirea următoare) |

## config.ini

Text simplu, câte o pereche `key=value` pe linie (liniile care încep cu `#` sau `;` sunt comentarii). Programul îl scrie la închidere, așa că **editați-l cu YA-MS închis**. Cheile pe care ați putea dori să le cunoașteți:

| Cheie | Implicit | Semnificație |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Locatorul și înălțimea dumneavoastră (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Locatorul și înălțimea stației DX (m) |
| `banda_MHz` | 144 | Banda (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Înălțimea urmei (km); 1 = folosește moda Collm |
| `elevazione_lobo_gradi` | 0 | Elevația lobului (°) |
| `boom_m` | 4.6 | Lungimea boom-ului Yagi (m) |
| `hot_spot_km` | 150 | Distanța lui Hot A / Hot B față de punctul median (30–400 km) |
| `lingua` | sistem / `it` | Codul limbii (unul dintre cele 36 de coduri de mai sus, de ex. `it`, `en`, `de`) |
| `tema` | `chiaro` | Schema de culori: `chiaro` (Luminos), `scuro` (Noapte), `nero` (Negru), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Urmă de meteor) |
| `carattere_pct` | 100 | Dimensiunea fontului (85–140 %) |
| `comandi_visibili` | 1 | 1 = rândurile de comenzi afișate, 0 = pliate |
| `mostra_mappa`, `vista_alto` | 1, 1 | Harta Europei, vederea de sus în Bolta cerească |
| `aggiornamento_automatico` | 1 | Verificarea automată a surselor la fiecare 5 minute |
| `esponente_lambda` | 3 | Exponentul λ în fila Flux radar |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Datele de intrare ale bilanțului legăturii |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Previziunea experimentală: frecvența, k, K |
| `rmob_osservatore` | gol | Numele observatorului RMOB |
| `rmob_automatico` | 0 | Descărcarea automată RMOB (activați doar cu permisiunea RMOB) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Șablonul adresei RMOB |
| `graves_sequenza` | 0 | Secvența fasciculului GRAVES: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |
| `controlla_aggiornamenti` | 1 | Căutarea versiunilor noi pe GitHub la pornire (o dată pe zi); 0 = nu |
| `aggiornamenti_salta` | gol | Versiunea pentru care ai ales *Sari peste această versiune* |

## Confidențialitate

YA-MS nu colectează date și nu afișează publicitate. Se conectează la internet doar pentru a descărca date publice: imaginile radarelor din Collm și Sodankylä, harta Natural Earth (la prima pornire) și, dacă cereți, un fișier RMOB.
