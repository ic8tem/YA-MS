[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · **Afrikaans** · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# Vierkantkaart

*Oortjie: Vierkantkaart.*

[![Vierkantkaart](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Die Maidenhead-vierkante (4 karakters) wat jy **gewerk** en **bevestig** het, gelees uit die ADIF-lêer van jou log, op 'n kaart van Europa – **een sub-oortjie per band: 50, 70, 144, 222 en 432 MHz**.

## Kontroles

| Kontrole | Wat dit doen |
|---|---|
| **Laai ADIF-lêer...** | Lees 'n `.adi`- / `.adif`-lêer. 'n Nuwe ADIF **vervang** die vorige data. |
| **Vee geheue uit** | Skrap al die vierkante wat uit ADIF gelaai is (vra vir bevestiging). |
| Muis | **Wieletjie = zoem, sleep = skuif, muis oor 'n vierkant = QSO's** (tot ses roepname met datum, *(bevestig)* wanneer bevestig) |

Ná die laai wys die status *… QSO's gelees, … QSO-vierkante in die 50-432 MHz-bande, … QSO's verwerp (ander bande of sonder vierkant)*. Elke bandkaart het die onderskrif *… vierkante gewerk, … bevestig*.

| Kleur | Betekenis |
|---|---|
| Oranje | gewerk |
| Groen | bevestig (QSL of LoTW) |

## Hoe die ADIF gelees word

- Velde wat gebruik word: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF-spesifikasie).
- Band uit `BAND`, of uit die frekwensie: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- 'n Vierkant is **bevestig** as minstens een QSO daarin `QSL_RCVD = Y` of `LOTW_QSL_RCVD = Y` het.
- Die vierkante word in `data/adif_quadrati.csv` bewaar totdat jy 'n ander lêer laai of **Vee geheue uit** druk.

YA-MS koppel **nie** aan LoTW nie: voer die ADIF uit jou logprogram (of uit LoTW) uit en laai dit hier.
