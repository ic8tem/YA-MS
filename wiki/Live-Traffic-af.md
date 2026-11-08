**English** · [Русский](Live-Traffic-ru) · [Deutsch](Live-Traffic-de) · [日本語](Live-Traffic-ja)

# Regstreekse verkeer

*Oortjie: Regstreeks en intydse data › Regstreekse verkeer.*

[![Regstreekse verkeer](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Wat dit wys

'n **Azimutale ekwidistante kaart** gesentreer op jou stasie (afstand vanaf die middel = werklike afstand, hoek = azimut) met **al die meteor scatter-verkeer** wat deur [Data-insameling](Data-Collection-af) versamel is. Vir elke kontak teken die program:

- die **pad** tussen die twee stasies, in die kleur van sy band: 28 MHz bruin, 50 MHz groen, 70 MHz siaan, 144 MHz oranje, 222 MHz pienk, 432 MHz violet;
- die twee **stasies** aan die punte van die pad;
- die **wolk**: waar die mees waarskynlike meteoorspore vir daardie pad en daardie tyd gekonsentreer is.

Spots met 'n stasie **buite die kaart** word verwerp. 'n Spot wat **pas aangekom** het (nie ouer as 3 minute nie) **flikker vir een minuut**, sodat nuwe aktiwiteit dadelik uitstaan.

## Hoe die wolk bereken word

Vir elke spot bou die program die pad tussen die twee lokators (dieselfde geometrie as vir jou eie pad, sien [Geometrie en padverlies](Geometry-and-Path-Loss-af)) en tel, op die tyd van die spot, punt vir punt van die E-laag die **spekulêre refleksiebydraes van elke aktiewe swerm** op, met sy ZHR geweeg – dieselfde berekening as die **PREV-sones** van die [hemelkoepel](Sky-View-af). Vir elke kant van die pad wat minstens 15 % van die totaal bevat, is die wolk 'n **ellips**: middelpunt by die geweegde gemiddelde van die punte, halfasse 1,5 keer die vierkantswortels van die eiewaardes van hul verspreiding, hoofas langs die hoof-eievektor. Wanneer geen swerm bydra nie (slegs sporadiese meteore), is die wolke die twee klassieke **hot spots**, met strepies geteken. Die volledige vergelykings is in hoofstuk 10 van die berekeningshandleiding.

## Kontroles

| Kontrole | Betekenis |
|---|---|
| **Kaartradius** | 600–3500 km vanaf jou stasie. |
| **Spots om te wys** | Laaste 15 of 30 minute, laaste uur, laaste 3 uur, laaste 24 uur. |
| **Tabel** | Kontakte op die kaart, nuutste eerste, in die bandkleur; *Wolk* gee die aandeel van refleksies aan die hoofkant, of *sporadies*. |
| **Klik** | Op 'n pad of 'n tabelry: die kontak word uitgelig en die blokkie wys die lokator van die wolk se middelpunt, sy aandeel, grootte en as. |
