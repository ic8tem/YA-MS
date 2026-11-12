[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · **Lietuvių** · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Efektyvumo skaičiavimas

*Kortelė: Prognozės skaičiavimas › Efektyvumo skaičiavimas.*

[![Efektyvumo skaičiavimas](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

Srauto **efektyvumas** procentais nurodo, kiek jo radianto padėtis leidžia atspindžius **jūsų** trasoje. Sąvoką sukūrė Ilkka **OH5IY** (MS-Soft), ją perėmė Cerrotta–Sartori straipsnis: efektyvumo maksimumas nesutampa su vizualiuoju maksimumu (ZHR), nes jis priklauso nuo radianto padėties dviejų stočių atžvilgiu. DL5MCG MCG_MS taiko tą pačią idėją keturioms fiksuotoms kryptims; YA-MS jį skaičiuoja **realiai trasai** tarp dviejų lokatorių.

Ši kortelė rodo jį kas valandą dienai, pasirinktai lauke *Skaičiavimo data (UTC)* (vertės kiekvienos valandos viduryje).

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

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Tas pats dėsnis yra DJ5HG QTFGUI ir jo teksto *"Die Geometrie von Meteorscatterverbindungen"* (2004) pagrindas: pėdsakas sklaido kūgiu, kurio ašis yra pats pėdsakas, ir jį girdi tik ant kūgio esantis imtuvas. Idealaus pėdsako kūgio sienelė labai plona (tūkstančių bangos ilgių ilgio spinduolis); programa priima sąlygą su Gauso tolerancija σ = 0,05 rad (apie 3°), kuri atspindi tai, ko idealus kūgis nemato: srautų radiantų sklaidą (0,3–1,4° pagal GMN matavimus), vėjo išlenktus pėdsakus ir jų baigtinį ilgį – *programos sprendimas*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Kiekvieno taško svoris.** Retojo pėdsako galia (McKinley; ITU-R P.843, 3 lygtis), φ = pusė sklaidos kampo (apribota 85°, *sprendimas*), β = kampas tarp pėdsako ir sklidimo plokštumos A-P-B, p̂ = tos plokštumos vienetinė normalė:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Parinktis „β kampas tarp pėdsako ir trasos (visa McKinley formulė)“** (numatytai įjungta, atsargus nustatymas). Įjungta: sklidimo plokštumą kertantys pėdsakai yra 10–15 dB mažiau vertingi nei joje gulintys, todėl nė vienas pėdsakas nepervertinamas. Išjungta: kiekvienas pėdsakas sveriamas taip, lyg gulėtų plokštumoje (β = 0, svoris su cos²φ), kaip iki 1.6 versijos. *Patikra:* 1000 km trasoje be β geriausias radianto azimutas yra 15°–90° nuo trasos, priklausomai nuo radianto elevacijos (30°, kai radiantas 30° aukštyje, statmenai trasai, kai radiantas 60° aukštyje), o statmenas radiantas esant 30° elevacijai vertas 67 %; su β geriausias radiantas visada yra išilgai trasos, o statmenasis nukrinta iki 15 %. Su β prarandama SM6FHZ / DH9GCD geriausios krypties taisyklė; β lieka parinktis, numatytai įjungta, nes duoda atsargiausias vertes, o ją išjungus taisyklė grįžta.

Į tašką patenkančių meteorų skaičius proporcingas radianto elevacijos ten sinusui (ŝ·û_P) – ta pati pataisa, kurią IMO taiko ZHR.

**Parinktis „Ilgesni pėdsakai esant žemam radiantui (DJ5HG)“** (žymimasis langelis virš diagramos, numatytai išjungtas, su paaiškinimu): DJ5HG pastebi, kad esant žemam radiantui į km² krenta mažiau meteorų, bet pėdsakai ilgesni (iki 100 km naudingo ilgio) ir dažniau tenkina atspindžio dėsnį. Įjungus parinktį, svoris tampa min(sin El, 15/100): naudingas sluoksnio storis, 15 km, padalytas iš elevacijos sinuso, duoda pėdsako ilgį, apribotą iki 100 km. Virš maždaug 9° abu efektai vienas kitą kompensuoja. Išjungus skaičiavimas lieka atsargus.

**Skaičiavimo nustatymas** (toje pačioje eilutėje, pasirinkimo mygtukai): **Atsargus** (numatytasis, atsargiausios vertės: pėdsakų aukštis iš radaro, įprasti pėdsakai, β įjungta), **Kaip DJ5HG** (102 km, ilgesni pėdsakai, β) ir **Pasirinktinis**, kuris parenkamas automatiškai, kai rankiniu būdu pakeičiate aukštį, langelį *iš radaro*, ilgesnių pėdsakų parinktį arba β.

**3. Suma ir procentas.** Taškai kas 15 km pėdsakų aukštyje, kuriuos abi stotys mato virš horizonto ir kurie sveriami abiejų antenų vertikaliąja diagrama (langelis *antenos diagrama*, numatytasis įjungtas; išjungus tik taškai virš skilties pakilimo) (*pasirinkimas*). 100 % yra palankiausia radianto padėtis tai trasai:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F apskaičiuojama vieną kartą kiekvienai trasai krypčių tinkle (azimutas kas 5°, elevacija kas 2,5°) ir interpoliuojama.

**Efektyvumas dB (DJ5HG atskaita).** Procentai yra santykiniai tik su geriausia radianto padėtimi tai trasai. Kad būtų galima palyginti skirtingas trasas, programa pateikia ir efektyvumą dB, palyginti su fiksuota DJ5HG atskaita: 0 dB yra 1000 km šiaurės–pietų trasos, kertančios pusiaujį, maksimumas, kai radiantas lygiadienio metu yra dangaus pusiaujyje, apskaičiuotas su tuo pačiu aukščiu ir tais pačiais svoriais. DJ5HG nurodo, kad jo vertės tikslesnės nei 6 dB.

**4. Pusė ir indeksas.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Lentelės raidė – pusė su didesne dalimi. *Programos sprendimai (vadovo 32–33 lygtys).*

## DH9GCD palyginimas

Pirminiai geriausios krypties šaltiniai yra Eshleman & Mlodnosky ir Meeks & James (Proc. IRE, 1957), Hines (1955) bei jo eksperimentinė patikra, atlikta Forsyth, Hines & Vogan (1955): naudingi tik radiantai, esantys dangaus pusapskritimyje, statmename sklaidos kampo pusiaukampinei, pėdsakų skaičius auga su sin El, o netoli vidurio taško naudingi pėdsakai krenta maždaug H·tan El į šoną, priešingoje radiantui pusėje. DJ5HG daro išlygą: kai **žemas** radiantas yra tiksliai išilgai trasos, McKinley formulė duoda stiprius signalus (Hamburgas–Narvikas, Kvadrantidai, apie 19 UTC), todėl „radiantas išilgai trasos = beveik nulis“ galioja tik aukštam radiantui; programa lieka atsargi ir rodo įspėjimą *ŽEMAS RADIANTAS IŠILGAI TRASOS*.

Nepriklausoma patikra: **DH9GCD** geriausios krypties formulė, pateikta **DF5HC** (DARC konferencija, 2018 m. sausis) – paskelbto pirminio šaltinio ji neturi – kur El ir Az – iš jūsų stoties matomo radianto elevacija ir azimutas, o P – korespondento azimutas:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Ji didžiausia, kai radiantas yra 45° aukštyje ir statmenai trasai. DF5HC laiko radiantą per žemu žemiau 20° ir **per aukštu virš 70°**: šios valandos lentelėje gauna ↑, o [Dangaus skliaute](Sky-View-lt#įspėjimai) – įspėjimą. Formulė neatsižvelgia į atstumą ir aukščius, bet yra geras atskaitos taškas.

## Patikros

| Patikra | Rezultatas |
|---|---|
| SM6FHZ taisyklė (VUSHF 2025): geriausia trasa statmena radianto azimutui, nukreipimas = radianto az ±90°, tolerancija ±40–50° | Modelis ją atkuria; kai radiantas sutampa su trasos kryptimi ir yra aukštai danguje, efektyvumas beveik nulinis |
| DJ5HG QTFGUI, Hamburgas JO53IM – Barselona, Kvadrantidai, sausio 4 d. (jo vadovo pavyzdys) | QTFGUI: 07:00 nukreipimas 252°, −8 dB; 08:00 nėra atspindžio zonos; 09:00 nukreipimas 168°, −4 dB. YA-MS (aukštis 102 km kaip QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Visi trys metodai mato 08:00 „skylę“, kai radiantas beveik zenite |
| DJ5HG kreivės (*Die Geometrie…*, Bild 8–9: iš Hamburgo ir Miuncheno, Kvadrantidai, sausio 4 d.; nuskaitytos iš grafiko, maždaug ±0,5 dB ir ±15 min) palyginti su automatiniu testu `--prova-dj5hg` (viena vertė per valandą) | Laikas: duobė, kai radiantas arti zenito, išpuola tomis pačiomis valandomis (Barselona 07:30–08:30 prieš 07–09; Sofija 06:36–07:48 prieš 07–08; Narvikas 07–08:30 prieš 07–09); Maskva abiem atvejais uždara 03–10, atvira iš Hamburgo iki maždaug 02:30 ir iš Miuncheno iki maždaug 00:30, kaip rašo DJ5HG. Kryptys: 2–10° skirtumas. Lygiai ir forma esant 102 km (vidutinis ir RMS skirtumas nuo kreivių): be β, be ilgesnių pėdsakų −1,6 / 4,0 dB; ilgesni pėdsakai +1,1 / 4,6 dB; β −5,4 / 6,2 dB, bet su geriausia forma (3,0 dB atėmus vidurkį, palyginti su 3,6): atsiranda gilūs minimumai esant žemam radiantui (Barselona −15,6 dB 17 val. prieš −16 dB 19:36; Sofija −18,5 dB 20 val. prieš −14 dB). β ir ilgesni pėdsakai (*Kaip DJ5HG*) −2,2 / 4,7 dB; atsargus nustatymas (radaro aukštis 89,5 km, β įjungta, be ilgesnių pėdsakų) −6,9 / 7,6 dB, forma 3,3 dB. Be β YA-MS vos parodo minimumą, kai radiantas žemas ir beveik išilgai trasos (−8,6 ir −10,4 dB): tai paties DJ5HG išlyga, todėl ir įspėjimas |
| Diskretizavimas kas 5 km vietoj 15 km | procentai pasikeičia mažiau nei 0,3 punkto |

> MS-Soft 5.2 dokumentacija apibrėžia OH5IY efektyvumą kaip santykinį indeksą tik retiesiems pėdsakams, su dviem veiksniais (radianto elevacija, geriausia apie 45°, ir kampas su trasa, geriausias 90°) ir minimumu, ranka pakeltu iki 20 % tankiesiems pėdsakams; formulė nepaskelbta. MCG_MS jį skaičiuoja keturioms fiksuotoms kryptims ir, nurodžius DX lokatorių, tikrajai trasai. Modelis vertina tik retuosius pėdsakus su izotropinėmis antenomis; tankiųjų pėdsakų žybsniai ir sporadinis fonas į efektyvumą neįtraukti (sporadinį foną atspindi radaro srautas). Nuo 1.8.1, kai langelis «antenos diagrama» įjungtas, taikoma vertikalioji antenų diagrama; azimute antenos lieka izotropinės.
