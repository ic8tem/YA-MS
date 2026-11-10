[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · **Afrikaans** · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh)

# GRAVES-radar

*Oortjie: Regstreeks en intydse data › GRAVES-radar.*

[![GRAVES-radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Wat GRAVES is

**GRAVES** is 'n Franse radar wat **CW op 143,050 MHz** uitsaai vanaf **Broye-lès-Pesmes** (47,348° N 5,515° O, lokator **JN27SI**, ongeveer 200 m bo seevlak; Wikipedia). Meteoorspore in die sone wat beide GRAVES en jy kan sien, reflekteer sy sein na jou deur **forward scatter**: jy hoor kort *pings* naby die draer. Dit is hoe die **RMOB**-waarnemers op 143,050 MHz meteore uur vir uur tel, en dit is 'n gratis toetssein wat altyd aan is vir jou 2 m-meteor scatter-stasie.

Die oortjie behandel **GRAVES → jy** as 'n meteor scatter-pad op sigself: met dieselfde funksies as die hoofpad (dieselfde spoorhoogte, lob-elevasie en hot spot-afstand) bereken dit swermdoeltreffendheid, aanbevole Hot en PREV-sones, en kontroleer dan of daardie sone **binne die GRAVES-bundel** is en **wanneer** die bundel dit belig.

## Boonste balk

| Kontrole | Wat dit doen |
|---|---|
| **Nou** | Bring die tyd van die hemelkoepel terug na intyds (die oortjie volg die skuifbalk *Tyd van die hemelkoepel*). |
| **Stel GRAVES as DX** | Die DX-stasie word GRAVES (JN27SI, hoogte 200 m) en die hoofpad word herbereken: al die ander oortjies wys dan die GRAVES-pad. |
| **Bundelvolgorde** | *0,8 s per stap · siklus 4,8 s (PE1ITR 2021)* (verstek) of *3,2 s per stap · siklus 19,2 s (PE1ITR 2007)*. |

## Die vier kaarte

| Kaart | Inhoud |
|---|---|
| **BRUIKBARE SONE IN DIE GRAVES-BUNDEL** | *Ja · sektor X* met die azimut en elevasie van die aanbevole hot spot soos vanaf GRAVES gesien en die stap (1–6); of *Nee: buite die sektore* / *Nee: onder die GRAVES-horison* / *Nee: bo die bundel (ongeveer 25°)* |
| **DOELTREFFENDHEID VAN DIE PAD GRAVES → JY NOU** | Padindeks Σ ZHR × doeltreffendheid, beste swerm, oorheersende kant A/B, en *verwagte eggo's ≈ …/uur* (eksperimenteel, sien hieronder) |
| **PAD** | Afstand na GRAVES; antenna na die aanbevole Hot (azimut en elevasie); direkte azimut na GRAVES |
| **VOLGENDE BUNDELDEURGANG OOR DIE SONE** | *nou · nog … s* of *oor … s*, die stap (bv. *B4*), die volgende drie tye (sekondes binne die minuut) en die fraksie spore wat opgevang word |

As geen swerm op daardie oomblik bruikbaar is nie, wys die program die hot spot **wat die beste by die bundel pas** (binne die sektore, die naaste aan suid) en sê so.

## Die hemel soos GRAVES dit sien

Volgens PE1ITR en die Bolidozor-wiki dek **vier fasegestuurde skikkings** die suidelike hemel van **90° tot 270°** azimut in vier **sektore van 45°**:

| Sektor | Azimut vanaf GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Elke sektor is verdeel in **6 stappe van 7,5°**, genommer 1 tot 6 vanaf die laagste azimut, wat een na die ander belig word, **op dieselfde oomblik in al vier sektore**. Die bundel is ongeveer **25° breed in elevasie**: op spoorhoogte dek dit die gekleurde ring tussen die twee stippelsirkels (*bundelhorison*). Op die tekening: oranje/pienk kolle = PREV-sones van die pad GRAVES → jy, groen lyn = rigting van jou stasie, rooi lyn = van jou stasie na die aanbevole hot spot; die stap wat nou belig word, word uitgelig.

## Chronologiese rekonstruksie

*CHRONOLOGIESE REKONSTRUKSIE · datum UTC* (dieselfde dag as die 24 h-tabel): vir elke uur die doeltreffendheid van die pad GRAVES → jy, die gunstigste swerm en die bruikbare venster (*hh:00 → hh:00 UTC · n h*), met die maksimum (*maks Σ … om hh:30*) en 'n rooi *nou*-merker. Daaronder die **besonderhede van die volgende sekondes**: die ses stappe van die sektor, die stap wat die bruikbare sone belig, en *moontlike eggo (+0,3 s spoor)*.

### Bundeltydsberekening

Die volgorde is aan **UTC** gekoppel (PE1ITR): die stap wat nou belig word, word bereken uit die sekondes sedert 00:00 UTC modulo die siklus (86 400 s is 'n veelvoud van sowel 4,8 s as 19,2 s). Die beheerstasie skuif die volgorde soms 'n paar stappe, so die besonderhede is 'n **voorspelling wat deur luister bevestig moet word**. Die geel pil **PC-horlosie gesinchroniseer** herinner jou daaraan: sinchroniseer jou rekenaar met 'n NTP-bediener (fout hoogstens 'n paar tiendes van 'n sekonde).

### Opsporingsfaktor

'n Spoor word slegs gehoor as die bundel dit belig terwyl dit duur:

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0,3 s is 'n tipiese duur van 'n onderdigte spoor op 143 MHz – 'n vaste waarde, *keuse van die program* (die λ²-reël van SM6FHZ skaal duurtes tussen bande maar gee geen beginwaarde nie).

### Verwagte eggo's (eksperimenteel)

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

Die voorspelling van [Eksperimentele voorspellings](Experimental-Forecasts-af) (wat reeds die stasiefaktor K bevat) word van sy frekwensie f_fc na 143,050 MHz geskaal met die SM6FHZ-reël (dieselfde eksponent k), gekorrigeer deur die verhouding van die swermindekse van die twee paaie (die konstante 10 stel die sporadiese agtergrond voor, soos in die voorspelling) en vermenigvuldig met die opsporingsfaktor. Slegs aanduidend: vergelyk met RMOB-waarnemers.

## Hoe om die GRAVES-pings te hoor

| Stap | Wat om te doen |
|---|---|
| Ontvanger | **USB op 143,049 MHz** (toon van ongeveer 1 kHz) of 143,050 MHz, **stadige of afgeskakelde AGC**, oudiobandwydte van **minstens 2,4 kHz** |
| Antenna | Na die **aanbevole hot spot** van die pad GRAVES → jy (kaart *PAD*), op **lae elevasie** |
| Waterval | Pings is **kort lyntjies naby die draer**; lang (oordigte) spore is wyer en toon Doppler |
| Telling | RMOB gebruik GRAVES vir uurlikse meteoortellings: **vergelyk jou pings met die waarnemers op 143,050 MHz** ([Eksperimentele voorspellings](Experimental-Forecasts-af#rmob-vergelyking)) |

## Bronne

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) en *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozor**-wiki, "Graves" – skikkings, sektore en bundeltydsberekening
3. **Wikipedia**, "GRAVES (system)" – sender by Broye-lès-Pesmes (47,348° N 5,515° O)
4. **RMOB** – waarnemers op 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** deur IC8TEM – oortjie Radar GRAVES (die ontwerpskets waaruit hierdie oortjie afgelei is)
