**English** · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Efficiency calculation

*Tab: Forecast calculation › Efficiency calculation.*

[![Efficiency calculation](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

The **efficiency** of a shower says, in percent, how much the position of its radiant allows reflections on **your** path. The concept is by Ilkka **OH5IY** (MS-Soft) and is taken up in the Cerrotta–Sartori article: the efficiency peak does not coincide with the visual peak (ZHR), because it depends on where the radiant is relative to the two stations. MCG_MS by DL5MCG applies the same idea to four fixed directions; YA-MS computes it for the **real path** between the two locators.

This tab shows it hour by hour for the day chosen in *Calculation date (UTC)* (values at half past each hour).

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

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

The same law underlies QTFGUI by DJ5HG and his text *"Die Geometrie von Meteorscatterverbindungen"* (2004): the trail scatters on a cone with the trail as axis, and only a receiver on the cone hears it. For an ideal trail the cone wall is very thin (a radiator thousands of wavelengths long); the program accepts the condition with a Gaussian tolerance σ = 0.05 rad (about 3°), which stands for what the ideal cone does not see: the spread of shower radiants (0.3–1.4° measured by GMN), trails bent by the wind and their finite length – *choice of the program*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Weight of each point.** Power of an underdense trail (McKinley; ITU-R P.843, eq. 3), φ = half the scattering angle (limited to 85°, *choice*), β = angle between the trail and the propagation plane A-P-B, p̂ = unit normal to that plane:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Option "β angle between trail and path (full McKinley)"** (on by default, cautious setting). On: trails crossing the propagation plane are worth 10–15 dB less than those lying in it, so no trail is overestimated. Off: every trail is weighted as if it lay in the plane (β = 0, weight with cos²φ), as up to version 1.6. *Check:* on a 1000 km path, without β the best radiant azimuth is 15°–90° from the path depending on the radiant elevation (30° with the radiant at 30°, broadside with the radiant at 60°), and the broadside radiant is worth 67 % at 30° elevation; with β the best radiant is always along the path and the broadside one drops to 15 %. With β the SM6FHZ / DH9GCD best-direction rule is lost; β stays an option, on by default because it gives the most cautious values, and switching it off brings the rule back.

The number of meteors reaching a point is proportional to the sine of the radiant elevation there (ŝ·û_P), the same correction the IMO uses for ZHR.

**Option "Longer trails with a low radiant (DJ5HG)"** (checkbox above the chart, off by default, tooltip): DJ5HG notes that with a low radiant fewer meteors fall per km² but the trails are longer (up to 100 km useful) and meet the reflection law more often. With the option on, the weight becomes min(sin El, 15/100): the useful layer thickness, 15 km, divided by the sine of the elevation gives the trail length, capped at 100 km. Above about 9° the two effects cancel. Off, the calculation stays cautious.

**Calculation settings** (same row, radio buttons): **Cautious** (default, the most cautious values: trail height from the radar, normal trails, β on), **As DJ5HG** (102 km, longer trails, β) and **Custom**, selected automatically when you change the height, the *from radar* box, the longer-trails option or β by hand.

**3. Sum and percentage.** Points every 15 km at the trail height, only where both stations see them above the lobe elevation (*choice*). 100 % is the most favourable radiant position for that path:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F is computed once per path on a grid of directions (azimuth every 5°, elevation every 2.5°) and interpolated.

**Efficiency in dB (DJ5HG reference).** The percentage is relative to the best radiant position for that path only. To compare different paths the program also gives the efficiency in dB relative to the fixed reference of DJ5HG: 0 dB is the maximum of a 1000 km north–south path across the equator with the radiant on the celestial equator at the equinox, computed with the same height and weights. DJ5HG gives his values as better than 6 dB.

**4. Side and index.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

The letter in the table is the side with the larger fraction. *Choices of the program (manual eq. 32–33).*

## DH9GCD comparison

The primary sources for the best direction are Eshleman & Mlodnosky and Meeks & James (Proc. IRE, 1957), Hines (1955) and its experimental check by Forsyth, Hines & Vogan (1955): only radiants on the half-circle of sky perpendicular to the bisector of the scattering angle are useful, the trail number grows with sin El, and near the midpoint the useful trails fall at about H·tan El to the side, on the side opposite the radiant. DJ5HG adds a reservation: with a **low** radiant right along the path, McKinley's formula gives strong signals (Hamburg–Narvik, Quadrantids, about 19 UTC), so "radiant aligned with the path = almost zero" holds for a high radiant only; the program stays cautious and shows the warning *LOW RADIANT ALONG THE PATH*.

An independent check: the best-direction formula by **DH9GCD**, reported by **DF5HC** (DARC conference, January 2018) – it has no published primary source – with El and Az the radiant elevation and azimuth seen from your station and P the azimuth of the DX station:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

It is maximum with the radiant at 45° and broadside to the path. DF5HC considers the radiant too low below 20° and **too high above 70°**: these hours get ↑ in the table and a warning on the [Sky dome](Sky-View#warnings). The formula ignores distance and heights, but it is a good reference.

## Checks

| Check | Result |
|---|---|
| SM6FHZ rule (VUSHF 2025): best path orthogonal to the radiant azimuth, heading = radiant az ±90°, tolerance ±40–50° | Reproduced by the model; with the radiant aligned with the path and high in the sky the efficiency is almost zero |
| QTFGUI by DJ5HG, Hamburg JO53IM – Barcelona, Quadrantids, 4 January (example of its manual) | QTFGUI: 07:00 heading 252°, −8 dB; 08:00 no reflection zone; 09:00 heading 168°, −4 dB. YA-MS (height 102 km as QTFGUI): 07:00 241°, −5.4 dB; 08:00 0.6 % (−22 dB); 09:00 161°, −4.0 dB. DH9GCD: 26 %, 2 %, 32 %. All three methods see the 08:00 hole, with the radiant almost at the zenith |
| DJ5HG curves (*Die Geometrie…*, Bild 8–9: from Hamburg and Munich, Quadrantids, 4 January; read from the chart, about ±0.5 dB and ±15 min) against the automatic test `--prova-dj5hg` (one value per hour) | Timing: the hole with the radiant near the zenith falls at the same hours (Barcelona 07:30–08:30 vs 07–09; Sofia 06:36–07:48 vs 07–08; Narvik 07–08:30 vs 07–09); Moscow is closed 03–10 in both, open from Hamburg until about 02:30 and from Munich until about 00:30, as DJ5HG writes. Headings: 2–10° apart. Levels and shape at 102 km (mean and RMS difference from the curves): no β, no longer trails −1.6 / 4.0 dB; longer trails +1.1 / 4.6 dB; β −5.4 / 6.2 dB but with the best shape (3.0 dB after removing the mean, vs 3.6): the deep minima with a low radiant appear (Barcelona −15.6 dB at 17 vs −16 dB at 19:36; Sofia −18.5 dB at 20 vs −14 dB). β and longer trails (*As DJ5HG*) −2.2 / 4.7 dB; the cautious setting (radar height 89.5 km, β on, no longer trails) −6.9 / 7.6 dB, shape 3.3 dB. Without β YA-MS barely shows the minimum with the radiant low and almost aligned with the path (−8.6 and −10.4 dB): this is DJ5HG's own reservation, hence the warning |
| Sampling every 5 km instead of 15 km | percentages change by less than 0.3 points |

> The MS-Soft 5.2 documentation defines OH5IY's efficiency as a relative index for underdense trails only, with two factors (radiant elevation, best about 45°, and angle to the path, best 90°) and a minimum raised by hand to 20 % for overdense trails; the formula is not published. MCG_MS computes it for four fixed directions and, with the DX locator, for the real path. The model considers only underdense trails, with isotropic antennas; overdense bursts and sporadic background are not in the efficiency (the sporadic background is represented by the radar flux).
