[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · **Lietuvių** · [Latviešu](Getting-Started-lv) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh)

# Pradžia

Pirmą kartą paleista YA-MS rodo pavyzdinę trasą (JN70CN → JO62QM, 144 MHz). Penkių minučių pakanka pritaikyti ją savo stočiai.

## 1. Trys valdymo eilutės

Virš kortelių yra trys valdymo eilutės, galiojančios visoms kortelėms. Mygtukas **Valdymas** viršuje dešinėje jas suskleidžia ir išskleidžia (naudinga su dideliu šriftu); pasirinkimas įsimenamas.

**1 eilutė – stotys ir juosta**

| Valdiklis | Ką daro |
|---|---|
| **Mano lokatorius** / **aukštis m** | Jūsų Maidenhead lokatorius (4, 6 arba 8 simboliai; naudojamas kvadrato centras) ir stoties aukštis virš jūros lygio. |
| **Korespondentas** / **aukštis m** | Stoties, su kuria norite užmegzti ryšį, lokatorius ir aukštis. |
| **Juosta MHz** | 28, 50, 70, 144, 222 arba 432 MHz: naudojama antenos stiprinimui ir lapeliui, srauto įverčiui ir ryšio biudžetui. |
| **Skaičiuoti** | Iš naujo apskaičiuoja trasą (E sluoksnio diskretizavimas: kelios sekundės). |
| **Antenos az** | Jūsų antenos azimutas: visada **DX kryptimi** (trasos azimutas). |
| **Šriftas** | Viso teksto dydis, 100–300 %. Žr. [Nustatymai](Settings-and-Data-Folder-lt#šriftas-ir-valdymas). |

**2 eilutė – E sluoksnis ir antena**

| Valdiklis | Ką daro |
|---|---|
| **Pėdsakų aukštis km** + **iš radaro** | Meteorų pėdsakų aukštis (numatytasis 90 km). Pažymėjus *iš radaro*, naudojamas dažniausias Collm radaro išmatuotas aukštis (moda); žr. [Radaro srautas](Radar-Flux-lt). |
| **Lapelio elevacija °** | Žemiausia jūsų antenos lapelio elevacija (0° = horizontas). Naudojami tik tie E sluoksnio taškai, kuriuos abi stotys mato virš šios elevacijos. |
| **Yagi antena: strėlė m** | Jūsų Yagi strėlės ilgis. Programa rodo ilgį λ, stiprinimą (DL6WU kreivė) ir −3 dB lapelį horizontalioje ir vertikalioje plokštumoje; žr. [Geometrija ir slopinimas](Geometry-and-Path-Loss-lt#antenos-stiprinimas-ir-lapelis). Žemiau 2 λ įvertis apytikslis. |
| **Hot spot nuo vidurio taško km** | Hot A ir Hot B atstumas nuo vidurio taško, 30–400 km (numatytasis 150 km, kaip AMS Bulletin 203 / W8WN / MSHV). |

**3 eilutė – laikas**

| Valdiklis | Ką daro |
|---|---|
| **Laikas** | UTC laikrodis. |
| **Skaičiavimo data (UTC)** | Skaičiavimo diena kortelėms [Prognozės skaičiavimas](Sky-View-lt) ir [GRAVES radaras](GRAVES-Radar-lt) (pagal nutylėjimą šiandien), esamu paros laiku. |
| **Valandos (nuo −12 iki +36 h)** | Perkelia skaičiavimo momentą nuo 12 valandų prieš iki 36 valandų po to laiko, 15 minučių žingsniais. Šalia: *Skaičiavimas: dabar* arba *Skaičiavimas: dd/mm hh:mm UTC*. |
| **Realus laikas** | Grįžti į dabartį. |
| **24 h lentelės diena (UTC)** | Diena, rodoma kortelėje [Efektyvumo skaičiavimas](Efficiency-Calculation-lt) ir GRAVES laiko juostoje. |

## 2. Jūsų stotis ir korespondentas

1. Įveskite **Mano lokatorius** ir **aukštis m**.
2. Įveskite **korespondento** lokatorių ir aukštį – arba spustelėkite žemėlapį [Dangaus skliaute](Sky-View-lt): **kairysis spustelėjimas = korespondento lokatorius**, **dešinysis spustelėjimas = mano stoties lokatorius**.
3. Pasirinkite **Juosta MHz** ir spauskite **Skaičiuoti**.

Būsenos juosta apačioje patvirtina: *Trasa apskaičiuota: … km, … atspindžio taškų imtis per … s*.

## 3. Jūsų antena

Įveskite savo Yagi **strėlės ilgį**. Programa apskaičiuoja stiprinimą ir lapelį ir įspėja, jei Hot A arba Hot B jau patenka **į lapelį**, kai antena nukreipta į korespondentą (tada jie piešiami pilkai: anteną sukti nereikia).

## 4. Rezultatų skaitymas

| Klausimas | Kur žiūrėti |
|---|---|
| Kuris srautas dabar padeda mano trasai ir iš kurios pusės? | [Dangaus skliautas](Sky-View-lt): srautų sąrašas, rekomenduojamas Hot raudonai, PREV zonos |
| Kuri šiandien geriausia valanda? | [Efektyvumo skaičiavimas](Efficiency-Calculation-lt): apžvalgos skydeliai ir valandinė lentelė |
| Kiek meteorų skaičiuoja radaras? | [Radaro srautas](Radar-Flux-lt) |
| Kiek atspindžių galiu tikėtis 144 MHz juostoje? | [Eksperimentinės prognozės](Experimental-Forecasts-lt) (eksperimentinė) |
| Ar mano stotis gali įveikti trasą? | [Geometrija ir slopinimas](Geometry-and-Path-Loss-lt): slopinimas ir atsarga |
| Kada kitas maksimumas? | [Srautai](Showers-lt) |
| Ar galiu išbandyti su GRAVES? | [GRAVES radaras](GRAVES-Radar-lt) |

## Praktinės taisyklės (iš šaltinių)

- **Nukreipkite statmenai srautui**: geriausia trasa yra statmena radianto azimutui; geriausias nukreipimas = radianto azimutas ±90°, tolerancija ±40–50° (SM6FHZ).
- **Šoninė sklaida**: pasukite anteną 10–30° į tą pusę (A arba B), iš kurios ateina dauguma atspindžių (Cerrotta–Sartori straipsnis).
- **Per aukštas radiantas** (virš 70°) arba per žemas (žemiau 20°) duoda mažai naudingų pėdsakų (DF5HC, DH9GCD).
- Sporadinių meteorų maksimumas – apie **06 UTC** (straipsnis; patvirtina Collm srautas).
- Naudingi atstumai 432 MHz juostoje: 800–2000 km, geriausias apie 1400 km (SM6FHZ); geriausias atstumas apskritai 1300–1500 km (DF5HC).

Toliau: [Dangaus skliautas](Sky-View-lt).
