[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · **Nederlands** · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Ελληνικά](Grid-Square-Map-el) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [ไทย](Grid-Square-Map-th) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh) · [中文 (繁體)](Grid-Square-Map-zh-tw)

# Vakkenkaart

*Tabblad: Vakkenkaart.*

[![Vakkenkaart](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/nl-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/nl-6.png)

De Maidenhead-vakken (4 tekens) die je hebt **gewerkt** en **bevestigd**, gelezen uit het ADIF-bestand van je log, op een kaart van Europa – **één subtabblad per band: 50, 70, 144, 222 en 432 MHz**.

## Bediening

| Element | Wat het doet |
|---|---|
| **ADIF-bestand laden...** | Leest een `.adi`- / `.adif`-bestand. Een nieuw ADIF-bestand **vervangt** de vorige gegevens. |
| **Geheugen wissen** | Wist alle uit het ADIF geladen vakken (vraagt om bevestiging). |
| Muis | **Scrollwiel = zoom, slepen = verschuiven, muis boven een vak = QSO** (tot zes roepnamen met datum, *(bevestigd)* als bevestigd) |

Na het laden toont de status *… QSO's gelezen, … QSO-vakken in de banden 50-432 MHz, … QSO's verworpen (andere banden of zonder vak)*. Elke bandkaart heeft het bijschrift *… vakken gewerkt, … bevestigd*.

| Kleur | Betekenis |
|---|---|
| Oranje | gewerkt |
| Groen | bevestigd (QSL of LoTW) |

## Hoe het ADIF wordt gelezen

- Gebruikte velden: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF-specificatie).
- Band uit `BAND`, of uit de frequentie: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Een vak is **bevestigd** als minstens één QSO erin `QSL_RCVD = Y` of `LOTW_QSL_RCVD = Y` heeft.
- De vakken blijven in `data/adif_quadrati.csv` totdat je een ander bestand laadt of op **Geheugen wissen** drukt.

YA-MS maakt **geen** verbinding met LoTW: exporteer het ADIF uit je logprogramma (of uit LoTW) en laad het hier.
