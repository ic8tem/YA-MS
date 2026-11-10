[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · **Afrikaans** · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [ไทย](Contributing-and-Contacts-th) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# Bydra en kontak

YA-MS verbeter deur die verslae van mense wat dit op die lug gebruik. Elke korreksie word aan sy bron toegeskryf.

## Kontak

| | |
|---|---|
| Outeur | Costantino Cerrotta **IC8TEM** |
| E-pos | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## 'n Probleem rapporteer

Open 'n **issue op GitHub** of skryf 'n e-pos met:

- bedryfstelsel en YA-MS-weergawe (in die venstertitel);
- die twee lokators, band en UTC-tyd;
- wat jy verwag het en wat jy gesien het ('n skermskoot help);
- vir radarprobleme, die boodskap wat in die oortjie [Radarvloed](Radar-Flux-af) gewys word.

## Wat veral nuttig is

- **Verslae van die lug.** Ure en paaie waar die doeltreffendheid of die voorspelling reg was – of verkeerd. Die model is eksperimenteel en moet met werklike QSO's en met MCG_MS / MS-Soft vergelyk word.
- **RMOB-vergelykings.** Waardes van die stasiefaktor K en van die eksponent k wat jy met die [RMOB-vergelyking](Experimental-Forecasts-af#rmob-vergelyking) gevind het, met jou band en stasie.
- **Data met 'n bron.** Beter radiantdrywings, aktiwiteitsprofiele, nuwe IMO-maksimumdatums (`data/massimi_imo.csv`), antennadata: sluit die bron in en dit sal aangehaal word.
- **Veranderings in die radargrafieke.** As die formaat van die Collm-grafiek verander, help 'n kopie van die beeld (`data/radar/`) om die lesing te herkalibreer.

## Vertalings

Die koppelvlakvertalings is gewone tekslêers in **`data/lingue/<code>.txt`** (UTF-8) en **enigiemand kan hulle korrigeer**:

```
<Italian text><TAB><translation>
```

- Een inskrywing per reël; reëls wat met `#` begin, is kommentaar.
- In albei kolomme beteken die twee karakters `\n` 'n reëlbreuk.
- Behou die plekhouers `{0}`, `{1}`, … met hul formaat (bv. `{0:F1}`, `{3:+0;-0}`), in die volgorde wat jou taal vereis.
- Ontbrekende of leë inskrywings word in Italiaans gewys. Die lys van al die sleutels is `data/lingue/chiavi.txt` (gegenereer deur `tools/estrai_chiavi.py`, moenie dit wysig nie).

Wysig die lêer in die `data/lingue`-gids van jou installasie en begin YA-MS weer (of verander die taal) om die resultaat te sien. Omdat hierdie lêers **by elke bywerking deur nuwer weergawes vervang word**, **stuur asseblief ook jou korreksies** – per e-pos of as 'n pull request op GitHub (`data/lingue/`) – sodat hulle in die volgende vrystelling opgeneem word.

Hierdie wiki bestaan in English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文; korreksies op die wikibladsye is ook welkom.
