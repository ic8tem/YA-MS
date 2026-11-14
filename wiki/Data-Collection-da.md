[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · **Dansk** · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

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
| **5. WSJT-X / JTDX / MSHV via UDP** | 127.0.0.1 : 2237 → 2238 | Som i LIVETROPOVHF: programmet lytter til UDP-beskederne fra det digitale program (i WSJT-X: Indstillinger, Reporting, UDP Server 127.0.0.1 port 2237) og gentager dem uændret på videresendelsesporten til de andre programmer (GridTracker, JTAlert, log). Hver dekodet station bliver et spot hørt af din station; afslutningsbeskeder (RR73, 73, RRR) mellem to andre stationer bliver strækningen for deres QSO. Spottene går gennem de samme filtre som de andre. |
| **Indsamlede MS-spots** | – | Tabel over de accepterede spots, nyeste først. |

Hver strøm har vært, port, kommandoer der sendes efter login, *Genforbind*, *Forbind ved opstart*, en konsol og en linje til at sende kommandoer. Skriv dit **kaldesignal til login** øverst. MQTT-kilden har vært, port, emner (ét pr. linje eller adskilt af `;`), *Genforbind* og *Forbind ved opstart* (slået fra som standard) og en konsol med de modtagne spots; dens spots går gennem det samme filter. En bjælke viser status for de fire kilder (grøn prik = forbundet). Sessionerne forbliver åbne, når du skifter sprog eller farveskema.

## Filteret (40 % af vinduet)

- **Valgfrit lokalt filter:** cluster-linjer under **27990,0 kHz** kasseres med det samme (vises ikke, gemmes ikke).
- CW-spots kasseres med det samme (CW eller WPM i kommentaren, eller 28000-28070 kHz): de vises ikke i konsollen og gemmes ikke, undtagen dem der er mærket <MS>. Feltet kan slås fra.

CALL3-database med reglerne fra LIVETROPOVHF. »Opdatér nu« henter CALL3.TXT fra MMMonVHF (mindst 100.000 gyldige linjer, den forrige bliver i data/call3.bak); med »Opdatér selv hver 7. dag« sker det ved start. Over filen gælder i rækkefølge: håndindtastninger (data/CALL3-MANUALE.TXT), cluster-rettelser (den 6-tegns locator, som spotteren angiver for sig selv), tilføjede filer (data/CALL3-AGGIUNTE), derefter CALL3.TXT og 6-tegns locatorer lært live (data/LOC6.TXT). En modtaget locator på 4 tegn, eller som ender på LL eller MM, erstattes af den 6-tegns fra databasen; portable (med skråstreg) kun med den præcise indtastning.

Sidste kilde, som i LIVETROPOVHF: for kaldesignaler uden 6-tegns locator i nogen anden kilde spørger programmet automatisk hver 6. time G7VRD's offentlige API (api.g7vrd.co.uk), i grupper på 40 kaldesignaler; hvert kaldesignal højst én gang om dagen. Kun en 6-tegns locator accepteres, ikke feltets midte (LL eller MM), i samme felt som den modtagne. Resultaterne ligger i data/CALL3-G7VRD.TXT og skrives, som alle rettelser, også ind i data/call3.txt.
- Spots mellem stationer tættere end 500 km kasseres straks, fordi forbindelsen på den afstand er direkte eller troposfærisk og ikke meteor scatter: de vises ikke i konsollen og gemmes ikke. Mangler en locator, beholdes spottet. Afstanden ændres under feltet.
- **1. kriterium – typiske MS-frekvenser:** 50190–50300, 70100–70400, 144290–144399 kHz. Et spot i disse vinduer accepteres også uden modenavnet, medmindre kommentaren angiver en anden udbredelse: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Vinduer og tags kan redigeres.
- **2. kriterium – MS-modes:** uden for vinduerne, eller med et af disse tags, beholdes et spot kun, hvis det indeholder **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digitale modes, der kun bruges til MS) eller **\<MS\>**, med store, små eller blandede bogstaver. Ord kan slås fra, tilføjes og fjernes; hvert har sin tæller.
- **Bånd** 28, 50, 70, 144, 222, 432 MHz; **test af filteret** på en indsat linje; **tællere**.

## Lokatorer og lagring

Manglende lokatorer, eller lokatorer med kun 4 tegn, hentes fra **CALL3**-arkivet (`data/call3.txt`, JTDX-fil, over en million kaldesignaler), som altid har forrang for en lokator med 4 tegn. Accepterede spots gemmes i `data/spot_ms`, én CSV-fil pr. dag, og føder kortet i [Live-trafik](Live-Traffic-da).
