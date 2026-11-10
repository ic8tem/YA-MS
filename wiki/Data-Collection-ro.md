[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · **Română** · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [ไทย](Data-Collection-th) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Colectare date

*Fila: Live și date în timp real › Colectare date.*

[![Colectare date](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Trei fluxuri de cluster

Fila colectează **spoturi meteor scatter** din trei fluxuri telnet, fiecare în propria sub-filă:

| Sub-filă | Implicit | Note |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Un cluster la alegere. Pe ON0DXK benzile VHF sunt filtrate: activează-le cu `set/filter dxbm/pass 6` (apoi 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmerele decodează rar modurile MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Clusterul DM4X care transportă spoturile **PSKReporter**: aici sosesc decodările MSK144 din WSJT-X și MSHV. |
| **Spoturi MS colectate** | – | Tabelul spoturilor acceptate, cele mai recente primele. |

Fiecare flux are host, port, comenzile trimise după login, *Reconectează*, *Conectare la pornire*, o consolă și un rând pentru trimiterea comenzilor. Scrie sus **indicativul pentru login**. O bandă arată starea celor trei sesiuni (punct verde = conectat). Sesiunile rămân deschise când schimbi limba sau schema de culori.

## Filtrul (40 % din fereastră)

- **Filtru local opțional:** rândurile clusterului sub **27990,0 kHz** sunt respinse imediat (nu sunt afișate, nu sunt memorate).
- **Criteriul 1 – frecvențe MS tipice:** 50190–50300, 70100–70400, 144290–144399 kHz. Un spot din aceste ferestre este acceptat chiar și fără numele modului, cu excepția cazului în care comentariul declară altă propagare: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Ferestrele și etichetele pot fi editate.
- **Criteriul 2 – moduri MS:** în afara ferestrelor sau cu una dintre acele etichete, un spot este păstrat doar dacă conține **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (moduri digitale folosite doar pentru MS) sau **\<MS\>**, cu litere mari, mici sau amestecate. Cuvintele pot fi dezactivate, adăugate și eliminate; fiecare are contorul său.
- **Benzi** 28, 50, 70, 144, 222, 432 MHz; **testul filtrului** pe un rând lipit; **contoare**.

## Locatori și memorare

Locatorii lipsă sau cei cu doar 4 caractere se iau din arhiva **CALL3** (`data/call3.txt`, fișier JTDX, peste un milion de indicative), care are întotdeauna prioritate față de un locator cu 4 caractere. Spoturile acceptate se salvează în `data/spot_ms`, câte un fișier CSV pe zi, și alimentează harta [Trafic în direct](Live-Traffic-ro).
