**English** · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Live traffic

*Tab: Live and real-time data › Live traffic.*

[![Live traffic](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## What it shows

An **azimuthal equidistant map** centred on your station (distance from the centre = true distance, angle = azimuth) with **all the meteor-scatter traffic** gathered by [Data collection](Data-Collection). For every contact the program draws:

- the **path** between the two stations, in the colour of its band: 28 MHz brown, 50 MHz green, 70 MHz cyan, 144 MHz orange, 222 MHz pink, 432 MHz violet;
- the two **stations** at the ends of the path;
- the **cloud**: where the most probable meteor trails for that path and that time are concentrated.

Spots with a station **outside the map** are discarded. A spot that has **just arrived** (not older than 3 minutes) **blinks for one minute**, so new activity stands out at a glance.

Show who is listening: triangles in the band colour mark the stations that, according to PSKReporter, are receiving in MSK144, FSK441, PSK2K or JTMS on 28, 50, 70, 144 and 432 MHz in the chosen time window. A click on a triangle shows call, locator, modes and last spot. The MQTT feed of the Data collection tab must be connected.

Also the active monitors of the PSKReporter map: hollow triangles for the stations that appear on the pskreporter.info map in MSK144, FSK441, PSK2K or JTMS but have not received any spot yet (MQTT only sends stations that receive something). YA-MS queries the PSKReporter retrieval service once every 5 minutes for all modes, as the service rules ask; a monitor stays on the map for at least 11 minutes. A click on the triangle shows callsign, locator, decoding software and the time the monitor was active. On by default.

FT8 beyond 1100 km with no parallel paths: an FT8 spot (from PSKReporter MQTT, the clusters or WSJT-X via UDP) between stations more than 1100 km apart that has no parallel paths in the 3 minutes before and after (same band, midpoint within 300 km, direction within 15°, another pair of stations) is drawn in light green and its row in the table at the bottom right always blinks. Sporadic-E and tropo give many close, parallel paths; an isolated spot may be a meteor trail. For this YA-MS also receives from MQTT the FT8 spots of 6 m, 4 m, 2 m, 1.25 m and 70 cm (not those of 10 m, too many). These spots do not go into the MS archive. On by default.

WSJT-X spots via UDP that concern your station (the decode contains your callsign: who calls you or answers you) are drawn with a dashed line that always blinks, in any mode and at any distance.

Exchange between YA-MS users: when another YA-MS user decodes via UDP a message addressed to your station (in MSK144, FSK441, PSK2K or JTMS, or in FT8 beyond 1100 km), their YA-MS sends it to you encrypted through three public MQTT brokers (HiveMQ, Mosquitto, EMQX); you see it as a violet dashed line that always blinks and as a line in the UDP console. Only you can read it (ECDH P-256 keys, AES-256 and HMAC-SHA256). FT8 spots are shown only if they have no parallel paths within 3 minutes. On by default; yams_scambio=0 in data/config.ini turns it off.

The map shows the callsigns of both stations of each spot, once per station. The projection can be azimuthal (centred on your station) or Mercator. The tooltip on the Cloud column explains its meaning.

Spots of all bands are shown, including those not chosen in Data collection (these are not stored). CW spots and spots between stations that are too close are not shown, if they are discarded in Data collection.

## How the cloud is computed

For each spot the program builds the path between the two locators (the same geometry as for your own path, see [Geometry and path loss](Geometry-and-Path-Loss)) and, at the time of the spot, adds up point by point of the E layer the **specular-reflection contributions of every active shower**, weighted with its ZHR – the same calculation as the **PREV zones** of the [sky dome](Sky-View). For each side of the path holding at least 15 % of the total, the cloud is an **ellipse**: centre at the weighted mean of the points, semi-axes 1.5 times the square roots of the eigenvalues of their spread, major axis along the main eigenvector. When no shower contributes (sporadic meteors only) the clouds are the two classic **hot spots**, drawn dashed. The full equations are in chapter 10 of the calculation manual.

## Controls

| Control | Meaning |
|---|---|
| **Map radius** | 600–3500 km from your station. |
| **Spots to show** | Last 15 or 30 minutes, last hour, last 3 hours, last 24 hours. |
| **Table** | Contacts on the map, newest first, in the band colour; *Cloud* gives the share of reflections on the main side, or *sporadics*. |
| **Click** | On a path or a table row: the contact is highlighted and the box shows the locator of the cloud centre, its share, size and axis. |
