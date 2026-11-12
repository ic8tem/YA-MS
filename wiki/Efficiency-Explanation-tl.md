[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · **Tagalog** · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Paliwanag ng pagkalkula ng kahusayan

*Tab: Mga teknikal na dokumento › Paliwanag ng pagkalkula ng kahusayan.*

[![Paliwanag ng pagkalkula ng kahusayan](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Isang teknikal na dokumento, *"Come YA-MS calcola l'efficienza di uno sciame"* (Paano kinakalkula ng YA-MS ang episyensya ng isang shower), na ipinapakita sa loob ng programa bilang isang maliwanag na pahina. Ipinapaliwanag nito **hakbang-hakbang** kung paano nakukuha ang episyensya, at sinasabi para sa bawat hakbang **kung saan ito nagmula**. Ipinapakita ito ng programa **sa wika ng interface** (lahat ng 36 na wika), gayundin ang manwal ng kalkulasyon; ibinibigay din ng wiki na ito ang nilalaman nito sa [Kalkulasyon ng episyensya](Efficiency-Calculation-tl#ang-modelo) at sa [Heometriya at path loss](Geometry-and-Path-Loss-tl).

## Mga label

May may-kulay na label ang bawat hakbang:

| Label | Kulay | Kahulugan |
|---|---|---|
| **FONTE** (sanggunian) | asul | ginagamit ng hakbang ang isang binanggit na sanggunian; tumutukoy ang numero sa bracket sa listahan sa dulo |
| **RILIEVO** (pagsusuri) | berde | paghahambing sa pagitan ng programa at ng mga sanggunian, kasama ang resulta |
| **SCELTA** (pagpili) | kahel | pagpili ng programa, hindi kinuha mula sa sanggunian: dapat suriin sa karanasan sa ere |

## Mga kabanata

| Kabanata | Nilalaman |
|---|---|
| 1. Panimula | Layunin, mga label, ang ibig sabihin ng episyensya (OH5IY, MCG_MS; ginagamit ng YA-MS ang totoong landas) |
| 2. Kung saan nangyayari ang mga repleksiyon: ang E layer | Mga bakas sa 80–120 km; taas ng bakas = moda ng histogram ng Collm (pagsusuri: 89.5 km noong 5/11/2026) |
| 3. Heometriya ng landas | Daigdig at gitnang punto; elebasyon ng antenna (pormula ng artikulo); karaniwang sona at ang mga hangganan nito; Hot A / Hot B; lobe ng antenna (DL6WU, Kraus, W4RNL) |
| 4. Ang radiant ng shower | Posisyon ng radiant (IMO 2026/2027), petsa ng peak (IMO o solar longitude), profile ng aktibidad |
| 5. Kondisyon ng repleksiyon | Specular na repleksiyon (McKinley), Gaussian na tolerance na 0.05 rad, pinakamahusay na tutok (SM6FHZ), pormula ng DH9GCD |
| 6. Mula sa isang punto patungo sa episyensya | Mga punto ng repleksiyon bawat 15 km, timbang ng bawat punto, porsiyento; paghahambing sa QTFGUI (DJ5HG) |
| 7. Pagbasa ng mga resulta | Panig A / B, indeks ng landas, kulay ng mga radiant, mga PREV na sona, seksiyong nakikita mula sa antenna |
| 8. Frequency ng operasyon at path loss | Mga tuntuning λ³ / λ², mula sa radar patungo sa amateur band, mga sanggunian ng path loss |
| 9. Mga kilalang limitasyon | Underdense na bakas lamang, isotropic na antenna, mga working value |
| 10. Mga sanggunian | 17 sangguniang may bilang |

## Mga button

| Button | Ano ang ginagawa |
|---|---|
| **I-export sa Word (.docx)...** | Nagse-save ng kopya ng `data/efficienza_spiegazione.docx` kung saan mo pipiliin (iminumungkahing pangalan *YA-MS - calcolo dell'efficienza.docx*) |
| **Buksan sa Word** | Binubuksan ang parehong `.docx` gamit ang default na programa para sa mga dokumentong Word (Word, LibreOffice, …) |

## Mga file

| File | Nilalaman |
|---|---|
| `data/efficienza_spiegazione.txt` | Ang tekstong ipinapakita sa tab, isang bloke bawat linya (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Ang bersyong Word |
| `data/spiegazione/efficienza_spiegazione_<code>.txt` / `.docx` | Ang parehong dokumento sa iba pang 35 wika (hal. `_en`, `_de`, `_pt-br`) |
| `doc/YA-MS_manuale_calcoli.docx` | Ang **manwal ng kalkulasyon** (Italyano): lahat ng ekwasyon (equation editor ng Word), may bilang, kasama ang kanilang mga sanggunian |
| `doc/manuali/YA-MS_manuale_calcoli_<code>.docx` | Ang manwal ng kalkulasyon sa iba pang 35 wika |

Muling nililikha ang dalawang dokumento mula sa source gamit ang `tools/build_spiegazione.py data [code]` at `node tools/build_manuale.js <file.docx> [code]`. Nasa `tools/traduzioni_doc/` ang mga salin (muling nililikha ng `tools/build_documenti.sh` ang lahat ng wika).
