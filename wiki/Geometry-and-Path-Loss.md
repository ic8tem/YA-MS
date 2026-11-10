**English** · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh)

# Geometry and path loss

*Tab: Forecast calculation › Geometry and path loss.*

[![Geometry and path loss](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

A text report of the path (selectable, so you can copy it) and, on the right, the chart **Antenna elevation versus distance from the scatter point**. Numbers in brackets refer to the equations of the calculation manual (`doc/YA-MS_manuale_calcoli.docx`).

## Inputs of this tab

| Field | Default | Use |
|---|---|---|
| **Power W** | 400 | Transmitter power for the link budget |
| **Antenna gain dBi (tx = rx)** | 14 | Same antenna at both ends |
| **Minimum signal dBm** | −130 | Minimum detectable signal (article: 8-element Yagi + preamp) |
| **Trail density q = 10^ … electrons/m** | 14 | Electron line density of the underdense trail |

The stations, band, trail height, lobe elevation, boom and hot spot distance come from the [rows of controls](Getting-Started#1-the-three-rows-of-controls).

## Report sections

| Section | Content |
|---|---|
| **PATH GEOMETRY (spherical Earth, R = 6372.7955 km)** | Station and DX with heights; distance, azimuth and back azimuth; midpoint (locator and coordinates); trail height (*← mode measured by the Collm radar* when taken from the radar); antenna elevation towards the midpoint |
| **HOT A / HOT B (classic hot spots, for antenna pointing)** | For each: locator, azimuth from you and offset from the direct path, azimuth from the DX, distance, elevation |
| **COMMON ZONE LIMITS** | Range at trail height with the lobe elevation; Limit A / Limit B with azimuths |
| Antenna | Boom in λ, gain, horizontal / vertical lobe; whether Hot A and Hot B are inside or outside the lobe |
| **PATH LOSS (underdense trail, McKinley 1961; antenna gains excluded)** | Table for the midpoint (forward), Hot A and Hot B at 28, 50, 70, 144, 222 and 432 MHz |
| **LINK BUDGET AT … MHz (midpoint)** | Power and EIRP, path loss, signal at the antenna, minimum detectable, **margin**; the same margin with OH5IY's average loss |
| **EXPERIMENTAL RULES BETWEEN BANDS (SM6FHZ, VUSHF 2025)** | Number/intensity and duration compared with 144 MHz; IARU maximum ping |

## Locator and path

Locator (4, 6 or 8 characters; centre of the square, IARU Maidenhead system) [14]. Distance, azimuth and midpoint with great-circle formulas on a sphere of radius **r = 6372.7955 km** (Cerrotta–Sartori article) [15–16]. Time-dependent calculations refer to the **midpoint**, because the best time can differ by up to 1.5 hours between the two ends (SM6FHZ).

## Antenna elevation

**Source:** formula of the Cerrotta–Sartori article (Figure 7), with x = d/r, d the ground distance to the reflection point, H the trail height and h the station height [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Check:** it matches exact spherical geometry within 0.03°. The program uses the two-argument arctangent, which gives negative values beyond the horizon and avoids the periodicity problem mentioned in the article. A negative elevation towards the midpoint means *path beyond the geometric range of a single hop*.

## Horizon range

Ground distance at which a ray with elevation e reaches the height H (geometric inverse of the formula above) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Check:** H = 89.5 km, e = 0° → **1062 km**. In the article's example (JN44BB–IO53RT) the drawing puts the horizon crossings about 870 km from the stations, which corresponds to a lobe raised about 2° (865 km).

## Common zone limits

**Source:** the article locates the crossings of the curves where each station's horizon meets the E layer: the crossings of two circles of angular radius ρ = d_H/r centred on A and B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

If 1 − |p0|² < 0 the path is longer than 2·d_H and the stations see **no common E-layer zone**.

**Check:** these are the **farthest edges** of the sky seen by both stations, **not points to aim at**. On JN70CN–IN78UO (1710 km, azimuth 308°) they fall 1062 km from the station, 37° left and right of the direct path, while MSHV suggests 10°. That is why they are called *Limit A* / *Limit B* and drawn faintly on the map.

## Hot A and Hot B

**Source:** reflections concentrate in two zones ("hot spots") about **50–150 km either side of the midpoint**. This is the basis of the antenna-offset table of AMS Bulletin No. 203, taken up by W8WN (10° offset for 1500 and 1800 km paths); MSHV by LZ2HV uses the same criterion.

**Choice:** Hot A and Hot B are the points at distance s from the midpoint M, perpendicular to the path (s = 150 km, adjustable 30–400 km); A to the left looking from your station to the DX, B to the right [21]. The offset seen from the station is about [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Check:** JN70CN–IN78UO, D = 1710 km: 6.7° with s = 100 km, **10.0° with s = 150 km** (same as MSHV and AMS/W8WN), 13.2° with s = 200 km.

## Underdense path loss

**Source:** McKinley's equation for underdense trails (β = 0, sin α = 1), antenna gains excluded; q = electron line density, r_e = classical electron radius = 2.818·10⁻¹⁵ m, R1, R2 distances from the trail, φ half the scattering angle [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\cos^2\varphi}{\lambda^3 q^2 r_e^2}\right]\ \mathrm{dB}
```

**Check:** with q = 10¹⁴ electrons/m at 144 MHz: **181–192 dB** between 600 and 2200 km, in line with the article references at 144 MHz: **182 dB minimum** (GM8JBJ, from Kaiser & Closs 1952) and **200 dB average** (OH5IY).

## Link budget

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Gains are entered and used in dBi: McKinley's loss refers to isotropic antennas, so no 2.15 dB dipole correction is subtracted (EIRP = power + gain). The report also gives the margin with **OH5IY's average path loss** (200 dB at 144 MHz, scaled with λ³ to the chosen band). Article reference: about **70 dBm EIRP** is needed (−130 dBm + 200 dB, e.g. about 400 W into 14 dBi).

## Antenna gain and lobe

**Gain – source:** curve by Günter Hoch **DL6WU** for long Yagis as a function of boom length L, reported by W8IO (valid from about 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Check against the NEC models of L.B. Cebik W4RNL at 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elements | Boom (λ) | W4RNL NEC (dBi) | Formula (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3.23 / 6.82 / 10.42 | 15.28 / 17.82 / 19.35 | 15.38 / 17.91 / 19.34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3.12 / 6.88 / 10.79 | 15.17 / 17.91 / 19.46 | 15.27 / 17.94 / 19.45 |

The difference never exceeds **0.1 dB**: the gain depends on the boom length more than on the design (VK3AUU Yagis have a shorter boom for the same number of elements). The Yagi Calculator by VK5DJ also gives estimates for the VK3AUU, WA2PHW and DJ9BV variants, whose formulas are not published.

**Lobe – source:** Kraus rule, with a circular lobe θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Check:** W4RNL's NEC models of DL6WU Yagis give a **horizontal lobe 5–10 % narrower** than Kraus: 33.8° / 26.4° / 22.6° for 12, 19 and 26 elements, against 37.3° / 28.0° / 23.9°. Simple formulas ignore the forward side lobes (W4RNL, *Long-Boom Yagi Rules of Thumb*). On long booms the vertical lobe is slightly wider than the horizontal (14 λ: 18.4° / 18.8°).

**Choice** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Example: 14 λ Yagi at 432 MHz → 20.3 dBi, lobe 18.1° horizontal and 19.5° vertical; W4RNL's models give 20.4 dBi and 18.4° / 18.8°. These are approximate rules derived from a few DL6WU antennas.

The antenna is always considered pointed at the DX. A hot spot is **inside the lobe** if |Az(Hot) − Az(antenna)| ≤ θ_horizontal/2: it is then drawn in grey on the [Sky dome](Sky-View) and a warning appears. In the efficiency calculation the antennas are isotropic; the real lobe is used only for this check.

## Experimental rules between bands

Compared with 144 MHz: number/intensity × (144/f)³ (in dB), duration × (144/f)² (SM6FHZ, VUSHF 2025). IARU Region 1 maximum ping duration: 1000 ms at 50 MHz, 500 ms at 70 MHz, 100 ms at 144 MHz, 13 ms at 432 MHz (VHF Handbook, quoted in the article). See also [Experimental forecasts](Experimental-Forecasts).
