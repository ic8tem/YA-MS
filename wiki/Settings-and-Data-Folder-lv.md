[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · **Latviešu** · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh)

# Iestatījumi un datu mape

## Ciļņu josla

Ciļņu joslas labajā galā, no labās uz kreiso:

| Vadīkla | Ko tā dara |
|---|---|
| **Valoda** (saraksts) | Saskarnes valoda; sk. [Valoda](#valoda) |
| **Tēma** (saraksts) | Krāsu shēma; sk. [Krāsu shēmas](#krāsu-shēmas) |
| **Vadība ▴ / ▾** | Sakļauj vai izvērš trīs vadības rindas virs cilnēm; sk. [Fonts un Vadība](#fonts-un-vadība) |

Valodas vai tēmas maiņa saglabā iestatījumus un **pārbūvē logu** tajā pašā vietā un izmērā, tajā pašā cilnē: restartēšana nav vajadzīga.

## Valoda

Sešas saskarnes valodas:

| Valoda | Kods | Fails |
|---|---|---|
| Italiano | `it` | nav: itāļu valoda ir bāzes valoda (atslēgas) |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

Pirmajā palaišanā YA-MS izmanto **sistēmas valodu**, ja tā ir viena no šīm, citādi itāļu. Skaitļi un datumi seko izvēlētajai valodai (piem. decimālpunkts angļu valodā, komats itāļu un vācu valodā). Jebkurš tulkojuma failā trūkstošs teksts tiek rādīts itāliski. Linux sistēmā japāņu valodai vajadzīgi piemēroti fonti: sk. [Problēmu risināšana](Troubleshooting-FAQ-lv#linux-japāņu-teksts-redzams-kā-kvadrātiņi).

Dokuments [Efektivitāte - skaidrojums](Efficiency-Explanation-lv) un aprēķinu rokasgrāmata ir itāļu valodā.

## Krāsu shēmas

Sarakstā **Tēma** ir 12 shēmas – tās pašas, kas autora EME programmā YAEC, plus oriģinālā YA-MS palete:

| Shēma | Apraksts |
|---|---|
| **Gaišs** | noklusējums |
| **Nakts** | tumši zili toņi lietošanai naktī |
| **Melns** | melns fons tumsai un OLED ekrāniem |
| Pasteļa gaišzils · Pasteļa oranžs · Pasteļa akvamarīns · Pasteļa zaļš · Pasteļa rozā · Pasteļa ceriņu · Pasteļa indigo · Pasteļa brūns | astoņas gaišas pasteļa shēmas |
| **Meteora sliede** | oriģinālais YA-MS stils (līdz 1.2.0. versijai): nakts violets ar gaiši zilu, violetu, gaiši zaļu, dzeltenu un oranžu |

Shēma attiecas uz visām cilnēm un tiek saglabāta failā `config.ini` (atslēga `tema`).

## Fonts un Vadība

- **Fonts** (pirmās vadības rindas beigās): palielina **visu tekstu** no **100 līdz 300 %** ar 10 % soli; līnijas, apļi un kartes saglabā savu izmēru. Ar lieliem fontiem cilnes pārnesas otrā rindā un kartītes kļūst lielākas.
- **Vadība**: ar lieliem fontiem vai mazu ekrānu sakļauj trīs vadības rindas, lai atbrīvotu vietu kartēm un grafikiem. Stāvoklis tiek atcerēts.

## Datu mape

Visi dati un iestatījumi ir vienā **`data`** mapē **blakus programmai** – ne AppData, ne sistēmas mapes:

| Sistēma | Programma | Dati |
|---|---|---|
| Windows (instalētājs) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (portatīvā) | tur, kur to atarhivēji | `data` blakus `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (blakus lietotnei) |

Startējot programma vajadzības gadījumā izveido mapi un nokopē tikai **trūkstošos** sākuma failus: tevis mainītie faili nekad netiek pārrakstīti. Tulkojumu faili mapē `data/lingue` ir programmas faili un tiek aizstāti, ja jaunās versijas faili ir svaigāki.

### Faili, ko vari rediģēt

| Fails | Saturs |
|---|---|
| `sciami.csv` | Plūsmu katalogs (IMO vērtības un darba vērtības); sk. [Plūsmas](Showers-lv#kataloga-rediģēšana) |
| `massimi_imo.csv` | IMO publicētie maksimumu datumi un laiki (2026, 2027): **jaunus gadus pievieno** šeit |
| `ant_radiante.csv` | Antihēlija avota stāvoklis (IMO 6. tabula) |
| `fonti_radar.csv` | Radaru adreses; `attivo=1` lejupielādē, `0` ignorē |
| `regole_sperimentali.csv` | Izmantotās konstantes un likumi, katrs ar avotu (uzziņai) |
| `lingue/<code>.txt` | Saskarnes tulkojumi; sk. [Līdzdalība](Contributing-and-Contacts-lv#tulkojumi) |
| `config.ini` | Iestatījumi (sk. zemāk) |

### Programmas izveidotie faili

| Fails / mape | Saturs |
|---|---|
| `config.ini` | Iestatījumi |
| `flusso_collm.csv` | Collm meteoru skaita stundu arhīvs |
| `quote_collm.csv` | Sliežu augstumu arhīvs |
| `radar/` | Jaunākie radaru attēli un RMOB faili |
| `mappa/` | Natural Earth krasta līnijas un robežas (lejupielādētas pirmajā palaišanā) |
| `adif_quadrati.csv` | Kvadrāti no pēdējā ielādētā ADIF |
| `efficienza_spiegazione.txt`, `.docx` | [Skaidrojuma dokuments](Efficiency-Explanation-lv) |

## config.ini

Vienkāršs teksts, viens `key=value` rindā (rindas, kas sākas ar `#` vai `;`, ir komentāri). Programma to raksta aizveroties, tāpēc **rediģē to, kad YA-MS ir aizvērta**. Atslēgas, kuras var noderēt:

| Atslēga | Noklusējums | Nozīme |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Tavs lokators un augstums (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Korespondenta lokators un augstums (m) |
| `banda_MHz` | 144 | Josla (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Sliežu augstums (km); 1 = izmantot Collm modu |
| `elevazione_lobo_gradi` | 0 | Ziedlapiņas elevācija (°) |
| `boom_m` | 4.6 | Yagi traverses garums (m) |
| `hot_spot_km` | 150 | Hot A / Hot B attālums no viduspunkta (30–400 km) |
| `lingua` | sistēmas / `it` | Valodas kods (`it`, `en`, `ru`, `ja`, `de`, `nl`) |
| `tema` | `chiaro` | Krāsu shēma: `chiaro` (Gaišs), `scuro` (Nakts), `nero` (Melns), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Meteora sliede) |
| `carattere_pct` | 100 | Fonta izmērs (100–300 %) |
| `comandi_visibili` | 1 | 1 = vadības rindas redzamas, 0 = sakļautas |
| `mostra_mappa`, `vista_alto` | 1, 1 | Eiropas karte, skats no augšas debess velvē |
| `aggiornamento_automatico` | 1 | Automātiska avotu pārbaude ik pēc 5 minūtēm |
| `esponente_lambda` | 3 | λ kāpinātājs cilnē Radara meteoru skaits |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Sakaru budžeta ievaddati |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Eksperimentālā prognoze: frekvence, k, K |
| `rmob_osservatore` | tukšs | RMOB novērotāja vārds |
| `rmob_automatico` | 0 | Automātiska RMOB lejupielāde (ieslēgt tikai ar RMOB atļauju) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | RMOB adreses veidne |
| `graves_sequenza` | 0 | GRAVES kūļa secība: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Privātums

YA-MS nevāc nekādus datus un nerāda reklāmas. Tā savienojas ar internetu tikai, lai lejupielādētu publiskus datus: Collm un Sodankylä radaru attēlus, Natural Earth karti (pirmajā palaišanā) un, ja to pieprasi, RMOB failu.
