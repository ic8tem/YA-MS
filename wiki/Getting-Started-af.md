[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · **Afrikaans** · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh)

# Aan die gang

By die eerste opstart wys YA-MS 'n voorbeeldpad (JN70CN → JO62QM op 144 MHz). Vyf minute is genoeg om dit vir jou stasie op te stel.

## 1. Die drie rye kontroles

Bo die oortjies is daar drie rye kontroles, geldig vir al die oortjies. Die knoppie **Kontroles** regs bo vou hulle weg en weer oop (nuttig met groot lettertipes); die keuse word onthou.

**Ry 1 – stasies en band**

| Kontrole | Wat dit doen |
|---|---|
| **My lokator** / **hoogte m** | Jou Maidenhead-lokator (4, 6 of 8 karakters; die middel van die vierkant word gebruik) en die hoogte van die stasie bo seevlak. |
| **DX-stasie** / **hoogte m** | Lokator en hoogte van die stasie wat jy wil werk. |
| **Band MHz** | 28, 50, 70, 144, 222 of 432 MHz: gebruik vir die antennawins en -lob, die vloedskatting en die skakelbegroting. |
| **Bereken** | Bereken die pad oor (monsterneming van die E-laag: 'n paar sekondes). |
| **Antenna az** | Azimut van jou antenna: altyd **na die DX** (azimut van die pad). |
| **Lettertipe** | Grootte van al die teks, 100–300 %. Sien [Instellings](Settings-and-Data-Folder-af#lettertipe-en-kontroles). |

**Ry 2 – E-laag en antenna**

| Kontrole | Wat dit doen |
|---|---|
| **Spoorhoogte km** + **van radar** | Hoogte van die meteoorspore (verstek 90 km). Met *van radar* gemerk word die mees algemene hoogte (modus) gebruik wat deur die Collm-radar gemeet is; sien [Radarvloed](Radar-Flux-af). |
| **Lob-elevasie °** | Laagste elevasie van jou antennalob (0° = horison). Slegs punte van die E-laag wat albei stasies bo hierdie elevasie sien, word gebruik. |
| **Yagi-antenna: boom m** | Boomlengte van jou Yagi. Die program wys die lengte in λ, die wins (DL6WU-kurwe) en die −3 dB-lob, horisontaal en vertikaal; sien [Geometrie en padverlies](Geometry-and-Path-Loss-af#wins-en-lob-van-die-antenna). Onder 2 λ is die skatting rof. |
| **Hot spot vanaf middelpunt km** + **auto (AMS)** | Afstand van Hot A en Hot B vanaf die middelpunt. Met *auto (AMS)* gemerk (verstek) volg dit die antennaverskuiwingstabel van J. Richardson (AMS) wat DJ5HG aanhaal: 13° by 1000 km, 11° by 1250 km, 10° by 1500 en 2000 km (ongeveer 115, 121, 132 en 176 km vanaf die middelpunt). Ontmerk dit om 30–400 km met die hand in te voer (MSHV gebruik 150 km). |

**Ry 3 – tyd**

| Kontrole | Wat dit doen |
|---|---|
| **Tyd** | UTC-horlosie. |
| **Berekeningsdatum (UTC)** | Die dag van die berekening vir [Voorspellingsberekening](Sky-View-af) en [GRAVES-radar](GRAVES-Radar-af) (verstek vandag), op die huidige tyd van die dag. |
| **Ure (−12 tot +36 h)** | Skuif die oomblik van die berekening van 12 uur voor tot 36 uur na daardie tyd, in stappe van 15 minute. Langsaan: *Berekening vir: nou* of *Berekening vir: dd/mm hh:mm UTC*. |
| **Intyds** | Terug na nou. |
| **Dag vir die 24 h-tabel (UTC)** | Die dag wat in [Berekening van doeltreffendheid](Efficiency-Calculation-af) en in die GRAVES-tydlyn gewys word. |

## 2. Jou stasie en die DX

1. Tik **My lokator** en **hoogte m** in.
2. Tik die lokator en hoogte van die **DX-stasie** in – of klik op die kaart in die [hemelkoepel](Sky-View-af): **linksklik = lokator van die DX-stasie**, **regsklik = lokator van my stasie**.
3. Kies die **Band MHz** en druk **Bereken**.

Die statusbalk onderaan bevestig: *Pad bereken: … km, … refleksiepunte in … s gemonster*.

## 3. Jou antenna

Voer die **boomlengte** van jou Yagi in. Die program lei die wins en lob af en waarsku jou as Hot A of Hot B reeds **binne die lob** val wanneer die antenna na die DX wys (dan word hulle in grys geteken: dit is nie nodig om die antenna te draai nie).

## 4. Lees die resultate

| Vraag | Waar om te kyk |
|---|---|
| Watter swerm help my pad nou, en van watter kant? | [Hemelkoepel](Sky-View-af): swermlys, aanbevole Hot in rooi, PREV-sones |
| Wat is die beste uur vandag? | [Berekening van doeltreffendheid](Efficiency-Calculation-af): oorsigkaarte en uurtabel |
| Hoeveel meteore tel die radar? | [Radarvloed](Radar-Flux-af) |
| Hoeveel pings kan ek op 144 MHz verwag? | [Eksperimentele voorspellings](Experimental-Forecasts-af) (eksperimenteel) |
| Kan my stasie die pad oorbrug? | [Geometrie en padverlies](Geometry-and-Path-Loss-af): padverlies en marge |
| Wanneer is die volgende maksimum? | [Swerms](Showers-af) |
| Kan ek met GRAVES toets? | [GRAVES-radar](GRAVES-Radar-af) |

## Praktiese reëls (uit die bronne)

- **Rig loodreg op die swerm**: die beste pad is ortogonaal op die azimut van die radiant; beste rigting = radiant-azimut ±90°, toleransie ±40–50° (SM6FHZ).
- **Side-scatter**: draai die antenna 10–30° na die kant (A of B) waarvandaan die meeste refleksies kom (Cerrotta–Sartori-artikel).
- **Radiant te hoog** (bo 70°) of te laag (onder 20°) gee min bruikbare spore (DF5HC, DH9GCD).
- Sporadiese meteore piek omstreeks **06 UTC** (artikel; bevestig deur die Collm-vloed).
- Bruikbare afstande op 432 MHz: 800–2000 km, die beste omstreeks 1400 km (SM6FHZ); beste afstand in die algemeen 1300–1500 km (DF5HC).

Volgende: [Hemelkoepel](Sky-View-af).
