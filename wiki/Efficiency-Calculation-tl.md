[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · **Tagalog** · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh)

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

Ang parehong batas ang pinagbabatayan ng QTFGUI ni DJ5HG (cone scattering). Tinatanggap ang kondisyon nang may Gaussian na tolerance na σ = 0.05 rad (mga 3°) – *pagpili ng programa*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Timbang ng bawat punto.** Lakas ng isang underdense na bakas (McKinley), φ = kalahati ng scattering angle (limitado sa 85°, *pagpili*):

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad w_P = \frac{1}{R_1 R_2 (R_1+R_2)\cos^2\varphi}
```

Proporsiyonal ang bilang ng meteor na umaabot sa isang punto sa sine ng elebasyon ng radiant doon (ŝ·û_P), ang parehong koreksiyon na ginagamit ng IMO para sa ZHR.

**3. Kabuuan at porsiyento.** Mga punto bawat 15 km sa taas ng bakas, kung saan lamang nakikita ito ng dalawang istasyon sa itaas ng elebasyon ng lobe (*pagpili*). Ang 100 % ay ang pinakapaborableng posisyon ng radiant para sa landas na iyon:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

Kinakalkula ang F nang isang beses bawat landas sa isang grid ng mga direksiyon (azimuth bawat 5°, elebasyon bawat 2.5°) at ini-interpolate.

**4. Panig at indeks.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Ang titik sa talahanayan ay ang panig na may mas malaking bahagi. *Mga pagpili ng programa (manwal eq. 32–33).*

## Paghahambing sa DH9GCD

Isang malayang pagsusuri: ang pormula ng pinakamahusay na direksiyon ni **DH9GCD**, ayon sa ulat ni **DF5HC** (kumperensiya ng DARC, Enero 2018), kung saan ang El at Az ay ang elebasyon at azimuth ng radiant mula sa iyong istasyon at ang P ay ang azimuth ng DX station:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Pinakamataas ito kapag ang radiant ay nasa 45° at nakapahalang sa landas. Itinuturing ni DF5HC na masyadong mababa ang radiant sa ilalim ng 20° at **masyadong mataas sa itaas ng 70°**: nakakakuha ng ↑ ang mga oras na ito sa talahanayan at isang babala sa [Kalangitan](Sky-View-tl#mga-babala). Hindi isinasaalang-alang ng pormula ang distansiya at mga taas, pero mahusay itong sanggunian.

## Mga pagsusuri

| Pagsusuri | Resulta |
|---|---|
| Tuntunin ni SM6FHZ (VUSHF 2025): pinakamahusay na landas na orthogonal sa azimuth ng radiant, tutok = az ng radiant ±90°, tolerance ±40–50° | Nagagaya ng modelo; kapag nakahanay ang radiant sa landas at mataas sa langit, halos zero ang episyensya |
| QTFGUI ni DJ5HG, Hamburg JO53IM – Barcelona, Quadrantids, 4 Enero (halimbawa ng manwal nito) | QTFGUI: 07:00 tutok 252°, −8 dB; 08:00 walang sona ng repleksiyon; 09:00 tutok 168°, −4 dB. YA-MS (taas 102 km gaya ng QTFGUI): 07:00 241°, −5.4 dB; 08:00 0.6 % (−22 dB); 09:00 161°, −4.0 dB. DH9GCD: 26 %, 2 %, 32 %. Nakikita ng tatlong pamamaraan ang butas sa 08:00, kung kailan halos nasa zenith ang radiant |
| Pag-sample bawat 5 km sa halip na 15 km | nagbabago ang mga porsiyento nang mas mababa sa 0.3 puntos |

> Hindi alam nang detalyado ang iskalang ginamit ng OH5IY at MCG_MS (hindi available ang mga manwal ng MS-Soft): ihambing ang mga porsiyento sa mga programang iyon bago ituring na katumbas. Underdense na bakas lamang ang isinasaalang-alang ng modelo, na may isotropic na antenna; wala sa episyensya ang mga overdense na burst at ang sporadic na background (kinakatawan ng flux ng radar ang sporadic na background).
