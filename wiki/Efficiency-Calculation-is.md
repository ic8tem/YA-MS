[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · **Íslenska** · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Útreikningur nýtni

*Flipi: Spáreikningur › Útreikningur nýtni.*

[![Útreikningur nýtni](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

**Nýtni** drífu segir, í prósentum, hve mikið staða geislapunktsins leyfir endurvörp á **þinni** leið. Hugtakið er komið frá Ilkka **OH5IY** (MS-Soft) og er tekið upp í grein Cerrotta–Sartori: hámark nýtninnar fellur ekki saman við sjónræna hámarkið (ZHR), því það ræðst af því hvar geislapunkturinn er miðað við stöðvarnar tvær. MCG_MS eftir DL5MCG beitir sömu hugmynd á fjórar fastar stefnur; YA-MS reiknar hana fyrir **raunverulegu leiðina** milli locatoranna tveggja.

Þessi flipi sýnir hana klukkustund fyrir klukkustund fyrir daginn sem valinn er í *Dagsetning útreiknings (UTC)* (gildi á hálfa tímanum).

## Yfirlitsspjöld

| Spjald | Innihald |
|---|---|
| **BESTI TÍMI DAGSINS** | Klukkustundin með hæsta leiðarstuðulinn, stuðullinn og ríkjandi hlið (A/B með %) |
| **HAGSTÆÐASTA DRÍFAN** | Drífan með hæsta ZHR × nýtni dagsins, nýtni hennar, klukkustund og hlið, og **besta stefna** (áttarhorn geislapunkts +90° / −90°) |
| **NÚNA** | Stuðull og ríkjandi hlið á þessari klukkustund, og ráðlagður Hot (aðeins þegar valinn dagur er í dag) |
| **TILRAUNASPÁ** | Væntanleg endurvörp/klst. núna, eftir 1 klst. og eftir 2 klst. á spátíðninni (Collm, reglur SM6FHZ; sjá [Tilraunaspár](Experimental-Forecasts-is)) |

Undir spjöldunum skýrir borði stafina A og B (sjá hér fyrir neðan).

## Graf

*Nýtni eftir klukkustundum fyrir … þann … (UTC, gildi á hálfa tímanum).* Fyrir allt að fimm drífur: nýtni í % sem heil lína og formúla DH9GCD sem punktalína í sama lit; **leiðarstuðullinn** sem bláar súlur á hægri kvarðanum.

## Klukkustundatafla

Ein lína fyrir hverja drífu sem er virk þann dag (raðað eftir ZHR), 24 dálkar fyrir klukkustundirnar (UTC):

| Reitur | Merking |
|---|---|
| `63A` | nýtni 63 %, flest endurvörp frá hlið **A** |
| `41B` | nýtni 41 %, hlið **B** |
| `3` | nýtni undir 5 %: tala án hliðarstafs |
| auður | nýtni undir 1 % |
| `…↑` | geislapunkturinn er **yfir 70°** séð frá þinni stöð á þeirri klukkustund (of hátt) |
| gulur texti | nýtni ≥ 50 % |

- **A** = **vinstri** séð frá þinni stöð í átt að mótstöðinni (svæðið Hot A); **B** = **hægri** (svæðið Hot B). Það borgar sig að snúa loftnetinu **10–30° í átt að þeirri hlið** (side-scatter, grein Cerrotta–Sartori).
- **Ljósbláar línur** (*DH9GCD %*, undir hverri drífu): formúla DH9GCD, til samanburðar.
- **Σ-lína**: *Leiðarstuðull (ZHR×nýtni)*.
- **Appelsínugul lína** (*Spá … MHz (endurv./klst.)*): tilraunaspáin, fyrir þær klukkustundir þar sem hún er til (í dag og hluti af morgundeginum).

## Líkanið

Öll skrefin eru í [reiknihandbókinni](Efficiency-Explanation-is) (`doc/YA-MS_manuale_calcoli.docx`, 5. kafli). Í stuttu máli:

**1. Speglunarendurvarp.** Slóð sendir merkið frá A til B aðeins ef hún snertir sporvölu (ellipsoid) með A og B í brennipunktunum (McKinley 1961). Slóðir drífu eru samsíða stefnu geislapunktsins ŝ (greinin; McKinley). Fyrir hvern punkt P í E-laginu, með einingarvigrum í átt að stöðvunum:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Sama lögmál liggur að baki QTFGUI eftir DJ5HG og texta hans *"Die Geometrie von Meteorscatterverbindungen"* (2004): slóðin dreifir á keilu sem hefur slóðina sem ás, og aðeins viðtæki á keilunni heyrir hana. Fyrir fullkomna slóð er keiluveggurinn mjög þunnur (geislari sem er þúsundir bylgjulengda langur); forritið samþykkir skilyrðið með Gauss-vikmörkum σ = 0,05 rad (um 3°), sem standa fyrir það sem fullkomna keilan sér ekki: dreifingu geislapunkta drífanna (0,3–1,4° samkvæmt mælingum GMN), slóðir sem vindurinn beygir og endanlega lengd þeirra – *val forritsins*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Vægi hvers punkts.** Afl frá undirþéttri slóð (McKinley; ITU-R P.843, jafna 3), φ = hálft dreifihornið (takmarkað við 85°, *val*), β = hornið milli slóðarinnar og útbreiðslusléttunnar A-P-B, p̂ = einingarþverill þeirrar sléttu:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Valkosturinn „β-horn milli slóðar og leiðar (fullur McKinley)“** (virkur sjálfgefið, varfærin stilling). Virkur: slóðir sem skera útbreiðslusléttuna eru 10–15 dB minna virði en þær sem liggja í henni, svo engin slóð er ofmetin. Óvirkur: hver slóð er vegin eins og hún lægi í sléttunni (β = 0, vægi með cos²φ), eins og fram að útgáfu 1.6. *Prófun:* á 1000 km leið er besta stefnuhorn geislapunktsins án β 15°–90° frá leiðinni eftir hæðarhorni geislapunktsins (30° með geislapunktinn í 30°, þvert á leiðina með geislapunktinn í 60°), og þverstæði geislapunkturinn er 67 % virði í 30° hæð; með β er besti geislapunkturinn alltaf eftir leiðinni og sá þverstæði fellur niður í 15 %. Með β tapast regla SM6FHZ / DH9GCD um bestu stefnu; β er áfram valkostur, virkur sjálfgefið vegna þess að hann gefur varfærnustu gildin, og sé hann gerður óvirkur kemur reglan aftur.

Fjöldi loftsteina sem nær punkti er í hlutfalli við sínus hæðarhorns geislapunktsins þar (ŝ·û_P), sama leiðrétting og IMO notar fyrir ZHR.

**Valkosturinn „Lengri slóðir með lágum geislapunkti (DJ5HG)“** (gátreitur fyrir ofan grafið, óvirkur sjálfgefið, með vísbendingu): DJ5HG bendir á að með lágum geislapunkti falla færri loftsteinar á km², en slóðirnar eru lengri (allt að 100 km nýtilegar) og uppfylla endurvarpslögmálið oftar. Með valkostinn virkan verður vægið min(sin El, 15/100): nýtileg lagþykkt, 15 km, deilt með sínus hæðarhornsins gefur lengd slóðarinnar, að hámarki 100 km. Yfir um 9° jafnast áhrifin tvö út. Óvirkur heldur útreikningurinn sér varfærinn.

**Stilling útreiknings** (sama röð, valhnappar): **Varfærin** (sjálfgefið, varfærnustu gildin: hæð slóða frá ratsjá, venjulegar slóðir, β virkt), **Eins og DJ5HG** (102 km, lengri slóðir, β) og **Sérsniðin**, sem er valin sjálfkrafa þegar þú breytir handvirkt hæðinni, reitnum *frá ratsjá*, valkostinum um lengri slóðir eða β.

**3. Summa og prósenta.** Punktar á 15 km fresti í slóðahæð, séðir af báðum stöðvum ofan sjóndeildarhrings og vegnir með lóðréttu geislamynstri beggja loftneta (reitur *geislamynstur loftnets*, sjálfgefið kveiktur; slökktur aðeins punktar ofan hæðar geislans) (*val*). 100 % er hagstæðasta staða geislapunktsins fyrir leiðina:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F er reiknað einu sinni fyrir hverja leið á neti stefna (áttarhorn á 5° fresti, hæðarhorn á 2,5° fresti) og brúað.

**Nýtni í dB (viðmið DJ5HG).** Prósentan miðast aðeins við bestu stöðu geislapunktsins fyrir þá leið. Til að bera saman ólíkar leiðir gefur forritið einnig nýtnina í dB miðað við fast viðmið DJ5HG: 0 dB er hámark 1000 km norður–suður-leiðar yfir miðbaug með geislapunktinn á miðbaug himins við jafndægur, reiknað með sömu hæð og sömu vægjum. DJ5HG segir gildi sín betri en 6 dB.

**4. Hlið og stuðull.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Stafurinn í töflunni er hliðin með stærra hlutfallið. *Val forritsins (handbók, jöfnur 32–33).*

## Samanburður við DH9GCD

Frumheimildirnar um bestu stefnu eru Eshleman & Mlodnosky og Meeks & James (Proc. IRE, 1957), Hines (1955) og tilraunaprófun á henni eftir Forsyth, Hines & Vogan (1955): aðeins geislapunktar á hálfhringnum á himninum hornrétt á helmingalínu dreifingarhornsins eru nýtilegir, fjöldi slóða vex með sin El, og nálægt miðpunktinum falla nýtilegu slóðirnar um H·tan El til hliðar, á hliðinni gegnt geislapunktinum. DJ5HG bætir við fyrirvara: með **lágan** geislapunkt beint eftir leiðinni gefur formúla McKinleys sterk merki (Hamborg–Narvík, Quadrantítar, um 19 UTC), svo „geislapunktur í línu við leiðina = nánast núll“ gildir aðeins fyrir háan geislapunkt; forritið heldur sér varfærið og sýnir viðvörunina *LÁGUR GEISLAPUNKTUR EFTIR LEIÐINNI*.

Óháð prófun: formúla **DH9GCD** fyrir bestu stefnu, sem **DF5HC** greindi frá (ráðstefna DARC, janúar 2018) – hún á sér enga birta frumheimild – þar sem El og Az eru hæðarhorn og áttarhorn geislapunktsins séð frá þinni stöð og P er áttarhorn mótstöðvarinnar:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Hún er mest þegar geislapunkturinn er í 45° og þvert á leiðina. DF5HC telur geislapunktinn of lágan undir 20° og **of háan yfir 70°**: þessar klukkustundir fá ↑ í töflunni og viðvörun í [Himinhvelfingunni](Sky-View-is#viðvaranir). Formúlan hunsar fjarlægð og hæðir, en er góð viðmiðun.

## Prófanir

| Prófun | Niðurstaða |
|---|---|
| Regla SM6FHZ (VUSHF 2025): besta leið hornrétt á áttarhorn geislapunkts, stefna = az geislapunkts ±90°, vikmörk ±40–50° | Líkanið endurskapar hana; þegar geislapunkturinn er í línu við leiðina og hátt á himni er nýtnin nánast núll |
| QTFGUI eftir DJ5HG, Hamborg JO53IM – Barcelona, Kvaðrantítar, 4. janúar (dæmi úr handbók þess) | QTFGUI: 07:00 stefna 252°, −8 dB; 08:00 ekkert endurvarpssvæði; 09:00 stefna 168°, −4 dB. YA-MS (hæð 102 km eins og QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Allar þrjár aðferðirnar sjá gatið kl. 08:00, með geislapunktinn nánast í hvirfilpunkti |
| Ferlar DJ5HG (*Die Geometrie…*, Bild 8–9: frá Hamborg og München, Quadrantítar, 4. janúar; lesnir af grafinu, um ±0,5 dB og ±15 mín.) borið saman við sjálfvirku prófunina `--prova-dj5hg` (eitt gildi á klukkustund) | Tímasetningar: gatið þegar geislapunkturinn er nálægt hvirfilpunkti fellur á sömu klukkustundir (Barcelona 07:30–08:30 á móti 07–09; Sofía 06:36–07:48 á móti 07–08; Narvík 07–08:30 á móti 07–09); Moskva er lokuð 03–10 í báðum, opin frá Hamborg til um 02:30 og frá München til um 00:30, eins og DJ5HG skrifar. Stefnur: 2–10° munur. Styrkur og lögun við 102 km (meðalfrávik og RMS-frávik frá ferlunum): ekkert β, engar lengri slóðir −1,6 / 4,0 dB; lengri slóðir +1,1 / 4,6 dB; β −5,4 / 6,2 dB en með bestu lögunina (3,0 dB eftir að meðaltalið er fjarlægt, á móti 3,6): djúpu lágmörkin með lágum geislapunkti koma fram (Barcelona −15,6 dB kl. 17 á móti −16 dB kl. 19:36; Sofía −18,5 dB kl. 20 á móti −14 dB). β og lengri slóðir (*Eins og DJ5HG*) −2,2 / 4,7 dB; varfærna stillingin (ratsjárhæð 89,5 km, β virkt, engar lengri slóðir) −6,9 / 7,6 dB, lögun 3,3 dB. Án β sýnir YA-MS varla lágmarkið þegar geislapunkturinn er lágur og nánast í stefnu leiðarinnar (−8,6 og −10,4 dB): þetta er fyrirvari DJ5HG sjálfs, þess vegna viðvörunin |
| Úrtak á 5 km fresti í stað 15 km | prósenturnar breytast um minna en 0,3 einingar |

> Skjölun MS-Soft 5.2 skilgreinir nýtni OH5IY sem afstæðan stuðul eingöngu fyrir undirþéttar slóðir, með tveimur þáttum (hæðarhorni geislapunktsins, best um 45°, og horni við leiðina, best 90°) og lágmarki sem hækkað er handvirkt í 20 % fyrir yfirþéttar slóðir; formúlan er óbirt. MCG_MS reiknar hana fyrir fjórar fastar stefnur og, með staðsetningarkóða DX-stöðvarinnar, fyrir raunverulegu leiðina. Líkanið tekur aðeins til undirþéttra slóða, með stefnulausum (ísótrópískum) loftnetum; yfirþéttir blossar og stopull bakgrunnur eru ekki í nýtninni (stopula bakgrunninn táknar ratsjárflæðið). Frá 1.8.1 er lóðrétt geislamynstur loftnetanna notað þegar reiturinn «geislamynstur loftnets» er kveiktur; í stefnuhorni eru loftnetin áfram stefnulaus.
