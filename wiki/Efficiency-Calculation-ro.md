[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · **Română** · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Calculul eficienței

*Filă: Calcul previzional › Calculul eficienței.*

[![Calculul eficienței](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

**Eficiența** unui roi spune, în procente, cât de mult permite poziția radiantului său reflexii pe traseul **dumneavoastră**. Conceptul aparține lui Ilkka **OH5IY** (MS-Soft) și este preluat în articolul Cerrotta–Sartori: maximul de eficiență nu coincide cu maximul vizual (ZHR), deoarece depinde de locul în care se află radiantul față de cele două stații. MCG_MS de DL5MCG aplică aceeași idee pe patru direcții fixe; YA-MS o calculează pentru **traseul real** dintre cei doi locatori.

Această filă o arată oră de oră pentru ziua aleasă în *Ziua pentru tabelul de 24 h (UTC)* (valori la jumătatea fiecărei ore).

## Carduri de sinteză

| Card | Conținut |
|---|---|
| **CEA MAI BUNĂ ORĂ A ZILEI** | Ora cu cel mai mare indice al traseului, indicele și latura predominantă (A/B cu procentul său) |
| **CEL MAI FAVORABIL ROI** | Roiul cu cel mai mare ZHR × eficiență al zilei, eficiența, ora și latura sa și **direcția optimă** (azimutul radiantului +90° / −90°) |
| **ACUM** | Indicele și latura predominantă la această oră și Hot-ul recomandat (doar când ziua aleasă este astăzi) |
| **PREVIZIUNE EXPERIMENTALĂ** | Reflexii așteptate pe oră acum, peste 1 h și peste 2 h la frecvența previziunii (Collm, regulile SM6FHZ; vedeți [Previziuni experimentale](Experimental-Forecasts-ro)) |

Sub carduri, o bandă explică literele A și B (vedeți mai jos).

## Grafic

*Eficiența orară pentru … din … (UTC, valori la jumătatea orei).* Pentru până la cinci roiuri: eficiența % ca linie continuă și formula DH9GCD ca linie punctată de aceeași culoare; **indicele traseului** ca bare albastre pe scala din dreapta.

## Tabelul orar

Un rând pentru fiecare roi activ în acea zi (ordonate după ZHR), 24 de coloane pentru ore (UTC):

| Celulă | Semnificație |
|---|---|
| `63A` | eficiență 63 %, cele mai multe reflexii din latura **A** |
| `41B` | eficiență 41 %, latura **B** |
| `3` | eficiență sub 5 %: număr fără litera laturii |
| goală | eficiență sub 1 % |
| `…↑` | radiantul este **peste 70°** de la stația dumneavoastră la acea oră (prea sus) |
| text galben | eficiență ≥ 50 % |

- **A** = **stânga** privind de la stația dumneavoastră spre stația DX (zona Hot A); **B** = **dreapta** (zona Hot B). Merită să rotiți antena cu **10–30° spre acea latură** (side-scatter, articolul Cerrotta–Sartori).
- **Rândurile albastru deschis** (*DH9GCD %*, sub fiecare roi): formula DH9GCD, pentru comparație.
- **Rândul Σ**: *Indicele traseului (ZHR×efic.)*.
- **Rândul portocaliu** (*Previziune … MHz (refl./oră)*): previziunea experimentală, pentru orele în care există (astăzi și o parte din mâine).

## Modelul

Toți pașii se află în [manualul de calcul](Efficiency-Explanation-ro) (`doc/YA-MS_manuale_calcoli.docx`, capitolul 5). Pe scurt:

**1. Reflexia speculară.** O urmă trimite semnalul de la A la B doar dacă este tangentă la un elipsoid cu A și B în focare (McKinley 1961). Urmele unui roi sunt paralele cu direcția radiantului ŝ (articolul; McKinley). Pentru fiecare punct P al stratului E, cu vectorii unitari spre stații:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Aceeași lege stă la baza QTFGUI de DJ5HG și a textului său *"Die Geometrie von Meteorscatterverbindungen"* (2004): urma împrăștie semnalul pe un con cu urma ca axă și doar un receptor aflat pe con o aude. Pentru o urmă ideală, peretele conului este foarte subțire (un radiator lung de mii de lungimi de undă); programul acceptă condiția cu o toleranță gaussiană σ = 0,05 rad (aproximativ 3°), care ține locul a ceea ce conul ideal nu vede: dispersia radianților roiului (0,3–1,4° măsurată de GMN), urmele îndoite de vânt și lungimea lor finită – *alegere a programului*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Ponderea fiecărui punct.** Puterea unei urme subdense (McKinley; ITU-R P.843, ec. 3), φ = jumătate din unghiul de împrăștiere (limitat la 85°, *alegere*), β = unghiul dintre urmă și planul de propagare A-P-B, p̂ = normala unitară la acel plan:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Opțiunea „Unghiul β dintre urmă și traseu (McKinley complet)”** (activată implicit, setare prudentă). Activată: urmele care traversează planul de propagare valorează cu 10–15 dB mai puțin decât cele care se află în el, astfel încât nicio urmă nu este supraestimată. Dezactivată: fiecare urmă este ponderată ca și cum s-ar afla în plan (β = 0, pondere cu cos²φ), ca până la versiunea 1.6. *Verificare:* pe un traseu de 1000 km, fără β cel mai bun azimut al radiantului este la 15°–90° de traseu în funcție de elevația radiantului (30° cu radiantul la 30°, perpendicular cu radiantul la 60°), iar radiantul perpendicular valorează 67 % la 30° elevație; cu β cel mai bun radiant este întotdeauna de-a lungul traseului, iar cel perpendicular scade la 15 %. Cu β se pierde regula direcției optime SM6FHZ / DH9GCD; β rămâne o opțiune, activată implicit pentru că dă valorile cele mai prudente, iar dezactivarea ei readuce regula.

Numărul de meteori care ajung într-un punct este proporțional cu sinusul elevației radiantului în acel punct (ŝ·û_P), aceeași corecție pe care IMO o folosește pentru ZHR.

**Opțiunea „Urme mai lungi cu radiant jos (DJ5HG)”** (casetă deasupra graficului, dezactivată implicit, cu tooltip): DJ5HG observă că, cu un radiant jos, cad mai puțini meteori pe km², dar urmele sunt mai lungi (până la 100 km utili) și respectă mai des legea reflexiei. Cu opțiunea activată, ponderea devine min(sin El, 15/100): grosimea utilă a stratului, 15 km, împărțită la sinusul elevației dă lungimea urmei, limitată la 100 km. Peste aproximativ 9° cele două efecte se anulează. Dezactivată, calculul rămâne prudent.

**Setările calculului** (același rând, butoane radio): **Prudent** (implicit, valorile cele mai prudente: înălțimea urmei de la radar, urme normale, β activat), **Ca DJ5HG** (102 km, urme mai lungi, β) și **Personalizat**, selectat automat când modificați manual înălțimea, caseta *de la radar*, opțiunea urmelor mai lungi sau β.

**3. Suma și procentul.** Puncte la fiecare 15 km la înălțimea urmei, doar acolo unde ambele stații le văd deasupra elevației lobului (*alegere*). 100 % este cea mai favorabilă poziție a radiantului pentru acel traseu:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F se calculează o singură dată pentru fiecare traseu pe o grilă de direcții (azimut la fiecare 5°, elevație la fiecare 2,5°) și se interpolează.

**Eficiența în dB (referința DJ5HG).** Procentul este relativ doar la cea mai bună poziție a radiantului pentru acel traseu. Pentru a compara trasee diferite, programul dă și eficiența în dB față de referința fixă a lui DJ5HG: 0 dB este maximul unui traseu nord–sud de 1000 km peste ecuator, cu radiantul pe ecuatorul ceresc la echinocțiu, calculat cu aceeași înălțime și aceleași ponderi. DJ5HG își dă valorile ca fiind mai bune de 6 dB.

**4. Latura și indicele.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Litera din tabel este latura cu fracția mai mare. *Alegeri ale programului (ec. 32–33 din manual).*

## Comparația cu DH9GCD

Sursele primare pentru direcția optimă sunt Eshleman & Mlodnosky și Meeks & James (Proc. IRE, 1957), Hines (1955) și verificarea sa experimentală de către Forsyth, Hines & Vogan (1955): sunt utili doar radianții de pe semicercul de cer perpendicular pe bisectoarea unghiului de împrăștiere, numărul de urme crește cu sin El, iar în apropierea punctului median urmele utile cad la aproximativ H·tan El lateral, pe partea opusă radiantului. DJ5HG adaugă o rezervă: cu un radiant **jos** exact de-a lungul traseului, formula lui McKinley dă semnale puternice (Hamburg–Narvik, Quadrantide, în jurul orei 19 UTC), deci „radiant aliniat cu traseul = aproape zero” este valabil doar pentru un radiant înalt; programul rămâne prudent și afișează avertismentul *RADIANT JOS DE-A LUNGUL TRASEULUI*.

O verificare independentă: formula direcției optime a lui **DH9GCD**, relatată de **DF5HC** (conferința DARC, ianuarie 2018) – nu are o sursă primară publicată –, cu El și Az elevația și azimutul radiantului văzute de la stația dumneavoastră și P azimutul stației DX:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Este maximă cu radiantul la 45° și perpendicular pe traseu. DF5HC consideră radiantul prea jos sub 20° și **prea sus peste 70°**: aceste ore primesc ↑ în tabel și un avertisment în [Bolta cerească](Sky-View-ro#avertismente). Formula ignoră distanța și înălțimile, dar este o bună referință.

## Verificări

| Verificare | Rezultat |
|---|---|
| Regula SM6FHZ (VUSHF 2025): cel mai bun traseu ortogonal pe azimutul radiantului, direcție = az. radiant ±90°, toleranță ±40–50° | Reprodusă de model; cu radiantul aliniat cu traseul și sus pe cer, eficiența este aproape zero |
| QTFGUI de DJ5HG, Hamburg JO53IM – Barcelona, Quadrantide, 4 ianuarie (exemplu din manualul său) | QTFGUI: 07:00 direcția 252°, −8 dB; 08:00 nicio zonă de reflexie; 09:00 direcția 168°, −4 dB. YA-MS (înălțime 102 km ca în QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Toate cele trei metode văd golul de la 08:00, cu radiantul aproape la zenit |
| Curbele DJ5HG (*Die Geometrie…*, Bild 8–9: din Hamburg și München, Quadrantide, 4 ianuarie; citite de pe grafic, aproximativ ±0,5 dB și ±15 min) comparate cu testul automat `--prova-dj5hg` (o valoare pe oră) | Momentele: golul cu radiantul aproape de zenit cade la aceleași ore (Barcelona 07:30–08:30 față de 07–09; Sofia 06:36–07:48 față de 07–08; Narvik 07–08:30 față de 07–09); Moscova este închisă 03–10 în ambele, deschisă din Hamburg până pe la 02:30 și din München până pe la 00:30, cum scrie DJ5HG. Direcții: la 2–10° distanță. Niveluri și formă la 102 km (diferența medie și RMS față de curbe): fără β, fără urme mai lungi −1,6 / 4,0 dB; urme mai lungi +1,1 / 4,6 dB; β −5,4 / 6,2 dB, dar cu cea mai bună formă (3,0 dB după eliminarea mediei, față de 3,6): apar minimele adânci cu radiant jos (Barcelona −15,6 dB la 17 față de −16 dB la 19:36; Sofia −18,5 dB la 20 față de −14 dB). β și urme mai lungi (*Ca DJ5HG*) −2,2 / 4,7 dB; setarea prudentă (înălțime radar 89,5 km, β activat, fără urme mai lungi) −6,9 / 7,6 dB, formă 3,3 dB. Fără β, YA-MS abia arată minimul cu radiantul jos și aproape aliniat cu traseul (−8,6 și −10,4 dB): aceasta este chiar rezerva lui DJ5HG, de aici avertismentul |
| Eșantionare la fiecare 5 km în loc de 15 km | procentele se schimbă cu mai puțin de 0,3 puncte |

> Documentația MS-Soft 5.2 definește eficiența lui OH5IY ca un indice relativ doar pentru urmele subdense, cu doi factori (elevația radiantului, optim aproximativ 45°, și unghiul față de traseu, optim 90°) și un minim ridicat manual la 20 % pentru urmele supradense; formula nu este publicată. MCG_MS o calculează pentru patru direcții fixe și, cu locatorul DX, pentru traseul real. Modelul ia în considerare doar urmele subdense, cu antene izotrope; exploziile supradense și fondul sporadic nu intră în eficiență (fondul sporadic este reprezentat de fluxul radar).
