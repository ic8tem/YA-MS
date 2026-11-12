[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · **Svenska** · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Effektivitetsberäkning

*Flik: Prognosberäkning › Effektivitetsberäkning.*

[![Effektivitetsberäkning](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

En svärms **effektivitet** anger i procent hur mycket radiantens läge tillåter reflexer på **din** sträcka. Begreppet kommer från Ilkka **OH5IY** (MS-Soft) och tas upp i artikeln av Cerrotta–Sartori: effektivitetens maximum sammanfaller inte med det visuella maximumet (ZHR), eftersom det beror på var radianten står i förhållande till de två stationerna. MCG_MS av DL5MCG tillämpar samma idé på fyra fasta riktningar; YA-MS beräknar den för den **verkliga sträckan** mellan de två lokatorerna.

Den här fliken visar den timme för timme för den dag som valts i *Beräkningsdatum (UTC)* (värden vid halvtimme).

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

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Samma lag ligger till grund för QTFGUI av DJ5HG och hans text *"Die Geometrie von Meteorscatterverbindungen"* (2004): spåret sprider på en kon med spåret som axel, och bara en mottagare på konen hör det. För ett idealt spår är konens vägg mycket tunn (en strålare tusentals våglängder lång); programmet godtar villkoret med en gaussisk tolerans σ = 0,05 rad (omkring 3°), som står för det som den ideala konen inte ser: spridningen hos svärmarnas radianter (0,3–1,4° uppmätt av GMN), spår som böjts av vinden och deras ändliga längd – *programmets val*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Varje punkts vikt.** Effekten från ett underdenst spår (McKinley; ITU-R P.843, ekv. 3), φ = halva spridningsvinkeln (begränsad till 85°, *val*), β = vinkeln mellan spåret och utbredningsplanet A-P-B, p̂ = enhetsnormalen till det planet:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Alternativet "β-vinkel mellan spår och sträcka (fullständig McKinley)"** (på som standard, försiktig inställning). På: spår som korsar utbredningsplanet är värda 10–15 dB mindre än de som ligger i det, så att inget spår överskattas. Av: varje spår viktas som om det låg i planet (β = 0, vikt med cos²φ), som till och med version 1.6. *Kontroll:* på en sträcka på 1000 km ligger den bästa radiantazimuten utan β 15°–90° från sträckan beroende på radiantens elevation (30° med radianten på 30°, tvärs sträckan med radianten på 60°), och den tvärställda radianten är värd 67 % vid 30° elevation; med β ligger den bästa radianten alltid längs sträckan och den tvärställda sjunker till 15 %. Med β går SM6FHZ / DH9GCD-regeln för bästa riktning förlorad; β förblir ett alternativ, på som standard eftersom det ger de mest försiktiga värdena, och stängs det av kommer regeln tillbaka.

Antalet meteorer som når en punkt är proportionellt mot sinus för radiantens elevation där (ŝ·û_P), samma korrektion som IMO använder för ZHR.

**Alternativet "Längre spår med låg radiant (DJ5HG)"** (kryssruta ovanför diagrammet, av som standard, med verktygstips): DJ5HG påpekar att med låg radiant faller färre meteorer per km², men spåren är längre (upp till 100 km användbara) och uppfyller reflexionslagen oftare. Med alternativet på blir vikten min(sin El, 15/100): den användbara skikttjockleken, 15 km, delad med sinus för elevationen ger spårlängden, begränsad till 100 km. Över omkring 9° tar de två effekterna ut varandra. Av förblir beräkningen försiktig.

**Beräkningsinställning** (samma rad, alternativknappar): **Försiktig** (standard, de mest försiktiga värdena: spårhöjd från radarn, normala spår, β på), **Som DJ5HG** (102 km, längre spår, β) och **Anpassad**, som väljs automatiskt när du ändrar höjden, rutan *från radar*, alternativet för längre spår eller β för hand.

**3. Summa och procent.** Punkter var 15:e km på spårhöjden, endast där båda stationerna ser dem ovanför lobelevationen (*val*). 100 % är det för sträckan mest gynnsamma radiantläget:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F beräknas en gång per sträcka på ett rutnät av riktningar (azimut var 5:e grad, elevation var 2,5:e grad) och interpoleras.

**Effektivitet i dB (DJ5HG-referens).** Procentsatsen är bara relativ till den bästa radiantpositionen för den sträckan. För att jämföra olika sträckor anger programmet också effektiviteten i dB relativt DJ5HG:s fasta referens: 0 dB är maximum för en 1000 km lång nord–sydlig sträcka över ekvatorn med radianten på himmelsekvatorn vid dagjämning, beräknat med samma höjd och samma vikter. DJ5HG anger sina värden som bättre än 6 dB.

**4. Sida och index.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Bokstaven i tabellen är den sida som har störst andel. *Programmets val (handboken ekv. 32–33).*

## Jämförelse med DH9GCD

Primärkällorna för bästa riktning är Eshleman & Mlodnosky och Meeks & James (Proc. IRE, 1957), Hines (1955) och den experimentella kontrollen av den gjord av Forsyth, Hines & Vogan (1955): bara radianter på den halvcirkel av himlen som står vinkelrätt mot bisektrisen till spridningsvinkeln är användbara, antalet spår växer med sin El, och nära mittpunkten hamnar de användbara spåren omkring H·tan El åt sidan, på motsatt sida om radianten. DJ5HG gör en reservation: med en **låg** radiant rakt längs sträckan ger McKinleys formel starka signaler (Hamburg–Narvik, Kvadrantiderna, omkring 19 UTC), så "radiant i linje med sträckan = nästan noll" gäller bara för en hög radiant; programmet förblir försiktigt och visar varningen *LÅG RADIANT LÄNGS STRÄCKAN*.

En oberoende kontroll: formeln för bästa riktning av **DH9GCD**, återgiven av **DF5HC** (DARC-konferensen, januari 2018) – den har ingen publicerad primärkälla – där El och Az är radiantens elevation och azimut sett från din station och P motstationens azimut:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Den är störst när radianten står på 45° och tvärs mot sträckan. DF5HC anser att radianten står för lågt under 20° och **för högt över 70°**: dessa timmar får ↑ i tabellen och en varning i [Himlavalvet](Sky-View-sv#varningar). Formeln bortser från avstånd och höjder, men är en bra referens.

## Kontroller

| Kontroll | Resultat |
|---|---|
| SM6FHZ:s regel (VUSHF 2025): bästa sträcka ortogonal mot radiantens azimut, riktning = radiantens az ±90°, tolerans ±40–50° | Återges av modellen; med radianten i linje med sträckan och högt på himlen är effektiviteten nästan noll |
| QTFGUI av DJ5HG, Hamburg JO53IM – Barcelona, Quadrantiderna, 4 januari (exempel ur dess handbok) | QTFGUI: 07:00 riktning 252°, −8 dB; 08:00 ingen reflexionszon; 09:00 riktning 168°, −4 dB. YA-MS (höjd 102 km som i QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Alla tre metoderna ser hålet kl. 08:00, med radianten nästan i zenit |
| DJ5HG:s kurvor (*Die Geometrie…*, Bild 8–9: från Hamburg och München, Kvadrantiderna, 4 januari; avlästa ur diagrammet, omkring ±0,5 dB och ±15 min) mot det automatiska testet `--prova-dj5hg` (ett värde per timme) | Tider: hålet med radianten nära zenit infaller vid samma timmar (Barcelona 07:30–08:30 mot 07–09; Sofia 06:36–07:48 mot 07–08; Narvik 07–08:30 mot 07–09); Moskva är stängt 03–10 i båda, öppet från Hamburg till omkring 02:30 och från München till omkring 00:30, som DJ5HG skriver. Riktningar: 2–10° skillnad. Nivåer och form vid 102 km (medel- och RMS-avvikelse från kurvorna): inget β, inga längre spår −1,6 / 4,0 dB; längre spår +1,1 / 4,6 dB; β −5,4 / 6,2 dB men med bäst form (3,0 dB efter att medelvärdet dragits bort, mot 3,6): de djupa minimumen med låg radiant syns (Barcelona −15,6 dB kl. 17 mot −16 dB kl. 19:36; Sofia −18,5 dB kl. 20 mot −14 dB). β och längre spår (*Som DJ5HG*) −2,2 / 4,7 dB; den försiktiga inställningen (radarhöjd 89,5 km, β på, inga längre spår) −6,9 / 7,6 dB, form 3,3 dB. Utan β visar YA-MS knappt minimumet med radianten lågt och nästan i linje med sträckan (−8,6 och −10,4 dB): detta är DJ5HG:s eget förbehåll, därav varningen |
| Sampling var 5:e km i stället för var 15:e km | procentsatserna ändras med mindre än 0,3 enheter |

> Dokumentationen till MS-Soft 5.2 definierar OH5IY:s effektivitet som ett relativt index enbart för underdensa spår, med två faktorer (radiantens elevation, bäst omkring 45°, och vinkel mot sträckan, bäst 90°) och ett minimum som höjts för hand till 20 % för overdensa spår; formeln är inte publicerad. MCG_MS beräknar den för fyra fasta riktningar och, med DX-lokatorn, för den verkliga sträckan. Modellen tar bara hänsyn till underdensa spår, med isotropa antenner; overdensa skurar och den sporadiska bakgrunden ingår inte i effektiviteten (den sporadiska bakgrunden representeras av radarflödet).
