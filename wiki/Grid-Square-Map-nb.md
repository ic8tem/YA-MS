**English** · [Русский](Grid-Square-Map-ru) · [Deutsch](Grid-Square-Map-de) · [日本語](Grid-Square-Map-ja)

# Rutekart

*Fane: Rutekart.*

[![Rutekart](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Maidenhead-rutene (4 tegn) du har **kjørt** og fått **bekreftet**, lest fra ADIF-filen i loggen din, på et Europakart – **én underfane per bånd: 50, 70, 144, 222 og 432 MHz**.

## Kontroller

| Kontroll | Hva den gjør |
|---|---|
| **Last inn ADIF-fil...** | Leser en `.adi`- / `.adif`-fil. En ny ADIF **erstatter** de tidligere dataene. |
| **Tøm minne** | Sletter alle rutene lastet fra ADIF (ber om bekreftelse). |
| Mus | **Hjul = zoom, dra = flytt, mus over en rute = QSO-er** (inntil seks kallesignaler med dato, *(bekreftet)* når de er bekreftet) |

Etter innlasting viser statusen *… QSO-er lest, … QSO-ruter på båndene 50-432 MHz, … QSO-er forkastet (andre bånd eller uten rute)*. Hvert båndkart har bildeteksten *… ruter kjørt, … bekreftet*.

| Farge | Betydning |
|---|---|
| Oransje | kjørt |
| Grønn | bekreftet (QSL eller LoTW) |

## Slik leses ADIF-filen

- Felter som brukes: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF-spesifikasjonen).
- Båndet fra `BAND`, eller fra frekvensen: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- En rute er **bekreftet** hvis minst én QSO i den har `QSL_RCVD = Y` eller `LOTW_QSL_RCVD = Y`.
- Rutene lagres i `data/adif_quadrati.csv` til du laster inn en annen fil eller trykker **Tøm minne**.

YA-MS kobler **ikke** til LoTW: eksporter ADIF fra loggprogrammet ditt (eller fra LoTW) og last den inn her.
