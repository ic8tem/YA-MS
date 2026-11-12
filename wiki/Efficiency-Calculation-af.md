[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · **Afrikaans** · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Berekening van doeltreffendheid

*Oortjie: Voorspellingsberekening › Berekening van doeltreffendheid.*

[![Berekening van doeltreffendheid](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

Die **doeltreffendheid** van 'n swerm sê, in persent, in watter mate die posisie van sy radiant refleksies op **jou** pad toelaat. Die konsep is van Ilkka **OH5IY** (MS-Soft) en word in die Cerrotta–Sartori-artikel oorgeneem: die doeltreffendheidsmaksimum val nie saam met die visuele maksimum (ZHR) nie, omdat dit afhang van waar die radiant relatief tot die twee stasies is. MCG_MS van DL5MCG pas dieselfde idee toe op vier vaste rigtings; YA-MS bereken dit vir die **werklike pad** tussen die twee lokators.

Hierdie oortjie wys dit uur vir uur vir die dag wat in *Berekeningsdatum (UTC)* gekies is (waardes op die halfuur van elke uur).

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

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Dieselfde wet lê ten grondslag van QTFGUI deur DJ5HG en sy teks *"Die Geometrie von Meteorscatterverbindungen"* (2004): die spoor verstrooi op 'n keël met die spoor as as, en slegs 'n ontvanger op die keël hoor dit. Vir 'n ideale spoor is die keëlwand baie dun ('n straler duisende golflengtes lank); die program aanvaar die voorwaarde met 'n Gaussiese toleransie σ = 0,05 rad (ongeveer 3°), wat staan vir wat die ideale keël nie sien nie: die verspreiding van swermradiante (0,3–1,4° deur GMN gemeet), spore wat deur die wind gebuig is en hul eindige lengte – *keuse van die program*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Gewig van elke punt.** Drywing van 'n onderdigte spoor (McKinley; ITU-R P.843, vgl. 3), φ = die helfte van die verstrooiingshoek (beperk tot 85°, *keuse*), β = hoek tussen die spoor en die voortplantingsvlak A-P-B, p̂ = eenheidsnormaal op daardie vlak:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Opsie "β-hoek tussen spoor en pad (volledige McKinley)"** (by verstek aan, versigtige instelling). Aan: spore wat die voortplantingsvlak kruis, is 10–15 dB minder werd as dié wat daarin lê, sodat geen spoor oorskat word nie. Af: elke spoor word geweeg asof dit in die vlak lê (β = 0, gewig met cos²φ), soos tot weergawe 1.6. *Kontrole:* op 'n pad van 1000 km is die beste radiant-azimut sonder β 15°–90° van die pad, afhangend van die radiant se elevasie (30° met die radiant op 30°, dwars op die pad met die radiant op 60°), en die dwars radiant is 67 % werd by 30° elevasie; met β is die beste radiant altyd langs die pad en die dwarse een daal tot 15 %. Met β gaan die SM6FHZ / DH9GCD-reël vir die beste rigting verlore; β bly 'n opsie, by verstek aan omdat dit die versigtigste waardes gee, en as dit afgeskakel word, keer die reël terug.

Die aantal meteore wat 'n punt bereik, is eweredig aan die sinus van die radiant se elevasie daar (ŝ·û_P), dieselfde korreksie wat die IMO vir die ZHR gebruik.

**Opsie "Langer spore met 'n lae radiant (DJ5HG)"** (merkblokkie bo die grafiek, by verstek af, met wenk): DJ5HG merk op dat met 'n lae radiant minder meteore per km² val, maar die spore langer is (tot 100 km bruikbaar) en meer dikwels aan die refleksiewet voldoen. Met die opsie aan word die gewig min(sin El, 15/100): die bruikbare laagdikte, 15 km, gedeel deur die sinus van die elevasie gee die spoorlengte, beperk tot 100 km. Bo ongeveer 9° kanselleer die twee effekte mekaar. Af bly die berekening versigtig.

**Berekeningsinstelling** (dieselfde ry, keuseknoppies): **Versigtig** (verstek, die versigtigste waardes: spoorhoogte van die radar, normale spore, β aan), **Soos DJ5HG** (102 km, langer spore, β) en **Pasgemaak**, wat outomaties gekies word wanneer jy die hoogte, die *van radar*-blokkie, die opsie vir langer spore of β met die hand verander.

**3. Som en persentasie.** Punte elke 15 km op spoorhoogte, slegs waar albei stasies hulle bo die lob-elevasie sien (*keuse*). 100 % is die gunstigste radiantposisie vir daardie pad:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F word een keer per pad bereken op 'n rooster van rigtings (azimut elke 5°, elevasie elke 2,5°) en geïnterpoleer.

**Doeltreffendheid in dB (DJ5HG-verwysing).** Die persentasie is slegs relatief tot die beste radiantposisie vir daardie pad. Om verskillende paaie te vergelyk, gee die program ook die doeltreffendheid in dB relatief tot die vaste verwysing van DJ5HG: 0 dB is die maksimum van 'n 1000 km noord–suid-pad oor die ewenaar met die radiant op die hemelewenaar by die equinoks, bereken met dieselfde hoogte en gewigte. DJ5HG gee sy waardes as beter as 6 dB.

**4. Kant en indeks.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Die letter in die tabel is die kant met die groter fraksie. *Keuses van die program (handleiding vgl. 32–33).*

## DH9GCD-vergelyking

Die primêre bronne vir die beste rigting is Eshleman & Mlodnosky en Meeks & James (Proc. IRE, 1957), Hines (1955) en die eksperimentele kontrole daarvan deur Forsyth, Hines & Vogan (1955): slegs radiante op die halwe sirkel van die hemel loodreg op die halveerlyn van die verstrooiingshoek is bruikbaar, die aantal spore groei met sin El, en naby die middelpunt val die bruikbare spore ongeveer H·tan El opsy, aan die kant teenoor die radiant. DJ5HG voeg 'n voorbehoud by: met 'n **lae** radiant reg langs die pad gee McKinley se formule sterk seine (Hamburg–Narvik, Quadrantide, omstreeks 19 UTC), dus geld "radiant in lyn met die pad = byna nul" net vir 'n hoë radiant; die program bly versigtig en wys die waarskuwing *LAE RADIANT LANGS DIE PAD*.

'n Onafhanklike kontrole: die formule vir die beste rigting deur **DH9GCD**, gerapporteer deur **DF5HC** (DARC-konferensie, Januarie 2018) – dit het geen gepubliseerde primêre bron nie – met El en Az die elevasie en azimut van die radiant soos vanaf jou stasie gesien en P die azimut van die DX-stasie:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Dit is maksimaal met die radiant op 45° en dwars op die pad. DF5HC beskou die radiant as te laag onder 20° en **te hoog bo 70°**: hierdie ure kry ↑ in die tabel en 'n waarskuwing op die [hemelkoepel](Sky-View-af#waarskuwings). Die formule ignoreer afstand en hoogtes, maar dit is 'n goeie verwysing.

## Kontroles

| Kontrole | Resultaat |
|---|---|
| SM6FHZ-reël (VUSHF 2025): beste pad ortogonaal op die radiant-azimut, rigting = radiant-az ±90°, toleransie ±40–50° | Deur die model weergegee; met die radiant in lyn met die pad en hoog in die lug is die doeltreffendheid byna nul |
| QTFGUI deur DJ5HG, Hamburg JO53IM – Barcelona, Kwadrantiede, 4 Januarie (voorbeeld uit sy handleiding) | QTFGUI: 07:00 rigting 252°, −8 dB; 08:00 geen refleksiesone nie; 09:00 rigting 168°, −4 dB. YA-MS (hoogte 102 km soos QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Al drie metodes sien die gat om 08:00, met die radiant byna in die senit |
| Krommes van DJ5HG (*Die Geometrie…*, Bild 8–9: vanaf Hamburg en München, Quadrantide, 4 Januarie; van die grafiek afgelees, ongeveer ±0,5 dB en ±15 min) teenoor die outomatiese toets `--prova-dj5hg` (een waarde per uur) | Tye: die gat met die radiant naby die senit val op dieselfde ure (Barcelona 07:30–08:30 teenoor 07–09; Sofia 06:36–07:48 teenoor 07–08; Narvik 07–08:30 teenoor 07–09); Moskou is in albei 03–10 gesluit, oop vanaf Hamburg tot omstreeks 02:30 en vanaf München tot omstreeks 00:30, soos DJ5HG skryf. Rigtings: 2–10° verskil. Vlakke en vorm by 102 km (gemiddelde en RMS-verskil van die krommes): geen β, geen langer spore −1,6 / 4,0 dB; langer spore +1,1 / 4,6 dB; β −5,4 / 6,2 dB maar met die beste vorm (3,0 dB ná verwydering van die gemiddelde, teenoor 3,6): die diep minima met 'n lae radiant verskyn (Barcelona −15,6 dB om 17 teenoor −16 dB om 19:36; Sofia −18,5 dB om 20 teenoor −14 dB). β en langer spore (*Soos DJ5HG*) −2,2 / 4,7 dB; die versigtige instelling (radarhoogte 89,5 km, β aan, geen langer spore) −6,9 / 7,6 dB, vorm 3,3 dB. Sonder β toon YA-MS skaars die minimum met die radiant laag en byna in lyn met die pad (−8,6 en −10,4 dB): dit is DJ5HG se eie voorbehoud, vandaar die waarskuwing |
| Monsterneming elke 5 km in plaas van 15 km | die persentasies verander met minder as 0,3 punte |

> Die MS-Soft 5.2-dokumentasie definieer OH5IY se doeltreffendheid as 'n relatiewe indeks slegs vir onderdigte spore, met twee faktore (radiantelevasie, beste omstreeks 45°, en hoek met die pad, beste 90°) en 'n minimum wat met die hand tot 20 % verhoog is vir oordigte spore; die formule is nie gepubliseer nie. MCG_MS bereken dit vir vier vaste rigtings en, met die DX-lokaliseerder, vir die werklike pad. Die model hou slegs rekening met onderdigte spore, met isotropiese antennas; oordigte uitbarstings en die sporadiese agtergrond is nie in die doeltreffendheid nie (die sporadiese agtergrond word deur die radarvloed voorgestel).
