# Genera il documento "Come si calcola l'efficienza dello sciame" in due formati dallo stesso testo:
#   efficienza_spiegazione.txt  -> mostrato nella linguetta "Spiegazione del calcolo dell'efficienza" di YA-MS
#   efficienza_spiegazione.docx -> esportazione in Word
# Uso: python3 tools/build_spiegazione.py <cartella data> [codice lingua]
#   senza codice (o "it"): data/efficienza_spiegazione.{txt,docx}; con un codice: data/spiegazione/efficienza_spiegazione_<codice>.{txt,docx}
#   con la traduzione di tools/traduzioni_doc/spiegazione/<codice>.json ({"testo italiano": "traduzione"}).
#   Con ESTRAI=<file.json> scrive l'elenco dei testi da tradurre.
import sys, os, json, re
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

LANG = sys.argv[2] if len(sys.argv) > 2 else 'it'
TRD = {} if LANG == 'it' else json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'traduzioni_doc', 'spiegazione', LANG + '.json'), encoding='utf-8'))
KEYS = []; MISS = []
def T(t):
    if not isinstance(t, str) or not re.search(r'[A-Za-zÀ-ÿ]{2,}', t): return t
    if t not in KEYS: KEYS.append(t)
    if LANG == 'it': return t
    if t not in TRD: MISS.append(t); return t
    return TRD[t]

TITLE = "Come YA-MS calcola l'efficienza di uno sciame"
SUB = "Documento tecnico - a cura di Costantino IC8TEM - novembre 2026"

# Blocchi: ("h1", testo) ("h2", testo) ("p", testo) ("tag", tipo, testo) ("eq", testo) ("li", testo) ("src", testo)
B = []
h1 = lambda t: B.append(("h1", T(t))); h2 = lambda t: B.append(("h2", T(t))); p = lambda t: B.append(("p", T(t)))
tag = lambda k, t: B.append(("tag", k, T(t))); eq = lambda t: B.append(("eq", T(t))); li = lambda t: B.append(("li", T(t)))

h1("1. Introduzione")
h2("1.1 Scopo del documento")
p("Questo documento spiega, passo per passo, come il programma ricava l'efficienza di uno sciame meteorico per una tratta di meteor scatter. Ogni passo indica da dove viene: da una fonte pubblicata, da una verifica fatta sul programma o da una scelta del programma stesso. Le equazioni complete, numerate, sono nel Manuale dei calcoli (cartella doc).")
h2("1.2 Come leggere le etichette")
tag("FONTE", "il passo riprende una fonte citata; il numero tra parentesi quadre rimanda all'elenco delle fonti in fondo.")
tag("RILIEVO", "confronto tra il programma e le fonti, con l'esito della verifica.")
tag("SCELTA", "scelta del programma, non presa da una fonte: va verificata con l'esperienza in banda.")
h2("1.3 Che cosa si intende per efficienza")
tag("FONTE", "L'efficienza indica in percentuale quanto la posizione dello sciame permette riflessioni su una data tratta. Il concetto è di Ilkka OH5IY (MS-Soft) [2] ed è ripreso nell'articolo [1]: il massimo di efficienza non coincide con il massimo visibile (ZHR), perché dipende da dove si trova il radiante rispetto alle due stazioni.")
tag("FONTE", "MCG_MS di DL5MCG [3] applica lo stesso concetto a quattro direzioni fisse (N/S, NE/SW, E/W, SE/NW) e, scrivendo il locator del corrispondente, anche alla tratta reale.")
tag("SCELTA", "YA-MS calcola l'efficienza per la tratta reale tra i due locator, non per direzioni fisse.")

h1("2. Dove avvengono le riflessioni: lo strato E")
h2("2.1 Le scie dello sciame")
tag("FONTE", "Le meteore dello sciame producono scie ionizzate nello strato E, tra 80 e 120 km di quota. I radar SKiYMET danno una quota media di circa 90 km [1].")
h2("2.2 La quota di calcolo")
tag("SCELTA", "Il programma legge l'istogramma delle quote del radar di Collm [7] e usa come quota di calcolo la più frequente (la moda). Se la casella \"dal radar\" è spenta, si usa il valore scritto a mano.")
tag("RILIEVO", "Grafico di Collm del 5/11/2026: moda 89,5 km, media 88,6 km, deviazione standard 6,8 km. Il dato conferma i 90 km dell'articolo [1].")
tag("RILIEVO", "DJ5HG [18] e QTFGUI [17] usano una quota fissa di 102 km; il programma preferisce il dato misurato dal radar. La Raccomandazione ITU-R P.843 [24] dà una quota media h = 124 − 17·log10(f) km: circa 97 km a 36,2 MHz e 87 km a 144 MHz, in linea con la moda di Collm (89,5 km il 5/11/2026).")

h1("3. La geometria della tratta")
h2("3.1 Terra, stazioni e punto medio")
tag("FONTE", "Terra sferica di raggio r = 6372,7955 km [1].")
tag("SCELTA", "La tratta è sempre quella reale tra il locator della stazione e quello del corrispondente. Distanza, azimut e punto medio si calcolano con le formule del cerchio massimo.")
tag("FONTE", "I calcoli che dipendono dall'ora si riferiscono al punto medio della tratta: tra le due estremità l'ora migliore può differire fino a 1,5 ore (SM6FHZ [4]).")
h2("3.2 Elevazione d'antenna")
tag("FONTE", "L'elevazione verso il punto di riflessione si calcola con la formula dell'articolo (Immagine 7) [1], con x = distanza / r, H quota della scia, h quota della stazione:")
eq("e = 90° − 57,3 · arctan[ (r·tan x + (H − r(1−cos x)/cos x)·sin x) / (H − r(1−cos x)/cos x − h·sin x) ]")
tag("RILIEVO", "La formula coincide entro 0,03° con la geometria sferica esatta. Il programma usa l'arcotangente a due argomenti, che oltre l'orizzonte dà valori negativi ed evita il problema di periodicità segnalato nell'articolo.")
h2("3.3 La zona comune e i suoi limiti")
tag("FONTE", "L'articolo [1] individua gli incroci delle curve dove l'orizzonte di ciascuna stazione incontra lo strato E. Sono gli incroci di due cerchi attorno alle stazioni, di raggio uguale alla portata alla quota delle scie:")
eq("d_H = r · [ π/2 − e − arcsin( (r+h)·cos e / (r+H) ) ]")
p("Con H = 89,5 km e il lobo a 0° la portata è di 1062 km. Se la tratta è più lunga del doppio della portata, le due stazioni non vedono una zona comune dello strato E.")
tag("RILIEVO", "Questi due punti sono i bordi più lontani del cielo visto da entrambe le stazioni, non i punti dove arrivano più riflessioni. Sulla tratta JN70CN - IN78UO (1710 km) cadono 37° a sinistra e a destra della direzione diretta, mentre MSHV consiglia 10°. Per questo il programma li chiama \"Limite A\" e \"Limite B\" e li disegna tenui sulla mappa, con i due cerchi della zona comune.")
tag("RILIEVO", "Nell'esempio dell'articolo (JN44BB - IO53RT) il disegno pone questi incroci a circa 870 km dalle stazioni: corrisponde a un lobo elevato di circa 2° (865 km).")
h2("3.4 Hot A e Hot B: dove puntare")
tag("FONTE", "Le riflessioni delle meteore sporadiche si concentrano in due zone (\"hot spot\") ai lati del punto medio della tratta. J. Richardson (AMS) [19], nella tabella riportata da DJ5HG [18], indica lo scarto d'antenna dalla direzione diretta: 13° a 1000 km, 11° a 1250 km, 10° a 1500 e a 2000 km. L'AMS Bulletin n. 203, ripreso da W8WN [14], dà 10° a 1500 e 1800 km.")
tag("SCELTA", "Hot A e Hot B sono i punti a distanza s dal punto medio, perpendicolari alla tratta (A a sinistra guardando dalla stazione verso il corrispondente, B a destra). Con la casella \"auto (AMS)\" accesa (di partenza) s viene dallo scarto della tabella di Richardson, interpolato in modo lineare (13° sotto 1000 km, 10° sopra 2000 km): s = (D/2)·tan(scarto). Spegnendo la casella si scrive s a mano (MSHV [15] usa 150 km).")
eq("Δaz ≈ arctan( s / (D/2) )")
tag("RILIEVO", "Con la tabella AMS: 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN-IN78UO (1710 km) → 10°, s ≈ 151 km, come i 150 km usati prima e da MSHV; sulle tratte corte la tabella avvicina gli hot spot al punto medio.")
tag("SCELTA", "Per l'ora mostrata sulla volta celeste il programma somma, su tutti gli sciami sopra l'orizzonte, ZHR x efficienza diviso tra lato A e lato B (capitolo 7.1). L'hot spot del lato che riceve più riflessioni è quello consigliato: compare in rosso sulla mappa.")
tag("FONTE", "Secondo DJ5HG, riportato da DF5HC [16], la riflessione avviene su un cono attorno alla scia: per le tratte più corte le antenne vanno puntate a lato della direzione diretta, entrambe le stazioni verso lo stesso punto, e secondo la posizione del radiante uno dei due punti (HOT-A o HOT-B) è più favorevole. DF5HC indica anche la distanza migliore in 1300-1500 km, con un massimo di poco oltre 2000 km.")
h2("3.5 Il lobo dell'antenna")
tag("FONTE", "Guadagno di una Yagi lunga dalla lunghezza del boom (curva DL6WU [10]) e apertura del lobo a −3 dB dal guadagno (regola di Kraus [11]):")
eq("G = 7,773 · log10(L/λ) + 11,43 dBi          θK = √( 41253 / 10^(G/10) )")
tag("RILIEVO", "Le simulazioni NEC di W4RNL [12] confermano la curva del guadagno entro 0,1 dB sia per le Yagi DL6WU sia per quelle di David Tanner VK3AUU, che a pari elementi hanno il boom più corto: il guadagno dipende dalla lunghezza del boom. Le stesse simulazioni danno un lobo orizzontale più stretto di Kraus del 5-10 %.")
tag("SCELTA", "Lobo orizzontale (quello del puntamento in azimut) = 0,93 · θK; lobo verticale = θK. Yagi di 14 λ a 432 MHz: 20,3 dBi, 18,1° orizzontale e 19,5° verticale; i modelli di W4RNL danno 20,4 dBi e 18,4°/18,8°.")
tag("SCELTA", "L'antenna si considera sempre puntata verso il corrispondente. Un hot spot che cade entro ±θ/2 da quella direzione è già coperto dal lobo: è segnato in grigio invece che in rosa e il programma lo avvisa. L'hot spot consigliato dall'efficienza resta comunque in rosso.")

h1("4. Il radiante dello sciame")
h2("4.1 Posizione del radiante")
tag("FONTE", "Ascensione retta, declinazione, longitudine solare del massimo, velocità, indice r e ZHR vengono dai calendari IMO 2026 e 2027 [5], tabelle 5 e 7; la sorgente Antielio dalla tabella 6. Sono inclusi anche gli sciami minori della lista IMO, per esempio le Camelopardalidi di ottobre (OCT, ZHR 5, attive il 5-6 ottobre), le Andromedidi e gli sciami diurni radio di aprile e maggio: anche con ZHR piccoli contribuiscono all'indice della tratta e al consiglio dell'hot spot.")
tag("SCELTA", "Per gli sciami diurni radio l'IMO non dà ZHR né velocità: il programma usa un valore di lavoro di 5.")
tag("FONTE", "Longitudine solare (equinozio J2000), tempo siderale e conversione in azimut ed elevazione: formule di Meeus [6].")
tag("SCELTA", "La deriva giornaliera del radiante usa valori di lavoro, scritti nel file sciami.csv e modificabili.")
tag("RILIEVO", "Confronto con il catalogo dell'IAU Meteor Data Center [32]: la linguetta Sciami mostra per ogni sciame quante soluzioni sono pubblicate nell'elenco degli sciami stabiliti e la differenza tra il catalogo IMO del programma e la mediana delle soluzioni: distanza angolare dei radianti (confrontati alla stessa longitudine solare, con la deriva del programma), Δλ (λ max del programma meno la mediana delle longitudini solari medie dell'attività, che non coincidono esattamente con il massimo) e Δv. Il fumetto elenca le soluzioni con i loro riferimenti. Il file originale si scarica al massimo una volta al mese da www.ta3.sk; il MDC chiede di citare Jenniskens et al. 2020 e Jopek e Kaňuchová 2017.")
h2("4.2 Data del massimo")
tag("FONTE", "Il programma mostra sempre il prossimo massimo. Quando l'IMO ha pubblicato il calendario di quell'anno (2026 e 2027 sono già inseriti in massimi_imo.csv) usa la data e l'ora IMO [5]; altrimenti calcola l'istante in cui il Sole raggiunge la longitudine del massimo.")
tag("RILIEVO", "Il calcolo coincide con i calendari IMO 2026 e 2027 entro pochi minuti per gli sciami di cui l'IMO dà l'ora (per esempio Quadrantidi 3/1/2026 21:13 contro 21:00, Geminidi 14/12/2027 19:51 contro 20:00). Fanno eccezione le kappa-Leonidi diurne 2026, un giorno dopo (26/9 invece di 25/9), e l'ora delle eta-Aquaridi 2027 (15:10 contro le 09:00 IMO): in questi casi vale il dato IMO.")
h2("4.3 Attività nel tempo")
tag("FONTE", "ZHR massimo dal calendario IMO [5].")
tag("SCELTA", "Attorno al massimo l'attività cala in modo esponenziale, con pendenza diversa in salita e in discesa (valori di lavoro in sciami.csv):")
eq("ZHR(λ) = ZHRmax · 10^( −B · |λ − λmax| )")

h1("5. La condizione di riflessione")
h2("5.1 La riflessione speculare")
tag("FONTE", "Una scia rimanda il segnale tra le due stazioni solo se è tangente a un ellissoide che ha le stazioni nei fuochi (McKinley [8]). Le scie di uno sciame sono parallele alla direzione del radiante [1, 8].")
p("In pratica, per ogni punto P dello strato E si prendono le direzioni da P verso le due stazioni e la loro bisettrice n. La scia, parallela al radiante (direzione s), riflette verso entrambe le stazioni quando è perpendicolare alla bisettrice:")
eq("s · n = 0")
tag("FONTE", "La stessa legge è alla base di QTFGUI di DJ5HG: il raggio che colpisce la scia viene diffuso su un cono attorno ad essa, e solo chi sta sul cono riceve il segnale. La condizione del cono equivale a s · n = 0. [17, 18] Nel suo testo del 2004 DJ5HG la descrive così: la scia attraversa lo strato E, le due antenne la illuminano e il ricevitore sta sul cono che ha la scia come asse; la parete del cono è il lobo di un radiatore lungo migliaia di lunghezze d'onda, quindi stretta, ma a incidenza radente (tratte lunghe) tocca il suolo su un'area ampia.")
h2("5.2 Tolleranza")
tag("SCELTA", "La condizione si accetta con una tolleranza gaussiana di 0,05 rad (circa 3°). La parete del cono, per una scia ideale, è molto più stretta [18]; i 3° rappresentano quello che il cono ideale non vede: la dispersione dei radianti di uno sciame (0,3-1,4° misurati dal GMN), la scia curvata dal vento e la sua lunghezza finita.")
tag("RILIEVO", "Per il meteor scatter QTFGUI di DJ5HG disegna scarti dalla legge di riflessione fino a 32°: la tolleranza gaussiana di 0,05 rad del programma è più severa e concentra il peso sui punti quasi esattamente speculari. Con il campionamento a 5 km invece di 15 km le percentuali cambiano meno di 0,3 punti.")
h2("5.3 Conseguenza pratica: il miglior puntamento")
tag("FONTE", "Una scia rimanda il segnale tra le due stazioni solo se è tangente a un ellissoide con le stazioni nei fuochi: in ogni punto dello strato E servono solo i radianti sul semicerchio del cielo perpendicolare alla bisettrice dell'angolo di scattering (Eshleman e Mlodnosky [20]; Meeks e James [21]). Vicino al punto medio questo semicerchio sale al massimo di traverso alla tratta: un radiante a elevazione El produce scie speculari a circa H·tan El di lato dal punto medio, dalla parte opposta al radiante, cioè negli hot spot che Eshleman e Mlodnosky e la Raccomandazione ITU-R P.843 [24] collocano a circa 100 km dai due lati. Il numero delle scie e la loro ionizzazione crescono con sin El [21]. La dipendenza degli echi dalla posizione del radiante è stata calcolata da Hines [22] e verificata su quattro sciami da Forsyth, Hines e Vogan [23]. Ne segue la regola pratica di SM6FHZ [4]: tratta migliore ortogonale all'azimut del radiante, puntamento Az ± 90°, tolleranza ±40-50°.")
tag("RILIEVO", "Riserva di DJ5HG [18]: con il radiante basso proprio lungo la tratta la formula di McKinley dà segnali forti, anche se le meteore sono poche (Amburgo-Narvik, Quadrantidi, verso le 19 UTC). La regola \"radiante allineato alla tratta = efficienza quasi nulla\" vale quindi per il radiante alto, non per quello radente. Il programma resta prudente e non alza l'efficienza, ma segnala sulla volta celeste \"RADIANTE BASSO LUNGO LA TRATTA\" quando uno sciame attivo ha il radiante sotto 20° ed entro 30° dalla direzione della tratta. Il buco con il radiante allo zenit tra le due stazioni è confermato (Quadrantidi, Amburgo-Barcellona, verso le 08 UTC).")
tag("RILIEVO", "La stessa regola compare nella formula di DH9GCD riportata da DF5HC [16]: efficacia = sin(El) · cos(El) · sin(P − Az), con El e Az elevazione e azimut del radiante e P azimut del corrispondente. È massima con il radiante a 45° e di traverso alla tratta; DF5HC considera il radiante troppo basso sotto 20° e troppo alto sopra 70°. La formula non tiene conto della distanza né delle quote, ma è un buon termine di confronto: nella sottolinguetta \"Calcolo previsionale › Calcolo dell'efficienza\" compare, in azzurro, sotto ogni sciame, in percentuale del suo massimo (0,5). Quando il radiante è sopra 70° dalla stazione il programma lo segnala con ↑ nella tabella e con un avviso sulla volta celeste.")
tag("RILIEVO", "La formula di DH9GCD non ha una fonte primaria pubblicata: unisce il fattore sin El (numero e ionizzazione delle scie) a un fattore cos El che rappresenta l'allontanamento del punto speculare dal centro della tratta quando il radiante sale. Calcolata con il radiante visto dal punto medio, come fa MS-Soft [25], riproduce la tabella di MS-Soft per KP30HV-JO52MM (1324 km, Quadrantidi, 4/1/2001) entro 4 punti tra 16° e 48° di elevazione ed entro 16 punti fino a 64°, con lo stesso massimo alle 13 UT (96 % contro 92 %). Resta un termine di confronto.")

h1("6. Dal singolo punto all'efficienza")
h2("6.1 I punti di riflessione")
tag("SCELTA", "Il programma divide lo strato E in punti ogni 15 km e tiene quelli che entrambe le stazioni vedono sopra l'orizzonte. Con la casella \"diagramma d'antenna\" accesa (di partenza) ogni punto pesa con il guadagno verticale delle due antenne: una direttiva fissata a 0° ha comunque il lobo principale qualche grado sopra l'orizzonte per la riflessione sul terreno, e l'\"Elevazione lobo\" è l'elevazione e0 di quel massimo. Con e l'elevazione del punto vista da una stazione e θV la larghezza verticale del lobo a −3 dB (paragrafo 3.5):")
eq("g(e) = 10^(−1,2·(e/θV)²) · sin²(π/2 · sin e / sin e0) per e < e0;   g(e) = 10^(−1,2·(e/θV)²) per e ≥ e0;   peso del punto × g(e1) · g(e2)")
tag("SCELTA", "Sotto il massimo il fattore del terreno porta il guadagno a zero all'orizzonte; il lobo ha un fondo di −20 dB. Un punto basso conta meno, ma conta: su una tratta lunga l'efficienza non sparisce. Con la casella spenta l'elevazione del lobo è un limite netto, come fino alla versione 1.8.0: i punti visti sotto e0 da una delle due stazioni non contano, e su una tratta lunga con il lobo a qualche grado tutte le efficienze possono valere 0 (JN70CN – JO76QP, 1791 km, lobo a 3°, scie a 88,5 km: nessun punto).")
h2("6.2 Il peso di ciascun punto")
tag("FONTE", "La potenza di una scia sottodensa (McKinley [8]; ITU-R P.843 [24]) cresce con λ³ e cala con le distanze R1, R2 dalle stazioni; φ è la metà dell'angolo di scattering, β l'angolo tra la scia e il piano che contiene le due stazioni e il punto:")
eq("peso = 1 / [ R1 · R2 · (R1 + R2) · (1 − cos²β · sin²φ) ]")
tag("SCELTA", "Fino alla versione 1.6 il programma prendeva β = 0 per tutte le scie (peso con cos²φ): le scie che attraversano il piano della tratta pesavano fino a 10-15 dB troppo. Dalla 1.7 β si può calcolare per ogni punto e per ogni direzione del radiante con l'opzione \"Angolo β tra scia e tratta (McKinley completo)\", accesa di partenza perché dà i valori più prudenti (nessuna scia è sopravvalutata).")
tag("SCELTA", "L'angolo φ è limitato a 85° per evitare valori infiniti nelle direzioni radenti.")
tag("FONTE", "Il numero di meteore che arrivano in un punto è proporzionale al seno dell'elevazione del radiante in quel punto: è la stessa correzione con cui l'IMO calcola lo ZHR [5].")
tag("SCELTA", "Opzione \"Scie più lunghe con il radiante basso (DJ5HG)\", spenta di partenza, nel Calcolo dell'efficienza: DJ5HG [18] osserva che con il radiante basso cadono meno meteore per km² ma le scie sono più lunghe (fino a 100 km utili) e soddisfano più spesso la legge di riflessione. Con l'opzione accesa il peso diventa min(sin El, 15/100): lo spessore utile dello strato, 15 km, diviso il seno dell'elevazione dà la lunghezza della scia, limitata a 100 km. Sopra circa 9° di elevazione i due effetti si compensano; spenta, il calcolo resta prudente.")
tag("SCELTA", "Impostazioni pronte del calcolo, nella stessa riga: \"Prudente\" (di partenza, i valori più prudenti: quota dal radar, scie normali, con β), \"Come DJ5HG\" (102 km, scie lunghe, con β) e \"Personalizzata\", che si seleziona da sola quando si cambia a mano la quota, la casella \"dal radar\", le scie lunghe o l'angolo β.")
tag("RILIEVO", "Effetto dell'angolo β sulla direzione migliore, tratta di 1000 km: senza β il massimo cade tra 15° e 90° dalla tratta secondo l'elevazione del radiante (30° con il radiante a 30°, perpendicolare con il radiante a 60°) e il radiante perpendicolare vale il 67 % con il radiante a 30°; con β il massimo è sempre con il radiante lungo la tratta e il radiante perpendicolare scende al 15 %. Con β si perde quindi la regola della direzione migliore di SM6FHZ e di DH9GCD: per questo β è un'opzione, accesa di partenza perché dà i valori più prudenti (nessuna scia è sopravvalutata).")
tag("FONTE", "Due tesi sulla direzione migliore del radiante. Tesi classica dei radioamatori: il radiante migliore è alto tra 15° e 70° e di traverso alla tratta, quello allineato alla tratta è marginale. La sostengono SM6FHZ [4] con le sue regole sperimentali, DH9GCD con la sua formula (riportata da DF5HC [16]) e meteor-mcp di qso-graph [31], che la motiva con la condizione di tangenza: le scie utili devono essere tangenti a un ellissoide con i fuochi nelle due stazioni, e quelle che corrono lungo la tratta lo sono di rado. Questa tesi conta dove le scie possono riflettere, ma non quanto riflette ciascuna.")
tag("FONTE", "Tesi della formula completa: McKinley [8] e l'ITU-R P.843 [24] danno alla potenza di ogni scia il fattore 1 / (1 − cos²β sin²φ), dove β è l'angolo tra la scia e il piano della tratta. Una scia che giace nel piano (β = 0) riflette 1/cos²φ volte più di una che lo attraversa (β = 90°): 10-15 dB tra 600 e 2000 km. Con il radiante allineato alla tratta le scie tangenti giacciono vicino al piano e pesano di più; con il radiante di traverso lo attraversano e pesano meno. DJ5HG [18] usa lo stesso fattore, e le sue curve orarie hanno la forma che YA-MS ritrova con β acceso (scarto di forma circa 3 dB).")
tag("RILIEVO", "Le due tesi usano la stessa condizione di riflessione speculare ma pesano le scie in modo diverso: la classica conta le scie utili, la completa ne pesa anche la potenza. Su 1000 km, con il radiante a 30°, il radiante perpendicolare vale il 67 % senza β e il 15 % con β. Un primo confronto con conteggi reali non le distingue (paragrafo seguente): per decidere servono tratte più lunghe e più ricevitori.")
tag("RILIEVO", "Confronto con conteggi reali: rilevamenti BRAMS ricevuti a Sonneberg (radiofaro di Dourbes, 49,97 MHz, tratta di 471 km) dal 12 al 28 agosto 2026, circa 97 000 echi rilevati con il metodo di M. Bundscherer [34]. Tolto il fondo (mediana ora per ora dal 22 al 27 agosto), le Perseidi aggiungono al massimo, il 13 agosto tra le 02 e le 10 UTC, circa 80-130 echi/ora su 300-470: a 50 MHz pesano poco rispetto alle sporadiche. L'eccesso orario segue il calcolo di YA-MS (efficienza delle Perseidi × ZHR) con correlazione 0,44 con β acceso e 0,43 con β spento, la stessa che dà lo ZHR per il seno dell'elevazione del radiante; con le scie lunghe scende a 0,36. Su questa tratta corta la geometria non aggiunge informazione e il confronto non decide tra le due tesi. Limiti: un solo ricevitore, soglia di rilevamento adattiva che può ridurre i conteggi nelle ore di maggiore attività, sciami minori ancora attivi nei giorni del fondo, antenna del radiofaro rivolta verso lo zenit.")
tag("RILIEVO", "Confronto con gli spot reali: 181 767 spot MSK144 su 50 MHz del Meteor Scatter QSO Party di HamSCI dell'11-12 agosto 2025 (Perseidi, stazioni quasi tutte nordamericane, 5207 tratte tra 300 e 2300 km) [35]. Ora per ora il numero di tratte con spot segue l'indice della tratta calcolato dal programma: correlazione 0,77 con l'angolo β acceso e 0,66 con β spento (sui ranghi 0,72 e 0,68), con il massimo tra le 10 e le 12 UTC in entrambi i giorni; quelle ore coincidono però anche con il massimo delle meteore sporadiche e con l'attività degli operatori. A parità di stazioni attive nella stessa ora, né il programma (β acceso o spento) né la formula di DH9GCD distinguono le coppie che si sono sentite da quelle che non si sono sentite (AUC 0,51-0,53, dove 0,5 vale a caso): quale coppia si sente dipende dalle meteore sporadiche, che l'indice non contiene, e dall'attività. Questi dati confermano l'andamento orario ma non distinguono le due tesi su β. Strumenti: opzione --indici-tratte del programma e tools/verifica_spot.py.")
tag("SCELTA", "Nel programma la casella \"Angolo β tra scia e tratta (McKinley completo)\" è accesa di partenza perché non sopravvaluta nessuna scia (valore prudente); spenta, applica la tesi classica. La casella \"Giudizio classico\" aggiunge sotto ogni sciame, nella tabella oraria, la riga del verdetto classico calcolato al punto medio della tratta: ✗ radiante sotto l'orizzonte, ◐ marginale (sotto 15° o sopra 70°, oppure a meno di 30° dalla direzione della tratta), ● buono, ★ migliore (tra 15° e 70° e a più di 60° dalla direzione della tratta), con le soglie di meteor-mcp [31]. Non cambia il calcolo: mostra ora per ora dove le due tesi concordano e dove no.")
h2("6.3 La percentuale")
tag("SCELTA", "Per ogni direzione del radiante si sommano i pesi di tutti i punti dove la scia riflette. Il 100% è la posizione del radiante più favorevole per quella tratta:")
tag("SCELTA", "Accanto alla percentuale, che vale per quella tratta sola, il programma dà l'efficienza in dB riferita al riferimento fisso di DJ5HG [18]: 0 dB è il massimo di una tratta nord-sud di 1000 km a cavallo dell'equatore con il radiante sull'equatore celeste all'equinozio (il radiante sale da est, passa per lo zenit e tramonta a ovest), calcolato con la stessa quota e gli stessi pesi. Così tratte diverse si confrontano tra loro. DJ5HG dichiara per i suoi valori una precisione migliore di 6 dB.")
eq("η = 100 · F(radiante) / F(posizione migliore)  %")
tag("RILIEVO", "Confronto con QTFGUI di DJ5HG (esempio del suo manuale): tratta Amburgo JO53IM - Barcellona, Quadrantidi, 4 gennaio. QTFGUI dà alle 07:00 UTC puntamento 252°, elevazione 1°, efficacia relativa -8 dB, radiante nella zona di riflessione az. 83° el. 75°; alle 08:00 nessuna zona di riflessione; alle 09:00 puntamento 168°, elevazione 2°, -4 dB, radiante az. 292° el. 74°. Il modello del programma (quota 102 km come QTFGUI) dà alle 07:00 241°, 0°, -5,4 dB, radiante az. 77° el. 74°; alle 08:00 0,6 % (-22 dB), cioè praticamente nulla; alle 09:00 161°, 4°, -4,0 dB, radiante az. 286° el. 75°. Nella stessa ora DH9GCD dà 26 %, 2 % e 32 %: tutti e tre i metodi vedono il buco delle 08:00, con il radiante quasi allo zenit. [17]")
tag("RILIEVO", "Confronto con le curve di DJ5HG [18] (Bild 8 e 9: da Amburgo e da Monaco, Quadrantidi, 4 gennaio), lette dal grafico (circa ±0,5 dB e ±15 min) e confrontate con la prova automatica del programma (--prova-dj5hg, un valore ogni ora). Orari: il buco con il radiante vicino allo zenit cade nelle stesse ore (Barcellona 7,5–8,5 UTC in DJ5HG, 7–9 nel programma; Sofia 6,6–7,8 e 7–8; Narvik 7–8,5 e 7–9); Mosca è chiusa dalle 3 alle 10 in entrambi, e il programma conferma il testo di DJ5HG: da Amburgo aperta fino alle 2:30 circa, da Monaco fino alle 0:30 circa. Puntamenti: scarti di 2–10° (Barcellona 225° e 233° contro 223° e 235° prima del buco, 160° contro 169° dopo; Mosca 84° contro 82°, 79° contro 76°; Narvik salta verso 338° alle 20:40 in DJ5HG, tra le 20 e le 21 nel programma). Livelli e forma, a 102 km (scarto medio e scarto tipico rispetto alle curve): senza β e senza scie lunghe −1,6 e 4,0 dB; con le scie lunghe +1,1 e 4,6 dB; con l'angolo β −5,4 e 6,2 dB, ma con la forma migliore (3,0 dB tolto lo scarto medio, contro 3,6): compaiono i minimi profondi con il radiante basso (Barcellona −15,6 dB alle 17, contro −16 dB alle 19:36; Sofia −18,5 dB alle 20, contro −14 dB). Con β e scie lunghe (impostazione \"come DJ5HG\") −2,2 e 4,7 dB; l'impostazione prudente (quota del radar, 89,5 km, con β, senza scie lunghe) dà −6,9 e 7,6 dB, con forma 3,3 dB. Senza β il programma vede appena il minimo con il radiante basso quasi allineato alla tratta (−8,6 e −10,4 dB): è il caso della riserva di DJ5HG, per questo resta l'avviso.")
tag("RILIEVO", "La documentazione di MS-Soft 5.2 [25] definisce l'efficienza di OH5IY come indice relativo per le sole scie sottodense, con due fattori: elevazione del radiante (ottimo circa 45°) e angolo con la tratta (90° = massimo). Il minimo è portato a mano al 20 % per le sovradense; la formula non è pubblicata. MCG_MS [3] calcola l'efficienza per quattro direzioni fisse e, scrivendo il locator del corrispondente, anche per la tratta reale.")

h1("7. Come leggere i risultati")
h2("7.1 Lato delle riflessioni (A / B)")
tag("SCELTA", "Per ogni ora il programma calcola quale parte delle riflessioni cade a sinistra della tratta (lato A) e quale a destra (lato B). Nella tabella oraria compare la lettera del lato prevalente.")
tag("FONTE", "Conviene spostare il puntamento di 10-30° verso quel lato (side-scatter) [1].")
h2("7.2 Indice della tratta")
tag("SCELTA", "L'indice riassume in un numero quanto il complesso degli sciami favorisce la tratta in un'ora:")
eq("I = Σ  ZHR · η / 100   (su tutti gli sciami attivi)")
h2("7.3 Colore dei radianti")
p("Sulla volta celeste il pallino del radiante è giallo con efficienza ≥ 50% e ZHR ≥ 2, arancio con efficienza ≥ 20%, rosso scuro sotto il 20%, grigio quando lo sciame è quasi inattivo.")

h2("7.4 Zone PREV in pianta")
tag("SCELTA", "Per l'ora mostrata il programma somma, punto per punto dello strato E, il contributo di ogni sciame attivo all'efficienza (la stessa condizione di riflessione speculare del capitolo 5), pesato con lo ZHR. I punti con almeno il 3 % del massimo formano le zone PREV, una per lato della tratta, disegnate in pianta come ellissi: centro = media pesata dei punti, assi = due volte la loro dispersione. È la regola pratica: se lo sciame scorre da nord a sud, le scie utili cadono a est e a ovest. La linea gialla indica la direzione di scorrimento (azimut del radiante) dello sciame selezionato, o del più favorevole.")
h2("7.5 Sezione vista dall'antenna")
tag("SCELTA", "La sezione mostra le stesse scie viste dalla stazione con l'antenna puntata verso il corrispondente: in orizzontale l'azimut rispetto al corrispondente (A a sinistra, B a destra), in verticale l'elevazione. Per ogni sciame si prendono i 14 punti di riflessione più forti; ogni scia è un segmento orientato verso il radiante, da 10 km sopra a 10 km sotto la quota delle scie (al massimo 60 km per lato), più spesso quanto più è probabile. Sono disegnati anche il lobo dell'antenna (cerchio a −3 dB attorno all'elevazione del lobo), il corrispondente e Hot A / Hot B.")

h1("8. Frequenza di lavoro e attenuazione")
h2("8.1 Regole tra le bande")
tag("FONTE", "Regole sperimentali di SM6FHZ [4]: il numero e l'intensità delle riflessioni scalano con λ³, la durata con λ². In forward scatter la durata cresce anche con sec²φ (τ = λ²·sec²φ / 16π²D, McKinley [8]; OH5IY [25]): il radar di Collm misura in backscatter (φ = 0), quindi sulla tratta la durata va moltiplicata per sec²φ al punto medio (×4 a 60°, ×8,5 a 70°, ×33 a 80°).")
tag("RILIEVO", "Misure reali (HamSCI, Meteor Scatter QSO Party [29]): R. Suggs NN4NT ha misurato la costante di decadimento della potenza di 1298 echi sottodensi nelle registrazioni MSK144 di NN4SA (EM64) durante le Perseidi 2026 (4736 file WAV di WSJT-X). Mediane: 148 ms a 28,145 MHz (41 echi), 78 ms a 50,260 MHz (1198), 53 ms a 144,150 MHz (59). Con λ² partendo dai 6 m sarebbero circa 245 ms e 9,5 ms: in 2 m i ping durano più di cinque volte quanto previsto. L'autore lo attribuisce a un probabile effetto del soffitto di quota in 2 m: alle frequenze alte restano visibili soprattutto le scie basse, dove la diffusione è più lenta. È un'analisi preliminare: una sola stazione ricevente, distanze diverse non normalizzate con sec²φ, solo gli echi abbastanza forti da essere rilevati.")
tag("FONTE", "Weitzen e Ralston [27]: la costante di decadimento varia da scia a scia con distribuzione esponenziale, con media τ = λ²·sec²φ / (32π²D) (costante della potenza; 16π² vale per l'ampiezza). Xia, Li e Zheng [28] danno D in funzione della quota, D = 10^(0,067·h − 5,6) m²/s: su 1000 km con la scia a 95 km risulta τ ≈ 47 ms a 144 MHz e 390 ms a 50 MHz. Il valore a 144 MHz è vicino alla mediana misurata, quello a 50 MHz è cinque volte più alto: D cresce di 10 volte ogni 15 km di quota, quindi la quota delle scie visibili, che cambia con la frequenza, pesa sulla durata più di λ².")
tag("SCELTA", "Il programma offre la scelta \"Durata dei ping tra le bande\" nella sottolinguetta Geometria e attenuazione. Teorica (di partenza, prudente): λ², che dà i ping più brevi. Osservata: interpolazione lineare in scala logaritmica tra le tre mediane di NN4SA; sotto 28 MHz si prolunga il tratto 10–6 m, sopra 144 MHz, dove non ci sono misure, si torna a λ². Con la scelta osservata un eco di 1 s a Collm (36,2 MHz) dura circa 473 ms a 144 MHz invece di 63 ms, e da 50 a 144 MHz i ping si accorciano di 1,5 volte invece di 8.")
tag("RILIEVO", "In McKinley [8] λ³ è la potenza di una singola scia sottodensa, non il numero di scie. A soglia fissa e con indice di massa s, il numero di scie sopra soglia scala con λ elevato a 1,5·(s − 1), cioè circa λ^1,5 per s = 2 (IZ5TEK [26]; OH5IY [25]). Il programma tiene k = 3, la regola sperimentale di SM6FHZ [4], e lo dichiara: con k = 3, 1000 meteore/ora a Collm diventano circa 16 riflessioni/ora a 144 MHz, con k = 1,5 circa 127. Gli osservatori RMOB del radar GRAVES a 143,050 MHz [13] contano in genere da 20 a 140 eco/ora; il valore giusto di k per la propria stazione si ricava dal confronto con RMOB (paragrafo seguente).")
tag("FONTE", "Durata massima di un ping secondo IARU Regione 1: 1000 ms a 50 MHz, 500 ms a 70 MHz, 100 ms a 144 MHz, 13 ms a 432 MHz [1].")
h2("8.2 Dal radar alla banda radioamatoriale")
eq("N(f) = N(36,2 MHz) · (36,2 / f)^k · K        con k = 3")
tag("RILIEVO", "Il valore di k per la propria stazione si ricava dal confronto con un osservatore RMOB sulla stessa banda: k = 3 è la regola di SM6FHZ, la teoria per scie sottodense con indice di massa 2 dà circa 1,5.")
tag("SCELTA", "Il pulsante \"k dagli indici di popolazione\" calcola per ogni sciame attivo k = 1,5·(s − 1) con s = 1 + 2,5·log10 r, cioè k = 3,75·log10 r, e ne fa la media pesata con lo ZHR. L'indice di popolazione r viene dalla tabella della pagina del flusso del Global Meteor Network [33] quando c'è, altrimenti dal catalogo IMO [5]; la linguetta Sciami mostra k per ogni sciame. Esempi: Perseidi r = 2,2, k = 1,28; Geminidi r = 2,6, k = 1,56. Il valore di partenza resta k = 3 di SM6FHZ [4], più prudente; i conteggi di Collm sono però per lo più meteore sporadiche, di cui il GMN non pubblica r.")
tag("FONTE", "Conteggi del Global Meteor Network [33]: nella linguetta Sciami in diretta e nella colonna \"GMN oggi\" della linguetta Sciami il programma legge il riassunto giornaliero delle traiettorie confermate dalle telecamere della rete (una riga per meteora, con il codice IAU dello sciame o \"...\" per le sporadiche) e le conta per sciame. È un conteggio, non un flusso: dipende da quante stazioni hanno il cielo sereno e buio. Dati CC BY 4.0.")
h2("8.3 Attenuazione di tratta")
eq("L = 10 · log10 [ 16π² · R1 · R2 · (R1 + R2) · (1 − cos²β · sin²φ) / (λ³ · q² · re²) ] − 10 · log10 a1        a1 = exp[ −8π² · r0² / (λ² · sec²φ) ]")
tag("FONTE", "McKinley [8] e Raccomandazione ITU-R P.843 [24]: β angolo tra la scia e il piano della tratta, a1 fattore del raggio iniziale della scia, con log10 r0 = 0,035 h − 3,45 (r0 in m, h in km). Nel bilancio si usa β = 90°, il caso più sfavorevole (valore prudente), e si mostra anche il caso migliore, β = 0.")
tag("FONTE", "Riferimenti: 172–190 dB dai calcoli di G4BAO, riportati da GM8JBJ (da Kaiser & Closs [9]); circa 200 dB in media a 144 MHz (OH5IY); segnale minimo ricevibile −130 dBm [1].")
tag("RILIEVO", "Con q = 10¹⁴ elettroni/m, scie a 89,5 km e β = 0, a 144 MHz risultano 182–192 dB tra 600 e 2100 km (185 dB a 1000 km). L'intervallo di 172–190 dB calcolato da John Worsnop G4BAO nella sua tesi di dottorato, riportato da GM8JBJ [9], comprende questi valori. Con β = 90° l'attenuazione cresce di 10 dB a 600 km, 13 dB a 1000 km e 16 dB a 2100 km: i 200 dB medi di OH5IY citati nell'articolo [1] stanno tra i due casi. Sempre secondo GM8JBJ, G4BAO trova circa 6 dB in meno per le scie allineate alla tratta.")
tag("RILIEVO", "I 182 dB della tabella di GM8JBJ [9] non sono una conferma: la tabella non indica la frequenza, i suoi 86,4 dB per tratto sono la perdita in spazio libero su 500 km a 1 MHz (manca il termine 20 log f: a 144 MHz sono 129,6 dB) e la somma delle voci, 86,4 + 0 − 9 + 86,4, fa 163,8 dB e non 182. La pagina non parla né di valore minimo né di 144 MHz.")
tag("RILIEVO", "Raggio iniziale alla quota media degli echi, h = 124 − 17 log f [24]: r0 = 0,76 m a 95 km per 50 MHz, 0,40 m a 87 km per 144 MHz, 0,21 m a 79 km per 432 MHz. Su 1000 km a1 vale 0,2 dB a 50 MHz, 0,6 dB a 144 MHz e 1,4 dB a 432 MHz (2,9 dB a 600 km). Alla quota fissa di 102 km di DJ5HG darebbe a 432 MHz circa 70 dB, cioè nessun eco: per questo si usa la quota media degli echi alla frequenza.")
tag("RILIEVO", "Incertezza del raggio iniziale: Stober et al. [30], con il radar CMOR a 17,45, 29,85 e 38,15 MHz e un modello di diffusione a onda piena, trovano tra 85 e 95 km r0 di 0,5–2 m, per lo più 1–1,5 m, con una dispersione di un fattore due a ogni quota; per la polarizzazione trasversale i valori sono circa il doppio delle misure precedenti (Greenhow e Hall 1960; Jones e Campbell-Brown 2005). Solo il 5 % circa degli echi si lascia descrivere dal modello ideale. La formula ITU-R P.843 [24] dà 0,5 m a 90 km e 0,75 m a 95 km, cioè il limite basso di queste misure.")
tag("SCELTA", "Il programma offre la scelta \"Raggio iniziale della scia\" nella sottolinguetta Geometria e attenuazione: doppio dell'ITU (di partenza, prudente, come le misure di Stober et al.), ITU-R P.843, escluso. Raddoppiando r0 il fattore a1 in dB si moltiplica per 4: su 1000 km 0,8 dB a 50 MHz, 2,4 dB a 144 MHz e 5,6 dB a 432 MHz (11,6 dB a 600 km). Le misure CMOR sono a frequenze più basse e a 85–95 km: usarle a 432 MHz, dove gli echi vengono da circa 79 km, è un'estrapolazione.")

h1("9. Limiti noti")
li("Il modello considera solo le scie sottodense. Le sovradense (i burst lunghi) e il fondo sporadico non entrano nell'efficienza; il fondo sporadico è rappresentato dal flusso radar.")
li("Il lobo verticale è un modello semplice: antenna orizzontale, lobo gaussiano largo θV a −3 dB (Kraus) e fattore del terreno fino al primo massimo; non si considerano i lobi successivi, l'altezza reale dell'antenna e il terreno attorno.")
li("Le derive del radiante e i coefficienti B del profilo di attività sono valori di lavoro.")
li("Le percentuali vanno confrontate con MCG_MS, MS-Soft e con le osservazioni in banda.")

SOURCES = [
 "C. Cerrotta IC8TEM, G. Sartori IV3GTH - \"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese\", articolo, versione 7 (fonte principale).",
 "I. Yrjölä OH5IY - MS-Soft, www.kolumbus.fi/oh5iy (sito storico).",
 "W. Rauh DL5MCG - MCG_MS, MS Efficiency Calculator v1.61, qsl.net/dl5mcg.",
 "SM6FHZ - \"432 MHz Meteorscatter, Challenges and Techniques\", 45th Nordic VUSHF, maggio 2025.",
 "International Meteor Organization - Meteor Shower Calendar 2026 e 2027, www.imo.net.",
 "J. Meeus - Astronomical Algorithms, 2ª ed., Willmann-Bell, 1998.",
 "Radar meteorico di Collm, Università di Lipsia (LIM) e IAP Kühlungsborn, wetterdaten.meteo.uni-leipzig.de/radar_flux.php.",
 "D.W.R. McKinley - Meteor Science and Engineering, McGraw-Hill, 1961.",
 "GM8JBJ - Meteor scatter path loss, hamradio.engineering (da Kaiser & Closs, 1952).",
 "G. Hoch DL6WU - curva del guadagno delle Yagi lunghe, riportata da W8IO, www.w8io.com.",
 "J.D. Kraus - Antennas, McGraw-Hill.",
 "L.B. Cebik W4RNL - Long-Boom Yagi Rules of Thumb: A Comparison with Modeling Data.",
 "RMOB, Radio Meteor Observatories On Line - www.rmob.org, bollettino di giugno 2018.",
 "AMS Bulletin n. 203, \"The AMS Radiometeor Project\", tabella degli offset d'antenna, ripresa da W8WN, qsl.net/w8wn/hscw/papers/ms_az_el.html.",
 "LZ2HV - MSHV, programma per i modi digitali MS (calcolo di Hot A / Hot B).",
 "J. DF5HC - \"Meteorscatter auf UKW\", conferenza DARC, gennaio 2018 (formula della migliore direzione di DH9GCD; diffusione a cono e HOT-A / HOT-B di DJ5HG, \"Meteorscatter Propagation\", www.vhfdx.de/mseff/MS-Geometrie.pdf; meteore sporadiche di KB0VUK).",
 "K. von der Heide DJ5HG - QTFGUI, programma per i puntamenti in aurora, FAI e meteor scatter, con manuale \"QTFGUI Help\" (2007) e dati meteorshowerdata.txt.",
 "K. von der Heide DJ5HG - \"Die Geometrie von Meteorscatterverbindungen\", agosto 2004 (legge del cono, efficienza relativa a riferimento fisso, scie utili fino a 100 km, quota 102 km).",
 "J. Richardson (AMS) - \"Some Notes and Equations for Forward Scatter\": scarti d'antenna di 13°, 11°, 10° e 10° a 1000, 1250, 1500 e 2000 km, tabella riportata da DJ5HG.",
 "V.R. Eshleman, R.F. Mlodnosky - \"Directional Characteristics of Meteor Propagation Derived from Radar Measurements\", Proc. IRE 45(12), 1715-1723, 1957.",
 "M.L. Meeks, J.C. James - \"On the Influence of Meteor-Radiant Distributions in Meteor-Scatter Communication\", Proc. IRE 45(12), 1724-1733, 1957.",
 "C.O. Hines - \"Diurnal Variations in the Number of Shower Meteors Detected by the Forward-Scattering of Radio Waves, Part I: Theory\", Can. J. Phys. 33, 493-503, 1955.",
 "P.A. Forsyth, C.O. Hines, E.L. Vogan - stesso titolo, \"Part II: Experiment\", Can. J. Phys. 33, 600-606, 1955.",
 "ITU-R P.843-1 - \"Communication by meteor-burst propagation\", 1997.",
 "I. Yrjölä OH5IY - \"Meteors & Communication\", parte 2, documentazione di MS-Soft 5.2 (2017).",
 "R. Pardini IZ5TEK - \"Il meteor-scatter e i collegamenti radioamatoriali via meteor-scatter\", ARI Pisa, 2014.",
 "J.A. Weitzen, W.T. Ralston - \"Meteor Scatter: An Overview\", IEEE Transactions on Antennas and Propagation 36(12), 1813-1819, 1988.",
 "B. Xia, L. Li, Y. Zheng - \"Modeling and Simulation of the Meteor Burst Channel\", Telecommunications Science, 2016 (9), DOI 10.11959/j.issn.1000-0801.2016206 (English translation by R. Hipple, github.com/HamSCI/MSQP).",
 "R. Suggs NN4NT, HamSCI Meteor Scatter Working Group - \"MSQP data analysis progress\", 4 November 2026, underdense_decay, github.com/HamSCI/MSQP (NN4SA, 2026 Perseids, Zenodo).",
 "G. Stober, P. Brown, M. Campbell-Brown, R.J. Weryk - \"Triple-frequency meteor radar full wave scattering: Measurements and comparison to theory\", Astronomy & Astrophysics, 2021, arXiv:2108.07647.",
 "meteor-mcp, qso-graph - meteor scatter MCP server, github.com/qso-graph/meteor-mcp, 2026.",
 "IAU Meteor Data Center - established showers list, www.ta3.sk/IAUC22DB/MDC2022 (Jenniskens et al., Planetary and Space Science 182, 104821, 2020; Jopek & Kaňuchová, Planetary and Space Science 143, 3-6, 2017).",
 "Global Meteor Network - shower flux and daily trajectory summary, globalmeteornetwork.org, CC BY 4.0 (Vida et al. 2021, 2022).",
 "M. Bundscherer - \"Meteor Detection based on Forward Scattering with SDR and the BRAMS Beacon\", WGN, Journal of the IMO 54(2), April 2026; code and data (Sonneberg, August 2026): github.com/maxbundscherer/meteor-scatter-v2.",
 "HamSCI Meteor Scatter QSO Party, 11-12 August 2025 - scoring files and cleansed PSKReporter data (G. Mikitin, N. Frissell), Zenodo, DOI 10.5281/zenodo.18109759, CC BY 4.0.",
]

TAGCOL = {"FONTE": (0x38, 0xBD, 0xF8), "RILIEVO": (0x86, 0xEF, 0xAC), "SCELTA": (0xFB, 0x92, 0x3C)}
TAGCOL_DOC = {"FONTE": (0x1F, 0x5F, 0xAD), "RILIEVO": (0x2E, 0x7D, 0x32), "SCELTA": (0xB4, 0x53, 0x09)}

# ---------------- RTF (per la linguetta, fondo scuro) ----------------
def rtf_esc(t):
    out = []
    for ch in t:
        o = ord(ch)
        if ch in '\\{}': out.append('\\' + ch)
        elif o < 128: out.append(ch)
        else:
            if o > 32767: o -= 65536
            out.append('\\u%d?' % o)
    return ''.join(out)

def build_rtf(path):
    # pagina chiara: testo scuro, titoli blu e viola, etichette blu/verde/arancio scuri, formule blu notte
    cols = [(0x1E, 0x1E, 0x2A), (0x1F, 0x38, 0x64), (0x5B, 0x21, 0xB6), (0x2E, 0x7D, 0x32), (0xB4, 0x53, 0x09), (0x1E, 0x3A, 0x8A), (0x60, 0x60, 0x60)]
    # indici: 1 testo, 2 titolo, 3 sottotitolo viola, 4 verde, 5 arancio, 6 blu (formule e FONTE), 7 grigio
    ct = '{\\colortbl;' + ''.join('\\red%d\\green%d\\blue%d;' % c for c in cols) + '}'
    ft = '{\\fonttbl{\\f0\\fswiss Segoe UI;}{\\f1\\froman Cambria Math;}}'
    tagidx = {"FONTE": 6, "RILIEVO": 4, "SCELTA": 5}
    o = ['{\\rtf1\\ansi\\ansicpg1252\\deff0', ft, ct, '\\viewkind4\\uc1\\pard\\sa120\\f0\\fs22\\cf1 ']
    o.append('\\pard\\sa60\\cf2\\b\\fs40 ' + rtf_esc(TITLE) + '\\b0\\par')
    o.append('\\pard\\sa240\\cf7\\i\\fs20 ' + rtf_esc(SUB) + '\\i0\\par')
    for b in B:
        k = b[0]
        if k == 'h1': o.append('\\pard\\sb360\\sa120\\keepn\\cf2\\b\\fs32 ' + rtf_esc(b[1]) + '\\b0\\par')
        elif k == 'h2': o.append('\\pard\\sb200\\sa80\\keepn\\cf3\\b\\fs25 ' + rtf_esc(b[1]) + '\\b0\\par')
        elif k == 'p': o.append('\\pard\\sa120\\cf1\\fs22 ' + rtf_esc(b[1]) + '\\par')
        elif k == 'tag': o.append('\\pard\\sa120\\li240\\fs22\\cf%d\\b [%s]\\b0\\cf1  %s\\par' % (tagidx[b[1]], b[1], rtf_esc(b[2])))
        elif k == 'eq': o.append('\\pard\\qc\\sb80\\sa160\\f1\\i\\cf6\\fs24 ' + rtf_esc(b[1]) + '\\i0\\f0\\par')
        elif k == 'li': o.append('\\pard\\sa80\\li480\\fi-240\\cf1\\fs22 \\u8226?  ' + rtf_esc(b[1]) + '\\par')
    o.append('\\pard\\sb360\\sa120\\keepn\\cf2\\b\\fs32 ' + rtf_esc(T('10. Fonti')) + '\\b0\\par')
    for i, s in enumerate(SOURCES, 1):
        o.append('\\pard\\sa80\\li480\\fi-360\\cf1\\fs21 %d.\\tab %s\\par' % (i, rtf_esc(s)))
    o.append('}')
    open(path, 'w', encoding='ascii').write('\n'.join(o))

# ---------------- DOCX (esportazione in Word, fondo bianco) ----------------
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
    d.add_heading(T('10. Fonti'), level=1)
    for s in SOURCES: d.add_paragraph(s, style='List Number')
    if LANG in ('ar', 'he', 'ur'):   # lingue da destra a sinistra: paragrafi e testo RTL
        from docx.oxml.ns import qn
        from docx.oxml import OxmlElement
        for para in d.paragraphs:
            para._p.get_or_add_pPr().append(OxmlElement('w:bidi'))
            for r in para.runs: r._r.get_or_add_rPr().append(OxmlElement('w:rtl'))
    d.save(path)

def build_txt(path):
    # formato semplice letto da YA-MS (una riga per blocco): TIPO|testo  oppure  TAG|tipo|testo
    o = ['TITLE|' + TITLE, 'SUB|' + SUB]
    for b in B:
        o.append('|'.join(x.replace('\n', ' ') for x in ((b[0].upper(),) + tuple(b[1:]))))
    o.append('H1|' + T('10. Fonti'))
    for i, s in enumerate(SOURCES): o.append('SRC|%d. %s' % (i + 1, s))
    open(path, 'w', encoding='utf-8').write('\n'.join(o) + '\n')

TITLE, SUB = T(TITLE), T(SUB)
SOURCES = [T(x) for x in SOURCES]
for k in ("FONTE", "RILIEVO", "SCELTA"): T(k)
out = sys.argv[1]
if LANG != 'it':
    out = os.path.join(out, 'spiegazione'); os.makedirs(out, exist_ok=True)
    base = out + '/efficienza_spiegazione_' + LANG
else:
    base = out + '/efficienza_spiegazione'
build_txt(base + '.txt')
build_docx(base + '.docx')
if os.environ.get('ESTRAI'): json.dump(KEYS, open(os.environ['ESTRAI'], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if MISS:
    print('testi senza traduzione (%s): %d' % (LANG, len(MISS)))
    if os.environ.get('MOSTRA'): [print('  ' + m) for m in MISS]
print('ok', LANG, len(B), 'blocchi')
