**English** · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [ไทย](Experimental-Forecasts-th) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Experimental forecasts

*Tab: Forecast calculation › Experimental forecasts.*

[![Experimental forecasts](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

This tab turns the meteor counts of the **Collm radar (36.2 MHz)** into an estimate of the **reflections per hour on an amateur band** (144 MHz by default, any frequency from 28 to 1300 MHz), forecasts the **next 24 hours** for your path and lets you **compare** the estimate with an **RMOB** observer – for example one listening to GRAVES on 143.050 MHz.

> Everything here is **experimental**: the frequency rule is an empirical rule, and the station factor depends on your station. Use the numbers to compare hours and days, and check them on the air.

## Controls

| Control | Default | What it does |
|---|---|---|
| **Target frequency MHz** | 144 | Frequency of the forecast (28–1300 MHz) |
| **λ^k exponent** | 3 | Exponent k of the frequency rule (SM6FHZ: 3) |
| **Station factor K** | 1 | Accounts for the receiving station (power, antennas); derived by comparison with an RMOB observer on the same band |
| **Load RMOB file from disk...** | | Reads a monthly RMOB text file (see below) |
| **Derive the exponent from the RMOB file** | | Fits k from the common hours of Collm and RMOB |
| **RMOB observer** | empty | Observer name as it appears in the file name (e.g. `NAME_112026rmob.TXT` → `NAME`) |
| **Download RMOB now** | | Downloads the current month's file of that observer once |
| **automatic download every 5 minutes (enable only with RMOB's permission)** | **off** | See [RMOB and automatic programs](#rmob-and-automatic-programs) |

The orange line under the controls shows the rule with the current numbers, e.g. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, the duration scaling and the IARU maximum ping at that frequency.

## From the radar to the amateur band

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}\sec^2\varphi
```

**Source:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, May 2025 – number and intensity of reflections scale with **λ³**, duration with **λ²** (432 MHz is 14–15 dB below 144 MHz and lasts 1/9). **Check:** in McKinley's equation λ³ is the power of a single underdense trail, not the number of trails; for mass index 2 the number of trails above a fixed threshold scales about as λ^1.5 (IZ5TEK; OH5IY). The program keeps k = 3, SM6FHZ's experimental rule, and says so; the right k for your station comes from the RMOB comparison. In forward scatter the duration also grows with sec²φ (McKinley; OH5IY): Collm measures in backscatter (φ = 0), so the forecast multiplies by sec²φ at the path midpoint (×4 at 60°, ×8.5 at 70°, ×33 at 80°). With k = 3, 1000 meteors/hour at Collm become about **16 reflections/hour at 144 MHz**; RMOB observers of GRAVES on 143.050 MHz usually count **20 to 140 echoes/hour** (RMOB bulletin, June 2018): the order of magnitude is compatible, and the difference is the station factor K. (Manual eq. 44–45.)

## Next 24 hours

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**Persistence:** the scaled value of the same hour of the day before (or two days before if missing), corrected by the change of the **path shower index** I (Σ ZHR × efficiency, see [Efficiency calculation](Efficiency-Calculation#the-model)). The constant 10 represents the sporadic background and limits the correction when the index is small. *Choice of the program (manual eq. 47).*

| Panel | Content |
|---|---|
| **Measured at Collm and scaled to f MHz – yesterday and today (UTC)** | Collm radar meteors/hour; scaled values (orange, right scale); the RMOB counts if loaded (green, right scale) |
| **Experimental forecast for the next 24 hours at f MHz for …** | Forecast reflections/hour (bars) and the path shower index (right scale) |
| Table | UTC time · Collm same hour · Scaled · Path shower index · Forecast /hour · **Rating** |

**Rating:** *good* when the forecast is at least 1.3 × the 24-hour mean, *fair* from 0.8 ×, *poor* below. The same forecast appears in the **EXPERIMENTAL FORECAST** card and in the orange row of the [Efficiency calculation](Efficiency-Calculation), and it is the base of the expected echoes in the [GRAVES radar](GRAVES-Radar#expected-echoes-experimental) tab.

## RMOB comparison

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) collects the hourly meteor counts of radio observers; many in Italy listen to GRAVES on 143.050 MHz (Venice Planetarium, Faenza, Rovereto and others).

**Reading RMOB files.** Two text formats are accepted:

| Format | Look | Notes |
|---|---|---|
| Monthly file (Colorgramme / Spectrum Lab) | one row per day, `day| n| n| …` with 24 hourly values | the usual `NAME_MMYYYYrmob.TXT` |
| Bulletin table | header ` UT |  1   2   3 …`, rows `0h|175 166 …` | if the file contains several observers they are read one after another: use a file with a single observer |

Month and year come from the file name (`…_MMYYYYrmob…`) or from the header; otherwise the current month is used (and the program says so).

**Fitting the exponent.** With K = 1, from the median of the RMOB/Collm ratios over the common hours (at least 3):

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*Choice of the program (manual eq. 46).* The dialog shows the common hours, the median ratio and k; **Yes** applies k (and sets K = 1), **No** keeps k = 3 – then adjust K by hand to the value suggested in the same dialog.

## RMOB and automatic programs

RMOB asks **automatic programs not to fetch its files**. For this reason the **automatic download is off** at the start and should be enabled **only after asking RMOB for permission**. Without it you can always use **Load RMOB file from disk...** or press **Download RMOB now** when you need it.

The download address is a template in `config.ini` (key `rmob_url`, default `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, where `{NOME}` is the observer and `{MMAAAA}` month and year); downloaded files are kept in `data/radar/`.
