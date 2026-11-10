[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · **Tagalog** · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh)

# Mga shower

*Tab: Mga shower.*

[![Mga shower](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Ang katalogo ng mga shower na ginagamit ng lahat ng kalkulasyon: **45 na shower** mula sa **IMO Meteor Shower Calendar 2026 at 2027** (mga talahanayan 5 at 7) pati ang **Antihelion Source** (talahanayan 6), bawat isa ay may **susunod na peak**.

## Mga column

| Column | Kahulugan |
|---|---|
| Kodigo | Kodigo ng IMO (QUA, PER, GEM, …) |
| Shower | Pangalan |
| Aktibidad | Panahon ng aktibidad (araw/buwan – araw/buwan) |
| λ max | Solar longitude ng peak (J2000), mula sa IMO |
| **Susunod na peak (UTC)** | Petsa at oras ng susunod na peak (tingnan sa ibaba) |
| **Pinagmulan ng peak** | *IMO 2026* / *IMO 2027* = petsa at oras na inilathala ng IMO; *IMO 2026 (araw)* = araw lamang ang ibinibigay ng IMO, kinalkula ang ipinapakitang oras (*~hh:mm kalk.*); *kinalkula mula sa λ* = walang halaga ng IMO para sa taong iyon |
| R.A., Dec. | Radiant sa peak (*gumagalaw* para sa Antihelion Source) |
| v km/s, r | Geocentric na bilis at population index |
| ZHR | Peak ZHR (*var.* = pabago-bago) |
| Uri | *biswal* o *radyo, sa araw* |

Naka-highlight na may dilaw na lambong at makapal na teksto ang mga shower na **aktibo ngayong araw (UTC)**.

## Susunod na peak

Laging ipinapakita ng programa ang **susunod** na peak. Kapag nailathala na ng IMO ang kalendaryo ng taong iyon, ginagamit nito ang **petsa at oras ng IMO** mula sa `data/massimi_imo.csv` (kasama ang 2026 at 2027); kung hindi, kinakalkula nito ang sandaling naaabot ng Araw ang solar longitude ng peak (Meeus, *Astronomical Algorithms*, kab. 25, nilutas gamit ang pamamaraan ni Newton).

**Pagsusuri:** tumutugma ang kalkulasyon sa mga kalendaryo ng IMO 2026 at 2027 sa loob ng ilang minuto kung saan ibinibigay ng IMO ang oras (hal. Quadrantids 3/1/2026 21:13 laban sa 21:00; Geminids 14/12/2027 19:51 laban sa 20:00). Mga eksepsiyon: Daytime kappa Leonids 2026 na isang araw na huli (26/9 sa halip na 25/9) at ang oras ng eta Aquariids 2027 (15:10 laban sa 09:00 ng IMO) – sa mga kasong ito, ginagamit ang halaga ng IMO.

**Pagdaragdag ng taon:** kapag naglathala ang IMO ng bagong kalendaryo, idagdag ang mga hanay nito sa `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, walang laman ang oras kung araw lamang ang ibinibigay ng IMO). Hanggang doon, kinakalkula ang peak.

## Maliliit na shower at mga shower sa araw

Kasama sa katalogo ang **maliliit na shower** ng listahan ng IMO – halimbawa ang October Camelopardalids (OCT, ZHR 5, aktibo 5–6 Oktubre), ang Andromedids, ang gamma Ursae Minorids – at ang **mga radio shower sa araw** ng Abril–Oktubre (Daytime April Piscids, Daytime Arietids, Daytime zeta Perseids, Daytime beta Taurids, Daytime kappa Leonids, Daytime Sextantids, …). Kahit maliit ang ZHR, nag-aambag sila sa [indeks ng landas](Efficiency-Calculation-tl#ang-modelo) at sa [inirerekomendang Hot](Sky-View-tl#inirerekomendang-hot). Para sa mga radio shower sa araw, walang ibinibigay na ZHR ang IMO: kung walang ibinigay, gumagamit ang programa ng working value na 5.

## Profile ng aktibidad at pag-usad ng radiant

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

Ang ZHR_max, α0, δ0 at λ_max ay mula sa kalendaryo ng IMO; ang mga slope na B (magkaiba bago at pagkatapos ng peak) at ang araw-araw na pag-usad na dα/dλ, dδ/dλ ay **mga working value** na nakasulat sa `data/sciami.csv` (hindi pa naipapasok ang talahanayan ng pag-usad ng IMO). *Manwal eq. 9 at 13.* Ini-interpolate nang linear ang posisyon ng Antihelion Source sa pagitan ng mga petsa ng talahanayan 6 ng IMO (`data/ant_radiante.csv`; aktibo 10 Disyembre – 20 Setyembre, ZHR mga 4).

## Pag-edit ng katalogo

Ang `data/sciami.csv` ay isang simpleng text file (separator na `;`) na maaari mong i-edit: kodigo, pangalan, simula at katapusan (MM-DD), λ max, R.A., Dec., pag-usad, v, r, ZHR, B bago/pagkatapos, uri (V biswal, R radyo sa araw). Kung mali ang isang linya, nagpapakita ang programa ng mensahe sa pagsisimula at hindi ito pinapansin.

Mga sanggunian: International Meteor Organization – Meteor Shower Calendar 2026 at 2027, [www.imo.net](https://www.imo.net) (mga talahanayan 5, 6 at 7); Philip G0ISW (pinakamataas na radio hourly rate); Rossano IZ5TEK (scattertek).
