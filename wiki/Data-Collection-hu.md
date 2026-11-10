**English** · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh)

# Adatgyűjtés

*Fül: Élő és valós idejű adatok › Adatgyűjtés.*

[![Adatgyűjtés](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Négy forrás

A fül **meteorszórásos spotokat** gyűjt három telnetes folyamból és a PSKReporter MQTT-csatornájából, mindegyiket a saját alfülén:

| Alfül | Alapértelmezés | Megjegyzés |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Tetszőleges cluster. Az ON0DXK-n a VHF-sávok szűrve vannak: engedélyezze őket a `set/filter dxbm/pass 6` paranccsal (majd 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). A skimmerek ritkán dekódolnak MS-módokat. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | A DM4X cluster, amely a **PSKReporter** spotjait továbbítja: ide érkeznek a WSJT-X és az MSHV MSK144-dekódolásai. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Élő PSKReporter-spotok **MQTT**-n keresztül (M0LTE szolgáltatása): bejelentkezés nélkül, minden spot már tartalmazza az adó- és a vevőállomás lokátorát. Alapértelmezett témák: MSK144 a 6 m, 4 m, 2 m, 1,25 m és 70 cm sávon, valamint FSK441 a 2 m sávon (`pskr/filter/v2/band/mode/#`); az *Alapértelmezett témák* gomb visszaállítja őket. |
| **Gyűjtött MS-spotok** | – | Az elfogadott spotok táblázata, a legújabb elöl. |

Minden folyamhoz tartozik gazdagép, port, a bejelentkezés után küldött parancsok, *Újracsatlakozás*, *Csatlakozás indításkor*, egy konzol és egy sor a parancsok küldéséhez. Felül írja be a **hívójelét a bejelentkezéshez**. Az MQTT-forrásnak van gazdagépe, portja, témái (soronként egy vagy `;`-vel elválasztva), *Újracsatlakozás* és *Csatlakozás indításkor* opciója (alapértelmezésben kikapcsolva), valamint egy konzolja a beérkezett spotokkal; spotjai ugyanazon a szűrőn mennek át. Egy sáv mutatja a négy forrás állapotát (zöld pont = csatlakozva). A munkamenetek nyitva maradnak, ha nyelvet vagy színsémát vált.

## A szűrő (az ablak 40 %-a)

- **Opcionális helyi szűrő:** a **27990,0 kHz** alatti clustersorok azonnal elvetésre kerülnek (nem jelennek meg, nem tárolódnak).
- **1. feltétel – tipikus MS-frekvenciák:** 50190–50300, 70100–70400, 144290–144399 kHz. Az ezekbe az ablakokba eső spotot a program a mód neve nélkül is elfogadja, kivéve, ha a megjegyzés más terjedési módot jelöl: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Az ablakok és a címkék szerkeszthetők.
- **2. feltétel – MS-módok:** az ablakokon kívül, vagy ha a fenti címkék egyike szerepel, a spot csak akkor marad meg, ha tartalmazza a következők egyikét: **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (csak MS-re használt digitális módok) vagy **\<MS\>**, nagy-, kis- vagy vegyes betűvel. A szavak kikapcsolhatók, hozzáadhatók és törölhetők; mindegyiknek saját számlálója van.
- **Sávok:** 28, 50, 70, 144, 222, 432 MHz; **szűrőteszt** egy beillesztett soron; **számlálók**.

## Lokátorok és tárolás

A hiányzó vagy csak 4 karakteres lokátorokat a program a **CALL3** archívumból veszi (`data/call3.txt`, JTDX-fájl, több mint egymillió hívójellel), amely mindig elsőbbséget élvez a 4 karakteres lokátorral szemben. Az elfogadott spotok a `data/spot_ms` mappába mentődnek, naponként egy CSV-fájlba, és ezek táplálják az [Élő forgalom](Live-Traffic-hu) térképét.
