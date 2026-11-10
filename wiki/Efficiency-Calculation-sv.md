[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · **Svenska** · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Effektivitetsberäkning

*Flik: Prognosberäkning › Effektivitetsberäkning.*

[![Effektivitetsberäkning](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

En svärms **effektivitet** anger i procent hur mycket radiantens läge tillåter reflexer på **din** sträcka. Begreppet kommer från Ilkka **OH5IY** (MS-Soft) och tas upp i artikeln av Cerrotta–Sartori: effektivitetens maximum sammanfaller inte med det visuella maximumet (ZHR), eftersom det beror på var radianten står i förhållande till de två stationerna. MCG_MS av DL5MCG tillämpar samma idé på fyra fasta riktningar; YA-MS beräknar den för den **verkliga sträckan** mellan de två lokatorerna.

Den här fliken visar den timme för timme för den dag som valts i *Dag för 24 h-tabellen (UTC)* (värden vid halvtimme).

## Översiktskort

| Kort | Innehåll |
|---|---|
| **DAGENS BÄSTA TID** | Timmen med högst sträckindex, indexet och den dominerande sidan (A/B med dess %) |
| **MEST GYNNSAM SVÄRM** | Den svärm som har störst ZHR × effektivitet under dagen, dess effektivitet, timme och sida, samt **bästa riktning** (radiantens azimut +90° / −90°) |
| **NU** | Index och dominerande sida vid den här timmen, och rekommenderad Hot (endast när den valda dagen är idag) |
| **EXPERIMENTELL PROGNOS** | Väntade reflexer/timme nu, om 1 h och om 2 h vid prognosfrekvensen (Collm, SM6FHZ:s regler; se [Experimentella prognoser](Experimental-Forecasts-sv)) |

Under korten förklarar ett band bokstäverna A och B (se nedan).

## Diagram

*Effektivitet per timme för … den … (UTC, värden vid halvtimme).* För upp till fem svärmar: effektivitet i % som heldragen linje och DH9GCD-formeln som prickad linje i samma färg; **sträckindex** som blå staplar mot den högra skalan.

## Timtabell

En rad per svärm som är aktiv den dagen (sorterade efter ZHR), 24 kolumner för timmarna (UTC):

| Cell | Betydelse |
|---|---|
| `63A` | effektivitet 63 %, flest reflexer från sida **A** |
| `41B` | effektivitet 41 %, sida **B** |
| `3` | effektivitet under 5 %: siffra utan sidbokstav |
| tom | effektivitet under 1 % |
| `…↑` | radianten står **över 70°** sett från din station vid den timmen (för högt) |
| gul text | effektivitet ≥ 50 % |

- **A** = **vänster** sett från din station mot motstationen (zonen Hot A); **B** = **höger** (zonen Hot B). Det lönar sig att vrida antennen **10–30° åt den sidan** (side-scatter, artikeln av Cerrotta–Sartori).
- **Ljusblå rader** (*DH9GCD %*, under varje svärm): DH9GCD-formeln, för jämförelse.
- **Σ-raden**: *Sträckindex (ZHR×eff.)*.
- **Orange rad** (*Prognos … MHz (refl./timme)*): den experimentella prognosen, för de timmar där den finns (idag och en del av morgondagen).

## Modellen

Alla steg finns i [beräkningshandboken](Efficiency-Explanation-sv) (`doc/YA-MS_manuale_calcoli.docx`, kapitel 5). I korthet:

**1. Spegelreflexion.** Ett spår skickar signalen från A till B endast om det tangerar en ellipsoid med A och B i brännpunkterna (McKinley 1961). En svärms spår är parallella med radiantens riktning ŝ (artikeln; McKinley). För varje punkt P i E-skiktet, med enhetsvektorer mot stationerna:

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     spegelvillkor: ŝ·n̂ = 0
```

Samma lag ligger till grund för QTFGUI av DJ5HG (cone scattering). Villkoret godtas med en gaussisk tolerans σ = 0,05 rad (omkring 3°) – *programmets val*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Varje punkts vikt.** Effekten från ett underdenst spår (McKinley), φ = halva spridningsvinkeln (begränsad till 85°, *val*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Antalet meteorer som når en punkt är proportionellt mot sinus för radiantens elevation där (ŝ·û_P), samma korrektion som IMO använder för ZHR.

**3. Summa och procent.** Punkter var 15:e km på spårhöjden, endast där båda stationerna ser dem ovanför lobelevationen (*val*). 100 % är det för sträckan mest gynnsamma radiantläget:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F beräknas en gång per sträcka på ett rutnät av riktningar (azimut var 5:e grad, elevation var 2,5:e grad) och interpoleras.

**4. Sida och index.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

Bokstaven i tabellen är den sida som har störst andel. *Programmets val (handboken ekv. 32–33).*

## Jämförelse med DH9GCD

En oberoende kontroll: formeln för bästa riktning av **DH9GCD**, återgiven av **DF5HC** (DARC-konferensen, januari 2018), där El och Az är radiantens elevation och azimut sett från din station och P motstationens azimut:

```
E = sin El · cos El · sin(P − Az)          visas som  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Den är störst när radianten står på 45° och tvärs mot sträckan. DF5HC anser att radianten står för lågt under 20° och **för högt över 70°**: dessa timmar får ↑ i tabellen och en varning i [Himlavalvet](Sky-View-sv#varningar). Formeln bortser från avstånd och höjder, men är en bra referens.

## Kontroller

| Kontroll | Resultat |
|---|---|
| SM6FHZ:s regel (VUSHF 2025): bästa sträcka ortogonal mot radiantens azimut, riktning = radiantens az ±90°, tolerans ±40–50° | Återges av modellen; med radianten i linje med sträckan och högt på himlen är effektiviteten nästan noll |
| QTFGUI av DJ5HG, Hamburg JO53IM – Barcelona, Quadrantiderna, 4 januari (exempel ur dess handbok) | QTFGUI: 07:00 riktning 252°, −8 dB; 08:00 ingen reflexionszon; 09:00 riktning 168°, −4 dB. YA-MS (höjd 102 km som i QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Alla tre metoderna ser hålet kl. 08:00, med radianten nästan i zenit |
| Sampling var 5:e km i stället för var 15:e km | procentsatserna ändras med mindre än 0,3 enheter |

> Den skala som OH5IY och MCG_MS använder är inte känd i detalj (handböckerna till MS-Soft finns inte tillgängliga): jämför procentsatserna med de programmen innan du behandlar dem som likvärdiga. Modellen tar bara hänsyn till underdensa spår, med isotropa antenner; overdensa skurar och den sporadiska bakgrunden ingår inte i effektiviteten (den sporadiska bakgrunden representeras av radarflödet).
