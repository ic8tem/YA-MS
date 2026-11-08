[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · **Tagalog** · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# Mapa ng grid square

*Tab: Mapa ng grid square.*

[![Mapa ng grid square](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Ang mga Maidenhead grid square (4 na character) na iyong **nakontak** at **kumpirmado**, binasa mula sa ADIF file ng iyong log, sa isang mapa ng Europa – **isang sub-tab bawat banda: 50, 70, 144, 222 at 432 MHz**.

## Mga kontrol

| Kontrol | Ano ang ginagawa |
|---|---|
| **Ikarga ang ADIF file...** | Binabasa ang isang `.adi` / `.adif` file. **Pinapalitan** ng bagong ADIF ang naunang datos. |
| **Burahin ang memorya** | Binubura ang lahat ng grid square na ikinarga mula sa ADIF (humihingi ng kumpirmasyon). |
| Mouse | **Gulong = zoom, hilahin = ilipat, mouse sa ibabaw ng grid square = mga QSO** (hanggang anim na callsign na may petsa, *(kumpirmado)* kapag kumpirmado) |

Pagkatapos magkarga, ipinapakita ng status ang *… QSO ang nabasa, … grid square ng QSO sa mga bandang 50-432 MHz, … QSO ang itinapon (ibang banda o walang grid square)*. May caption ang mapa ng bawat banda na *… grid square na nakontak, … kumpirmado*.

| Kulay | Kahulugan |
|---|---|
| Kahel | nakontak |
| Berde | kumpirmado (QSL o LoTW) |

## Paano binabasa ang ADIF

- Mga field na ginagamit: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (espesipikasyon ng ADIF).
- Banda mula sa `BAND`, o mula sa frequency: 50–54 MHz = 6 m, 69.9–71.5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1.25 m, 420–450 MHz = 70 cm.
- **Kumpirmado** ang isang grid square kung hindi bababa sa isang QSO roon ang may `QSL_RCVD = Y` o `LOTW_QSL_RCVD = Y`.
- Iniimbak ang mga grid square sa `data/adif_quadrati.csv` hanggang magkarga ka ng ibang file o pindutin ang **Burahin ang memorya**.

**Hindi** kumokonekta ang YA-MS sa LoTW: i-export ang ADIF mula sa iyong logging program (o mula sa LoTW) at ikarga ito rito.
