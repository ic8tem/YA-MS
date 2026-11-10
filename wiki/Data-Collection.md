**English** · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [ไทย](Data-Collection-th) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Data collection

*Tab: Live and real-time data › Data collection.*

[![Data collection](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Three cluster streams

The tab collects **meteor-scatter spots** from three telnet streams, each in its own sub-tab:

| Sub-tab | Default | Notes |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | A cluster of your choice. On ON0DXK the VHF bands are filtered: enable them with `set/filter dxbm/pass 6` (then 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmers rarely decode MS modes. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X cluster carrying the **PSKReporter** spots: the MSK144 decodes of WSJT-X and MSHV arrive here. |
| **MS spots collected** | – | Table of the accepted spots, newest first. |

Each stream has host, port, commands sent after the login, *Reconnect*, *Connect at start-up*, a console and a line to send commands. Write your **callsign for the login** at the top. A strip shows the state of the three sessions (green dot = connected). The sessions stay open when you change language or colour scheme.

## The filter (40 % of the window)

- **Optional local filter:** cluster lines below **27990.0 kHz** are discarded at once (not shown, not stored).
- **1st criterion – typical MS frequencies:** 50190–50300, 70100–70400, 144290–144399 kHz. A spot in these windows is accepted even without the mode name, unless the comment declares another propagation: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Windows and tags can be edited.
- **2nd criterion – MS modes:** outside the windows, or with one of those tags, a spot is kept only if it contains **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digital modes used only for MS) or **\<MS\>**, in upper, lower or mixed case. Words can be switched off, added and removed; each has its counter.
- **Bands** 28, 50, 70, 144, 222, 432 MHz; **filter test** on a pasted line; **counters**.

## Locators and storage

Missing locators, or locators with only 4 characters, are taken from the **CALL3** archive (`data/call3.txt`, JTDX file, over a million callsigns), which always wins over a 4-character locator. Accepted spots are saved in `data/spot_ms`, one CSV file per day, and feed the [Live traffic](Live-Traffic) map.
