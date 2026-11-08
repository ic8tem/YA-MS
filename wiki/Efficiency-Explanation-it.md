**English** · [Русский](Efficiency-Explanation-ru) · [Deutsch](Efficiency-Explanation-de) · [日本語](Efficiency-Explanation-ja)

# Efficienza - spiegazione

*Linguetta: Documenti tecnici › Efficienza - spiegazione.*

[![Efficienza - spiegazione](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/it-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/it-3_3.png)

Un documento tecnico, *"Come YA-MS calcola l'efficienza di uno sciame"*, mostrato all'interno del programma come una pagina chiara. Spiega **passo per passo** come si ottiene l'efficienza e dice per ogni passaggio **da dove viene**. Il documento è attualmente **in italiano**; questa wiki ne riassume il contenuto anche in [Calcolo dell'efficienza](Efficiency-Calculation-it#il-modello) e in [Geometria e attenuazione](Geometry-and-Path-Loss-it).

## Etichette

Ogni passaggio porta un'etichetta colorata:

| Etichetta | Colore | Significato |
|---|---|---|
| **FONTE** | blu | il passaggio riprende una fonte citata; il numero tra parentesi rimanda all'elenco finale |
| **RILIEVO** | verde | confronto tra il programma e le fonti, con il risultato |
| **SCELTA** | arancione | una scelta del programma, non presa da una fonte: da verificare con l'esperienza in aria |

## Capitoli

| Capitolo | Contenuto |
|---|---|
| 1. Introduzione | Scopo, etichette, che cosa significa efficienza (OH5IY, MCG_MS; YA-MS usa la tratta reale) |
| 2. Dove avvengono le riflessioni: lo strato E | Scie a 80–120 km; quota delle scie = moda dell'istogramma di Collm (rilievo: 89,5 km il 5/11/2026) |
| 3. Geometria della tratta | Terra e punto medio; elevazione d'antenna (formula dell'articolo); zona comune e suoi limiti; Hot A / Hot B; lobo d'antenna (DL6WU, Kraus, W4RNL) |
| 4. Il radiante dello sciame | Posizione del radiante (IMO 2026/2027), data del massimo (IMO o longitudine solare), profilo di attività |
| 5. Condizione di riflessione | Riflessione speculare (McKinley), tolleranza gaussiana 0,05 rad, puntamento migliore (SM6FHZ), formula DH9GCD |
| 6. Da un punto all'efficienza | Punti di riflessione ogni 15 km, peso di ogni punto, percentuale; confronto con QTFGUI (DJ5HG) |
| 7. Leggere i risultati | Lato A / B, indice della tratta, colori dei radianti, zone PREV, sezione vista dall'antenna |
| 8. Frequenza di lavoro e attenuazione | Regole λ³ / λ², dal radar alla banda radioamatoriale, riferimenti per l'attenuazione di tratta |
| 9. Limiti noti | Solo scie sottodense, antenne isotrope, valori di lavoro |
| 10. Fonti | 17 fonti numerate |

## Pulsanti

| Pulsante | Che cosa fa |
|---|---|
| **Esporta in Word (.docx)...** | Salva una copia di `data/efficienza_spiegazione.docx` dove scegli tu (nome suggerito *YA-MS - calcolo dell'efficienza.docx*) |
| **Apri in Word** | Apre lo stesso `.docx` con il programma predefinito per i documenti Word (Word, LibreOffice, …) |

## File

| File | Contenuto |
|---|---|
| `data/efficienza_spiegazione.txt` | Il testo mostrato nella linguetta, un blocco per riga (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | La versione Word |
| `doc/YA-MS_manuale_calcoli.docx` | Il **manuale dei calcoli**: tutte le equazioni (editor di equazioni di Word), numerate, con le loro fonti |

I due documenti si rigenerano dal sorgente con `tools/build_spiegazione.py data` e `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
