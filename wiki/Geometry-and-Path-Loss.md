**English** · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

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

**Source:** reflections of sporadic meteors concentrate in two zones ("hot spots") either side of the midpoint. J. Richardson (AMS), in the table quoted by DJ5HG (*Die Geometrie von Meteorscatterverbindungen*, 2004), gives the antenna offset from the direct heading: **13° at 1000 km, 11° at 1250 km, 10° at 1500 and 2000 km**. AMS Bulletin No. 203, taken up by W8WN, gives 10° at 1500 and 1800 km.

**Choice:** Hot A and Hot B are the points at distance s from the midpoint M, perpendicular to the path. With *auto (AMS)* ticked (default) s comes from the offset of Richardson's table, interpolated linearly (13° below 1000 km, 10° above 2000 km): s = (D/2)·tan(offset). Unticked, s is entered by hand, 30–400 km (MSHV uses 150 km); A to the left looking from your station to the DX, B to the right [21]. The offset seen from the station is about [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Check:** with the AMS table, 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, the same as the 150 km used before and by MSHV; on short paths the table brings the hot spots closer to the midpoint.

## Underdense path loss

**Source:** McKinley's equation and ITU-R Recommendation P.843 for underdense trails (sin α = 1), antenna gains excluded; q = electron line density, r_e = classical electron radius = 2.818·10⁻¹⁵ m, R1, R2 distances from the trail, φ half the scattering angle, β angle between the trail and the path plane, a₁ initial-radius factor with r₀ in m and h in km (P.843, eq. 4 and 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Choice:** the budget and the loss table use β = 90° (trail crossing the path plane, the least favourable case: cautious value) and the budget also shows the best case, β = 0. r₀ is taken at the mean echo height for the frequency, h = 124 − 17 log f (P.843, eq. 15): 0.76 m at 95 km for 50 MHz, 0.40 m at 87 km for 144 MHz, 0.21 m at 79 km for 432 MHz. Over 1000 km a₁ is 0.2 dB at 50 MHz, 0.6 dB at 144 MHz and 1.4 dB at 432 MHz (2.9 dB at 600 km); at DJ5HG's fixed 102 km it would be about 70 dB at 432 MHz, i.e. no echo at all.

**Check:** with q = 10¹⁴ electrons/m, trails at 89.5 km and β = 0, at 144 MHz: **182–192 dB** between 600 and 2100 km (185 dB at 1000 km), inside the **172–190 dB** range computed by John Worsnop **G4BAO** in his PhD thesis, as reported by GM8JBJ. With β = 90° the loss grows by 10 dB at 600 km, 13 dB at 1000 km and 16 dB at 2100 km; the **200 dB average** of OH5IY lies between the two cases. The 182 dB in GM8JBJ's table are not a confirmation: the table gives no frequency, its 86.4 dB per leg are the free-space loss over 500 km at 1 MHz (the 20 log f term is missing: 129.6 dB at 144 MHz) and its items add up to 163.8 dB, not 182; the page says neither "minimum" nor "144 MHz".

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
