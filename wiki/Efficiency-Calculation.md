**English** · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh)

# Efficiency calculation

*Tab: Forecast calculation › Efficiency calculation.*

[![Efficiency calculation](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

The **efficiency** of a shower says, in percent, how much the position of its radiant allows reflections on **your** path. The concept is by Ilkka **OH5IY** (MS-Soft) and is taken up in the Cerrotta–Sartori article: the efficiency peak does not coincide with the visual peak (ZHR), because it depends on where the radiant is relative to the two stations. MCG_MS by DL5MCG applies the same idea to four fixed directions; YA-MS computes it for the **real path** between the two locators.

This tab shows it hour by hour for the day chosen in *Day for the 24 h table (UTC)* (values at half past each hour).

## Glance cards

| Card | Content |
|---|---|
| **BEST TIME OF THE DAY** | Hour with the highest path index, the index and the prevailing side (A/B with its %) |
| **MOST FAVOURABLE SHOWER** | The shower with the largest ZHR × efficiency of the day, its efficiency, hour and side, and the **best heading** (radiant azimuth +90° / −90°) |
| **NOW** | Index and prevailing side at this hour, and the recommended Hot (only when the chosen day is today) |
| **EXPERIMENTAL FORECAST** | Expected reflections/hour now, in 1 h and in 2 h at the forecast frequency (Collm, SM6FHZ rules; see [Experimental forecasts](Experimental-Forecasts)) |

Below the cards a band explains the letters A and B (see below).

## Chart

*Hourly efficiency for … on … (UTC, values at half past the hour).* For up to five showers: efficiency % as a solid line and the DH9GCD formula as a dotted line of the same colour; the **path index** as blue bars on the right scale.

## Hourly table

One row per shower active on that day (sorted by ZHR), 24 columns for the hours (UTC):

| Cell | Meaning |
|---|---|
| `63A` | efficiency 63 %, most reflections from side **A** |
| `41B` | efficiency 41 %, side **B** |
| `3` | efficiency under 5 %: number without side letter |
| empty | efficiency under 1 % |
| `…↑` | the radiant is **above 70°** from your station at that hour (too high) |
| yellow text | efficiency ≥ 50 % |

- **A** = **left** looking from your station towards the DX station (Hot A zone); **B** = **right** (Hot B zone). It is worth turning the antenna **10–30° towards that side** (side-scatter, Cerrotta–Sartori article).
- **Light-blue rows** (*DH9GCD %*, under each shower): the DH9GCD formula, for comparison.
- **Σ row**: *Path index (ZHR×eff.)*.
- **Orange row** (*Forecast … MHz (refl./hour)*): the experimental forecast, for the hours where it exists (today and part of tomorrow).

## The model

All steps are in the [calculation manual](Efficiency-Explanation) (`doc/YA-MS_manuale_calcoli.docx`, chapter 5). In short:

**1. Specular reflection.** A trail sends the signal from A to B only if it is tangent to an ellipsoid with A and B at the foci (McKinley 1961). The trails of a shower are parallel to the radiant direction ŝ (article; McKinley). For each point P of the E layer, with unit vectors towards the stations:

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

The same law underlies QTFGUI by DJ5HG (cone scattering). The condition is accepted with a Gaussian tolerance σ = 0.05 rad (about 3°) – *choice of the program*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Weight of each point.** Power of an underdense trail (McKinley), φ = half the scattering angle (limited to 85°, *choice*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

The number of meteors reaching a point is proportional to the sine of the radiant elevation there (ŝ·û_P), the same correction the IMO uses for ZHR.

**3. Sum and percentage.** Points every 15 km at the trail height, only where both stations see them above the lobe elevation (*choice*). 100 % is the most favourable radiant position for that path:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F is computed once per path on a grid of directions (azimuth every 5°, elevation every 2.5°) and interpolated.

**4. Side and index.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

The letter in the table is the side with the larger fraction. *Choices of the program (manual eq. 32–33).*

## DH9GCD comparison

An independent check: the best-direction formula by **DH9GCD**, reported by **DF5HC** (DARC conference, January 2018), with El and Az the radiant elevation and azimuth seen from your station and P the azimuth of the DX station:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

It is maximum with the radiant at 45° and broadside to the path. DF5HC considers the radiant too low below 20° and **too high above 70°**: these hours get ↑ in the table and a warning on the [Sky dome](Sky-View#warnings). The formula ignores distance and heights, but it is a good reference.

## Checks

| Check | Result |
|---|---|
| SM6FHZ rule (VUSHF 2025): best path orthogonal to the radiant azimuth, heading = radiant az ±90°, tolerance ±40–50° | Reproduced by the model; with the radiant aligned with the path and high in the sky the efficiency is almost zero |
| QTFGUI by DJ5HG, Hamburg JO53IM – Barcelona, Quadrantids, 4 January (example of its manual) | QTFGUI: 07:00 heading 252°, −8 dB; 08:00 no reflection zone; 09:00 heading 168°, −4 dB. YA-MS (height 102 km as QTFGUI): 07:00 241°, −5.4 dB; 08:00 0.6 % (−22 dB); 09:00 161°, −4.0 dB. DH9GCD: 26 %, 2 %, 32 %. All three methods see the 08:00 hole, with the radiant almost at the zenith |
| Sampling every 5 km instead of 15 km | percentages change by less than 0.3 points |

> The scale used by OH5IY and MCG_MS is not known in detail (the MS-Soft manuals are not available): compare the percentages with those programs before treating them as equivalent. The model considers only underdense trails, with isotropic antennas; overdense bursts and sporadic background are not in the efficiency (the sporadic background is represented by the radar flux).
