// Uso: node tools/build_manuale.js <file.docx> [codice lingua]
//   senza codice (o "it") il manuale e' in italiano; con un codice usa tools/traduzioni_doc/manuale/<codice>.json
//   ({"testo italiano": "traduzione"}). Con ESTRAI=<file.json> scrive l'elenco dei testi da tradurre.
const fs = require('fs');
const path = require('path');
const d = require('docx');
const LANG = process.argv[3] || 'it';
const TRD = LANG === 'it' ? {} : JSON.parse(fs.readFileSync(path.join(__dirname, 'traduzioni_doc', 'manuale', LANG + '.json'), 'utf8'));
const KEYS = []; const SEEN = new Set(); const MISS = [];
// traduce un testo (solo se contiene lettere); le chiavi sono i testi italiani
function T(s) {
  if (typeof s !== 'string' || !/[A-Za-zÀ-ÿ]{2,}/.test(s)) return s;
  if (!SEEN.has(s)) { SEEN.add(s); KEYS.push(s); }
  if (LANG === 'it') return s;
  if (TRD[s] === undefined) { MISS.push(s); return s; }
  return TRD[s];
}
const MATHFN = /^(arccos|arcsin|arctan|atan2|log|sin|cos|tan|sec|exp|max|min|argmax|ln|lim|det)$/;
const RTL = ['ar', 'he', 'ur'].includes(LANG);   // lingue da destra a sinistra
class TextRun extends d.TextRun {
  constructor(o) {
    if (typeof o === 'string') o = { text: T(o) }; else if (o && typeof o.text === 'string') o = Object.assign({}, o, { text: T(o.text) });
    if (RTL && o && typeof o === 'object') o = Object.assign({ rightToLeft: true }, o);
    super(o);
  }
}
class Paragraph extends d.Paragraph {
  constructor(o) { if (RTL && o && typeof o === 'object' && !Array.isArray(o)) o = Object.assign({ bidirectional: true }, o); super(o); }
}
class MathRun extends d.MathRun {
  // nelle formule si traducono solo le parole (almeno 4 lettere) che non sono funzioni matematiche
  constructor(t) { super(typeof t === 'string' && /[A-Za-zÀ-ÿ]{4,}/.test(t) && !MATHFN.test(t.trim()) ? T(t) : t); }
}
const { Document, Packer, HeadingLevel, AlignmentType, TabStopType, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, LevelFormat, Footer, PageNumber, TableOfContents,
  Math: M, MathFraction, MathSubScript, MathSuperScript, MathSubSuperScript, MathRadical, MathRoundBrackets,
  MathSquareBrackets, MathFunction, MathSum } = d;

// ---------- mini DSL per le equazioni ----------
const A = (x) => (Array.isArray(x) ? x : [typeof x === 'string' ? new MathRun(x) : x]).flat()
  .map(e => typeof e === 'string' ? new MathRun(e) : e);
const r = (t) => new MathRun(t);
const fr = (n, den) => new MathFraction({ numerator: A(n), denominator: A(den) });
const sb = (b, s) => new MathSubScript({ children: A(b), subScript: A(s) });
const sp = (b, s) => new MathSuperScript({ children: A(b), superScript: A(s) });
const sbsp = (b, s, p) => new MathSubSuperScript({ children: A(b), subScript: A(s), superScript: A(p) });
const sq = (x, deg) => new MathRadical(deg ? { children: A(x), degree: A(deg) } : { children: A(x) });
const br = (...x) => new MathRoundBrackets({ children: A(x.flat()) });
const sbr = (...x) => new MathSquareBrackets({ children: A(x.flat()) });
const fn = (name, ...x) => new MathFunction({ name: A(name), children: A(x.flat()) });
const sum = (s, x) => new MathSum({ children: A(x), subScript: A(s) });

let eqn = 0;
function EQ(...parts) {
  eqn++;
  return new Paragraph({
    tabStops: [{ type: TabStopType.CENTER, position: 4819 }, { type: TabStopType.RIGHT, position: 9638 }],
    spacing: { before: 100, after: 140 },
    children: [new TextRun('\t'), new M({ children: A(parts.flat()) }), new TextRun('\t(' + eqn + ')')],
  });
}
const FONT = 'Calibri';
function P(...runs) {
  return new Paragraph({ spacing: { after: 120 }, children: runs.map(x => typeof x === 'string' ? new TextRun(x) : x) });
}
const B = (t) => new TextRun({ text: t, bold: true });
const I = (t) => new TextRun({ text: t, italics: true });
function TAG(kind, text) {
  const col = { FONTE: '1F5FAD', RILIEVO: '2E7D32', SCELTA: 'B45309' }[kind];
  return new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: '[' + kind + '] ', bold: true, color: col }), new TextRun(text)] });
}
const H1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)] });
const H2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)] });
const bullet = (t) => new Paragraph({ numbering: { reference: 'bul', level: 0 }, spacing: { after: 60 }, children: (Array.isArray(t) ? t : [t]).map(x => typeof x === 'string' ? new TextRun(x) : x) });

const border = { style: BorderStyle.SINGLE, size: 4, color: 'B0B7C3' };
const borders = { top: border, bottom: border, left: border, right: border };
function table(widths, rows) {
  const tw = widths.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: tw, type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((row, ri) => new TableRow({
      tableHeader: ri === 0,
      children: row.map((c, ci) => new TableCell({
        width: { size: widths[ci], type: WidthType.DXA }, borders,
        shading: ri === 0 ? { fill: 'DCE6F2', type: ShadingType.CLEAR, color: 'auto' } : undefined,
        margins: { top: 60, bottom: 60, left: 100, right: 100 },
        children: [new Paragraph({ children: [ri === 0 ? new TextRun({ text: c, bold: true }) : (typeof c === 'string' ? new TextRun(c) : new M({ children: A(c) }))] })],
      })),
    })),
  });
}

// ---------- contenuto ----------
const C = [];
C.push(new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun('YA-MS - Manuale dei calcoli')] }));
C.push(P(I('Previsione e calcolo in diretta dell\'efficienza degli sciami meteorici per il meteor scatter. Versione 1.7.0, a cura di Costantino IC8TEM, novembre 2026.')));
C.push(new TableOfContents(T('Indice'), { hyperlink: true, headingStyleRange: '1-2' }));
C.push(P(I('(Se l\'indice è vuoto: in Word, clic destro sull\'indice > Aggiorna campo.)')));

C.push(H1('1. Convenzioni'));
C.push(P('Ogni passo del calcolo è accompagnato da un\'etichetta che ne indica l\'origine. Le fonti sono numerate nel capitolo 12.'));
C.push(TAG('FONTE', 'il passo riprende una fonte citata.'));
C.push(TAG('RILIEVO', 'confronto tra il programma e le fonti, con l\'esito della verifica.'));
C.push(TAG('SCELTA', 'scelta del programma, non presa da una fonte; va verificata con l\'esperienza in banda.'));
C.push(P('Angoli in gradi salvo diversa indicazione; distanze in km; tempi in UTC. I vettori sono in grassetto e sono riferiti a un sistema geocentrico solidale con la Terra (asse x verso il meridiano di Greenwich all\'equatore, asse z verso il polo nord).'));
C.push(table([1900, 7738], [
  ['Simbolo', 'Significato'],
  [['r'], 'raggio terrestre medio, 6372,7955 km [1]'],
  [['H'], 'quota della scia (strato E), dal radar SKiYMET'],
  [['h'], 'quota della stazione sul livello del mare'],
  [[sb('φ', 'A'), ', ', sb('λ', 'A')], 'latitudine e longitudine della stazione A (la mia) e della stazione B (il corrispondente)'],
  [['α, δ'], 'ascensione retta e declinazione del radiante'],
  [[sb('λ', '⊙')], 'longitudine solare (equinozio J2000)'],
  [['ŝ'], 'versore della direzione del radiante'],
  [['Az, El'], 'azimut (da nord verso est) ed elevazione'],
]));

C.push(H1('2. Tempo e posizione del radiante'));
C.push(H2('2.1 Giorno giuliano'));
C.push(TAG('FONTE', 'Meeus, Astronomical Algorithms [6], cap. 7. Con Y, M l\'anno e il mese (per gennaio e febbraio Y−1 e M+12) e D il giorno con la frazione decimale:'));
C.push(EQ('JD=', fn('int', br('365,25', br('Y+4716'))), '+', fn('int', br('30,6001', br('M+1'))), '+D+B−1524,5'));
C.push(EQ('B=2−A+', fn('int', fr('A', '4')), ',   A=', fn('int', fr('Y', '100'))));
C.push(EQ('T=', fr('JD−2451545,0', '36525')));
C.push(H2('2.2 Tempo siderale di Greenwich'));
C.push(TAG('FONTE', 'Meeus [6], cap. 12:'));
C.push(EQ('θ', '=280,46061837+360,98564736629', br('JD−2451545'), '+0,000387933 ', sp('T', '2'), '−', fr(sp('T', '3'), '38710000')));
C.push(H2('2.3 Longitudine solare'));
C.push(TAG('FONTE', 'Meeus [6], cap. 25 (precisione bassa, circa 0,01°). L\'IMO esprime i massimi in longitudine solare riferita all\'equinozio J2000 [5]; il termine −1,397 T riporta il valore all\'equinozio J2000.'));
C.push(EQ(sb('L', '0'), '=280,46646+36000,76983 T+0,0003032 ', sp('T', '2')));
C.push(EQ('M=357,52911+35999,05029 T−0,0001537 ', sp('T', '2')));
C.push(EQ('C=', br('1,914602−0,004817 T'), fn('sin', 'M'), '+', br('0,019993−0,000101 T'), fn('sin', '2M'), '+0,000289 ', fn('sin', '3M')));
C.push(EQ(sb('λ', '⊙'), '=', sb('L', '0'), '+C−1,397 T'));
C.push(TAG('SCELTA', 'L\'istante del massimo di uno sciame si trova risolvendo λ⊙(JD) = λmax con il metodo di Newton (8 iterazioni, passo 0,98561° al giorno).'));
C.push(TAG('RILIEVO', 'Massimi 2026 calcolati: Quadrantidi 3/1, Perseidi 13/8, Orionidi 21/10, Leonidi 17/11, Geminidi 14/12. Coincidono con il calendario IMO 2026 [5].'));
C.push(H2('2.4 Radiante e sua deriva'));
C.push(TAG('FONTE', 'α, δ e λmax dai calendari IMO 2026 e 2027 [5], tabelle 5 e 7, compresi gli sciami minori della lista IMO (per esempio Camelopardalidi di ottobre, Andromedidi, sciami diurni radio di aprile e maggio); per la sorgente Antielio la tabella 6, interpolata linearmente tra le date. Gli sciami minori contribuiscono all\'indice della tratta e al consiglio dell\'hot spot con il loro ZHR.'));
C.push(EQ('α=', sb('α', '0'), '+', fr('dα', 'dλ'), ' Δλ,   δ=', sb('δ', '0'), '+', fr('dδ', 'dλ'), ' Δλ,   Δλ=', sb('λ', '⊙'), '−', sb('λ', 'max')));
C.push(TAG('SCELTA', 'Le derive dα/dλ e dδ/dλ sono valori di lavoro scritti in data\\sciami.csv: la tabella delle derive IMO non è ancora stata inserita.'));
C.push(TAG('RILIEVO', 'Confronto con il catalogo dell\'IAU Meteor Data Center [36]: la linguetta Sciami mostra per ogni sciame quante soluzioni sono pubblicate nell\'elenco degli sciami stabiliti e la differenza tra il catalogo IMO del programma e la mediana delle soluzioni: distanza angolare dei radianti (confrontati alla stessa longitudine solare, con la deriva del programma), Δλ (λ max del programma meno la mediana delle longitudini solari medie dell\'attività, che non coincidono esattamente con il massimo) e Δv. Il fumetto elenca le soluzioni con i loro riferimenti. Il file originale si scarica al massimo una volta al mese da www.ta3.sk; il MDC chiede di citare Jenniskens et al. 2020 e Jopek e Kaňuchová 2017.'));
C.push(H2('2.5 Dal radiante all\'azimut e all\'elevazione'));
C.push(TAG('FONTE', 'Conversione vettoriale equivalente alle formule di Meeus [6], cap. 13. Angolo orario di Greenwich H = θ − α:'));
C.push(EQ('ŝ=', sbr(fn('cos', 'δ'), fn('cos', 'H'), ' ;  −', fn('cos', 'δ'), fn('sin', 'H'), ' ;  ', fn('sin', 'δ'))));
C.push(P('Nel punto di latitudine φ e longitudine λ si usano i versori locali alto (û), est (ê) e nord (n̂):'));
C.push(EQ('û=', sbr(fn('cos', 'φ'), fn('cos', 'λ'), ' ; ', fn('cos', 'φ'), fn('sin', 'λ'), ' ; ', fn('sin', 'φ')), ',   ê=', sbr('−', fn('sin', 'λ'), ' ; ', fn('cos', 'λ'), ' ; 0'), ',   n̂=û×ê'));
C.push(EQ('El=', fn('arcsin', br('ŝ·û')), ',    Az=', fn('atan2', br('ŝ·ê , ŝ·n̂'))));
C.push(P('Nota: nel programma il segno di sin H è incluso nella forma (θ − α); il risultato è lo stesso.'));
C.push(H2('2.6 Attività dello sciame'));
C.push(TAG('FONTE', 'ZHRmax dal calendario IMO 2026 [5].'));
C.push(TAG('SCELTA', 'Profilo esponenziale attorno al massimo, con pendenza diversa in salita e in discesa (valori di lavoro in sciami.csv):'));
C.push(EQ('ZHR', br(sb('λ', '⊙')), '=', sb('ZHR', 'max'), '·', sp('10', ['−', sb('B', '±'), '|Δλ|'])));

C.push(H1('3. Geografia della tratta'));
C.push(H2('3.1 Dal locator alle coordinate'));
C.push(TAG('FONTE', 'Sistema Maidenhead (IARU). Per un locator di 6 caratteri L1 L2 N3 N4 L5 L6 (lettere contate da A = 0), al centro del quadratino:'));
C.push(EQ('λ=20·', sb('L', '1'), '−180+2·', sb('N', '3'), '+', fr(sb('L', '5'), '12'), '+', fr('1', '24'), ',    φ=10·', sb('L', '2'), '−90+', sb('N', '4'), '+', fr(sb('L', '6'), '24'), '+', fr('1', '48')));
C.push(H2('3.2 Distanza, azimut e punto medio'));
C.push(TAG('FONTE', 'Formule del cerchio massimo su sfera di raggio r [1]:'));
C.push(EQ('D=r·', fn('arccos', br(sb('û', 'A'), '·', sb('û', 'B')))));
C.push(EQ(sb('Az', 'AB'), '=', fn('atan2', br(fn('sin', 'Δλ'), fn('cos', sb('φ', 'B')), ' , ', fn('cos', sb('φ', 'A')), fn('sin', sb('φ', 'B')), '−', fn('sin', sb('φ', 'A')), fn('cos', sb('φ', 'B')), fn('cos', 'Δλ')))));
C.push(P('Il punto medio M è il punto a distanza D/2 da A lungo l\'azimut AzAB.'));
C.push(TAG('FONTE', 'Il calcolo si riferisce al punto medio della tratta, perché tra le due estremità l\'ora migliore può differire fino a 1,5 ore (SM6FHZ [4]).'));
C.push(TAG('SCELTA', 'La tratta è sempre quella reale tra i due locator. L\'antenna si considera sempre puntata verso il corrispondente (Az(antenna) = AzAB), per il controllo del lobo (capitolo 7).'));

C.push(H1('4. Geometria del meteor scatter'));
C.push(H2('4.1 Quota delle scie'));
C.push(TAG('FONTE', 'Lo sciame produce scie ionizzate nello strato E, tra 80 e 120 km; i radar SKiYMET danno una quota media di circa 90 km [1].'));
C.push(TAG('SCELTA', 'Si usa la quota più frequente (moda) dell\'istogramma del radar di Collm [7] (capitolo 8).'));
C.push(TAG('RILIEVO', 'DJ5HG [22] e QTFGUI [18] usano una quota fissa di 102 km; il programma preferisce il dato misurato dal radar. La Raccomandazione ITU-R P.843 [28] dà una quota media h = 124 − 17·log10(f) km: circa 97 km a 36,2 MHz e 87 km a 144 MHz, in linea con la moda di Collm (89,5 km il 5/11/2026).'));
C.push(TAG('RILIEVO', 'Grafico del 5/11/2026: moda 89,5 km, media 88,6 km, deviazione standard 6,8 km. Conferma i 90 km dell\'articolo [1].'));
C.push(H2('4.2 Elevazione d\'antenna'));
C.push(TAG('FONTE', 'Formula dell\'articolo [1] (Immagine 7), con x = d/r e d la distanza a terra dal punto di riflessione:'));
C.push(EQ('e=90°−57,3·', fn('arctan', sbr(fr(['r ', fn('tan', 'x'), '+', br('H−', fr(['r', br('1−', fn('cos', 'x'))], fn('cos', 'x'))), fn('sin', 'x')], ['H−', fr(['r', br('1−', fn('cos', 'x'))], fn('cos', 'x')), '−h ', fn('sin', 'x')])))));
C.push(TAG('RILIEVO', 'Coincide entro 0,03° con la geometria sferica esatta. Il programma usa l\'arcotangente a due argomenti, che oltre l\'orizzonte dà valori negativi ed evita la periodicità segnalata nell\'articolo.'));
C.push(H2('4.3 Portata alla quota delle scie'));
C.push(TAG('SCELTA', 'Distanza a terra alla quale un raggio con elevazione e raggiunge la quota H (inversa geometrica della 4.2):'));
C.push(EQ(sb('d', 'H'), '=r', sbr(fr('π', '2'), '−e−', fn('arcsin', br(fr([br('r+h'), fn('cos', 'e')], 'r+H'))))));
C.push(TAG('RILIEVO', 'Con H = 89,5 km ed e = 0° si ottengono 1062 km. Nell\'esempio dell\'articolo (JN44BB–IO53RT) il disegno pone gli incroci delle curve d\'orizzonte (paragrafo 4.4) a circa 870 km dalle stazioni, che corrispondono a un lobo elevato di circa 2° (865 km).'));
C.push(H2('4.4 Zona comune e suoi limiti (Limite A, Limite B)'));
C.push(TAG('FONTE', 'L\'articolo [1] individua gli incroci delle curve dove l\'orizzonte di ciascuna stazione incontra lo strato E. Sono gli incroci di due cerchi di raggio angolare ρ = dH/r centrati in A e B:'));
C.push(EQ(sb('p', '0'), '=', fr(fn('cos', 'ρ'), ['1+', sb('û', 'A'), '·', sb('û', 'B')]), br(sb('û', 'A'), '+', sb('û', 'B'))));
C.push(EQ(sb('p', 'A,B'), '=', sb('p', '0'), '±', sq(fr(['1−', sp(['|', sb('p', '0'), '|'], '2')], sp(['|', sb('û', 'A'), '×', sb('û', 'B'), '|'], '2'))), br(sb('û', 'A'), '×', sb('û', 'B'))));
C.push(P('Se 1 − |p0|² < 0 la tratta è più lunga di 2·dH e le due stazioni non vedono una zona comune dello strato E.'));
C.push(TAG('RILIEVO', 'Questi due punti sono i bordi più lontani della zona di strato E vista da entrambe le stazioni, non i punti dove arrivano più riflessioni. Sulla tratta JN70CN–IN78UO (1710 km, azimut 308°) cadono a 1062 km dalla stazione, 37° a sinistra e a destra della direzione diretta: troppo di lato per il puntamento. Il programma li chiama "Limite A" e "Limite B" e li disegna tenui sulla mappa, insieme ai due cerchi della zona comune.'));
C.push(H2('4.5 Hot A e Hot B (hot spot per il puntamento)'));
C.push(TAG('FONTE', 'Le riflessioni delle meteore sporadiche si concentrano in due zone ("hot spot") ai lati del punto medio della tratta. J. Richardson (AMS) [23], nella tabella riportata da DJ5HG [22], indica lo scarto d\'antenna dalla direzione diretta: 13° a 1000 km, 11° a 1250 km, 10° a 1500 e a 2000 km. L\'AMS Bulletin n. 203, ripreso da W8WN [15], dà 10° a 1500 e 1800 km.'));
C.push(TAG('SCELTA', 'Hot A e Hot B sono i punti a distanza s dal punto medio, perpendicolari alla tratta (A a sinistra guardando dalla stazione verso il corrispondente, B a destra). Con la casella "auto (AMS)" accesa (di partenza) s viene dallo scarto della tabella di Richardson, interpolato in modo lineare (13° sotto 1000 km, 10° sopra 2000 km): s = (D/2)·tan(scarto). Spegnendo la casella si scrive s a mano (MSHV [16] usa 150 km).'));
C.push(EQ(sb('P', 'A,B'), '=destinazione', br('M , ', sb('Az', 'M→B'), '∓90° , s')));
C.push(P('Lo scarto dalla direzione diretta, visto dalla stazione, vale con buona approssimazione:'));
C.push(EQ('Δ', sb('Az', 'hot'), '≈', fn('arctan', fr('s', 'D/2'))));
C.push(TAG('RILIEVO', 'Con la tabella AMS: 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN-IN78UO (1710 km) → 10°, s ≈ 151 km, come i 150 km usati prima e da MSHV; sulle tratte corte la tabella avvicina gli hot spot al punto medio.'));
C.push(H2('4.6 Hot consigliato dall\'efficienza'));
C.push(TAG('SCELTA', 'Per l\'ora mostrata sulla volta celeste il programma somma, su tutti gli sciami sopra l\'orizzonte, il peso ZHR·η/100 diviso tra lato A (frazione fA, capitolo 5.5) e lato B. L\'hot spot del lato con il peso maggiore è quello consigliato e compare in rosso sulla mappa:'));
C.push(EQ(sb('W', 'A'), '=', sum('sciami', [fr(['ZHR·η'], '100'), '·', sb('f', 'A')]), ',    ', sb('W', 'B'), '=', sum('sciami', [fr(['ZHR·η'], '100'), '·', br('1−', sb('f', 'A'))]), ',    consigliato = lato con W maggiore'));
C.push(TAG('FONTE', 'Lo spostamento di 10–30° verso il lato delle riflessioni (side-scatter) è indicato nell\'articolo [1].'));
C.push(TAG('FONTE', 'DJ5HG, riportato da DF5HC [17]: la riflessione avviene su un cono attorno alla scia; per le tratte più corte le antenne vanno puntate a lato della direzione diretta, entrambe le stazioni verso lo stesso punto, e secondo la posizione del radiante uno dei due punti (HOT-A o HOT-B) è più favorevole. È lo stesso criterio del consiglio del programma.'));

C.push(H1('5. Efficienza dello sciame'));
C.push(H2('5.1 Concetto'));
C.push(TAG('FONTE', 'L\'efficienza indica in percentuale quanto la posizione dello sciame permette riflessioni su una tratta (OH5IY [2], ripreso nell\'articolo [1]); MCG_MS [3] la calcola per quattro direzioni fisse e, con il locator del corrispondente, per la tratta reale.'));
C.push(H2('5.2 Condizione di riflessione speculare'));
C.push(TAG('FONTE', 'Una scia rimanda il segnale tra A e B solo se è tangente a un ellissoide che ha A e B nei fuochi (McKinley [8]). Le scie di uno sciame sono parallele alla direzione del radiante [1, 8]. Per un punto P dello strato E, con i versori verso le stazioni:'));
C.push(EQ(sb('ê', 'A'), '=', fr(['A−P'], '|A−P|'), ',   ', sb('ê', 'B'), '=', fr(['B−P'], '|B−P|'), ',   n̂=', fr([sb('ê', 'A'), '+', sb('ê', 'B')], ['|', sb('ê', 'A'), '+', sb('ê', 'B'), '|'])));
C.push(EQ('condizione speculare:   ŝ·n̂=0'));
C.push(TAG('FONTE', 'La stessa legge è alla base di QTFGUI di DJ5HG: il raggio che colpisce la scia viene diffuso su un cono attorno ad essa, e solo chi sta sul cono riceve il segnale. La condizione del cono equivale a ŝ·n̂ = 0. [18, 22] Nel suo testo del 2004 DJ5HG la descrive cosi\': la scia attraversa lo strato E, le due antenne la illuminano e il ricevitore sta sul cono che ha la scia come asse; la parete del cono e\' il lobo di un radiatore lungo migliaia di lunghezze d\'onda, quindi stretta, ma a incidenza radente (tratte lunghe) tocca il suolo su un\'area ampia.'));
C.push(TAG('SCELTA', 'La condizione si accetta con una tolleranza gaussiana di σ = 0,05 rad (circa 3°). La parete del cono, per una scia ideale, e\' molto piu\' stretta [22]; i 3° rappresentano quello che il cono ideale non vede: la dispersione dei radianti di uno sciame (0,3-1,4° misurati dal GMN), la scia curvata dal vento e la sua lunghezza finita:'));
C.push(EQ(sb('S', 'P'), '=', sp('e', ['−', fr(sp(br('ŝ·n̂'), '2'), ['2', sp('σ', '2')])])));
C.push(TAG('RILIEVO', 'Per il meteor scatter QTFGUI di DJ5HG disegna scarti dalla legge di riflessione fino a 32°: la tolleranza gaussiana di 0,05 rad del programma è più severa e concentra il peso sui punti quasi esattamente speculari. Con il campionamento a 5 km invece di 15 km le percentuali cambiano meno di 0,3 punti. [18]'));
C.push(H2('5.3 Peso di ciascun punto'));
C.push(TAG('FONTE', 'Potenza di una scia sottodensa (McKinley [8]; ITU-R P.843 [28], eq. 3): proporzionale a λ³ / [R1 R2 (R1+R2) (1 − cos²β sin²φ)], con R1 = |A−P|, R2 = |B−P|, φ metà dell\'angolo di scattering e β angolo tra la scia e il piano di propagazione A-P-B. Con p̂ versore normale al piano, sin β = |ŝ·p̂|:'));
C.push(EQ('φ=', fr('1', '2'), fn('arccos', br(sb('ê', 'A'), '·', sb('ê', 'B'))), ',    p̂=', fr([sb('ê', 'A'), '×', sb('ê', 'B')], ['|', sb('ê', 'A'), '×', sb('ê', 'B'), '|']), ',    sin β=|ŝ·p̂|'));
C.push(EQ(sb('w', 'P'), br('ŝ'), '=', fr('1', [sb('R', '1'), sb('R', '2'), br(sb('R', '1'), '+', sb('R', '2')), br('1−', sp(fn('cos', 'β'), '2'), sp(fn('sin', 'φ'), '2'))])));
C.push(TAG('SCELTA', 'Fino alla versione 1.6 il programma prendeva β = 0 per tutte le scie, cioè il peso 1/[R1 R2 (R1+R2) cos²φ]: le scie che attraversano il piano della tratta pesavano fino a 1/cos²φ volte troppo, 10-15 dB tra 600 e 2000 km. Dalla 1.7 β si può calcolare per ogni punto e per ogni direzione del radiante con l\'opzione "Angolo β tra scia e tratta (McKinley completo)", accesa di partenza perché dà i valori più prudenti (nessuna scia è sopravvalutata); spegnendo l\'opzione si usa β = 0 come prima. La correzione è stata segnalata confrontando la pagina di GM8JBJ [9], che riporta i circa 6 dB in meno di G4BAO per le scie allineate alla tratta.'));
C.push(TAG('SCELTA', 'φ limitato a 85° per evitare valori infiniti nelle direzioni radenti.'));
C.push(TAG('FONTE', 'Il numero di meteore che arrivano in un punto è proporzionale al seno dell\'elevazione del radiante in quel punto (la stessa correzione usata dall\'IMO per lo ZHR [5]): ŝ·ûP.'));
C.push(TAG('SCELTA', 'Opzione "Scie più lunghe con il radiante basso (DJ5HG)", spenta di partenza, nel Calcolo dell\'efficienza: DJ5HG [22] osserva che con il radiante basso cadono meno meteore per km² ma le scie sono più lunghe (fino a 100 km utili) e soddisfano più spesso la legge di riflessione. Con l\'opzione accesa il peso diventa min(sin El, 15/100): lo spessore utile dello strato, 15 km, diviso il seno dell\'elevazione dà la lunghezza della scia, limitata a 100 km. Sopra circa 9° di elevazione i due effetti si compensano; spenta, il calcolo resta prudente.'));
C.push(TAG('SCELTA', 'Impostazioni pronte del calcolo, nella stessa riga: "Prudente" (di partenza, i valori più prudenti: quota dal radar, scie normali, con β), "Come DJ5HG" (102 km, scie lunghe, con β) e "Personalizzata", che si seleziona da sola quando si cambia a mano la quota, la casella "dal radar", le scie lunghe o l\'angolo β.'));
C.push(TAG('RILIEVO', 'Effetto dell\'angolo β sulla direzione migliore, tratta di 1000 km: senza β il massimo cade tra 15° e 90° dalla tratta secondo l\'elevazione del radiante (30° con il radiante a 30°, perpendicolare con il radiante a 60°) e il radiante perpendicolare vale il 67 % con il radiante a 30°; con β il massimo è sempre con il radiante lungo la tratta e il radiante perpendicolare scende al 15 %. Con β si perde quindi la regola della direzione migliore di SM6FHZ e di DH9GCD: β resta un\'opzione: è accesa di partenza perché dà i valori più prudenti (nessuna scia sopravvalutata), e spegnendola si torna alla regola.'));
C.push(TAG('FONTE', 'Due tesi sulla direzione migliore del radiante. Tesi classica dei radioamatori: il radiante migliore è alto tra 15° e 70° e di traverso alla tratta, quello allineato alla tratta è marginale. La sostengono SM6FHZ [4] con le sue regole sperimentali, DH9GCD con la sua formula (riportata da DF5HC [17]) e meteor-mcp di qso-graph [35], che la motiva con la condizione di tangenza: le scie utili devono essere tangenti a un ellissoide con i fuochi nelle due stazioni, e quelle che corrono lungo la tratta lo sono di rado. Questa tesi conta dove le scie possono riflettere, ma non quanto riflette ciascuna.'));
C.push(TAG('FONTE', 'Tesi della formula completa: McKinley [8] e l\'ITU-R P.843 [28] danno alla potenza di ogni scia il fattore 1 / (1 − cos²β sin²φ), dove β è l\'angolo tra la scia e il piano della tratta. Una scia che giace nel piano (β = 0) riflette 1/cos²φ volte più di una che lo attraversa (β = 90°): 10-15 dB tra 600 e 2000 km. Con il radiante allineato alla tratta le scie tangenti giacciono vicino al piano e pesano di più; con il radiante di traverso lo attraversano e pesano meno. DJ5HG [22] usa lo stesso fattore, e le sue curve orarie hanno la forma che YA-MS ritrova con β acceso (scarto di forma circa 3 dB).'));
C.push(TAG('RILIEVO', 'Le due tesi usano la stessa condizione di riflessione speculare ma pesano le scie in modo diverso: la classica conta le scie utili, la completa ne pesa anche la potenza. Su 1000 km, con il radiante a 30°, il radiante perpendicolare vale il 67 % senza β e il 15 % con β. Un primo confronto con conteggi reali non le distingue (paragrafo seguente): per decidere servono tratte più lunghe e più ricevitori.'));
C.push(TAG('RILIEVO', 'Confronto con conteggi reali: rilevamenti BRAMS ricevuti a Sonneberg (radiofaro di Dourbes, 49,97 MHz, tratta di 471 km) dal 12 al 28 agosto 2026, circa 97 000 echi rilevati con il metodo di M. Bundscherer [38]. Tolto il fondo (mediana ora per ora dal 22 al 27 agosto), le Perseidi aggiungono al massimo, il 13 agosto tra le 02 e le 10 UTC, circa 80-130 echi/ora su 300-470: a 50 MHz pesano poco rispetto alle sporadiche. L\'eccesso orario segue il calcolo di YA-MS (efficienza delle Perseidi × ZHR) con correlazione 0,44 con β acceso e 0,43 con β spento, la stessa che dà lo ZHR per il seno dell\'elevazione del radiante; con le scie lunghe scende a 0,36. Su questa tratta corta la geometria non aggiunge informazione e il confronto non decide tra le due tesi. Limiti: un solo ricevitore, soglia di rilevamento adattiva che può ridurre i conteggi nelle ore di maggiore attività, sciami minori ancora attivi nei giorni del fondo, antenna del radiofaro rivolta verso lo zenit.'));
C.push(TAG('SCELTA', 'Nel programma la casella "Angolo β tra scia e tratta (McKinley completo)" è accesa di partenza perché non sopravvaluta nessuna scia (valore prudente); spenta, applica la tesi classica. La casella "Giudizio classico" aggiunge sotto ogni sciame, nella tabella oraria, la riga del verdetto classico calcolato al punto medio della tratta: ✗ radiante sotto l\'orizzonte, ◐ marginale (sotto 15° o sopra 70°, oppure a meno di 30° dalla direzione della tratta), ● buono, ★ migliore (tra 15° e 70° e a più di 60° dalla direzione della tratta), con le soglie di meteor-mcp [35]. Non cambia il calcolo: mostra ora per ora dove le due tesi concordano e dove no.'));
C.push(H2('5.4 Somma e percentuale'));
C.push(TAG('SCELTA', 'I punti P si campionano ogni 15 km alla quota H, solo dove entrambe le stazioni vedono il punto sopra l\'elevazione minima del lobo. Per ogni direzione del radiante:'));
C.push(EQ('F', br('ŝ'), '=', sum('P', [sb('w', 'P'), sb('S', 'P'), 'max', br('0 , ŝ·', sb('û', 'P'))])));
C.push(EQ('η', br('ŝ'), '=100·', fr(['F', br('ŝ')], [sb('max', 'ŝ′'), ' F', br('ŝ′')]), '  %'));
C.push(P('F si calcola una volta per tratta su una griglia di direzioni (azimut ogni 5°, elevazione ogni 2,5°, nel riferimento del punto medio) e poi si interpola in modo bilineare.'));
C.push(TAG('SCELTA', 'Accanto alla percentuale, che vale per quella tratta sola, il programma dà l\'efficienza in dB riferita al riferimento fisso di DJ5HG [22]: 0 dB è il massimo di una tratta nord-sud di 1000 km a cavallo dell\'equatore con il radiante sull\'equatore celeste all\'equinozio (il radiante sale da est, passa per lo zenit e tramonta a ovest), calcolato con la stessa quota e gli stessi pesi. Così tratte diverse si confrontano tra loro. DJ5HG dichiara per i suoi valori una precisione migliore di 6 dB.'));
C.push(TAG('FONTE', 'Una scia rimanda il segnale tra le due stazioni solo se è tangente a un ellissoide con le stazioni nei fuochi: in ogni punto dello strato E servono solo i radianti sul semicerchio del cielo perpendicolare alla bisettrice dell\'angolo di scattering (Eshleman e Mlodnosky [24]; Meeks e James [25]). Vicino al punto medio questo semicerchio sale al massimo di traverso alla tratta: un radiante a elevazione El produce scie speculari a circa H·tan El di lato dal punto medio, dalla parte opposta al radiante, cioè negli hot spot che Eshleman e Mlodnosky e la Raccomandazione ITU-R P.843 [28] collocano a circa 100 km dai due lati. Il numero delle scie e la loro ionizzazione crescono con sin El [25]. La dipendenza degli echi dalla posizione del radiante è stata calcolata da Hines [26] e verificata su quattro sciami da Forsyth, Hines e Vogan [27]. Ne segue la regola pratica di SM6FHZ [4]: tratta migliore ortogonale all\'azimut del radiante, puntamento Az ± 90°, tolleranza ±40-50°.'));
C.push(TAG('RILIEVO', 'Riserva di DJ5HG [22]: con il radiante basso proprio lungo la tratta la formula di McKinley dà segnali forti, anche se le meteore sono poche (Amburgo-Narvik, Quadrantidi, verso le 19 UTC). La regola "radiante allineato alla tratta = efficienza quasi nulla" vale quindi per il radiante alto, non per quello radente. Il programma resta prudente e non alza l\'efficienza, ma segnala sulla volta celeste "RADIANTE BASSO LUNGO LA TRATTA" quando uno sciame attivo ha il radiante sotto 20° ed entro 30° dalla direzione della tratta. Il buco con il radiante allo zenit tra le due stazioni è confermato (Quadrantidi, Amburgo-Barcellona, verso le 08 UTC).'));
C.push(TAG('RILIEVO', 'Termine di confronto indipendente: la formula di DH9GCD riportata da DF5HC [17], con El e Az elevazione e azimut del radiante e P azimut del corrispondente. È massima per El = 45° e P − Az = 90°; DF5HC considera il radiante troppo basso sotto 20° e troppo alto sopra 70°. Non tiene conto della distanza né delle quote:'));
C.push(TAG('RILIEVO', 'La formula di DH9GCD non ha una fonte primaria pubblicata: unisce il fattore sin El (numero e ionizzazione delle scie) a un fattore cos El che rappresenta l\'allontanamento del punto speculare dal centro della tratta quando il radiante sale. Calcolata con il radiante visto dal punto medio, come fa MS-Soft [29], riproduce la tabella di MS-Soft per KP30HV-JO52MM (1324 km, Quadrantidi, 4/1/2001) entro 4 punti tra 16° e 48° di elevazione ed entro 16 punti fino a 64°, con lo stesso massimo alle 13 UT (96 % contro 92 %). Resta un termine di confronto.'));
C.push(EQ(sb('E', 'DH9GCD'), '=', fn('sin', 'El'), '·', fn('cos', 'El'), '·', fn('sin', br('P−Az'))));
C.push(TAG('SCELTA', 'Nella sottolinguetta "Calcolo previsionale › Calcolo dell\'efficienza" il programma mostra sotto ogni sciame, in azzurro, la formula in percentuale del suo massimo, con El e Az visti dalla stazione e P azimut del corrispondente; con il simbolo ↑ (e un avviso sulla volta celeste) segnala il radiante sopra 70°:'));
C.push(EQ(sb('E', '%'), '=200·', fn('sin', 'El'), '·', fn('cos', 'El'), '·|', fn('sin', br('P−Az')), '|'));
C.push(TAG('RILIEVO', 'Confronto con QTFGUI di DJ5HG (esempio del suo manuale): tratta Amburgo JO53IM - Barcellona, Quadrantidi, 4 gennaio. QTFGUI dà alle 07:00 UTC puntamento 252°, elevazione 1°, efficacia relativa -8 dB, radiante nella zona di riflessione az. 83° el. 75°; alle 08:00 nessuna zona di riflessione; alle 09:00 puntamento 168°, elevazione 2°, -4 dB, radiante az. 292° el. 74°. Il modello del programma (quota 102 km come QTFGUI) dà alle 07:00 241°, 0°, -5,4 dB, radiante az. 77° el. 74°; alle 08:00 0,6 % (-22 dB), cioè praticamente nulla; alle 09:00 161°, 4°, -4,0 dB, radiante az. 286° el. 75°. DH9GCD dà 26 %, 2 % e 32 %: tutti e tre i metodi vedono il buco delle 08:00, con il radiante quasi allo zenit [18].'));
C.push(TAG('RILIEVO', 'Confronto con le curve di DJ5HG [22] (Bild 8 e 9: da Amburgo e da Monaco, Quadrantidi, 4 gennaio), lette dal grafico (circa ±0,5 dB e ±15 min) e confrontate con la prova automatica del programma (--prova-dj5hg, un valore ogni ora). Orari: il buco con il radiante vicino allo zenit cade nelle stesse ore (Barcellona 7,5–8,5 UTC in DJ5HG, 7–9 nel programma; Sofia 6,6–7,8 e 7–8; Narvik 7–8,5 e 7–9); Mosca è chiusa dalle 3 alle 10 in entrambi, e il programma conferma il testo di DJ5HG: da Amburgo aperta fino alle 2:30 circa, da Monaco fino alle 0:30 circa. Puntamenti: scarti di 2–10° (Barcellona 225° e 233° contro 223° e 235° prima del buco, 160° contro 169° dopo; Mosca 84° contro 82°, 79° contro 76°; Narvik salta verso 338° alle 20:40 in DJ5HG, tra le 20 e le 21 nel programma). Livelli e forma, a 102 km (scarto medio e scarto tipico rispetto alle curve): senza β e senza scie lunghe −1,6 e 4,0 dB; con le scie lunghe +1,1 e 4,6 dB; con l\'angolo β −5,4 e 6,2 dB, ma con la forma migliore (3,0 dB tolto lo scarto medio, contro 3,6): compaiono i minimi profondi con il radiante basso (Barcellona −15,6 dB alle 17, contro −16 dB alle 19:36; Sofia −18,5 dB alle 20, contro −14 dB). Con β e scie lunghe (impostazione "come DJ5HG") −2,2 e 4,7 dB; l\'impostazione prudente (quota del radar, 89,5 km, con β, senza scie lunghe) dà −6,9 e 7,6 dB, con forma 3,3 dB. Senza β il programma vede appena il minimo con il radiante basso quasi allineato alla tratta (−8,6 e −10,4 dB): è il caso della riserva di DJ5HG, per questo resta l\'avviso.'));
C.push(TAG('RILIEVO', 'La documentazione di MS-Soft 5.2 [29] definisce l\'efficienza di OH5IY come indice relativo per le sole scie sottodense, con due fattori: elevazione del radiante (ottimo circa 45°) e angolo con la tratta (90° = massimo). Il minimo è portato a mano al 20 % per le sovradense; la formula non è pubblicata. MCG_MS [3] calcola l\'efficienza per quattro direzioni fisse e, scrivendo il locator del corrispondente, anche per la tratta reale.'));
C.push(H2('5.5 Lato delle riflessioni e indice della tratta'));
C.push(TAG('SCELTA', 'Frazione delle riflessioni dal lato A (sinistra della tratta); nella tabella oraria compare la lettera del lato prevalente:'));
C.push(EQ(sb('f', 'A'), '=', fr(sum('P∈A', [sb('w', 'P'), sb('S', 'P'), '(ŝ·', sb('û', 'P'), ')']), sum('P', [sb('w', 'P'), sb('S', 'P'), '(ŝ·', sb('û', 'P'), ')']))));
C.push(TAG('FONTE', 'Side-scatter: spostamento del puntamento di 10–30° verso il lato prevalente [1].'));
C.push(TAG('SCELTA', 'Indice della tratta, somma su tutti gli sciami attivi:'));
C.push(EQ('I', br('t'), '=', sum('sciami', [fr(['ZHR', br('t'), '·', 'η', br('t')], '100')])));

C.push(H2('5.6 Zone PREV in pianta e sezione vista dall\'antenna'));
C.push(TAG('SCELTA', 'Per l\'ora mostrata il programma somma, punto per punto dello strato E, il contributo di ogni sciame attivo all\'efficienza (la stessa condizione di riflessione speculare del capitolo 5), pesato con lo ZHR. I punti con almeno il 3 % del massimo formano le zone PREV, una per lato della tratta, disegnate in pianta come ellissi: centro = media pesata dei punti, assi = due volte la loro dispersione. È la regola pratica: se lo sciame scorre da nord a sud, le scie utili cadono a est e a ovest. La linea gialla indica la direzione di scorrimento (azimut del radiante) dello sciame selezionato, o del più favorevole.'));
C.push(EQ(sb('W', 'P'), '=', sum('sciami', ['ZHR·', sb('c', 'P'), br('ŝ')]), ',    ', sb('c', 'P'), '=100·', fr([sb('w', 'P'), sb('S', 'P'), 'max', br('0 , ŝ·', sb('û', 'P'))], [sb('max', 'ŝ′'), ' F', br('ŝ′')]), ',    PREV: ', sb('W', 'P'), '≥0,03·max W'));
C.push(TAG('SCELTA', 'La sezione mostra le stesse scie viste dalla stazione con l\'antenna puntata verso il corrispondente: in orizzontale l\'azimut rispetto al corrispondente (A a sinistra, B a destra), in verticale l\'elevazione. Per ogni sciame si prendono i 14 punti di riflessione più forti; ogni scia è un segmento orientato verso il radiante, da 10 km sopra a 10 km sotto la quota delle scie (al massimo 60 km per lato), più spesso quanto più è probabile. Sono disegnati anche il lobo dell\'antenna (cerchio a −3 dB attorno all\'elevazione del lobo), il corrispondente e Hot A / Hot B.'));
C.push(EQ('Q=P±', sb('t', '½'), 'ŝ,    ', sb('t', '½'), '=min', br('60 km , ', fr('10 km', ['max(0,17 , |ŝ·', sb('û', 'P'), '|)']))));
C.push(H1('6. Attenuazione e bilancio'));
C.push(TAG('FONTE', 'Equazione di McKinley [8] e della Raccomandazione ITU-R P.843 [28] per le scie sottodense (sin α = 1), guadagni d\'antenna esclusi; q densità lineare di elettroni della scia, re raggio classico dell\'elettrone = 2,818·10⁻¹⁵ m, β angolo tra la scia e il piano della tratta, a1 fattore del raggio iniziale della scia r0 (P.843, eq. 4 e 7; r0 in m, h quota in km):'));
C.push(EQ('L=10 ', sb('log', '10'), sbr(fr(['16 ', sp('π', '2'), sb('R', '1'), sb('R', '2'), br(sb('R', '1'), '+', sb('R', '2')), br('1−', sp(fn('cos', 'β'), '2'), sp(fn('sin', 'φ'), '2'))], [sp('λ', '3'), sp('q', '2'), sp(sb('r', 'e'), '2')])), '−10 ', sb('log', '10'), sb('a', '1'), '  dB'));
C.push(EQ(sb('a', '1'), '=', sp('e', ['−', fr(['8', sp('π', '2'), sp(sb('r', '0'), '2')], [sp('λ', '2'), sp(fn('sec', 'φ'), '2')])]), ',    ', sb('log', '10'), sb('r', '0'), '=0,035 h−3,45'));
C.push(TAG('SCELTA', 'Nel bilancio si usa β = 90° (scia che attraversa il piano della tratta, il caso più sfavorevole: valore prudente) e si mostra anche il caso migliore, β = 0. Il raggio iniziale si calcola alla quota delle scie usata dal programma; nelle regole tra le bande (λ³ di SM6FHZ) non si aggiunge, perché quelle regole sono sperimentali e lo contengono già.'));
C.push(TAG('RILIEVO', 'Con q = 10¹⁴ elettroni/m, scie a 89,5 km e β = 0, a 144 MHz risultano 182–192 dB tra 600 e 2100 km (185 dB a 1000 km). L\'intervallo di 172–190 dB calcolato da John Worsnop G4BAO nella sua tesi di dottorato, riportato da GM8JBJ [9], comprende questi valori. Con β = 90° l\'attenuazione cresce di 10 dB a 600 km, 13 dB a 1000 km e 16 dB a 2100 km: i 200 dB medi di OH5IY citati nell\'articolo [1] stanno tra i due casi. Sempre secondo GM8JBJ, G4BAO trova circa 6 dB in meno per le scie allineate alla tratta.'));
C.push(TAG('RILIEVO', 'I 182 dB della tabella di GM8JBJ [9] non sono una conferma: la tabella non indica la frequenza, i suoi 86,4 dB per tratto sono la perdita in spazio libero su 500 km a 1 MHz (manca il termine 20 log f: a 144 MHz sono 129,6 dB) e la somma delle voci, 86,4 + 0 − 9 + 86,4, fa 163,8 dB e non 182. La pagina non parla né di valore minimo né di 144 MHz.'));
C.push(TAG('RILIEVO', 'Raggio iniziale alla quota media degli echi, h = 124 − 17 log f [28]: r0 = 0,76 m a 95 km per 50 MHz, 0,40 m a 87 km per 144 MHz, 0,21 m a 79 km per 432 MHz. Su 1000 km a1 vale 0,2 dB a 50 MHz, 0,6 dB a 144 MHz e 1,4 dB a 432 MHz (2,9 dB a 600 km). Alla quota fissa di 102 km di DJ5HG darebbe a 432 MHz circa 70 dB, cioè nessun eco: per questo si usa la quota media degli echi alla frequenza.'));
C.push(TAG('RILIEVO', 'Incertezza del raggio iniziale: Stober et al. [34], con il radar CMOR a 17,45, 29,85 e 38,15 MHz e un modello di diffusione a onda piena, trovano tra 85 e 95 km r0 di 0,5–2 m, per lo più 1–1,5 m, con una dispersione di un fattore due a ogni quota; per la polarizzazione trasversale i valori sono circa il doppio delle misure precedenti (Greenhow e Hall 1960; Jones e Campbell-Brown 2005). Solo il 5 % circa degli echi si lascia descrivere dal modello ideale. La formula ITU-R P.843 [28] dà 0,5 m a 90 km e 0,75 m a 95 km, cioè il limite basso di queste misure.'));
C.push(TAG('SCELTA', 'Il programma offre la scelta "Raggio iniziale della scia" nella sottolinguetta Geometria e attenuazione: doppio dell\'ITU (di partenza, prudente, come le misure di Stober et al.), ITU-R P.843, escluso. Raddoppiando r0 il fattore a1 in dB si moltiplica per 4: su 1000 km 0,8 dB a 50 MHz, 2,4 dB a 144 MHz e 5,6 dB a 432 MHz (11,6 dB a 600 km). Le misure CMOR sono a frequenze più basse e a 85–95 km: usarle a 432 MHz, dove gli echi vengono da circa 79 km, è un\'estrapolazione.'));
C.push(EQ(sb('P', 'rx'), '=', sb('P', 'tx'), br('dBm'), '+', sb('G', 'tx'), '−L+', sb('G', 'rx')));
C.push(TAG('SCELTA', 'I guadagni d\'antenna si usano in dBi, senza togliere i 2,15 dB del dipolo: la perdita di McKinley è riferita ad antenne isotrope. Così EIRP = potenza + guadagno, come nell\'articolo [1] (400 W e 14 dBi danno circa +70 dBm).'));
C.push(EQ('margine=', sb('P', 'rx'), '−', sb('P', 'min'), ',    ', sb('P', 'min'), '=−130 dBm  [1]'));

C.push(H1('7. Antenna e lobo'));
C.push(TAG('FONTE', 'Guadagno di una Yagi lunga in funzione della lunghezza del boom L (curva DL6WU [10], valida da circa 2 λ):'));
C.push(EQ('G=7,773 ', sb('log', '10'), br(fr('L', 'λ')), '+11,43  dBi'));
C.push(TAG('RILIEVO', 'Verifica con le simulazioni NEC di W4RNL a 432 MHz [12][19][20]: DL6WU 13, 22 e 31 elementi (3,23 / 6,82 / 10,42 λ) 15,28 / 17,82 / 19,35 dBi, formula 15,38 / 17,91 / 19,34 dBi; Yagi VK3AUU di David Tanner, con boom più corto a pari elementi, 16, 28 e 40 elementi (3,12 / 6,88 / 10,79 λ) 15,17 / 17,91 / 19,46 dBi, formula 15,27 / 17,94 / 19,45 dBi. Lo scarto non supera 0,1 dB: il guadagno dipende dalla lunghezza del boom più che dal progetto. Il calcolatore di VK5DJ [21] offre anche stime per le varianti VK3AUU, WA2PHW e DJ9BV, di cui non sono pubblicate le formule.'));
C.push(TAG('FONTE', 'Apertura a −3 dB dal guadagno, regola di Kraus [11], con lobo circolare (θE = θH = θK):'));
C.push(EQ(sb('G', 'lin'), '=', fr('41253', [sb('θ', 'E'), sb('θ', 'H')]), '   ⇒   ', sb('θ', 'K'), '=', sq(fr('41253', sp('10', 'G/10')))));
C.push(TAG('RILIEVO', 'Le simulazioni NEC delle Yagi DL6WU [19] danno un lobo orizzontale più stretto di Kraus del 5–10 %: 33,8° / 26,4° / 22,6° per 12, 19 e 26 elementi, contro 37,3° / 28,0° / 23,9° di Kraus. Le formule semplici ignorano i lobi laterali in avanti [12]. Sui boom lunghi il lobo verticale è di poco più largo dell\'orizzontale (14 λ: 18,4° / 18,8°).'));
C.push(TAG('SCELTA', 'Lobo orizzontale (piano E, azimut con polarizzazione orizzontale) = 0,93 · θK; lobo verticale (piano H) = θK. Regole approssimate, ricavate da poche antenne DL6WU:'));
C.push(EQ(sb('θ', 'oriz'), '=0,93·', sb('θ', 'K'), ',    ', sb('θ', 'vert'), '=', sb('θ', 'K')));
C.push(TAG('RILIEVO', 'Yagi di 14 λ a 432 MHz: 20,3 dBi, lobo 18,1° orizzontale e 19,5° verticale. I modelli di W4RNL [12] danno 20,4 dBi e 18,4° / 18,8°.'));
C.push(TAG('SCELTA', 'L\'antenna si considera puntata verso il corrispondente. Un hot spot (paragrafo 4.5) è nel lobo se |Az(Hot) − Az(antenna)| ≤ θoriz/2: in quel caso è segnato in grigio invece che in rosa e la finestra principale avvisa. L\'hot spot consigliato dall\'efficienza (paragrafo 4.6) è sempre in rosso.'));

C.push(H1('8. Flusso dal radar e traslazione di frequenza'));
C.push(H2('8.1 Lettura del grafico di Collm'));
C.push(TAG('SCELTA', 'Il grafico SKiYMET di Collm [7] (720×720 pixel, colori puri) ha posizioni fisse degli assi, ma il radar adatta ogni giorno la scala verticale ai valori misurati (per esempio 0–1,2 ·10³ il 5/11/2026 e 0–1,0 ·10³ il 6/11/2026, con tacche spostate). Il programma trova le tacche lunghe dell\'asse e legge le etichette della più alta e della più bassa (0.0) confrontando ogni carattere con i modelli del carattere a matrice del grafico. Per l\'ora i-esima (0–47, ieri e oggi) la colonna centrale e il primo pixel ciano dall\'alto y danno:'));
C.push(EQ(sb('x', 'i'), '=101+', br('i+0,5'), fr('676−101', '48'), ',    N=', br([sb('y', '0'), '−y']), fr(sb('N', 'top'), [sb('y', '0'), '−', sb('y', 'top')]), '  meteore/ora'));
C.push(P('ytop e y0 sono le righe della tacca più alta e di quella dello zero, Ntop il valore letto sull\'etichetta più alta (×1000). La risoluzione è di circa 7–8 meteore/ora per pixel. Se un\'etichetta non si riesce a leggere, il programma torna alla taratura del 5/11/2026 (0–1200) e lo segnala nella sottolinguetta "Live e dati real-time › Flusso radar".'));
C.push(H2('8.2 Statistica delle quote'));
C.push(TAG('SCELTA', 'Istogramma per km tra 70 e 110 km (nk meteore nel km k, quota media hk):'));
C.push(EQ(sb('h', 'moda'), '=', sb('h', [sb('k', '*')]), ',   ', sb('k', '*'), '=', sb('argmax', 'k'), ' ', sb('n', 'k'), ',    ', 'h̄=', fr(sum('k', [sb('n', 'k'), sb('h', 'k')]), sum('k', sb('n', 'k'))), ',    ', 's=', sq(fr(sum('k', [sb('n', 'k'), sp(br(sb('h', 'k'), '−h̄'), '2')]), sum('k', sb('n', 'k'))))));
C.push(H2('8.3 Traslazione a un\'altra frequenza'));
C.push(TAG('FONTE', 'Regole sperimentali di SM6FHZ [4]: il numero (e l\'intensità) delle riflessioni scala con λ³, la durata con λ². Con f0 = 36,2 MHz (Collm) e f la frequenza di arrivo:'));
C.push(EQ(sb('N', 'f'), '=', sb('N', sb('f', '0')), '·', sp(br(fr(sb('f', '0'), 'f')), 'k'), '·K,    k=3'));
C.push(EQ(sb('τ', 'f'), '=', sb('τ', sb('f', '0')), '·', sp(br(fr(sb('f', '0'), 'f')), '2'), '·', sp(fn('sec', 'φ'), '2')));
C.push(TAG('FONTE', 'La durata di una scia sottodensa vale τ = λ²·sec²φ / (16π²D), con D coefficiente di diffusione (McKinley [8]; OH5IY [29]; IZ5TEK [30]). Il radar di Collm misura in backscatter (φ = 0); su una tratta in forward scatter la durata cresce di sec²φ, con φ al punto medio: ×4 a 60°, ×8,5 a 70°, ×33 a 80°. La sottolinguetta Attuazione sperimentale previsioni lo applica.'));
C.push(TAG('RILIEVO', 'Misure reali (HamSCI, Meteor Scatter QSO Party [33]): R. Suggs NN4NT ha misurato la costante di decadimento della potenza di 1298 echi sottodensi nelle registrazioni MSK144 di NN4SA (EM64) durante le Perseidi 2026 (4736 file WAV di WSJT-X). Mediane: 148 ms a 28,145 MHz (41 echi), 78 ms a 50,260 MHz (1198), 53 ms a 144,150 MHz (59). Con λ² partendo dai 6 m sarebbero circa 245 ms e 9,5 ms: in 2 m i ping durano più di cinque volte quanto previsto. L\'autore lo attribuisce a un probabile effetto del soffitto di quota in 2 m: alle frequenze alte restano visibili soprattutto le scie basse, dove la diffusione è più lenta. È un\'analisi preliminare: una sola stazione ricevente, distanze diverse non normalizzate con sec²φ, solo gli echi abbastanza forti da essere rilevati.'));
C.push(TAG('FONTE', 'Weitzen e Ralston [31]: la costante di decadimento varia da scia a scia con distribuzione esponenziale, con media τ = λ²·sec²φ / (32π²D) (costante della potenza; 16π² vale per l\'ampiezza). Xia, Li e Zheng [32] danno D in funzione della quota, D = 10^(0,067·h − 5,6) m²/s: su 1000 km con la scia a 95 km risulta τ ≈ 47 ms a 144 MHz e 390 ms a 50 MHz. Il valore a 144 MHz è vicino alla mediana misurata, quello a 50 MHz è cinque volte più alto: D cresce di 10 volte ogni 15 km di quota, quindi la quota delle scie visibili, che cambia con la frequenza, pesa sulla durata più di λ².'));
C.push(TAG('SCELTA', 'Il programma offre la scelta "Durata dei ping tra le bande" nella sottolinguetta Geometria e attenuazione. Teorica (di partenza, prudente): λ², che dà i ping più brevi. Osservata: interpolazione lineare in scala logaritmica tra le tre mediane di NN4SA; sotto 28 MHz si prolunga il tratto 10–6 m, sopra 144 MHz, dove non ci sono misure, si torna a λ². Con la scelta osservata un eco di 1 s a Collm (36,2 MHz) dura circa 473 ms a 144 MHz invece di 63 ms, e da 50 a 144 MHz i ping si accorciano di 1,5 volte invece di 8.'));
C.push(TAG('RILIEVO', 'In McKinley [8] λ³ è la potenza di una singola scia sottodensa, non il numero di scie. A soglia fissa e con indice di massa s, il numero di scie sopra soglia scala con λ elevato a 1,5·(s − 1), cioè circa λ^1,5 per s = 2 (IZ5TEK [30]; OH5IY [29]). Il programma tiene k = 3, la regola sperimentale di SM6FHZ [4], e lo dichiara: con k = 3, 1000 meteore/ora a Collm diventano circa 16 riflessioni/ora a 144 MHz, con k = 1,5 circa 127. Gli osservatori RMOB del radar GRAVES a 143,050 MHz [13] contano in genere da 20 a 140 eco/ora; il valore giusto di k per la propria stazione si ricava dal confronto con RMOB (paragrafo seguente).'));
C.push(TAG('SCELTA', 'Il pulsante "k dagli indici di popolazione" calcola per ogni sciame attivo k = 1,5·(s − 1) con s = 1 + 2,5·log10 r, cioè k = 3,75·log10 r, e ne fa la media pesata con lo ZHR. L\'indice di popolazione r viene dalla tabella della pagina del flusso del Global Meteor Network [37] quando c\'è, altrimenti dal catalogo IMO [5]; la linguetta Sciami mostra k per ogni sciame. Esempi: Perseidi r = 2,2, k = 1,28; Geminidi r = 2,6, k = 1,56. Il valore di partenza resta k = 3 di SM6FHZ [4], più prudente; i conteggi di Collm sono però per lo più meteore sporadiche, di cui il GMN non pubblica r.'));
C.push(H2('8.4 Esponente ricavato da un file RMOB'));
C.push(TAG('SCELTA', 'Con K = 1, dalla mediana dei rapporti tra i conteggi RMOB e quelli di Collm nelle stesse ore:'));
C.push(EQ(sb('k', 'emp'), '=−', fr(['ln ', fn('mediana', br(fr(sb('N', 'RMOB'), sb('N', 'Collm'))))], ['ln ', br(fr('f', sb('f', '0')))])));
C.push(H2('8.5 Previsione delle prossime 24 ore'));
C.push(TAG('SCELTA', 'Persistenza: il valore traslato della stessa ora del giorno prima, corretto con la variazione dell\'indice della tratta (5.5). La costante 10 rappresenta il fondo sporadico e limita la correzione quando l\'indice è piccolo:'));
C.push(EQ(sb('N', 'prev'), br('t'), '=', sb('N', 'f'), br('t−24 h'), '·', fr(['I', br('t'), '+10'], ['I', br('t−24 h'), '+10'])));

C.push(H1('9. Mappa dei quadrati da ADIF'));
C.push(TAG('FONTE', 'Formato ADIF (campi CALL, GRIDSQUARE, VUCC_GRIDS, BAND, FREQ, QSO_DATE, QSL_RCVD, LOTW_QSL_RCVD). Banda dal campo BAND oppure dalla frequenza: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.'));
C.push(TAG('SCELTA', 'Un quadrato (4 caratteri) è "confermato" se almeno un QSO ha QSL_RCVD = Y o LOTW_QSL_RCVD = Y. Il caricamento di un nuovo ADIF sostituisce i dati precedenti.'));

C.push(H1('10. Raccolta dati e traffico in diretta'));
C.push(H2('10.1 Riconoscimento degli spot meteor scatter'));
C.push(TAG('SCELTA', 'Gli spot arrivano in telnet da tre flussi (un DX cluster a scelta, Reverse Beacon Network, il cluster di DM4X con PSKReporter) come righe "DX de SPOTTER: FREQ DX commento HHMMZ", e dalla quarta fonte, PSKReporter via MQTT (mqtt.pskreporter.info, servizio di M0LTE), come messaggi JSON gia\' strutturati: frequenza, modo, rapporto, ora, nominativo e locator di chi trasmette e di chi riceve. Gli argomenti di partenza sono MSK144 su 6 m, 4 m, 2 m, 1,25 m e 70 cm e FSK441 su 2 m; anche questi spot passano dagli stessi criteri. Con la casella accesa le righe sotto 27990,0 kHz si scartano subito (regola dell\'autore). Uno spot è meteor scatter se soddisfa il primo criterio oppure, fuori dalle finestre o con una scritta di altra propagazione, il secondo:'));
C.push(bullet([B('1° criterio (regola dell\'autore): '), 'frequenza nelle finestre tipiche degli spot MS, 50190–50300, 70100–70400, 144290–144399 kHz, e nessuna scritta di altra propagazione nel commento (<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>).']));
C.push(bullet([B('2° criterio: '), 'il commento contiene, in maiuscolo, minuscolo o misto, un modo digitale usato solo per il MS (MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M) oppure la scritta <MS>.']));
C.push(TAG('SCELTA', 'Locator: quelli scritti nello spot; se mancano o hanno solo 4 caratteri si prende quello a 6 caratteri dell\'archivio CALL3 (call3.txt di JTDX), anche se indica un altro quadrato (regola dell\'autore).'));
C.push(TAG('FONTE', 'Conteggi del Global Meteor Network [37]: nella linguetta Sciami in diretta e nella colonna "GMN oggi" della linguetta Sciami il programma legge il riassunto giornaliero delle traiettorie confermate dalle telecamere della rete (una riga per meteora, con il codice IAU dello sciame o "..." per le sporadiche) e le conta per sciame. È un conteggio, non un flusso: dipende da quante stazioni hanno il cielo sereno e buio. Dati CC BY 4.0.'));
C.push(H2('10.2 Nuvola delle scie probabili di un contatto'));
C.push(TAG('SCELTA', 'Per ogni spot con i due locator il programma costruisce la tratta tra le due stazioni (capitoli 3 e 4) e, all\'ora dello spot, somma punto per punto dello strato E i contributi di riflessione speculare di tutti gli sciami attivi pesati con lo ZHR (stesso calcolo delle zone PREV, paragrafo 5.6). Per ciascun lato della tratta che raccoglie almeno il 15 % del totale si calcolano la media pesata dei punti e la loro dispersione (in km, sul piano locale x = est, y = nord):'));
C.push(EQ('x̄=', fr(sum('P', [sb('W', 'P'), sb('x', 'P')]), sum('P', sb('W', 'P'))), ',    ', sb('σ', 'xx'), '=', fr(sum('P', [sb('W', 'P'), sp(br(sb('x', 'P'), '−x̄'), '2')]), sum('P', sb('W', 'P'))), ',  ', sb('σ', 'yy'), ',  ', sb('σ', 'xy'), ' analoghi'));
C.push(TAG('SCELTA', 'La nuvola è l\'ellisse con centro nella media, semiassi pari a 1,5 volte le radici degli autovalori della matrice di dispersione (minimo 30 e 20 km) e asse maggiore nella direzione dell\'autovettore principale:'));
C.push(EQ(sb('λ', '1,2'), '=', fr([sb('σ', 'xx'), '+', sb('σ', 'yy')], '2'), '±', sq([sp(br(fr([sb('σ', 'xx'), '−', sb('σ', 'yy')], '2')), '2'), '+', sp(sb('σ', 'xy'), '2')]), ',    ', sb('a', '1,2'), '=1,5', sq(sb('λ', '1,2')), ',    θ=', fr('1', '2'), 'atan2', br('2', sb('σ', 'xy'), ' , ', sb('σ', 'xx'), '−', sb('σ', 'yy'))));
C.push(TAG('SCELTA', 'Se nessuno sciame contribuisce (solo meteore sporadiche) le nuvole sono i due hot spot classici (paragrafo 4.5), cerchi tratteggiati di 70 km. La mappa è azimutale equidistante centrata sulla stazione: gli spot con una stazione oltre il raggio scelto non si disegnano; gli spot arrivati da meno di un minuto e non più vecchi di 3 minuti lampeggiano.'));

C.push(H1('11. Limiti noti'));
['Il modello considera solo le scie sottodense. Le sovradense (burst lunghi) e il fondo sporadico non entrano nell\'efficienza; il fondo sporadico è rappresentato dal flusso radar.',
 'Le antenne sono considerate isotrope nel calcolo dell\'efficienza; il lobo reale serve solo per il controllo degli Hot.',
 'Le derive del radiante e i coefficienti B del profilo di attività sono valori di lavoro.',
 'La lettura del grafico di Collm dipende dal formato attuale: se cambia, va ritarata.',
 'Le percentuali di efficienza vanno confrontate con MCG_MS, MS-Soft e con le osservazioni in banda.'].forEach(t => C.push(bullet(t)));

C.push(H1('12. Fonti'));
[
 'C. Cerrotta IC8TEM, G. Sartori IV3GTH - "METEOR-SCATTER. Ovvero come collegare l\'Europa in VHF tutto l\'anno senza tante pretese", articolo, versione 7 (fonte principale).',
 'I. Yrjölä OH5IY - MS-Soft, www.kolumbus.fi/oh5iy (sito storico), con i dati EURO.DAT, ZHRDATA e MSDATA.',
 'W. Rauh DL5MCG - MCG_MS, MS Efficiency Calculator v1.61, qsl.net/dl5mcg.',
 'SM6FHZ - "432 MHz Meteorscatter, Challenges and Techniques", 45th Nordic VUSHF, maggio 2025.',
 'International Meteor Organization - Meteor Shower Calendar 2026, www.imo.net.',
 'J. Meeus - Astronomical Algorithms, 2ª ed., Willmann-Bell, 1998.',
 'Radar meteorico di Collm, Università di Lipsia (LIM) e IAP Kühlungsborn - wetterdaten.meteo.uni-leipzig.de/radar_flux.php.',
 'D.W.R. McKinley - Meteor Science and Engineering, McGraw-Hill, 1961.',
 'GM8JBJ - Meteor scatter path loss, hamradio.engineering (da Kaiser & Closs, 1952).',
 'G. Hoch DL6WU - curva del guadagno delle Yagi lunghe, riportata da W8IO, www.w8io.com.',
 'J.D. Kraus - Antennas, McGraw-Hill.',
 'L.B. Cebik W4RNL - Long-Boom Yagi Rules of Thumb: A Comparison with Modeling Data.',
 'RMOB, Radio Meteor Observatories On Line - www.rmob.org, bollettino di giugno 2018 (osservatori GRAVES 143,050 MHz).',
 'Natural Earth - coste e confini 1:50 milioni, dominio pubblico, www.naturalearthdata.com.',
 'AMS Bulletin n. 203, "The AMS Radiometeor Project", tabella degli offset d\'antenna, ripresa da S. W8WN, qsl.net/w8wn/hscw/papers/ms_az_el.html.',
 'LZ2HV - MSHV, programma per i modi digitali MS (calcolo di Hot A / Hot B).',
 'J. DF5HC - "Meteorscatter auf UKW", conferenza DARC, gennaio 2018 (formula della migliore direzione di DH9GCD; diffusione a cono e HOT-A / HOT-B di DJ5HG, "Meteorscatter Propagation", www.vhfdx.de/mseff/MS-Geometrie.pdf; meteore sporadiche di KB0VUK).',
 'K. von der Heide DJ5HG - QTFGUI, programma per i puntamenti in aurora, FAI e meteor scatter, con manuale "QTFGUI Help" (2007) e dati meteorshowerdata.txt.',
 'L.B. Cebik W4RNL - Appreciating DL6WU Wide-Band Long-Boom Yagi Design (simulazioni NEC, 432 MHz).',
 'L.B. Cebik W4RNL - 70-CM Yagi Stacks Part 2: 10- to 40-Element VK3AUU Examples (Yagi di David Tanner VK3AUU).',
 'J. Drew VK5DJ - Yagi Calculator (stime del guadagno per le varianti VK3AUU, WA2PHW, DJ9BV).',
 'K. von der Heide DJ5HG - "Die Geometrie von Meteorscatterverbindungen", agosto 2004 (legge del cono, efficienza relativa a riferimento fisso, scie utili fino a 100 km, quota 102 km).',
 'J. Richardson (AMS) - "Some Notes and Equations for Forward Scatter": scarti d\'antenna di 13°, 11°, 10° e 10° a 1000, 1250, 1500 e 2000 km, tabella riportata da DJ5HG.',
 'V.R. Eshleman, R.F. Mlodnosky - "Directional Characteristics of Meteor Propagation Derived from Radar Measurements", Proc. IRE 45(12), 1715-1723, 1957.',
 'M.L. Meeks, J.C. James - "On the Influence of Meteor-Radiant Distributions in Meteor-Scatter Communication", Proc. IRE 45(12), 1724-1733, 1957.',
 'C.O. Hines - "Diurnal Variations in the Number of Shower Meteors Detected by the Forward-Scattering of Radio Waves, Part I: Theory", Can. J. Phys. 33, 493-503, 1955.',
 'P.A. Forsyth, C.O. Hines, E.L. Vogan - stesso titolo, "Part II: Experiment", Can. J. Phys. 33, 600-606, 1955.',
 'ITU-R P.843-1 - "Communication by meteor-burst propagation", 1997.',
 'I. Yrjölä OH5IY - "Meteors & Communication", parte 2, documentazione di MS-Soft 5.2 (2017).',
 'R. Pardini IZ5TEK - "Il meteor-scatter e i collegamenti radioamatoriali via meteor-scatter", ARI Pisa, 2014.',
 'J.A. Weitzen, W.T. Ralston - "Meteor Scatter: An Overview", IEEE Transactions on Antennas and Propagation 36(12), 1813-1819, 1988.',
 'B. Xia, L. Li, Y. Zheng - "Modeling and Simulation of the Meteor Burst Channel", Telecommunications Science, 2016 (9), DOI 10.11959/j.issn.1000-0801.2016206 (English translation by R. Hipple, github.com/HamSCI/MSQP).',
 'R. Suggs NN4NT, HamSCI Meteor Scatter Working Group - "MSQP data analysis progress", 4 November 2026, underdense_decay, github.com/HamSCI/MSQP (NN4SA, 2026 Perseids, Zenodo).',
 'G. Stober, P. Brown, M. Campbell-Brown, R.J. Weryk - "Triple-frequency meteor radar full wave scattering: Measurements and comparison to theory", Astronomy & Astrophysics, 2021, arXiv:2108.07647.',
 'meteor-mcp, qso-graph - meteor scatter MCP server, github.com/qso-graph/meteor-mcp, 2026.',
 'IAU Meteor Data Center - established showers list, www.ta3.sk/IAUC22DB/MDC2022 (Jenniskens et al., Planetary and Space Science 182, 104821, 2020; Jopek & Kaňuchová, Planetary and Space Science 143, 3-6, 2017).',
 'Global Meteor Network - shower flux and daily trajectory summary, globalmeteornetwork.org, CC BY 4.0 (Vida et al. 2021, 2022).',
 'M. Bundscherer - "Meteor Detection based on Forward Scattering with SDR and the BRAMS Beacon", WGN, Journal of the IMO 54(2), April 2026; code and data (Sonneberg, August 2026): github.com/maxbundscherer/meteor-scatter-v2.',
].forEach((t, i) => C.push(new Paragraph({ numbering: { reference: 'num', level: 0 }, spacing: { after: 60 }, children: [new TextRun(t)] })));

const doc = new Document({
  creator: 'Costantino IC8TEM', title: T('YA-MS - Manuale dei calcoli'),
  styles: {
    default: { document: { run: { font: FONT, size: 22 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', next: 'Normal', run: { font: FONT, size: 44, bold: true, color: '1F3864' }, paragraph: { spacing: { before: 0, after: 160 }, keepNext: true } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 32, bold: true, color: '1F3864' }, paragraph: { spacing: { before: 360, after: 120 }, keepNext: true, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 26, bold: true, color: '2F5496' }, paragraph: { spacing: { before: 240, after: 100 }, keepNext: true, outlineLevel: 1 } },
    ],
  },
  numbering: { config: [
    { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
    { reference: 'num', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 400 } } } }] },
  ] },
  features: { updateFields: true },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: 'YA-MS - Manuale dei calcoli - pagina ', size: 18, color: '808080' }), new TextRun({ children: [PageNumber.CURRENT], size: 18, color: '808080' })] })] }) },
    children: C,
  }],
});
if (process.env.ESTRAI) fs.writeFileSync(process.env.ESTRAI, JSON.stringify(KEYS, null, 1));
if (MISS.length) console.log('testi senza traduzione (' + LANG + '):', MISS.length);
Packer.toBuffer(doc).then(b => { fs.writeFileSync(process.argv[2], b); console.log('ok', LANG, eqn, 'equazioni'); });
