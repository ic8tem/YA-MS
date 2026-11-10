[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · **Lietuvių** · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Efektyvumas - paaiškinimas

*Kortelė: Techniniai dokumentai › Efektyvumas - paaiškinimas.*

[![Efektyvumas - paaiškinimas](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Techninis dokumentas *"Come YA-MS calcola l'efficienza di uno sciame"* (Kaip YA-MS skaičiuoja srauto efektyvumą), programoje rodomas kaip šviesus puslapis. Jis **žingsnis po žingsnio** paaiškina, kaip gaunamas efektyvumas, ir kiekvienam žingsniui nurodo, **iš kur jis kilęs**. Programa jį rodo **sąsajos kalba** (visomis 36 kalbomis), kaip ir skaičiavimų vadovą; šioje wiki jo turinys taip pat pateiktas puslapiuose [Efektyvumo skaičiavimas](Efficiency-Calculation-lt#modelis) ir [Geometrija ir slopinimas](Geometry-and-Path-Loss-lt).

## Žymos

Kiekvienas žingsnis turi spalvotą žymą:

| Žyma | Spalva | Reikšmė |
|---|---|---|
| **FONTE** (šaltinis) | mėlyna | žingsnis perima cituojamą šaltinį; skaičius skliaustuose nurodo sąrašą pabaigoje |
| **RILIEVO** (patikra) | žalia | programos ir šaltinių palyginimas su rezultatu |
| **SCELTA** (sprendimas) | oranžinė | programos sprendimas, nepaimtas iš šaltinio: tikrintinas patirtimi eteryje |

## Skyriai

| Skyrius | Turinys |
|---|---|
| 1. Įvadas | Tikslas, žymos, ką reiškia efektyvumas (OH5IY, MCG_MS; YA-MS naudoja realią trasą) |
| 2. Kur vyksta atspindžiai: E sluoksnis | Pėdsakai 80–120 km aukštyje; pėdsakų aukštis = Collm histogramos moda (patikra: 89,5 km 2026-11-05) |
| 3. Trasos geometrija | Žemė ir vidurio taškas; antenos elevacija (straipsnio formulė); bendroji zona ir jos ribos; Hot A / Hot B; antenos lapelis (DL6WU, Kraus, W4RNL) |
| 4. Srauto radiantas | Radianto padėtis (IMO 2026/2027), maksimumo data (IMO arba Saulės ilguma), aktyvumo profilis |
| 5. Atspindžio sąlyga | Veidrodinis atspindys (McKinley), Gauso tolerancija 0,05 rad, geriausias nukreipimas (SM6FHZ), DH9GCD formulė |
| 6. Nuo vieno taško iki efektyvumo | Atspindžio taškai kas 15 km, kiekvieno taško svoris, procentas; palyginimas su QTFGUI (DJ5HG) |
| 7. Rezultatų skaitymas | Pusė A / B, trasos indeksas, radiantų spalvos, PREV zonos, pjūvis, matomas iš antenos |
| 8. Darbo dažnis ir slopinimas | λ³ / λ² taisyklės, nuo radaro iki mėgėjų juostos, slopinimo duomenys |
| 9. Žinomi ribojimai | Tik retieji pėdsakai, izotropinės antenos, darbinės vertės |
| 10. Šaltiniai | 17 sunumeruotų šaltinių |

## Mygtukai

| Mygtukas | Ką daro |
|---|---|
| **Eksportuoti į Word (.docx)...** | Išsaugo `data/efficienza_spiegazione.docx` kopiją jūsų pasirinktoje vietoje (siūlomas pavadinimas *YA-MS - calcolo dell'efficienza.docx*) |
| **Atverti Word** | Atveria tą patį `.docx` numatytąja Word dokumentų programa (Word, LibreOffice, …) |

## Failai

| Failas | Turinys |
|---|---|
| `data/efficienza_spiegazione.txt` | Kortelėje rodomas tekstas, po vieną bloką eilutėje (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Word versija |
| `data/spiegazione/efficienza_spiegazione_<code>.txt` / `.docx` | Tas pats dokumentas kitomis 35 kalbomis (pvz., `_en`, `_de`, `_pt-br`) |
| `doc/YA-MS_manuale_calcoli.docx` | **Skaičiavimų vadovas** (italų kalba): visos lygtys (Word lygčių rengyklė), sunumeruotos, su šaltiniais |
| `doc/manuali/YA-MS_manuale_calcoli_<code>.docx` | Skaičiavimų vadovas kitomis 35 kalbomis |

Abu dokumentai iš naujo sugeneruojami iš išeitinio kodo komandomis `tools/build_spiegazione.py data [code]` ir `node tools/build_manuale.js <file.docx> [code]`. Vertimai yra kataloge `tools/traduzioni_doc/` (`tools/build_documenti.sh` iš naujo sugeneruoja visas kalbas).
