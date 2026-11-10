[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-BR) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · **Eesti** · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-TW)

# Efektiivsus - selgitus

*Sakk: Tehnilised dokumendid › Efektiivsus - selgitus.*

[![Efektiivsus - selgitus](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Tehniline dokument *"Come YA-MS calcola l'efficienza di uno sciame"* (Kuidas YA-MS arvutab meteoorivoolu efektiivsust), mida näidatakse programmis heleda lehena. See selgitab **samm-sammult**, kuidas efektiivsus saadakse, ja ütleb iga sammu kohta, **kust see pärineb**. Dokument on praegu **itaalia keeles**; see wiki esitab selle sisu eesti keeles lehtedel [Efektiivsuse arvutus](Efficiency-Calculation-et#mudel) ja [Geomeetria ja sumbumine](Geometry-and-Path-Loss-et).

## Märgendid

Igal sammul on värviline märgend:

| Märgend | Värv | Tähendus |
|---|---|---|
| **FONTE** (allikas) | sinine | samm võtab üle viidatud allika; sulgudes number viitab lõpus olevale loetelule |
| **RILIEVO** (kontroll) | roheline | programmi ja allikate võrdlus koos tulemusega |
| **SCELTA** (valik) | oranž | programmi valik, mis ei ole võetud allikast: tuleb kontrollida eetrikogemusega |

## Peatükid

| Peatükk | Sisu |
|---|---|
| 1. Sissejuhatus | Eesmärk, märgendid, mida tähendab efektiivsus (OH5IY, MCG_MS; YA-MS kasutab tegelikku trassi) |
| 2. Kus peegeldused tekivad: E-kiht | Jäljed 80–120 km kõrgusel; jälgede kõrgus = Collmi histogrammi mood (kontroll: 89,5 km 5.11.2026) |
| 3. Trassi geomeetria | Maa ja keskpunkt; antenni elevatsioon (artikli valem); ühisala ja selle piirid; Hot A / Hot B; antenni peaharu (DL6WU, Kraus, W4RNL) |
| 4. Meteoorivoolu radiant | Radiandi asend (IMO 2026/2027), maksimumi kuupäev (IMO või Päikese pikkus), aktiivsusprofiil |
| 5. Peegeldustingimus | Peegelpeegeldus (McKinley), Gaussi tolerants 0,05 rad, parim suund (SM6FHZ), DH9GCD valem |
| 6. Ühest punktist efektiivsuseni | Peegelduspunktid iga 15 km järel, iga punkti kaal, protsent; võrdlus QTFGUI-ga (DJ5HG) |
| 7. Tulemuste lugemine | Pool A / B, trassi indeks, radiantide värvid, PREV alad, antennist nähtav lõige |
| 8. Töösagedus ja sumbumine | λ³ / λ² reeglid, radarilt amatöörsagedusalale, sumbumise viited |
| 9. Teadaolevad piirangud | Ainult alatihedad jäljed, isotroopsed antennid, tööväärtused |
| 10. Allikad | 17 nummerdatud allikat |

## Nupud

| Nupp | Mida see teeb |
|---|---|
| **Ekspordi Wordi (.docx)...** | Salvestab faili `data/efficienza_spiegazione.docx` koopia sinu valitud kohta (soovitatud nimi *YA-MS - calcolo dell'efficienza.docx*) |
| **Ava Wordis** | Avab sama `.docx` faili Wordi dokumentide vaikeprogrammiga (Word, LibreOffice, …) |

## Failid

| Fail | Sisu |
|---|---|
| `data/efficienza_spiegazione.txt` | Sakil näidatav tekst, üks plokk rea kohta (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Wordi versioon |
| `doc/YA-MS_manuale_calcoli.docx` | **Arvutusjuhend**: kõik võrrandid (Wordi valemiredaktor), nummerdatud, koos allikatega |

Mõlemad dokumendid luuakse lähtekoodist uuesti käskudega `tools/build_spiegazione.py data` ja `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
