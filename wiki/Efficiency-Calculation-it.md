[English](Efficiency-Calculation) · **Italiano** · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh)

# Calcolo dell'efficienza

*Linguetta: Calcolo previsionale › Calcolo dell'efficienza.*

[![Calcolo dell'efficienza](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/it-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/it-2_3.png)

L'**efficienza** di uno sciame dice, in percentuale, quanto la posizione del suo radiante consente riflessioni sulla **tua** tratta. Il concetto è di Ilkka **OH5IY** (MS-Soft) ed è ripreso nell'articolo Cerrotta–Sartori: il massimo di efficienza non coincide con il massimo visuale (ZHR), perché dipende da dove si trova il radiante rispetto alle due stazioni. MCG_MS di DL5MCG applica la stessa idea a quattro direzioni fisse; YA-MS la calcola per la **tratta reale** tra i due locator.

Questa linguetta la mostra ora per ora per il giorno scelto in *Giorno per la tabella 24 h (UTC)* (valori alla mezza di ogni ora).

## Schede riassuntive

| Scheda | Contenuto |
|---|---|
| **ORA MIGLIORE DEL GIORNO** | Ora con l'indice di tratta più alto, l'indice e il lato prevalente (A/B con la sua %) |
| **SCIAME PIÙ FAVOREVOLE** | Lo sciame con il ZHR × efficienza più alto della giornata, la sua efficienza, ora e lato, e il **puntamento migliore** (azimut del radiante +90° / −90°) |
| **ADESSO** | Indice e lato prevalente in quest'ora, e l'Hot consigliato (solo quando il giorno scelto è oggi) |
| **PREVISIONE SPERIMENTALE** | Riflessioni/ora attese adesso, tra 1 h e tra 2 h alla frequenza della previsione (Collm, regole SM6FHZ; vedi [Attuazione sperimentale previsioni](Experimental-Forecasts-it)) |

Sotto le schede una fascia spiega le lettere A e B (vedi sotto).

## Grafico

*Efficienza oraria per … del … (UTC, valori a metà ora).* Per un massimo di cinque sciami: l'efficienza % come linea continua e la formula DH9GCD come linea punteggiata dello stesso colore; l'**indice della tratta** come barre blu sulla scala a destra.

## Tabella oraria

Una riga per ogni sciame attivo quel giorno (ordinati per ZHR), 24 colonne per le ore (UTC):

| Cella | Significato |
|---|---|
| `63A` | efficienza 63 %, la maggior parte delle riflessioni dal lato **A** |
| `41B` | efficienza 41 %, lato **B** |
| `3` | efficienza sotto il 5 %: numero senza lettera del lato |
| vuota | efficienza sotto l'1 % |
| `…↑` | il radiante è **sopra 70°** dalla tua stazione a quell'ora (troppo alto) |
| testo giallo | efficienza ≥ 50 % |

- **A** = a **sinistra** guardando dalla tua stazione verso il corrispondente (zona Hot A); **B** = a **destra** (zona Hot B). Conviene girare l'antenna di **10–30° verso quel lato** (side-scatter, articolo Cerrotta–Sartori).
- **Righe azzurre** (*DH9GCD %*, sotto ogni sciame): la formula DH9GCD, per confronto.
- **Riga Σ**: *Indice tratta (ZHR×eff.)*.
- **Riga arancione** (*Previsione … MHz (rifl./ora)*): la previsione sperimentale, per le ore in cui esiste (oggi e parte di domani).

## Il modello

Tutti i passaggi sono nel [manuale dei calcoli](Efficiency-Explanation-it) (`doc/YA-MS_manuale_calcoli.docx`, capitolo 5). In breve:

**1. Riflessione speculare.** Una scia manda il segnale da A a B solo se è tangente a un ellissoide con A e B nei fuochi (McKinley 1961). Le scie di uno sciame sono parallele alla direzione del radiante ŝ (articolo; McKinley). Per ogni punto P dello strato E, con i versori verso le stazioni:

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

La stessa legge sta alla base di QTFGUI di DJ5HG (cone scattering). La condizione è accettata con una tolleranza gaussiana σ = 0,05 rad (circa 3°) – *scelta del programma*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Peso di ogni punto.** Potenza di una scia sottodensa (McKinley), φ = metà dell'angolo di diffusione (limitato a 85°, *scelta*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Il numero di meteore che raggiungono un punto è proporzionale al seno dell'elevazione del radiante in quel punto (ŝ·û_P), la stessa correzione che l'IMO usa per lo ZHR.

**3. Somma e percentuale.** Punti ogni 15 km alla quota delle scie, solo dove entrambe le stazioni li vedono sopra l'elevazione del lobo (*scelta*). Il 100 % è la posizione del radiante più favorevole per quella tratta:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F si calcola una volta per tratta su una griglia di direzioni (azimut ogni 5°, elevazione ogni 2,5°) e si interpola.

**4. Lato e indice.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

La lettera nella tabella è il lato con la frazione maggiore. *Scelte del programma (eq. 32–33 del manuale).*

## Confronto con DH9GCD

Una verifica indipendente: la formula della direzione migliore di **DH9GCD**, riportata da **DF5HC** (convegno DARC, gennaio 2018), con El e Az elevazione e azimut del radiante visti dalla tua stazione e P l'azimut del corrispondente:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

È massima con il radiante a 45° e di traverso rispetto alla tratta. DF5HC considera il radiante troppo basso sotto 20° e **troppo alto sopra 70°**: queste ore ricevono ↑ nella tabella e un avviso nella [Volta celeste](Sky-View-it#avvisi). La formula ignora distanza e quote, ma è un buon riferimento.

## Verifiche

| Verifica | Risultato |
|---|---|
| Regola di SM6FHZ (VUSHF 2025): tratta migliore ortogonale all'azimut del radiante, puntamento = az. del radiante ±90°, tolleranza ±40–50° | Riprodotta dal modello; con il radiante allineato alla tratta e alto nel cielo l'efficienza è quasi zero |
| QTFGUI di DJ5HG, Amburgo JO53IM – Barcellona, Quadrantidi, 4 gennaio (esempio del suo manuale) | QTFGUI: 07:00 puntamento 252°, −8 dB; 08:00 nessuna zona di riflessione; 09:00 puntamento 168°, −4 dB. YA-MS (quota 102 km come QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Tutti e tre i metodi vedono il buco delle 08:00, con il radiante quasi allo zenit |
| Campionamento ogni 5 km invece di 15 km | le percentuali cambiano di meno di 0,3 punti |

> La scala usata da OH5IY e da MCG_MS non è nota nei dettagli (i manuali di MS-Soft non sono disponibili): confronta le percentuali con quei programmi prima di considerarle equivalenti. Il modello considera solo le scie sottodense, con antenne isotrope; i burst sovradensi e il fondo sporadico non entrano nell'efficienza (il fondo sporadico è rappresentato dal flusso radar).
