[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · **Nederlands** · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Gegevensverzameling

*Tabblad: Live en realtimegegevens › Gegevensverzameling.*

[![Gegevensverzameling](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/nl-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/nl-1_4.png)

## Vier bronnen

Het tabblad verzamelt **meteorscatter-spots** uit drie telnet-stromen en uit de MQTT-feed van PSKReporter, elk in een eigen subtabblad:

| Subtabblad | Standaard | Opmerkingen |
|---|---|---|
| **1. DX-cluster** | on0dxk.dyndns.org : 8000 | Een cluster naar keuze. Op ON0DXK zijn de VHF-banden gefilterd: schakel ze in met `set/filter dxbm/pass 6` (daarna 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmers decoderen zelden MS-modes. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X-cluster met de **PSKReporter**-spots: hier komen de MSK144-decodes van WSJT-X en MSHV binnen. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Live PSKReporter-spots via **MQTT** (dienst van M0LTE): zonder login, elke spot bevat al de locators van het zendende en het ontvangende station. Standaardonderwerpen: MSK144 op 6 m, 4 m, 2 m, 1,25 m, 70 cm en FSK441 op 2 m (`pskr/filter/v2/band/mode/#`); *Standaardonderwerpen* zet ze terug. |
| **5. WSJT-X / JTDX / MSHV via UDP** | 127.0.0.1 : 2237 → 2238 | Zoals in LIVETROPOVHF: het programma luistert naar de UDP-berichten van het digitale programma (in WSJT-X: Instellingen, Reporting, UDP Server 127.0.0.1 poort 2237) en herhaalt ze ongewijzigd op de doorstuurpoort voor de andere programma's (GridTracker, JTAlert, log). Elk gedecodeerd station wordt een spot gehoord door jouw station; afsluitberichten (RR73, 73, RRR) tussen twee andere stations worden het traject van hun QSO. De spots gaan door dezelfde filters als de andere. |
| **Verzamelde MS-spots** | – | Tabel van de geaccepteerde spots, nieuwste bovenaan. |

Elke stroom heeft host, poort, commando's die na het inloggen worden verzonden, *Opnieuw verbinden*, *Verbinden bij opstarten*, een console en een regel om commando's te verzenden. Vul bovenaan je **roepnaam voor het inloggen** in. De MQTT-bron heeft host, poort, onderwerpen (één per regel of gescheiden door `;`), *Opnieuw verbinden* en *Verbinden bij opstarten* (standaard uit) en een console met de ontvangen spots; die spots gaan door hetzelfde filter. Een strook toont de status van de vier bronnen (groene stip = verbonden). De sessies blijven open als je van taal of kleurenschema wisselt.

## Het filter (40 % van het venster)

- **Optioneel lokaal filter:** clusterregels onder **27990,0 kHz** worden meteen weggegooid (niet getoond, niet opgeslagen).
- CW-spots worden meteen weggegooid (CW of WPM in het commentaar, of 28000-28070 kHz): ze verschijnen niet in de console en worden niet opgeslagen, tenzij ze met <MS> gemarkeerd zijn. Het vakje kan uit.

CALL3-database met de regels van LIVETROPOVHF. „Nu bijwerken" downloadt CALL3.TXT van MMMonVHF (minstens 100.000 geldige regels, de vorige blijft in data/call3.bak); met „Zelf elke 12 uur bijwerken" gebeurt dat bij het starten. Boven het bestand gelden, in volgorde: handmatige invoer (data/CALL3-MANUALE.TXT), clustercorrecties (de 6-tekens-locator die de spotter van zichzelf opgeeft), toegevoegde bestanden (data/CALL3-AGGIUNTE), daarna CALL3.TXT en de live geleerde 6-tekens-locators (data/LOC6.TXT). Een ontvangen locator van 4 tekens, of eindigend op LL of MM, wordt vervangen door die van 6 tekens uit de database; portables (met schuine streep) alleen met de exacte invoer.

Laatste bron, zoals in LIVETROPOVHF: voor roepletters zonder 6-tekens-locator in enige andere bron vraagt het programma automatisch elke 30 minuten de openbare G7VRD-API (api.g7vrd.co.uk), in groepen van 40 roepletters; elke roepletter hooguit eens per dag. Alleen een 6-tekens-locator wordt aanvaard, niet het midden van het vak (LL of MM), in hetzelfde vak als de ontvangen. De resultaten staan in data/CALL3-G7VRD.TXT en worden, zoals alle correcties, ook in data/call3.txt geschreven.

Na G7VRD komt de JTDX-laag (data/grid_data.bin, ongeveer 365.000 roepnamen): alleen voor roepnamen zonder 6-tekens-locator in alle andere bronnen, alleen in hetzelfde vak als de ontvangen locator, en nooit geschreven in data/call3.txt.
- Spots tussen stations die minder dan 500 km van elkaar liggen worden direct weggegooid, omdat de verbinding op die afstand direct of troposferisch is en geen meteor scatter: ze verschijnen niet in de console en worden niet opgeslagen. Ontbreekt een locator, dan blijft de spot staan. De afstand is onder het vakje te wijzigen.
- **1e criterium – typische MS-frequenties:** 50190–50300, 70100–70400, 144290–144399 kHz. Een spot in deze vensters wordt ook zonder naam van de mode geaccepteerd, behalve als het commentaar een andere propagatie noemt: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Vensters en aanduidingen zijn aan te passen.
- **2e criterium – MS-modes:** buiten de vensters, of met een van die aanduidingen, wordt een spot alleen bewaard als hij **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digitale modes die alleen voor MS worden gebruikt) of **\<MS\>** bevat, in hoofdletters, kleine letters of gemengd. Woorden kun je uitschakelen, toevoegen en verwijderen; elk heeft zijn eigen teller.
- **Banden** 28, 50, 70, 144, 222, 432 MHz; **filtertest** op een geplakte regel; **tellers**.

## Locators en opslag

Ontbrekende locators, of locators met maar 4 tekens, worden uit het **CALL3**-archief gehaald (`data/call3.txt`, JTDX-bestand, ruim een miljoen roepnamen), dat altijd voorgaat op een locator van 4 tekens. Geaccepteerde spots worden opgeslagen in `data/spot_ms`, één CSV-bestand per dag, en voeden de kaart van [Verkeer live](Live-Traffic-nl).
