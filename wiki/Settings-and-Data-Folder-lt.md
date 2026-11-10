[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · **Lietuvių** · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Ελληνικά](Settings-and-Data-Folder-el) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh) · [中文 (繁體)](Settings-and-Data-Folder-zh-tw)

# Nustatymai ir duomenų aplankas

## Kortelių juosta

Kortelių juostos dešiniajame gale, iš dešinės į kairę:

| Valdiklis | Ką daro |
|---|---|
| **Kalba** (sąrašas) | Sąsajos kalba; žr. [Kalba](#kalba) |
| **Tema** (sąrašas) | Spalvų schema; žr. [Spalvų schemos](#spalvų-schemos) |
| **Valdymas ▴ / ▾** | Suskleidžia arba išskleidžia tris valdymo eilutes virš kortelių; žr. [Šriftas ir valdymas](#šriftas-ir-valdymas) |

Pakeitus kalbą ar temą, nustatymai išsaugomi, o **langas perkuriamas** toje pačioje vietoje ir tokio paties dydžio, toje pačioje kortelėje: paleisti iš naujo nereikia.

## Kalba

Šešios sąsajos kalbos:

| Kalba | Kodas | Failas |
|---|---|---|
| Italiano | `it` | nėra: italų kalba yra bazinė (raktai) |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

Pirmą kartą paleista YA-MS naudoja **sistemos kalbą**, jei ji yra viena iš šių, kitu atveju – italų. Skaičiai ir datos atitinka pasirinktą kalbą (pvz., dešimtainis taškas anglų, kablelis italų ir vokiečių kalbomis). Jei vertimo faile teksto trūksta, jis rodomas itališkai. Linux sistemoje japonų kalbai reikia tinkamų šriftų: žr. [Trikčių šalinimas](Troubleshooting-FAQ-lt#linux-japoniškas-tekstas-rodomas-kvadratėliais).

Dokumentas [Efektyvumas - paaiškinimas](Efficiency-Explanation-lt) ir skaičiavimų vadovas yra italų kalba.

## Spalvų schemos

Sąraše **Tema** yra 12 schemų – tos pačios kaip autoriaus EME programoje YAEC, ir originali YA-MS paletė:

| Schema | Aprašymas |
|---|---|
| **Šviesi** | numatytoji |
| **Naktis** | tamsiai mėlyni tonai, naudoti naktį |
| **Juoda** | juodas fonas, tamsai ir OLED ekranams |
| Pastelinė žydra · Pastelinė oranžinė · Pastelinė akvamarino · Pastelinė žalia · Pastelinė rožinė · Pastelinė alyvinė · Pastelinė indigo · Pastelinė ruda | aštuonios šviesios pastelinės schemos |
| **Meteoro pėdsakas** | originalus YA-MS stilius (iki 1.2.0 versijos): naktinė violetinė su žydra, violetine, šviesiai žalia, geltona ir oranžine |

Schema taikoma visoms kortelėms ir išsaugoma `config.ini` (raktas `tema`).

## Šriftas ir valdymas

- **Šriftas** (pirmosios valdymo eilutės gale): padidina **visą tekstą** nuo **100 iki 300 %** 10 % žingsniais; linijos, apskritimai ir žemėlapiai išlaiko savo dydį. Su dideliu šriftu kortelės persikelia į antrą eilutę, o skydeliai padidėja.
- **Valdymas**: su dideliu šriftu ar mažu ekranu suskleiskite tris valdymo eilutes, kad liktų vietos žemėlapiams ir grafikams. Būsena įsimenama.

## Duomenų aplankas

Visi duomenys ir nustatymai yra viename **`data`** aplanke **šalia programos** – jokio AppData, jokių sisteminių aplankų:

| Sistema | Programa | Duomenys |
|---|---|---|
| Windows (diegimo programa) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (nešiojamoji) | ten, kur išskleidėte | `data` šalia `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (šalia programos) |

Paleidžiant programa prireikus sukuria aplanką ir nukopijuoja tik **trūkstamus** pradinius failus: jūsų pakeisti failai niekada neperrašomi. Vertimų failai aplanke `data/lingue` yra programos failai ir pakeičiami, kai naujos versijos failai yra naujesni.

### Failai, kuriuos galite redaguoti

| Failas | Turinys |
|---|---|
| `sciami.csv` | Srautų katalogas (IMO vertės ir darbinės vertės); žr. [Srautai](Showers-lt#katalogo-redagavimas) |
| `massimi_imo.csv` | IMO paskelbtos maksimumų datos ir laikai (2026, 2027): **naujus metus pridėkite čia** |
| `ant_radiante.csv` | Antihelio šaltinio padėtis (IMO 6 lentelė) |
| `fonti_radar.csv` | Radarų adresai; `attivo=1` atsisiunčia, `0` ignoruoja |
| `regole_sperimentali.csv` | Naudojamos konstantos ir taisyklės, kiekviena su šaltiniu (informacija) |
| `lingue/<code>.txt` | Sąsajos vertimai; žr. [Prisidėjimas](Contributing-and-Contacts-lt#vertimai) |
| `config.ini` | Nustatymai (žr. toliau) |

### Programos sukuriami failai

| Failas / aplankas | Turinys |
|---|---|
| `config.ini` | Nustatymai |
| `flusso_collm.csv` | Collm srauto valandinis archyvas |
| `quote_collm.csv` | Pėdsakų aukščių archyvas |
| `radar/` | Naujausi radarų vaizdai ir RMOB failai |
| `mappa/` | Natural Earth pakrantės ir sienos (atsisiunčiamos pirmą kartą paleidžiant) |
| `adif_quadrati.csv` | Paskutinio įkelto ADIF kvadratai |
| `efficienza_spiegazione.txt`, `.docx` | [Paaiškinimo dokumentas](Efficiency-Explanation-lt) |

## config.ini

Paprastas tekstas, po vieną `key=value` eilutėje (eilutės, prasidedančios `#` arba `;`, yra komentarai). Programa jį įrašo užsidarydama, todėl **redaguokite jį, kai YA-MS uždaryta**. Raktai, kuriuos verta žinoti:

| Raktas | Numatytasis | Reikšmė |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Jūsų lokatorius ir aukštis (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Korespondento lokatorius ir aukštis (m) |
| `banda_MHz` | 144 | Juosta (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Pėdsakų aukštis (km); 1 = naudoti Collm modą |
| `elevazione_lobo_gradi` | 0 | Lapelio elevacija (°) |
| `boom_m` | 4.6 | Yagi strėlės ilgis (m) |
| `hot_spot_km` | 150 | Hot A / Hot B atstumas nuo vidurio taško (30–400 km) |
| `lingua` | sistemos / `it` | Kalbos kodas (`it`, `en`, `ru`, `ja`, `de`, `nl`) |
| `tema` | `chiaro` | Spalvų schema: `chiaro` (Šviesi), `scuro` (Naktis), `nero` (Juoda), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Meteoro pėdsakas) |
| `carattere_pct` | 100 | Šrifto dydis (100–300 %) |
| `comandi_visibili` | 1 | 1 = valdymo eilutės rodomos, 0 = suskleistos |
| `mostra_mappa`, `vista_alto` | 1, 1 | Europos žemėlapis, vaizdas iš viršaus Dangaus skliaute |
| `aggiornamento_automatico` | 1 | Automatinis šaltinių tikrinimas kas 5 minutes |
| `esponente_lambda` | 3 | λ rodiklis kortelėje Radaro srautas |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Ryšio biudžeto įvesties duomenys |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Eksperimentinė prognozė: dažnis, k, K |
| `rmob_osservatore` | tuščia | RMOB stebėtojo vardas |
| `rmob_automatico` | 0 | Automatinis RMOB atsisiuntimas (įjungti tik gavus RMOB leidimą) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | RMOB adreso šablonas |
| `graves_sequenza` | 0 | GRAVES pluošto seka: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Privatumas

YA-MS nerenka jokių duomenų ir nerodo reklamų. Prie interneto ji jungiasi tik viešiems duomenims atsisiųsti: Collm ir Sodankylä radarų vaizdams, Natural Earth žemėlapiui (pirmą kartą paleidžiant) ir, jei to paprašote, RMOB failui.
