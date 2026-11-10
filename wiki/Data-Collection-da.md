[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · **Dansk** · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh)

# Dataindsamling

*Fane: Live og realtidsdata › Dataindsamling.*

[![Dataindsamling](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Fire kilder

Fanen samler **meteor scatter-spots** fra tre telnet-strømme og fra PSKReporters MQTT-feed, hver i sin egen underfane:

| Underfane | Standard | Bemærkninger |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | En valgfri cluster. På ON0DXK er VHF-båndene filtreret: aktivér dem med `set/filter dxbm/pass 6` (derefter 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmere dekoder sjældent MS-modes. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X' cluster med **PSKReporter**-spots: MSK144-dekodningerne fra WSJT-X og MSHV kommer her. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | PSKReporter-spots live via **MQTT** (tjeneste fra M0LTE): intet login, hvert spot har allerede lokatorerne for den sendende og den modtagende station. Standardemner: MSK144 på 6 m, 4 m, 2 m, 1,25 m, 70 cm og FSK441 på 2 m (`pskr/filter/v2/band/mode/#`); *Standardemner* gendanner dem. |
| **Indsamlede MS-spots** | – | Tabel over de accepterede spots, nyeste først. |

Hver strøm har vært, port, kommandoer der sendes efter login, *Genforbind*, *Forbind ved opstart*, en konsol og en linje til at sende kommandoer. Skriv dit **kaldesignal til login** øverst. MQTT-kilden har vært, port, emner (ét pr. linje eller adskilt af `;`), *Genforbind* og *Forbind ved opstart* (slået fra som standard) og en konsol med de modtagne spots; dens spots går gennem det samme filter. En bjælke viser status for de fire kilder (grøn prik = forbundet). Sessionerne forbliver åbne, når du skifter sprog eller farveskema.

## Filteret (40 % af vinduet)

- **Valgfrit lokalt filter:** cluster-linjer under **27990,0 kHz** kasseres med det samme (vises ikke, gemmes ikke).
- **1. kriterium – typiske MS-frekvenser:** 50190–50300, 70100–70400, 144290–144399 kHz. Et spot i disse vinduer accepteres også uden modenavnet, medmindre kommentaren angiver en anden udbredelse: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Vinduer og tags kan redigeres.
- **2. kriterium – MS-modes:** uden for vinduerne, eller med et af disse tags, beholdes et spot kun, hvis det indeholder **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digitale modes, der kun bruges til MS) eller **\<MS\>**, med store, små eller blandede bogstaver. Ord kan slås fra, tilføjes og fjernes; hvert har sin tæller.
- **Bånd** 28, 50, 70, 144, 222, 432 MHz; **test af filteret** på en indsat linje; **tællere**.

## Lokatorer og lagring

Manglende lokatorer, eller lokatorer med kun 4 tegn, hentes fra **CALL3**-arkivet (`data/call3.txt`, JTDX-fil, over en million kaldesignaler), som altid har forrang for en lokator med 4 tegn. Accepterede spots gemmes i `data/spot_ms`, én CSV-fil pr. dag, og føder kortet i [Live-trafik](Live-Traffic-da).
