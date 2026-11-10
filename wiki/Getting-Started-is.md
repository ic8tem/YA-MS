[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · **Íslenska** · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh)

# Fyrstu skrefin

Við fyrstu ræsingu sýnir YA-MS dæmi um leið (JN70CN → JO62QM á 144 MHz). Fimm mínútur nægja til að stilla það fyrir þína stöð.

## 1. Þrjár raðir stýringa

Fyrir ofan flipana eru þrjár raðir stýringa sem gilda fyrir alla flipa. Hnappurinn **Stýringar** efst til hægri fellir þær saman og opnar aftur (hentugt með stóru letri); valið er munað.

**Röð 1 – stöðvar og tíðnisvið**

| Stýring | Hvað hún gerir |
|---|---|
| **Minn locator** / **hæð m** | Maidenhead-locator þinn (4, 6 eða 8 stafir; miðja reitsins er notuð) og hæð stöðvarinnar yfir sjávarmáli. |
| **Mótstöð** / **hæð m** | Locator og hæð stöðvarinnar sem þú vilt ná sambandi við. |
| **Tíðnisvið MHz** | 28, 50, 70, 144, 222 eða 432 MHz: notað fyrir mögnun og geisla loftnetsins, mat á flæði og aflreikninginn. |
| **Reikna** | Reiknar leiðina upp á nýtt (úrtak úr E-laginu: nokkrar sekúndur). |
| **Loftnet az** | Áttarhorn loftnetsins þíns: alltaf **að DX** (áttarhorn leiðarinnar). |
| **Letur** | Stærð alls texta, 100–300 %. Sjá [Stillingar](Settings-and-Data-Folder-is#letur-og-stýringar). |

**Röð 2 – E-lagið og loftnetið**

| Stýring | Hvað hún gerir |
|---|---|
| **Hæð slóða km** + **frá ratsjá** | Hæð loftsteinaslóðanna (sjálfgefið 90 km). Þegar hakað er við *frá ratsjá* er notuð algengasta hæðin (tíðasta gildið) sem Collm-ratsjáin mælir; sjá [Ratsjárflæði](Radar-Flux-is). |
| **Hæðarhorn geisla °** | Lægsta hæðarhorn loftnetsgeislans (0° = sjóndeildarhringur). Aðeins punktar í E-laginu sem báðar stöðvar sjá ofar þessu hæðarhorni eru notaðir. |
| **Yagi-loftnet: bóma m** | Lengd bómunnar á Yagi-loftnetinu þínu. Forritið sýnir lengdina í λ, mögnunina (DL6WU-ferillinn) og −3 dB geislann, láréttan og lóðréttan; sjá [Rúmfræði og deyfing](Geometry-and-Path-Loss-is#loftnetsmögnun-og-geisli). Undir 2 λ er matið gróft. |
| **Heitur blettur frá miðpunkti km** | Fjarlægð Hot A og Hot B frá miðpunktinum, 30–400 km (sjálfgefið 150 km, eins og í AMS Bulletin 203 / W8WN / MSHV). |

**Röð 3 – tími**

| Stýring | Hvað hún gerir |
|---|---|
| **Tími** | UTC-klukka. |
| **Tími útreiknings (±36 klst.)** | Færir tíma útreikningsins – [Spáreikningur](Sky-View-is) og [GRAVES-ratsjá](GRAVES-Radar-is) – allt að 36 klukkustundir aftur á bak eða fram, í 15 mínútna skrefum. Við hliðina: *Útreikningur fyrir: núna* eða *Útreikningur fyrir: dd/mm hh:mm UTC*. |
| **Rauntími** | Aftur til líðandi stundar. |
| **Dagur fyrir 24 klst. töfluna (UTC)** | Dagurinn sem sýndur er í [Útreikningi nýtni](Efficiency-Calculation-is) og á tímalínu GRAVES. |

## 2. Þín stöð og mótstöðin

1. Sláðu inn **Minn locator** og **hæð m**.
2. Sláðu inn locator og hæð **Mótstöðvar** – eða smelltu á kortið í [Himinhvelfingunni](Sky-View-is): **vinstri smellur = locator mótstöðvar**, **hægri smellur = locator minnar stöðvar**.
3. Veldu **Tíðnisvið MHz** og ýttu á **Reikna**.

Stöðustikan neðst staðfestir: *Leið reiknuð: … km, … endurvarpspunktar teknir í úrtak á … s*.

## 3. Loftnetið þitt

Sláðu inn **lengd bómunnar** á Yagi-loftnetinu þínu. Forritið leiðir af henni mögnun og geisla og varar þig við ef Hot A eða Hot B lenda þegar **innan geislans** þegar loftnetinu er beint að DX (þá eru þeir teiknaðir gráir: óþarfi að snúa loftnetinu).

## 4. Lestu niðurstöðurnar

| Spurning | Hvar á að líta |
|---|---|
| Hvaða drífa hjálpar leiðinni minni núna, og frá hvorri hlið? | [Himinhvelfing](Sky-View-is): listi yfir drífur, ráðlagður Hot í rauðu, PREV-svæði |
| Hver er besta klukkustund dagsins? | [Útreikningur nýtni](Efficiency-Calculation-is): yfirlitsspjöld og klukkustundatafla |
| Hve marga loftsteina telur ratsjáin? | [Ratsjárflæði](Radar-Flux-is) |
| Hve mörg ping get ég búist við á 144 MHz? | [Tilraunaspár](Experimental-Forecasts-is) (tilraun) |
| Getur stöðin mín lokað leiðinni? | [Rúmfræði og deyfing](Geometry-and-Path-Loss-is): leiðardeyfing og borð fyrir báru |
| Hvenær er næsta hámark? | [Drífur](Showers-is) |
| Get ég prófað með GRAVES? | [GRAVES-ratsjá](GRAVES-Radar-is) |

## Hagnýtar reglur (úr heimildunum)

- **Beindu þvert á drífuna**: besta leiðin er hornrétt á áttarhorn geislapunktsins; besta stefna = áttarhorn geislapunktsins ±90°, vikmörk ±40–50° (SM6FHZ).
- **Side-scatter**: snúðu loftnetinu 10–30° í átt að þeirri hlið (A eða B) sem flest endurvörp berast frá (grein Cerrotta–Sartori).
- **Geislapunktur of hátt** (yfir 70°) eða of lágt (undir 20°) gefur fáar nýtilegar slóðir (DF5HC, DH9GCD).
- Stopulir loftsteinar ná hámarki um **06 UTC** (greinin; staðfest af flæðinu frá Collm).
- Nýtilegar fjarlægðir á 432 MHz: 800–2000 km, best um 1400 km (SM6FHZ); besta fjarlægð almennt 1300–1500 km (DF5HC).

Næst: [Himinhvelfing](Sky-View-is).
