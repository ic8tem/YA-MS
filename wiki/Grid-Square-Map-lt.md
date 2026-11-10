[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · **Lietuvių** · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Ελληνικά](Grid-Square-Map-el) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [ไทย](Grid-Square-Map-th) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh) · [中文 (繁體)](Grid-Square-Map-zh-tw)

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
