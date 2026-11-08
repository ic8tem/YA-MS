**English** · [Русский](Grid-Square-Map-ru) · [Deutsch](Grid-Square-Map-de) · [日本語](Grid-Square-Map-ja)

# Kvadrātu karte

*Cilne: Kvadrātu karte.*

[![Kvadrātu karte](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Tavi **strādātie** un **apstiprinātie** Maidenhead kvadrāti (4 rakstzīmes), nolasīti no tava žurnāla ADIF faila, Eiropas kartē – **viena apakšcilne katrai joslai: 50, 70, 144, 222 un 432 MHz**.

## Vadība

| Vadīkla | Ko tā dara |
|---|---|
| **Ielādēt ADIF failu...** | Nolasa `.adi` / `.adif` failu. Jauns ADIF **aizstāj** iepriekšējos datus. |
| **Notīrīt atmiņu** | Dzēš visus no ADIF ielādētos kvadrātus (prasa apstiprinājumu). |
| Pele | **Ritenītis = tālummaiņa, vilkt = pārvietot, pele virs kvadrāta = QSO** (līdz sešiem izsaukuma signāliem ar datumu, *(apstiprināts)*, ja apstiprināts) |

Pēc ielādes statusā redzams *… QSO nolasīti, … QSO kvadrāti 50-432 MHz joslās, … QSO atmesti (citas joslas vai nav kvadrāta)*. Katrai joslas kartei ir paraksts *… strādāti kvadrāti, … apstiprināti*.

| Krāsa | Nozīme |
|---|---|
| Oranža | strādāts |
| Zaļa | apstiprināts (QSL vai LoTW) |

## Kā tiek nolasīts ADIF

- Izmantotie lauki: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF specifikācija).
- Josla no `BAND` vai no frekvences: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Kvadrāts ir **apstiprināts**, ja vismaz vienam tā QSO ir `QSL_RCVD = Y` vai `LOTW_QSL_RCVD = Y`.
- Kvadrāti tiek glabāti failā `data/adif_quadrati.csv`, līdz ielādē citu failu vai nospied **Notīrīt atmiņu**.

YA-MS **nesavienojas** ar LoTW: eksportē ADIF no savas žurnāla programmas (vai no LoTW) un ielādē to šeit.
