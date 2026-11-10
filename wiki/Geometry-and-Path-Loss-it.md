[English](Geometry-and-Path-Loss) · **Italiano** · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-BR) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-TW)

# Geometria e attenuazione

*Linguetta: Calcolo previsionale › Geometria e attenuazione.*

[![Geometria e attenuazione](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/it-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/it-2_2.png)

Un resoconto testuale della tratta (selezionabile, così puoi copiarlo) e, a destra, il grafico **Elevazione d'antenna in funzione della distanza dallo scatter point**. I numeri tra parentesi rimandano alle equazioni del manuale dei calcoli (`doc/YA-MS_manuale_calcoli.docx`).

## Dati di questa linguetta

| Campo | Predefinito | Uso |
|---|---|---|
| **Potenza W** | 400 | Potenza del trasmettitore per il bilancio del collegamento |
| **Guadagno antenna dBi (tx = rx)** | 14 | Stessa antenna ai due estremi |
| **Segnale minimo dBm** | −130 | Segnale minimo rilevabile (articolo: Yagi a 8 elementi + preamplificatore) |
| **Densita' scia q = 10^ … elettroni/m** | 14 | Densità lineare di elettroni della scia sottodensa |

Stazioni, banda, quota delle scie, elevazione del lobo, boom e distanza degli hot spot vengono dalle [righe di comandi](Getting-Started-it#1-le-tre-righe-di-comandi).

## Sezioni del resoconto

| Sezione | Contenuto |
|---|---|
| **GEOMETRIA DELLA TRATTA (Terra sferica, R = 6372,7955 km)** | Stazione e corrispondente con le quote; distanza, azimut e azimut inverso; punto medio (locator e coordinate); quota delle scie (*<- moda misurata dal radar Collm* quando è presa dal radar); elevazione d'antenna verso il punto medio |
| **HOT A / HOT B (hot spot classici, per il puntamento d'antenna)** | Per ciascuno: locator, azimut da te e scostamento dalla tratta diretta, azimut dal corrispondente, distanza, elevazione |
| **LIMITI DELLA ZONA COMUNE** | Portata alla quota delle scie con l'elevazione del lobo; Limite A / Limite B con gli azimut |
| Antenna | Boom in λ, guadagno, lobo orizzontale / verticale; se Hot A e Hot B sono dentro o fuori dal lobo |
| **ATTENUAZIONE DI TRATTA (scia sottodensa, McKinley 1961; guadagni d'antenna esclusi)** | Tabella per il punto medio (forward), Hot A e Hot B a 28, 50, 70, 144, 222 e 432 MHz |
| **BILANCIO A … MHz (punto medio)** | Potenza ed EIRP, attenuazione di tratta, segnale in antenna, minimo rilevabile, **margine**; lo stesso margine con l'attenuazione media di OH5IY |
| **REGOLE SPERIMENTALI TRA LE BANDE (SM6FHZ, VUSHF 2025)** | Numero/intensità e durata rispetto a 144 MHz; ping massimo IARU |

## Locator e tratta

Locator (4, 6 o 8 caratteri; centro del quadrato, sistema IARU Maidenhead) [14]. Distanza, azimut e punto medio con le formule ortodromiche su una sfera di raggio **r = 6372,7955 km** (articolo Cerrotta–Sartori) [15–16]. I calcoli che dipendono dall'ora si riferiscono al **punto medio**, perché l'ora migliore può differire fino a 1,5 ore tra i due estremi (SM6FHZ).

## Elevazione d'antenna

**Fonte:** formula dell'articolo Cerrotta–Sartori (Figura 7), con x = d/r, d la distanza al suolo fino al punto di riflessione, H la quota delle scie e h la quota della stazione [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Verifica:** coincide con la geometria sferica esatta entro 0,03°. Il programma usa l'arcotangente a due argomenti, che dà valori negativi oltre l'orizzonte ed evita il problema di periodicità citato nell'articolo. Un'elevazione negativa verso il punto medio significa *tratta oltre la portata geometrica del singolo salto*.

## Portata all'orizzonte

Distanza al suolo alla quale un raggio con elevazione e raggiunge la quota H (inversa geometrica della formula precedente) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Verifica:** H = 89,5 km, e = 0° → **1062 km**. Nell'esempio dell'articolo (JN44BB–IO53RT) il disegno pone gli incroci con l'orizzonte a circa 870 km dalle stazioni, il che corrisponde a un lobo alzato di circa 2° (865 km).

## Limiti della zona comune

**Fonte:** l'articolo individua gli incroci delle curve dove l'orizzonte di ciascuna stazione incontra lo strato E: gli incroci di due cerchi di raggio angolare ρ = d_H/r centrati in A e B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Se 1 − |p0|² < 0 la tratta è più lunga di 2·d_H e le stazioni non vedono **nessuna zona comune dello strato E**.

**Verifica:** questi sono i **bordi più lontani** del cielo visto da entrambe le stazioni, **non punti verso cui puntare**. Su JN70CN–IN78UO (1710 km, azimut 308°) cadono a 1062 km dalla stazione, 37° a sinistra e a destra della tratta diretta, mentre MSHV suggerisce 10°. Per questo si chiamano *Limite A* / *Limite B* e sono disegnati tenui sulla mappa.

## Hot A e Hot B

**Fonte:** le riflessioni delle meteore sporadiche si concentrano in due zone ("hot spot") da una parte e dall'altra del punto medio. J. Richardson (AMS), nella tabella citata da DJ5HG (*Die Geometrie von Meteorscatterverbindungen*, 2004), dà lo scostamento d'antenna rispetto al puntamento diretto: **13° a 1000 km, 11° a 1250 km, 10° a 1500 e 2000 km**. L'AMS Bulletin n. 203, ripreso da W8WN, dà 10° a 1500 e 1800 km.

**Scelta:** Hot A e Hot B sono i punti a distanza s dal punto medio M, perpendicolari alla tratta. Con *auto (AMS)* spuntato (predefinito) s deriva dallo scostamento della tabella di Richardson, interpolato linearmente (13° sotto 1000 km, 10° sopra 2000 km): s = (D/2)·tan(scostamento). Non spuntato, s si inserisce a mano, 30–400 km (MSHV usa 150 km); A a sinistra guardando dalla tua stazione verso il DX, B a destra [21]. Lo scostamento visto dalla stazione è circa [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Verifica:** con la tabella AMS, 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, uguale ai 150 km usati prima e da MSHV; sulle tratte corte la tabella avvicina gli hot spot al punto medio.

## Attenuazione per scie sottodense

**Fonte:** equazione di McKinley e Raccomandazione ITU-R P.843 per le scie sottodense (sin α = 1), guadagni d'antenna esclusi; q = densità lineare di elettroni, r_e = raggio classico dell'elettrone = 2,818·10⁻¹⁵ m, R1, R2 distanze dalla scia, φ metà dell'angolo di diffusione, β angolo tra la scia e il piano della tratta, a₁ fattore del raggio iniziale con r₀ in m e h in km (P.843, eq. 4 e 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Scelta:** il bilancio e la tabella delle attenuazioni usano β = 90° (scia che attraversa il piano della tratta, il caso meno favorevole: valore prudente) e il bilancio mostra anche il caso migliore, β = 0. r₀ è preso alla quota media degli echi per la frequenza, h = 124 − 17 log f (P.843, eq. 15): 0,76 m a 95 km per 50 MHz, 0,40 m a 87 km per 144 MHz, 0,21 m a 79 km per 432 MHz. Su 1000 km a₁ vale 0,2 dB a 50 MHz, 0,6 dB a 144 MHz e 1,4 dB a 432 MHz (2,9 dB a 600 km); alla quota fissa di 102 km di DJ5HG sarebbe circa 70 dB a 432 MHz, cioè nessun eco.

**Verifica:** con q = 10¹⁴ elettroni/m, scie a 89,5 km e β = 0, a 144 MHz: **182–192 dB** tra 600 e 2100 km (185 dB a 1000 km), dentro l'intervallo di **172–190 dB** calcolato da John Worsnop **G4BAO** nella sua tesi di dottorato, come riportato da GM8JBJ. Con β = 90° l'attenuazione cresce di 10 dB a 600 km, 13 dB a 1000 km e 16 dB a 2100 km; i **200 dB medi** di OH5IY stanno tra i due casi. I 182 dB della tabella di GM8JBJ non sono una conferma: la tabella non indica la frequenza, i suoi 86,4 dB per tratto sono l'attenuazione di spazio libero su 500 km a 1 MHz (manca il termine 20 log f: 129,6 dB a 144 MHz) e le sue voci sommano 163,8 dB, non 182; la pagina non dice né "minimo" né "144 MHz".

## Bilancio del collegamento

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. I guadagni si inseriscono e si usano in dBi: l'attenuazione di McKinley si riferisce ad antenne isotrope, quindi non si sottrae la correzione di 2,15 dB del dipolo (EIRP = potenza + guadagno). Il resoconto dà anche il margine con l'**attenuazione media di OH5IY** (200 dB a 144 MHz, scalata con λ³ alla banda scelta). Riferimento dell'articolo: servono circa **70 dBm di EIRP** (−130 dBm + 200 dB, per esempio circa 400 W su 14 dBi).

## Guadagno e lobo dell'antenna

**Guadagno – fonte:** curva di Günter Hoch **DL6WU** per le Yagi lunghe in funzione della lunghezza del boom L, riportata da W8IO (valida da circa 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Verifica con i modelli NEC di L.B. Cebik W4RNL a 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementi | Boom (λ) | W4RNL NEC (dBi) | Formula (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

La differenza non supera mai **0,1 dB**: il guadagno dipende dalla lunghezza del boom più che dal progetto (le Yagi VK3AUU hanno un boom più corto a parità di elementi). Lo Yagi Calculator di VK5DJ dà stime anche per le varianti VK3AUU, WA2PHW e DJ9BV, le cui formule non sono pubblicate.

**Lobo – fonte:** regola di Kraus, con lobo circolare θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Verifica:** i modelli NEC di W4RNL delle Yagi DL6WU danno un **lobo orizzontale più stretto del 5–10 %** rispetto a Kraus: 33,8° / 26,4° / 22,6° per 12, 19 e 26 elementi, contro 37,3° / 28,0° / 23,9°. Le formule semplici ignorano i lobi laterali anteriori (W4RNL, *Long-Boom Yagi Rules of Thumb*). Sui boom lunghi il lobo verticale è un po' più largo di quello orizzontale (14 λ: 18,4° / 18,8°).

**Scelta** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Esempio: Yagi da 14 λ a 432 MHz → 20,3 dBi, lobo di 18,1° in orizzontale e 19,5° in verticale; i modelli di W4RNL danno 20,4 dBi e 18,4° / 18,8°. Sono regole approssimate ricavate da poche antenne DL6WU.

L'antenna si considera sempre puntata verso il DX. Un hot spot è **dentro il lobo** se |Az(Hot) − Az(antenna)| ≤ θ_horizontal/2: allora viene disegnato in grigio nella [Volta celeste](Sky-View-it) e compare un avviso. Nel calcolo dell'efficienza le antenne sono isotrope; il lobo reale si usa solo per questa verifica.

## Regole sperimentali tra le bande

Rispetto a 144 MHz: numero/intensità × (144/f)³ (in dB), durata × (144/f)² (SM6FHZ, VUSHF 2025). Durata massima del ping secondo la IARU Regione 1: 1000 ms a 50 MHz, 500 ms a 70 MHz, 100 ms a 144 MHz, 13 ms a 432 MHz (VHF Handbook, citato nell'articolo). Vedi anche [Attuazione sperimentale previsioni](Experimental-Forecasts-it).
