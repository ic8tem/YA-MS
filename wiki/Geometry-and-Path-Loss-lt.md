[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · **Lietuvių** · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [ไทย](Geometry-and-Path-Loss-th) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

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

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Patikra:** sutampa su tikslia sferine geometrija 0,03° tikslumu. Programa naudoja dviejų argumentų arktangentą, kuris už horizonto duoda neigiamas vertes ir išvengia straipsnyje minėtos periodiškumo problemos. Neigiama elevacija į vidurio tašką reiškia *trasa už geometrinio vieno šuolio nuotolio*.

## Horizonto nuotolis

Atstumas žeme, kuriame spindulys su elevacija e pasiekia aukštį H (geometrinė aukščiau pateiktos formulės atvirkštinė) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Patikra:** H = 89,5 km, e = 0° → **1062 km**. Straipsnio pavyzdyje (JN44BB–IO53RT) brėžinys horizonto sankirtas rodo maždaug 870 km nuo stočių, o tai atitinka apie 2° pakeltą lapelį (865 km).

## Bendrosios zonos ribos

**Šaltinis:** straipsnyje nustatomos kreivių sankirtos, kur kiekvienos stoties horizontas susitinka su E sluoksniu: dviejų apskritimų, kurių kampinis spindulys ρ = d_H/r ir centrai A ir B, sankirtos [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Jei 1 − |p0|² < 0, trasa ilgesnė nei 2·d_H ir stotys **nemato bendrosios E sluoksnio zonos**.

**Patikra:** tai **tolimiausi dangaus kraštai**, matomi iš abiejų stočių, **o ne taškai, į kuriuos reikia nukreipti**. Trasoje JN70CN–IN78UO (1710 km, azimutas 308°) jie yra 1062 km nuo stoties, 37° kairėje ir dešinėje nuo tiesioginės krypties, o MSHV siūlo 10°. Todėl jie vadinami *Riba A* / *Riba B* ir žemėlapyje piešiami blankiai.

## Hot A ir Hot B

**Šaltinis:** atspindžiai susitelkia dviejose zonose („hot spot“) maždaug **50–150 km abipus vidurio taško**. Tai AMS Bulletin No. 203 antenos nuokrypių lentelės pagrindas, kurį perėmė W8WN (10° nuokrypis 1500 ir 1800 km trasoms); LZ2HV MSHV taiko tą patį kriterijų.

**Sprendimas:** Hot A ir Hot B – taškai, nutolę atstumu s nuo vidurio taško M, statmenai trasai (s = 150 km, reguliuojama 30–400 km); A – kairėje, žiūrint iš jūsų stoties į korespondentą, B – dešinėje [21]. Iš stoties matomas nuokrypis yra maždaug [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Patikra:** JN70CN–IN78UO, D = 1710 km: 6,7°, kai s = 100 km, **10,0°, kai s = 150 km** (kaip MSHV ir AMS/W8WN), 13,2°, kai s = 200 km.

## Retojo pėdsako slopinimas

**Šaltinis:** McKinley lygtis retiesiems pėdsakams (β = 0, sin α = 1), be antenų stiprinimo; q – elektronų linijinis tankis, r_e – klasikinis elektrono spindulys = 2,818·10⁻¹⁵ m, R1, R2 – atstumai nuo pėdsako, φ – pusė sklaidos kampo [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Patikra:** su q = 10¹⁴ elektronų/m ties 144 MHz: **181–192 dB** nuo 600 iki 2200 km, atitinka straipsnio duomenis ties 144 MHz: **182 dB mažiausias** (GM8JBJ, pagal Kaiser & Closs 1952) ir **200 dB vidutinis** (OH5IY).

## Ryšio biudžetas

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. Stiprinimai įvedami dBi, o naudojami dBd (dBi − 2,15). Ataskaitoje taip pat pateikiama atsarga su **vidutiniu OH5IY slopinimu** (200 dB ties 144 MHz, perskaičiuota pagal λ³ pasirinktai juostai). Straipsnio duomuo: reikia apie **70 dBm EIRP** (−130 dBm + 200 dB, pvz., apie 400 W į 14 dBi anteną).

## Antenos stiprinimas ir lapelis

**Stiprinimas – šaltinis:** Günter Hoch **DL6WU** kreivė ilgosioms Yagi antenoms kaip strėlės ilgio L funkcija, pateikta W8IO (galioja nuo maždaug 2 λ) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Patikra pagal L.B. Cebik W4RNL NEC modelius ties 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementai | Strėlė (λ) | W4RNL NEC (dBi) | Formulė (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Skirtumas niekada neviršija **0,1 dB**: stiprinimas labiau priklauso nuo strėlės ilgio nei nuo konstrukcijos (VK3AUU Yagi su tuo pačiu elementų skaičiumi turi trumpesnę strėlę). VK5DJ Yagi Calculator taip pat pateikia įverčius VK3AUU, WA2PHW ir DJ9BV variantams, kurių formulės nepaskelbtos.

**Lapelis – šaltinis:** Krauso taisyklė su apskritu lapeliu θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Patikra:** W4RNL DL6WU Yagi NEC modeliai duoda **5–10 % siauresnį horizontalųjį lapelį** nei Krausas: 33,8° / 26,4° / 22,6° 12, 19 ir 26 elementams, palyginti su 37,3° / 28,0° / 23,9°. Paprastos formulės neatsižvelgia į priekinius šoninius lapelius (W4RNL, *Long-Boom Yagi Rules of Thumb*). Ilgose strėlėse vertikalusis lapelis šiek tiek platesnis už horizontalųjį (14 λ: 18,4° / 18,8°).

**Sprendimas** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Pavyzdys: 14 λ Yagi ties 432 MHz → 20,3 dBi, lapelis 18,1° horizontaliai ir 19,5° vertikaliai; W4RNL modeliai duoda 20,4 dBi ir 18,4° / 18,8°. Tai apytikslės taisyklės, išvestos iš kelių DL6WU antenų.

Laikoma, kad antena visada nukreipta į DX. Hot spot yra **lapelio viduje**, jei |Az(Hot) − Az(antena)| ≤ θ_horizontalus/2: tada [Dangaus skliaute](Sky-View-lt) jis piešiamas pilkai ir pasirodo įspėjimas. Efektyvumo skaičiavime antenos izotropinės; tikrasis lapelis naudojamas tik šiai patikrai.

## Eksperimentinės taisyklės tarp juostų

Palyginti su 144 MHz: skaičius/intensyvumas × (144/f)³ (dB), trukmė × (144/f)² (SM6FHZ, VUSHF 2025). IARU 1 regiono didžiausia atspindžio trukmė: 1000 ms ties 50 MHz, 500 ms ties 70 MHz, 100 ms ties 144 MHz, 13 ms ties 432 MHz (VHF Handbook, cituojama straipsnyje). Taip pat žr. [Eksperimentinės prognozės](Experimental-Forecasts-lt).
