**English** · [Русский](Efficiency-Calculation-ru) · [Deutsch](Efficiency-Calculation-de) · [日本語](Efficiency-Calculation-ja)

# Efektyvumo skaičiavimas

*Kortelė: Prognozės skaičiavimas › Efektyvumo skaičiavimas.*

[![Efektyvumo skaičiavimas](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

Srauto **efektyvumas** procentais nurodo, kiek jo radianto padėtis leidžia atspindžius **jūsų** trasoje. Sąvoką sukūrė Ilkka **OH5IY** (MS-Soft), ją perėmė Cerrotta–Sartori straipsnis: efektyvumo maksimumas nesutampa su vizualiuoju maksimumu (ZHR), nes jis priklauso nuo radianto padėties dviejų stočių atžvilgiu. DL5MCG MCG_MS taiko tą pačią idėją keturioms fiksuotoms kryptims; YA-MS jį skaičiuoja **realiai trasai** tarp dviejų lokatorių.

Ši kortelė rodo jį kas valandą dienai, pasirinktai lauke *24 h lentelės diena (UTC)* (vertės kiekvienos valandos viduryje).

## Apžvalgos skydeliai

| Skydelis | Turinys |
|---|---|
| **GERIAUSIAS DIENOS LAIKAS** | Valanda su didžiausiu trasos indeksu, indeksas ir vyraujanti pusė (A/B su %) |
| **PALANKIAUSIAS SRAUTAS** | Dienos srautas su didžiausiu ZHR × efektyvumas, jo efektyvumas, valanda ir pusė bei **geriausias nukreipimas** (radianto azimutas +90° / −90°) |
| **DABAR** | Indeksas ir vyraujanti pusė šią valandą bei rekomenduojamas Hot (tik kai pasirinkta diena yra šiandien) |
| **EKSPERIMENTINĖ PROGNOZĖ** | Laukiami atspindžiai/val. dabar, po 1 h ir po 2 h prognozės dažniu (Collm, SM6FHZ taisyklės; žr. [Eksperimentinės prognozės](Experimental-Forecasts-lt)) |

Po skydeliais juostelė paaiškina raides A ir B (žr. toliau).

## Grafikas

*Valandinis efektyvumas: …, … (UTC, vertės valandos viduryje).* Iki penkių srautų: efektyvumas % ištisine linija ir DH9GCD formulė tos pačios spalvos taškine linija; **trasos indeksas** mėlynais stulpeliais dešinėje skalėje.

## Valandinė lentelė

Po vieną eilutę kiekvienam tą dieną aktyviam srautui (surikiuota pagal ZHR), 24 stulpeliai valandoms (UTC):

| Langelis | Reikšmė |
|---|---|
| `63A` | efektyvumas 63 %, dauguma atspindžių iš pusės **A** |
| `41B` | efektyvumas 41 %, pusė **B** |
| `3` | efektyvumas mažesnis nei 5 %: skaičius be pusės raidės |
| tuščias | efektyvumas mažesnis nei 1 % |
| `…↑` | radiantas tą valandą yra **aukščiau nei 70°** iš jūsų stoties (per aukštai) |
| geltonas tekstas | efektyvumas ≥ 50 % |

- **A** = **kairėje**, žiūrint iš jūsų stoties į korespondentą (Hot A zona); **B** = **dešinėje** (Hot B zona). Verta pasukti anteną **10–30° į tą pusę** (šoninė sklaida, Cerrotta–Sartori straipsnis).
- **Žydros eilutės** (*DH9GCD %*, po kiekvienu srautu): DH9GCD formulė palyginimui.
- **Eilutė Σ**: *Trasos indeksas (ZHR×efekt.)*.
- **Oranžinė eilutė** (*Prognozė … MHz (atsp./val.)*): eksperimentinė prognozė valandoms, kurioms ji yra (šiandien ir dalis rytojaus).

## Modelis

Visi žingsniai pateikti [skaičiavimų vadove](Efficiency-Explanation-lt) (`doc/YA-MS_manuale_calcoli.docx`, 5 skyrius). Trumpai:

**1. Veidrodinis atspindys.** Pėdsakas siunčia signalą iš A į B tik tada, jei jis liečia elipsoidą, kurio židiniuose yra A ir B (McKinley 1961). Srauto pėdsakai lygiagretūs radianto krypčiai ŝ (straipsnis; McKinley). Kiekvienam E sluoksnio taškui P, su vienetiniais vektoriais stočių kryptimi:

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

Tas pats dėsnis yra DJ5HG QTFGUI pagrindas (kūginė sklaida). Sąlyga priimama su Gauso tolerancija σ = 0,05 rad (apie 3°) – *programos sprendimas*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Kiekvieno taško svoris.** Retojo pėdsako galia (McKinley), φ = pusė sklaidos kampo (apribota 85°, *sprendimas*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Į tašką patenkančių meteorų skaičius proporcingas radianto elevacijos ten sinusui (ŝ·û_P) – ta pati pataisa, kurią IMO taiko ZHR.

**3. Suma ir procentas.** Taškai kas 15 km pėdsakų aukštyje, tik ten, kur abi stotys juos mato virš lapelio elevacijos (*sprendimas*). 100 % – palankiausia radianto padėtis tai trasai:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F apskaičiuojama vieną kartą kiekvienai trasai krypčių tinkle (azimutas kas 5°, elevacija kas 2,5°) ir interpoliuojama.

**4. Pusė ir indeksas.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

Lentelės raidė – pusė su didesne dalimi. *Programos sprendimai (vadovo 32–33 lygtys).*

## DH9GCD palyginimas

Nepriklausoma patikra: **DH9GCD** geriausios krypties formulė, pateikta **DF5HC** (DARC konferencija, 2018 m. sausis), kur El ir Az – iš jūsų stoties matomo radianto elevacija ir azimutas, o P – korespondento azimutas:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Ji didžiausia, kai radiantas yra 45° aukštyje ir statmenai trasai. DF5HC laiko radiantą per žemu žemiau 20° ir **per aukštu virš 70°**: šios valandos lentelėje gauna ↑, o [Dangaus skliaute](Sky-View-lt#įspėjimai) – įspėjimą. Formulė neatsižvelgia į atstumą ir aukščius, bet yra geras atskaitos taškas.

## Patikros

| Patikra | Rezultatas |
|---|---|
| SM6FHZ taisyklė (VUSHF 2025): geriausia trasa statmena radianto azimutui, nukreipimas = radianto az ±90°, tolerancija ±40–50° | Modelis ją atkuria; kai radiantas sutampa su trasos kryptimi ir yra aukštai danguje, efektyvumas beveik nulinis |
| DJ5HG QTFGUI, Hamburgas JO53IM – Barselona, Kvadrantidai, sausio 4 d. (jo vadovo pavyzdys) | QTFGUI: 07:00 nukreipimas 252°, −8 dB; 08:00 nėra atspindžio zonos; 09:00 nukreipimas 168°, −4 dB. YA-MS (aukštis 102 km kaip QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Visi trys metodai mato 08:00 „skylę“, kai radiantas beveik zenite |
| Diskretizavimas kas 5 km vietoj 15 km | procentai pasikeičia mažiau nei 0,3 punkto |

> OH5IY ir MCG_MS naudojama skalė detaliai nežinoma (MS-Soft vadovai neprieinami): prieš laikydami procentus lygiaverčiais, palyginkite juos su šiomis programomis. Modelis vertina tik retuosius pėdsakus su izotropinėmis antenomis; tankiųjų pėdsakų žybsniai ir sporadinis fonas į efektyvumą neįtraukti (sporadinį foną atspindi radaro srautas).
