**English** · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh)

# Radar flux

*Tab: Live and real-time data › Radar flux.*

[![Radar flux](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

This tab shows what professional meteor radars are counting **now**: the hourly meteor counts and the trail heights from the **Collm** SKiYMET radar (Leipzig University / IAP Kühlungsborn, Germany, 36.2 MHz), and the latest image of the **Sodankylä** radar (SGO, Finland). The Collm counts feed the estimate at your band and the [Experimental forecasts](Experimental-Forecasts); the measured trail height feeds the whole geometry.

## Controls

| Control | What it does |
|---|---|
| **Download now** | Checks all external sources at once. |
| **Automatic update of all sources every 5 minutes** | On by default. Every 5 minutes all sources are checked and **only those that changed** are downloaded again (*unchanged (checked at … UTC)* / *new data at … UTC*). |
| **λ exponent (SM6FHZ)** | Exponent k of the frequency rule, default 3 (1–4). |

## What is shown

| Panel | Content |
|---|---|
| **Meteors/hour – yesterday and today (UTC)** | Cyan bars = Collm counts (valid), red bars = discarded, thick orange line = *estimate at … MHz* on the right scale |
| **Trail heights (Collm)** | Meteors per km of height between 70 and 110 km, with most frequent height (mode), mean, median and standard deviation |
| Collm image | The original SKiYMET chart, as downloaded |
| Sodankylä image | The latest meteor-count image of the Sodankylä radar (shown only; its format is not read) |

The line above the charts says when the Collm chart was read and which vertical scale was found (*scale read from chart: 0-… meteors/hour*).

## How the Collm chart is read

The Collm chart (720 × 720 pixels, pure colours) has fixed axis positions, but the radar **adapts the vertical scale every day** to the measured values (e.g. 0–1.2·10³ on 5/11/2026 and 0–1.0·10³ on 6/11/2026, with moved tick marks). YA-MS therefore:

1. finds the long tick marks of the axis;
2. **reads the labels** of the highest tick and of the zero by comparing each character with the dot-matrix font of the chart;
3. for each hour i (0–47, yesterday and today) takes the centre column and the first cyan pixel from the top, y:

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top and y0 are the rows of the highest tick and of the zero, N_top the value read on the highest label (×1000). Resolution: about 7–8 meteors/hour per pixel. *Choice of the program (manual eq. 42).*

If a label cannot be read, the program falls back to the calibration of 5/11/2026 (**calibrated scale 0-1200 meteors/hour**) and says so in orange: *Cannot read the vertical flux scale (top label: …): values need checking.* If the chart format itself changes (*Chart format changed (…x…): cannot be read* or *Flux axes not found in the expected position*), the reading must be recalibrated: please report it (see [Contributing](Contributing-and-Contacts)).

### Trail heights

From the height histogram (n_k meteors in km k, mean height h_k):

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*Manual eq. 43.* With **from radar** ticked (row 2 of the controls) the **mode** becomes the trail height of all calculations. Check: chart of 5/11/2026 – mode 89.5 km, mean 88.6 km, standard deviation 6.8 km, confirming the ~90 km of the Cerrotta–Sartori article (SKiYMET mean).

If the scale of the height chart changes, the program warns: *height statistics (mode, mean, median) remain valid, absolute counts do not.*

## Estimate at your band

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

Experimental rules by **SM6FHZ** (VUSHF 2025): number and intensity of reflections scale with λ³, duration with λ²; the λ³ dependence is the same as in McKinley's underdense equation. The IARU Region 1 maximum ping duration is shown too (1000 ms at 50 MHz, 500 ms at 70 MHz, 100 ms at 144 MHz, 13 ms at 432 MHz). Values are indicative, to compare with experience on the air. The station factor K and the comparison with RMOB are in [Experimental forecasts](Experimental-Forecasts).

## Offline

If no source can be reached, a message appears **once**: *No internet connection. Radar and RMOB data cannot be updated: the program uses the last saved data and retries by itself every 5 minutes.* The status bar at the bottom turns red (*NO INTERNET CONNECTION …*) until the connection returns (*Connection restored.*).

## Archives and sources

| File (in `data/`) | Content |
|---|---|
| `flusso_collm.csv` | Hourly archive of the flux read from Collm (hours already present are updated) |
| `quote_collm.csv` | Archive of the trail heights |
| `radar/` | Latest downloaded images (and RMOB files) |
| `fonti_radar.csv` | Addresses of the radar sources, `attivo=1/0` to enable/disable each |

| Source | Frequency | Notes |
|---|---|---|
| Collm meteor radar, Leipzig University (LIM) and IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36.2 MHz | updated every hour at minute 10 UTC; flux yesterday + today, height distribution |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36.9 MHz | image only (radar being updated, DECC project) |
| swan.ms (copy of Collm) | 36.2 MHz | disabled by default; use only with DL1DBC's permission |

> Radar data belong to their institutions (Leipzig University / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
