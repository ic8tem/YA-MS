[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · **Magyar** · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

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
| **5. WSJT-X / JTDX / MSHV UDP-n** | 127.0.0.1 : 2237 → 2238 | Mint a LIVETROPOVHF-ben: a program figyeli a digitális program UDP üzeneteit (WSJT-X-ben: Beállítások, Reporting, UDP Server 127.0.0.1 port 2237), és változatlanul továbbítja őket a továbbító porton a többi programnak (GridTracker, JTAlert, napló). Minden dekódolt állomás az állomásod által hallott spot lesz; két másik állomás közötti záró üzenetek (RR73, 73, RRR) a QSO-juk útvonalává válnak. A spotok ugyanazokon a szűrőkön mennek át, mint a többi. |
| **Gyűjtött MS-spotok** | – | Az elfogadott spotok táblázata, a legújabb elöl. |

Minden folyamhoz tartozik gazdagép, port, a bejelentkezés után küldött parancsok, *Újracsatlakozás*, *Csatlakozás indításkor*, egy konzol és egy sor a parancsok küldéséhez. Felül írja be a **hívójelét a bejelentkezéshez**. Az MQTT-forrásnak van gazdagépe, portja, témái (soronként egy vagy `;`-vel elválasztva), *Újracsatlakozás* és *Csatlakozás indításkor* opciója (alapértelmezésben kikapcsolva), valamint egy konzolja a beérkezett spotokkal; spotjai ugyanazon a szűrőn mennek át. Egy sáv mutatja a négy forrás állapotát (zöld pont = csatlakozva). A munkamenetek nyitva maradnak, ha nyelvet vagy színsémát vált.

## A szűrő (az ablak 40 %-a)

- **Opcionális helyi szűrő:** a **27990,0 kHz** alatti clustersorok azonnal elvetésre kerülnek (nem jelennek meg, nem tárolódnak).
- A CW spotokat azonnal eldobja (CW vagy WPM a megjegyzésben, vagy 28000-28070 kHz): nem jelennek meg a konzolon és nem mentődnek, hacsak nincs rajtuk <MS> jelölés. A négyzet kikapcsolható.

CALL3 adatbázis a LIVETROPOVHF szabályaival. A „Frissítés most" letölti a CALL3.TXT-t az MMMonVHF-ről (legalább 100 000 érvényes sor, az előző a data/call3.bak fájlban marad); a „Frissítés magától 12 óránként" beállítással indításkor történik. A fájl felett sorrendben érvényesek: kézi bejegyzések (data/CALL3-MANUALE.TXT), klaszterjavítások (a spotoló saját magáról megadott 6 karakteres lokátora), hozzáadott fájlok (data/CALL3-AGGIUNTE), majd a CALL3.TXT és az élőben tanult 6 karakteres lokátorok (data/LOC6.TXT). A kapott 4 karakteres vagy LL-re, MM-re végződő lokátort az adatbázis 6 karakteres lokátora váltja fel; a hordozható állomásokat (perjellel) csak pontos bejegyzéssel.

Utolsó forrás, mint a LIVETROPOVHF-ben: azokra a hívójelekre, amelyeknek egyetlen más forrásban sincs 6 karakteres lokátora, a program 30 percenként automatikusan a G7VRD nyilvános API-jától (api.g7vrd.co.uk) kérdez, 40 hívójeles csoportokban; mindegyiket legfeljebb naponta egyszer. Csak 6 karakteres lokátort fogad el, nem a négyzet közepét (LL vagy MM), a kapottal azonos négyzetben. Az eredmények a data/CALL3-G7VRD.TXT fájlban vannak, és mint minden javítás, a data/call3.txt fájlba is beíródnak.
- Az 500 km-nél közelebbi állomások közötti spotok azonnal elvetésre kerülnek, mert ekkora távolságon az összeköttetés közvetlen vagy troposzférikus, nem meteor scatter: nem jelennek meg a konzolon és nem tárolódnak. Ha hiányzik egy lokátor, a spot megmarad. A távolság a jelölőnégyzet alatt módosítható.
- **1. feltétel – tipikus MS-frekvenciák:** 50190–50300, 70100–70400, 144290–144399 kHz. Az ezekbe az ablakokba eső spotot a program a mód neve nélkül is elfogadja, kivéve, ha a megjegyzés más terjedési módot jelöl: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Az ablakok és a címkék szerkeszthetők.
- **2. feltétel – MS-módok:** az ablakokon kívül, vagy ha a fenti címkék egyike szerepel, a spot csak akkor marad meg, ha tartalmazza a következők egyikét: **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (csak MS-re használt digitális módok) vagy **\<MS\>**, nagy-, kis- vagy vegyes betűvel. A szavak kikapcsolhatók, hozzáadhatók és törölhetők; mindegyiknek saját számlálója van.
- **Sávok:** 28, 50, 70, 144, 222, 432 MHz; **szűrőteszt** egy beillesztett soron; **számlálók**.

## Lokátorok és tárolás

A hiányzó vagy csak 4 karakteres lokátorokat a program a **CALL3** archívumból veszi (`data/call3.txt`, JTDX-fájl, több mint egymillió hívójellel), amely mindig elsőbbséget élvez a 4 karakteres lokátorral szemben. Az elfogadott spotok a `data/spot_ms` mappába mentődnek, naponként egy CSV-fájlba, és ezek táplálják az [Élő forgalom](Live-Traffic-hu) térképét.
