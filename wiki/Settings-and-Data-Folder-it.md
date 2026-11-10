[English](Settings-and-Data-Folder) · **Italiano** · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Ελληνικά](Settings-and-Data-Folder-el) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [ไทย](Settings-and-Data-Folder-th) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh) · [中文 (繁體)](Settings-and-Data-Folder-zh-tw)

# Impostazioni e cartella dei dati

## La barra delle linguette

All'estremità destra della barra delle linguette, da destra verso sinistra:

| Comando | Che cosa fa |
|---|---|
| **Lingua** (elenco) | Lingua dell'interfaccia; vedi [Lingua](#lingua) |
| **Tema** (elenco) | Schema di colori; vedi [Schemi di colori](#schemi-di-colori) |
| **Comandi ▴ / ▾** | Ripiega o riapre le tre righe di comandi sopra le linguette; vedi [Carattere e Comandi](#carattere-e-comandi) |

Cambiando lingua o tema le impostazioni vengono salvate e **la finestra viene ricostruita** nella stessa posizione e dimensione, sulla stessa linguetta: non serve riavviare.

## Lingua

Sei lingue dell'interfaccia:

| Lingua | Codice | File |
|---|---|---|
| Italiano | `it` | nessuno: l'italiano è la lingua di base (le chiavi) |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

Al primo avvio YA-MS usa la **lingua del sistema** se è una di queste, altrimenti l'italiano. Numeri e date seguono la lingua scelta (per esempio punto decimale in inglese, virgola in italiano e in tedesco). Un testo che manca in un file di traduzione viene mostrato in italiano. Su Linux il giapponese richiede font adatti: vedi [Problemi e domande frequenti](Troubleshooting-FAQ-it#linux-il-testo-giapponese-appare-come-quadratini).

Il documento [Efficienza - spiegazione](Efficiency-Explanation-it) e il manuale dei calcoli sono in italiano.

## Schemi di colori

L'elenco **Tema** offre 12 schemi, gli stessi di YAEC, il programma EME dell'autore, più la tavolozza originale di YA-MS:

| Schema | Descrizione |
|---|---|
| **Chiaro** | predefinito |
| **Notte** | toni blu scuro, per l'uso di notte |
| **Nero** | sfondo nero, per il buio e per gli schermi OLED |
| Pastello azzurro · Pastello arancione · Pastello acquamarina · Pastello verde · Pastello rosa · Pastello lilla · Pastello indaco · Pastello marrone | otto schemi pastello chiari |
| **Scia meteorica** | lo stile originale di YA-MS (fino alla versione 1.2.0): viola notte con azzurro, viola, verde chiaro, giallo e arancione |

Lo schema vale per tutte le linguette ed è salvato in `config.ini` (chiave `tema`).

## Carattere e Comandi

- **Carattere** (in fondo alla prima riga di comandi): ingrandisce **tutto il testo** dal **100 al 300 %** a passi del 10 %; linee, cerchi e mappe mantengono la loro dimensione. Con caratteri grandi le linguette vanno a capo su una seconda riga e le schede si ingrandiscono.
- **Comandi**: con caratteri grandi o uno schermo piccolo, ripiega le tre righe di comandi per lasciare spazio a mappe e grafici. Lo stato viene ricordato.

## Cartella dei dati

Tutti i dati e le impostazioni stanno in un'unica cartella **`data`** **accanto al programma** – niente AppData, niente cartelle di sistema:

| Sistema | Programma | Dati |
|---|---|---|
| Windows (installatore) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (portatile) | dove l'hai estratto | `data` accanto a `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (accanto all'app) |

All'avvio il programma crea la cartella se serve e copia solo i file iniziali **mancanti**: i file che hai modificato non vengono mai sovrascritti. I file di traduzione in `data/lingue` sono file del programma e vengono sostituiti quando quelli della nuova versione sono più recenti.

### File che puoi modificare

| File | Contenuto |
|---|---|
| `sciami.csv` | Catalogo degli sciami (valori IMO e valori di lavoro); vedi [Sciami](Showers-it#modificare-il-catalogo) |
| `massimi_imo.csv` | Date e ore dei massimi pubblicate dall'IMO (2026, 2027): **aggiungi qui i nuovi anni** |
| `ant_radiante.csv` | Posizione della Sorgente Antielio (tabella 6 dell'IMO) |
| `fonti_radar.csv` | Indirizzi dei radar; `attivo=1` scarica, `0` ignora |
| `regole_sperimentali.csv` | Costanti e regole usate, ognuna con la sua fonte (riferimento) |
| `lingue/<codice>.txt` | Traduzioni dell'interfaccia; vedi [Contribuire](Contributing-and-Contacts-it#traduzioni) |
| `config.ini` | Impostazioni (vedi sotto) |

### File creati dal programma

| File / cartella | Contenuto |
|---|---|
| `config.ini` | Impostazioni |
| `flusso_collm.csv` | Archivio orario del flusso di Collm |
| `quote_collm.csv` | Archivio delle quote delle scie |
| `radar/` | Ultime immagini radar e file RMOB |
| `mappa/` | Coste e confini di Natural Earth (scaricati al primo avvio) |
| `adif_quadrati.csv` | Quadrati dall'ultimo ADIF caricato |
| `efficienza_spiegazione.txt`, `.docx` | Il [documento di spiegazione](Efficiency-Explanation-it) |

## config.ini

Testo semplice, una `chiave=valore` per riga (le righe che iniziano con `#` o `;` sono commenti). Il programma lo scrive quando si chiude, quindi **modificalo con YA-MS chiuso**. Le chiavi che può essere utile conoscere:

| Chiave | Predefinito | Significato |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Il tuo locator e la tua quota (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Locator e quota del corrispondente (m) |
| `banda_MHz` | 144 | Banda (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Quota delle scie (km); 1 = usa la moda di Collm |
| `elevazione_lobo_gradi` | 0 | Elevazione del lobo (°) |
| `boom_m` | 4.6 | Lunghezza del boom della Yagi (m) |
| `hot_spot_km` | 150 | Distanza di Hot A / Hot B dal punto medio (30–400 km) |
| `lingua` | sistema / `it` | Codice della lingua (`it`, `en`, `ru`, `ja`, `de`, `nl`) |
| `tema` | `chiaro` | Schema di colori: `chiaro` (Chiaro), `scuro` (Notte), `nero` (Nero), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Scia meteorica) |
| `carattere_pct` | 100 | Dimensione del carattere (100–300 %) |
| `comandi_visibili` | 1 | 1 = righe di comandi visibili, 0 = ripiegate |
| `mostra_mappa`, `vista_alto` | 1, 1 | Mappa d'Europa, vista dall'alto nella Volta celeste |
| `aggiornamento_automatico` | 1 | Controllo automatico delle fonti ogni 5 minuti |
| `esponente_lambda` | 3 | Esponente λ nella linguetta Flusso radar |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Dati del bilancio del collegamento |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Previsione sperimentale: frequenza, k, K |
| `rmob_osservatore` | vuoto | Nome dell'osservatore RMOB |
| `rmob_automatico` | 0 | Prelievo automatico da RMOB (attivare solo con il permesso di RMOB) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Modello dell'indirizzo RMOB |
| `graves_sequenza` | 0 | Sequenza del fascio di GRAVES: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Privacy

YA-MS non raccoglie dati e non mostra pubblicità. Si collega a internet solo per scaricare dati pubblici: le immagini dei radar di Collm e Sodankylä, la mappa di Natural Earth (primo avvio) e, se lo chiedi, un file RMOB.
