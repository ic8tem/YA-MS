# Genera il documento "Come si calcola l'efficienza dello sciame" in due formati dallo stesso testo:
#   efficienza_spiegazione.txt  -> mostrato nella linguetta "Efficienza - spiegazione" di YA-MS
#   efficienza_spiegazione.docx -> esportazione in Word
import sys
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

TITLE = "Come YA-MS calcola l'efficienza di uno sciame"
SUB = "Documento tecnico - a cura di Costantino IC8TEM - novembre 2026"

# Blocchi: ("h1", testo) ("h2", testo) ("p", testo) ("tag", tipo, testo) ("eq", testo) ("li", testo) ("src", testo)
B = []
h1 = lambda t: B.append(("h1", t)); h2 = lambda t: B.append(("h2", t)); p = lambda t: B.append(("p", t))
tag = lambda k, t: B.append(("tag", k, t)); eq = lambda t: B.append(("eq", t)); li = lambda t: B.append(("li", t))

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
tag("SCELTA", "Il programma divide lo strato E in punti ogni 15 km e tiene solo quelli che entrambe le stazioni vedono sopra l'elevazione minima del lobo.")
h2("6.2 Il peso di ciascun punto")
tag("FONTE", "La potenza di una scia sottodensa (McKinley [8]) cresce con λ³ e cala con le distanze R1, R2 dalle stazioni; φ è la metà dell'angolo di scattering:")
eq("peso = 1 / [ R1 · R2 · (R1 + R2) · cos²φ ]")
tag("SCELTA", "L'angolo φ è limitato a 85° per evitare valori infiniti nelle direzioni radenti.")
tag("FONTE", "Il numero di meteore che arrivano in un punto è proporzionale al seno dell'elevazione del radiante in quel punto: è la stessa correzione con cui l'IMO calcola lo ZHR [5].")
tag("SCELTA", "Opzione \"Scie più lunghe con il radiante basso (DJ5HG)\", spenta di partenza, nel Calcolo dell'efficienza: DJ5HG [18] osserva che con il radiante basso cadono meno meteore per km² ma le scie sono più lunghe (fino a 100 km utili) e soddisfano più spesso la legge di riflessione. Con l'opzione accesa il peso diventa min(sin El, 15/100): lo spessore utile dello strato, 15 km, diviso il seno dell'elevazione dà la lunghezza della scia, limitata a 100 km. Sopra circa 9° di elevazione i due effetti si compensano; spenta, il calcolo resta prudente.")
h2("6.3 La percentuale")
tag("SCELTA", "Per ogni direzione del radiante si sommano i pesi di tutti i punti dove la scia riflette. Il 100% è la posizione del radiante più favorevole per quella tratta:")
tag("SCELTA", "Accanto alla percentuale, che vale per quella tratta sola, il programma dà l'efficienza in dB riferita al riferimento fisso di DJ5HG [18]: 0 dB è il massimo di una tratta nord-sud di 1000 km a cavallo dell'equatore con il radiante sull'equatore celeste all'equinozio (il radiante sale da est, passa per lo zenit e tramonta a ovest), calcolato con la stessa quota e gli stessi pesi. Così tratte diverse si confrontano tra loro. DJ5HG dichiara per i suoi valori una precisione migliore di 6 dB.")
eq("η = 100 · F(radiante) / F(posizione migliore)  %")
tag("RILIEVO", "Confronto con QTFGUI di DJ5HG (esempio del suo manuale): tratta Amburgo JO53IM - Barcellona, Quadrantidi, 4 gennaio. QTFGUI dà alle 07:00 UTC puntamento 252°, elevazione 1°, efficacia relativa -8 dB, radiante nella zona di riflessione az. 83° el. 75°; alle 08:00 nessuna zona di riflessione; alle 09:00 puntamento 168°, elevazione 2°, -4 dB, radiante az. 292° el. 74°. Il modello del programma (quota 102 km come QTFGUI) dà alle 07:00 241°, 0°, -5,4 dB, radiante az. 77° el. 74°; alle 08:00 0,6 % (-22 dB), cioè praticamente nulla; alle 09:00 161°, 4°, -4,0 dB, radiante az. 286° el. 75°. Nella stessa ora DH9GCD dà 26 %, 2 % e 32 %: tutti e tre i metodi vedono il buco delle 08:00, con il radiante quasi allo zenit. [17]")
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
tag("RILIEVO", "In McKinley [8] λ³ è la potenza di una singola scia sottodensa, non il numero di scie. A soglia fissa e con indice di massa s, il numero di scie sopra soglia scala con λ elevato a 1,5·(s − 1), cioè circa λ^1,5 per s = 2 (IZ5TEK [26]; OH5IY [25]). Il programma tiene k = 3, la regola sperimentale di SM6FHZ [4], e lo dichiara: con k = 3, 1000 meteore/ora a Collm diventano circa 16 riflessioni/ora a 144 MHz, con k = 1,5 circa 127. Gli osservatori RMOB del radar GRAVES a 143,050 MHz [13] contano in genere da 20 a 140 eco/ora; il valore giusto di k per la propria stazione si ricava dal confronto con RMOB (paragrafo seguente).")
tag("FONTE", "Durata massima di un ping secondo IARU Regione 1: 1000 ms a 50 MHz, 500 ms a 70 MHz, 100 ms a 144 MHz, 13 ms a 432 MHz [1].")
h2("8.2 Dal radar alla banda radioamatoriale")
eq("N(f) = N(36,2 MHz) · (36,2 / f)^k · K        con k = 3")
tag("RILIEVO", "Il valore di k per la propria stazione si ricava dal confronto con un osservatore RMOB sulla stessa banda: k = 3 è la regola di SM6FHZ, la teoria per scie sottodense con indice di massa 2 dà circa 1,5.")
h2("8.3 Attenuazione di tratta")
tag("FONTE", "Riferimenti dell'articolo a 144 MHz: almeno 182 dB (GM8JBJ, da Kaiser & Closs [9]) e circa 200 dB in media (OH5IY); segnale minimo ricevibile −130 dBm [1].")
tag("RILIEVO", "Con l'equazione di McKinley [8] e una scia di 10^14 elettroni/m, a 144 MHz risultano da 181 a 192 dB tra 600 e 2200 km: in linea con i 182 dB dell'articolo.")

h1("9. Limiti noti")
li("Il modello considera solo le scie sottodense. Le sovradense (i burst lunghi) e il fondo sporadico non entrano nell'efficienza; il fondo sporadico è rappresentato dal flusso radar.")
li("Nel calcolo dell'efficienza le antenne sono considerate isotrope; il lobo reale serve solo per il controllo degli Hot.")
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
    o.append('\\pard\\sb360\\sa120\\keepn\\cf2\\b\\fs32 ' + rtf_esc('10. Fonti') + '\\b0\\par')
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
            r = para.add_run('[' + b[1] + '] '); r.bold = True; r.font.color.rgb = RGBColor(*TAGCOL_DOC[b[1]])
            para.add_run(b[2])
        elif k == 'eq':
            para = d.add_paragraph(); para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = para.add_run(b[1]); r.italic = True; r.font.name = 'Cambria Math'; r.font.size = Pt(12)
        elif k == 'li': d.add_paragraph(b[1], style='List Bullet')
    d.add_heading('10. Fonti', level=1)
    for s in SOURCES: d.add_paragraph(s, style='List Number')
    d.save(path)

def build_txt(path):
    # formato semplice letto da YA-MS (una riga per blocco): TIPO|testo  oppure  TAG|tipo|testo
    o = ['TITLE|' + TITLE, 'SUB|' + SUB]
    for b in B:
        o.append('|'.join(x.replace('\n', ' ') for x in ((b[0].upper(),) + tuple(b[1:]))))
    o.append('H1|10. Fonti')
    for i, s in enumerate(SOURCES): o.append('SRC|%d. %s' % (i + 1, s))
    open(path, 'w', encoding='utf-8').write('\n'.join(o) + '\n')

out = sys.argv[1]
build_txt(out + '/efficienza_spiegazione.txt')
build_docx(out + '/efficienza_spiegazione.docx')
print('ok', len(B), 'blocchi')
