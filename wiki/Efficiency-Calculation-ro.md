[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · **Română** · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Calculul eficienței

*Fila: Calcul previzional › Calculul eficienței.*

[![Calculul eficienței](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

**Eficiența** unui roi spune, în procente, cât permite poziția radiantului său reflexii pe traseul **tău**. Conceptul îi aparține lui Ilkka **OH5IY** (MS-Soft) și este preluat în articolul Cerrotta–Sartori: maximul eficienței nu coincide cu maximul vizual (ZHR), deoarece depinde de locul în care se află radiantul față de cele două stații. MCG_MS de DL5MCG aplică aceeași idee la patru direcții fixe; YA-MS o calculează pentru **traseul real** dintre cei doi locatori.

Această filă o arată oră de oră pentru ziua aleasă în *Ziua pentru tabelul 24 h (UTC)* (valori la jumătatea fiecărei ore).

## Casete de sinteză

| Casetă | Conținut |
|---|---|
| **CEA MAI BUNĂ ORĂ A ZILEI** | Ora cu cel mai mare indice al traseului, indicele și latura predominantă (A/B cu procentul ei) |
| **ROIUL CEL MAI FAVORABIL** | Roiul cu cel mai mare ZHR × eficiență al zilei, eficiența, ora și latura lui, precum și **orientarea optimă** (azimutul radiantului +90° / −90°) |
| **ACUM** | Indicele și latura predominantă la această oră, plus Hot-ul recomandat (doar când ziua aleasă este azi) |
| **PROGNOZĂ EXPERIMENTALĂ** | Reflexiile/oră așteptate acum, peste 1 h și peste 2 h la frecvența prognozei (Collm, reguli SM6FHZ; vezi [Implementare experimentală a prognozelor](Experimental-Forecasts-ro)) |

Sub casete, o bandă explică literele A și B (vezi mai jos).

## Grafic

*Eficiența orară pentru … din … (UTC, valori la jumătatea orei).* Pentru cel mult cinci roiuri: eficiența % ca linie continuă și formula DH9GCD ca linie punctată de aceeași culoare; **indicele traseului** ca bare albastre pe scara din dreapta.

## Tabelul orar

Un rând pentru fiecare roi activ în acea zi (ordonate după ZHR), 24 de coloane pentru ore (UTC):

| Celulă | Semnificație |
|---|---|
| `63A` | eficiență 63 %, cele mai multe reflexii din latura **A** |
| `41B` | eficiență 41 %, latura **B** |
| `3` | eficiență sub 5 %: număr fără litera laturii |
| goală | eficiență sub 1 % |
| `…↑` | radiantul este la **peste 70°** deasupra orizontului stației tale la acea oră (prea sus) |
| text galben | eficiență ≥ 50 % |

- **A** = **stânga** privind de la stația ta spre corespondent (zona Hot A); **B** = **dreapta** (zona Hot B). Merită să rotești antena **cu 10–30° spre acea latură** (side-scatter, articolul Cerrotta–Sartori).
- **Rândurile bleu** (*DH9GCD %*, sub fiecare roi): formula DH9GCD, pentru comparație.
- **Rândul Σ**: *Indice traseu (ZHR×efic.)*.
- **Rândul portocaliu** (*Prognoză … MHz (refl./oră)*): prognoza experimentală, pentru orele în care există (azi și o parte din mâine).

## Modelul

Toți pașii se află în [manualul de calcul](Efficiency-Explanation-ro) (`doc/YA-MS_manuale_calcoli.docx`, capitolul 5). Pe scurt:

**1. Reflexie speculară.** O urmă trimite semnalul de la A la B doar dacă este tangentă la un elipsoid cu A și B în focare (McKinley 1961). Urmele unui roi sunt paralele cu direcția radiantului ŝ (articol; McKinley). Pentru fiecare punct P al stratului E, cu vectorii unitari spre stații:

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

Aceeași lege stă la baza QTFGUI de DJ5HG (cone scattering). Condiția este acceptată cu o toleranță gaussiană σ = 0,05 rad (circa 3°) – *alegere a programului*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Ponderea fiecărui punct.** Puterea unei urme subdense (McKinley), φ = jumătate din unghiul de împrăștiere (limitat la 85°, *alegere*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Numărul de meteori care ajung într-un punct este proporțional cu sinusul elevației radiantului în acel loc (ŝ·û_P), aceeași corecție pe care IMO o folosește pentru ZHR.

**3. Suma și procentul.** Puncte la fiecare 15 km la altitudinea urmelor, doar acolo unde ambele stații le văd deasupra elevației lobului (*alegere*). 100 % este poziția cea mai favorabilă a radiantului pentru acel traseu:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F se calculează o singură dată pe traseu, pe o grilă de direcții (azimut la fiecare 5°, elevație la fiecare 2,5°), și se interpolează.

**4. Latura și indicele.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

Litera din tabel este latura cu fracțiunea mai mare. *Alegeri ale programului (manual, ec. 32–33).*

## Comparația DH9GCD

O verificare independentă: formula celei mai bune direcții a lui **DH9GCD**, citată de **DF5HC** (conferința DARC, ianuarie 2018), cu El și Az elevația și azimutul radiantului văzute de la stația ta și P azimutul corespondentului:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Este maximă cu radiantul la 45° și lateral față de traseu. DF5HC consideră radiantul prea jos sub 20° și **prea sus peste 70°**: aceste ore primesc ↑ în tabel și un avertisment în [Bolta cerească](Sky-View-ro#avertismente). Formula ignoră distanța și altitudinile, dar este o referință bună.

## Verificări

| Verificare | Rezultat |
|---|---|
| Regula SM6FHZ (VUSHF 2025): cel mai bun traseu este ortogonal pe azimutul radiantului, orientare = az. radiant ±90°, toleranță ±40–50° | Reprodusă de model; cu radiantul aliniat cu traseul și sus pe cer, eficiența este aproape nulă |
| QTFGUI de DJ5HG, Hamburg JO53IM – Barcelona, Quadrantide, 4 ianuarie (exemplul din manualul său) | QTFGUI: 07:00 orientare 252°, −8 dB; 08:00 nicio zonă de reflexie; 09:00 orientare 168°, −4 dB. YA-MS (altitudine 102 km ca în QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Toate cele trei metode văd golul de la 08:00, cu radiantul aproape la zenit |
| Eșantionare la fiecare 5 km în loc de 15 km | procentele se schimbă cu mai puțin de 0,3 puncte |

> Scara folosită de OH5IY și de MCG_MS nu este cunoscută în detaliu (manualele MS-Soft nu sunt disponibile): compară procentele cu cele ale acestor programe înainte de a le considera echivalente. Modelul ia în considerare doar urmele subdense, cu antene izotrope; exploziile overdense și fondul sporadic nu intră în eficiență (fondul sporadic este reprezentat de fluxul radar).
