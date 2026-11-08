**English** · [Русский](Grid-Square-Map-ru) · [Deutsch](Grid-Square-Map-de) · [日本語](Grid-Square-Map-ja)

# Kvadratų žemėlapis

*Kortelė: Kvadratų žemėlapis.*

[![Kvadratų žemėlapis](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Jūsų **dirbti** ir **patvirtinti** Maidenhead kvadratai (4 simboliai), nuskaityti iš jūsų žurnalo ADIF failo, Europos žemėlapyje – **kiekviena juosta atskiroje vidinėje kortelėje: 50, 70, 144, 222 ir 432 MHz**.

## Valdikliai

| Valdiklis | Ką daro |
|---|---|
| **Įkelti ADIF failą...** | Nuskaito `.adi` / `.adif` failą. Naujas ADIF **pakeičia** ankstesnius duomenis. |
| **Išvalyti atmintį** | Ištrina visus iš ADIF įkeltus kvadratus (prašo patvirtinimo). |
| Pelė | **Ratukas = mastelis, tempti = slinkti, pelė virš kvadrato = QSO** (iki šešių šaukinių su data, *(patvirtinta)*, kai patvirtinta) |

Įkėlus būsenos eilutė rodo *Nuskaityta … QSO, … QSO kvadratų 50-432 MHz juostose, atmesta … QSO (kitos juostos arba be kvadrato)*. Kiekvieno juostos žemėlapio užrašas – *dirbta … kvadratų, patvirtinta …*.

| Spalva | Reikšmė |
|---|---|
| Oranžinė | dirbta |
| Žalia | patvirtinta (QSL arba LoTW) |

## Kaip skaitomas ADIF

- Naudojami laukai: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF specifikacija).
- Juosta iš `BAND` arba pagal dažnį: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Kvadratas yra **patvirtintas**, jei bent vienas jame esantis QSO turi `QSL_RCVD = Y` arba `LOTW_QSL_RCVD = Y`.
- Kvadratai saugomi `data/adif_quadrati.csv`, kol įkeliate kitą failą arba spaudžiate **Išvalyti atmintį**.

YA-MS **nesijungia** prie LoTW: eksportuokite ADIF iš savo žurnalo programos (arba iš LoTW) ir įkelkite jį čia.
