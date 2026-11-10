[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · **Eesti** · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Ελληνικά](Grid-Square-Map-el) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh) · [中文 (繁體)](Grid-Square-Map-zh-tw)

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
