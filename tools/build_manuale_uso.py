# Genera il "Manuale d'uso di YA-MS" in due formati dallo stesso testo, con la formattazione della
# "Spiegazione del calcolo dell'efficienza":
#   manuale_uso.txt  -> mostrato nella linguetta "Documenti tecnici > Manuale d'uso" di YA-MS
#   manuale_uso.docx -> esportazione in Word
# Uso: python3 tools/build_manuale_uso.py <cartella data> [codice lingua]
#   senza codice (o "it"): data/manuale_uso.{txt,docx}; con un codice: data/manuale_uso/manuale_uso_<codice>.{txt,docx}
#   con la traduzione di tools/traduzioni_doc/manuale_uso/<codice>.json ({"testo italiano": "traduzione"}).
#   Con ESTRAI=<file.json> scrive l'elenco dei testi da tradurre.
# Etichette: [PROCEDURA] passi da seguire, [NOTA] informazione utile, [ATTENZIONE] errore frequente o limite.
import sys, os, json, re
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

LANG = sys.argv[2] if len(sys.argv) > 2 else 'it'
_tf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'traduzioni_doc', 'manuale_uso', LANG + '.json')
TRD = {} if LANG == 'it' or not os.path.exists(_tf) else json.load(open(_tf, encoding='utf-8'))
KEYS = []; MISS = []
def T(t):
    if not isinstance(t, str) or not re.search(r'[A-Za-zÀ-ÿ]{2,}', t): return t
    if t not in KEYS: KEYS.append(t)
    if LANG == 'it': return t
    if t not in TRD: MISS.append(t); return t
    return TRD[t]

TITLE = "Manuale d'uso di YA-MS"
SUB = "Versione 1.8.15 - a cura di Costantino IC8TEM - novembre 2026"

B = []
h1 = lambda t: B.append(("h1", T(t))); h2 = lambda t: B.append(("h2", T(t))); p = lambda t: B.append(("p", T(t)))
tag = lambda k, t: B.append(("tag", k, T(t))); eq = lambda t: B.append(("eq", T(t))); li = lambda t: B.append(("li", T(t)))

# ======================================================================
h1("1. Introduzione")
h2("1.1 A che cosa serve YA-MS")
p("YA-MS aiuta a prevedere e a seguire in diretta le condizioni di meteor scatter tra la tua stazione e un corrispondente, da 28 a 432 MHz. Per ogni sciame meteorico attivo dice quanto la posizione del suo radiante favorisce la tua tratta (l'efficienza), in quali ore, da quale lato della tratta arrivano le riflessioni e dove conviene puntare l'antenna. Accanto alla previsione mostra i dati misurati in diretta: i conteggi del radar meteorico di Collm, le telecamere del Global Meteor Network, il radar CMOR, il trasmettitore GRAVES e il traffico meteor scatter raccolto dai cluster e da PSKReporter.")
p("Il programma è gratuito, funziona su Windows, Linux (anche Raspberry Pi) e macOS, ed è tradotto in 36 lingue. Non comanda la radio né il rotore: per il collegamento si usa il solito programma dei modi digitali (MSHV, WSJT-X).")
h2("1.2 Come leggere questo manuale")
p("Il manuale descrive le linguette una per una, partendo dal calcolo previsionale. Ogni capitolo dice che cosa mostra la linguetta, che cosa fa ogni comando e come leggere i risultati. Il capitolo 14 raccoglie le procedure più comuni, il capitolo 15 i problemi frequenti. Come si calcola l'efficienza, con le fonti e le verifiche, è spiegato nel documento \"Spiegazione del calcolo dell'efficienza\"; le equazioni complete sono nel Manuale dei calcoli (cartella doc).")
tag("PROCEDURA", "passi da seguire, nell'ordine.")
tag("NOTA", "informazione utile per capire o usare meglio una funzione.")
tag("ATTENZIONE", "errore frequente, limite del calcolo o comportamento da conoscere.")
p("I nomi dei comandi sono scritti come compaiono nel programma in italiano; nelle altre lingue hanno lo stesso posto e lo stesso ordine.")

# ======================================================================
h1("2. Installazione, avvio e aggiornamenti")
h2("2.1 Quale pacchetto scaricare")
p("Tutti i pacchetti sono nella pagina delle release su GitHub (github.com/ic8tem/YA-MS/releases). Non serve installare .NET: è già dentro il pacchetto.")
li("Windows 64 bit: YA-MS-<versione>-windows-x64-setup.exe (installa in C:\\YA-MS, senza diritti di amministratore) oppure lo zip portatile, da estrarre in una cartella qualsiasi. Per Windows a 32 bit gli stessi file con x86.")
li("Linux (Debian, Ubuntu, Mint): il pacchetto .deb, da installare con sudo apt install ./ya-ms_<versione>_amd64.deb; al primo avvio il programma si copia in ~/YA-MS. Per le altre distribuzioni il .tar.gz, da estrarre ed eseguire con ./YA-MS.")
li("Raspberry Pi 3, 4, 5, 400 e 500: il pacchetto raspberry-pi-64bit (Raspberry Pi OS 64 bit) oppure raspberry-pi-32bit, in .tar.gz o .deb.")
li("Altri Linux ARM (per esempio Slackware ARM64 o schede armv7l): il pacchetto linux-arm64 oppure linux-armv7l, in .tar.gz, come per Linux.")
li("Windows su ARM (PC con Snapdragon): il pacchetto windows-arm64. Fedora e openSUSE: il pacchetto .rpm (x86_64 o aarch64), con sudo dnf install oppure sudo zypper install.")
li("Arch, Manjaro e Arch Linux ARM: il pacchetto .pkg.tar.zst, con sudo pacman -U. Slackware64 e Slackware ARM64: il pacchetto .txz, con installpkg da root. Qualsiasi Linux: l'AppImage (x86_64 o aarch64), da rendere eseguibile e avviare. Alpine Linux: il pacchetto alpine-x64 o alpine-arm64, in .tar.gz.")
li("macOS: il .dmg per Apple Silicon (M1 e successivi) o per Intel, oppure l'app.zip. Trascina YA-MS.app in una cartella tua (per esempio ~/YA-MS): la cartella data si crea accanto all'app.")
tag("ATTENZIONE", "Windows può mostrare \"Windows ha protetto il PC\": scegli \"Ulteriori informazioni\" e poi \"Esegui comunque\". Su macOS, la prima volta, apri l'app con il tasto destro e \"Apri\". Il programma non è firmato con un certificato a pagamento.")
h2("2.2 Il primo avvio")
p("All'avvio compare per pochi secondi la schermata con le Perseidi sopra il VLT dell'ESO. Al primo avvio YA-MS sceglie la lingua del sistema, se è una delle 36, altrimenti l'italiano; scarica la mappa d'Europa (Natural Earth) nella cartella data/mappa e mostra una tratta di esempio. Bastano pochi minuti per impostarlo per la tua stazione (capitolo 4).")
h2("2.3 La cartella data")
p("Tutte le impostazioni e tutti i dati stanno in un'unica cartella data accanto al programma: niente AppData, niente cartelle di sistema. Per spostare YA-MS su un altro computer basta copiare la cartella del programma con la sua cartella data. Il contenuto della cartella è descritto nel capitolo 13.")
h2("2.4 Aggiornamenti automatici")
p("Dalla versione 1.8.6 gli aggiornamenti sono automatici e silenziosi: all'avvio e poi ogni 30 minuti YA-MS controlla GitHub e, se c'è una versione nuova, la scarica, la installa e si riavvia da solo senza chiedere nulla (lo dice solo la barra di stato). Anche i file mancanti si riscaricano senza chiedere. La finestra descritta qui sotto compare solo premendo \"Aggiornamenti\" oppure se scrivi aggiornamenti_automatici=0 nel file data/config.ini.")
p("Dalla versione 1.8.0 YA-MS controlla da solo su GitHub, all'avvio e al massimo una volta al giorno, se è uscita una versione nuova. Se c'è, compare la finestra \"Aggiornamento disponibile\" con le novità e tre pulsanti:")
li("Aggiorna adesso: scarica il pacchetto adatto al tuo sistema, sostituisce i file del programma, tiene la cartella data e riavvia YA-MS. I file del programma nella cartella data che la nuova versione cambia vengono prima copiati in data/backup/v<versione vecchia>; i tuoi file (impostazioni, archivi, spot, ADIF) non vengono toccati.")
li("Più tardi: chiude la finestra; il controllo si ripete il giorno dopo.")
li("Salta questa versione: non ripropone più quella versione all'avvio.")
p("Il pulsante \"Aggiornamenti\" in basso a destra, nella barra di stato, fa lo stesso controllo a mano, anche per una versione saltata.")
tag("ATTENZIONE", "L'aggiornamento automatico deve poter scrivere nella cartella del programma. Se non può (per esempio un programma copiato in una cartella di sistema), YA-MS lo dice e propone di aprire la pagina delle release per installare a mano. Le versioni fino alla 1.7.0 non hanno questa funzione: la prima volta l'aggiornamento va fatto a mano, installando sopra la versione precedente.")
tag("NOTA", "Per non controllare più le versioni nuove scrivi controlla_aggiornamenti=0 nel file data/config.ini.")
h2("2.5 File del programma mancanti")
p("All'avvio YA-MS controlla di avere tutti i suoi file (traduzioni, cataloghi, documenti). Se ne manca qualcuno, per esempio dopo una copia incompleta, la finestra \"File mancanti\" li elenca e propone \"Scarica i file mancanti\" da GitHub, nella stessa versione del programma, oppure \"Continua senza\". Lo stesso controllo si ripete premendo \"Aggiornamenti\".")

# ======================================================================
h1("3. La finestra principale")
h2("3.1 Le parti della finestra")
li("In alto, due righe di comandi valide per tutte le linguette: strato E e antenna, ora del calcolo (capitolo 4). La tua stazione (locator, quota, banda e Calcola) sta in alto a destra nel Traffico in diretta.")
li("La barra delle linguette principali, con a destra il pulsante Comandi, lo schema di colori (Tema) e la lingua.")
li("Le sotto-linguette, in una riga più chiara, per le linguette che ne hanno.")
li("In basso, la barra di stato: messaggi del calcolo, avvisi sulla connessione, e il pulsante \"Aggiornamenti\".")
h2("3.2 Le linguette")
li("Live e dati real-time: Traffico in diretta, Flusso radar, Radar GRAVES, Raccolta dati (capitolo 9).")
li("Calcolo previsionale: Calcolo previsionale, Geometria e attenuazione, Calcolo dell'efficienza, Attuazione sperimentale previsioni (capitoli 5-8).")
li("Sciami in diretta, Sciami, Mappa quadrati (capitoli 10-11).")
li("Documenti tecnici, ultima: Manuale d'uso, Fonti, Mappa dei radar europei, Spiegazione del calcolo dell'efficienza (capitolo 12).")
h2("3.3 Lingua, colori, carattere")
li("Lingua: 36 lingue. Cambiando lingua la finestra si ricostruisce nella stessa posizione e sulla stessa linguetta, senza riavviare. Numeri e date seguono la lingua scelta (virgola decimale in italiano, punto in inglese).")
li("Tema: 12 schemi di colori; Chiaro è quello di partenza, Notte e Nero servono al buio, Scia meteorica è lo stile originale di YA-MS.")
li("Carattere (linguetta Impostazioni): rimpicciolisce o ingrandisce tutto il testo dall'85 al 140 %, a passi del 5 %. Con caratteri grandi le linguette vanno a capo.")
li("Comandi: ripiega e riapre le due righe di comandi, per dare spazio a mappe e grafici. La scelta viene ricordata.")
tag("NOTA", "Quasi ogni comando ha un fumetto: tieni fermo il mouse sopra il comando per leggere a che cosa serve e da quale fonte viene il valore di partenza.")

# ======================================================================
h1("4. Impostare la stazione e la tratta")
h2("4.1 La mia stazione (Traffico in diretta, in alto a destra)")
li("Il mio locator e quota m: il tuo locator Maidenhead (4, 6 o 8 caratteri; si usa il centro del quadrato) e la quota della stazione sul livello del mare.")
li("Banda MHz: 28, 50, 70, 144, 222 o 432 MHz. Serve per il guadagno e il lobo dell'antenna, per l'attenuazione e il bilancio, per la stima del flusso.")
li("Calcola: ricalcola la tratta (campionamento dello strato E, meno di un secondo).")
h2("4.2 Riga 1: strato E e antenna")
li("Quota scie km e dal radar: quota delle scie meteoriche. Con \"dal radar\" spuntato si usa la quota più frequente misurata dal radar di Collm (di solito 88-90 km); togli la spunta per scriverla a mano.")
li("Elevazione lobo °: elevazione del massimo del lobo verticale della tua antenna. Una direttiva fissata a 0° ha comunque il lobo principale qualche grado sopra l'orizzonte, per la riflessione sul terreno: di solito 3-8°, secondo l'altezza dell'antenna in lunghezze d'onda.")
li("diagramma d'antenna: accesa (di partenza), i punti di riflessione contano con il guadagno verticale delle due antenne: pieno attorno al massimo del lobo, sempre meno verso l'orizzonte e verso l'alto. Spenta, l'elevazione del lobo è un limite netto: i punti visti più in basso non contano.")
li("Antenna Yagi: boom m: lunghezza del boom. Accanto il programma scrive la lunghezza in lunghezze d'onda, il guadagno (curva DL6WU) e il lobo a -3 dB orizzontale e verticale. Sotto 2 λ la stima è poco precisa.")
li("Hot spot dal punto medio km e auto (AMS): distanza di Hot A e Hot B dal punto medio. Con \"auto (AMS)\" spuntato segue la tabella di J. Richardson citata da DJ5HG (13° di scarto a 1000 km, 10° oltre 1500 km); togli la spunta per scrivere 30-400 km a mano (MSHV usa 150 km).")
tag("ATTENZIONE", "Con \"diagramma d'antenna\" spento e il lobo a qualche grado, su una tratta lunga le due stazioni possono non vedere nessun punto comune dello strato: tutte le efficienze valgono 0 e compare l'avviso \"NESSUNA ZONA COMUNE\" con il lobo o la quota delle scie che servirebbero. Esempio: JN70CN - JO76QP, 1791 km, lobo a 3°, scie a 88,5 km.")
h2("4.3 Riga 2: ora del calcolo")
li("Ora: orologio UTC.")
li("Data del calcolo (UTC): il giorno del calcolo. Vale per Calcolo previsionale, per la tabella delle 24 ore di Calcolo dell'efficienza e per la cronologia di Radar GRAVES. Di partenza è oggi e a mezzanotte segue il giorno nuovo.")
li("Ore (da −12 a +36 h): sposta il momento del calcolo, a passi di 15 minuti. Accanto: \"Calcolo per: adesso\" oppure la data e l'ora scelte.")
li("Tempo reale: torna al momento attuale.")
h2("4.4 Impostare la propria stazione")
tag("PROCEDURA", "1) Scrivi Il mio locator e la quota. 2) Scrivi il locator e la quota del corrispondente, oppure fai clic sulla mappa di Calcolo previsionale: clic sinistro = corrispondente, clic destro = la tua stazione. 3) Scegli la banda. 4) Scrivi la lunghezza del boom e l'elevazione del lobo della tua antenna. 5) Premi Calcola: la barra di stato conferma \"Tratta calcolata: ... km, ... punti di riflessione campionati\".")
tag("NOTA", "Le impostazioni vengono salvate in data/config.ini alla chiusura e a ogni calcolo: al prossimo avvio ritrovi la stessa tratta.")

# ======================================================================
h1("5. Calcolo previsionale")
p("La prima sotto-linguetta del gruppo Calcolo previsionale mette in una schermata dove cadono adesso le scie utili e dove puntare. Tutto si riferisce al momento scelto con la data e il cursore delle ore.")
h2("5.1 La striscia di riepilogo")
p("Sopra la mappa una striscia riassume il calcolo per quel momento: data e ora, indice della tratta (somma di ZHR × efficienza degli sciami attivi), lo sciame più utile con il suo ZHR e la sua efficienza (anche in dB rispetto al riferimento di DJ5HG), il numero di sciami sopra l'orizzonte e l'Hot consigliato con il suo azimut.")
h2("5.2 La mappa in pianta")
p("Accanto alla mappa, a destra, c'è una colonna unica. In alto il riquadro del corrispondente: prima il puntamento dell'antenna (Antenna az, sempre verso il corrispondente), poi il nominativo (scrivilo e premi Invio: il locator si prende dall'archivio CALL3, come in YAEC e LIVETROPOVHF), il locator e la quota. Il nominativo si può scrivere anche nella casella del locator. In basso c'è la legenda dei simboli della mappa: un clic sul titolo la ripiega.")
p("Se per quel nominativo scrivi un locator diverso da quello dell'archivio, si accende il pulsante «Memorizza» accanto alla casella del locator: premendolo il nuovo locator diventa una voce a mano (data/CALL3-MANUALE.TXT, che vale sopra tutte le altre fonti) e viene scritto subito anche dentro data/call3.txt.")
p("A sinistra la mappa d'Europa vista dall'alto (est a destra), con la scala dei gradi tutt'intorno:")
li("linea verde: la tratta vera tra i due locator;")
li("Hot A e Hot B: i due hot spot ai lati del punto medio. Rosso = consigliato, rosa = fuori dal lobo dell'antenna, grigio = già dentro il lobo (con un avviso);")
li("lobo dell'antenna: il settore a -3 dB attorno all'azimut dell'antenna;")
li("Limite A e Limite B, tenui: i bordi più lontani del cielo visto da entrambe le stazioni, non i punti da puntare;")
li("linea gialla: la direzione in cui lo sciame selezionato (o il più favorevole) spazza il cielo; punti arancioni: i due puntamenti perpendicolari (azimut del radiante ±90°);")
li("zone PREV, ellissi chiare: dove cadono adesso le scie più probabili, una per lato della tratta.")
p("Clic sinistro sulla mappa = locator del corrispondente, clic destro = locator della tua stazione; la tratta si ricalcola subito. Le caselle sopra l'elenco degli sciami accendono e spengono le direzioni degli Hot, la mappa d'Europa e la vista dall'alto.")
h2("5.3 L'elenco degli sciami")
p("Per ogni sciame: nome e sigla IMO, ZHR in questo momento, azimut ed elevazione del radiante dalla tua stazione, efficienza per la tratta, lato prevalente (A o B), puntamento migliore, sorgere e tramonto del radiante. Un clic su una riga seleziona lo sciame: la linea gialla e i punti arancioni lo seguono.")
h2("5.4 La piccola volta celeste e il testo del calcolo")
p("I radianti visti dalla tua stazione, con il codice IMO e il percorso giornaliero in ciano. Giallo = efficienza almeno 50 % e ZHR almeno 2; arancione = almeno 20 %; rosso scuro = meno; grigio = quasi inattivo. La linea arancione per lo zenit dà le direzioni d'antenna giuste, ortogonali allo scorrimento dello sciame. Accanto, il testo del calcolo: tratta, punto medio, Hot consigliato con la percentuale delle riflessioni previste, limiti della zona comune.")
h2("5.5 La sezione")
p("In basso a destra le scie più probabili viste dall'antenna verso il corrispondente: in orizzontale l'azimut rispetto al corrispondente (A a sinistra, B a destra), in verticale l'elevazione. Ogni scia è un segmento orientato verso il radiante, più spesso quanto più è probabile. Sono disegnati anche il lobo dell'antenna, il corrispondente e gli Hot.")
h2("5.6 Gli avvisi")
li("ATTENZIONE: Hot A (o Hot B) entra nel lobo dell'antenna: con questo puntamento quell'hot spot è già coperto.")
li("RADIANTE TROPPO ALTO: un radiante utile è sopra 70°; le scie scendono quasi verticali e riflettono poco verso la tratta.")
li("RADIANTE BASSO LUNGO LA TRATTA: l'efficienza calcolata resta bassa, ma con scie radenti allineate DJ5HG prevede riflessioni rare e forti: vale la pena ascoltare.")
li("TRATTA OLTRE L'ORIZZONTE DELLA SCIA: alla quota delle scie il punto medio è sotto l'orizzonte; l'avviso dice quale quota servirebbe.")
li("NESSUNA ZONA COMUNE: nessun punto dello strato è visibile da entrambe le stazioni; l'avviso dice di quanto manca e che cosa servirebbe.")

# ======================================================================
h1("6. Geometria e attenuazione")
p("Un resoconto testuale della tratta, selezionabile e copiabile, e a destra il grafico dell'elevazione d'antenna in funzione della distanza dal punto di riflessione, per tre quote delle scie.")
h2("6.1 I dati di questa linguetta")
li("Potenza W (400), Guadagno antenna dBi (14; stessa antenna ai due estremi), Segnale minimo dBm (-130), Densità scia q = 10^14 elettroni/m: servono al bilancio del collegamento.")
li("Raggio iniziale della scia: doppio dell'ITU (Stober 2021, prudente, di partenza), ITU-R P.843, oppure escluso. Più grande è il raggio, più si perde alle frequenze alte.")
li("Durata dei ping tra le bande: teorica λ² (McKinley, SM6FHZ; prudente, di partenza) oppure osservata (misure HamSCI MSQP di NN4SA, Perseidi 2026: da 50 a 144 MHz i ping si accorciano di 1,5 volte invece di 8).")
h2("6.2 Il resoconto")
li("GEOMETRIA DELLA TRATTA: stazioni e quote, distanza, azimut, punto medio, quota delle scie, elevazione d'antenna verso il punto medio.")
li("HOT A / HOT B: locator, azimut, scarto dalla direzione diretta, distanza ed elevazione di ciascun hot spot.")
li("LIMITI DELLA ZONA COMUNE: portata alla quota delle scie fino all'orizzonte, il lobo d'antenna con il suo massimo e la sua larghezza verticale, Limite A e Limite B; guadagno e lobo della Yagi.")
li("ATTENUAZIONE DI TRATTA: per punto medio, Hot A e Hot B, a 28, 50, 70, 144, 222 e 432 MHz (scia che attraversa il piano della tratta, il caso più sfavorevole).")
li("BILANCIO: potenza ed EIRP, attenuazione, segnale in antenna, segnale minimo e margine; il caso migliore (scia nel piano della tratta) e il margine con l'attenuazione media di OH5IY.")
li("REGOLE SPERIMENTALI TRA LE BANDE: numero, intensità e durata delle riflessioni rispetto a 144 MHz; ping massimo IARU; durata osservata dalle misure MSQP.")
tag("NOTA", "Un margine positivo dice che una scia sottodensa media basta a chiudere la tratta con la tua stazione; un margine negativo dice che servono scie più dense o meteore sovradense. È una stima: il riferimento resta l'esperienza in banda.")

# ======================================================================
h1("7. Calcolo dell'efficienza")
p("L'efficienza dice, in percentuale, quanto la posizione del radiante di uno sciame consente riflessioni sulla tua tratta: 100 % è la posizione più favorevole per quella tratta. Questa sotto-linguetta la mostra ora per ora per il giorno della \"Data del calcolo\", con i valori a metà di ogni ora.")
h2("7.1 I quattro riquadri")
li("ORA MIGLIORE DEL GIORNO: l'ora con l'indice della tratta più alto e il lato prevalente.")
li("SCIAME PIÙ FAVOREVOLE: lo sciame che contribuisce di più, con l'ora, il lato e i due puntamenti migliori.")
li("ADESSO: indice e lato in questa ora e l'Hot consigliato (solo se il giorno scelto è oggi).")
li("PREVISIONE SPERIMENTALE: riflessioni all'ora previste adesso, tra 1 e tra 2 ore (capitolo 8).")
p("Quando un riquadro non ha valori dice perché: nessuna zona comune, nessuno sciame attivo, oppure radianti sfavorevoli per tutto il giorno. Il fumetto di ogni riquadro spiega che cosa mostra. Sotto i riquadri, quando serve, l'avviso NESSUNA ZONA COMUNE e una fascia che spiega le lettere A e B.")
h2("7.2 L'impostazione del calcolo")
li("Prudente (di partenza): quota delle scie dal radar, scie normali, angolo β acceso. Dà i valori più bassi.")
li("Come DJ5HG: quota fissa di 102 km, scie più lunghe con il radiante basso, angolo β acceso; ricalca il programma QTFGUI.")
li("Personalizzata: si seleziona da sola quando cambi a mano una delle caselle o la quota.")
li("Scie più lunghe con il radiante basso (DJ5HG): con il radiante basso cadono meno meteore, ma le scie sono più lunghe e riflettono più spesso; sopra circa 9° i due effetti si compensano.")
li("Angolo β tra scia e tratta (McKinley completo), nel riquadro arancione con la scritta \"la scelta che pesa di più\": accesa, le scie che attraversano il piano della tratta valgono 10-15 dB meno di quelle che vi giacciono e prevalgono i radianti allineati alla tratta. Spenta, vale la regola classica: radiante migliore alto 15-70° e di traverso alla tratta.")
li("Giudizio classico: aggiunge sotto ogni sciame la riga \"classico\" con il verdetto della regola dei radioamatori al punto medio della tratta: ✗ radiante sotto l'orizzonte, ◐ marginale (troppo basso, troppo alto o quasi allineato alla tratta), ● buono, ★ ottimo (di traverso alla tratta). Non cambia il calcolo.")
tag("ATTENZIONE", "L'angolo β cambia molto i valori sulle tratte lunghe: JN70CN - JO76QP (1791 km), Geminidi del 14/12/2026, 98 % con β spento e 13 % con β acceso. Le due tesi hanno fonti diverse e un primo confronto con i conteggi BRAMS non le distingue: confronta i due casi con l'esperienza in banda. Le percentuali sono relative alla posizione migliore del radiante per quella tratta; per confrontare tratte diverse si usa l'efficienza in dB.")
h2("7.3 Quanto fidarsi dei numeri")
p("Le ore migliori e il lato sono le informazioni più solide: cambiano poco con le impostazioni del calcolo. Le percentuali, invece, dipendono molto dalle scelte, soprattutto dall'angolo β. Il confronto con 181 767 spot MSK144 reali su 50 MHz (HamSCI, Perseidi dell'11-12 agosto 2025) conferma l'andamento orario dell'indice della tratta, ma mostra anche che quale coppia di stazioni si sente in una data ora dipende soprattutto dalle meteore sporadiche e dall'attività in aria, che il modello non contiene.")
tag("NOTA", "Usa il programma per scegliere l'ora e il lato verso cui girare l'antenna; non leggere le percentuali come probabilità di riuscita del collegamento.")
h2("7.4 Il grafico")
p("Per un massimo di cinque sciami: l'efficienza come linea continua e la formula di DH9GCD come linea punteggiata dello stesso colore; l'indice della tratta come barre sulla scala di destra. Le ore locali sono scritte sotto quelle UTC.")
p("Sul grafico una barra rossa verticale segna l'orario del calcolo (data e cursore delle ore della riga 3).")
h2("7.5 La tabella delle 24 ore")
li("Una riga per ogni sciame attivo quel giorno, 24 colonne per le ore UTC.")
li("63A: efficienza 63 %, la maggior parte delle riflessioni dal lato A; 41B: lato B; cella vuota: sotto l'1 %; ↑: radiante sopra 70° (troppo alto); colore più caldo = efficienza più alta.")
li("A = a sinistra guardando dalla tua stazione verso il corrispondente (zona Hot A); B = a destra (zona Hot B). Conviene girare l'antenna di 10-30° verso quel lato (side-scatter).")
li("Righe azzurre DH9GCD %: la formula della direzione migliore di DH9GCD, per confronto; non considera né l'orizzonte né il lobo.")
li("Riga Σ: indice della tratta, somma di ZHR × efficienza di tutti gli sciami attivi.")
li("Riga arancione: la previsione sperimentale delle riflessioni all'ora, per le ore in cui esiste.")
tag("PROCEDURA", "Per scegliere l'ora di uno sked: imposta la data, guarda la riga Σ e il riquadro ORA MIGLIORE DEL GIORNO; nella riga dello sciame scelto leggi la lettera A o B e gira l'antenna di 10-30° verso quel lato. Tieni il mouse su una cella per leggere il dettaglio dell'Hot di quell'ora.")

# ======================================================================
h1("8. Attuazione sperimentale previsioni")
p("Trasforma i conteggi del radar di Collm (36,2 MHz) in una stima delle riflessioni all'ora su una banda radioamatoriale (144 MHz di partenza, da 28 a 1300 MHz), fa la previsione delle prossime 24 ore per la tua tratta e la confronta con un osservatore RMOB. Tutto qui è sperimentale: i numeri servono a confrontare ore e giorni.")
h2("8.1 I comandi")
li("Frequenza di arrivo MHz: frequenza della previsione.")
li("Esponente λ^k (3, SM6FHZ) e Fattore di stazione K (1): regola sulla frequenza e correzione per la tua stazione.")
li("k dagli indici di popolazione: propone k dagli indici di popolazione r degli sciami attivi (GMN, altrimenti IMO; k = 3,75 · log10 r, pesato con lo ZHR) e chiede conferma prima di applicarlo.")
li("Carica file RMOB dal disco e Ricava l'esponente dal file RMOB: leggono un file mensile RMOB e ricavano k dalle ore in comune con Collm.")
li("Osservatore RMOB, Scarica RMOB adesso e prelievo automatico ogni 5 minuti: il prelievo automatico è spento e va acceso solo con il permesso di RMOB. Questi comandi sono nella linguetta Impostazioni.")
h2("8.2 I risultati")
li("Il grafico di ieri e oggi: meteore all'ora a Collm, valori traslati alla tua frequenza e, se caricati, i conteggi RMOB.")
li("La previsione delle prossime 24 ore: la stessa ora del giorno prima, corretta per la variazione dell'indice degli sciami della tratta.")
li("La tabella con il giudizio: buono, medio o scarso rispetto alla media delle 24 ore.")
tag("NOTA", "La durata delle riflessioni segue la scelta \"Durata dei ping tra le bande\" di Geometria e attenuazione; in forward scatter la durata cresce anche con sec²φ al punto medio della tratta.")

# ======================================================================
h1("9. Live e dati real-time")
h2("9.1 Traffico in diretta")
p("Una mappa azimutale equidistante centrata sulla tua stazione con tutto il traffico meteor scatter raccolto: per ogni collegamento la tratta nel colore della banda (28 marrone, 50 verde, 70 ciano, 144 arancione, 222 rosa, 432 viola), le due stazioni e la zona dello sciame delle scie più probabili a quell'ora. Gli spot appena arrivati lampeggiano per un minuto.")
li("Raggio della mappa: 600-3500 km. Spot da mostrare: ultimi 3, 15 o 30 minuti, ultima ora, ultime 3 o 24 ore.")
li("Il Mercatore si sposta trascinandolo con il mouse; doppio clic: di nuovo centrato sulla mia stazione. L'azimutale resta centrata sulla mia stazione.")
li("Un clic su una tratta o su una riga della tabella evidenzia il collegamento e mostra il centro della zona dello sciame, la sua quota e le sue dimensioni.")
li("I dettagli del contatto o della stazione in ascolto scelta compaiono in un riquadro in rilievo sopra la mappa, in alto a sinistra, sia con l'azimutale sia con il Mercatore.")
li("Mostra chi è in ascolto: triangoli del colore della banda segnano le stazioni che, secondo PSKReporter, ricevono in MSK144, FSK441, PSK2K o JTMS su 28, 50, 70, 144 e 432 MHz nella finestra di tempo scelta. Un clic sul triangolo mostra nominativo, locator, modi e ultimo spot. Serve il flusso MQTT della linguetta Raccolta dati connesso.")
li("Anche i monitor attivi della mappa di PSKReporter: triangoli vuoti per le stazioni che compaiono sulla mappa di pskreporter.info in MSK144, FSK441, PSK2K o JTMS ma non hanno ancora ricevuto nessuno spot (MQTT manda solo chi riceve qualcosa). YA-MS interroga il servizio di consultazione di PSKReporter una volta ogni 5 minuti per tutti i modi, come chiede il regolamento del servizio; un monitor resta sulla mappa almeno 11 minuti. Un clic sul triangolo mostra nominativo, locator, programma di decodifica e ora in cui il monitor era attivo. Acceso di partenza.")
li("FT8 oltre i 1100 km senza tratte parallele: uno spot FT8 (da PSKReporter MQTT, dai cluster o da WSJT-X via UDP) tra stazioni lontane più di 1100 km che nei 3 minuti prima e dopo non ha tratte parallele (stessa banda, punto medio entro 300 km, direzione entro 15°, un'altra coppia di stazioni) si disegna in verde chiaro e la sua riga nella tabella in basso a destra lampeggia sempre. L'E-sporadico e la tropo danno molte tratte vicine e parallele; uno spot isolato può essere una scia meteorica. Per questo YA-MS riceve da MQTT anche gli FT8 di 6 m, 4 m, 2 m, 1,25 m e 70 cm (mai i 28 MHz, in nessun caso). Questi spot non entrano nell'archivio MS. Acceso di partenza. Controlli in più con PSKReporter MQTT: lo spot non è isolato se la stazione ricevente sente in MQTT altre stazioni oltre i 1100 km nella stessa banda entro 3 minuti (banda aperta); gli spot dei cluster e di RBN valgono solo se la stessa coppia arriva anche da MQTT; gli skimmer RBN (nominativi con «-#») non entrano mai.")
li("Gli spot di WSJT-X via UDP che riguardano la tua stazione (la decodifica contiene il tuo nominativo: chi ti chiama o ti risponde) si disegnano con un tratteggio che lampeggia sempre, in qualsiasi modo e a qualsiasi distanza.")
li("Scambio tra gli utenti di YA-MS: quando un altro utente di YA-MS decodifica via UDP un messaggio rivolto alla tua stazione (in MSK144, FSK441, PSK2K o JTMS, oppure in FT8 oltre i 1100 km), il suo YA-MS te lo manda cifrato attraverso tre broker MQTT pubblici (HiveMQ, Mosquitto, EMQX); lo vedi con un tratteggio viola che lampeggia sempre e con una riga nella console UDP. Solo tu puoi leggerlo (chiavi ECDH P-256, AES-256 e HMAC-SHA256). Gli FT8 si mostrano solo se non hanno tratte parallele nei 3 minuti. Acceso di partenza; yams_scambio=0 in data/config.ini lo spegne.")
li("Si vedono gli spot di tutte le bande, anche di quelle non scelte nella Raccolta dati (quelli non si memorizzano). Gli spot CW e quelli tra stazioni troppo vicine non si vedono, se sono scartati nella Raccolta dati.")
li("Sulla mappa si scrivono i nominativi di entrambe le stazioni di ogni spot, una volta sola per stazione. La proiezione si sceglie tra azimutale (centrata sulla tua stazione) e Mercatore. Il fumetto sulla colonna % sciame ne spiega il significato.")
h2("9.2 Flusso radar")
p("I conteggi orari delle meteore e le quote delle scie del radar SKiYMET di Collm (36,2 MHz) e l'ultima immagine del radar di Sodankylä (36,9 MHz).")
li("Scarica adesso e Aggiornamento automatico di tutte le fonti ogni 5 minuti: ogni fonte viene riscaricata solo se è cambiata. L'aggiornamento automatico si imposta nella linguetta Impostazioni.")
li("Esponente λ (SM6FHZ): esponente della stima sulla tua banda (linea arancione sulla scala di destra).")
li("Quote delle scie: istogramma con moda, media, mediana e deviazione standard; con \"dal radar\" la moda diventa la quota di tutti i calcoli.")
tag("ATTENZIONE", "Se la scala del grafico di Collm non si riesce a leggere compare un avviso arancione e i valori vanno verificati. Senza connessione il programma usa gli ultimi dati salvati, lo dice una volta e riprova da solo ogni 5 minuti; la barra di stato diventa rossa finché la connessione non torna.")
h2("9.3 Radar GRAVES")
p("GRAVES trasmette in CW su 143,050 MHz da Broye-lès-Pesmes (JN27SI). La sotto-linguetta tratta GRAVES → te come una tratta meteor scatter a sé: calcola efficienza, Hot consigliato e zone PREV, verifica se la zona è dentro il fascio e quando il fascio la illumina.")
li("Adesso: riporta il calcolo al tempo reale. Metti GRAVES come DX: il corrispondente diventa GRAVES. Sequenza del fascio: 0,8 s per passo (PE1ITR 2021) oppure 3,2 s (2007).")
li("Le schede: ZONA UTILE NEL FASCIO, EFFICIENZA DELLA TRATTA GRAVES → TE ADESSO (con le eco attese, sperimentali), TRATTA (dove puntare), PROSSIMO PASSAGGIO DEL FASCIO.")
li("La ricostruzione cronologica del giorno e il dettaglio dei prossimi secondi.")
tag("PROCEDURA", "Per ascoltare GRAVES: USB su 143,049 MHz (tono a circa 1 kHz), AGC lento o spento, banda audio di almeno 2,4 kHz; antenna verso l'hot spot consigliato della scheda TRATTA, a bassa elevazione; orologio del PC sincronizzato. I ping sono brevi righe vicino alla portante nel waterfall.")
h2("9.4 Raccolta dati")
p("Raccoglie gli spot meteor scatter da tre flussi telnet (DX cluster, RBN, DM4X con gli spot di PSKReporter) e dal flusso MQTT di PSKReporter, ognuno nella sua sotto-linguetta, e li filtra.")
p("Come in LIVETROPOVHF: il programma ascolta i messaggi UDP del programma digitale (in WSJT-X: Impostazioni, Reporting, UDP Server 127.0.0.1 porta 2237) e li ripete identici sulla porta di inoltro per gli altri programmi (GridTracker, JTAlert, log). Ogni stazione decodificata diventa uno spot sentito dalla tua stazione; i messaggi di chiusura (RR73, 73, RRR) tra due altre stazioni diventano la tratta del loro QSO. Gli spot passano dagli stessi filtri degli altri.")
li("Scrivi in alto il tuo nominativo per il login. Ogni flusso ha host, porta, comandi dopo il login, Riconnetti, Connetti all'avvio e una console.")
li("Il filtro accetta gli spot nelle frequenze tipiche del meteor scatter (50190-50300, 70100-70400, 144290-144399 kHz) o con un modo MS (MSK144, FSK441, PSK2K, JTMS, JT6M, <MS>), e scarta quelli che dichiarano un'altra propagazione. Finestre e parole si possono modificare; ognuna ha il suo contatore.")
li("Gli spot CW si scartano subito (CW o WPM nel commento, oppure 28000-28070 kHz): non compaiono nella console e non si memorizzano, salvo quelli segnati <MS>. La casella si può spegnere.")
li("Gli spot tra stazioni più vicine di 500 km si scartano subito, perché a quella distanza il collegamento è diretto o troposferico e non meteor scatter: non compaiono nella console e non si memorizzano. Se manca un locator lo spot resta. La distanza si cambia sotto la casella.")
li("I locator mancanti vengono presi dall'archivio CALL3; gli spot accettati vanno in data/spot_ms, un file al giorno, e nella mappa del Traffico in diretta.")
li("Archivio CALL3 con le regole di LIVETROPOVHF. «Aggiorna adesso» scarica il CALL3.TXT da MMMonVHF (almeno 100.000 righe valide, il precedente resta in data/call3.bak); con «Aggiorna da solo ogni 12 ore» lo fa all'avvio. Sopra il file valgono, in ordine: voci a mano (data/CALL3-MANUALE.TXT), correzioni dal cluster (il locatore a 6 caratteri che chi spotta dichiara di sé), file aggiunti (data/CALL3-AGGIUNTE), poi CALL3.TXT e i locatori a 6 caratteri imparati dal vivo (data/LOC6.TXT). Un locatore ricevuto di 4 caratteri, o che finisce con LL o MM, si sostituisce con quello a 6 caratteri del database; i portatili (con la barra) solo con la voce esatta.")
li("Ultima fonte, come in LIVETROPOVHF: per i nominativi che in nessun'altra fonte hanno un locatore a 6 caratteri il programma lo chiede in automatico ogni 30 minuti all'API pubblica di G7VRD (api.g7vrd.co.uk), in gruppi di 40 nominativi; ogni nominativo al massimo una volta al giorno. Si accetta solo un locatore a 6 caratteri, non il centro del quadrato (LL o MM), nello stesso quadrato di quello ricevuto. I risultati stanno in data/CALL3-G7VRD.TXT e, come tutte le correzioni, vengono scritti anche dentro data/call3.txt.")
li("Dopo G7VRD c'è lo strato JTDX (data/grid_data.bin, circa 365.000 nominativi): vale solo per i nominativi senza locatore a 6 caratteri in tutte le altre fonti, solo nello stesso quadrato di quello ricevuto, e non si scrive mai dentro data/call3.txt.")

# ======================================================================
h1("10. Sciami in diretta e catalogo degli sciami")
h2("10.1 Sciami in diretta")
p("A sinistra il flusso e lo ZHR misurati dal Global Meteor Network per gli sciami attivi, con i conteggi del giorno delle telecamere GMN per sciame (un conteggio, non un flusso: dipende da quante stazioni vedono il cielo sereno); a destra le mappe dei radianti del radar CMOR, comprese quelle degli sciami diurni. I file si riscaricano solo se cambiati, al massimo ogni 30 minuti, oppure con Scarica adesso.")
h2("10.2 Sciami")
p("Il catalogo usato da tutti i calcoli: gli sciami del calendario IMO 2026 e 2027 più la Sorgente Antielio. Gli sciami attivi oggi sono evidenziati.")
li("Sigla, nome, periodo di attività, longitudine solare del massimo, prossimo massimo (UTC) e sua fonte (IMO o calcolato), radiante, velocità, indice di popolazione r, ZHR, tipo (visuale o radio diurno).")
li("k: esponente della traslazione di frequenza dall'indice di popolazione (GMN se disponibile, altrimenti IMO).")
li("IAU MDC: soluzioni, Δ radiante, Δλ, Δv: confronto con il catalogo dell'IAU Meteor Data Center (soluzioni pubblicate e differenze del catalogo del programma dalla loro mediana).")
li("GMN oggi: traiettorie confermate nell'ultimo file giornaliero del Global Meteor Network.")
tag("NOTA", "Il catalogo è il file data/sciami.csv e i massimi IMO sono in data/massimi_imo.csv: si possono modificare con un editor di testo. Una riga sbagliata viene segnalata all'avvio e ignorata.")

# ======================================================================
h1("11. Mappa quadrati")
p("I quadrati Maidenhead lavorati (arancione) e confermati (verde, QSL o LoTW) letti dal file ADIF del tuo log, su una mappa d'Europa, con una sotto-linguetta per banda: 50, 70, 144, 222 e 432 MHz.")
li("Carica file ADIF: legge un file .adi o .adif; un nuovo file sostituisce il precedente. Cancella memoria: cancella i quadrati caricati.")
li("Rotellina = zoom, trascina = sposta, mouse sopra un quadrato = i QSO di quel quadrato.")
tag("NOTA", "YA-MS non si collega a LoTW: esporta l'ADIF dal tuo programma di log o da LoTW e caricalo qui.")

# ======================================================================
h1("12. Documenti tecnici")
li("Manuale d'uso: questo documento.")
li("Fonti: tutte le fonti del programma, con i riferimenti.")
li("Mappa dei radar europei: dove si trovano Collm, Sodankylä, GRAVES e CMOR rispetto alla tua stazione, con il cielo visto da ciascun radar.")
li("Spiegazione del calcolo dell'efficienza: come si calcola l'efficienza, passo per passo, con le etichette FONTE, RILIEVO e SCELTA.")
p("I documenti seguono la lingua dell'interfaccia quando la traduzione esiste, altrimenti sono in italiano. \"Esporta in Word (.docx)\" ne salva una copia dove vuoi; \"Apri in Word\" lo apre con il programma predefinito. Il Manuale dei calcoli, con tutte le equazioni, è nella cartella doc (italiano) e doc/manuali (le altre lingue).")

# ======================================================================
h1("13. La cartella data e le impostazioni")
h2("13.1 I file principali")
li("config.ini: tutte le impostazioni (testo, chiave=valore).")
li("lingue/: le traduzioni dell'interfaccia; mappa/: la mappa d'Europa.")
li("sciami.csv, massimi_imo.csv, ant_radiante.csv: il catalogo degli sciami e la posizione della Sorgente Antielio; regole_sperimentali.csv: le regole tra le bande.")
li("flusso_collm.csv, quote_collm.csv: archivi del radar di Collm; radar/: ultime immagini, file RMOB e dati delle fonti in diretta; fonti_radar.csv: indirizzi delle fonti, abilitabili una per una.")
li("cataloghi/: catalogo IAU MDC; radar/diretta/: dati GMN e CMOR.")
li("call3.txt: archivio dei locator; spot_ms/: spot meteor scatter raccolti; adif_quadrati.csv: quadrati dall'ADIF.")
li("efficienza_spiegazione.*, spiegazione/, manuale_uso.*, manuale_uso/: i documenti tecnici.")
li("backup/: copie dei file sostituiti da un aggiornamento; aggiornamento/: pacchetto scaricato (cancellato al riavvio).")
h2("13.3 La linguetta Impostazioni")
p("La linguetta Impostazioni raccoglie il funzionamento generale del programma: Aspetto (carattere, tema e lingua), Aggiornamenti del programma (controllo su GitHub all'avvio e ogni 30 minuti, aggiornamenti automatici e silenziosi, Controlla adesso), Fonti in diretta (aggiornamento automatico ogni 5 minuti), RMOB (osservatore, scarico adesso e prelievo automatico) e Programma (righe dei comandi e cartella dei dati). I parametri del calcolo restano nelle righe dei comandi sopra le linguette.")
h2("13.2 Alcune chiavi di config.ini")
li("controlla_aggiornamenti=0: non controllare le versioni nuove; aggiornamenti_salta: versione saltata.")
li("lobo_diagramma, angolo_beta, lunghezza_scie, giudizio_classico: le caselle del calcolo.")
li("raggio_iniziale (0 = doppio dell'ITU, 1 = ITU, 2 = escluso), durata_ping (0 = λ², 1 = osservata).")
li("rmob_osservatore, rmob_automatico, rmob_url: RMOB.")
li("psk_rimando=0: spegne il rimando a PSKReporter delle decodifiche MS (MSK144, FSK441, PSK2K, JTMS) ricevute via UDP. È acceso di partenza e lavora da solo: se il tuo nominativo non compare da più di 20 minuti tra chi manda rapporti a PSKReporter (il programma digitale non sta inviando), YA-MS manda ogni 5 minuti le stazioni MS che decodifichi, con te come ricevitore; appena il programma digitale riprende a inviare, YA-MS si ferma. Una riga nella console UDP dice quando parte e quando si ferma. Se in WSJT-X.ini (o JTDX.ini) l'invio a PSKReporter è spento, YA-MS rimanda subito, senza aspettare i 20 minuti.")
tag("ATTENZIONE", "Modifica config.ini solo con il programma chiuso: alla chiusura YA-MS lo riscrive.")

# ======================================================================
h1("14. Procedure tipiche")
h2("14.1 Preparare uno sked su uno sciame")
tag("PROCEDURA", "1) Imposta le due stazioni e premi Calcola. 2) In Sciami controlla il prossimo massimo dello sciame. 3) Metti quella data in Data del calcolo. 4) In Calcolo dell'efficienza guarda la riga dello sciame e la riga Σ: scegli le ore con l'efficienza più alta. 5) Annota il lato (A o B) e gira l'antenna di 10-30° verso quel lato. 6) In Geometria e attenuazione controlla il margine del bilancio.")
h2("14.2 Seguire una sessione in diretta")
tag("PROCEDURA", "1) Premi Tempo reale. 2) In Calcolo previsionale segui l'Hot consigliato e le zone PREV, che si aggiornano ogni minuto. 3) In Flusso radar controlla che il radar di Collm stia contando meteore. 4) In Traffico in diretta guarda chi sta lavorando e dove cadono le loro scie.")
h2("14.3 Provare la stazione con GRAVES")
tag("PROCEDURA", "1) In Radar GRAVES controlla la scheda ZONA UTILE NEL FASCIO. 2) Punta l'antenna come dice la scheda TRATTA. 3) Ascolta in USB su 143,049 MHz nelle finestre del prossimo passaggio del fascio. 4) Confronta i ping con le eco attese e con gli osservatori RMOB.")
h2("14.4 Tarare la previsione con RMOB")
tag("PROCEDURA", "1) In Attuazione sperimentale previsioni carica un file RMOB mensile di un osservatore sulla tua banda. 2) Premi Ricava l'esponente dal file RMOB e accetta k se le ore in comune sono abbastanza. 3) Regola il fattore di stazione K sul valore suggerito.")

# ======================================================================
h1("15. Problemi frequenti")
li("Tutte le efficienze valgono 0: leggi l'avviso NESSUNA ZONA COMUNE. Con \"diagramma d'antenna\" spento abbassa l'elevazione del lobo; altrimenti la tratta è oltre l'orizzonte alla quota delle scie.")
li("I valori sono molto più bassi di quelli di DH9GCD o di una versione vecchia: controlla la casella dell'angolo β (capitolo 7.2).")
li("\"Locator della stazione non valido\": scrivi un locator di 4, 6 o 8 caratteri (per esempio JN70CN o JN70CN83).")
li("Hot A e Hot B sono grigi: con l'antenna verso il corrispondente sono già dentro il lobo; non serve girare l'antenna.")
li("Manca la mappa d'Europa: serve la connessione al primo avvio; il programma riprova da solo.")
li("Il testo è troppo piccolo o i grafici non hanno spazio: usa Carattere e il pulsante Comandi.")
li("Il passaggio del fascio di GRAVES sembra spostato: sincronizza l'orologio del PC con un server NTP; la sequenza del fascio a volte viene spostata dalla stazione di comando.")
li("Linux, testo cinese o giapponese a quadratini: installa i font Noto CJK.")

# ======================================================================
h1("16. Contatti")
p("YA-MS è un programma gratuito per i radioamatori, a cura di Costantino IC8TEM (Capri). Segnalazioni, proposte e dati di confronto sono benvenuti: indica il sistema operativo, la versione di YA-MS e che cosa hai fatto. Codice e release: github.com/ic8tem/YA-MS. Contatti: ccerrotta@gmail.com, ic8tem@gmail.com, www.qrz.com/db/ic8tem. Chi vuole sostenere il lavoro può farlo su ko-fi.com/ic8tem.")

# ======================================================================
TAGCOL_DOC = {"PROCEDURA": (0x1F, 0x5F, 0xAD), "NOTA": (0x2E, 0x7D, 0x32), "ATTENZIONE": (0xB4, 0x53, 0x09)}

def build_docx(path):
    d = Document()
    sec = d.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    for m in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'): setattr(sec, m, Cm(2))
    st = d.styles
    st['Normal'].font.name = 'Calibri'; st['Normal'].font.size = Pt(11)
    for name, size, col in (('Title', 24, (0x1F, 0x38, 0x64)), ('Heading 1', 16, (0x1F, 0x38, 0x64)), ('Heading 2', 13, (0x2F, 0x54, 0x96))):
        s = st[name]; s.font.name = 'Calibri'; s.font.size = Pt(size); s.font.bold = True; s.font.color.rgb = RGBColor(*col)
        s.paragraph_format.keep_with_next = True
    d.add_paragraph(TITLE, style='Title')
    r = d.add_paragraph().add_run(SUB); r.italic = True; r.font.color.rgb = RGBColor(0x60, 0x60, 0x60)
    for b in B:
        k = b[0]
        if k == 'h1': d.add_heading(b[1], level=1)
        elif k == 'h2': d.add_heading(b[1], level=2)
        elif k == 'p': d.add_paragraph(b[1])
        elif k == 'tag':
            para = d.add_paragraph(); para.paragraph_format.left_indent = Cm(0.4)
            r = para.add_run('[' + T(b[1]) + '] '); r.bold = True; r.font.color.rgb = RGBColor(*TAGCOL_DOC[b[1]])
            para.add_run(b[2])
        elif k == 'eq':
            para = d.add_paragraph(); para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = para.add_run(b[1]); r.italic = True; r.font.name = 'Cambria Math'; r.font.size = Pt(12)
        elif k == 'li': d.add_paragraph(b[1], style='List Bullet')
    if LANG in ('ar', 'he', 'ur'):   # lingue da destra a sinistra
        from docx.oxml import OxmlElement
        for para in d.paragraphs:
            para._p.get_or_add_pPr().append(OxmlElement('w:bidi'))
            for r in para.runs: r._r.get_or_add_rPr().append(OxmlElement('w:rtl'))
    d.save(path)

def build_txt(path):
    # una riga per blocco: TIPO|testo oppure TAG|tipo|testo (stesso formato della spiegazione)
    o = ['TITLE|' + TITLE, 'SUB|' + SUB]
    for b in B:
        o.append('|'.join(x.replace('\n', ' ') for x in ((b[0].upper(),) + tuple(b[1:]))))
    open(path, 'w', encoding='utf-8').write('\n'.join(o) + '\n')

TITLE, SUB = T(TITLE), T(SUB)
for k in ("PROCEDURA", "NOTA", "ATTENZIONE"): T(k)
out = sys.argv[1]
if LANG != 'it':
    out = os.path.join(out, 'manuale_uso'); os.makedirs(out, exist_ok=True)
    base = out + '/manuale_uso_' + LANG
else:
    base = out + '/manuale_uso'
build_txt(base + '.txt')
build_docx(base + '.docx')
if os.environ.get('ESTRAI'): json.dump(KEYS, open(os.environ['ESTRAI'], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if MISS: print('testi senza traduzione (%s): %d' % (LANG, len(MISS)))
print('ok', LANG, len(B), 'blocchi')
