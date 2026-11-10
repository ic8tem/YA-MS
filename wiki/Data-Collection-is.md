[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · **Íslenska** · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [ไทย](Data-Collection-th) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Gagnasöfnun

*Flipi: Beint og rauntímagögn › Gagnasöfnun.*

[![Gagnasöfnun](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Þrír straumar frá klösum

Flipinn safnar **meteor scatter-spotum** úr þremur telnet-straumum, hverjum á sínum undirflipa:

| Undirflipi | Sjálfgefið | Athugasemdir |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Klasi að eigin vali. Á ON0DXK eru VHF-tíðnisviðin síuð: virkjaðu þau með `set/filter dxbm/pass 6` (síðan 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmers afkóða sjaldan MS-hætti. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Klasi DM4X sem flytur spot frá **PSKReporter**: hingað berast MSK144-afkóðanir WSJT-X og MSHV. |
| **Söfnuð MS-spot** | – | Tafla yfir samþykkt spot, nýjustu fyrst. |

Hver straumur hefur hýsil, gátt, skipanir sem sendar eru eftir innskráningu, *Tengja aftur*, *Tengja við ræsingu*, skjáborð (console) og línu til að senda skipanir. Skrifaðu **kallmerki fyrir innskráningu** efst. Rönd sýnir stöðu lotanna þriggja (grænn punktur = tengt). Loturnar haldast opnar þegar þú skiptir um tungumál eða litaþema.

## Sían (40 % af glugganum)

- **Valfrjáls staðbundin sía:** línum frá klösum undir **27990,0 kHz** er hent strax (ekki sýndar, ekki geymdar).
- **1. viðmið – dæmigerðar MS-tíðnir:** 50190–50300, 70100–70400, 144290–144399 kHz. Spot í þessum gluggum er samþykkt jafnvel án heitis háttarins, nema athugasemdin tilgreini annars konar útbreiðslu: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Hægt er að breyta gluggum og merkjum.
- **2. viðmið – MS-hættir:** utan glugganna, eða með einu af þessum merkjum, er spot aðeins haldið ef það inniheldur **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (stafrænir hættir sem aðeins eru notaðir fyrir MS) eða **\<MS\>**, með hástöfum, lágstöfum eða blandað. Hægt er að slökkva á orðum, bæta þeim við og fjarlægja þau; hvert hefur sinn teljara.
- **Tíðnisvið** 28, 50, 70, 144, 222, 432 MHz; **prófun síunnar** á línu sem límd er inn; **teljarar**.

## Locatorar og geymsla

Locatorar sem vantar, eða locatorar með aðeins 4 stöfum, eru sóttir í safnið **CALL3** (`data/call3.txt`, JTDX-skrá, yfir milljón kallmerki), sem hefur alltaf forgang fram yfir 4 stafa locator. Samþykkt spot eru vistuð í `data/spot_ms`, ein CSV-skrá á dag, og fæða kortið [Umferð í beinni](Live-Traffic-is).
