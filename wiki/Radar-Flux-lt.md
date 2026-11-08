**English** · [Русский](Radar-Flux-ru) · [Deutsch](Radar-Flux-de) · [日本語](Radar-Flux-ja)

# Radaro srautas

*Kortelė: Tiesiogiai ir realiojo laiko duomenys › Radaro srautas.*

[![Radaro srautas](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Ši kortelė rodo, ką profesionalūs meteorų radarai skaičiuoja **dabar**: **Collm** SKiYMET radaro (Leipcigo universitetas / IAP Kühlungsborn, Vokietija, 36,2 MHz) valandinius meteorų skaičius ir pėdsakų aukščius bei naujausią **Sodankylä** radaro (SGO, Suomija) vaizdą. Collm skaičiai naudojami jūsų juostos įverčiui ir [Eksperimentinėms prognozėms](Experimental-Forecasts-lt); išmatuotas pėdsakų aukštis naudojamas visoje geometrijoje.

## Valdikliai

| Valdiklis | Ką daro |
|---|---|
| **Atsisiųsti dabar** | Iš karto patikrina visus išorinius šaltinius. |
| **Visų šaltinių automatinis atnaujinimas kas 5 minutes** | Įjungta pagal nutylėjimą. Kas 5 minutes tikrinami visi šaltiniai ir iš naujo atsisiunčiami **tik pasikeitę** (*nepakito (tikrinta … UTC)* / *nauji duomenys … UTC*). |
| **λ rodiklis (SM6FHZ)** | Dažnio taisyklės rodiklis k, numatytasis 3 (1–4). |

## Kas rodoma

| Skydelis | Turinys |
|---|---|
| **Meteorai/val. – vakar ir šiandien (UTC)** | Žydri stulpeliai = Collm skaičiai (galiojantys), raudoni stulpeliai = atmesti, stora oranžinė linija = *įvertis ties … MHz* dešinėje skalėje |
| **Pėdsakų aukščiai (Collm)** | Meteorai aukščio kilometrui nuo 70 iki 110 km, su dažniausiu aukščiu (moda), vidurkiu, mediana ir standartiniu nuokrypiu |
| Collm vaizdas | Originalus SKiYMET grafikas, toks, koks atsisiųstas |
| Sodankylä vaizdas | Naujausias Sodankylä radaro meteorų skaičiaus vaizdas (tik rodomas; jo formatas neskaitomas) |

Eilutė virš grafikų nurodo, kada buvo nuskaitytas Collm grafikas ir kokia vertikali skalė rasta (*skalė, nuskaityta iš grafiko: 0-… meteorų/val.*).

## Kaip skaitomas Collm grafikas

Collm grafiko (720 × 720 pikselių, grynos spalvos) ašių padėtys fiksuotos, bet radaras **kasdien pritaiko vertikalią skalę** išmatuotoms vertėms (pvz., 0–1,2·10³ 2026-11-05 ir 0–1,0·10³ 2026-11-06, su paslinktomis padalomis). Todėl YA-MS:

1. randa ilgąsias ašies padalas;
2. **nuskaito aukščiausios padalos ir nulio užrašus**, lygindama kiekvieną simbolį su grafiko taškinės matricos šriftu;
3. kiekvienai valandai i (0–47, vakar ir šiandien) ima vidurinį stulpelį ir pirmą žydrą pikselį iš viršaus, y:

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top ir y0 – aukščiausios padalos ir nulio eilutės, N_top – aukščiausiame užraše nuskaityta vertė (×1000). Skiriamoji geba: apie 7–8 meteorai/val. vienam pikseliui. *Programos sprendimas (vadovo 42 lygtis).*

Jei užrašo nuskaityti nepavyksta, programa naudoja 2026-11-05 kalibravimą (**kalibruota skalė 0-1200 meteorų/val.**) ir praneša apie tai oranžine spalva: *Nepavyko nuskaityti vertikalios srauto skalės (viršutinė žymė: …): vertes reikia patikrinti.* Jei pasikeičia pats grafiko formatas (*Pasikeitė grafiko formatas (…x…): nuskaityti negalima* arba *Srauto ašys nerastos numatytoje vietoje*), skaitymą reikia iš naujo kalibruoti: praneškite apie tai (žr. [Prisidėjimas](Contributing-and-Contacts-lt)).

### Pėdsakų aukščiai

Iš aukščių histogramos (n_k meteorų k-ajame kilometre, vidutinis aukštis h_k):

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*Vadovo 43 lygtis.* Pažymėjus **iš radaro** (2 valdymo eilutė), **moda** tampa visų skaičiavimų pėdsakų aukščiu. Patikra: 2026-11-05 grafikas – moda 89,5 km, vidurkis 88,6 km, standartinis nuokrypis 6,8 km, patvirtina Cerrotta–Sartori straipsnio ~90 km (SKiYMET vidurkis).

Jei pasikeičia aukščių grafiko skalė, programa įspėja: *aukščių statistika (moda, vidurkis, mediana) lieka galioti, absoliutūs skaičiai – ne.*

## Įvertis jūsų juostai

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

**SM6FHZ** eksperimentinės taisyklės (VUSHF 2025): atspindžių skaičius ir intensyvumas kinta pagal λ³, trukmė – pagal λ²; λ³ priklausomybė ta pati kaip McKinley retojo pėdsako lygtyje. Taip pat rodoma IARU 1 regiono didžiausia atspindžio trukmė (1000 ms ties 50 MHz, 500 ms ties 70 MHz, 100 ms ties 144 MHz, 13 ms ties 432 MHz). Vertės orientacinės, lygintinos su patirtimi eteryje. Stoties koeficientas K ir palyginimas su RMOB pateikti puslapyje [Eksperimentinės prognozės](Experimental-Forecasts-lt).

## Be tinklo

Jei nepasiekiamas nė vienas šaltinis, **vieną kartą** pasirodo pranešimas: *Nėra interneto ryšio. Radarų ir RMOB duomenų atnaujinti negalima: programa naudoja paskutinius išsaugotus duomenis ir pati bando iš naujo kas 5 minutes.* Būsenos juosta apačioje tampa raudona (*NĖRA INTERNETO RYŠIO …*), kol ryšys atsistato (*Ryšys atkurtas.*).

## Archyvai ir šaltiniai

| Failas (aplanke `data/`) | Turinys |
|---|---|
| `flusso_collm.csv` | Iš Collm nuskaityto srauto valandinis archyvas (jau esančios valandos atnaujinamos) |
| `quote_collm.csv` | Pėdsakų aukščių archyvas |
| `radar/` | Naujausi atsisiųsti vaizdai (ir RMOB failai) |
| `fonti_radar.csv` | Radarų šaltinių adresai, `attivo=1/0` kiekvienam įjungti/išjungti |

| Šaltinis | Dažnis | Pastabos |
|---|---|---|
| Collm meteorų radaras, Leipcigo universitetas (LIM) ir IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | atnaujinamas kas valandą 10 minutę UTC; srautas vakar + šiandien, aukščių pasiskirstymas |
| Sodankylä geofizikos observatorija – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | tik vaizdas (radaras atnaujinamas, projektas DECC) |
| swan.ms (Collm kopija) | 36,2 MHz | išjungta pagal nutylėjimą; naudoti tik gavus DL1DBC leidimą |

> Radarų duomenys priklauso atitinkamoms institucijoms (Leipcigo universitetas / IAP Kühlungsborn, Sodankylä geofizikos observatorija).
