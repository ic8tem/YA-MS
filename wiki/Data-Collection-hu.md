[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · **Magyar** · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [ไทย](Data-Collection-th) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Adatgyűjtés

*Fül: Élő és valós idejű adatok › Adatgyűjtés.*

[![Adatgyűjtés](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Három cluster-adatfolyam

A fül **meteor scatter spotokat** gyűjt három telnetes adatfolyamból, mindegyiket saját alfülön:

| Alfül | Alapértelmezés | Megjegyzés |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Tetszőlegesen választott cluster. Az ON0DXK-n a VHF-sávok szűrve vannak: engedélyezze őket a `set/filter dxbm/pass 6` paranccsal (majd 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). A skimmerek ritkán dekódolnak MS-üzemmódokat. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | A **PSKReporter** spotjait továbbító DM4X cluster: ide érkeznek a WSJT-X és az MSHV MSK144-dekódolásai. |
| **Gyűjtött MS-spotok** | – | Az elfogadott spotok táblázata, a legújabb elöl. |

Minden adatfolyamnak van gazdagépe, portja, a bejelentkezés után küldött parancsai, *Újracsatlakozás* és *Csatlakozás induláskor* beállítása, konzolja és egy sora a parancsok küldéséhez. Írja be felül a **bejelentkezési hívójelét**. Egy sáv mutatja a három munkamenet állapotát (zöld pont = csatlakozva). A munkamenetek nyitva maradnak, amikor nyelvet vagy színsémát vált.

## A szűrő (az ablak 40 %-a)

- **Választható helyi szűrő:** a **27990,0 kHz** alatti cluster-sorokat a program azonnal elveti (nem jelennek meg és nem tárolódnak).
- **1. szempont – jellemző MS-frekvenciák:** 50190–50300, 70100–70400, 144290–144399 kHz. Az ezekbe az ablakokba eső spot az üzemmód neve nélkül is elfogadásra kerül, kivéve, ha a megjegyzés más terjedési módot jelöl: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Az ablakok és a címkék szerkeszthetők.
- **2. szempont – MS-üzemmódok:** az ablakokon kívül, vagy ha a fenti címkék egyike szerepel, egy spot csak akkor marad meg, ha tartalmazza az **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (csak MS-re használt digitális üzemmódok) vagy a **\<MS\>** szót, nagy-, kis- vagy vegyes betűkkel. A szavak kikapcsolhatók, hozzáadhatók és törölhetők; mindegyiknek saját számlálója van.
- **Sávok** 28, 50, 70, 144, 222, 432 MHz; **szűrőpróba** egy beillesztett soron; **számlálók**.

## Lokátorok és tárolás

A hiányzó vagy csak 4 karakteres lokátorokat a program a **CALL3** archívumból veszi (`data/call3.txt`, JTDX-fájl, több mint egymillió hívójellel), amely mindig elsőbbséget élvez a 4 karakteres lokátorral szemben. Az elfogadott spotok a `data/spot_ms` mappába kerülnek, naponta egy CSV-fájlba, és ezek táplálják az [Élő forgalom](Live-Traffic-hu) térképét.
