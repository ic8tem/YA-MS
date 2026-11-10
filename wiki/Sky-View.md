**English** · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh)

# Sky dome

*Tab: Forecast calculation › Forecast calculation.*

[![Sky dome](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

This sub-tab (the sky dome of earlier versions) puts on one screen **where** the useful trails are now and **where to point**. On the left the **plan view** of the path; on the right the shower list, a small sky dome with the radiants, the text of the calculation and the **section** seen from your antenna. Everything refers to the moment chosen with *Calculation date (UTC)* and the *Hours (−12 to +36 h)* slider (real time by default, 15-minute steps).

A **strip above the plan view** sums up the calculation for that moment: date and time (*now* or hours from now), the **path index Σ ZHR×η**, the **most useful shower** with its ZHR and efficiency (also in dB relative to the DJ5HG reference, see [Efficiency calculation](Efficiency-Calculation)), the number of showers above the horizon and the **recommended Hot** with its azimuth.

In the small sky dome an **orange line** through the zenith always gives the **right antenna directions**, orthogonal to the drift of the selected shower (or of the most favourable one): radiant azimuth ±90°, labelled *antenna NNN°* at both ends, with the ±45° tolerance as thin lines. Short orange ticks on the rim give the orthogonal directions of the other useful showers.

## Plan view (left)

A map of Europe seen from above (**E to the right**) with a degree scale around it. The caption under the map gives its radius (*Map: edge = … km from the station*).

| Element | Drawing |
|---|---|
| Path / DX | Green line from your station to the DX station (always the real great-circle path between the locators) |
| **Hot A / Hot B** | Points either side of the midpoint, perpendicular to the path, at the distance given by the AMS offset table (or entered by hand). **Red = recommended**, **pink = outside the antenna lobe**, **grey = inside the lobe** (with a warning) |
| Antenna lobe | The −3 dB horizontal lobe around the antenna azimuth (antenna always pointed at the DX), labelled *lobe …°* |
| Common zone limits | Faint *lim. A* / *lim. B* points and the two circles where each station's horizon meets the E layer (see [Geometry](Geometry-and-Path-Loss#common-zone-limits)) |
| Shower drift | **Yellow line**: direction in which the selected shower (or the most favourable one) sweeps the sky, i.e. the radiant azimuth |
| Best headings | **Orange dots**: the two headings perpendicular to the drift (radiant azimuth ±90°, SM6FHZ) |
| **PREV zones** | Light ellipses: where the most likely trails fall **now**, one per side of the path |

Labels do not overlap: Hot A and PREV A are written on the left of the path, B on the right. The **Legend** is a foldable column on the right of the map.

**Mouse on the map:** **left click = DX station locator**, **right click = my station locator**. The path is recomputed at once.

Options above the shower list: **Hot A / Hot B directions**, **Map of Europe** (Natural Earth, downloaded into `data/mappa` on the first start), **Top view (E to the right)**.

### Recommended Hot

For the time shown, the program adds up over all showers above the horizon the weight ZHR × efficiency, split between side A (fraction f_A) and side B. The side with the larger weight gives the recommended Hot, drawn in red:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Choice of the program (manual eq. 23).* Source of the idea: DJ5HG, reported by DF5HC (DARC conference 2018) – depending on the radiant position one of the two points, HOT-A or HOT-B, is more favourable. Turning 10–30° towards that side (side-scatter) comes from the Cerrotta–Sartori article.

### PREV zones

For each point P of the E layer the contributions of all active showers to the efficiency (same specular condition as the [efficiency](Efficiency-Calculation#the-model)) are added, weighted with ZHR. Points with at least 3 % of the maximum form the PREV zones; each is drawn as an ellipse with centre = weighted mean of the points and axes = twice their spread.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Choice of the program (manual eq. 34).* It is the practical rule: if the shower sweeps from north to south, the useful trails fall east and west.

## Shower list (top right)

| Column | Meaning |
|---|---|
| Shower, Code | Name and IMO code |
| ZHR now | Activity at this moment (IMO peak ZHR with the activity profile) |
| Azimuth, Elev. | Radiant position seen from your station |
| Effic. % | Efficiency of the shower for this path |
| Side | A or B, the side from which most reflections arrive |
| Best heading | Radiant azimuth ±90° |
| Rise, Set | Radiant rise and set (UTC); *circumpolar* or *always below* when it applies |

Click a row to select the shower: the yellow drift line and the orange dots follow it.

## Small sky dome (middle right)

The radiants on a sky dome seen from your station, with their **IMO code** and **daily track in cyan** (UTC hours). **Click a radiant** to select it. Colours:

| Colour | Meaning |
|---|---|
| Yellow | efficiency ≥ 50 % and ZHR ≥ 2 |
| Orange | efficiency ≥ 20 % |
| Dark red | efficiency < 20 % |
| Grey | almost inactive |

Next to it, the text of the calculation: path length and azimuth, midpoint and its elevation, Hot A / Hot B azimuths and offsets, the recommended Hot (*… recommended now: az. …° (…% of expected reflections)*), the common zone limits, and the reminder: *best pointing for the shower: PERPENDICULAR to the direction of arrival (radiant azimuth ±90°, tolerance ±40–50°, SM6FHZ)*.

## Section (bottom right)

*SECTION – the most likely trails seen from the antenna towards the DX station.* Horizontally the **azimuth relative to the DX station** (← A left, B → right), vertically the **elevation**. For each shower the 14 strongest reflection points are taken; each trail is a segment oriented towards the radiant, from 10 km above to 10 km below the trail height (at most 60 km per side), thicker when more likely. Also drawn: the antenna lobe (−3 dB circle around the lobe elevation), the DX station and Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Choice of the program (manual eq. 35).*

## Warnings

| Warning | When |
|---|---|
| **WARNING: Hot A (and/or Hot B) falls inside the antenna lobe …** | The hot spot is within ±θ/2 of the antenna azimuth (θ = horizontal −3 dB lobe): with this heading it is already covered. Shown in grey on the map. The recommended Hot stays red. |
| **RADIANT TOO HIGH (above 70°)** | A useful radiant is above 70° from your station: trails fall almost vertically and reflect little towards the path (DF5HC, DH9GCD). The same hours are marked ↑ in the [hourly table](Efficiency-Calculation#hourly-table). |
| **LOW RADIANT ALONG THE PATH** | An active radiant is below 20° and within 30° of the path direction. The calculated efficiency stays low (cautious), but DJ5HG expects rare, strong reflections from grazing trails aligned with the path (Hamburg–Narvik, Quadrantids, about 19 UTC): worth listening. |
| **PATH BEYOND THE TRAIL HORIZON** | At the trail height the path midpoint is below the horizon of both stations (about 2120 km with trails at 90 km). The warning gives the minimum trail height needed (about 96 km for 2200 km, 105 km for 2300 km): the link is possible only with the highest trails, and efficiencies and losses are at the limit of the model |
| *No common E-layer zone* | The path is longer than twice the range at trail height: the two stations do not see a common part of the E layer (single hop impossible). |
| *No recommended Hot* | Almost no active shower at this time. |

Reference for the sky dome graphics: Swan Meteor Skyview by DL1DBC (swan.ms); polar plot with the best direction: RadiantCalc by SM6FHZ.
