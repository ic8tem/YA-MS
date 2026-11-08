**English** · [Русский](Grid-Square-Map-ru) · [Deutsch](Grid-Square-Map-de) · [日本語](Grid-Square-Map-ja)

# Ruutude kaart

*Sakk: Ruutude kaart.*

[![Ruutude kaart](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Sinu **töötatud** ja **kinnitatud** Maidenheadi ruudud (4 märki), loetud sinu logi ADIF-failist, Euroopa kaardil – **iga sagedusala oma alamsakil: 50, 70, 144, 222 ja 432 MHz**.

## Juhtnupud

| Juhtnupp | Mida see teeb |
|---|---|
| **Laadi ADIF-fail...** | Loeb faili `.adi` / `.adif`. Uus ADIF **asendab** eelmised andmed. |
| **Tühjenda mälu** | Kustutab kõik ADIF-ist laaditud ruudud (küsib kinnitust). |
| Hiir | **Rullik = suum, lohista = nihuta, hiir ruudu kohal = QSO-d** (kuni kuus kutsungit kuupäevaga, kinnitamise korral *(kinnitatud)*) |

Pärast laadimist näitab olekurida *… QSO-d loetud, … QSO-ruutu sagedusaladel 50-432 MHz, … QSO-d kõrvale jäetud (muud sagedusalad või ruut puudub)*. Igal sagedusala kaardil on allkiri *… ruutu töötatud, … kinnitatud*.

| Värv | Tähendus |
|---|---|
| Oranž | töötatud |
| Roheline | kinnitatud (QSL või LoTW) |

## Kuidas ADIF-i loetakse

- Kasutatavad väljad: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF-i spetsifikatsioon).
- Sagedusala väljast `BAND` või sageduse järgi: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Ruut on **kinnitatud**, kui vähemalt ühel selle QSO-l on `QSL_RCVD = Y` või `LOTW_QSL_RCVD = Y`.
- Ruute hoitakse failis `data/adif_quadrati.csv`, kuni laadid teise faili või vajutad **Tühjenda mälu**.

YA-MS **ei** ühendu LoTW-ga: ekspordi ADIF oma logiprogrammist (või LoTW-st) ja laadi see siia.
