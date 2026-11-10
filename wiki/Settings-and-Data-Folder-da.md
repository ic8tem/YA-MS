[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-BR) · **Dansk** · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Ελληνικά](Settings-and-Data-Folder-el) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [ไทย](Settings-and-Data-Folder-th) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh) · [中文 (繁體)](Settings-and-Data-Folder-zh-TW)

# Indstillinger og datamappe

## Fanelinjen

I højre ende af fanelinjen, fra højre mod venstre:

| Element | Hvad det gør |
|---|---|
| **Sprog** (liste) | Brugerfladens sprog; se [Sprog](#sprog) |
| **Tema** (liste) | Farveskema; se [Farveskemaer](#farveskemaer) |
| **Betjening ▴ / ▾** | Folder de tre rækker betjeningselementer over fanerne sammen eller ud; se [Skrifttype og Betjening](#skrifttype-og-betjening) |

Når du skifter sprog eller tema, gemmes indstillingerne, og **vinduet genopbygges** i samme position og størrelse på samme fane: ingen genstart er nødvendig.

## Sprog

36 sprog i brugerfladen, de samme som i YAEC og E-LAYER ANALYZER (termer, der er fælles med YAEC, er oversat på samme måde):

| Sprog | Kode | Fil |
|---|---|---|
| Italiano | `it` | ingen: italiensk er grundsproget (nøglerne) |
| English | `en` | `data/lingue/en.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Français | `fr` | `data/lingue/fr.txt` |
| Español | `es` | `data/lingue/es.txt` |
| Português (Portugal) | `pt` | `data/lingue/pt.txt` |
| Português (Brasil) | `pt-BR` | `data/lingue/pt-BR.txt` |
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
| 中文 (繁體) | `zh-TW` | `data/lingue/zh-TW.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| 한국어 | `ko` | `data/lingue/ko.txt` |

Ved første opstart bruger YA-MS **systemets sprog**, hvis det er et af disse, ellers italiensk. Tal og datoer følger det valgte sprog (fx decimalpunktum på engelsk, komma på italiensk og tysk). Tekst, der mangler i en oversættelsesfil, vises på italiensk. På Linux kræver kinesisk, japansk, koreansk, arabisk, hebraisk, urdu, hindi og bengali passende skrifttyper (fx Noto-familierne): se [Fejlfinding](Troubleshooting-FAQ-da#linux-japansk-tekst-vises-som-firkanter).

Dokumentet [Effektivitet - forklaring](Efficiency-Explanation-da) følger brugerfladens sprog; beregningsmanualen ligger i `doc/` (italiensk) og `doc/manuali/` (de øvrige 35 sprog).

## Farveskemaer

Listen **Tema** tilbyder 12 skemaer, de samme som i forfatterens EME-program YAEC plus den oprindelige YA-MS-palet:

| Skema | Beskrivelse |
|---|---|
| **Lys** | standard |
| **Nat** | mørkeblå toner til brug om natten |
| **Sort** | sort baggrund, til mørke og til OLED-skærme |
| Pastel lyseblå · Pastel orange · Pastel akvamarin · Pastel grøn · Pastel lyserød · Pastel lilla · Pastel indigo · Pastel brun | otte lyse pastelskemaer |
| **Meteorspor** | den oprindelige YA-MS-stil (op til version 1.2.0): natteviolet med lyseblå, violet, lysegrøn, gul og orange |

Skemaet gælder for alle faner og gemmes i `config.ini` (nøglen `tema`).

## Skrifttype og Betjening

- **Skrifttype** (i slutningen af første række betjeningselementer): forstørrer **al tekst** fra **100 til 300 %** i trin på 10 %; linjer, cirkler og kort beholder deres størrelse. Med store skrifttyper brydes fanerne over på en ekstra linje, og boksene vokser.
- **Betjening**: med store skrifttyper eller en lille skærm kan du folde de tre rækker betjeningselementer sammen for at give plads til kort og grafer. Tilstanden huskes.

## Datamappe

Alle data og indstillinger ligger i én enkelt **`data`**-mappe **ved siden af programmet** – ingen AppData, ingen systemmapper:

| System | Program | Data |
|---|---|---|
| Windows (installationsprogram) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (portabel) | hvor du pakkede det ud | `data` ved siden af `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (ved siden af appen) |

Ved opstart opretter programmet mappen om nødvendigt og kopierer kun de **manglende** startfiler: filer, du har ændret, overskrives aldrig. Oversættelsesfilerne i `data/lingue` er programfiler og udskiftes, når den nye versions filer er nyere.

### Filer, du kan redigere

| Fil | Indhold |
|---|---|
| `sciami.csv` | Sværmkatalog (IMO-værdier og arbejdsværdier); se [Sværme](Showers-da#redigering-af-kataloget) |
| `massimi_imo.csv` | Datoer og tidspunkter for maksima publiceret af IMO (2026, 2027): **tilføj nye år** her |
| `ant_radiante.csv` | Antihelion-kildens position (IMO's tabel 6) |
| `fonti_radar.csv` | Radaradresser; `attivo=1` henter, `0` ignorerer |
| `regole_sperimentali.csv` | Anvendte konstanter og regler, hver med sin kilde (reference) |
| `lingue/<code>.txt` | Oversættelser af brugerfladen; se [Bidrag](Contributing-and-Contacts-da#oversættelser) |
| `config.ini` | Indstillinger (se nedenfor) |

### Filer oprettet af programmet

| Fil / mappe | Indhold |
|---|---|
| `config.ini` | Indstillinger |
| `flusso_collm.csv` | Timearkiv med Collm-fluxen |
| `quote_collm.csv` | Arkiv med sporhøjderne |
| `radar/` | Seneste radarbilleder og RMOB-filer |
| `mappa/` | Kystlinjer og grænser fra Natural Earth (hentes ved første opstart) |
| `adif_quadrati.csv` | Felter fra den senest indlæste ADIF |
| `efficienza_spiegazione.txt`, `.docx` | [Forklaringsdokumentet](Efficiency-Explanation-da) |

## config.ini

Almindelig tekst, én `key=value` pr. linje (linjer, der begynder med `#` eller `;`, er kommentarer). Programmet skriver filen, når det lukkes, så **redigér den, mens YA-MS er lukket**. De nøgler, du måske vil kende:

| Nøgle | Standard | Betydning |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Din lokator og højde (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Modstationens lokator og højde (m) |
| `banda_MHz` | 144 | Bånd (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Sporhøjde (km); 1 = brug Collm-typetallet |
| `elevazione_lobo_gradi` | 0 | Lapelevation (°) |
| `boom_m` | 4.6 | Yagi'ens bomlængde (m) |
| `hot_spot_km` | 150 | Afstand fra Hot A / Hot B til midtpunktet (30–400 km) |
| `lingua` | system / `it` | Sprogkode (en af de 36 koder ovenfor, fx `it`, `en`, `de`) |
| `tema` | `chiaro` | Farveskema: `chiaro` (Lys), `scuro` (Nat), `nero` (Sort), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Meteorspor) |
| `carattere_pct` | 100 | Skriftstørrelse (100–300 %) |
| `comandi_visibili` | 1 | 1 = rækker af betjeningselementer vises, 0 = sammenfoldet |
| `mostra_mappa`, `vista_alto` | 1, 1 | Europakort, set ovenfra i himmelkuplen |
| `aggiornamento_automatico` | 1 | Automatisk kontrol af kilderne hvert 5. minut |
| `esponente_lambda` | 3 | λ-eksponent i fanen Radarflux |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Inddata til linkbudgettet |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Eksperimentel prognose: frekvens, k, K |
| `rmob_osservatore` | tom | Navnet på RMOB-observatøren |
| `rmob_automatico` | 0 | Automatisk hentning fra RMOB (aktivér kun med tilladelse fra RMOB) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Skabelon for RMOB-adressen |
| `graves_sequenza` | 0 | GRAVES-strålesekvens: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Privatliv

YA-MS indsamler ingen data og viser ingen reklamer. Det forbinder kun til internettet for at hente offentlige data: radarbillederne fra Collm og Sodankylä, Natural Earth-kortet (første opstart) og, hvis du beder om det, en RMOB-fil.
