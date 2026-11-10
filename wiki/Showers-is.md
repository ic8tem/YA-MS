[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · **Íslenska** · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh)

# Drífur

*Flipi: Drífur.*

[![Drífur](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Skráin yfir drífur sem allir útreikningar nota: **45 drífur** úr **IMO Meteor Shower Calendar 2026 og 2027** (töflur 5 og 7) auk **Antihelion Source** (tafla 6), hver með sínu **næsta hámarki**.

## Dálkar

| Dálkur | Merking |
|---|---|
| Kóði | IMO-kóði (QUA, PER, GEM, …) |
| Drífa | Heiti |
| Virkni | Virknitímabil (dagur/mánuður – dagur/mánuður) |
| λ max | Sólarlengd við hámark (J2000), frá IMO |
| **Næsta hámark (UTC)** | Dagsetning og tími næsta hámarks (sjá hér fyrir neðan) |
| **Uppruni hámarks** | *IMO 2026* / *IMO 2027* = dagsetning og tími sem IMO birtir; *IMO 2026 (dagur)* = IMO gefur aðeins daginn, tíminn sem sýndur er er reiknaður (*~hh:mm reikn.*); *reiknað út frá λ* = ekkert IMO-gildi fyrir það ár |
| R.A., Stjörnubr. | Geislapunktur við hámark (*hreyfanleg* fyrir Antihelion Source) |
| v km/s, r | Jarðmiðjuhraði og fjöldastuðull |
| ZHR | ZHR við hámark (*breyt.* = breytilegt) |
| Gerð | *sjónræn* eða *útvarp, dagur* |
| Virk í dag | *já* þegar drífan er virk núna |

## Næsta hámark

Forritið sýnir alltaf **næsta** hámark. Þegar IMO hefur birt dagatal ársins notar það **dagsetningu og tíma IMO** úr `data/massimi_imo.csv` (2026 og 2027 fylgja með); annars reiknar það augnablikið þegar sólin nær sólarlengd hámarksins (Meeus, *Astronomical Algorithms*, 25. kafli, leyst með aðferð Newtons).

**Prófun:** útreikningurinn ber saman við dagatöl IMO fyrir 2026 og 2027 innan fárra mínútna þar sem IMO gefur tímann (t.d. Kvaðrantítar 3/1/2026 21:13 á móti 21:00; Geminítar 14/12/2027 19:51 á móti 20:00). Undantekningar: Daytime kappa Leonids 2026 degi seinna (26/9 í stað 25/9) og tími eta Aquariids 2027 (15:10 á móti 09:00 hjá IMO) – í þessum tilvikum er gildi IMO notað.

**Ári bætt við:** þegar IMO birtir nýtt dagatal skaltu bæta línum þess við `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, tími auður ef IMO gefur aðeins daginn). Þangað til er hámarkið reiknað.

## Minni drífur og dagdrífur

Skráin inniheldur **minni drífurnar** á lista IMO – til dæmis October Camelopardalids (OCT, ZHR 5, virk 5.–6. október), Andrómedítana, gamma Ursae Minorids – og **radíódagdrífurnar** frá apríl til október (Daytime April Piscids, Daytime Arietids, Daytime zeta Perseids, Daytime beta Taurids, Daytime kappa Leonids, Daytime Sextantids, …). Jafnvel með lágt ZHR leggja þær sitt af mörkum til [leiðarstuðulsins](Efficiency-Calculation-is#líkanið) og [ráðlagðs Hot](Sky-View-is#ráðlagður-hot). Fyrir radíódagdrífurnar gefur IMO ekkert ZHR: þar sem ekkert er gefið notar forritið vinnugildið 5.

## Virknisnið og rek geislapunkts

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max, α0, δ0 og λ_max koma úr dagatali IMO; hallatölurnar B (ólíkar fyrir og eftir hámark) og daglegt rek dα/dλ, dδ/dλ eru **vinnugildi** skráð í `data/sciami.csv` (rektafla IMO hefur ekki enn verið færð inn). *Handbók, jöfnur 9 og 13.* Staðsetning Antihelion Source er brúuð línulega milli dagsetninga í töflu 6 hjá IMO (`data/ant_radiante.csv`; virk 10. desember – 20. september, ZHR um 4).

## Breyta skránni

`data/sciami.csv` er venjuleg textaskrá (skiltákn `;`) sem þú getur breytt: kóði, heiti, upphaf og endir (MM-DD), λ max, R.A., Stjörnubr., rek, v, r, ZHR, B fyrir/eftir, gerð (V sjónræn, R radíó að degi). Ef lína er röng birtir forritið skilaboð við ræsingu og hunsar hana.

Heimildir: International Meteor Organization – Meteor Shower Calendar 2026 og 2027, [www.imo.net](https://www.imo.net) (töflur 5, 6 og 7); Philip G0ISW (hámarkstíðni á klukkustund í radíó); Rossano IZ5TEK (scattertek).
