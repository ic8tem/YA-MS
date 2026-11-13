**English** · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Data collection

*Tab: Live and real-time data › Data collection.*

[![Data collection](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Four sources

The tab collects **meteor-scatter spots** from three telnet streams and from the PSKReporter MQTT feed, each in its own sub-tab:

| Sub-tab | Default | Notes |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | A cluster of your choice. On ON0DXK the VHF bands are filtered: enable them with `set/filter dxbm/pass 6` (then 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmers rarely decode MS modes. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X cluster carrying the **PSKReporter** spots: the MSK144 decodes of WSJT-X and MSHV arrive here. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Live PSKReporter spots via **MQTT** (service by M0LTE): no login, each spot already carries the locators of the transmitting and the receiving station. Default topics: MSK144 on 6 m, 4 m, 2 m, 1.25 m, 70 cm and FSK441 on 2 m (`pskr/filter/v2/band/mode/#`); *Default topics* restores them. |
| **MS spots collected** | – | Table of the accepted spots, newest first. |

Each stream has host, port, commands sent after the login, *Reconnect*, *Connect at start-up*, a console and a line to send commands. Write your **callsign for the login** at the top. The MQTT source has host, port, topics (one per line or separated by `;`), *Reconnect* and *Connect at start-up* (off by default) and a console with the received spots; its spots go through the same filter. A strip shows the state of the four sources (green dot = connected). The sessions stay open when you change language or colour scheme.

## The filter (40 % of the window)

- **Optional local filter:** cluster lines below **27990.0 kHz** are discarded at once (not shown, not stored).
- CW spots are discarded straight away (CW or WPM in the comment, or 28000-28070 kHz): they do not appear in the console and are not stored, unless they are marked <MS>. The box can be switched off.

CALL3 database with the LIVETROPOVHF rules. "Update now" downloads CALL3.TXT from MMMonVHF (at least 100,000 valid lines, the previous one stays in data/call3.bak); with "Update by itself every 7 days" it does so at start-up. Above the file, in order: manual entries (data/CALL3-MANUALE.TXT), cluster corrections (the 6-character locator the spotter declares for itself), added files (data/CALL3-AGGIUNTE), then CALL3.TXT and the 6-character locators learned live (data/LOC6.TXT). A received 4-character locator, or one ending in LL or MM, is replaced by the 6-character one from the database; portables (with a slash) only with the exact entry.

Last source, as in LIVETROPOVHF: for callsigns that have no 6-character locator in any other source, the program asks the public G7VRD API (api.g7vrd.co.uk) in the background. Only a 6-character locator is accepted, not the square centre (LL or MM), in the same square as the received one; at most 40 callsigns per minute, each callsign once a day. The results are kept in data/CALL3-G7VRD.TXT.
- Spots between stations closer than 500 km are discarded straight away, because at that distance the path is direct or tropospheric, not meteor scatter: they do not appear in the console and are not stored. If a locator is missing the spot is kept. The distance can be changed below the box.
- **1st criterion – typical MS frequencies:** 50190–50300, 70100–70400, 144290–144399 kHz. A spot in these windows is accepted even without the mode name, unless the comment declares another propagation: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Windows and tags can be edited.
- **2nd criterion – MS modes:** outside the windows, or with one of those tags, a spot is kept only if it contains **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digital modes used only for MS) or **\<MS\>**, in upper, lower or mixed case. Words can be switched off, added and removed; each has its counter.
- **Bands** 28, 50, 70, 144, 222, 432 MHz; **filter test** on a pasted line; **counters**.

## Locators and storage

Missing locators, or locators with only 4 characters, are taken from the **CALL3** archive (`data/call3.txt`, JTDX file, over a million callsigns), which always wins over a 4-character locator. Accepted spots are saved in `data/spot_ms`, one CSV file per day, and feed the [Live traffic](Live-Traffic) map.
