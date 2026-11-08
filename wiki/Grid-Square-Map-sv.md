**English** · [Русский](Grid-Square-Map-ru) · [Deutsch](Grid-Square-Map-de) · [日本語](Grid-Square-Map-ja)

# Rutkarta

*Flik: Rutkarta.*

[![Rutkarta](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

De Maidenhead-rutor (4 tecken) som du har **kört** och fått **bekräftade**, lästa från ADIF-filen i din logg, på en karta över Europa – **en underflik per band: 50, 70, 144, 222 och 432 MHz**.

## Reglage

| Reglage | Vad det gör |
|---|---|
| **Läs in ADIF-fil...** | Läser en `.adi`- / `.adif`-fil. En ny ADIF **ersätter** tidigare data. |
| **Rensa minnet** | Raderar alla rutor som lästs in från ADIF (ber om bekräftelse). |
| Mus | **Hjul = zoom, dra = panorera, musen över en ruta = QSO** (upp till sex anropssignaler med datum, *(bekräftad)* när de är bekräftade) |

Efter inläsningen visar statusen *… QSO lästa, … QSO-rutor på banden 50-432 MHz, … QSO kasserade (andra band eller utan ruta)*. Varje bands karta har texten *… rutor körda, … bekräftade*.

| Färg | Betydelse |
|---|---|
| Orange | körd |
| Grön | bekräftad (QSL eller LoTW) |

## Hur ADIF-filen läses

- Fält som används: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF-specifikationen).
- Bandet från `BAND`, eller från frekvensen: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- En ruta är **bekräftad** om minst ett QSO i den har `QSL_RCVD = Y` eller `LOTW_QSL_RCVD = Y`.
- Rutorna sparas i `data/adif_quadrati.csv` tills du läser in en annan fil eller trycker på **Rensa minnet**.

YA-MS ansluter **inte** till LoTW: exportera ADIF-filen från ditt loggprogram (eller från LoTW) och läs in den här.
