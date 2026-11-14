[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · **Norsk** · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Datainnsamling

*Fane: Direkte og sanntidsdata › Datainnsamling.*

[![Datainnsamling](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Fire kilder

Fanen samler **meteor scatter-spot** fra tre telnet-strømmer og fra MQTT-strømmen til PSKReporter, hver i sin egen underfane:

| Underfane | Standard | Merknader |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | En valgfri cluster. På ON0DXK er VHF-båndene filtrert: aktiver dem med `set/filter dxbm/pass 6` (deretter 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmere dekoder sjelden MS-modi. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X-cluster med **PSKReporter**-spot: MSK144-dekodingene fra WSJT-X og MSHV kommer hit. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | PSKReporter-spot direkte via **MQTT** (tjeneste fra M0LTE): ingen innlogging, hvert spot har allerede lokatorene til sendende og mottakende stasjon. Standardemner: MSK144 på 6 m, 4 m, 2 m, 1,25 m, 70 cm og FSK441 på 2 m (`pskr/filter/v2/band/mode/#`); *Standardemner* gjenoppretter dem. |
| **5. WSJT-X / JTDX / MSHV via UDP** | 127.0.0.1 : 2237 → 2238 | Som i LIVETROPOVHF: programmet lytter på UDP-meldingene fra det digitale programmet (i WSJT-X: Innstillinger, Reporting, UDP Server 127.0.0.1 port 2237) og gjentar dem uendret på videresendingsporten for de andre programmene (GridTracker, JTAlert, logg). Hver dekodet stasjon blir en spot hørt av din stasjon; avslutningsmeldinger (RR73, 73, RRR) mellom to andre stasjoner blir strekningen for deres QSO. Spottene går gjennom de samme filtrene som de andre. |
| **Innsamlede MS-spot** | – | Tabell over godtatte spot, nyeste først. |

Hver strøm har vert, port, kommandoer som sendes etter innlogging, *Koble til på nytt*, *Koble til ved oppstart*, en konsoll og en linje for å sende kommandoer. Skriv **kallesignalet for innlogging** øverst. MQTT-kilden har vert, port, emner (ett per linje eller skilt med `;`), *Koble til på nytt* og *Koble til ved oppstart* (av som standard) og en konsoll med de mottatte spotene; spotene derfra går gjennom det samme filteret. En stripe viser tilstanden til de fire kildene (grønn prikk = tilkoblet). Øktene holdes åpne når du bytter språk eller fargeskjema.

## Filteret (40 % av vinduet)

- **Valgfritt lokalt filter:** clusterlinjer under **27990,0 kHz** forkastes med en gang (vises ikke, lagres ikke).
- CW-spotter forkastes med en gang (CW eller WPM i kommentaren, eller 28000-28070 kHz): de vises ikke i konsollen og lagres ikke, unntatt de som er merket <MS>. Boksen kan slås av.

CALL3-database med reglene fra LIVETROPOVHF. «Oppdater nå» laster ned CALL3.TXT fra MMMonVHF (minst 100 000 gyldige linjer, den forrige blir liggende i data/call3.bak); med «Oppdater selv hver 7. dag» skjer det ved oppstart. Over filen gjelder i rekkefølge: håndoppføringer (data/CALL3-MANUALE.TXT), klyngekorreksjoner (6-tegns lokatoren som spotteren oppgir for seg selv), tillagte filer (data/CALL3-AGGIUNTE), så CALL3.TXT og 6-tegns lokatorer lært live (data/LOC6.TXT). En mottatt lokator med 4 tegn, eller som slutter på LL eller MM, erstattes med 6-tegns lokatoren fra databasen; portable (med skråstrek) bare med eksakt oppføring.

Siste kilde, som i LIVETROPOVHF: for kallesignaler uten 6-tegns lokator i noen annen kilde spør programmet automatisk hver 6. time det offentlige G7VRD-API-et (api.g7vrd.co.uk), i grupper på 40 kallesignaler; hvert kallesignal høyst én gang om dagen. Bare en 6-tegns lokator godtas, ikke rutens midte (LL eller MM), i samme rute som den mottatte. Resultatene ligger i data/CALL3-G7VRD.TXT og skrives, som alle korreksjoner, også inn i data/call3.txt.
- Spotter mellom stasjoner nærmere enn 500 km forkastes straks, fordi forbindelsen på den avstanden er direkte eller troposfærisk og ikke meteor scatter: de vises ikke i konsollen og lagres ikke. Mangler en lokator, beholdes spotten. Avstanden endres under avkrysningsboksen.
- **1. kriterium – typiske MS-frekvenser:** 50190–50300, 70100–70400, 144290–144399 kHz. Et spot i disse vinduene godtas også uten modusnavn, med mindre kommentaren oppgir en annen utbredelse: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Vinduer og tagger kan redigeres.
- **2. kriterium – MS-modi:** utenfor vinduene, eller med en av disse taggene, beholdes et spot bare hvis det inneholder **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digitale modi som bare brukes til MS) eller **\<MS\>**, med store, små eller blandede bokstaver. Ord kan slås av, legges til og fjernes; hvert har sin teller.
- **Bånd** 28, 50, 70, 144, 222, 432 MHz; **test av filteret** på en innlimt linje; **tellere**.

## Lokatorer og lagring

Manglende lokatorer, eller lokatorer med bare 4 tegn, hentes fra **CALL3**-arkivet (`data/call3.txt`, JTDX-fil, over en million kallesignaler), som alltid går foran en lokator med 4 tegn. Godtatte spot lagres i `data/spot_ms`, én CSV-fil per dag, og mater kartet i [Trafikk direkte](Live-Traffic-nb).
