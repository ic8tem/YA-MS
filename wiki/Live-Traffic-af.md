[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · **Afrikaans** · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Regstreekse verkeer

*Oortjie: Regstreeks en intydse data › Regstreekse verkeer.*

[![Regstreekse verkeer](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Wat dit wys

'n **Azimutale ekwidistante kaart** gesentreer op jou stasie (afstand vanaf die middel = werklike afstand, hoek = azimut) met **al die meteor scatter-verkeer** wat deur [Data-insameling](Data-Collection-af) versamel is. Vir elke kontak teken die program:

- die **pad** tussen die twee stasies, in die kleur van sy band: 28 MHz bruin, 50 MHz groen, 70 MHz siaan, 144 MHz oranje, 222 MHz pienk, 432 MHz violet;
- die twee **stasies** aan die punte van die pad;
- die **wolk**: waar die mees waarskynlike meteoorspore vir daardie pad en daardie tyd gekonsentreer is.

Spots met 'n stasie **buite die kaart** word verwerp. 'n Spot wat **pas aangekom** het (nie ouer as 3 minute nie) **flikker vir een minuut**, sodat nuwe aktiwiteit dadelik uitstaan.

Wys wie luister: driehoeke in die bandkleur merk die stasies wat volgens PSKReporter in die gekose tydvenster MSK144, FSK441, PSK2K of JTMS op 28, 50, 70, 144 en 432 MHz ontvang. 'n Klik op 'n driehoek wys roepsein, lokator, modusse en laaste spot. Die MQTT-stroom in die oortjie Data-insameling moet gekoppel wees.

Ook die aktiewe monitors op die PSKReporter-kaart: leë driehoeke vir stasies wat op die kaart van pskreporter.info in MSK144, FSK441, PSK2K of JTMS verskyn maar nog geen spot ontvang het nie (MQTT stuur net stasies wat iets ontvang). YA-MS bevra die navraagdiens van PSKReporter een modus op 'n slag, elke 3 minute, sodat elke modus elke 12 minute bygewerk word, soos die diens se reëls vra. 'n Klik op die driehoek wys roepsein, lokator, dekodeerprogram en die tyd toe die monitor aktief was. By verstek aan.

Die kaart wys die roepname van albei stasies van elke spot, een keer per stasie. Die projeksie kan azimutaal (gesentreer op jou stasie) of Mercator wees. Die wenk op die kolom Wolk verduidelik die betekenis.

Spots van alle bande word gewys, ook van bande wat nie in Data-insameling gekies is nie (dié word nie gestoor nie). CW-spots en spots tussen stasies wat te naby is, word nie gewys nie as hulle in Data-insameling weggegooi word.

## Hoe die wolk bereken word

Vir elke spot bou die program die pad tussen die twee lokators (dieselfde geometrie as vir jou eie pad, sien [Geometrie en padverlies](Geometry-and-Path-Loss-af)) en tel, op die tyd van die spot, punt vir punt van die E-laag die **spekulêre refleksiebydraes van elke aktiewe swerm** op, met sy ZHR geweeg – dieselfde berekening as die **PREV-sones** van die [hemelkoepel](Sky-View-af). Vir elke kant van die pad wat minstens 15 % van die totaal bevat, is die wolk 'n **ellips**: middelpunt by die geweegde gemiddelde van die punte, halfasse 1,5 keer die vierkantswortels van die eiewaardes van hul verspreiding, hoofas langs die hoof-eievektor. Wanneer geen swerm bydra nie (slegs sporadiese meteore), is die wolke die twee klassieke **hot spots**, met strepies geteken. Die volledige vergelykings is in hoofstuk 10 van die berekeningshandleiding.

## Kontroles

| Kontrole | Betekenis |
|---|---|
| **Kaartradius** | 600–3500 km vanaf jou stasie. |
| **Spots om te wys** | Laaste 15 of 30 minute, laaste uur, laaste 3 uur, laaste 24 uur. |
| **Tabel** | Kontakte op die kaart, nuutste eerste, in die bandkleur; *Wolk* gee die aandeel van refleksies aan die hoofkant, of *sporadies*. |
| **Klik** | Op 'n pad of 'n tabelry: die kontak word uitgelig en die blokkie wys die lokator van die wolk se middelpunt, sy aandeel, grootte en as. |
