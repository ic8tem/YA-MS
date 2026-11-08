**English** · [Русский](Efficiency-Calculation-ru) · [Deutsch](Efficiency-Calculation-de) · [日本語](Efficiency-Calculation-ja)

# Berekening van doeltreffendheid

*Oortjie: Voorspellingsberekening › Berekening van doeltreffendheid.*

[![Berekening van doeltreffendheid](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

Die **doeltreffendheid** van 'n swerm sê, in persent, in watter mate die posisie van sy radiant refleksies op **jou** pad toelaat. Die konsep is van Ilkka **OH5IY** (MS-Soft) en word in die Cerrotta–Sartori-artikel oorgeneem: die doeltreffendheidsmaksimum val nie saam met die visuele maksimum (ZHR) nie, omdat dit afhang van waar die radiant relatief tot die twee stasies is. MCG_MS van DL5MCG pas dieselfde idee toe op vier vaste rigtings; YA-MS bereken dit vir die **werklike pad** tussen die twee lokators.

Hierdie oortjie wys dit uur vir uur vir die dag wat in *Dag vir die 24 h-tabel (UTC)* gekies is (waardes op die halfuur van elke uur).

## Oorsigkaarte

| Kaart | Inhoud |
|---|---|
| **BESTE TYD VAN DIE DAG** | Uur met die hoogste padindeks, die indeks en die oorheersende kant (A/B met sy %) |
| **GUNSTIGSTE SWERM** | Die swerm met die grootste ZHR × doeltreffendheid van die dag, sy doeltreffendheid, uur en kant, en die **beste rigting** (radiant-azimut +90° / −90°) |
| **NOU** | Indeks en oorheersende kant op hierdie uur, en die aanbevole Hot (slegs wanneer die gekose dag vandag is) |
| **EKSPERIMENTELE VOORSPELLING** | Verwagte refleksies/uur nou, oor 1 h en oor 2 h op die voorspellingsfrekwensie (Collm, SM6FHZ-reëls; sien [Eksperimentele voorspellings](Experimental-Forecasts-af)) |

Onder die kaarte verduidelik 'n strook die letters A en B (sien hieronder).

## Grafiek

*Uurlikse doeltreffendheid vir … op … (UTC, waardes op die halfuur).* Vir tot vyf swerms: doeltreffendheid in % as 'n soliede lyn en die DH9GCD-formule as 'n stippellyn in dieselfde kleur; die **padindeks** as blou stawe op die regterskaal.

## Uurtabel

Een ry per swerm wat op daardie dag aktief is (volgens ZHR gesorteer), 24 kolomme vir die ure (UTC):

| Sel | Betekenis |
|---|---|
| `63A` | doeltreffendheid 63 %, die meeste refleksies van kant **A** |
| `41B` | doeltreffendheid 41 %, kant **B** |
| `3` | doeltreffendheid onder 5 %: getal sonder kantletter |
| leeg | doeltreffendheid onder 1 % |
| `…↑` | die radiant is op daardie uur **hoër as 70°** vanaf jou stasie (te hoog) |
| geel teks | doeltreffendheid ≥ 50 % |

- **A** = **links** as jy van jou stasie na die DX-stasie kyk (Hot A-sone); **B** = **regs** (Hot B-sone). Dit is die moeite werd om die antenna **10–30° na daardie kant** te draai (side-scatter, Cerrotta–Sartori-artikel).
- **Ligblou rye** (*DH9GCD %*, onder elke swerm): die DH9GCD-formule, ter vergelyking.
- **Ry Σ**: *Padindeks (ZHR×doeltr.)*.
- **Oranje ry** (*Voorspelling … MHz (refl./uur)*): die eksperimentele voorspelling, vir die ure waarvoor dit bestaan (vandag en 'n deel van môre).

## Die model

Al die stappe is in die [berekeningshandleiding](Efficiency-Explanation-af) (`doc/YA-MS_manuale_calcoli.docx`, hoofstuk 5). Kortliks:

**1. Spekulêre refleksie.** 'n Spoor stuur die sein slegs van A na B as dit raak aan 'n ellipsoïde met A en B in die brandpunte (McKinley 1961). Die spore van 'n swerm is parallel aan die radiantrigting ŝ (artikel; McKinley). Vir elke punt P van die E-laag, met eenheidsvektore na die stasies:

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

Dieselfde wet lê ten grondslag van QTFGUI deur DJ5HG (keëlverstrooiing). Die voorwaarde word aanvaar met 'n Gaussiese toleransie σ = 0,05 rad (ongeveer 3°) – *keuse van die program*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Gewig van elke punt.** Drywing van 'n onderdigte spoor (McKinley), φ = die helfte van die verstrooiingshoek (beperk tot 85°, *keuse*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Die aantal meteore wat 'n punt bereik, is eweredig aan die sinus van die radiant se elevasie daar (ŝ·û_P), dieselfde korreksie wat die IMO vir die ZHR gebruik.

**3. Som en persentasie.** Punte elke 15 km op spoorhoogte, slegs waar albei stasies hulle bo die lob-elevasie sien (*keuse*). 100 % is die gunstigste radiantposisie vir daardie pad:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F word een keer per pad bereken op 'n rooster van rigtings (azimut elke 5°, elevasie elke 2,5°) en geïnterpoleer.

**4. Kant en indeks.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

Die letter in die tabel is die kant met die groter fraksie. *Keuses van die program (handleiding vgl. 32–33).*

## DH9GCD-vergelyking

'n Onafhanklike kontrole: die formule vir die beste rigting deur **DH9GCD**, gerapporteer deur **DF5HC** (DARC-konferensie, Januarie 2018), met El en Az die elevasie en azimut van die radiant soos vanaf jou stasie gesien en P die azimut van die DX-stasie:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Dit is maksimaal met die radiant op 45° en dwars op die pad. DF5HC beskou die radiant as te laag onder 20° en **te hoog bo 70°**: hierdie ure kry ↑ in die tabel en 'n waarskuwing op die [hemelkoepel](Sky-View-af#waarskuwings). Die formule ignoreer afstand en hoogtes, maar dit is 'n goeie verwysing.

## Kontroles

| Kontrole | Resultaat |
|---|---|
| SM6FHZ-reël (VUSHF 2025): beste pad ortogonaal op die radiant-azimut, rigting = radiant-az ±90°, toleransie ±40–50° | Deur die model weergegee; met die radiant in lyn met die pad en hoog in die lug is die doeltreffendheid byna nul |
| QTFGUI deur DJ5HG, Hamburg JO53IM – Barcelona, Kwadrantiede, 4 Januarie (voorbeeld uit sy handleiding) | QTFGUI: 07:00 rigting 252°, −8 dB; 08:00 geen refleksiesone nie; 09:00 rigting 168°, −4 dB. YA-MS (hoogte 102 km soos QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Al drie metodes sien die gat om 08:00, met die radiant byna in die senit |
| Monsterneming elke 5 km in plaas van 15 km | die persentasies verander met minder as 0,3 punte |

> Die skaal wat OH5IY en MCG_MS gebruik, is nie in besonderhede bekend nie (die MS-Soft-handleidings is nie beskikbaar nie): vergelyk die persentasies met daardie programme voordat jy hulle as gelykwaardig beskou. Die model hou slegs rekening met onderdigte spore, met isotropiese antennas; oordigte uitbarstings en die sporadiese agtergrond is nie in die doeltreffendheid nie (die sporadiese agtergrond word deur die radarvloed voorgestel).
