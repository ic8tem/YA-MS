**English** · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh)

# Showers

*Tab: Showers.*

[![Showers](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

The shower catalogue used by all calculations: **45 showers** from the **IMO Meteor Shower Calendar 2026 and 2027** (tables 5 and 7) plus the **Antihelion Source** (table 6), each with its **next peak**.

## Columns

| Column | Meaning |
|---|---|
| Code | IMO code (QUA, PER, GEM, …) |
| Shower | Name |
| Activity | Activity period (day/month – day/month) |
| λ max | Solar longitude of the peak (J2000), from IMO |
| **Next peak (UTC)** | Date and time of the next peak (see below) |
| **Peak source** | *IMO 2026* / *IMO 2027* = date and time published by the IMO; *IMO 2026 (day)* = the IMO gives only the day, the time shown is calculated (*~hh:mm calc.*); *calculated from λ* = no IMO value for that year |
| R.A., Dec. | Radiant at the peak (*moving* for the Antihelion Source) |
| v km/s, r | Geocentric speed and population index |
| ZHR | Peak ZHR (*var.* = variable) |
| Type | *visual* or *radio, daytime* |
| Active today | *yes* when the shower is active now |

## Next peak

The program always shows the **next** peak. When the IMO has published that year's calendar it uses the **IMO date and time** from `data/massimi_imo.csv` (2026 and 2027 are included); otherwise it computes the instant at which the Sun reaches the solar longitude of the peak (Meeus, *Astronomical Algorithms*, ch. 25, solved with Newton's method).

**Check:** the calculation agrees with the IMO 2026 and 2027 calendars within a few minutes where the IMO gives the time (e.g. Quadrantids 3/1/2026 21:13 against 21:00; Geminids 14/12/2027 19:51 against 20:00). Exceptions: Daytime kappa Leonids 2026 one day later (26/9 instead of 25/9) and the time of the eta Aquariids 2027 (15:10 against 09:00 IMO) – in these cases the IMO value is used.

**Adding a year:** when the IMO publishes a new calendar, add its rows to `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, time empty if the IMO gives only the day). Until then the peak is calculated.

## Minor and daytime showers

The catalogue includes the **minor showers** of the IMO list – for example the October Camelopardalids (OCT, ZHR 5, active 5–6 October), the Andromedids, the gamma Ursae Minorids – and the **daytime radio showers** of April–October (Daytime April Piscids, Daytime Arietids, Daytime zeta Perseids, Daytime beta Taurids, Daytime kappa Leonids, Daytime Sextantids, …). Even with small ZHRs they contribute to the [path index](Efficiency-Calculation#the-model) and to the [recommended Hot](Sky-View#recommended-hot). For the daytime radio showers the IMO gives no ZHR: where none is given the program uses a working value of 5.

## Activity profile and radiant drift

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

ZHR_max, α0, δ0 and λ_max from the IMO calendar; the slopes B (different before and after the peak) and the daily drifts dα/dλ, dδ/dλ are **working values** written in `data/sciami.csv` (the IMO drift table has not been entered yet). *Manual eq. 9 and 13.* The Antihelion Source position is interpolated linearly between the dates of IMO table 6 (`data/ant_radiante.csv`; active 10 December – 20 September, ZHR about 4).

## Editing the catalogue

`data/sciami.csv` is a plain text file (separator `;`) that you can edit: code, name, start and end (MM-DD), λ max, R.A., Dec., drifts, v, r, ZHR, B before/after, type (V visual, R daytime radio). If a line is wrong the program shows a message at start-up and ignores it.

Sources: International Meteor Organization – Meteor Shower Calendar 2026 and 2027, [www.imo.net](https://www.imo.net) (tables 5, 6 and 7); Philip G0ISW (maximum radio hourly rates); Rossano IZ5TEK (scattertek).
