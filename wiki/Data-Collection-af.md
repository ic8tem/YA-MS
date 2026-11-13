[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · **Afrikaans** · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Data-insameling

*Oortjie: Regstreeks en intydse data › Data-insameling.*

[![Data-insameling](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Vier bronne

Die oortjie versamel **meteor scatter-spots** uit drie telnet-strome en uit die PSKReporter MQTT-stroom, elkeen in sy eie sub-oortjie:

| Sub-oortjie | Verstek | Opmerkings |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | 'n Cluster na keuse. Op ON0DXK word die VHF-bande gefiltreer: skakel hulle aan met `set/filter dxbm/pass 6` (dan 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmers dekodeer selde MS-modusse. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X-cluster wat die **PSKReporter**-spots dra: die MSK144-dekoderings van WSJT-X en MSHV kom hier aan. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Intydse PSKReporter-spots via **MQTT** ('n diens van M0LTE): geen aanmelding nie, elke spot bevat reeds die lokators van die uitsaai- en die ontvangstasie. Verstekonderwerpe: MSK144 op 6 m, 4 m, 2 m, 1,25 m, 70 cm en FSK441 op 2 m (`pskr/filter/v2/band/mode/#`); *Verstekonderwerpe* stel hulle terug. |
| **Versamelde MS-spots** | – | Tabel van die aanvaarde spots, nuutste eerste. |

Elke stroom het 'n gasheer, poort, opdragte wat ná die aanmelding gestuur word, *Herkoppel*, *Koppel by opstart*, 'n konsole en 'n reël om opdragte te stuur. Skryf jou **roepnaam vir aanmelding** bo-aan. Die MQTT-bron het 'n gasheer, poort, onderwerpe (een per reël of geskei deur `;`), *Herkoppel* en *Koppel by opstart* (by verstek af) en 'n konsole met die ontvangde spots; sy spots gaan deur dieselfde filter. 'n Strook wys die toestand van die vier bronne (groen kol = gekoppel). Die sessies bly oop wanneer jy die taal of kleurskema verander.

## Die filter (40 % van die venster)

- **Opsionele plaaslike filter:** clusterreëls onder **27990,0 kHz** word dadelik verwerp (nie gewys nie, nie gestoor nie).
- CW-spots word dadelik weggegooi (CW of WPM in die kommentaar, of 28000-28070 kHz): hulle verskyn nie in die konsole nie en word nie gestoor nie, tensy hulle met <MS> gemerk is. Die blokkie kan afgeskakel word.

CALL3-databasis met die reëls van LIVETROPOVHF. "Werk nou by" laai CALL3.TXT van MMMonVHF af (ten minste 100 000 geldige reëls, die vorige bly in data/call3.bak); met "Werk self elke 7 dae by" gebeur dit by die begin. Bo die lêer geld in volgorde: handinskrywings (data/CALL3-MANUALE.TXT), cluster-regstellings (die 6-karakter-lokator wat die spotter vir homself verklaar), bygevoegde lêers (data/CALL3-AGGIUNTE), dan CALL3.TXT en 6-karakter-lokators wat regstreeks geleer is (data/LOC6.TXT). 'n Ontvangde 4-karakter-lokator, of een wat op LL of MM eindig, word deur die 6-karakter-een uit die databasis vervang; draagbares (met 'n skuinsstreep) net met die presiese inskrywing.

Laaste bron, soos in LIVETROPOVHF: vir roepname sonder 'n 6-karakter-lokator in enige ander bron vra die program in die agtergrond die openbare G7VRD-API (api.g7vrd.co.uk). Net 'n 6-karakter-lokator word aanvaar, nie die middel van die vierkant (LL of MM) nie, in dieselfde vierkant as die ontvangde een; hoogstens 40 roepname per minuut, elkeen een keer per dag. Die resultate is in data/CALL3-G7VRD.TXT.
- Spots tussen stasies nader as 500 km word dadelik weggegooi, want op daardie afstand is die verbinding direk of troposferies en nie meteor scatter nie: hulle verskyn nie in die konsole nie en word nie gestoor nie. As 'n lokator ontbreek, bly die spot. Die afstand word onder die blokkie verander.
- **1ste kriterium – tipiese MS-frekwensies:** 50190–50300, 70100–70400, 144290–144399 kHz. 'n Spot in hierdie vensters word aanvaar selfs sonder die modusnaam, tensy die kommentaar 'n ander voortplanting verklaar: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Vensters en etikette kan gewysig word.
- **2de kriterium – MS-modusse:** buite die vensters, of met een van daardie etikette, word 'n spot slegs behou as dit **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digitale modusse wat slegs vir MS gebruik word) of **\<MS\>** bevat, in hoof-, klein- of gemengde letters. Woorde kan afgeskakel, bygevoeg en verwyder word; elkeen het sy teller.
- **Bande** 28, 50, 70, 144, 222, 432 MHz; **filtertoets** op 'n geplakte reël; **tellers**.

## Lokators en berging

Ontbrekende lokators, of lokators met slegs 4 karakters, word uit die **CALL3**-databasis geneem (`data/call3.txt`, JTDX-lêer, meer as 'n miljoen roepname), wat altyd voorrang bo 'n lokator van 4 karakters kry. Aanvaarde spots word in `data/spot_ms` gestoor, een CSV-lêer per dag, en voed die kaart van [Regstreekse verkeer](Live-Traffic-af).
