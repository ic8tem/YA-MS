[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Português (Brasil)](Sky-View-pt-BR) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · **Íslenska** · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Polski](Sky-View-pl) · [Čeština](Sky-View-cs) · [Magyar](Sky-View-hu) · [Română](Sky-View-ro) · [Ελληνικά](Sky-View-el) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [ไทย](Sky-View-th) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh) · [中文 (繁體)](Sky-View-zh-TW)

# Himinhvelfing

*Flipi: Spáreikningur › Spáreikningur.*

[![Himinhvelfing](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Þessi undirflipi (himinhvelfingin í eldri útgáfum) sýnir á einum skjá **hvar** nýtilegu slóðirnar eru núna og **hvert skal beina loftnetinu**. Til vinstri er **grunnmynd** leiðarinnar; til hægri listi yfir drífur, lítil himinhvelfing með geislapunktunum, texti útreikningsins og **sniðið** séð frá loftnetinu þínu. Allt miðast við tímann sem valinn er með *Dagsetning útreiknings (UTC)* og sleðanum *Klukkustundir (−12 til +36 klst.)* (rauntími sjálfgefið, í 15 mínútna skrefum).

**Rönd fyrir ofan grunnmyndina** dregur saman útreikninginn fyrir þá stund: dagsetningu og tíma (*núna* eða klukkustundir frá núna), **leiðarstuðulinn Σ ZHR×η**, **gagnlegustu drífuna** með ZHR hennar og nýtni (einnig í dB miðað við viðmið DJ5HG, sjá [Útreikningur nýtni](Efficiency-Calculation-is)), fjölda drífa yfir sjóndeildarhring og **ráðlagðan Hot** með áttarhorni hans.

Í litlu himinhvelfingunni sýnir **appelsínugul lína** gegnum hvirfilpunktinn alltaf **réttu loftnetsstefnurnar**, hornrétt á rek valinnar drífu (eða þeirrar hagstæðustu): áttarhorn geislapunkts ±90°, merkt *loftnet NNN°* í báðum endum, með vikmörkunum ±45° sem grönnum línum. Stutt appelsínugul strik á jaðrinum sýna hornréttu stefnurnar fyrir hinar nýtilegu drífurnar.

## Grunnmynd (vinstri)

Kort af Evrópu séð ofan frá (**A til hægri**) með gráðukvarða umhverfis. Textinn undir kortinu gefur radíus þess (*Kort: jaðar = … km frá stöðinni*).

| Atriði | Teikning |
|---|---|
| Leið / DX | Græn lína frá þinni stöð til mótstöðvarinnar (alltaf raunveruleg stórhringsleið milli locatoranna) |
| **Hot A / Hot B** | Punktar sitt hvorum megin við miðpunktinn, hornrétt á leiðina, í þeirri fjarlægð sem frávikstafla AMS gefur (eða slegin inn handvirkt). **Rautt = ráðlagður**, **bleikt = utan loftnetsgeislans**, **grátt = innan geislans** (með viðvörun) |
| Loftnetsgeisli | Lárétti −3 dB geislinn umhverfis áttarhorn loftnetsins (loftnetinu alltaf beint að DX), merktur *geisli …°* |
| Mörk sameiginlega svæðisins | Daufir punktar *mörk A* / *mörk B* og hringirnir tveir þar sem sjóndeildarhringur hvorrar stöðvar mætir E-laginu (sjá [Rúmfræði](Geometry-and-Path-Loss-is#mörk-sameiginlega-svæðisins)) |
| Rek drífunnar | **Gul lína**: stefnan sem valin drífa (eða sú hagstæðasta) sópar himininn í, þ.e. áttarhorn geislapunktsins |
| Bestu stefnur | **Appelsínugulir punktar**: stefnurnar tvær hornrétt á rekið (áttarhorn geislapunkts ±90°, SM6FHZ) |
| **PREV-svæði** | Ljósir sporbaugar: þar sem líklegustu slóðirnar lenda **núna**, einn fyrir hvora hlið leiðarinnar |

Merkingar skarast ekki: Hot A og PREV A eru skrifuð vinstra megin við leiðina, B hægra megin. **Skýringar** eru samfellanlegur dálkur hægra megin við kortið.

**Músin á kortinu:** **vinstri smellur = locator mótstöðvar**, **hægri smellur = locator minnar stöðvar**. Leiðin er endurreiknuð strax.

Valkostir fyrir ofan listann yfir drífur: **Stefnur Hot A / Hot B**, **Kort af Evrópu** (Natural Earth, sótt í `data/mappa` við fyrstu ræsingu), **Séð ofan frá (A til hægri)**.

### Ráðlagður Hot

Fyrir sýndan tíma leggur forritið saman, yfir allar drífur ofan sjóndeildarhrings, vægið ZHR × nýtni, skipt á milli hliðar A (hlutfallið f_A) og hliðar B. Hliðin með meira vægi gefur ráðlagðan Hot, teiknaðan í rauðu:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Val forritsins (handbók, jafna 23).* Uppruni hugmyndarinnar: DJ5HG, eftir frásögn DF5HC (ráðstefna DARC 2018) – eftir stöðu geislapunktsins er annar punkturinn, HOT-A eða HOT-B, hagstæðari. Að snúa 10–30° í átt að þeirri hlið (side-scatter) kemur úr grein Cerrotta–Sartori.

### PREV-svæði

Fyrir hvern punkt P í E-laginu eru framlög allra virkra drífa til nýtninnar (sama speglunarskilyrði og fyrir [nýtnina](Efficiency-Calculation-is#líkanið)) lögð saman, vegin með ZHR. Punktar með a.m.k. 3 % af hámarkinu mynda PREV-svæðin; hvert þeirra er teiknað sem sporbaugur með miðju = vegnu meðaltali punktanna og ása = tvöfaldri dreifingu þeirra.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Val forritsins (handbók, jafna 34).* Þetta er hagnýta reglan: ef drífan sópar frá norðri til suðurs lenda nýtilegu slóðirnar í austri og vestri.

## Listi yfir drífur (efst til hægri)

| Dálkur | Merking |
|---|---|
| Drífa, Kóði | Heiti og IMO-kóði |
| ZHR núna | Virkni á þessari stundu (ZHR við hámark samkvæmt IMO með virknisniðinu) |
| Áttarhorn, Hæðarh. | Staða geislapunktsins séð frá þinni stöð |
| Nýtni % | Nýtni drífunnar fyrir þessa leið |
| Hlið | A eða B, hliðin sem flest endurvörp berast frá |
| Besta stefna | Áttarhorn geislapunkts ±90° |
| Rís, Sest | Hvenær geislapunkturinn rís og sest (UTC); *sírisa* eða *alltaf undir* þegar það á við |

Smelltu á línu til að velja drífuna: gula reklínan og appelsínugulu punktarnir fylgja henni.

## Lítil himinhvelfing (miðja til hægri)

Geislapunktarnir á himinhvelfingu séðri frá þinni stöð, með **IMO-kóða** sínum og **daglegri braut í blágrænu** (UTC-klukkustundir). **Smelltu á geislapunkt** til að velja hann. Litir:

| Litur | Merking |
|---|---|
| Gulur | nýtni ≥ 50 % og ZHR ≥ 2 |
| Appelsínugulur | nýtni ≥ 20 % |
| Dökkrauður | nýtni < 20 % |
| Grár | nánast óvirkur |

Við hliðina er texti útreikningsins: lengd og áttarhorn leiðarinnar, miðpunkturinn og hæðarhorn hans, áttarhorn og frávik Hot A / Hot B, ráðlagður Hot (*… ráðlagt núna: az. …° (…% væntanlegra endurvarpa)*), mörk sameiginlega svæðisins og áminningin: *besta stefna fyrir drífuna: HORNRÉTT á komustefnuna (áttarhorn geislapunkts ±90°, vikmörk ±40–50°, SM6FHZ)*.

## Snið (neðst til hægri)

*SNIÐ – líklegustu slóðirnar séðar frá loftnetinu í átt að mótstöðinni.* Lárétt er **áttarhorn miðað við mótstöðina** (← A vinstri, B → hægri), lóðrétt **hæðarhornið**. Fyrir hverja drífu eru teknir 14 sterkustu endurvarpspunktarnir; hver slóð er strik sem snýr að geislapunktinum, frá 10 km ofan við til 10 km neðan við hæð slóðanna (í mesta lagi 60 km á hvora hlið), þykkara eftir því sem það er líklegra. Einnig eru teiknuð: loftnetsgeislinn (−3 dB hringur umhverfis hæðarhorn geislans), mótstöðin og Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Val forritsins (handbók, jafna 35).*

## Viðvaranir

| Viðvörun | Hvenær |
|---|---|
| **VIÐVÖRUN: Hot A (og/eða Hot B) lendir innan loftnetsgeislans …** | Heiti bletturinn er innan ±θ/2 frá áttarhorni loftnetsins (θ = láréttur −3 dB geisli): með þessari stefnu er hann þegar þakinn. Sýndur grár á kortinu. Ráðlagður Hot helst rauður. |
| **GEISLAPUNKTUR OF HÁTT (yfir 70°)** | Nýtilegur geislapunktur er yfir 70° séð frá þinni stöð: slóðirnar falla nánast lóðrétt og endurvarpa litlu í átt að leiðinni (DF5HC, DH9GCD). Sömu klukkustundir eru merktar ↑ í [klukkustundatöflunni](Efficiency-Calculation-is#klukkustundatafla). |
| **LÁGUR GEISLAPUNKTUR EFTIR LEIÐINNI** | Virkur geislapunktur er undir 20° og innan 30° frá stefnu leiðarinnar. Reiknuð nýtni helst lág (varfærin), en DJ5HG býst við sjaldgæfum, sterkum endurvörpum frá strjúkandi slóðum í línu við leiðina (Hamborg–Narvík, Quadrantítar, um 19 UTC): þess virði að hlusta. |
| **LEIÐ HANDAN SJÓNDEILDARHRINGS SLÓÐANNA** | Í hæð slóðanna er miðpunktur leiðarinnar undir sjóndeildarhring beggja stöðva (um 2120 km með slóðir í 90 km). Viðvörunin gefur upp lágmarkshæð slóða sem þarf (um 96 km fyrir 2200 km, 105 km fyrir 2300 km): sambandið er aðeins mögulegt með hæstu slóðunum, og nýtni og deyfing eru á mörkum líkansins. |
| *Ekkert sameiginlegt svæði í E-laginu* | Leiðin er lengri en tvöföld drægnin í hæð slóðanna: stöðvarnar tvær sjá engan sameiginlegan hluta E-lagsins (eitt stökk ómögulegt). |
| *Enginn ráðlagður Hot* | Nánast engin virk drífa á þessum tíma. |

Viðmiðun fyrir grafík himinhvelfingarinnar: Swan Meteor Skyview eftir DL1DBC (swan.ms); pólrit með bestu stefnu: RadiantCalc eftir SM6FHZ.
