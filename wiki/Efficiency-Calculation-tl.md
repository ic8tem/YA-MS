[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · **Tagalog** · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Kalkulasyon ng episyensya

*Tab: Kalkulasyon ng pagtataya › Kalkulasyon ng episyensya.*

[![Kalkulasyon ng episyensya](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

Sinasabi ng **episyensya** ng isang shower, sa porsiyento, kung gaano pinahihintulutan ng posisyon ng radiant nito ang mga repleksiyon sa **iyong** landas. Ang konsepto ay kay Ilkka **OH5IY** (MS-Soft) at ginamit sa artikulong Cerrotta–Sartori: hindi nagkakasabay ang peak ng episyensya at ang biswal na peak (ZHR), dahil nakadepende ito sa kinaroroonan ng radiant kaugnay ng dalawang istasyon. Ginagamit ng MCG_MS ni DL5MCG ang parehong ideya sa apat na nakapirming direksiyon; kinakalkula ito ng YA-MS para sa **totoong landas** sa pagitan ng dalawang locator.

Ipinapakita ito ng tab na ito bawat oras para sa araw na pinili sa *Araw para sa 24 h na talahanayan (UTC)* (mga halaga sa kalahating oras).

## Mga card na mabilisang tingnan

| Card | Nilalaman |
|---|---|
| **PINAKAMAHUSAY NA ORAS NG ARAW** | Ang oras na may pinakamataas na indeks ng landas, ang indeks at ang nangingibabaw na panig (A/B kasama ang %) |
| **PINAKAPABORABLENG SHOWER** | Ang shower na may pinakamalaking ZHR × episyensya sa araw na iyon, ang episyensya, oras at panig nito, at ang **pinakamahusay na tutok** (azimuth ng radiant +90° / −90°) |
| **NGAYON** | Indeks at nangingibabaw na panig sa oras na ito, at ang inirerekomendang Hot (kapag ngayon lamang ang napiling araw) |
| **EKSPERIMENTAL NA PAGTATAYA** | Inaasahang repleksiyon/oras ngayon, sa loob ng 1 h at 2 h sa frequency ng pagtataya (Collm, mga tuntunin ni SM6FHZ; tingnan ang [Eksperimental na pagtataya](Experimental-Forecasts-tl)) |

Sa ilalim ng mga card, ipinapaliwanag ng isang banda ang mga titik na A at B (tingnan sa ibaba).

## Graph

*Episyensya bawat oras para sa … sa … (UTC, halaga sa kalahating oras).* Para sa hanggang limang shower: episyensya % bilang buong linya at ang pormula ng DH9GCD bilang tuldok-tuldok na linya ng parehong kulay; ang **indeks ng landas** bilang mga asul na bar sa iskala sa kanan.

## Talahanayan bawat oras

Isang hanay bawat shower na aktibo sa araw na iyon (nakaayos ayon sa ZHR), 24 na column para sa mga oras (UTC):

| Cell | Kahulugan |
|---|---|
| `63A` | episyensya 63 %, karamihan ng repleksiyon mula sa panig **A** |
| `41B` | episyensya 41 %, panig **B** |
| `3` | episyensyang mas mababa sa 5 %: numerong walang titik ng panig |
| walang laman | episyensyang mas mababa sa 1 % |
| `…↑` | ang radiant ay **higit sa 70°** mula sa iyong istasyon sa oras na iyon (masyadong mataas) |
| dilaw na teksto | episyensya ≥ 50 % |

- **A** = **kaliwa** kung titingin mula sa iyong istasyon patungo sa DX station (sona ng Hot A); **B** = **kanan** (sona ng Hot B). Sulit na ipihit ang antenna nang **10–30° patungo sa panig na iyon** (side-scatter, artikulong Cerrotta–Sartori).
- **Mga hanay na mapusyaw na asul** (*DH9GCD %*, sa ilalim ng bawat shower): ang pormula ng DH9GCD, para sa paghahambing.
- **Hanay na Σ**: *Indeks ng landas (ZHR×epis.)*.
- **Kahel na hanay** (*Pagtataya … MHz (repl./oras)*): ang eksperimental na pagtataya, para sa mga oras na mayroon nito (ngayon at bahagi ng bukas).

## Ang modelo

Nasa [manwal ng kalkulasyon](Efficiency-Explanation-tl) ang lahat ng hakbang (`doc/YA-MS_manuale_calcoli.docx`, kabanata 5). Sa madaling salita:

**1. Specular na repleksiyon.** Ipinapadala ng isang bakas ang signal mula A patungong B kung tangent lamang ito sa isang ellipsoid na nasa foci ang A at B (McKinley 1961). Parallel sa direksiyon ng radiant ŝ ang mga bakas ng isang shower (artikulo; McKinley). Para sa bawat punto P ng E layer, gamit ang mga unit vector patungo sa mga istasyon:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Ang parehong batas ang pinagbabatayan ng QTFGUI ni DJ5HG at ng kanyang sulatin na *"Die Geometrie von Meteorscatterverbindungen"* (2004): ikinakalat ng bakas ang signal sa isang kono na ang aksis ay ang bakas mismo, at tanging ang receiver na nasa kono ang nakaririnig dito. Para sa isang ideyal na bakas, napakanipis ng pader ng kono (isang radiator na libu-libong wavelength ang haba); tinatanggap ng programa ang kondisyon nang may Gaussian na tolerance na σ = 0.05 rad (mga 3°), na kumakatawan sa hindi nakikita ng ideyal na kono: ang pagkalat ng mga radiant ng mga shower (0.3–1.4° ayon sa sukat ng GMN), mga bakas na binaluktot ng hangin at ang kanilang may-hangganang haba – *pagpili ng programa*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Timbang ng bawat punto.** Lakas ng isang underdense na bakas (McKinley; ITU-R P.843, eq. 3), φ = kalahati ng scattering angle (limitado sa 85°, *pagpili*), β = anggulo sa pagitan ng bakas at ng propagation plane na A-P-B, p̂ = unit normal ng planong iyon:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Opsiyong "Anggulong β sa pagitan ng bakas at landas (buong McKinley)"** (naka-on bilang default, maingat na setting). Naka-on: ang mga bakas na tumatawid sa propagation plane ay 10–15 dB na mas mababa ang halaga kaysa sa mga nakahiga rito, kaya walang bakas na sobrang tinataya. Naka-off: tinitimbang ang bawat bakas na para bang nasa plane ito (β = 0, timbang na may cos²φ), gaya hanggang bersiyon 1.6. *Pagsusuri:* sa landas na 1000 km, kung walang β ang pinakamahusay na azimuth ng radiant ay 15°–90° mula sa landas depende sa elebasyon ng radiant (30° kapag nasa 30° ang radiant, patayo sa landas kapag nasa 60°), at ang radiant na patayo sa landas ay may halagang 67 % sa elebasyong 30°; kapag may β, ang pinakamahusay na radiant ay laging nasa kahabaan ng landas at bumababa sa 15 % ang patayo. Kapag may β, nawawala ang tuntunin ng pinakamahusay na direksiyon ng SM6FHZ / DH9GCD; nananatiling opsiyon ang β, naka-on bilang default dahil ito ang nagbibigay ng pinakamaingat na halaga, at bumabalik ang tuntunin kapag pinatay ito.

Proporsiyonal ang bilang ng meteor na umaabot sa isang punto sa sine ng elebasyon ng radiant doon (ŝ·û_P), ang parehong koreksiyon na ginagamit ng IMO para sa ZHR.

**Opsiyong "Mas mahahabang bakas kapag mababa ang radiant (DJ5HG)"** (checkbox sa itaas ng tsart, naka-off bilang default, may tooltip): Sinasabi ni DJ5HG na kapag mababa ang radiant, mas kaunting meteor ang bumabagsak bawat km², ngunit mas mahahaba ang mga bakas (hanggang 100 km na magagamit) at mas madalas na tumutugon sa batas ng repleksiyon. Kapag naka-on ang opsiyon, ang timbang ay nagiging min(sin El, 15/100): ang magagamit na kapal ng layer, 15 km, na hinati sa sine ng elebasyon ay nagbibigay ng haba ng bakas, na may limitasyong 100 km. Sa itaas ng mga 9°, nagkakansela ang dalawang epekto. Kapag naka-off, nananatiling maingat ang kalkulasyon.

**Setting ng kalkulasyon** (parehong hanay, radio button): **Maingat** (default, ang pinakamaingat na halaga: taas ng bakas mula sa radar, karaniwang bakas, naka-on ang β), **Gaya ni DJ5HG** (102 km, mas mahahabang bakas, β) at **Custom**, na awtomatikong napipili kapag mano-mano mong binago ang taas, ang kahong *mula sa radar*, ang opsiyon ng mas mahahabang bakas, o ang β.

**3. Kabuuan at porsiyento.** Mga punto bawat 15 km sa taas ng bakas, kung saan lamang nakikita ito ng dalawang istasyon sa itaas ng elebasyon ng lobe (*pagpili*). Ang 100 % ay ang pinakapaborableng posisyon ng radiant para sa landas na iyon:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

Kinakalkula ang F nang isang beses bawat landas sa isang grid ng mga direksiyon (azimuth bawat 5°, elebasyon bawat 2.5°) at ini-interpolate.

**Episyensya sa dB (reperensiya ni DJ5HG).** Ang porsiyento ay relatibo lamang sa pinakamahusay na posisyon ng radiant para sa landas na iyon. Upang maihambing ang iba't ibang landas, ibinibigay din ng programa ang episyensya sa dB kaugnay ng nakapirming reperensiya ni DJ5HG: ang 0 dB ay ang pinakamataas na halaga ng isang 1000 km na landas na hilaga–timog na tumatawid sa ekwador, na nasa celestial equator ang radiant sa equinox, na kinalkula gamit ang parehong taas at parehong mga timbang. Sinasabi ni DJ5HG na mas mahusay sa 6 dB ang kanyang mga halaga.

**4. Panig at indeks.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Ang titik sa talahanayan ay ang panig na may mas malaking bahagi. *Mga pagpili ng programa (manwal eq. 32–33).*

## Paghahambing sa DH9GCD

Ang mga pangunahing sanggunian para sa pinakamahusay na direksiyon ay sina Eshleman & Mlodnosky at Meeks & James (Proc. IRE, 1957), si Hines (1955) at ang eksperimental na pagsusuri nito nina Forsyth, Hines & Vogan (1955): magagamit lamang ang mga radiant na nasa kalahating bilog ng langit na patayo sa bisector ng anggulo ng scattering, dumarami ang mga bakas kasabay ng sin El, at malapit sa gitnang punto ay bumabagsak ang mga magagamit na bakas nang mga H·tan El patagilid, sa panig na kasalungat ng radiant. May idinagdag na pasubali si DJ5HG: kapag **mababa** ang radiant at eksaktong kahabaan ng landas, malalakas na signal ang ibinibigay ng pormula ni McKinley (Hamburg–Narvik, Quadrantids, mga 19 UTC), kaya ang "radiant na nakahanay sa landas = halos zero" ay totoo lamang para sa mataas na radiant; nananatiling maingat ang programa at ipinapakita ang babalang *MABABANG RADIANT SA KAHABAAN NG LANDAS*.

Isang malayang pagsusuri: ang pormula ng pinakamahusay na direksiyon ni **DH9GCD**, ayon sa ulat ni **DF5HC** (kumperensiya ng DARC, Enero 2018) – wala itong nailathalang pangunahing sanggunian – kung saan ang El at Az ay ang elebasyon at azimuth ng radiant mula sa iyong istasyon at ang P ay ang azimuth ng DX station:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Pinakamataas ito kapag ang radiant ay nasa 45° at nakapahalang sa landas. Itinuturing ni DF5HC na masyadong mababa ang radiant sa ilalim ng 20° at **masyadong mataas sa itaas ng 70°**: nakakakuha ng ↑ ang mga oras na ito sa talahanayan at isang babala sa [Kalangitan](Sky-View-tl#mga-babala). Hindi isinasaalang-alang ng pormula ang distansiya at mga taas, pero mahusay itong sanggunian.

## Mga pagsusuri

| Pagsusuri | Resulta |
|---|---|
| Tuntunin ni SM6FHZ (VUSHF 2025): pinakamahusay na landas na orthogonal sa azimuth ng radiant, tutok = az ng radiant ±90°, tolerance ±40–50° | Nagagaya ng modelo; kapag nakahanay ang radiant sa landas at mataas sa langit, halos zero ang episyensya |
| QTFGUI ni DJ5HG, Hamburg JO53IM – Barcelona, Quadrantids, 4 Enero (halimbawa ng manwal nito) | QTFGUI: 07:00 tutok 252°, −8 dB; 08:00 walang sona ng repleksiyon; 09:00 tutok 168°, −4 dB. YA-MS (taas 102 km gaya ng QTFGUI): 07:00 241°, −5.4 dB; 08:00 0.6 % (−22 dB); 09:00 161°, −4.0 dB. DH9GCD: 26 %, 2 %, 32 %. Nakikita ng tatlong pamamaraan ang butas sa 08:00, kung kailan halos nasa zenith ang radiant |
| Mga kurba ni DJ5HG (*Die Geometrie…*, Bild 8–9: mula sa Hamburg at Munich, Quadrantids, 4 Enero; binasa mula sa tsart, mga ±0.5 dB at ±15 min) laban sa awtomatikong pagsubok na `--prova-dj5hg` (isang halaga bawat oras) | Oras: ang butas kapag malapit sa zenith ang radiant ay nasa parehong mga oras (Barcelona 07:30–08:30 laban sa 07–09; Sofia 06:36–07:48 laban sa 07–08; Narvik 07–08:30 laban sa 07–09); sarado ang Moscow sa 03–10 sa dalawa, bukas mula Hamburg hanggang mga 02:30 at mula Munich hanggang mga 00:30, gaya ng isinulat ni DJ5HG. Direksiyon: 2–10° ang pagitan. Antas at hugis sa 102 km (karaniwan at RMS na pagkakaiba mula sa mga kurba): walang β, walang mas mahahabang bakas −1.6 / 4.0 dB; mas mahahabang bakas +1.1 / 4.6 dB; β −5.4 / 6.2 dB ngunit may pinakamahusay na hugis (3.0 dB matapos alisin ang average, laban sa 3.6): lumilitaw ang malalalim na minimum kapag mababa ang radiant (Barcelona −15.6 dB sa 17 laban sa −16 dB sa 19:36; Sofia −18.5 dB sa 20 laban sa −14 dB). β at mas mahahabang bakas (*Gaya ni DJ5HG*) −2.2 / 4.7 dB; ang maingat na setting (taas mula sa radar 89.5 km, naka-on ang β, walang mas mahahabang bakas) −6.9 / 7.6 dB, hugis 3.3 dB. Kung walang β, halos hindi ipinapakita ng YA-MS ang minimum kapag mababa ang radiant at halos nakahanay sa landas (−8.6 at −10.4 dB): ito ang mismong reserbasyon ni DJ5HG, kaya may babala |
| Pag-sample bawat 5 km sa halip na 15 km | nagbabago ang mga porsiyento nang mas mababa sa 0.3 puntos |

> Tinutukoy ng dokumentasyon ng MS-Soft 5.2 ang episyensya ng OH5IY bilang relatibong indeks para lamang sa underdense na bakas, na may dalawang salik (elebasyon ng radiant, pinakamahusay sa mga 45°, at anggulo sa landas, pinakamahusay sa 90°) at isang minimum na mano-manong itinaas sa 20 % para sa overdense na bakas; hindi nailathala ang pormula. Kinakalkula ito ng MCG_MS para sa apat na nakapirming direksiyon at, kapag may locator ng DX, para sa tunay na landas. Underdense na bakas lamang ang isinasaalang-alang ng modelo, na may isotropic na antenna; wala sa episyensya ang mga overdense na burst at ang sporadic na background (kinakatawan ng flux ng radar ang sporadic na background).
