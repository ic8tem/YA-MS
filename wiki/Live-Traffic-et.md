[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · **Eesti** · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Liiklus otse

*Sakk: Otse ja reaalajas andmed › Liiklus otse.*

[![Liiklus otse](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Mida see näitab

Sinu jaamale tsentreeritud **asimuutne kaugustruu kaart** (kaugus keskpunktist = tegelik kaugus, nurk = asimuut) **kogu meteor scatteri liiklusega**, mille on kogunud [Andmete kogumine](Data-Collection-et). Iga side kohta joonistab programm:

- kahe jaama vahelise **trassi** oma sagedusala värvis: 28 MHz pruun, 50 MHz roheline, 70 MHz tsüaansinine, 144 MHz oranž, 222 MHz roosa, 432 MHz violetne;
- trassi otstes olevad kaks **jaama**;
- **voo tsoon**: kuhu koonduvad selle trassi ja selle aja kõige tõenäolisemad meteoorijäljed.

Spotid, mille üks jaam on **kaardist väljas**, jäetakse kõrvale. Vilguvad ainult sinu WSJT-X-i (UDP) dekodeeringud, milles korrespondent sulle vastab.

Näita, kes kuulab: riba värvi kolmnurgad märgivad jaamu, mis PSKReporteri järgi võtavad valitud ajaaknas vastu MSK144, FSK441, PSK2K või JTMS režiimis 28, 50, 70, 144 ja 432 MHz sagedusel. Klõps kolmnurgal näitab kutsungit, lokaatorit, režiime ja viimast spotti. Vahekaardi Andmete kogumine MQTT-voog peab olema ühendatud.

Ka PSKReporteri kaardi aktiivsed monitorid: tühjad kolmnurgad jaamadele, mis on pskreporter.info kaardil MSK144, FSK441, PSK2K või JTMS režiimis, kuid pole veel ühtegi spotti vastu võtnud (MQTT saadab ainult jaamu, mis midagi vastu võtavad). YA-MS pärib PSKReporteri päringuteenust kord 5 minuti jooksul kõigi režiimide kohta, nagu teenuse reeglid nõuavad; monitor jääb kaardile vähemalt 11 minutiks. Klõps kolmnurgal näitab kutsungit, lokaatorit, dekodeerimisprogrammi ja aega, mil monitor oli aktiivne. Vaikimisi sees.

FT8 üle 1100 km ilma paralleelsete trassideta: FT8-spot (PSKReporteri MQTT-st, klastritest või WSJT-X-ist UDP kaudu) üle 1100 km kaugusel olevate jaamade vahel, millel pole 3 minuti jooksul enne ja pärast paralleelseid trasse (sama sagedusala, keskpunkt 300 km piires, suund 15° piires, teine jaamapaar), joonistatakse helerohelisena, nagu ka selle rida paremal all tabelis (ilma vilkumiseta). Sporaadiline E ja troposfäär annavad palju lähedasi paralleelseid trasse; üksik spot võib olla meteoorijälg. Seepärast võtab YA-MS MQTT-st vastu ka 6 m, 4 m, 2 m, 1,25 m ja 70 cm FT8-spotid (mitte kunagi 28 MHz). Need spotid ei lähe MS-arhiivi. Vaikimisi sees. Lisakontrollid PSKReporteri MQTT-ga: spot ei ole üksik, kui vastuvõttev jaam kuuleb MQTT-s 3 minuti jooksul samal sagedusalal teisi jaamu üle 1100 km (avatud ala); klastrite ja RBN-i spotid kehtivad ainult siis, kui sama paar tuleb ka MQTT kaudu; RBN-i skimmerid (kutsungid «-#») ei kehti kunagi.

Sinu WSJT-X-i UDP kaudu tulnud dekodeeringud, milles korrespondent sulle vastab (sõnumi esimene kutsung on sinu oma), joonistatakse vilkuva katkendjoonena igas modulatsioonis ja igal kaugusel ning nende rida tabelis vilgub kollasel taustal. See on ainus juhtum, kus midagi vilgub.

Vahetus YA-MS-i kasutajate vahel: kui mõni teine YA-MS-i kasutaja dekodeerib UDP kaudu sinu jaamale adresseeritud sõnumi (MSK144, FSK441, PSK2K või JTMS režiimis või FT8-s üle 1100 km), saadab tema YA-MS selle sulle krüptitult kolme avaliku MQTT-maakleri kaudu (HiveMQ, Mosquitto, EMQX); näed seda püsiva violetse katkendjoonena ja reana UDP konsoolis. Ainult sina saad seda lugeda (ECDH P-256 võtmed, AES-256 ja HMAC-SHA256). FT8-spotte näidatakse ainult siis, kui neil pole 3 minuti jooksul paralleelseid trasse. Vaikimisi sees; yams_scambio=0 failis data/config.ini lülitab selle välja.

Kaardil kirjutatakse iga spoti mõlema jaama kutsung, üks kord jaama kohta. Projektsioon on valitav: asimuutne (keskel sinu jaam) või Mercator. Veeru voo tsoon kohtspikker selgitab selle tähendust.

Näidatakse kõigi sagedusalade spotte, ka nende, mida Andmekogumises ei ole valitud (neid ei salvestata). CW-spotte ja liiga lähedaste jaamade vahelisi spotte ei näidata, kui need Andmekogumises ära visatakse.

## Kuidas voo tsoon arvutatakse

Iga spoti jaoks ehitab programm kahe lokaatori vahelise trassi (sama geomeetria nagu sinu enda trassil, vt [Geomeetria ja sumbumine](Geometry-and-Path-Loss-et)) ja liidab spoti ajal E-kihi punkt-punktilt **iga aktiivse meteoorivoolu peegelpeegelduse panused**, kaalutuna selle ZHR-iga – sama arvutus nagu [taevavõlvi](Sky-View-et) **PREV alade** puhul. Igal trassi poolel, kus on vähemalt 15 % kogusummast, on voo tsoon **ellips**: keskpunkt punktide kaalutud keskmises, pooltelgedeks 1,5-kordsed ruutjuured nende hajuvuse omaväärtustest, suur telg piki peamist omavektorit. Kui ükski meteoorivool ei panusta (ainult sporaadilised meteoorid), on voo tsoon kaks klassikalist **hot spoti**, joonistatud katkendjoonega. Täielikud võrrandid on arvutusjuhendi 10. peatükis.

## Juhtnupud

| Juhtnupp | Tähendus |
|---|---|
| **Kaardi raadius** | 600–3500 km sinu jaamast. |
| **Näidatavad spotid** | Viimased 15 või 30 minutit, viimane tund, viimased 3 tundi, viimased 24 tundi. |
| **Tabel** | Kaardil olevad sided, uusimad eespool, sagedusala värvis; *% voog* annab peegelduste osa põhipoolel või *sporaadilised*. |
| **Klõps** | Trassil või tabeli real: side tõstetakse esile ja kast näitab voo tsoon keskpunkti lokaatorit, selle osa, suurust ja telge. |
