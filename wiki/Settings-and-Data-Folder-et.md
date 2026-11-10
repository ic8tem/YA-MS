[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · **Eesti** · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh)

# Seaded ja andmekaust

## Sakiriba

Sakiriba paremas otsas, paremalt vasakule:

| Juhtnupp | Mida see teeb |
|---|---|
| **Keel** (loend) | Kasutajaliidese keel; vt [Keel](#keel) |
| **Teema** (loend) | Värviskeem; vt [Värviskeemid](#värviskeemid) |
| **Juhtnupud ▴ / ▾** | Peidab või näitab sakkide kohal olevat kolme juhtnuppude rida; vt [Font ja juhtnupud](#font-ja-juhtnupud) |

Keele või teema vahetamine salvestab seaded ja **ehitab akna uuesti üles** samas asukohas ja suuruses, samal sakil: taaskäivitust pole vaja.

## Keel

Kuus kasutajaliidese keelt:

| Keel | Kood | Fail |
|---|---|---|
| Italiano | `it` | puudub: itaalia keel on põhikeel (võtmed) |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

Esimesel käivitusel kasutab YA-MS **süsteemi keelt**, kui see on üks neist, muidu itaalia keelt. Numbrid ja kuupäevad järgivad valitud keelt (nt inglise keeles kümnendpunkt, itaalia ja saksa keeles koma). Tõlkefailist puuduv tekst kuvatakse itaalia keeles. Linuxis vajab jaapani keel sobivaid fonte: vt [Tõrkeotsing](Troubleshooting-FAQ-et#linux-jaapani-tekst-kuvatakse-kastikestena).

Dokument [Efektiivsus - selgitus](Efficiency-Explanation-et) ja arvutusjuhend on itaalia keeles.

## Värviskeemid

Loend **Teema** pakub 12 skeemi, samad mis autori EME-programmis YAEC, pluss YA-MS-i algne palett:

| Skeem | Kirjeldus |
|---|---|
| **Hele** | vaikimisi |
| **Öö** | tumesinised toonid öiseks kasutamiseks |
| **Must** | must taust, pimeduse ja OLED-ekraanide jaoks |
| Pastelne helesinine · Pastelne oranž · Pastelne akvamariin · Pastelne roheline · Pastelne roosa · Pastelne lilla · Pastelne indigo · Pastelne pruun | kaheksa heledat pastelset skeemi |
| **Meteoorijälg** | YA-MS-i algne stiil (kuni versioonini 1.2.0): öine violetne koos helesinise, violetse, helerohelise, kollase ja oranžiga |

Skeem kehtib kõigil sakkidel ja salvestatakse faili `config.ini` (võti `tema`).

## Font ja juhtnupud

- **Font** (juhtnuppude esimese rea lõpus): suurendab **kogu teksti** **100 kuni 300 %** 10 % sammudega; jooned, ringid ja kaardid säilitavad oma suuruse. Suure fondi korral murduvad sakid teisele reale ja infokaardid kasvavad.
- **Juhtnupud**: suure fondi või väikese ekraani korral peida kolm juhtnuppude rida, et jätta ruumi kaartidele ja graafikutele. Olek jäetakse meelde.

## Andmekaust

Kõik andmed ja seaded on ühes **programmi kõrval** olevas kaustas **`data`** – ei AppData-t ega süsteemikaustu:

| Süsteem | Programm | Andmed |
|---|---|---|
| Windows (paigaldaja) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (kaasaskantav) | kuhu iganes selle lahti pakkisid | `data` faili `YA-MS.exe` kõrval |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (rakenduse kõrval) |

Käivitamisel loob programm vajaduse korral kausta ja kopeerib ainult **puuduvad** algfailid: sinu muudetud faile ei kirjutata kunagi üle. Kausta `data/lingue` tõlkefailid on programmifailid ja need asendatakse, kui uue versiooni failid on värskemad.

### Muudetavad failid

| Fail | Sisu |
|---|---|
| `sciami.csv` | Meteoorivoolude kataloog (IMO väärtused ja tööväärtused); vt [Meteoorivoolud](Showers-et#kataloogi-muutmine) |
| `massimi_imo.csv` | IMO avaldatud maksimumide kuupäevad ja kellaajad (2026, 2027): **lisa siia uued aastad** |
| `ant_radiante.csv` | Antiheeliumi allika asend (IMO tabel 6) |
| `fonti_radar.csv` | Radarite aadressid; `attivo=1` laadib alla, `0` ignoreerib |
| `regole_sperimentali.csv` | Kasutatud konstandid ja reeglid, igaüks koos allikaga (viide) |
| `lingue/<code>.txt` | Kasutajaliidese tõlked; vt [Kaastöö](Contributing-and-Contacts-et#tõlked) |
| `config.ini` | Seaded (vt allpool) |

### Programmi loodud failid

| Fail / kaust | Sisu |
|---|---|
| `config.ini` | Seaded |
| `flusso_collm.csv` | Collmi voo tunniarhiiv |
| `quote_collm.csv` | Jälgede kõrguste arhiiv |
| `radar/` | Viimased radaripildid ja RMOB-failid |
| `mappa/` | Natural Earthi rannajooned ja piirid (laaditakse esimesel käivitusel) |
| `adif_quadrati.csv` | Viimati laaditud ADIF-i ruudud |
| `efficienza_spiegazione.txt`, `.docx` | [Selgitusdokument](Efficiency-Explanation-et) |

## config.ini

Lihttekst, üks `key=value` rea kohta (märgiga `#` või `;` algavad read on kommentaarid). Programm kirjutab selle sulgemisel, seega **muuda seda siis, kui YA-MS on suletud**. Võtmed, mida võiksid teada:

| Võti | Vaikimisi | Tähendus |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Sinu lokaator ja kõrgus (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Korrespondendi lokaator ja kõrgus (m) |
| `banda_MHz` | 144 | Sagedusala (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Jälgede kõrgus (km); 1 = kasuta Collmi moodi |
| `elevazione_lobo_gradi` | 0 | Peaharu elevatsioon (°) |
| `boom_m` | 4.6 | Yagi poomi pikkus (m) |
| `hot_spot_km` | 150 | Hot A / Hot B kaugus keskpunktist (30–400 km) |
| `lingua` | süsteem / `it` | Keele kood (`it`, `en`, `ru`, `ja`, `de`, `nl`) |
| `tema` | `chiaro` | Värviskeem: `chiaro` (Hele), `scuro` (Öö), `nero` (Must), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Meteoorijälg) |
| `carattere_pct` | 100 | Fondi suurus (100–300 %) |
| `comandi_visibili` | 1 | 1 = juhtnuppude read nähtaval, 0 = peidetud |
| `mostra_mappa`, `vista_alto` | 1, 1 | Euroopa kaart, pealtvaade Taevavõlvis |
| `aggiornamento_automatico` | 1 | Allikate automaatne kontroll iga 5 minuti järel |
| `esponente_lambda` | 3 | λ astendaja sakil Radari voog |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Lingi eelarve sisendid |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Eksperimentaalne prognoos: sagedus, k, K |
| `rmob_osservatore` | tühi | RMOB-i vaatleja nimi |
| `rmob_automatico` | 0 | RMOB-i automaatne allalaadimine (lülita sisse ainult RMOB-i loal) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | RMOB-i aadressi mall |
| `graves_sequenza` | 0 | GRAVESi kiire järjestus: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Privaatsus

YA-MS ei kogu andmeid ega näita reklaami. See ühendub internetiga ainult avalike andmete allalaadimiseks: Collmi ja Sodankylä radaripildid, Natural Earthi kaart (esimesel käivitusel) ja soovi korral RMOB-fail.
