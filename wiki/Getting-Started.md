**English** · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Getting started

At the first start YA-MS shows an example path (JN70CN → JO62QM on 144 MHz). Five minutes are enough to set it up for your station.

## 1. The three rows of controls

Above the tabs there are three rows of controls, valid for all tabs. The **Controls** button at the top right folds and unfolds them (useful with large fonts); the choice is remembered.

**Row 1 – stations and band**

| Control | What it does |
|---|---|
| **My locator** / **height m** | Your Maidenhead locator (4, 6 or 8 characters; the centre of the square is used) and the height of the station above sea level. |
| **DX station** / **height m** | Next to the map, on the right, is the correspondent box: type the callsign and press Enter, the locator is taken from the CALL3 database (as in YAEC and LIVETROPOVHF); below are the locator and the height. The callsign can also be typed in the locator box. |
| **Band MHz** | 28, 50, 70, 144, 222 or 432 MHz: used for the antenna gain and lobe, the flux estimate and the link budget. |
| **Calculate** | Recomputes the path (sampling of the E layer: a few seconds). |
| **Antenna az** | At the top of the correspondent box, next to the map: azimuth of your antenna, always **towards the DX** (azimuth of the path). The map legend is below, in the same column. |

**Row 2 – E layer and antenna**

| Control | What it does |
|---|---|
| **Trail height km** + **from radar** | Height of the meteor trails (default 90 km). With *from radar* ticked, the most frequent height (mode) measured by the Collm radar is used; see [Radar flux](Radar-Flux). |
| **Lobe elevation °** | Elevation of the peak of your antenna's vertical lobe: a beam fixed at 0° still has its lobe a few degrees above the horizon because of the ground reflection (usually 3-8°). With the **antenna pattern** box on (default) the points of the E layer are weighted with the vertical pattern of both antennas; with it off, only the points that both stations see above this elevation are used. |
| **Yagi antenna: boom m** | Boom length of your Yagi. The program shows the length in λ, the gain (DL6WU curve) and the −3 dB lobe, horizontal and vertical; see [Geometry and path loss](Geometry-and-Path-Loss#antenna-gain-and-lobe). Below 2 λ the estimate is rough. |
| **Hot spot from midpoint km** + **auto (AMS)** | Distance of Hot A and Hot B from the midpoint. With *auto (AMS)* ticked (default) it follows the antenna-offset table by J. Richardson (AMS) quoted by DJ5HG: 13° at 1000 km, 11° at 1250 km, 10° at 1500 and 2000 km (about 115, 121, 132 and 176 km from the midpoint). Untick it to enter 30–400 km by hand (MSHV uses 150 km). |

**Row 3 – time**

| Control | What it does |
|---|---|
| **Time** | UTC clock. |
| **Calculation date (UTC)** | The day of the calculation for [Forecast calculation](Sky-View) and [GRAVES radar](GRAVES-Radar) (today by default), at the current time of day. Also: the day shown in [Efficiency calculation](Efficiency-Calculation) and in the GRAVES timeline. |
| **Hours (−12 to +36 h)** | Moves the moment of the calculation from 12 hours before to 36 hours after that time, in 15-minute steps. Next to it: *Calculation for: now* or *Calculation for: dd/mm hh:mm UTC*. |
| **Real time** | Back to now. |

## 2. Your station and the DX

1. Type **My locator** and **height m**.
2. Type the **DX station** locator and height – or click the map in the [Sky dome](Sky-View): **left click = DX station locator**, **right click = my station locator**.
3. Choose the **Band MHz** and press **Calculate**.

The status bar at the bottom confirms: *Path computed: … km, … reflection points sampled in … s*.

## 3. Your antenna

Enter the **boom length** of your Yagi. The program derives gain and lobe and warns you if Hot A or Hot B already fall **inside the lobe** when the antenna points at the DX (then they are drawn in grey: no need to turn the antenna).

## 4. Read the results

| Question | Where to look |
|---|---|
| Which shower helps my path now, and from which side? | [Sky dome](Sky-View): shower list, recommended Hot in red, PREV zones |
| What is the best hour today? | [Efficiency calculation](Efficiency-Calculation): glance cards and hourly table |
| How many meteors is the radar counting? | [Radar flux](Radar-Flux) |
| How many pings can I expect on 144 MHz? | [Experimental forecasts](Experimental-Forecasts) (experimental) |
| Can my station close the path? | [Geometry and path loss](Geometry-and-Path-Loss): path loss and margin |
| When is the next peak? | [Showers](Showers) |
| Can I test with GRAVES? | [GRAVES radar](GRAVES-Radar) |

## Practical rules (from the sources)

- **Point perpendicular to the shower**: the best path is orthogonal to the radiant azimuth; best heading = radiant azimuth ±90°, tolerance ±40–50° (SM6FHZ).
- **Side-scatter**: turn the antenna 10–30° towards the side (A or B) from which most reflections arrive (Cerrotta–Sartori article).
- **Radiant too high** (above 70°) or too low (below 20°) gives few useful trails (DF5HC, DH9GCD).
- Sporadic meteors peak around **06 UTC** (article; confirmed by the Collm flux).
- Useful distances on 432 MHz: 800–2000 km, best about 1400 km (SM6FHZ); best distance in general 1300–1500 km (DF5HC).

Next: [Sky dome](Sky-View).
