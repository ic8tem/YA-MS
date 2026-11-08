**English** · [Русский](Grid-Square-Map-ru) · [Deutsch](Grid-Square-Map-de) · [日本語](Grid-Square-Map-ja)

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
