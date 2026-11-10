[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · **Svenska** · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Ελληνικά](Settings-and-Data-Folder-el) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh) · [中文 (繁體)](Settings-and-Data-Folder-zh-tw)

# Inställningar och datamapp

## Flikraden

I högra änden av flikraden, från höger till vänster:

| Reglage | Vad det gör |
|---|---|
| **Språk** (lista) | Gränssnittets språk; se [Språk](#språk) |
| **Tema** (lista) | Färgschema; se [Färgscheman](#färgscheman) |
| **Reglage ▴ / ▾** | Fäller ihop eller ut de tre raderna med reglage ovanför flikarna; se [Typsnitt och Reglage](#typsnitt-och-reglage) |

När du byter språk eller tema sparas inställningarna och **fönstret byggs om** i samma position och storlek, på samma flik: ingen omstart behövs.

## Språk

Sex gränssnittsspråk:

| Språk | Kod | Fil |
|---|---|---|
| Italiano | `it` | ingen: italienska är grundspråket (nycklarna) |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

Vid första starten använder YA-MS **systemets språk** om det är ett av dessa, annars italienska. Tal och datum följer det valda språket (t.ex. decimalpunkt på engelska, decimalkomma på italienska och tyska). Text som saknas i en översättningsfil visas på italienska. På Linux behöver japanska lämpliga typsnitt: se [Felsökning](Troubleshooting-FAQ-sv#linux-japansk-text-visas-som-rutor).

Dokumentet [Effektivitet - förklaring](Efficiency-Explanation-sv) och beräkningshandboken är på italienska.

## Färgscheman

Listan **Tema** erbjuder 12 scheman, desamma som i upphovsmannens EME-program YAEC plus den ursprungliga YA-MS-paletten:

| Schema | Beskrivning |
|---|---|
| **Ljust** | standard |
| **Natt** | mörkblå toner, för användning på natten |
| **Svart** | svart bakgrund, för mörker och för OLED-skärmar |
| Pastell ljusblå · Pastell orange · Pastell akvamarin · Pastell grön · Pastell rosa · Pastell lila · Pastell indigo · Pastell brun | åtta ljusa pastellscheman |
| **Meteorspår** | den ursprungliga YA-MS-stilen (till och med version 1.2.0): nattviolett med ljusblått, violett, ljusgrönt, gult och orange |

Schemat gäller alla flikar och sparas i `config.ini` (nyckeln `tema`).

## Typsnitt och Reglage

- **Typsnitt** (i slutet av den första raden med reglage): förstorar **all text** från **100 till 300 %** i steg om 10 %; linjer, cirklar och kartor behåller sin storlek. Med stora typsnitt bryts flikarna över till en andra rad och korten växer.
- **Reglage**: med stora typsnitt eller en liten skärm, fäll ihop de tre raderna med reglage för att ge plats åt kartor och diagram. Tillståndet sparas.

## Datamapp

Alla data och inställningar finns i en enda mapp **`data`** **bredvid programmet** – ingen AppData, inga systemmappar:

| System | Program | Data |
|---|---|---|
| Windows (installationsprogram) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (portabel) | där du packade upp det | `data` bredvid `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (bredvid appen) |

Vid start skapar programmet mappen om det behövs och kopierar bara de **saknade** startfilerna: filer som du har ändrat skrivs aldrig över. Översättningsfilerna i `data/lingue` är programfiler och ersätts när den nya versionens filer är nyare.

### Filer som du kan redigera

| Fil | Innehåll |
|---|---|
| `sciami.csv` | Svärmkatalog (IMO-värden och arbetsvärden); se [Svärmar](Showers-sv#redigera-katalogen) |
| `massimi_imo.csv` | Datum och tider för maximum publicerade av IMO (2026, 2027): **lägg till nya år** här |
| `ant_radiante.csv` | Positionen för Antihelion Source (IMO tabell 6) |
| `fonti_radar.csv` | Radaradresser; `attivo=1` hämtar, `0` ignorerar |
| `regole_sperimentali.csv` | Konstanter och regler som används, var och en med sin källa (referens) |
| `lingue/<code>.txt` | Gränssnittets översättningar; se [Bidra](Contributing-and-Contacts-sv#översättningar) |
| `config.ini` | Inställningar (se nedan) |

### Filer som skapas av programmet

| Fil / mapp | Innehåll |
|---|---|
| `config.ini` | Inställningar |
| `flusso_collm.csv` | Timarkiv över flödet från Collm |
| `quote_collm.csv` | Arkiv över spårhöjderna |
| `radar/` | Senaste radarbilder och RMOB-filer |
| `mappa/` | Kustlinjer och gränser från Natural Earth (hämtas vid första starten) |
| `adif_quadrati.csv` | Rutor från den senast inlästa ADIF-filen |
| `efficienza_spiegazione.txt`, `.docx` | [Förklaringsdokumentet](Efficiency-Explanation-sv) |

## config.ini

Vanlig text, en `nyckel=värde` per rad (rader som börjar med `#` eller `;` är kommentarer). Programmet skriver filen när det stängs, så **redigera den med YA-MS stängt**. De nycklar du kan vilja känna till:

| Nyckel | Standard | Betydelse |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Din lokator och höjd (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Motstationens lokator och höjd (m) |
| `banda_MHz` | 144 | Band (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Spårhöjd (km); 1 = använd typvärdet från Collm |
| `elevazione_lobo_gradi` | 0 | Lobelevation (°) |
| `boom_m` | 4.6 | Yagins bomlängd (m) |
| `hot_spot_km` | 150 | Avstånd från mittpunkten till Hot A / Hot B (30–400 km) |
| `lingua` | system / `it` | Språkkod (`it`, `en`, `ru`, `ja`, `de`, `nl`) |
| `tema` | `chiaro` | Färgschema: `chiaro` (Ljust), `scuro` (Natt), `nero` (Svart), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Meteorspår) |
| `carattere_pct` | 100 | Typsnittets storlek (100–300 %) |
| `comandi_visibili` | 1 | 1 = raderna med reglage visas, 0 = hopfällda |
| `mostra_mappa`, `vista_alto` | 1, 1 | Europakarta, vy ovanifrån i himlavalvet |
| `aggiornamento_automatico` | 1 | Automatisk kontroll av källorna var 5:e minut |
| `esponente_lambda` | 3 | λ-exponenten i fliken Radarflöde |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Indata till länkbudgeten |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Experimentell prognos: frekvens, k, K |
| `rmob_osservatore` | tom | RMOB-observatörens namn |
| `rmob_automatico` | 0 | Automatisk hämtning från RMOB (aktivera endast med tillstånd från RMOB) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Adressmall för RMOB |
| `graves_sequenza` | 0 | GRAVES lobsekvens: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Integritet

YA-MS samlar inte in några data och visar ingen reklam. Det ansluter till internet bara för att hämta offentliga data: radarbilderna från Collm och Sodankylä, kartan från Natural Earth (första starten) och, om du ber om det, en RMOB-fil.
