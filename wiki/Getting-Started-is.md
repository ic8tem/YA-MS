[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · **Íslenska** · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Fyrstu skrefin

Við fyrstu ræsingu sýnir YA-MS dæmi um leið (JN70CN → JO62QM á 144 MHz). Fimm mínútur nægja til að stilla það fyrir þína stöð.

## 1. Tvær raðir stýringa

Fyrir ofan flipana eru tvær raðir stýringa sem gilda fyrir alla flipa. Hnappurinn **Stýringar** efst til hægri fellir þær saman og opnar aftur (hentugt með stóru letri); valið er munað. Stöðin þín (reitur, hæð, band og Reikna) er efst til hægri í Umferð í rauntíma.

**Stöðin mín – Umferð í beinni**

| Stýring | Hvað hún gerir |
|---|---|
| **Minn locator** / **hæð m** | Maidenhead-locator þinn (4, 6 eða 8 stafir; miðja reitsins er notuð) og hæð stöðvarinnar yfir sjávarmáli. |
| **Mótstöð** / **hæð m** | Við hlið kortsins, til hægri, er reitur mótstöðvarinnar: skrifaðu kallmerkið og ýttu á Enter, reiturinn er sóttur í CALL3-gagnagrunninn (eins og í YAEC og LIVETROPOVHF); fyrir neðan eru reitur og hæð. Einnig má skrifa kallmerkið í reitarboxið. |
| **Tíðnisvið MHz** | 28, 50, 70, 144, 222 eða 432 MHz: notað fyrir mögnun og geisla loftnetsins, mat á flæði og aflreikninginn. |
| **Reikna** | Reiknar leiðina upp á nýtt (úrtak úr E-laginu: nokkrar sekúndur). |
| **Loftnet az** | Efst í reit mótstöðvarinnar, við hlið kortsins: stefna loftnetsins þíns, alltaf **að DX** (stefna leiðarinnar). Fyrir neðan, í sama dálki, er skýring kortsins. |

**Röð 1 – E-lagið og loftnetið**

| Stýring | Hvað hún gerir |
|---|---|
| **Hæð slóða km** + **frá ratsjá** | Hæð loftsteinaslóðanna (sjálfgefið 90 km). Þegar hakað er við *frá ratsjá* er notuð algengasta hæðin (tíðasta gildið) sem Collm-ratsjáin mælir; sjá [Ratsjárflæði](Radar-Flux-is). |
| **Hæðarhorn geisla °** | Hæð hámarks lóðrétta geisla loftnetsins: stefnuvirkt loftnet fest á 0° hefur samt geislann nokkrum gráðum yfir sjóndeildarhring vegna endurvarps frá jörðu (oftast 3-8°). Með reitinn **geislamynstur loftnets** kveiktan (sjálfgefið) eru punktar E-lagsins vegnir með lóðréttu geislamynstri beggja loftneta; slökktur eru aðeins notaðir punktar sem báðar stöðvar sjá ofan þessarar hæðar. |
| **Yagi-loftnet: bóma m** | Lengd bómunnar á Yagi-loftnetinu þínu. Forritið sýnir lengdina í λ, mögnunina (DL6WU-ferillinn) og −3 dB geislann, láréttan og lóðréttan; sjá [Rúmfræði og deyfing](Geometry-and-Path-Loss-is#loftnetsmögnun-og-geisli). Undir 2 λ er matið gróft. |
| **Heitur blettur frá miðpunkti km** + **auto (AMS)** | Fjarlægð Hot A og Hot B frá miðpunktinum. Þegar hakað er við *auto (AMS)* (sjálfgefið) fylgir hún töflu J. Richardsons (AMS) um frávik loftnets, sem DJ5HG vitnar í: 13° við 1000 km, 11° við 1250 km, 10° við 1500 og 2000 km (um 115, 121, 132 og 176 km frá miðpunktinum). Taktu hakið af til að slá inn 30–400 km handvirkt (MSHV notar 150 km). |

**Röð 2 – tími**

| Stýring | Hvað hún gerir |
|---|---|
| **Tími** | UTC-klukka. |
| **Dagsetning útreiknings (UTC)** | Dagur útreikningsins fyrir [Spáreikning](Sky-View-is) og [GRAVES-ratsjá](GRAVES-Radar-is) (sjálfgefið í dag), á núverandi tíma sólarhringsins. Einnig: dagurinn sem sýndur er í [Útreikningi nýtni](Efficiency-Calculation-is) og á tímalínu GRAVES. |
| **Klukkustundir (−12 til +36 klst.)** | Færir tíma útreikningsins frá 12 klukkustundum á undan til 36 klukkustunda á eftir þeim tíma, í 15 mínútna skrefum. Við hliðina: *Útreikningur fyrir: núna* eða *Útreikningur fyrir: dd/mm hh:mm UTC*. |
| **Rauntími** | Aftur til líðandi stundar. |

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
