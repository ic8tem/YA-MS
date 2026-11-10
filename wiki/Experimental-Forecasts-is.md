[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · **Íslenska** · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh)

# Tilraunaspár

*Flipi: Spáreikningur › Tilraunaspár.*

[![Tilraunaspár](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Þessi flipi breytir loftsteinatalningum **Collm-ratsjárinnar (36,2 MHz)** í mat á **endurvörpum á klukkustund á amatörtíðnisviði** (144 MHz sjálfgefið, hvaða tíðni sem er frá 28 til 1300 MHz), spáir fyrir um **næstu 24 klukkustundir** fyrir þína leið og leyfir þér að **bera** matið **saman** við **RMOB**-athuganda – til dæmis einn sem hlustar á GRAVES á 143,050 MHz.

> Allt hér er **tilraun**: tíðnireglan er reynsluregla, og stöðvarstuðullinn ræðst af þinni stöð. Notaðu tölurnar til að bera saman klukkustundir og daga, og sannreyndu þær í loftinu.

## Stýringar

| Stýring | Sjálfgefið | Hvað hún gerir |
|---|---|---|
| **Markmiðstíðni MHz** | 144 | Tíðni spárinnar (28–1300 MHz) |
| **Veldisvísir λ^k** | 3 | Veldisvísirinn k í tíðnireglunni (SM6FHZ: 3) |
| **Stöðvarstuðull K** | 1 | Tekur tillit til móttökustöðvarinnar (afl, loftnet); fundinn með samanburði við RMOB-athuganda á sama tíðnisviði |
| **Hlaða RMOB-skrá af diski...** | | Les mánaðarlega RMOB-textaskrá (sjá hér fyrir neðan) |
| **Finna veldisvísinn út frá RMOB-skránni** | | Aðlagar k út frá sameiginlegum klukkustundum Collm og RMOB |
| **RMOB-athugandi** | autt | Nafn athugandans eins og það birtist í skráarheitinu (t.d. `NAME_112026rmob.TXT` → `NAME`) |
| **Sækja RMOB núna** | | Sækir skrá yfirstandandi mánaðar fyrir þann athuganda einu sinni |
| **sjálfvirk sókn á 5 mínútna fresti (virkjaðu aðeins með leyfi RMOB)** | **af** | Sjá [RMOB og sjálfvirk forrit](#rmob-og-sjálfvirk-forrit) |

Appelsínugula línan undir stýringunum sýnir regluna með núverandi tölum, t.d. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, kvörðun lengdarinnar og hámarkslengd pings samkvæmt IARU á þeirri tíðni.

## Frá ratsjánni að amatörtíðnisviðinu

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

**Heimild:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, maí 2025 – fjöldi og styrkur endurvarpa breytist með **λ³**, lengd með **λ²** (432 MHz er 14–15 dB undir 144 MHz og varir 1/9 af tímanum). **Prófun:** λ³-háðin er sú sama og í jöfnu McKinleys fyrir undirþéttar slóðir. Með k = 3 verða 1000 loftsteinar/klst. í Collm um **16 endurvörp/klst. á 144 MHz**; RMOB-athugendur GRAVES á 143,050 MHz telja venjulega **20 til 140 bergmál/klst.** (fréttabréf RMOB, júní 2018): stærðargráðan samrýmist, og munurinn er stöðvarstuðullinn K. (Handbók, jöfnur 44–45.)

## Næstu 24 klukkustundir

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**Viðvarandi gildi (persistence):** kvarðaða gildið fyrir sömu klukkustund daginn áður (eða tveimur dögum áður ef það vantar), leiðrétt með breytingu **drífustuðuls leiðarinnar** I (Σ ZHR × nýtni, sjá [Útreikningur nýtni](Efficiency-Calculation-is#líkanið)). Fastinn 10 táknar stopula bakgrunninn og takmarkar leiðréttinguna þegar stuðullinn er lítill. *Val forritsins (handbók, jafna 47).*

| Spjald | Innihald |
|---|---|
| **Mælt í Collm og kvarðað í f MHz – í gær og í dag (UTC)** | Loftsteinar/klst. hjá Collm-ratsjánni; kvörðuð gildi (appelsínugult, hægri kvarði); RMOB-talningar ef þeim hefur verið hlaðið (grænt, hægri kvarði) |
| **Tilraunaspá næstu 24 klst. við f MHz fyrir …** | Spáð endurvörp/klst. (súlur) og drífustuðull leiðarinnar (hægri kvarði) |
| Tafla | UTC-tími · Collm sama klukkutíma · Kvarðað · Drífustuðull leiðar · Spá /klst. · **Mat** |

**Mat:** *gott* þegar spáin er a.m.k. 1,3 × meðaltal 24 klukkustunda, *sæmilegt* frá 0,8 ×, *lélegt* þar undir. Sama spá birtist á spjaldinu **TILRAUNASPÁ** og í appelsínugulu línunni í [Útreikningi nýtni](Efficiency-Calculation-is), og hún er grunnurinn að væntanlegum bergmálum á flipanum [GRAVES-ratsjá](GRAVES-Radar-is#væntanleg-bergmál-tilraun).

## Samanburður við RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) safnar loftsteinatalningum radíóathugenda eftir klukkustundum; margir á Ítalíu hlusta á GRAVES á 143,050 MHz (stjörnuverið í Feneyjum, Faenza, Rovereto og fleiri).

**Lestur RMOB-skráa.** Tvö textasnið eru samþykkt:

| Snið | Útlit | Athugasemdir |
|---|---|---|
| Mánaðarskrá (Colorgramme / Spectrum Lab) | ein lína á dag, `day| n| n| …` með 24 klukkustundargildum | hin venjulega `NAME_MMYYYYrmob.TXT` |
| Tafla úr fréttabréfi | haus ` UT |  1   2   3 …`, línur `0h|175 166 …` | ef skráin inniheldur marga athugendur eru þeir lesnir hver á eftir öðrum: notaðu skrá með einum athuganda |

Mánuður og ár eru tekin úr skráarheitinu (`…_MMYYYYrmob…`) eða úr hausnum; annars er yfirstandandi mánuður notaður (og forritið segir frá því).

**Aðlögun veldisvísisins.** Með K = 1, út frá miðgildi hlutfallanna RMOB/Collm yfir sameiginlegu klukkustundirnar (a.m.k. 3):

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*Val forritsins (handbók, jafna 46).* Glugginn sýnir sameiginlegu klukkustundirnar, miðgildi hlutfallsins og k; **Já** beitir k (og setur K = 1), **Nei** heldur k = 3 – stilltu þá K handvirkt á gildið sem lagt er til í sama glugga.

## RMOB og sjálfvirk forrit

RMOB biður um að **sjálfvirk forrit sæki ekki skrár þess**. Þess vegna er **sjálfvirk sókn óvirk** í upphafi og ætti aðeins að virkja hana **eftir að hafa beðið RMOB um leyfi**. Án þess geturðu alltaf notað **Hlaða RMOB-skrá af diski...** eða ýtt á **Sækja RMOB núna** þegar þú þarft.

Niðurhalsslóðin er sniðmát í `config.ini` (lykillinn `rmob_url`, sjálfgefið `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, þar sem `{NOME}` er athugandinn og `{MMAAAA}` mánuður og ár); sóttar skrár eru geymdar í `data/radar/`.
