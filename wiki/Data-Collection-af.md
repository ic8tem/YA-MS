[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · **Afrikaans** · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh)

# Data-insameling

*Oortjie: Regstreeks en intydse data › Data-insameling.*

[![Data-insameling](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Drie clusterstrome

Die oortjie versamel **meteor scatter-spots** uit drie telnet-strome, elkeen in sy eie sub-oortjie:

| Sub-oortjie | Verstek | Opmerkings |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | 'n Cluster na keuse. Op ON0DXK word die VHF-bande gefiltreer: skakel hulle aan met `set/filter dxbm/pass 6` (dan 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmers dekodeer selde MS-modusse. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X-cluster wat die **PSKReporter**-spots dra: die MSK144-dekoderings van WSJT-X en MSHV kom hier aan. |
| **Versamelde MS-spots** | – | Tabel van die aanvaarde spots, nuutste eerste. |

Elke stroom het 'n gasheer, poort, opdragte wat ná die aanmelding gestuur word, *Herkoppel*, *Koppel by opstart*, 'n konsole en 'n reël om opdragte te stuur. Skryf jou **roepnaam vir aanmelding** bo-aan. 'n Strook wys die toestand van die drie sessies (groen kol = gekoppel). Die sessies bly oop wanneer jy die taal of kleurskema verander.

## Die filter (40 % van die venster)

- **Opsionele plaaslike filter:** clusterreëls onder **27990,0 kHz** word dadelik verwerp (nie gewys nie, nie gestoor nie).
- **1ste kriterium – tipiese MS-frekwensies:** 50190–50300, 70100–70400, 144290–144399 kHz. 'n Spot in hierdie vensters word aanvaar selfs sonder die modusnaam, tensy die kommentaar 'n ander voortplanting verklaar: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Vensters en etikette kan gewysig word.
- **2de kriterium – MS-modusse:** buite die vensters, of met een van daardie etikette, word 'n spot slegs behou as dit **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digitale modusse wat slegs vir MS gebruik word) of **\<MS\>** bevat, in hoof-, klein- of gemengde letters. Woorde kan afgeskakel, bygevoeg en verwyder word; elkeen het sy teller.
- **Bande** 28, 50, 70, 144, 222, 432 MHz; **filtertoets** op 'n geplakte reël; **tellers**.

## Lokators en berging

Ontbrekende lokators, of lokators met slegs 4 karakters, word uit die **CALL3**-databasis geneem (`data/call3.txt`, JTDX-lêer, meer as 'n miljoen roepname), wat altyd voorrang bo 'n lokator van 4 karakters kry. Aanvaarde spots word in `data/spot_ms` gestoor, een CSV-lêer per dag, en voed die kaart van [Regstreekse verkeer](Live-Traffic-af).
