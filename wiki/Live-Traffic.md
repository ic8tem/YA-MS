**English** · [Русский](Live-Traffic-ru) · [Deutsch](Live-Traffic-de) · [日本語](Live-Traffic-ja)

# Live traffic

*Tab: Live and real-time data › Live traffic.*

[![Live traffic](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## What it shows

An **azimuthal equidistant map** centred on your station (distance from the centre = true distance, angle = azimuth) with **all the meteor-scatter traffic** gathered by [Data collection](Data-Collection). For every contact the program draws:

- the **path** between the two stations, in the colour of its band: 28 MHz brown, 50 MHz green, 70 MHz cyan, 144 MHz orange, 222 MHz pink, 432 MHz violet;
- the two **stations** at the ends of the path;
- the **cloud**: where the most probable meteor trails for that path and that time are concentrated.

Spots with a station **outside the map** are discarded. A spot that has **just arrived** (not older than 3 minutes) **blinks for one minute**, so new activity stands out at a glance.

## How the cloud is computed

For each spot the program builds the path between the two locators (the same geometry as for your own path, see [Geometry and path loss](Geometry-and-Path-Loss)) and, at the time of the spot, adds up point by point of the E layer the **specular-reflection contributions of every active shower**, weighted with its ZHR – the same calculation as the **PREV zones** of the [sky dome](Sky-View). For each side of the path holding at least 15 % of the total, the cloud is an **ellipse**: centre at the weighted mean of the points, semi-axes 1.5 times the square roots of the eigenvalues of their spread, major axis along the main eigenvector. When no shower contributes (sporadic meteors only) the clouds are the two classic **hot spots**, drawn dashed. The full equations are in chapter 10 of the calculation manual.

## Controls

| Control | Meaning |
|---|---|
| **Map radius** | 600–3500 km from your station. |
| **Spots to show** | Last 15 or 30 minutes, last hour, last 3 hours, last 24 hours. |
| **Table** | Contacts on the map, newest first, in the band colour; *Cloud* gives the share of reflections on the main side, or *sporadics*. |
| **Click** | On a path or a table row: the contact is highlighted and the box shows the locator of the cloud centre, its share, size and axis. |
