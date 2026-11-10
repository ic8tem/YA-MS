[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · **Lietuvių** · [Latviešu](Geometry-and-Path-Loss-lv) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh)

# Geometrija ir slopinimas

*Kortelė: Prognozės skaičiavimas › Geometrija ir slopinimas.*

[![Geometrija ir slopinimas](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Tekstinė trasos ataskaita (pažymima, todėl ją galima kopijuoti) ir dešinėje – grafikas **Antenos elevacija priklausomai nuo atstumo iki sklaidos taško**. Skaičiai laužtiniuose skliaustuose nurodo skaičiavimų vadovo (`doc/YA-MS_manuale_calcoli.docx`) lygtis.

## Šios kortelės įvesties duomenys

| Laukas | Numatytasis | Paskirtis |
|---|---|---|
| **Galia W** | 400 | Siųstuvo galia ryšio biudžetui |
| **Antenos stiprinimas dBi (tx = rx)** | 14 | Ta pati antena abiejuose galuose |
| **Minimalus signalas dBm** | −130 | Mažiausias aptinkamas signalas (straipsnis: 8 elementų Yagi + priešstiprintuvis) |
| **Pėdsako tankis q = 10^ … elektronų/m** | 14 | Retojo pėdsako elektronų linijinis tankis |

Stotys, juosta, pėdsakų aukštis, lapelio elevacija, strėlė ir hot spot atstumas imami iš [valdymo eilučių](Getting-Started-lt#1-trys-valdymo-eilutės).

## Ataskaitos skyriai

| Skyrius | Turinys |
|---|---|
| **TRASOS GEOMETRIJA (sferinė Žemė, R = 6372,7955 km)** | Stotis ir korespondentas su aukščiais; atstumas, azimutas ir atgalinis azimutas; vidurio taškas (lokatorius ir koordinatės); pėdsakų aukštis (*<- moda, išmatuota Collm radaru*, kai paimta iš radaro); antenos elevacija į vidurio tašką |
| **HOT A / HOT B (klasikiniai hot spot, antenai nukreipti)** | Kiekvienam: lokatorius, azimutas nuo jūsų ir nuokrypis nuo tiesioginės krypties, azimutas nuo korespondento, atstumas, elevacija |
| **BENDROSIOS ZONOS RIBOS** | Nuotolis pėdsakų aukštyje su lapelio elevacija; Riba A / Riba B su azimutais |
| Antena | Strėlė λ, stiprinimas, horizontalusis / vertikalusis lapelis; ar Hot A ir Hot B yra lapelio viduje ar už jo |
| **TRASOS SLOPINIMAS (retasis pėdsakas, McKinley 1961; be antenų stiprinimo)** | Lentelė vidurio taškui (forward), Hot A ir Hot B ties 28, 50, 70, 144, 222 ir 432 MHz |
| **BIUDŽETAS TIES … MHz (vidurio taškas)** | Galia ir EIRP, slopinimas, signalas antenoje, mažiausias aptinkamas, **atsarga**; ta pati atsarga su vidutiniu OH5IY slopinimu |
| **EKSPERIMENTINĖS TAISYKLĖS TARP JUOSTŲ (SM6FHZ, VUSHF 2025)** | Skaičius/intensyvumas ir trukmė palyginti su 144 MHz; IARU didžiausias atspindys |

## Lokatorius ir trasa

Lokatorius (4, 6 arba 8 simboliai; kvadrato centras, IARU Maidenhead sistema) [14]. Atstumas, azimutas ir vidurio taškas pagal didžiojo apskritimo formules sferoje, kurios spindulys **r = 6372,7955 km** (Cerrotta–Sartori straipsnis) [15–16]. Nuo laiko priklausantys skaičiavimai susieti su **vidurio tašku**, nes geriausias laikas abiejuose galuose gali skirtis iki 1,5 valandos (SM6FHZ).

## Antenos elevacija

**Šaltinis:** Cerrotta–Sartori straipsnio formulė (7 pav.), kur x = d/r, d – atstumas žeme iki atspindžio taško, H – pėdsakų aukštis, h – stoties aukštis [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Patikra:** sutampa su tikslia sferine geometrija 0,03° tikslumu. Programa naudoja dviejų argumentų arktangentą, kuris už horizonto duoda neigiamas vertes ir išvengia straipsnyje minėtos periodiškumo problemos. Neigiama elevacija į vidurio tašką reiškia *trasa už geometrinio vieno šuolio nuotolio*.

## Horizonto nuotolis

Atstumas žeme, kuriame spindulys su elevacija e pasiekia aukštį H (geometrinė aukščiau pateiktos formulės atvirkštinė) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Patikra:** H = 89,5 km, e = 0° → **1062 km**. Straipsnio pavyzdyje (JN44BB–IO53RT) brėžinys horizonto sankirtas rodo maždaug 870 km nuo stočių, o tai atitinka apie 2° pakeltą lapelį (865 km).

## Bendrosios zonos ribos

**Šaltinis:** straipsnyje nustatomos kreivių sankirtos, kur kiekvienos stoties horizontas susitinka su E sluoksniu: dviejų apskritimų, kurių kampinis spindulys ρ = d_H/r ir centrai A ir B, sankirtos [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Jei 1 − |p0|² < 0, trasa ilgesnė nei 2·d_H ir stotys **nemato bendrosios E sluoksnio zonos**.

**Patikra:** tai **tolimiausi dangaus kraštai**, matomi iš abiejų stočių, **o ne taškai, į kuriuos reikia nukreipti**. Trasoje JN70CN–IN78UO (1710 km, azimutas 308°) jie yra 1062 km nuo stoties, 37° kairėje ir dešinėje nuo tiesioginės krypties, o MSHV siūlo 10°. Todėl jie vadinami *Riba A* / *Riba B* ir žemėlapyje piešiami blankiai.

## Hot A ir Hot B

**Šaltinis:** sporadinių meteorų atspindžiai susitelkia dviejose zonose („hot spot“) abipus vidurio taško. J. Richardson (AMS) lentelėje, kurią cituoja DJ5HG (*Die Geometrie von Meteorscatterverbindungen*, 2004), pateikia antenos nuokrypį nuo tiesioginės krypties: **13° ties 1000 km, 11° ties 1250 km, 10° ties 1500 ir 2000 km**. AMS Bulletin No. 203, kurį perėmė W8WN, nurodo 10° ties 1500 ir 1800 km.

**Sprendimas:** Hot A ir Hot B – taškai, nutolę atstumu s nuo vidurio taško M, statmenai trasai. Pažymėjus *auto (AMS)* (numatytasis), s gaunamas iš Richardson lentelės nuokrypio, interpoliuojant tiesiškai (13° žemiau 1000 km, 10° virš 2000 km): s = (D/2)·tan(nuokrypis). Nepažymėjus s įvedamas ranka, 30–400 km (MSHV naudoja 150 km); A – kairėje, žiūrint iš jūsų stoties į korespondentą, B – dešinėje [21]. Iš stoties matomas nuokrypis yra maždaug [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Patikra:** pagal AMS lentelę 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, tiek pat, kiek anksčiau naudoti ir MSHV naudojami 150 km; trumpose trasose lentelė priartina hot spot prie vidurio taško.

## Retojo pėdsako slopinimas

**Šaltinis:** McKinley lygtis ir ITU-R rekomendacija P.843 retiesiems pėdsakams (sin α = 1), be antenų stiprinimo; q – elektronų linijinis tankis, r_e – klasikinis elektrono spindulys = 2,818·10⁻¹⁵ m, R1, R2 – atstumai nuo pėdsako, φ – pusė sklaidos kampo, β – kampas tarp pėdsako ir trasos plokštumos, a₁ – pradinio spindulio daugiklis, r₀ metrais ir h kilometrais (P.843, 4 ir 7 lygtys) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Sprendimas:** ryšio biudžete ir slopinimo lentelėje naudojama β = 90° (pėdsakas kerta trasos plokštumą, nepalankiausias atvejis: atsargi vertė), o biudžete rodomas ir geriausias atvejis, β = 0. r₀ imamas vidutiniame aido aukštyje tam dažniui, h = 124 − 17 log f (P.843, 15 lygtis): 0,76 m ties 95 km 50 MHz dažniui, 0,40 m ties 87 km 144 MHz, 0,21 m ties 79 km 432 MHz. 1000 km trasoje a₁ yra 0,2 dB ties 50 MHz, 0,6 dB ties 144 MHz ir 1,4 dB ties 432 MHz (2,9 dB ties 600 km); esant fiksuotam DJ5HG 102 km aukščiui ties 432 MHz jis būtų apie 70 dB, t. y. jokio aido.

**Patikra:** su q = 10¹⁴ elektronų/m, pėdsakais 89,5 km aukštyje ir β = 0, ties 144 MHz: **182–192 dB** nuo 600 iki 2100 km (185 dB ties 1000 km), **172–190 dB** intervale, kurį savo daktaro disertacijoje apskaičiavo John Worsnop **G4BAO**, kaip nurodo GM8JBJ. Su β = 90° slopinimas padidėja 10 dB ties 600 km, 13 dB ties 1000 km ir 16 dB ties 2100 km; OH5IY **200 dB vidurkis** yra tarp šių dviejų atvejų. 182 dB GM8JBJ lentelėje nėra patvirtinimas: lentelėje nenurodytas dažnis, jos 86,4 dB vienai atkarpai yra laisvosios erdvės slopinimas 500 km atstumu ties 1 MHz (trūksta nario 20 log f: 129,6 dB ties 144 MHz), o jos eilučių suma yra 163,8 dB, ne 182; puslapyje nerašoma nei „mažiausias“, nei „144 MHz“.

## Ryšio biudžetas

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Stiprinimai įvedami ir naudojami dBi: McKinley slopinimas taikomas izotropinėms antenoms, todėl 2,15 dB dipolio pataisa neatimama (EIRP = galia + stiprinimas). Ataskaitoje taip pat pateikiama atsarga su **vidutiniu OH5IY slopinimu** (200 dB ties 144 MHz, perskaičiuota pagal λ³ pasirinktai juostai). Straipsnio duomuo: reikia apie **70 dBm EIRP** (−130 dBm + 200 dB, pvz., apie 400 W į 14 dBi anteną).

## Antenos stiprinimas ir lapelis

**Stiprinimas – šaltinis:** Günter Hoch **DL6WU** kreivė ilgosioms Yagi antenoms kaip strėlės ilgio L funkcija, pateikta W8IO (galioja nuo maždaug 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Patikra pagal L.B. Cebik W4RNL NEC modelius ties 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementai | Strėlė (λ) | W4RNL NEC (dBi) | Formulė (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Skirtumas niekada neviršija **0,1 dB**: stiprinimas labiau priklauso nuo strėlės ilgio nei nuo konstrukcijos (VK3AUU Yagi su tuo pačiu elementų skaičiumi turi trumpesnę strėlę). VK5DJ Yagi Calculator taip pat pateikia įverčius VK3AUU, WA2PHW ir DJ9BV variantams, kurių formulės nepaskelbtos.

**Lapelis – šaltinis:** Krauso taisyklė su apskritu lapeliu θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Patikra:** W4RNL DL6WU Yagi NEC modeliai duoda **5–10 % siauresnį horizontalųjį lapelį** nei Krausas: 33,8° / 26,4° / 22,6° 12, 19 ir 26 elementams, palyginti su 37,3° / 28,0° / 23,9°. Paprastos formulės neatsižvelgia į priekinius šoninius lapelius (W4RNL, *Long-Boom Yagi Rules of Thumb*). Ilgose strėlėse vertikalusis lapelis šiek tiek platesnis už horizontalųjį (14 λ: 18,4° / 18,8°).

**Sprendimas** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Pavyzdys: 14 λ Yagi ties 432 MHz → 20,3 dBi, lapelis 18,1° horizontaliai ir 19,5° vertikaliai; W4RNL modeliai duoda 20,4 dBi ir 18,4° / 18,8°. Tai apytikslės taisyklės, išvestos iš kelių DL6WU antenų.

Laikoma, kad antena visada nukreipta į DX. Hot spot yra **lapelio viduje**, jei |Az(Hot) − Az(antena)| ≤ θ_horizontalus/2: tada [Dangaus skliaute](Sky-View-lt) jis piešiamas pilkai ir pasirodo įspėjimas. Efektyvumo skaičiavime antenos izotropinės; tikrasis lapelis naudojamas tik šiai patikrai.

## Eksperimentinės taisyklės tarp juostų

Palyginti su 144 MHz: skaičius/intensyvumas × (144/f)³ (dB), trukmė × (144/f)² (SM6FHZ, VUSHF 2025). IARU 1 regiono didžiausia atspindžio trukmė: 1000 ms ties 50 MHz, 500 ms ties 70 MHz, 100 ms ties 144 MHz, 13 ms ties 432 MHz (VHF Handbook, cituojama straipsnyje). Taip pat žr. [Eksperimentinės prognozės](Experimental-Forecasts-lt).
