[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · **Lietuvių** · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [ไทย](Contributing-and-Contacts-th) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# Prisidėjimas ir kontaktai

YA-MS tobulėja dėka žmonių, kurie ją naudoja eteryje ir praneša apie savo pastebėjimus. Kiekvienas pataisymas priskiriamas jo šaltiniui.

## Kontaktai

| | |
|---|---|
| Autorius | Costantino Cerrotta **IC8TEM** |
| El. paštas | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Pranešimas apie problemą

Atverkite **issue GitHub** svetainėje arba parašykite el. laišką, nurodydami:

- operacinę sistemą ir YA-MS versiją (lango pavadinime);
- abu lokatorius, juostą ir UTC laiką;
- ko tikėjotės ir ką pamatėte (ekrano kopija padeda);
- radarų problemoms – pranešimą, rodomą kortelėje [Radaro srautas](Radar-Flux-lt).

## Kas ypač naudinga

- **Pranešimai iš eterio.** Valandos ir trasos, kur efektyvumas ar prognozė pasitvirtino – arba ne. Modelis eksperimentinis, jį reikia lyginti su realiais QSO ir su MCG_MS / MS-Soft.
- **Palyginimai su RMOB.** Stoties koeficiento K ir rodiklio k vertės, kurias radote [palyginę su RMOB](Experimental-Forecasts-lt#palyginimas-su-rmob), nurodant savo juostą ir stotį.
- **Duomenys su šaltiniu.** Tikslesni radiantų slinkimai, aktyvumo profiliai, naujos IMO maksimumų datos (`data/massimi_imo.csv`), antenų duomenys: nurodykite šaltinį ir jis bus cituojamas.
- **Radarų grafikų pokyčiai.** Jei pasikeičia Collm grafiko formatas, vaizdo kopija (`data/radar/`) padeda iš naujo kalibruoti skaitymą.

## Vertimai

Sąsajos vertimai yra paprasti tekstiniai failai **`data/lingue/<code>.txt`** (UTF-8), ir **kiekvienas gali juos taisyti**:

```
<Italian text><TAB><translation>
```

- Vienas įrašas eilutėje; eilutės, prasidedančios `#`, yra komentarai.
- Abiejuose stulpeliuose du simboliai `\n` reiškia eilutės lūžį.
- Išlaikykite vietos rezervavimo ženklus `{0}`, `{1}`, … su jų formatu (pvz., `{0:F1}`, `{3:+0;-0}`), tokia tvarka, kokios reikia jūsų kalbai.
- Trūkstami arba tušti įrašai rodomi itališkai. Visų raktų sąrašas – `data/lingue/chiavi.txt` (sugeneruotas `tools/estrai_chiavi.py`, jo neredaguokite).

Redaguokite failą savo įdiegties aplanke `data/lingue` ir paleiskite YA-MS iš naujo (arba perjunkite kalbą), kad pamatytumėte rezultatą. Kadangi šie failai **kiekvieno atnaujinimo metu pakeičiami naujesniais**, prašome savo pataisymus taip pat **atsiųsti** – el. paštu arba kaip pull request GitHub (`data/lingue/`) – kad jie patektų į kitą leidimą.

Ši wiki yra 36 kalbomis (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, ไทย, 日本語, 한국어, 中文, 中文 (繁體)); laukiami ir wiki puslapių pataisymai.
