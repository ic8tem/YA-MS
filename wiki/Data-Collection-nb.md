[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · **Norsk** · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [ไทย](Data-Collection-th) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Datainnsamling

*Fane: Direkte og sanntidsdata › Datainnsamling.*

[![Datainnsamling](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Tre clusterstrømmer

Fanen samler **meteor scatter-spot** fra tre telnet-strømmer, hver i sin egen underfane:

| Underfane | Standard | Merknader |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | En valgfri cluster. På ON0DXK er VHF-båndene filtrert: aktiver dem med `set/filter dxbm/pass 6` (deretter 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmere dekoder sjelden MS-modi. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X-cluster med **PSKReporter**-spot: MSK144-dekodingene fra WSJT-X og MSHV kommer hit. |
| **Innsamlede MS-spot** | – | Tabell over godtatte spot, nyeste først. |

Hver strøm har vert, port, kommandoer som sendes etter innlogging, *Koble til på nytt*, *Koble til ved oppstart*, en konsoll og en linje for å sende kommandoer. Skriv **kallesignalet for innlogging** øverst. En stripe viser tilstanden til de tre øktene (grønn prikk = tilkoblet). Øktene holdes åpne når du bytter språk eller fargeskjema.

## Filteret (40 % av vinduet)

- **Valgfritt lokalt filter:** clusterlinjer under **27990,0 kHz** forkastes med en gang (vises ikke, lagres ikke).
- **1. kriterium – typiske MS-frekvenser:** 50190–50300, 70100–70400, 144290–144399 kHz. Et spot i disse vinduene godtas også uten modusnavn, med mindre kommentaren oppgir en annen utbredelse: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Vinduer og tagger kan redigeres.
- **2. kriterium – MS-modi:** utenfor vinduene, eller med en av disse taggene, beholdes et spot bare hvis det inneholder **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digitale modi som bare brukes til MS) eller **\<MS\>**, med store, små eller blandede bokstaver. Ord kan slås av, legges til og fjernes; hvert har sin teller.
- **Bånd** 28, 50, 70, 144, 222, 432 MHz; **test av filteret** på en innlimt linje; **tellere**.

## Lokatorer og lagring

Manglende lokatorer, eller lokatorer med bare 4 tegn, hentes fra **CALL3**-arkivet (`data/call3.txt`, JTDX-fil, over en million kallesignaler), som alltid går foran en lokator med 4 tegn. Godtatte spot lagres i `data/spot_ms`, én CSV-fil per dag, og mater kartet i [Trafikk direkte](Live-Traffic-nb).
