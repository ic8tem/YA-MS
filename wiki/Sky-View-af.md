[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · **Afrikaans** · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh)

# Hemelkoepel

*Oortjie: Voorspellingsberekening › Voorspellingsberekening.*

[![Hemelkoepel](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Hierdie sub-oortjie (die hemelkoepel van vroeër weergawes) wys op een skerm **waar** die bruikbare spore nou is en **waarheen om te rig**. Links die **bo-aansig** van die pad; regs die swermlys, 'n klein hemelkoepel met die radiante, die teks van die berekening en die **deursnee** soos vanaf jou antenna gesien. Alles verwys na die oomblik wat met *Berekeningsdatum (UTC)* en die skuifbalk *Ure (−12 tot +36 h)* gekies is (verstek intyds, in stappe van 15 minute).

'n **Strook bo die bo-aansig** som die berekening vir daardie oomblik op: datum en tyd (*nou* of ure van nou af), die **padindeks Σ ZHR×η**, die **nuttigste swerm** met sy ZHR en doeltreffendheid, die aantal swerms bo die horison en die **aanbevole Hot** met sy azimut.

In die klein hemelkoepel gee 'n **oranje lyn** deur die senit altyd die **regte antennarigtings**, ortogonaal op die drywing van die gekose swerm (of van die gunstigste een): radiant-azimut ±90°, met die etiket *antenna NNN°* aan albei kante, en die toleransie van ±45° as dun lyne. Kort oranje merkies op die rand gee die ortogonale rigtings van die ander bruikbare swerms.

## Bo-aansig (links)

'n Kaart van Europa van bo gesien (**O regs**) met 'n gradeskaal rondom. Die onderskrif onder die kaart gee die radius daarvan (*Kaart: rand = … km vanaf die stasie*).

| Element | Tekening |
|---|---|
| Pad / DX | Groen lyn van jou stasie na die DX-stasie (altyd die werklike grootsirkelpad tussen die lokators) |
| **Hot A / Hot B** | Punte 150 km (verstelbaar) aan weerskante van die middelpunt, loodreg op die pad. **Rooi = aanbevole**, **pienk = buite die antennalob**, **grys = binne die lob** (met 'n waarskuwing) |
| Antennalob | Die horisontale −3 dB-lob rondom die antenna-azimut (antenna altyd na die DX gerig), met die etiket *lob …°* |
| Grense van die gemeenskaplike sone | Dowwe punte *gr. A* / *gr. B* en die twee sirkels waar elke stasie se horison die E-laag ontmoet (sien [Geometrie](Geometry-and-Path-Loss-af#grense-van-die-gemeenskaplike-sone)) |
| Swermdrywing | **Geel lyn**: rigting waarin die gekose swerm (of die gunstigste een) die hemel deurkruis, d.w.s. die radiant-azimut |
| Beste rigtings | **Oranje kolle**: die twee rigtings loodreg op die drywing (radiant-azimut ±90°, SM6FHZ) |
| **PREV-sones** | Ligte ellipse: waar die mees waarskynlike spore **nou** val, een aan elke kant van die pad |

Etikette oorvleuel nie: Hot A en PREV A word links van die pad geskryf, B regs. Die **Sleutel** is 'n opvoubare kolom regs van die kaart.

**Muis op die kaart:** **linksklik = lokator van die DX-stasie**, **regsklik = lokator van my stasie**. Die pad word dadelik herbereken.

Opsies bo die swermlys: **Hot A / Hot B-rigtings**, **Kaart van Europa** (Natural Earth, by die eerste opstart in `data/mappa` afgelaai), **Bo-aansig (O regs)**.

### Aanbevole Hot

Vir die getoonde tyd tel die program oor al die swerms bo die horison die gewig ZHR × doeltreffendheid op, verdeel tussen kant A (fraksie f_A) en kant B. Die kant met die groter gewig gee die aanbevole Hot, in rooi geteken:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Keuse van die program (handleiding vgl. 23).* Oorsprong van die idee: DJ5HG, gerapporteer deur DF5HC (DARC-konferensie 2018) – afhangend van die radiantposisie is een van die twee punte, HOT-A of HOT-B, gunstiger. Om 10–30° na daardie kant te draai (side-scatter) kom uit die Cerrotta–Sartori-artikel.

### PREV-sones

Vir elke punt P van die E-laag word die bydraes van al die aktiewe swerms tot die doeltreffendheid (dieselfde spekulêre voorwaarde as vir die [doeltreffendheid](Efficiency-Calculation-af#die-model)) opgetel, met ZHR geweeg. Punte met minstens 3 % van die maksimum vorm die PREV-sones; elkeen word geteken as 'n ellips met middelpunt = geweegde gemiddelde van die punte en asse = twee keer hul verspreiding.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Keuse van die program (handleiding vgl. 34).* Dit is die praktiese reël: as die swerm van noord na suid beweeg, val die bruikbare spore oos en wes.

## Swermlys (regs bo)

| Kolom | Betekenis |
|---|---|
| Swerm, Kode | Naam en IMO-kode |
| ZHR nou | Aktiwiteit op hierdie oomblik (IMO-ZHR by die maksimum met die aktiwiteitsprofiel) |
| Azimut, Elev. | Radiantposisie soos vanaf jou stasie gesien |
| Doeltr. % | Doeltreffendheid van die swerm vir hierdie pad |
| Kant | A of B, die kant waarvandaan die meeste refleksies kom |
| Beste rigting | Radiant-azimut ±90° |
| Opkoms, Ondergang | Opkoms en ondergang van die radiant (UTC); *sirkumpolêr* of *altyd onder* waar van toepassing |

Klik op 'n ry om die swerm te kies: die geel drywingslyn en die oranje kolle volg dit.

## Klein hemelkoepel (regs in die middel)

Die radiante op 'n hemelkoepel soos vanaf jou stasie gesien, met hul **IMO-kode** en **daaglikse baan in siaan** (UTC-ure). **Klik op 'n radiant** om dit te kies. Kleure:

| Kleur | Betekenis |
|---|---|
| Geel | doeltreffendheid ≥ 50 % en ZHR ≥ 2 |
| Oranje | doeltreffendheid ≥ 20 % |
| Donkerrooi | doeltreffendheid < 20 % |
| Grys | byna onaktief |

Daarnaas die teks van die berekening: padlengte en -azimut, middelpunt en sy elevasie, azimute en verskuiwings van Hot A / Hot B, die aanbevole Hot (*… nou aanbeveel: az. …° (…% van die verwagte refleksies)*), die grense van die gemeenskaplike sone, en die herinnering: *beste rigting vir die swerm: LOODREG op die rigting van aankoms (radiant-azimut ±90°, toleransie ±40–50°, SM6FHZ)*.

## Deursnee (regs onder)

*DEURSNEE – die mees waarskynlike spore gesien vanaf die antenna na die DX-stasie.* Horisontaal die **azimut relatief tot die DX-stasie** (← A links, B → regs), vertikaal die **elevasie**. Vir elke swerm word die 14 sterkste refleksiepunte geneem; elke spoor is 'n segment wat na die radiant gerig is, van 10 km bo tot 10 km onder die spoorhoogte (hoogstens 60 km per kant), dikker hoe waarskynliker. Ook geteken: die antennalob (−3 dB-sirkel rondom die lob-elevasie), die DX-stasie en Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Keuse van die program (handleiding vgl. 35).*

## Waarskuwings

| Waarskuwing | Wanneer |
|---|---|
| **WAARSKUWING: Hot A (en/of Hot B) val binne die antennalob …** | Die hot spot is binne ±θ/2 van die antenna-azimut (θ = horisontale −3 dB-lob): met hierdie rigting is dit reeds gedek. In grys op die kaart gewys. Die aanbevole Hot bly rooi. |
| **RADIANT TE HOOG (bo 70°)** | 'n Bruikbare radiant is hoër as 70° vanaf jou stasie: die spore val byna vertikaal en reflekteer min na die pad (DF5HC, DH9GCD). Dieselfde ure word in die [uurtabel](Efficiency-Calculation-af#uurtabel) met ↑ gemerk. |
| *Geen gemeenskaplike E-laagsone nie* | Die pad is langer as twee keer die bereik op spoorhoogte: die twee stasies sien geen gemeenskaplike deel van die E-laag nie (enkele sprong onmoontlik). |
| *Geen aanbevole Hot nie* | Byna geen aktiewe swerm op hierdie tyd nie. |

Verwysing vir die grafika van die hemelkoepel: Swan Meteor Skyview deur DL1DBC (swan.ms); poolgrafiek met die beste rigting: RadiantCalc deur SM6FHZ.
