[English](Troubleshooting-FAQ) · **Italiano** · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh)

# Problemi e domande frequenti

## Installazione e avvio

### Windows SmartScreen dice "Windows ha protetto il PC"
Il programma non è firmato con un certificato commerciale. Fai clic su *Ulteriori informazioni* → *Esegui comunque*. Scaricalo solo dalla pagina [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: non è possibile aprire perché proviene da uno sviluppatore non identificato
YA-MS non è firmato da Apple, quindi **Gatekeeper** lo blocca la prima volta. Nel `.dmg` fai **clic destro su "Installa YA-MS.command" → Apri** e conferma. Lo script toglie a `~/YA-MS/YA-MS.app` il contrassegno di quarantena "scaricato da internet" e lo apre. Se macOS si rifiuta ancora, apri *Impostazioni di Sistema → Privacy e sicurezza* e premi *Apri comunque*.

### macOS: quale .dmg?
`-mac-apple-silicon.dmg` per i processori M1/M2/M3/M4, `-mac-intel.dmg` per i Mac Intel (menu Apple → *Informazioni su questo Mac* ti dice quale hai).

### Linux: YA-MS non è nel menu delle applicazioni
Esegui `./installa.sh` dalla cartella estratta (non da `~/YA-MS`). Alcuni desktop richiedono di uscire e rientrare nella sessione per mostrare le nuove voci. Puoi sempre avviarlo con `~/YA-MS/YA-MS`.

### Manca la mappa d'Europa
*Mappa d'Europa non disponibile (serve la rete al primo avvio).* La mappa di Natural Earth viene scaricata in `data/mappa` al primo avvio. Collegati a internet e riavvia YA-MS.

## Visualizzazione

### Linux: il testo giapponese appare come quadratini
Al sistema mancano i font CJK. Installa i font **Noto CJK** e riavvia YA-MS:

| Distribuzione | Comando |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Il testo è troppo piccolo, o i grafici non hanno spazio
Usa il cursore **Carattere** (100–300 %) e ripiega le righe con **Comandi**. Vedi [Impostazioni](Settings-and-Data-Folder-it#carattere-e-comandi).

### Di notte lo schermo è troppo luminoso
Scegli **Notte** o **Nero** nell'elenco **Tema**.

## Internet e dati radar

### Messaggio "Connessione internet assente"
YA-MS lo mostra **una sola volta** quando nessuna fonte è raggiungibile; la barra di stato diventa rossa. Il programma continua a funzionare con gli **ultimi dati salvati** e riprova da solo ogni 5 minuti; quando la rete torna compare *Connessione ripristinata.* Non c'è niente da fare.

### Avviso arancione in Flusso radar: "Non riesco a leggere la scala verticale del flusso …"
Il radar di Collm cambia la scala verticale ogni giorno e YA-MS la legge dalle etichette del grafico. Se un'etichetta non si riesce a leggere, il programma usa la scala tarata 0–1200 meteore/ora e avvisa che i **valori sono da verificare**. Di solito il grafico dell'ora successiva viene letto correttamente. Se per molte ore vedi *Formato del grafico cambiato* oppure *Assi del flusso non trovati nella posizione attesa*, il radar ha cambiato il formato del grafico: per favore [segnalalo](Contributing-and-Contacts-it).

### "La scala del grafico delle quote è cambiata"
Le statistiche delle quote (moda, media, mediana) restano valide; solo i conteggi assoluti dell'istogramma delle quote non lo sono.

### "Flusso radar: nessun dato"
Premi **Scarica adesso** in [Flusso radar](Radar-Flux-it) e controlla che `data/fonti_radar.csv` abbia `attivo=1` per Collm.

### RMOB: perché il prelievo automatico è spento?
RMOB chiede ai **programmi automatici di non prelevare i suoi file**. Attiva *prelievo automatico ogni 5 minuti* solo dopo che RMOB ti ha dato il permesso. Nel frattempo usa **Scarica RMOB adesso** oppure **Carica file RMOB dal disco...**. Vedi [Attuazione sperimentale previsioni](Experimental-Forecasts-it#rmob-e-programmi-automatici).

### RMOB: "Non ho riconosciuto il formato del file" o poche ore lette
Usa il file di testo mensile dell'osservatore (`NOME_MMAAAArmob.TXT`) o una tabella del bollettino con un solo osservatore. Per ricavare l'esponente servono almeno 3 ore in comune con i dati di Collm (ieri e oggi).

## Calcoli

### "Locator della stazione non valido" / "Locator del corrispondente non valido"
I locator devono avere 4, 6 o 8 caratteri (per esempio `JN70`, `JN70CN`, `JN70CN12`).

### "Nessuna zona comune dello strato E"
La tratta è più lunga del doppio della portata alla quota delle scie (circa 2 × 1062 km con il lobo a 0° e le scie a 89,5 km): un singolo salto in meteor scatter non può coprirla. Alzando l'**Elevazione lobo** la portata si accorcia ancora.

### Hot A / Hot B sono grigi
Sono già **dentro il lobo della tua antenna** quando punta verso il DX: non serve girarla. Vedi [Volta celeste](Sky-View-it#avvisi).

### L'efficienza è diversa da quella di MCG_MS o MS-Soft
YA-MS usa la tratta reale e un modello proprio; la scala di OH5IY e di MCG_MS non è documentata nei dettagli. Confronta ore e andamenti più che le percentuali assolute, e vedi il [modello](Efficiency-Calculation-it#il-modello).

### Il passaggio del fascio di GRAVES sembra spostato
La sequenza del fascio si calcola dall'orologio del PC: sincronizzalo con un server NTP. Inoltre la stazione di comando di GRAVES a volte sposta la sequenza di qualche passo; il dettaglio è una previsione da confermare all'ascolto.

## Altre domande

**YA-MS è gratuito?** Sì, è un programma gratuito per i radioamatori.

**Comanda il mio rotore o la mia radio?** No. YA-MS è uno strumento di previsione e pianificazione; per il QSO usa il tuo programma per i modi digitali (per esempio MSHV, WSJT-X).

**Funziona sopra i 432 MHz?** L'elenco delle bande si ferma a 432 MHz (28, 50, 70, 144, 222, 432). La previsione sperimentale accetta qualsiasi frequenza da 28 a 1300 MHz, ma le regole di SM6FHZ che usa vengono dall'esperienza su 144 e 432 MHz.

**Qualcosa non ha funzionato.** Scrivi all'autore indicando il sistema operativo, la versione di YA-MS e che cosa hai fatto: vedi [Contribuire e contatti](Contributing-and-Contacts-it).
