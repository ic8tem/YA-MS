[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · **Íslenska** · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh)

# Útreikningur nýtni

*Flipi: Spáreikningur › Útreikningur nýtni.*

[![Útreikningur nýtni](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

**Nýtni** drífu segir, í prósentum, hve mikið staða geislapunktsins leyfir endurvörp á **þinni** leið. Hugtakið er komið frá Ilkka **OH5IY** (MS-Soft) og er tekið upp í grein Cerrotta–Sartori: hámark nýtninnar fellur ekki saman við sjónræna hámarkið (ZHR), því það ræðst af því hvar geislapunkturinn er miðað við stöðvarnar tvær. MCG_MS eftir DL5MCG beitir sömu hugmynd á fjórar fastar stefnur; YA-MS reiknar hana fyrir **raunverulegu leiðina** milli locatoranna tveggja.

Þessi flipi sýnir hana klukkustund fyrir klukkustund fyrir daginn sem valinn er í *Dagur fyrir 24 klst. töfluna (UTC)* (gildi á hálfa tímanum).

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

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     speglunarskilyrði: ŝ·n̂ = 0
```

Sama lögmál liggur að baki QTFGUI eftir DJ5HG (cone scattering). Skilyrðið er samþykkt með Gauss-vikmörkum σ = 0,05 rad (um 3°) – *val forritsins*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Vægi hvers punkts.** Afl frá undirþéttri slóð (McKinley), φ = hálft dreifihornið (takmarkað við 85°, *val*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Fjöldi loftsteina sem nær punkti er í hlutfalli við sínus hæðarhorns geislapunktsins þar (ŝ·û_P), sama leiðrétting og IMO notar fyrir ZHR.

**3. Summa og prósenta.** Punktar á 15 km fresti í hæð slóðanna, aðeins þar sem báðar stöðvar sjá þá ofar hæðarhorni geislans (*val*). 100 % er hagstæðasta staða geislapunktsins fyrir þá leið:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F er reiknað einu sinni fyrir hverja leið á neti stefna (áttarhorn á 5° fresti, hæðarhorn á 2,5° fresti) og brúað.

**4. Hlið og stuðull.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

Stafurinn í töflunni er hliðin með stærra hlutfallið. *Val forritsins (handbók, jöfnur 32–33).*

## Samanburður við DH9GCD

Óháð prófun: formúla **DH9GCD** fyrir bestu stefnu, sem **DF5HC** greindi frá (ráðstefna DARC, janúar 2018), þar sem El og Az eru hæðarhorn og áttarhorn geislapunktsins séð frá þinni stöð og P er áttarhorn mótstöðvarinnar:

```
E = sin El · cos El · sin(P − Az)          birt sem  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Hún er mest þegar geislapunkturinn er í 45° og þvert á leiðina. DF5HC telur geislapunktinn of lágan undir 20° og **of háan yfir 70°**: þessar klukkustundir fá ↑ í töflunni og viðvörun í [Himinhvelfingunni](Sky-View-is#viðvaranir). Formúlan hunsar fjarlægð og hæðir, en er góð viðmiðun.

## Prófanir

| Prófun | Niðurstaða |
|---|---|
| Regla SM6FHZ (VUSHF 2025): besta leið hornrétt á áttarhorn geislapunkts, stefna = az geislapunkts ±90°, vikmörk ±40–50° | Líkanið endurskapar hana; þegar geislapunkturinn er í línu við leiðina og hátt á himni er nýtnin nánast núll |
| QTFGUI eftir DJ5HG, Hamborg JO53IM – Barcelona, Kvaðrantítar, 4. janúar (dæmi úr handbók þess) | QTFGUI: 07:00 stefna 252°, −8 dB; 08:00 ekkert endurvarpssvæði; 09:00 stefna 168°, −4 dB. YA-MS (hæð 102 km eins og QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Allar þrjár aðferðirnar sjá gatið kl. 08:00, með geislapunktinn nánast í hvirfilpunkti |
| Úrtak á 5 km fresti í stað 15 km | prósenturnar breytast um minna en 0,3 einingar |

> Kvarðinn sem OH5IY og MCG_MS nota er ekki þekktur í smáatriðum (handbækur MS-Soft eru ekki aðgengilegar): berðu prósenturnar saman við þessi forrit áður en þú lítur á þær sem jafngildar. Líkanið tekur aðeins til undirþéttra slóða, með stefnulausum (ísótrópískum) loftnetum; yfirþéttir blossar og stopull bakgrunnur eru ekki í nýtninni (stopula bakgrunninn táknar ratsjárflæðið).
