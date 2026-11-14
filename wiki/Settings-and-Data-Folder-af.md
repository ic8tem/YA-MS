[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Ελληνικά](Settings-and-Data-Folder-el) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · **Afrikaans** · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [ไทย](Settings-and-Data-Folder-th) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh) · [中文 (繁體)](Settings-and-Data-Folder-zh-tw)

# Instellings en datagids

## Die oortjie Instellings

Die oortjie Instellings versamel die algemene werking van die program: Voorkoms (lettertipe, tema en taal), Programbywerkings (kontrole op GitHub by begin en elke 30 minute, outomatiese stil bywerkings, Kontroleer nou), Regstreekse bronne (outomatiese bywerking elke 5 minute), RMOB (waarnemer, laai nou af en outomatiese haal) en Program (opdragrye en datavouer). Die berekeningsparameters bly in die opdragrye bo die oortjies.

## Die oortjiebalk

Aan die regterkant van die oortjiebalk, van regs na links:

| Kontrole | Wat dit doen |
|---|---|
| **Taal** (lys) | Koppelvlaktaal; sien [Taal](#taal) |
| **Tema** (lys) | Kleurskema; sien [Kleurskemas](#kleurskemas) |
| **Kontroles ▴ / ▾** | Vou die twee rye kontroles bo die oortjies weg of oop; sien [Lettertipe en Kontroles](#lettertipe-en-kontroles) |

As jy die taal of tema verander, word die instellings gestoor en die **venster herbou** in dieselfde posisie en grootte, op dieselfde oortjie: geen herbegin is nodig nie.

## Taal

36 koppelvlaktale, dieselfde as dié van YAEC en E-LAYER ANALYZER (terme wat met YAEC gedeel word, word op dieselfde manier vertaal):

| Taal | Kode | Lêer |
|---|---|---|
| Italiano | `it` | geen: Italiaans is die basistaal (die sleutels) |
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

By die eerste opstart gebruik YA-MS die **stelseltaal** as dit een van hierdie is, anders Italiaans. Getalle en datums volg die gekose taal (bv. desimale punt in Engels, komma in Italiaans en Duits). Enige teks wat in 'n vertaallêer ontbreek, word in Italiaans gewys. Op Linux het Chinees, Japannees, Koreaans, Arabies, Hebreeus, Oerdoe, Hindi en Bengaals geskikte lettertipes nodig (bv. die Noto-families): sien [Probleemoplossing](Troubleshooting-FAQ-af#linux-japannese-teks-verskyn-as-blokkies).

Die dokument [Verduideliking van die doeltreffendheidsberekening](Efficiency-Explanation-af) volg die koppelvlaktaal; die berekeningshandleiding is in `doc/` (Italiaans) en `doc/manuali/` (die ander 35 tale).

## Kleurskemas

Die lys **Tema** bied 12 skemas, dieselfde as dié van die outeur se EME-program YAEC plus die oorspronklike YA-MS-palet:

| Skema | Beskrywing |
|---|---|
| **Lig** | verstek |
| **Nag** | donkerblou tone, vir gebruik in die nag |
| **Swart** | swart agtergrond, vir die donker en vir OLED-skerms |
| Pastel-ligblou · Pastel-oranje · Pastel-akwamaryn · Pastel-groen · Pastel-pienk · Pastel-lila · Pastel-indigo · Pastel-bruin | agt ligte pastelskemas |
| **Meteoorspoor** | die oorspronklike YA-MS-styl (tot weergawe 1.2.0): nagviolet met ligblou, violet, liggroen, geel en oranje |

Die skema geld vir al die oortjies en word in `config.ini` gestoor (sleutel `tema`).

## Lettertipe en Kontroles

- **Lettertipe** (Instellings): vergroot **al die teks** van **85 tot 140 %** in stappe van 5 %; lyne, sirkels en kaarte behou hul grootte. Met groot lettertipes loop die oortjies oor na 'n tweede reël en word die kaarte groter.
- **Kontroles**: met groot lettertipes of 'n klein skerm, vou die twee rye kontroles weg om plek te maak vir kaarte en grafieke. Die toestand word onthou.

## Datagids

Alle data en instellings is in 'n enkele **`data`**-gids **langs die program** – geen AppData, geen stelselgidse nie:

| Stelsel | Program | Data |
|---|---|---|
| Windows (installeerder) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (draagbaar) | waar jy dit uitgepak het | `data` langs `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (langs die app) |

By opstart skep die program die gids indien nodig en kopieer slegs die **ontbrekende** beginlêers: lêers wat jy verander het, word nooit oorskryf nie. Vertaallêers in `data/lingue` is programlêers en word vervang wanneer die nuwe weergawe se lêers meer onlangs is.

### Lêers wat jy kan wysig

| Lêer | Inhoud |
|---|---|
| `sciami.csv` | Swermkatalogus (IMO-waardes en werkwaardes); sien [Swerms](Showers-af#die-katalogus-wysig) |
| `massimi_imo.csv` | Datums en tye van die maksimums soos deur die IMO gepubliseer (2026, 2027): **voeg nuwe jare** hier by |
| `ant_radiante.csv` | Posisie van die Antihelion-bron (IMO-tabel 6) |
| `fonti_radar.csv` | Radaradresse; `attivo=1` laai af, `0` ignoreer |
| `regole_sperimentali.csv` | Konstantes en reëls wat gebruik word, elkeen met sy bron (verwysing) |
| `lingue/<code>.txt` | Koppelvlakvertalings; sien [Bydra](Contributing-and-Contacts-af#vertalings) |
| `config.ini` | Instellings (sien hieronder) |

### Lêers wat die program skep

| Lêer / gids | Inhoud |
|---|---|
| `config.ini` | Instellings |
| `flusso_collm.csv` | Uurlikse argief van die Collm-vloed |
| `quote_collm.csv` | Argief van die spoorhoogtes |
| `radar/` | Jongste radarbeelde en RMOB-lêers |
| `mappa/` | Natural Earth-kuslyne en -grense (by die eerste opstart afgelaai) |
| `adif_quadrati.csv` | Vierkante uit die laaste gelaaide ADIF |
| `efficienza_spiegazione.txt`, `.docx` | Die [verduidelikingsdokument](Efficiency-Explanation-af) |
| `backup/` | Kopieë van programlêers wat deur 'n bywerking vervang is (een vouer per weergawe) |
| `aggiornamento/` | Pakket afgelaai tydens 'n bywerking (by die volgende begin geskrap) |

## config.ini

Gewone teks, een `sleutel=waarde` per reël (reëls wat met `#` of `;` begin, is kommentaar). Die program skryf dit wanneer dit sluit, so **wysig dit terwyl YA-MS gesluit is**. Die sleutels wat jy dalk wil ken:

| Sleutel | Verstek | Betekenis |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Jou lokator en hoogte (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Lokator en hoogte van die DX-stasie (m) |
| `banda_MHz` | 144 | Band (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Spoorhoogte (km); 1 = gebruik die Collm-modus |
| `elevazione_lobo_gradi` | 0 | Lob-elevasie (°) |
| `boom_m` | 4.6 | Boomlengte van die Yagi (m) |
| `hot_spot_km` | 150 | Afstand van Hot A / Hot B vanaf die middelpunt (30–400 km) |
| `lingua` | stelsel / `it` | Taalkode (een van die 36 kodes hierbo, bv. `it`, `en`, `de`) |
| `tema` | `chiaro` | Kleurskema: `chiaro` (Lig), `scuro` (Nag), `nero` (Swart), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Meteoorspoor) |
| `carattere_pct` | 100 | Lettergrootte (85–140 %) |
| `comandi_visibili` | 1 | 1 = rye kontroles gewys, 0 = weggevou |
| `mostra_mappa`, `vista_alto` | 1, 1 | Kaart van Europa, bo-aansig in die hemelkoepel |
| `aggiornamento_automatico` | 1 | Outomatiese kontrole van die bronne elke 5 minute |
| `esponente_lambda` | 3 | λ-eksponent in die oortjie Radarvloed |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Invoere vir die skakelbegroting |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Eksperimentele voorspelling: frekwensie, k, K |
| `rmob_osservatore` | leeg | Naam van die RMOB-waarnemer |
| `rmob_automatico` | 0 | Outomatiese RMOB-aflaai (skakel slegs aan met RMOB se toestemming) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Sjabloon vir die RMOB-adres |
| `graves_sequenza` | 0 | GRAVES-bundelvolgorde: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |
| `controlla_aggiornamenti` | 1 | Soek by die begin op GitHub na nuwe weergawes (een keer per dag); 0 = nee |
| `aggiornamenti_salta` | leeg | Weergawe waarvoor jy *Slaan hierdie weergawe oor* gekies het |

## Privaatheid

YA-MS versamel geen data nie en wys geen advertensies nie. Dit koppel slegs aan die internet om publieke data af te laai: die Collm- en Sodankylä-radarbeelde, die Natural Earth-kaart (eerste opstart) en, as jy daarvoor vra, 'n RMOB-lêer.
