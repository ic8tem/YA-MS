[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · **Svenska** · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Datainsamling

*Flik: Live och realtidsdata › Datainsamling.*

[![Datainsamling](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Fyra källor

Fliken samlar in **meteorscatter-spots** från tre telnetflöden och från PSKReporters MQTT-flöde, vart och ett i sin egen underflik:

| Underflik | Standard | Anmärkningar |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Ett kluster som du väljer. På ON0DXK är VHF-banden filtrerade: aktivera dem med `set/filter dxbm/pass 6` (sedan 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmers avkodar sällan MS-moder. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X:s kluster som för vidare spots från **PSKReporter**: hit kommer MSK144-avkodningarna från WSJT-X och MSHV. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | PSKReporter-spots live via **MQTT** (tjänst från M0LTE): ingen inloggning, varje spot har redan lokatorerna för den sändande och den mottagande stationen. Standardämnen: MSK144 på 6 m, 4 m, 2 m, 1,25 m, 70 cm och FSK441 på 2 m (`pskr/filter/v2/band/mode/#`); *Standardämnen* återställer dem. |
| **5. WSJT-X / JTDX / MSHV via UDP** | 127.0.0.1 : 2237 → 2238 | Som i LIVETROPOVHF: programmet lyssnar på UDP-meddelandena från det digitala programmet (i WSJT-X: Inställningar, Reporting, UDP Server 127.0.0.1 port 2237) och upprepar dem oförändrade på vidarebefordringsporten för de andra programmen (GridTracker, JTAlert, logg). Varje avkodad station blir en spott hörd av din station; avslutningsmeddelanden (RR73, 73, RRR) mellan två andra stationer blir sträckan för deras QSO. Spottarna går genom samma filter som de andra. |
| **Insamlade MS-spots** | – | Tabell över de godkända spotsen, nyaste först. |

Varje flöde har värd, port, kommandon som skickas efter inloggningen, *Återanslut*, *Anslut vid start*, en konsol och en rad för att skicka kommandon. Skriv in din **anropssignal för inloggning** högst upp. MQTT-källan har värd, port, ämnen (ett per rad eller åtskilda med `;`), *Återanslut* och *Anslut vid start* (av som standard) och en konsol med de mottagna spotsen; dess spots går genom samma filter. En list visar tillståndet för de fyra källorna (grön punkt = ansluten). Sessionerna förblir öppna när du byter språk eller färgschema.

## Filtret (40 % av fönstret)

- **Valfritt lokalt filter:** klusterrader under **27990,0 kHz** kasseras direkt (visas inte, sparas inte).
- CW-spottar kastas direkt (CW eller WPM i kommentaren, eller 28000-28070 kHz): de visas inte i konsolen och sparas inte, utom de som är märkta <MS>. Rutan kan stängas av.

CALL3-databas med LIVETROPOVHF:s regler. ”Uppdatera nu” laddar ner CALL3.TXT från MMMonVHF (minst 100 000 giltiga rader, den föregående blir kvar i data/call3.bak); med ”Uppdatera själv var 12:e timme” sker det vid start. Över filen gäller i ordning: handposter (data/CALL3-MANUALE.TXT), klusterkorrigeringar (den 6-teckens lokator som spottaren anger för sig själv), tillagda filer (data/CALL3-AGGIUNTE), sedan CALL3.TXT och 6-teckens lokatorer inlärda live (data/LOC6.TXT). En mottagen lokator med 4 tecken, eller som slutar på LL eller MM, ersätts med den 6-teckens från databasen; portabla (med snedstreck) bara med exakt post.

Sista källan, som i LIVETROPOVHF: för anropssignaler utan 6-teckens lokator i någon annan källa frågar programmet automatiskt var 30:e minut G7VRD:s öppna API (api.g7vrd.co.uk), i grupper om 40 anropssignaler; varje anropssignal högst en gång om dagen. Endast en 6-teckens lokator godtas, inte rutans mitt (LL eller MM), i samma ruta som den mottagna. Resultaten finns i data/CALL3-G7VRD.TXT och skrivs, som alla korrigeringar, även in i data/call3.txt.
- Spottar mellan stationer närmare än 500 km kastas direkt, eftersom förbindelsen på det avståndet är direkt eller troposfärisk och inte meteor scatter: de visas inte i konsolen och sparas inte. Saknas en lokator behålls spotten. Avståndet ändras under rutan.
- **1:a kriteriet – typiska MS-frekvenser:** 50190–50300, 70100–70400, 144290–144399 kHz. En spot i dessa fönster godkänns även utan modens namn, såvida inte kommentaren anger en annan utbredning: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Fönster och taggar kan redigeras.
- **2:a kriteriet – MS-moder:** utanför fönstren, eller med en av de taggarna, behålls en spot endast om den innehåller **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digitala moder som bara används för MS) eller **\<MS\>**, med versaler, gemener eller blandat. Ord kan stängas av, läggas till och tas bort; vart och ett har sin räknare.
- **Band** 28, 50, 70, 144, 222, 432 MHz; **test av filtret** på en inklistrad rad; **räknare**.

## Lokatorer och lagring

Saknade lokatorer, eller lokatorer med bara 4 tecken, hämtas från arkivet **CALL3** (`data/call3.txt`, JTDX-fil, över en miljon anropssignaler), som alltid har företräde framför en lokator med 4 tecken. Godkända spots sparas i `data/spot_ms`, en CSV-fil per dag, och matar kartan [Trafik live](Live-Traffic-sv).
