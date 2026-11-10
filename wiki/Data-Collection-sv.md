[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · **Svenska** · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [ไทย](Data-Collection-th) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Datainsamling

*Flik: Live och realtidsdata › Datainsamling.*

[![Datainsamling](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Tre klusterflöden

Fliken samlar in **meteorscatter-spots** från tre telnetflöden, vart och ett i sin egen underflik:

| Underflik | Standard | Anmärkningar |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Ett kluster som du väljer. På ON0DXK är VHF-banden filtrerade: aktivera dem med `set/filter dxbm/pass 6` (sedan 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmers avkodar sällan MS-moder. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X:s kluster som för vidare spots från **PSKReporter**: hit kommer MSK144-avkodningarna från WSJT-X och MSHV. |
| **Insamlade MS-spots** | – | Tabell över de godkända spotsen, nyaste först. |

Varje flöde har värd, port, kommandon som skickas efter inloggningen, *Återanslut*, *Anslut vid start*, en konsol och en rad för att skicka kommandon. Skriv in din **anropssignal för inloggning** högst upp. En list visar tillståndet för de tre sessionerna (grön punkt = ansluten). Sessionerna förblir öppna när du byter språk eller färgschema.

## Filtret (40 % av fönstret)

- **Valfritt lokalt filter:** klusterrader under **27990,0 kHz** kasseras direkt (visas inte, sparas inte).
- **1:a kriteriet – typiska MS-frekvenser:** 50190–50300, 70100–70400, 144290–144399 kHz. En spot i dessa fönster godkänns även utan modens namn, såvida inte kommentaren anger en annan utbredning: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Fönster och taggar kan redigeras.
- **2:a kriteriet – MS-moder:** utanför fönstren, eller med en av de taggarna, behålls en spot endast om den innehåller **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digitala moder som bara används för MS) eller **\<MS\>**, med versaler, gemener eller blandat. Ord kan stängas av, läggas till och tas bort; vart och ett har sin räknare.
- **Band** 28, 50, 70, 144, 222, 432 MHz; **test av filtret** på en inklistrad rad; **räknare**.

## Lokatorer och lagring

Saknade lokatorer, eller lokatorer med bara 4 tecken, hämtas från arkivet **CALL3** (`data/call3.txt`, JTDX-fil, över en miljon anropssignaler), som alltid har företräde framför en lokator med 4 tecken. Godkända spots sparas i `data/spot_ms`, en CSV-fil per dag, och matar kartan [Trafik live](Live-Traffic-sv).
