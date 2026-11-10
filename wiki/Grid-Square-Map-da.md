[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · **Dansk** · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# Kort over felter

*Fane: Kort over felter.*

[![Kort over felter](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

De Maidenhead-felter (4 tegn), du har **kørt** og fået **bekræftet**, læst fra ADIF-filen fra din log, på et Europakort – **én underfane pr. bånd: 50, 70, 144, 222 og 432 MHz**.

## Betjening

| Element | Hvad det gør |
|---|---|
| **Indlæs ADIF-fil...** | Læser en `.adi`- / `.adif`-fil. En ny ADIF **erstatter** de tidligere data. |
| **Ryd hukommelsen** | Sletter alle felter indlæst fra ADIF (beder om bekræftelse). |
| Mus | **Scrollhjul = zoom, træk = flyt, mus over et felt = QSO'er** (op til seks kaldesignaler med dato, *(bekræftet)* når de er bekræftet) |

Efter indlæsning viser statuslinjen *… QSO'er læst, … QSO-felter på båndene 50-432 MHz, … QSO'er kasseret (andre bånd eller uden felt)*. Hvert båndkort har billedteksten *… felter kørt, … bekræftet*.

| Farve | Betydning |
|---|---|
| Orange | kørt |
| Grøn | bekræftet (QSL eller LoTW) |

## Sådan læses ADIF-filen

- Anvendte felter: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF-specifikationen).
- Båndet fra `BAND` eller fra frekvensen: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Et felt er **bekræftet**, hvis mindst én QSO i det har `QSL_RCVD = Y` eller `LOTW_QSL_RCVD = Y`.
- Felterne gemmes i `data/adif_quadrati.csv`, indtil du indlæser en anden fil eller trykker på **Ryd hukommelsen**.

YA-MS forbinder **ikke** til LoTW: eksportér ADIF fra dit logprogram (eller fra LoTW), og indlæs den her.
