[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Ελληνικά](Settings-and-Data-Folder-el) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · **Tagalog** · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh) · [中文 (繁體)](Settings-and-Data-Folder-zh-tw)

# Mga setting at folder ng datos

## Ang tab bar

Sa kanang dulo ng tab bar, mula kanan pakaliwa:

| Kontrol | Ano ang ginagawa |
|---|---|
| **Wika** (listahan) | Wika ng interface; tingnan ang [Wika](#wika) |
| **Tema** (listahan) | Scheme ng kulay; tingnan ang [Mga scheme ng kulay](#mga-scheme-ng-kulay) |
| **Mga kontrol ▴ / ▾** | Itinitiklop o ibinubuka ang tatlong hanay ng mga kontrol sa itaas ng mga tab; tingnan ang [Font at Mga kontrol](#font-at-mga-kontrol) |

Kapag pinalitan ang wika o tema, sine-save ang mga setting at **muling binubuo ang window** sa parehong posisyon at laki, sa parehong tab: hindi kailangang i-restart.

## Wika

Anim na wika ng interface:

| Wika | Kodigo | File |
|---|---|---|
| Italiano | `it` | wala: Italyano ang batayang wika (ang mga key) |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

Sa unang pagsisimula, ginagamit ng YA-MS ang **wika ng sistema** kung isa ito sa mga ito, kung hindi ay Italyano. Sumusunod sa napiling wika ang mga numero at petsa (hal. tuldok bilang decimal sa Ingles, kuwit sa Italyano at Aleman). Anumang tekstong nawawala sa isang file ng salin ay ipinapakita sa Italyano. Sa Linux, kailangan ng angkop na font ang Hapones: tingnan ang [Pag-troubleshoot](Troubleshooting-FAQ-tl#linux-lumalabas-na-mga-kahon-ang-tekstong-hapones).

Nasa Italyano ang dokumentong [Episyensya - paliwanag](Efficiency-Explanation-tl) at ang manwal ng kalkulasyon.

## Mga scheme ng kulay

Nag-aalok ang listahang **Tema** ng 12 scheme, kapareho ng sa EME program ng may-akda na YAEC pati ang orihinal na palette ng YA-MS:

| Scheme | Paglalarawan |
|---|---|
| **Maliwanag** | default |
| **Gabi** | madilim na asul na kulay, para gamitin sa gabi |
| **Itim** | itim na background, para sa dilim at sa mga OLED na screen |
| Pastel na mapusyaw na asul · Pastel na kahel · Pastel na aquamarine · Pastel na berde · Pastel na rosas · Pastel na lila · Pastel na indigo · Pastel na kayumanggi | walong maliwanag na pastel na scheme |
| **Bakas ng meteor** | ang orihinal na istilo ng YA-MS (hanggang bersyon 1.2.0): biyoletang pang-gabi na may mapusyaw na asul, biyoleta, mapusyaw na berde, dilaw at kahel |

Inilalapat ang scheme sa lahat ng tab at sine-save sa `config.ini` (key na `tema`).

## Font at Mga kontrol

- **Font** (dulo ng unang hanay ng mga kontrol): pinalalaki ang **lahat ng teksto** mula **100 hanggang 300 %** sa mga hakbang na 10 %; hindi nagbabago ang laki ng mga linya, bilog at mapa. Kapag malaki ang font, bumababa sa ikalawang linya ang mga tab at lumalaki ang mga card.
- **Mga kontrol**: kapag malaki ang font o maliit ang screen, itiklop ang tatlong hanay ng mga kontrol para magkaroon ng puwang ang mga mapa at graph. Natatandaan ang kalagayan.

## Folder ng datos

Nasa iisang **`data`** folder **katabi ng programa** ang lahat ng datos at setting – walang AppData, walang system folder:

| Sistema | Programa | Datos |
|---|---|---|
| Windows (installer) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (portable) | kung saan mo ito in-extract | `data` katabi ng `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (katabi ng app) |

Sa pagsisimula, nililikha ng programa ang folder kung kailangan at kinokopya lamang ang mga **nawawalang** panimulang file: hindi kailanman pinapatungan ang mga file na binago mo. Ang mga file ng salin sa `data/lingue` ay mga file ng programa at pinapalitan kapag mas bago ang mga file ng bagong bersyon.

### Mga file na maaari mong i-edit

| File | Nilalaman |
|---|---|
| `sciami.csv` | Katalogo ng mga shower (mga halaga ng IMO at working value); tingnan ang [Mga shower](Showers-tl#pag-edit-ng-katalogo) |
| `massimi_imo.csv` | Mga petsa at oras ng peak na inilathala ng IMO (2026, 2027): **magdagdag ng bagong taon** dito |
| `ant_radiante.csv` | Posisyon ng Antihelion Source (talahanayan 6 ng IMO) |
| `fonti_radar.csv` | Mga address ng radar; `attivo=1` nagda-download, `0` hindi pinapansin |
| `regole_sperimentali.csv` | Mga constant at tuntuning ginamit, bawat isa ay may sanggunian (para sa reference) |
| `lingue/<code>.txt` | Mga salin ng interface; tingnan ang [Pag-ambag](Contributing-and-Contacts-tl#mga-salin) |
| `config.ini` | Mga setting (tingnan sa ibaba) |

### Mga file na nililikha ng programa

| File / folder | Nilalaman |
|---|---|
| `config.ini` | Mga setting |
| `flusso_collm.csv` | Archive bawat oras ng flux ng Collm |
| `quote_collm.csv` | Archive ng taas ng mga bakas |
| `radar/` | Pinakabagong larawan ng radar at mga RMOB file |
| `mappa/` | Mga baybayin at hangganan ng Natural Earth (dina-download sa unang pagsisimula) |
| `adif_quadrati.csv` | Mga grid square mula sa huling ikinargang ADIF |
| `efficienza_spiegazione.txt`, `.docx` | Ang [dokumento ng paliwanag](Efficiency-Explanation-tl) |

## config.ini

Simpleng teksto, isang `key=value` bawat linya (komento ang mga linyang nagsisimula sa `#` o `;`). Isinusulat ito ng programa kapag nagsasara, kaya **i-edit ito habang nakasara ang YA-MS**. Ang mga key na maaaring gusto mong malaman:

| Key | Default | Kahulugan |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Ang iyong locator at taas (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Locator at taas (m) ng DX station |
| `banda_MHz` | 144 | Banda (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Taas ng bakas (km); 1 = gamitin ang moda ng Collm |
| `elevazione_lobo_gradi` | 0 | Elebasyon ng lobe (°) |
| `boom_m` | 4.6 | Haba ng boom ng Yagi (m) |
| `hot_spot_km` | 150 | Distansiya ng Hot A / Hot B mula sa gitnang punto (30–400 km) |
| `lingua` | sistema / `it` | Kodigo ng wika (`it`, `en`, `ru`, `ja`, `de`, `nl`) |
| `tema` | `chiaro` | Scheme ng kulay: `chiaro` (Maliwanag), `scuro` (Gabi), `nero` (Itim), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Bakas ng meteor) |
| `carattere_pct` | 100 | Laki ng font (100–300 %) |
| `comandi_visibili` | 1 | 1 = nakikita ang mga hanay ng kontrol, 0 = nakatiklop |
| `mostra_mappa`, `vista_alto` | 1, 1 | Mapa ng Europa, tanaw mula sa itaas sa Kalangitan |
| `aggiornamento_automatico` | 1 | Awtomatikong pagsusuri ng mga sanggunian bawat 5 minuto |
| `esponente_lambda` | 3 | Exponent ng λ sa tab na Flux ng radar |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Mga input ng link budget |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Eksperimental na pagtataya: frequency, k, K |
| `rmob_osservatore` | walang laman | Pangalan ng RMOB observer |
| `rmob_automatico` | 0 | Awtomatikong pag-download ng RMOB (i-enable lamang kung may pahintulot ng RMOB) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Template ng address ng RMOB |
| `graves_sequenza` | 0 | Sequence ng beam ng GRAVES: 0 = 0.8 s (2021), 1 = 3.2 s (2007) |

## Privacy

Walang kinokolektang datos ang YA-MS at walang ipinapakitang advertising. Kumokonekta lamang ito sa internet para mag-download ng pampublikong datos: ang mga larawan ng radar ng Collm at Sodankylä, ang mapa ng Natural Earth (unang pagsisimula) at, kung hihilingin mo, isang RMOB file.
