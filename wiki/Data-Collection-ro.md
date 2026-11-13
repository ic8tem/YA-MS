[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · **Română** · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Colectare date

*Filă: Date live și în timp real › Colectare date.*

[![Colectare date](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Patru surse

Fila colectează **spoturi meteor-scatter** din trei fluxuri telnet și din fluxul MQTT PSKReporter, fiecare în propria subfilă:

| Subfilă | Implicit | Note |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Un cluster ales de dumneavoastră. Pe ON0DXK benzile VHF sunt filtrate: activați-le cu `set/filter dxbm/pass 6` (apoi 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmer-ele decodează rar modurile MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Clusterul DM4X care transportă spoturile **PSKReporter**: decodările MSK144 ale WSJT-X și MSHV ajung aici. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Spoturi PSKReporter live prin **MQTT** (serviciu oferit de M0LTE): fără autentificare, fiecare spot conține deja locatorii stației care emite și ai celei care recepționează. Topicuri implicite: MSK144 pe 6 m, 4 m, 2 m, 1,25 m, 70 cm și FSK441 pe 2 m (`pskr/filter/v2/band/mode/#`); *Topicuri implicite* le restabilește. |
| **Spoturi MS colectate** | – | Tabelul spoturilor acceptate, cele mai noi primele. |

Fiecare flux are host, port, comenzi trimise după autentificare, *Reconectare*, *Conectare la pornire*, o consolă și o linie pentru trimiterea comenzilor. Scrieți **indicativul pentru autentificare** în partea de sus. Sursa MQTT are host, port, topicuri (câte unul pe linie sau separate prin `;`), *Reconectare* și *Conectare la pornire* (dezactivat implicit) și o consolă cu spoturile primite; spoturile sale trec prin același filtru. O bandă arată starea celor patru surse (punct verde = conectat). Sesiunile rămân deschise când schimbați limba sau schema de culori.

## Filtrul (40 % din fereastră)

- **Filtru local opțional:** liniile de cluster sub **27990,0 kHz** sunt eliminate imediat (nu sunt afișate, nu sunt stocate).
- Spoturile CW sunt eliminate imediat (CW sau WPM în comentariu, sau 28000-28070 kHz): nu apar în consolă și nu se salvează, cu excepția celor marcate <MS>. Căsuța se poate dezactiva.

Baza CALL3 cu regulile LIVETROPOVHF. „Actualizează acum" descarcă CALL3.TXT de la MMMonVHF (cel puțin 100.000 de rânduri valide, cel anterior rămâne în data/call3.bak); cu „Actualizează singur la fiecare 7 zile" se face la pornire. Deasupra fișierului contează, în ordine: intrările manuale (data/CALL3-MANUALE.TXT), corecturile din cluster (locatorul de 6 caractere pe care cel care face spotul îl declară despre sine), fișierele adăugate (data/CALL3-AGGIUNTE), apoi CALL3.TXT și locatoarele de 6 caractere învățate live (data/LOC6.TXT). Un locator primit de 4 caractere, sau terminat în LL ori MM, se înlocuiește cu cel de 6 caractere din bază; stațiile portabile (cu bară) doar cu intrarea exactă.
- Spoturile între stații aflate la mai puțin de 500 km se elimină imediat, deoarece la această distanță legătura este directă sau troposferică, nu meteor scatter: nu apar în consolă și nu se memorează. Dacă lipsește un locator, spotul rămâne. Distanța se schimbă sub căsuță.
- **Primul criteriu – frecvențe MS tipice:** 50190–50300, 70100–70400, 144290–144399 kHz. Un spot în aceste ferestre este acceptat chiar și fără numele modului, cu excepția cazului în care comentariul declară o altă propagare: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Ferestrele și etichetele pot fi editate.
- **Al doilea criteriu – moduri MS:** în afara ferestrelor, sau cu una dintre acele etichete, un spot este păstrat doar dacă conține **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (moduri digitale folosite doar pentru MS) sau **\<MS\>**, cu majuscule, minuscule sau amestecat. Cuvintele pot fi dezactivate, adăugate și eliminate; fiecare are contorul său.
- **Benzi** 28, 50, 70, 144, 222, 432 MHz; **testul filtrului** pe o linie lipită; **contoare**.

## Locatori și stocare

Locatorii lipsă, sau cei cu doar 4 caractere, sunt luați din arhiva **CALL3** (`data/call3.txt`, fișierul JTDX, peste un milion de indicative), care are întotdeauna prioritate față de un locator de 4 caractere. Spoturile acceptate sunt salvate în `data/spot_ms`, câte un fișier CSV pe zi, și alimentează harta [Trafic live](Live-Traffic-ro).
