[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · **Íslenska** · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# Reitakort

*Flipi: Reitakort.*

[![Reitakort](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Maidenhead-reitirnir (4 stafir) sem þú hefur **unnið** og fengið **staðfesta**, lesnir úr ADIF-skrá dagbókarinnar þinnar, á korti af Evrópu – **einn undirflipi fyrir hvert tíðnisvið: 50, 70, 144, 222 og 432 MHz**.

## Stýringar

| Stýring | Hvað hún gerir |
|---|---|
| **Hlaða ADIF-skrá...** | Les `.adi`- / `.adif`-skrá. Ný ADIF-skrá **kemur í stað** fyrri gagna. |
| **Hreinsa minni** | Eyðir öllum reitum sem hlaðið var úr ADIF (biður um staðfestingu). |
| Mús | **Hjól = aðdráttur, draga = hliðra, mús yfir reit = QSO** (allt að sex kallmerki með dagsetningu, *(staðfest)* þegar staðfest) |

Eftir hleðslu sýnir stöðulínan *… QSO lesin, … QSO-reitir á tíðnisviðunum 50-432 MHz, … QSO hafnað (önnur tíðnisvið eða án reits)*. Kort hvers tíðnisviðs hefur yfirskriftina *… reitir unnir, … staðfestir*.

| Litur | Merking |
|---|---|
| Appelsínugulur | unninn |
| Grænn | staðfestur (QSL eða LoTW) |

## Hvernig ADIF-skráin er lesin

- Reitir sem eru notaðir: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF-staðallinn).
- Tíðnisvið úr `BAND`, eða út frá tíðninni: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Reitur er **staðfestur** ef a.m.k. eitt QSO í honum hefur `QSL_RCVD = Y` eða `LOTW_QSL_RCVD = Y`.
- Reitirnir eru geymdir í `data/adif_quadrati.csv` þar til þú hleður annarri skrá eða ýtir á **Hreinsa minni**.

YA-MS tengist **ekki** LoTW: fluttu ADIF-skrána út úr dagbókarforritinu þínu (eða frá LoTW) og hladdu henni inn hér.
