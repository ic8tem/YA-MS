[English](Getting-Started) · **Italiano** · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Primi passi

Al primo avvio YA-MS mostra una tratta di esempio (JN70CN → JO62QM su 144 MHz). Bastano cinque minuti per impostarlo per la tua stazione.

## 1. Le tre righe di comandi

Sopra le linguette ci sono tre righe di comandi, valide per tutte le linguette. Il pulsante **Comandi** in alto a destra le ripiega e le riapre (utile con i caratteri grandi); la scelta viene ricordata.

**Riga 1 – stazioni e banda**

| Comando | Che cosa fa |
|---|---|
| **Il mio locator** / **quota m** | Il tuo locator Maidenhead (4, 6 o 8 caratteri; si usa il centro del quadrato) e la quota della stazione sul livello del mare. |
| **Corrispondente** / **quota m** | Accanto alla mappa, a destra, c'è il riquadro del corrispondente: scrivi il nominativo e premi Invio, il locator si prende dall'archivio CALL3 (come in YAEC e LIVETROPOVHF); sotto ci sono il locator e la quota. Il nominativo si può scrivere anche nella casella del locator. |
| **Banda MHz** | 28, 50, 70, 144, 222 o 432 MHz: serve per il guadagno e il lobo dell'antenna, la stima del flusso e il bilancio del collegamento. |
| **Calcola** | Ricalcola la tratta (campionamento dello strato E: qualche secondo). |
| **Antenna az** | In alto nel riquadro del corrispondente, accanto alla mappa: azimut della tua antenna, sempre **verso il DX** (azimut della tratta). Sotto, nella stessa colonna, c'è la legenda della mappa. |

**Riga 2 – strato E e antenna**

| Comando | Che cosa fa |
|---|---|
| **Quota scie km** + **dal radar** | Quota delle scie meteoriche (predefinita 90 km). Con *dal radar* spuntato si usa la quota più frequente (moda) misurata dal radar di Collm; vedi [Flusso radar](Radar-Flux-it). |
| **Elevazione lobo °** | Elevazione del massimo del lobo verticale della tua antenna: una direttiva fissata a 0° ha comunque il lobo qualche grado sopra l'orizzonte per la riflessione sul terreno (di solito 3-8°). Con la casella **diagramma d'antenna** accesa (di partenza) i punti dello strato E pesano con il diagramma verticale delle due antenne; spenta, si usano solo i punti che entrambe le stazioni vedono sopra questa elevazione. |
| **Antenna Yagi: boom m** | Lunghezza del boom della tua Yagi. Il programma mostra la lunghezza in λ, il guadagno (curva DL6WU) e il lobo a −3 dB, orizzontale e verticale; vedi [Geometria e attenuazione](Geometry-and-Path-Loss-it#guadagno-e-lobo-dellantenna). Sotto 2 λ la stima è poco precisa. |
| **Hot spot dal punto medio km** + **auto (AMS)** | Distanza di Hot A e Hot B dal punto medio. Con *auto (AMS)* spuntato (predefinito) segue la tabella degli scostamenti d'antenna di J. Richardson (AMS) citata da DJ5HG: 13° a 1000 km, 11° a 1250 km, 10° a 1500 e 2000 km (circa 115, 121, 132 e 176 km dal punto medio). Togli la spunta per inserire a mano 30–400 km (MSHV usa 150 km). |

**Riga 3 – ora**

| Comando | Che cosa fa |
|---|---|
| **Ora** | Orologio UTC. |
| **Data del calcolo (UTC)** | Il giorno del calcolo per [Calcolo previsionale](Sky-View-it) e [Radar GRAVES](GRAVES-Radar-it) (oggi per impostazione predefinita), all'ora attuale del giorno. Anche: il giorno mostrato in [Calcolo dell'efficienza](Efficiency-Calculation-it) e nella cronologia di GRAVES. |
| **Ore (da −12 a +36 h)** | Sposta il momento del calcolo da 12 ore prima a 36 ore dopo quell'ora, a passi di 15 minuti. Accanto: *Calcolo per: adesso* oppure *Calcolo per: gg/mm hh:mm UTC*. |
| **Tempo reale** | Torna al momento attuale. |

## 2. La tua stazione e il DX

1. Scrivi **Il mio locator** e **quota m**.
2. Scrivi locator e quota del **Corrispondente** – oppure fai clic sulla mappa nella [Volta celeste](Sky-View-it): **clic sinistro = locator del corrispondente**, **clic destro = locator della mia stazione**.
3. Scegli la **Banda MHz** e premi **Calcola**.

La barra di stato in basso conferma: *Tratta calcolata: … km, … punti di riflessione campionati in … s*.

## 3. La tua antenna

Inserisci la **lunghezza del boom** della tua Yagi. Il programma ne ricava guadagno e lobo e ti avvisa se Hot A o Hot B cadono già **dentro il lobo** quando l'antenna punta verso il DX (in quel caso sono disegnati in grigio: non serve girare l'antenna).

## 4. Leggere i risultati

| Domanda | Dove guardare |
|---|---|
| Quale sciame aiuta la mia tratta adesso, e da quale lato? | [Volta celeste](Sky-View-it): elenco degli sciami, Hot consigliato in rosso, zone PREV |
| Qual è l'ora migliore oggi? | [Calcolo dell'efficienza](Efficiency-Calculation-it): schede riassuntive e tabella oraria |
| Quante meteore sta contando il radar? | [Flusso radar](Radar-Flux-it) |
| Quanti ping posso aspettarmi su 144 MHz? | [Attuazione sperimentale previsioni](Experimental-Forecasts-it) (sperimentale) |
| La mia stazione riesce a chiudere la tratta? | [Geometria e attenuazione](Geometry-and-Path-Loss-it): attenuazione di tratta e margine |
| Quando c'è il prossimo massimo? | [Sciami](Showers-it) |
| Posso fare una prova con GRAVES? | [Radar GRAVES](GRAVES-Radar-it) |

## Regole pratiche (dalle fonti)

- **Punta perpendicolarmente allo sciame**: la tratta migliore è ortogonale all'azimut del radiante; puntamento migliore = azimut del radiante ±90°, tolleranza ±40–50° (SM6FHZ).
- **Side-scatter**: gira l'antenna di 10–30° verso il lato (A o B) da cui arriva la maggior parte delle riflessioni (articolo Cerrotta–Sartori).
- **Radiante troppo alto** (sopra 70°) o troppo basso (sotto 20°) dà poche scie utili (DF5HC, DH9GCD).
- Le meteore sporadiche hanno il massimo verso le **06 UTC** (articolo; confermato dal flusso di Collm).
- Distanze utili su 432 MHz: 800–2000 km, migliore circa 1400 km (SM6FHZ); distanza migliore in generale 1300–1500 km (DF5HC).

Avanti: [Volta celeste](Sky-View-it).
